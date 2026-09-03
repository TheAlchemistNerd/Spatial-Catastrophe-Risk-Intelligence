param(
  [string]$Output = "output/pdf/Kenya_Multi_Hazard_Catastrophe_Intelligence_Series.pdf"
)

$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force -Path "tmp/pdfs/mermaid" | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Output) | Out-Null

$env:MERMAID_OUTPUT_DIR = "tmp/pdfs/mermaid"
$env:MERMAID_CONFIG_FILE = "mermaid-config.json"
$env:MERMAID_PUPPETEER_CONFIG = "puppeteer-config.json"
$env:MERMAID_CLI = (Get-Command "mmdc.cmd").Source.Replace("\", "/")
$env:MERMAID_NODE = (Get-Command "node.exe").Source
$mmdcRoot = Split-Path -Parent (Get-Command "mmdc.cmd").Source
$env:MERMAID_CLI_SCRIPT = Join-Path $mmdcRoot "node_modules\@mermaid-js\mermaid-cli\src\cli.js"

$parts = @(
  "01_KENYA_MULTI_HAZARD_INTELLIGENCE_THESIS.md",
  "02_CROWD_AI_AND_OBSERVATION_ARCHITECTURE.md",
  "03_SPATIOTEMPORAL_HAZARD_STATE_MODELLING.md",
  "04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md",
  "05_INSURANCE_INVESTMENT_AND_RESILIENCE_FINANCE.md",
  "06_GOVERNANCE_VALIDATION_AND_IMPLEMENTATION.md"
)

pandoc @parts `
  --from=markdown+tex_math_dollars+tex_math_single_backslash `
  --metadata-file=pdf-metadata.yaml `
  --lua-filter=series-structure.lua `
  --lua-filter=mermaid-filter.lua `
  --include-in-header=pdf-header.tex `
  --include-before-body=pdf-frontmatter.tex `
  --top-level-division=chapter `
  --pdf-engine=xelatex `
  --pdf-engine-opt=--enable-installer `
  --resource-path=".;tmp/pdfs/mermaid" `
  --standalone `
  --output=$Output

if ($LASTEXITCODE -ne 0) { throw "Pandoc PDF build failed with exit code $LASTEXITCODE" }
