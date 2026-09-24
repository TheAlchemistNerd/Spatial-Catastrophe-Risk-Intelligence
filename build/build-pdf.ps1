param(
  [string]$Output = "output/pdf/Spatial_Catastrophe_Risk_Intelligence_White_Paper.pdf",
  [switch]$ReuseMermaid
)

$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
$pandocDir = Join-Path $PSScriptRoot "pandoc"
$manuscriptDir = Join-Path $projectRoot "manuscripts"
$mermaidDir = Join-Path $projectRoot "tmp\pdfs\mermaid"
$outputPath = if ([System.IO.Path]::IsPathRooted($Output)) {
  $Output
} else {
  Join-Path $projectRoot $Output
}

New-Item -ItemType Directory -Force -Path $mermaidDir | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $outputPath) | Out-Null

$env:MERMAID_OUTPUT_DIR = $mermaidDir
$env:MERMAID_CONFIG_FILE = Join-Path $pandocDir "mermaid-config.json"
$env:MERMAID_PUPPETEER_CONFIG = Join-Path $pandocDir "puppeteer-config.json"
$env:MERMAID_CLI = (Get-Command "mmdc.cmd").Source.Replace("\", "/")
$env:MERMAID_NODE = (Get-Command "node.exe").Source
$env:MERMAID_FORCE_RENDER = if ($ReuseMermaid) { "0" } else { "1" }
$mmdcRoot = Split-Path -Parent (Get-Command "mmdc.cmd").Source
$env:MERMAID_CLI_SCRIPT = Join-Path $mmdcRoot "node_modules\@mermaid-js\mermaid-cli\src\cli.js"

$parts = @(
  "01_KENYA_MULTI_HAZARD_INTELLIGENCE_THESIS.md",
  "02_CROWD_AI_AND_OBSERVATION_ARCHITECTURE.md",
  "03_SPATIOTEMPORAL_HAZARD_STATE_MODELLING.md",
  "04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md",
  "05_INSURANCE_INVESTMENT_AND_RESILIENCE_FINANCE.md",
  "06_GOVERNANCE_VALIDATION_AND_IMPLEMENTATION.md",
  "07_APPENDICES.md"
) | ForEach-Object {
  Join-Path $manuscriptDir $_
}

$metadataFile = Join-Path $pandocDir "pdf-metadata.yaml"
$structureFilter = Join-Path $pandocDir "series-structure.lua"
$mermaidFilter = Join-Path $pandocDir "mermaid-filter.lua"
$headerFile = Join-Path $pandocDir "pdf-header.tex"
$frontmatterFile = Join-Path $pandocDir "pdf-frontmatter.tex"
$pdfInfoScript = Join-Path $PSScriptRoot "set-pdf-info.py"

Push-Location $projectRoot
try {
  pandoc @parts `
    --from=markdown+tex_math_dollars+tex_math_single_backslash `
    "--metadata-file=$metadataFile" `
    "--lua-filter=$structureFilter" `
    "--lua-filter=$mermaidFilter" `
    "--include-in-header=$headerFile" `
    "--include-before-body=$frontmatterFile" `
    --top-level-division=chapter `
    --pdf-engine=xelatex `
    --pdf-engine-opt=--enable-installer `
    "--resource-path=$projectRoot;$mermaidDir" `
    --standalone `
    "--output=$outputPath"

  if ($LASTEXITCODE -ne 0) { throw "Pandoc PDF build failed with exit code $LASTEXITCODE" }

  python $pdfInfoScript $outputPath
  if ($LASTEXITCODE -ne 0) { throw "PDF metadata finalisation failed with exit code $LASTEXITCODE" }
} finally {
  Pop-Location
}
