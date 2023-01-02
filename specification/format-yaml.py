#!/usr/bin/env python3
#
# Convert temporary YAML (created by pandoc with a specialized "extract
# requirements" filter) to "standard" YAML that will become the source of
# truth for the requirements.
#
# Once the final version of this script has been run, it will never be run
# again.

import argparse
import glob
import logging
import os
import re
import sys
import textwrap

from typing import Any, Dict, List, Optional

import yaml

# XXX want just the name part; need some utilities / rules / conventions
prog_basename = os.path.basename(sys.argv[0])
(prog_root, _) = os.path.splitext(prog_basename)
logger = logging.getLogger(prog_root)


def aslist(value):
    return value if value is None or isinstance(value, list) else [value]


class Node:
    def __init__(self, parent: Optional['Node'] = None,
                 name: Optional[str] = None, key: Optional[str] = None):
        assert not parent or name not in parent._children

        self._parent = parent
        self._name = name
        self._key = key
        self._description = None
        self._after = None
        self._requirements = []
        self._children = {}

        if parent:
            parent._children[name] = self

    # the key only applies to the last name (leaf node)
    def traverse(self, names: List[str], key: Optional[str] = None) -> 'Node':
        node = self
        for i, name in enumerate(names):
            key_ = key if i == len(names) - 1 else None
            node = node.get(name, key=key_)
        return node

    # the key is only used if a new node needs to be created
    def get(self, name: str, key: Optional[str] = None) -> 'Node':
        if name in self._children:
            return self._children[name]
        else:
            return Node(self, name, key)

    # XXX can separate out the visitor pattern aspects later
    def output(self, *, level: int = 0) -> None:
        # if there's no key, attempt to derive it from the name
        key = self._key
        if key is None and self._name is not None:
            key = self._derive_key(self._name)
            if key is None:
                logger.warning('%s has no key; file not written' % self)

        # write the file (if there's a key); note that all markdown is
        # terminated by a blank line; this is taken into account when
        # deciding where to add more blank lines
        if key is not None:
            # XXX shouldn't hard-code the path!
            file = '../requirements/%s.yaml' % key

            # noinspection PyListCreation
            lines = []
            lines.append('---')
            lines.append('%s:' % key)
            lines.append('  name: |')
            for line in textwrap.wrap(self._clean_name(self._name)):
                lines.append('    %s' % line)
            lines.append('')
            if self._description:
                lines.append('  description: |')
                for line in self._description:
                    if not line:
                        lines.append('')
                    else:
                        lines.append('    %s' % line.rstrip())
            if self._children:
                lines.append('  categories:')
                for child in self._children.values():
                    key = child._key or self._derive_key(child._name)
                    if not key:
                        logger.warning('%s has no key' % child)
                    else:
                        lines.append('    - !include %s.yaml' % key)
                lines.append('')
            if self._requirements:
                ids = set()
                lines.append('  requirements:')
                for id_, req_lines in self._requirements:
                    # XXX rely on yamllint to detect duplicate IDs
                    lines.append('    %s: |' % self._extract_id(id_))
                    for req_line in req_lines:
                        # XXX a single valid number might have become an int
                        #     (probably utils.toyaml()'s fault)
                        for req_line_ in self._unescape(str(req_line)):
                            if not req_line_:
                                lines.append('')
                            else:
                                lines.append('      %s' % req_line_.rstrip())
                    ids.add(id_)
            if self._after:
                lines.append('  after: |')
                for line in self._after:
                    if not line:
                        lines.append('')
                    else:
                        lines.append('    %s' % line.rstrip())

            # ignore final empty line
            end = -1 if lines[-1].strip() == '' else None

            with open(file, 'w') as fd:
                fd.write('\n'.join(lines[:end]) + '\n')
                fd.close()

            logger.debug('wrote %3d lines to %s' % (len(lines), file))

        # descend to children
        for child in self._children.values():
            child.output(level=level + 1)

    def add_description(self, description: List[str]) -> None:
        self._description = description

    def add_after(self, after: List[str]) -> None:
        self._after = after

    def add_requirement(self, id_: str, lines: List[str]) -> None:
        self._requirements.append((id_, lines))

    @staticmethod
    def _derive_key(name: str) -> str:
        # remove anything after -, -- or – (en-dash)
        key = re.sub(r'\s+(-|--|–)\s+.*$', '', name.strip())

        # if the resulting key contains spaces, arbitrarily use the last
        # word (lower-case)
        # XXX this is intended for 'Residential Gateway Requirements' ->
        #     'requirements'
        if ' ' in key:
            key = key.split()[-1].lower()

        return key

    @staticmethod
    def _clean_name(name: str) -> str:
        # remove anything before -, -- or – (en-dash)
        return re.sub(r'^.*\s+(-|--|–)\s+', '', name.strip())

    @staticmethod
    def _extract_id(full_id: str) -> str:
        # 'A.B.n' -> 'n'
        id_ = full_id.split('.')[-1]
        # '0n' -> 'n'
        return '%d' % int(id_) if id_.isnumeric() else id_

    # this isn't perfect, but it will help to undo escaping within table rows
    @staticmethod
    def _unescape(line: str) -> List[str]:
        # if it starts with \*, remove the \
        if line.startswith('\\*'):
            line = line[1:]

        # if it starts with \| replace all \| with |
        elif line.startswith('\\|'):
            line = line.replace('\\|', '|')

        # if it starts with 'nnn. ' (three or more digits) or is 'n.' (any
        # number of digits), it's unlikely to be a list item, so insert an
        # empty span to protect it
        # XXX this isn't unescaping! is there a neater way of doing this?
        elif re.match(r'(\d{3,}\.\s)|(\d+\.$)', line):
            line = '[]{} ' + line

        # if it ends \\, remove \\ and add a blank line
        lines = [line]
        if line.endswith('\\'):
            line = line[:-1]
            lines = [line, '']

        return lines

    @property
    def parent(self) -> Optional['Node']:
        return self._parent

    @property
    def name(self) -> str:
        return self._name or ''

    @property
    def key(self) -> str:
        return self._key or ''

    @property
    def description(self) -> List[str]:
        return self._description or []

    @property
    def requirements(self) -> List[Any]:
        return self._requirements or []

    @property
    def after(self) -> List[str]:
        return self._after or []

    @property
    def children(self) -> Dict[str, 'Node']:
        return self._children or {}

    def __str__(self):
        return '%s (%d)' % (self._name, len(self._children))

    __repr__ = __str__


