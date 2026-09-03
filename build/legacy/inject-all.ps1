function Inject-Diagram ($file, $injections) {
    $lines = [System.IO.File]::ReadAllLines($file, [System.Text.Encoding]::UTF8)
    $newLines = @()
    $inTarget = $false
    $inPara = $false
    $targetHeader = ""
    $currentInjection = $null

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $newLines += $line

        if ($currentInjection -eq $null) {
            foreach ($key in $injections.Keys) {
                if ($line -match "^$key") {
                    $inTarget = $true
                    $targetHeader = $key
                    $currentInjection = $injections[$key]
                    break
                }
            }
        }
        elseif ($inTarget) {
            if ($line.Trim().Length -gt 0 -and (-not ($line -match "^#"))) {
                $inPara = $true
            }
            elseif ($inPara -and $line.Trim().Length -eq 0) {
                $newLines[$newLines.Count - 2] += " " + $currentInjection.Ref
                $newLines += ""
                $newLines += "```mermaid"
                $newLines += $currentInjection.Mermaid
                $newLines += "```"
                $newLines += ""
                $inTarget = $false
                $inPara = $false
                $currentInjection = $null
            }
        }
    }
    [System.IO.File]::WriteAllLines($file, $newLines, [System.Text.Encoding]::UTF8)
}

# --- Part 1 ---
$p1 = [ordered]@{
    "## Hydrological and Climate Vulnerabilities" = @{
        Ref = "As illustrated in the process flow below, this architecture fundamentally shifts catastrophe response from a lagging, reactive indemnification process into a proactive, continuous intelligence lifecycle."
        Mermaid = @("graph LR", "  subgraph Reactive", "    E1[Event] --> L1[Lagging Detection] --> C1[Triage] --> P1[Delayed Payout]", "  end", "  subgraph Continuous Intelligence", "    E2[Event] --> D2[Observation Mesh] --> H2[Dynamic Inference] --> U2[Instant Assessment]", "  end")
    }
    "## Telemetry and Actuarial Observation Gaps" = @{
        Ref = "The diagram below demonstrates how disparate observation methodologies are spatially and temporally fused to construct a unified hazard map."
        Mermaid = @("flowchart TD", "  S[Satellites] --> F(Spatial Registration)", "  C[Crowd] --> F", "  V[Sensors] --> F", "  F --> B{Bayesian Fusion Engine} --> H[Dynamic Hazard Polygon]")
    }
    "## Socio-Economic and Agricultural Exposure" = @{
        Ref = "The sequence below illustrates the cascading economic degradation occurring when an acute trigger evolves into a systemic livelihood crisis."
        Mermaid = @("graph TD", "  A[Precipitation Deficit] --> B[Soil Moisture Depletion] --> C{Agricultural Viability}", "  C -->|Minor| D[Yield Reduction]", "  C -->|Severe| E[Total Crop Failure] --> F[Distress Livestock Sales] --> G[Market Collapse]")
    }
}
Inject-Diagram "01_KENYA_MULTI_HAZARD_INTELLIGENCE_THESIS.md" $p1

# --- Part 2 ---
$p2 = [ordered]@{
    "## Distributed Intelligence and Sensor Networks" = @{
        Ref = "The network topology mapped below showcases the hierarchical ingestion of data from the physical environment into the centralized processing mesh."
        Mermaid = @("graph TD", "  S[Satellites] & D[Drones] & C[Smartphones] --> N[Regional Nodes] --> Core[Processing Matrix] --> Act[Actuarial Engine]")
    }
    "## Machine Perception and Crowd Integration" = @{
        Ref = "The flowchart below details how raw optical feeds are algorithmically transformed into actionable, geometric damage representations."
        Mermaid = @("flowchart LR", "  I[Optical Image] --> V[Vision Transformer] --> Y[YOLOv8 Detection] --> B[Box Regression]", "  B --> C{Confidence > 0.85?}", "  C -->|Yes| P[Semantic Polygon]", "  C -->|No| R[Request Crowd Corroboration]")
    }
    "## Bayesian Evidence Aggregation" = @{
        Ref = "This directed acyclic graph visualizes the rigorous filtering mechanism isolating only the statistically significant ground-truth signal."
        Mermaid = @("graph TD", "  Raw[Unfiltered Reports] --> F1[Spatial Density] & F2[Temporal Sequencing] --> iHMM{Hidden Markov Model}", "  iHMM -->|Noise| Drop[Discard]", "  iHMM -->|Consensus| Post[Posterior Credible Interval] --> Valid[Validated Input]")
    }
}
Inject-Diagram "02_CROWD_AI_AND_OBSERVATION_ARCHITECTURE.md" $p2

