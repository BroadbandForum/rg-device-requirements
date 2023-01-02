#!/usr/bin/env python3
#
# Parse "standard" requirements YAML into a tree structure from which various
# products can be generated, e.g., requirements markdown.
#
# This script will be run as part of the build process.

# XXX could check for gaps in requirement IDs

import argparse
import glob
import logging
import os.path
import re
import sys

from typing import Any, Callable, Dict, List, Optional, Set, Union

# pip3 install PyYAML
# noinspection PyPackageRequirements
import yaml

# XXX want just the name part; need some utilities / rules / conventions
prog_basename = os.path.basename(__file__)
(prog_root, _) = os.path.splitext(prog_basename)
logger = logging.getLogger(prog_root)

# all active and loaded YAML files
active = {}
loaded = {}


# derived from https://stackoverflow.com/questions/528281
class IncludeFullLoader(yaml.FullLoader):
    def include(self, node):
        file = self.construct_scalar(node)

        # try expanding variables; if the resulting path exists, just use it
        path = os.path.expandvars(file)

        # otherwise, and if it's not an absolute path, look in the same
        # directory as the 'including' file
        if not os.path.exists(path) and not os.path.isabs(path):
            head, tail = os.path.split(node.start_mark.name)
            path = os.path.join(head, file)

        # give up if not found
        if not os.path.exists(path):
            raise ReqsException('%s file not found' % file)

        # check for recursion
        if file in active:
            raise ReqsException("can't load %s from %s; already loaded "
                                "from %s" % (file, node.start_mark.name,
                                             active[file]))

        # load the included file
        active[path] = node.start_mark.name
        obj = yaml.load(open(path), Loader=IncludeFullLoader)
        del active[path]
        logger.debug('loaded %s' % path)
        loaded[path] = node.start_mark.name

        # expect file to define a single-element dict; if so, the key should
        # match the filename
        if isinstance(obj, dict) and len(obj.keys()) == 1:
            key = next(iter(obj.keys()))
            name, ext = os.path.splitext(file)
            if key != name:
                logger.warning("key %s doesn't match filename %s" % (key,
                                                                     file))
        return obj


# XXX should also use constructors for building the trees as we go; then we
#     could provide more helpful error messages, e.g., line numbers
IncludeFullLoader.add_constructor('!include', IncludeFullLoader.include)


class ReqsException(Exception):
    pass


# XXX could/should make this a Base class method?
def fix_dict(dct: Union[None, Dict[str, Any]], *, fix_keys: bool = True) \
        -> Dict[str, Any]:
    """Fix dict keys (replace hyphens with underscores)."""
    if dct is None:
        dct = {}

    # argument must be a dict
    if not isinstance(dct, dict):
        raise ReqsException('invalid %s value should be a dict' %
                            type(dct).__name__)

    # otherwise fix keys and/or values
    def fix_key(k):
        return k.replace('-', '_') if fix_keys and isinstance(k, str) else k

    return {fix_key(key): value for key, value in dct.items()}