def main(argv=None):
    """Main program."""

    if argv is None:
        argv = sys.argv

    default_loglevel = 0

    formatter_class = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog=prog_basename, description=__doc__,
                                     fromfile_prefix_chars='@',
                                     formatter_class=formatter_class,
                                     add_help=False)

    parser.add_argument("file", type=str, nargs='+',
                        help="YAML file(s) to format (can include wildcards)")

    parser.add_argument("-l", "--loglevel", type=int, default=default_loglevel,
                        help="logging level; default: %r" % default_loglevel)

    args = parser.parse_args(argv[1:])

    loglevel_map = {0: logging.WARN, 1: logging.INFO, 2: logging.DEBUG}
    logging.basicConfig(level=loglevel_map[args.loglevel])

    # get files
    # XXX we assume that lexical sort is sufficient
    files = []
    for file in args.file:
        files += glob.glob(file)
    files = sorted(files)

    # root of node tree
    root = Node()

    # process the files, creating the node tree
    for file in files:
        # extract key from filename
        file_dir, file_id = os.path.split(file)
        file_id, file_ext = os.path.splitext(file_id)
        file_id = re.sub(r'^\d+-', '', file_id)
        file_id = file_id.replace('.yaml', '')

        # load YAML, which is a list of items
        # XXX will change this to scan a directory or expand a wildcard
        items = yaml.load(open(file), Loader=yaml.Loader)
        logger.debug('loaded %s' % file)

        # expect {'headers': list[str],
        #         'preamble': list[str],
        #         'requirements': list[
        #           {'id': str, 'requirements': list[str]}
        #         ]}
        # XXX single-element lists will be scalars owing to a vagary of the
        #     utils.toyaml() lua function
        assert items.keys() == {'headers', 'preamble', 'requirements'}
        headers = aslist(items['headers'])
        preamble = aslist(items['preamble'])

        # this creates nodes as needed and adds them to the tree
        logger.debug('headers %r' % headers)
        node = root.traverse(headers, file_id)

        # XXX this is hack: if the first line starts 'POST: ' then this is
        #     'after' text (from below the table) rather than a description
        logger.debug('preamble %r' % preamble)
        if preamble:
            if not preamble[0].startswith('POST: '):
                node.add_description(preamble)
            else:
                after = [preamble[0].replace('POST: ', '')] + preamble[1:]
                node.add_after(after)

        for requirement_dict in aslist(items['requirements']):
            assert requirement_dict.keys() == {'id', 'requirement'}
            id_ = requirement_dict['id']
            lines = aslist(requirement_dict['requirement'])
            logger.debug('  id %r requirement %r' % (id_, lines))
            node.add_requirement(id_, lines)

    # traverse the node tree generating the output files
    root.output()


if __name__ == "__main__":
    sys.exit(main())