# --- Part 3 ---
$p3 = [ordered]@{
    "## Dynamic Spatial Polygon Processing" = @{
        Ref = "The state diagram below illustrates the autoregressive spatial-temporal framework used to process expanding hazard boundaries."
        Mermaid = @("stateDiagram-v2", "  [*] --> BaseState", "  BaseState --> ExpandingPolygon : Hydrological Anomaly", "  ExpandingPolygon --> StablePolygon : Remediation", "  StablePolygon --> [*]")
    }
    "## Mobile Perils and Isolated Hazards" = @{
        Ref = "The flowchart below maps the multi-dimensional kinetic modeling approach used for tracking biological catastrophes like locust swarms."
        Mermaid = @("flowchart TD", "  W[Wind Vectors] & V[Vegetation Density] & L[Lifecycle Stage] --> M[Movement Algorithm]", "  M --> T[Directional Velocity Vector] --> P[Future Hazard Polygon]")
    }
    "## Actuarial Digital Twins and Intensity Metrics" = @{
        Ref = "This architecture diagram shows how physical hazard manifestations are computationally mapped against insured exposures."
        Mermaid = @("graph LR", "  H[Hazard Polygon] --> I[Intersection Engine]", "  E[Exposure Database] --> I", "  I --> D[Damage Ratio Curve] --> L[Expected Loss Computation]")
    }
}
Inject-Diagram "03_SPATIOTEMPORAL_HAZARD_STATE_MODELLING.md" $p3

# --- Part 4 ---
$p4 = [ordered]@{
    "## Financial Severity and Negative Binomial Overdispersion" = @{
        Ref = "The process flow below demonstrates how overdispersed event frequencies are parameterized within the continuous loss engine."
        Mermaid = @("graph TD", "  E[Earned Exposure] --> M[Mean Estimation]", "  O[Overdispersion Parameter] --> N[Negative Binomial Frequency]", "  M --> N --> S[Stochastic Event Generation]")
    }
    "## Copulas and Tail Risk Quantification" = @{
        Ref = "The structural mapping below visualizes how asymmetric copulas synchronize disparate marginal loss functions into a joint probability space."
        Mermaid = @("flowchart LR", "  M1[Property Loss] & M2[Agri Loss] & M3[Business Interruption] --> C{Gaussian/Student-t Copula}", "  C --> J[Joint Exceedance Probability] --> T[Tail Value at Risk]")
    }
    "## Operational Abstracting and Latency Dynamics" = @{
        Ref = "This diagram highlights how structural detection latency fundamentally alters the physical trajectory and severity of the catastrophic event."
        Mermaid = @("graph LR", "  I[Ignition] --> D[Detection Latency] --> R[Response Time]", "  R --> S[Severity Escalation]", "  D -.->|Latency Reduction| S")
    }
}
Inject-Diagram "04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md" $p4

# --- Part 5 ---
$p5 = [ordered]@{
    "## Continuous Underwriting and the Renewal Cycle" = @{
        Ref = "The circular flowchart below contrasts the continuous underwriting feedback loop against the fractured timeline of traditional annual renewals."
        Mermaid = @("graph TD", "  T[Traditional: Annual Renewal] --> L[Lagging Pricing]", "  C[Continuous: Real-time Telemetry] --> U[Dynamic Premium Adjustment] --> P[Proactive Capital Allocation]")
    }
    "## Reinsurance Capital and Prospective Pricing" = @{
        Ref = "This diagram tracks the flow of real-time intelligence up the financial stack to optimize reinsurance treaty negotiations."
        Mermaid = @("flowchart LR", "  L[Localized Severity Data] --> A[Accumulation Dashboard]", "  A --> R[Reinsurance Treaty Structuring] --> O[Optimized Capital Efficiency]")
    }
    "## Resilience Finance and Parametric Accuracy" = @{
        Ref = "The feedback loop modeled below demonstrates how underwriting savings are securitized to fund critical municipal climate adaptation."
        Mermaid = @("graph TD", "  D[Detection Savings] --> B[Resilience Bond Issuance]", "  B --> M[Municipal Infrastructure] --> V[Decreased Vulnerability] --> D")
    }
}
Inject-Diagram "05_INSURANCE_INVESTMENT_AND_RESILIENCE_FINANCE.md" $p5

# --- Part 6 ---
$p6 = [ordered]@{
    "## Regulatory Compliance and Algorithmic Privacy" = @{
        Ref = "The architecture diagram below outlines the bifurcated data environment ensuring that highly sensitive telemetry is securely segregated from pricing algorithms."
        Mermaid = @("flowchart TD", "  R[Raw Telemetry] --> E[Encryption Gateway]", "  E --> P[Perception Layer] --> A[Anonymized Hazard State]", "  A --> U[Underwriting Pricing Logic]")
    }
    "## Shadow-Mode Actuarial Validation" = @{
        Ref = "This process flow illustrates the dual-track validation pipeline required to explicitly prove the AI model's superiority prior to national scale-up."
        Mermaid = @("graph LR", "  T[Telemetry] --> N[New AI Engine] & L[Legacy Static Model]", "  N --> C[Comparative Loss Analysis]", "  L --> C", "  C --> A[Regulatory Approval Gate]")
    }
    "## Cloud Architecture and Systemic Scaling" = @{
        Ref = "The infrastructure diagram below details the highly available cloud topology necessary to process extreme observation volatility during active disasters."
        Mermaid = @("graph TD", "  I[Ingestion APIs] --> L[Load Balancers]", "  L --> K[Kubernetes Processing Cluster]", "  K --> D[Distributed Actuarial Database] --> R[Real-time Underwriting Dashboards]")
    }
}
Inject-Diagram "06_GOVERNANCE_VALIDATION_AND_IMPLEMENTATION.md" $p6

& ".\build-pdf.ps1"