class Node:
    @classmethod
    def create(cls, parent: Optional['Node'], dct: Optional[Dict] = None) -> \
            Optional['Node']:
        try:
            assert isinstance(dct, dict) and len(dct) == 1, \
                'argument must be a single-item dict, not %r' % dct
            for key, value in dct.items():
                return Node(parent, key, **fix_dict(value))
        except (AssertionError, ReqsException) as e:
            key = next(iter(dct.keys())) if isinstance(dct, dict) else None
            logger.error('%s: %s' % (key or 'UNKNOWN', e))

    def __init__(self, parent: Optional['Node'], key: str, name: str, *,
                 description: Optional[str] = None,
                 requirements: Optional[Dict[str, str]] = None,
                 categories: Optional[Union[
                     Dict[str, Dict[str, Any]],
                     List[Dict[str, Any]]
                 ]] = None,
                 categories_dict: Optional[Dict[str, Dict[str, Any]]] = None,
                 categories_list: Optional[List[Dict[str, Any]]] = None,
                 after: Optional[str] = None):
        self._parent = parent
        self._key = key

        # id is the last component of the key (or the key if there are no dots)
        parent_path, self._id = key.rsplit('.', 1) if '.' in key else ('', key)
        # if the key has multiple components and there's a parent, the leading
        # part of the key must be the parent path
        # XXX this was an assertion but (for now) it's just a warning
        if parent and parent_path and parent_path != parent.path:
            logger.warning('%s: unexpected parent %s (need to define '
                           'category %s)' % (key, parent.path, parent_path))

        self._name = name
        self._description = description
        self._requirements = requirements

        self._categories = None
        if categories or categories_dict or categories_list:
            self._categories = []
            if isinstance(categories, dict) or categories_dict:
                assert not (isinstance(categories, dict) and categories_dict),\
                    "can't specify both dict-valued 'categories' and " \
                    "'categories-dict'"
                categories_dict = categories_dict or categories
                for id_, cat in categories_dict.items():
                    if cat:
                        # allow inline categories by simulating the single-item
                        # dicts that are used when using multiple files
                        dct = cat if isinstance(cat, dict) and id_ in cat \
                            else {id_: cat}
                        child = Node.create(self, dct)
                        assert child.id == id_, "category %s doesn't match " \
                                                "key %s" % (child.id, id_)
                        self._categories.append(child)
            if isinstance(categories, list) or categories_list:
                assert not (isinstance(categories, list) and categories_list),\
                    "can't specify both list-valued 'categories' and " \
                    "'categories-list'"
                categories_list = categories_list or categories
                for cat in categories_list:
                    self._categories.append(Node.create(self, cat))

        self._after = after

    def visit(self, func: Callable, *, level: Optional[int] = 0, **kwargs) \
            -> None:
        func(self, level=level, **kwargs)
        for category in self.categories:
            if category:
                category.visit(func, level=level + 1, **kwargs)

    @property
    def parent(self) -> Optional['Node']:
        return self._parent

    @property
    def key(self) -> str:
        return self._key

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def path(self) -> str:
        # this is a bit tricky: the node key might or not be a full path; if it
        # is, then use it, but otherwise derive the path from ancestor ids
        if '.' in self._key:
            return self._key

        # the derived path doesn't include the root node id, which is typically
        # 'requirements'
        # XXX this is error-prone, and can fail unexpectedly if a different
        #     node is the root node (this is only likely when testing)
        else:
            return ('%s.' % self.parent.path if
                    self.parent and self.parent.parent else '') + self._id

    @property
    def description(self) -> str:
        return self._description or ''

    @property
    def requirements(self) -> Dict[str, str]:
        return self._requirements or {}

    @property
    def categories(self) -> List['Node']:
        return self._categories or []

    @property
    def after(self) -> str:
        return self._after or ''

    def __str__(self):
        return self.path

    __repr__ = __str__


# XXX this isn't just node paths, it's also requirement paths
def get_paths(node: Node, *, paths: Set[str], **_kwargs) -> None:
    if node.path in paths:
        logger.error('duplicate node path %s' % node.path)
    else:
        paths.add(node.path)

    for id_ in node.requirements:
        path = '%s.%s' % (node.path, id_)
        if path in paths:
            logger.error('duplicate requirement path %s' % path)
        else:
            paths.add(path)


