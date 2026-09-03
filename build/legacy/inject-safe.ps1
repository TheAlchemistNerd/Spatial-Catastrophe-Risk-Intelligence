function Append-To-Section($file, $header, $ref, $mermaid) {
    $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
    # Find the header
    $idx = $content.IndexOf($header)
    if ($idx -eq -1) { Write-Host "Header not found: $header"; return }
    
    # Find the next header
    $nextIdx = $content.IndexOf("## ", $idx + $header.Length)
    if ($nextIdx -eq -1) { $nextIdx = $content.Length }
    
    # We want to insert right before nextIdx
    $part1 = $content.Substring(0, $nextIdx).TrimEnd()
    $part2 = $content.Substring($nextIdx)
    
    $insert = "`r`n`r`n" + $ref + "`r`n`r`n```mermaid`r`n" + $mermaid + "`r`n````r`n`r`n"
    $newContent = $part1 + $insert + $part2
    
    [System.IO.File]::WriteAllText($file, $newContent, [System.Text.Encoding]::UTF8)
}

# --- Part 1 ---
$f = "01_KENYA_MULTI_HAZARD_INTELLIGENCE_THESIS.md"
Append-To-Section $f "## Hydrological and Climate Vulnerabilities" "As illustrated in the process flow below, this architecture fundamentally shifts catastrophe response from a lagging, reactive indemnification process into a proactive, continuous intelligence lifecycle." "graph LR`n  subgraph Reactive`n    E1[Event] --> L1[Lagging Detection] --> C1[Triage] --> P1[Delayed Payout]`n  end`n  subgraph Continuous Intelligence`n    E2[Event] --> D2[Observation Mesh] --> H2[Dynamic Inference] --> U2[Instant Assessment]`n  end"
Append-To-Section $f "## Telemetry and Actuarial Observation Gaps" "The diagram below demonstrates how disparate observation methodologies are spatially and temporally fused to construct a unified hazard map." "flowchart TD`n  S[Satellites] --> F(Spatial Registration)`n  C[Crowd] --> F`n  V[Sensors] --> F`n  F --> B{Bayesian Fusion Engine} --> H[Dynamic Hazard Polygon]"
Append-To-Section $f "## Socio-Economic and Agricultural Exposure" "The sequence below illustrates the cascading economic degradation occurring when an acute trigger evolves into a systemic livelihood crisis." "graph TD`n  A[Precipitation Deficit] --> B[Soil Moisture Depletion] --> C{Agricultural Viability}`n  C -->|Minor| D[Yield Reduction]`n  C -->|Severe| E[Total Crop Failure] --> F[Distress Livestock Sales] --> G[Market Collapse]"

# --- Part 2 ---
$f = "02_CROWD_AI_AND_OBSERVATION_ARCHITECTURE.md"
Append-To-Section $f "## Distributed Intelligence and Sensor Networks" "The network topology mapped below showcases the hierarchical ingestion of data from the physical environment into the centralized processing mesh." "graph TD`n  S[Satellites] & D[Drones] & C[Smartphones] --> N[Regional Nodes] --> Core[Processing Matrix] --> Act[Actuarial Engine]"
Append-To-Section $f "## Machine Perception and Crowd Integration" "The flowchart below details how raw optical feeds are algorithmically transformed into actionable, geometric damage representations." "flowchart LR`n  I[Optical Image] --> V[Vision Transformer] --> Y[YOLOv8 Detection] --> B[Box Regression]`n  B --> C{Confidence > 0.85?}`n  C -->|Yes| P[Semantic Polygon]`n  C -->|No| R[Request Crowd Corroboration]"
Append-To-Section $f "## Bayesian Evidence Aggregation" "This directed acyclic graph visualizes the rigorous filtering mechanism isolating only the statistically significant ground-truth signal." "graph TD`n  Raw[Unfiltered Reports] --> F1[Spatial Density] & F2[Temporal Sequencing] --> iHMM{Hidden Markov Model}`n  iHMM -->|Noise| Drop[Discard]`n  iHMM -->|Consensus| Post[Posterior Credible Interval] --> Valid[Validated Input]"

