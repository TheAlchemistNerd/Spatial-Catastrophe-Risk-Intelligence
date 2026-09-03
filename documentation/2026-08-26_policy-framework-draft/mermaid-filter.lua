-- Pandoc Lua filter for rendering fenced Mermaid blocks to high-resolution PNG.
-- Usage: pandoc ... --lua-filter=mermaid-filter.lua

local diagram_counter = 0
local working_dir = pandoc.system.get_working_directory()
local output_dir = os.getenv("MERMAID_OUTPUT_DIR") or "tmp/pdfs/mermaid"
local config_file = os.getenv("MERMAID_CONFIG_FILE") or "mermaid-config.json"
local puppeteer_config = os.getenv("MERMAID_PUPPETEER_CONFIG") or "puppeteer-config.json"
local cli = os.getenv("MERMAID_CLI") or "mmdc.cmd"
local node = os.getenv("MERMAID_NODE")
local cli_script = os.getenv("MERMAID_CLI_SCRIPT")
local force_render = os.getenv("MERMAID_FORCE_RENDER") == "1"

if not pandoc.path.is_absolute(output_dir) then
  output_dir = pandoc.path.join({working_dir, output_dir})
end
if not pandoc.path.is_absolute(config_file) then
  config_file = pandoc.path.join({working_dir, config_file})
end
if not pandoc.path.is_absolute(puppeteer_config) then
  puppeteer_config = pandoc.path.join({working_dir, puppeteer_config})
end

local function contains_class(classes, wanted)
  for _, class in ipairs(classes) do
    if class == wanted then return true end
  end
  return false
end

local function safe_identifier(value)
  value = value or ""
  value = value:gsub("[^%w_-]", "-")
  value = value:gsub("%-+", "-")
  value = value:gsub("^%-", ""):gsub("%-$", "")
  return value
end

local function ensure_directory(path)
  local ok = pcall(function() pandoc.system.make_directory(path, true) end)
  if not ok then
    pandoc.pipe("cmd.exe", {"/d", "/s", "/c", "if not exist " .. path .. " mkdir " .. path}, "")
  end
end

local function write_file(path, contents)
  local handle, message = io.open(path, "wb")
  if not handle then error("Cannot write Mermaid source " .. path .. ": " .. tostring(message)) end
  handle:write(contents)
  handle:close()
end

local function render_mermaid(source, identifier)
  diagram_counter = diagram_counter + 1
  local stem = safe_identifier(identifier)
  if stem == "" then stem = string.format("mermaid-%03d", diagram_counter) end
  local input_path = output_dir .. "/" .. stem .. ".mmd"
  local output_path = output_dir .. "/" .. stem .. ".png"

  ensure_directory(output_dir)
  write_file(input_path, source)

  if not force_render then
    local cached = io.open(output_path, "rb")
    if cached then
      local size = cached:seek("end") or 0
      cached:close()
      if size > 0 then return output_path end
    end
  end

  local args = {
    "-i", input_path,
    "-o", output_path,
    "-c", config_file,
    "-p", puppeteer_config,
    "-t", "neutral",
    "-b", "transparent",
    "-w", "2200",
    "-s", "1.5"
  }

  local ok, message = pcall(function()
    if node and cli_script then
      local node_args = {cli_script}
      for _, value in ipairs(args) do table.insert(node_args, value) end
      pandoc.pipe(node, node_args, "")
    else
      pandoc.pipe(cli, args, "")
    end
  end)
  if not ok then
    error("Mermaid rendering failed for " .. stem .. ": " .. tostring(message))
  end
  local rendered = io.open(output_path, "rb")
  if rendered then rendered:close() end
  if not rendered then
    error("Mermaid renderer returned without producing " .. output_path)
  end
  return output_path
end

function CodeBlock(block)
  if not contains_class(block.classes, "mermaid") then return nil end
  local image_path = render_mermaid(block.text, block.identifier)
  local alt = block.attributes["alt"] or block.attributes["caption"] or block.identifier or "Mermaid diagram"
  local width = block.attributes["width"] or "96%"
  return pandoc.Para({
    pandoc.Image({pandoc.Str(alt)}, image_path, "", pandoc.Attr("", {}, {{"width", width}}))
  })
end

-- Keep the PDF toolchain robust even when source prose contains typographic dashes.
function Str(element)
  if FORMAT:match("latex") and element.text:match("^https?://") then
    local target = element.text:gsub("([{}])", "\\%1")
    return pandoc.RawInline("latex", "\\url{" .. target .. "}")
  end
  element.text = element.text:gsub("‑", "-"):gsub("–", "--"):gsub("—", "---")
  return element
end

-- Pandoc emits bare web addresses as hyperlinks.  In LaTeX, render links whose
-- visible label is the address itself through \url so xurl can break them safely.
function Link(element)
  if not FORMAT:match("latex") then return nil end
  if not element.target:match("^https?://") then return nil end
  if pandoc.utils.stringify(element.content) ~= element.target then return nil end
  local target = element.target:gsub("([{}])", "\\%1")
  return pandoc.RawInline("latex", "\\url{" .. target .. "}")
end
