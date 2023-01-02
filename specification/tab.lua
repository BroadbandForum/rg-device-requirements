-- pandoc utilities
local stringify = pandoc.utils.stringify

-- BBF utilities
local utils = require 'utils'
if false then utils.logLevel = 2 end

-- current headers; indexed by level (1, 2, 3, ...)
local currents = pandoc.List()

-- current header
local current = nil

-- whether requirements table seen since header
local seen = nil

-- paras since header
local paras = pandoc.List()

-- file counter (is incremented before use)
local count = 0

function Header(header)
    local level = header.level
    local content = header.content
    currents[level] = content
    for i, _ in pairs(currents) do
        if i > level then
            currents[i] = nil
        end
    end
    current = content
    if seen then
        utils.warning('trailing paras ignored:', stringify(paras))
    end
    seen = nil
    paras = pandoc.List()
end

function Para(para)
    if type(seen) ~= 'nil' then
        seen = true
    end
    paras:extend{para}
end

function Table(tab)
    local head = tab.head

    local head_rows = head.rows
    if #head_rows == 0 then
        return
    end

    local head_row1 = head_rows[1]
    local head_cells = head_row1.cells

    local head_values = head_cells:map(function(cell)
                                           return stringify(cell.contents) end)
    utils.debug('head_values', head_values)

    -- requirements tables should be (ID, Requirement) but there are various
    -- variations, and some indicate 'Requirements' (plural), so be lenient
    if (#head_values >= 2 and
            head_values[1] == 'ID' and
        head_values[2]:match('^Requirement')) then
        -- (ID, Requirement)
    elseif (#head_values >= 2 and
            head_values[1] == 'Section' and
        head_values[2]:match('^Requirement')) then
        -- (Section, Requirement)
    elseif (#head_values >= 3 and
                head_values[1] == 'ID' and
                head_values[2] == 'ID' and
            head_values[3]:match('^Requirement')) then
        -- (ID, ID, Requirement)
    elseif (#head_values >= 3 and
                head_values[1] == '' and
                head_values[2] == 'ID' and
            head_values[3]:match('^Requirement')) then
        -- (, ID, Requirement)
    elseif (#head_cells >= 3 and
                head_values[1] == 'Section' and
                head_values[2] == 'Section' and
            head_values[3]:match('^Requirement')) then
        -- (Section, Section, Requirement)
    elseif (#head_cells >= 3 and
                head_values[1] == 'Section' and
                head_values[2] == 'Item' and
            head_values[3]:match('^Requirement')) then
        -- (Section, Item, Requirement)
    else
        -- not a requirements table
        return
    end

    -- report current header
    utils.info(stringify(current))

    -- treat tables as a list of cells to ease handling the different cases
    local values = pandoc.List()
    local prev_value = nil
    for i, body in ipairs(tab.bodies) do
        for j, row in ipairs(body.body) do
            for k, cell in ipairs(row.cells) do
                local value = cell.contents
                if not prev_value or value ~= prev_value then
                    utils.debug(i, j, k, value)
                    values:extend{value}
                    prev_value = value
                end
            end
        end
    end

    local id = ''
    local id_first = nil
    local state = 'id'
    local reqs = pandoc.List()
    for _, value in ipairs(values) do
        -- combine (Section, Item) into ID
        utils.debug('state', state, 'id', id, 'value', value)
        if state == 'id' then
            value = stringify(value)
            if #id == 0 then
                id = value
            else
                id = id .. '.' .. (value:match('^%d+$') and
                                       string.format('%02d', value) or value)
            end
            if id:match('%.%d+%l?$') then
                if not id_first then
                    id_first = id
                end
                state = 'requirement'
            end
        else
            local markdown  = pandoc.write(pandoc.Pandoc(value), 'markdown')
            local lines = pandoc.List()
            for line in markdown:gmatch("[^\r\n]*") do
                lines:extend{line}
            end
            utils.debug('ID', id, 'Requirement', lines)
            if id:match('%s') then
                utils.warning('invalid ID', id)
            end
            reqs:extend{{id=id, requirement=lines}}
            id = ''
            state = 'id'
        end
    end
    if state == 'id' and #id > 0 then
        utils.warning('unterminated ID', id)
    end

    -- derive filename (this is a temporary file)
    -- XXX use the first id rather than the header, because not all the headers
    --     are correct
    count = count + 1
    local name = ''
    name = string.format('%03d', count) .. '-'
    name = name .. id_first or stringify(current)
    name = name:match('^(%g+)'):gsub('%.[^.]+$', '')
    name = 'temp/' .. name .. '.yaml'
    local file = io.open(name, 'w+')

    -- output as YAML
    -- XXX paras after the table haven't yet been seen and so can't be
    --     included, but they will be reported and should be manually moved
    --     with a 'POST:' prefix to allow subsequent processing
    local headers = currents:map(function(header) return stringify(header) end)
    local preamble = pandoc.List()
    if #paras > 0 then
        local markdown = pandoc.write(pandoc.Pandoc(paras), 'markdown')
        for line in markdown:gmatch("[^\r\n]*") do
            preamble:extend{line}
        end
    end

    local lines = utils.toyaml({headers=headers, preamble=preamble,
                                requirements=reqs})
    for _, line in ipairs(lines) do
        file:write(line .. '\n')
    end
    file:close()
    utils.info('wrote', #lines, 'lines to', name)

    -- this indicates that a requirements table has been seen but that no
    -- trailing paras have (yet) been seen
    seen = false

    -- XXX this will need to be edited but will do for now
    return pandoc.Para(pandoc.Str('!include ' .. name))
end