# --- Part 3 ---
$f = "03_SPATIOTEMPORAL_HAZARD_STATE_MODELLING.md"
Append-To-Section $f "## Dynamic Spatial Polygon Processing" "The state diagram below illustrates the autoregressive spatial-temporal framework used to process expanding hazard boundaries." "stateDiagram-v2`n  [*] --> BaseState`n  BaseState --> ExpandingPolygon : Hydrological Anomaly`n  ExpandingPolygon --> StablePolygon : Remediation`n  StablePolygon --> [*]"
Append-To-Section $f "## Mobile Perils and Isolated Hazards" "The flowchart below maps the multi-dimensional kinetic modeling approach used for tracking biological catastrophes like locust swarms." "flowchart TD`n  W[Wind Vectors] & V[Vegetation Density] & L[Lifecycle Stage] --> M[Movement Algorithm]`n  M --> T[Directional Velocity Vector] --> P[Future Hazard Polygon]"
Append-To-Section $f "## Actuarial Digital Twins and Intensity Metrics" "This architecture diagram shows how physical hazard manifestations are computationally mapped against insured exposures." "graph LR`n  H[Hazard Polygon] --> I[Intersection Engine]`n  E[Exposure Database] --> I`n  I --> D[Damage Ratio Curve] --> L[Expected Loss Computation]"

# --- Part 4 ---
$f = "04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md"
Append-To-Section $f "## Financial Severity and Negative Binomial Overdispersion" "The process flow below demonstrates how overdispersed event frequencies are parameterized within the continuous loss engine." "graph TD`n  E[Earned Exposure] --> M[Mean Estimation]`n  O[Overdispersion Parameter] --> N[Negative Binomial Frequency]`n  M --> N --> S[Stochastic Event Generation]"
Append-To-Section $f "## Copulas and Tail Risk Quantification" "The structural mapping below visualizes how asymmetric copulas synchronize disparate marginal loss functions into a joint probability space." "flowchart LR`n  M1[Property Loss] & M2[Agri Loss] & M3[Business Interruption] --> C{Gaussian/Student-t Copula}`n  C --> J[Joint Exceedance Probability] --> T[Tail Value at Risk]"
Append-To-Section $f "## Operational Abstracting and Latency Dynamics" "This diagram highlights how structural detection latency fundamentally alters the physical trajectory and severity of the catastrophic event." "graph LR`n  I[Ignition] --> D[Detection Latency] --> R[Response Time]`n  R --> S[Severity Escalation]`n  D -.->|Latency Reduction| S"

# --- Part 5 ---
$f = "05_INSURANCE_INVESTMENT_AND_RESILIENCE_FINANCE.md"
Append-To-Section $f "## Continuous Underwriting and the Renewal Cycle" "The circular flowchart below contrasts the continuous underwriting feedback loop against the fractured timeline of traditional annual renewals." "graph TD`n  T[Traditional: Annual Renewal] --> L[Lagging Pricing]`n  C[Continuous: Real-time Telemetry] --> U[Dynamic Premium Adjustment] --> P[Proactive Capital Allocation]"
Append-To-Section $f "## Reinsurance Capital and Prospective Pricing" "This diagram tracks the flow of real-time intelligence up the financial stack to optimize reinsurance treaty negotiations." "flowchart LR`n  L[Localized Severity Data] --> A[Accumulation Dashboard]`n  A --> R[Reinsurance Treaty Structuring] --> O[Optimized Capital Efficiency]"
Append-To-Section $f "## Resilience Finance and Parametric Accuracy" "The feedback loop modeled below demonstrates how underwriting savings are securitized to fund critical municipal climate adaptation." "graph TD`n  D[Detection Savings] --> B[Resilience Bond Issuance]`n  B --> M[Municipal Infrastructure] --> V[Decreased Vulnerability] --> D"

# --- Part 6 ---
$f = "06_GOVERNANCE_VALIDATION_AND_IMPLEMENTATION.md"
Append-To-Section $f "## Regulatory Compliance and Algorithmic Privacy" "The architecture diagram below outlines the bifurcated data environment ensuring that highly sensitive telemetry is securely segregated from pricing algorithms." "flowchart TD`n  R[Raw Telemetry] --> E[Encryption Gateway]`n  E --> P[Perception Layer] --> A[Anonymized Hazard State]`n  A --> U[Underwriting Pricing Logic]"
Append-To-Section $f "## Shadow-Mode Actuarial Validation" "This process flow illustrates the dual-track validation pipeline required to explicitly prove the AI model's superiority prior to national scale-up." "graph LR`n  T[Telemetry] --> N[New AI Engine] & L[Legacy Static Model]`n  N --> C[Comparative Loss Analysis]`n  L --> C`n  C --> A[Regulatory Approval Gate]"
Append-To-Section $f "## Cloud Architecture and Systemic Scaling" "The infrastructure diagram below details the highly available cloud topology necessary to process extreme observation volatility during active disasters." "graph TD`n  I[Ingestion APIs] --> L[Load Balancers]`n  L --> K[Kubernetes Processing Cluster]`n  K --> D[Distributed Actuarial Database] --> R[Real-time Dashboards]"

& ".\build-pdf.ps1"
