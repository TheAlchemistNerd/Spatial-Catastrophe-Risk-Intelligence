-- Map each manuscript H1 to a LaTeX Part while preserving H2+ as flowing sections.
-- This avoids forcing a chapter break for every internal manuscript section.

local function latex_escape(value)
  value = value:gsub("\\", "\\textbackslash{}")
  value = value:gsub("([%%#$&_{}])", "\\%1")
  value = value:gsub("~", "\\textasciitilde{}")
  value = value:gsub("%^", "\\textasciicircum{}")
  return value
end

local first_part = true

function Header(header)
  if header.level ~= 1 then return nil end
  local title = latex_escape(pandoc.utils.stringify(header.content))
  local command = "\\part{" .. title .. "}"
  if first_part then
    command = command .. "\n\\pagenumbering{arabic}"
    first_part = false
  end
  return pandoc.RawBlock("latex", command)
end