def get_markdown(node: Node, *, level: Optional[int] = 0,
                 paths: Set[str], lines: List[str],
                 state: Dict[str, Any], **_kwargs) -> None:
    header = '%s ' % ((level + 1) * '#')
    prefix = node.path if level > 0 else ''
    suffix = node.name.strip()
    midfix = ' -- ' if prefix and suffix else ''
    attr0 = '#req:%s' % node.path.lower()
    attr1 = ' .new-file' if level < 2 else ''
    attr2 = ' .new-page' if level < 2 and not state.get('last_was_empty') \
        else ''
    attrs = ' {%s%s%s}' % (attr0, attr1, attr2)

    # nodes with requirements are currently regarded as non-empty
    # XXX could also regard nodes with 'long' descriptions as non-empty
    state['last_was_empty'] = True

    lines.append('%s%s%s%s%s' % (header, prefix, midfix, suffix, attrs))
    lines.append('')
    if node.description:
        for line in node.description.splitlines():
            lines.append(line)
        lines.append('')

    if node.requirements:
        def add_anchor(full_id_):
            return '[%s]{#req:}' % full_id_

        def add_links(line_):
            def repl(match_):
                text_ = match_.group(0)
                # A.B.01a -> A.B.1a
                text__ = text_.replace('.0', '.')
                if text_ in paths:
                    return '[%s](#req:)' % text_
                elif text__ in paths:
                    logger.warning('should use %s rather than %s to '
                                   'reference requirements' % (text__, text_))
                    return '[%s](#req:%s)' % (text_, text__.lower())
                else:
                    return text_

            return re.sub(r'\b[\w-]+\.[\w.-]+\b', repl, line_)

        lines.append('::: {.list-table .requirements-table widths=20,80} :::')
        lines.append('')
        lines.append('* - ID')
        lines.append('  - Requirement')
        lines.append('')
        for id_, requirement in node.requirements.items():
            full_id = '%s.%s' % (node.path, id_)
            lines.append('* - %s' % add_anchor(full_id))
            prefix = '-'
            for line in requirement.splitlines():
                lines.append('  %s %s' % (prefix, add_links(line)))
                prefix = ' '
            lines.append('')
        lines.append(':::')
        lines.append('')

        state['last_was_empty'] = False

    if node.after:
        for line in node.after.splitlines():
            lines.append(line)
        lines.append('')


def main(argv=None):
    """Main program."""

    if argv is None:
        argv = sys.argv

    default_output = sys.stdout
    default_loglevel = 0

    formatter_class = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog=prog_basename, description=__doc__,
                                     fromfile_prefix_chars='@',
                                     formatter_class=formatter_class,
                                     add_help=False)

    parser.add_argument('file', type=argparse.FileType('r'),
                        help='YAML file to parse')

    parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                        default=default_output,
                        help='markdown file to generate; default: stdout')

    parser.add_argument('-l', '--loglevel', type=int, default=default_loglevel,
                        help='logging level; default: %r' % default_loglevel)

    args = parser.parse_args(argv[1:])

    loglevel_map = {0: logging.WARN, 1: logging.INFO, 2: logging.DEBUG}
    logging.basicConfig(level=loglevel_map[args.loglevel])

    # load YAML
    try:
        obj = yaml.load(args.file, Loader=IncludeFullLoader)
    except ReqsException as e:
        logger.error('failed to load %s: %s' % (args.file.name, e))
        obj = None
    loaded[args.file.name] = ''
    logger.debug('loaded %s' % args.file.name)

    # XXX sanity check that all YAML files have been loaded (this checks that
    #     they're all referenced
    # XXX this shouldn't be done unconditionally
    dirname = os.path.dirname(args.file.name)
    all_files = set(glob.glob(os.path.join(dirname, '*.yaml')))
    loaded_keys = set(loaded.keys())
    if all_files - loaded_keys:
        logger.warning("these files weren't loaded: %s" % (all_files -
                                                           loaded_keys))

    # create node tree
    root = Node.create(None, obj)

    # collect all node and requirement paths
    paths = set()
    if root:
        root.visit(get_paths, paths=paths)

    # output markdown
    lines = []
    state = {}
    if root:
        root.visit(get_markdown, paths=paths, lines=lines, state=state)

    if lines:
        end = -1 if lines[-1].strip() == '' else None
        args.output.write('\n'.join(lines[:end]) + '\n')


if __name__ == '__main__':
    sys.exit(main())
