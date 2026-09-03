-- Convert each manuscript H1 into a book part and build compact, numbered
-- section spines without changing the Markdown manuscript text.

local function latex_escape(value)
  value = value:gsub("\\", "\\textbackslash{}")
  value = value:gsub("([%%#$&_{}])", "\\%1")
  value = value:gsub("~", "\\textasciitilde{}")
  value = value:gsub("%^", "\\textasciicircum{}")
  return value
end

local first_part = true
local current_part = 0
local section_counter = 0
local subsection_counter = 0
local in_appendices = false

local function toc_entry(level, label, title)
  local number = ""
  if label and label ~= "" then
    number = "\\protect\\numberline{" .. latex_escape(label) .. "}"
  end
  return "\\addcontentsline{toc}{" .. level .. "}{" .. number .. latex_escape(title) .. "}"
end

function Header(header)
  local title = pandoc.utils.stringify(header.content)

  if header.level == 1 then
    local explicit_number, clean_title = title:match("^Part%s+(%d+):%s*(.+)$")
    clean_title = clean_title or title

    if clean_title:lower() == "appendices" then
      in_appendices = true
      return pandoc.RawBlock("latex", table.concat({
        "\\appendix",
        "\\cleardoublepage",
        "\\phantomsection",
        "\\part*{Appendices}",
        "\\markboth{Appendices}{Appendices}"
      }, "\n"))
    end

    current_part = explicit_number and tonumber(explicit_number) or (current_part + 1)
    section_counter = 0
    subsection_counter = 0
    local command = "\\part{" .. latex_escape(clean_title) .. "}\n\\markboth{Part " .. current_part .. "}{Part " .. current_part .. "}"
    if first_part then
      command = "\\mainmatter\n" .. command
      first_part = false
    end
    return pandoc.RawBlock("latex", command)
  end

  if header.level == 2 then
    subsection_counter = 0

    if in_appendices then
      return pandoc.RawBlock("latex", "\\section*{" .. latex_escape(title) .. "}\n" .. toc_entry("section", "", title))
    end

    if title == "References" then
      return pandoc.RawBlock("latex", "\\section*{References}\n" .. toc_entry("section", "", "References"))
    end

    section_counter = section_counter + 1
    local label = tostring(section_counter) .. "."
    return pandoc.RawBlock("latex", "\\section*{" .. latex_escape(label .. " " .. title) .. "}\n" .. toc_entry("section", label, title))
  end

  if header.level == 3 then
    if in_appendices then
      return pandoc.RawBlock("latex", "\\subsection*{" .. latex_escape(title) .. "}\n" .. toc_entry("subsection", "", title))
    end

    subsection_counter = subsection_counter + 1
    local label = tostring(section_counter) .. "." .. tostring(subsection_counter) .. "."
    return pandoc.RawBlock("latex", "\\subsection*{" .. latex_escape(label .. " " .. title) .. "}\n" .. toc_entry("subsection", label, title))
  end

  return header
end
