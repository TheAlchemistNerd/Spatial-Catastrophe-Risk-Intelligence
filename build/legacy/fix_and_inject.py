import os
import re

header_replacements = {
    "02_CROWD_AI_AND_OBSERVATION_ARCHITECTURE.md": [
        ("## How Do We Construct a Multi-Tiered Observation Mesh?", "## Distributed Intelligence and Sensor Networks"),
        ("## What Are the Dangers of Unfiltered Algorithmic Propagation?", "## Machine Perception and Crowd Integration"),
        ("## Can Machine Perception and Human Intelligence be Mathematically Fused?", "## Bayesian Evidence Aggregation")
    ],
    "03_SPATIOTEMPORAL_HAZARD_STATE_MODELLING.md": [
        ("## Why Must We Abandon Rigid Academic Models for Practical Tracking?", "## Dynamic Spatial Polygon Processing"),
        ("## How Does the Architecture Map Non-Visual or Isolated Hazards?", "## Mobile Perils and Isolated Hazards"),
        ("## How Are Physical Manifestations Translated into Standardized Intensity Metrics?", "## Actuarial Digital Twins and Intensity Metrics")
    ],
    "04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md": [
        ("## How is Environmental Intensity Converted into Financial Severity?", "## Financial Severity and Negative Binomial Overdispersion"),
        ("## Can We Synthesize Distinct Statistical Models into a Unified Hierarchy?", "## Copulas and Tail Risk Quantification"),
        ("## How Are Correlated Claims and Spatial Dependencies Accurately Modeled?", "## Operational Abstracting and Latency Dynamics")
    ],
    "05_INSURANCE_INVESTMENT_AND_RESILIENCE_FINANCE.md": [
        ("## How Does Continuous Underwriting Disrupt the Annual Renewal Cycle?", "## Continuous Underwriting and the Renewal Cycle"),
        ("## How Does Localized Severity Data Revolutionize Prospective Pricing?", "## Reinsurance Capital and Prospective Pricing"),
        ("## Can Disaster Detection Networks Generate Monetizable Financial Assets?", "## Resilience Finance and Parametric Accuracy")
    ],
    "06_GOVERNANCE_VALIDATION_AND_IMPLEMENTATION.md": [
        ("## Why is Stringent Regulatory Governance Non-Negotiable for Insurtech?", "## Regulatory Compliance and Algorithmic Privacy"),
        ("## How Do We Eliminate Algorithmic Bias and Guarantee Actuarial Explainability?", "## Shadow-Mode Actuarial Validation"),
        ("## How Are Systemic Operational Risks Isolated During Live Commercial Pilots?", "## Cloud Architecture and Systemic Scaling")
    ]
}

diagrams = {
    "01_KENYA_MULTI_HAZARD_INTELLIGENCE_THESIS.md": [
        ("## Hydrological and Climate Vulnerabilities", "As illustrated in the process flow below, this architecture fundamentally shifts catastrophe response from a lagging, reactive indemnification process into a proactive, continuous intelligence lifecycle.", "```mermaid\ngraph LR\n  subgraph Reactive\n    E1[Event] --> L1[Lagging Detection] --> C1[Triage] --> P1[Delayed Payout]\n  end\n  subgraph Continuous Intelligence\n    E2[Event] --> D2[Observation Mesh] --> H2[Dynamic Inference] --> U2[Instant Assessment]\n  end\n```"),
        ("## Telemetry and Actuarial Observation Gaps", "The diagram below demonstrates how disparate observation methodologies are spatially and temporally fused to construct a unified hazard map.", "```mermaid\nflowchart TD\n  S[Satellites] --> F(Spatial Registration)\n  C[Crowd] --> F\n  V[Sensors] --> F\n  F --> B{Bayesian Fusion Engine} --> H[Dynamic Hazard Polygon]\n```"),
        ("## Socio-Economic and Agricultural Exposure", "The sequence below illustrates the cascading economic degradation occurring when an acute trigger evolves into a systemic livelihood crisis.", "```mermaid\ngraph TD\n  A[Precipitation Deficit] --> B[Soil Moisture Depletion] --> C{Agricultural Viability}\n  C -->|Minor| D[Yield Reduction]\n  C -->|Severe| E[Total Crop Failure] --> F[Distress Livestock Sales] --> G[Market Collapse]\n```")
    ],
    "02_CROWD_AI_AND_OBSERVATION_ARCHITECTURE.md": [
        ("## Distributed Intelligence and Sensor Networks", "The network topology mapped below showcases the hierarchical ingestion of data from the physical environment into the centralized processing mesh.", "```mermaid\ngraph TD\n  S[Satellites] & D[Drones] & C[Smartphones] --> N[Regional Nodes] --> Core[Processing Matrix] --> Act[Actuarial Engine]\n```"),
        ("## Machine Perception and Crowd Integration", "The flowchart below details how raw optical feeds are algorithmically transformed into actionable, geometric damage representations.", "```mermaid\nflowchart LR\n  I[Optical Image] --> V[Vision Transformer] --> Y[YOLOv8 Detection] --> B[Box Regression]\n  B --> C{Confidence > 0.85?}\n  C -->|Yes| P[Semantic Polygon]\n  C -->|No| R[Request Crowd Corroboration]\n```"),
        ("## Bayesian Evidence Aggregation", "This directed acyclic graph visualizes the rigorous filtering mechanism isolating only the statistically significant ground-truth signal.", "```mermaid\ngraph TD\n  Raw[Unfiltered Reports] --> F1[Spatial Density] & F2[Temporal Sequencing] --> iHMM{Hidden Markov Model}\n  iHMM -->|Noise| Drop[Discard]\n  iHMM -->|Consensus| Post[Posterior Credible Interval] --> Valid[Validated Input]\n```")
    ],
    "03_SPATIOTEMPORAL_HAZARD_STATE_MODELLING.md": [
        ("## Dynamic Spatial Polygon Processing", "The state diagram below illustrates the autoregressive spatial-temporal framework used to process expanding hazard boundaries.", "```mermaid\nstateDiagram-v2\n  [*] --> BaseState\n  BaseState --> ExpandingPolygon : Hydrological Anomaly\n  ExpandingPolygon --> StablePolygon : Remediation\n  StablePolygon --> [*]\n```"),
        ("## Mobile Perils and Isolated Hazards", "The flowchart below maps the multi-dimensional kinetic modeling approach used for tracking biological catastrophes like locust swarms.", "```mermaid\nflowchart TD\n  W[Wind Vectors] & V[Vegetation Density] & L[Lifecycle Stage] --> M[Movement Algorithm]\n  M --> T[Directional Velocity Vector] --> P[Future Hazard Polygon]\n```"),
        ("## Actuarial Digital Twins and Intensity Metrics", "This architecture diagram shows how physical hazard manifestations are computationally mapped against insured exposures.", "```mermaid\ngraph LR\n  H[Hazard Polygon] --> I[Intersection Engine]\n  E[Exposure Database] --> I\n  I --> D[Damage Ratio Curve] --> L[Expected Loss Computation]\n```")
    ],
    "04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md": [
        ("## Financial Severity and Negative Binomial Overdispersion", "The process flow below demonstrates how overdispersed event frequencies are parameterized within the continuous loss engine.", "```mermaid\ngraph TD\n  E[Earned Exposure] --> M[Mean Estimation]\n  O[Overdispersion Parameter] --> N[Negative Binomial Frequency]\n  M --> N --> S[Stochastic Event Generation]\n```"),
        ("## Copulas and Tail Risk Quantification", "The structural mapping below visualizes how asymmetric copulas synchronize disparate marginal loss functions into a joint probability space.", "```mermaid\nflowchart LR\n  M1[Property Loss] & M2[Agri Loss] & M3[Business Interruption] --> C{Gaussian/Student-t Copula}\n  C --> J[Joint Exceedance Probability] --> T[Tail Value at Risk]\n```"),
        ("## Operational Abstracting and Latency Dynamics", "This diagram highlights how structural detection latency fundamentally alters the physical trajectory and severity of the catastrophic event.", "```mermaid\ngraph LR\n  I[Ignition] --> D[Detection Latency] --> R[Response Time]\n  R --> S[Severity Escalation]\n  D -.->|Latency Reduction| S\n```")
    ],
    "05_INSURANCE_INVESTMENT_AND_RESILIENCE_FINANCE.md": [
        ("## Continuous Underwriting and the Renewal Cycle", "The circular flowchart below contrasts the continuous underwriting feedback loop against the fractured timeline of traditional annual renewals.", "```mermaid\ngraph TD\n  T[Traditional: Annual Renewal] --> L[Lagging Pricing]\n  C[Continuous: Real-time Telemetry] --> U[Dynamic Premium Adjustment] --> P[Proactive Capital Allocation]\n```"),
        ("## Reinsurance Capital and Prospective Pricing", "This diagram tracks the flow of real-time intelligence up the financial stack to optimize reinsurance treaty negotiations.", "```mermaid\nflowchart LR\n  L[Localized Severity Data] --> A[Accumulation Dashboard]\n  A --> R[Reinsurance Treaty Structuring] --> O[Optimized Capital Efficiency]\n```"),
        ("## Resilience Finance and Parametric Accuracy", "The feedback loop modeled below demonstrates how underwriting savings are securitized to fund critical municipal climate adaptation.", "```mermaid\ngraph TD\n  D[Detection Savings] --> B[Resilience Bond Issuance]\n  B --> M[Municipal Infrastructure] --> V[Decreased Vulnerability] --> D\n```")
    ],
    "06_GOVERNANCE_VALIDATION_AND_IMPLEMENTATION.md": [
        ("## Regulatory Compliance and Algorithmic Privacy", "The architecture diagram below outlines the bifurcated data environment ensuring that highly sensitive telemetry is securely segregated from pricing algorithms.", "```mermaid\nflowchart TD\n  R[Raw Telemetry] --> E[Encryption Gateway]\n  E --> P[Perception Layer] --> A[Anonymized Hazard State]\n  A --> U[Underwriting Pricing Logic]\n```"),
        ("## Shadow-Mode Actuarial Validation", "This process flow illustrates the dual-track validation pipeline required to explicitly prove the AI model's superiority prior to national scale-up.", "```mermaid\ngraph LR\n  T[Telemetry] --> N[New AI Engine] & L[Legacy Static Model]\n  N --> C[Comparative Loss Analysis]\n  L --> C\n  C --> A[Regulatory Approval Gate]\n```"),
        ("## Cloud Architecture and Systemic Scaling", "The infrastructure diagram below details the highly available cloud topology necessary to process extreme observation volatility during active disasters.", "```mermaid\ngraph TD\n  I[Ingestion APIs] --> L[Load Balancers]\n  L --> K[Kubernetes Processing Cluster]\n  K --> D[Distributed Actuarial Database] --> R[Real-time Dashboards]\n```")
    ]
}

for filename in os.listdir("."):
    if not filename.endswith(".md") or not filename.startswith("0"): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for part_diagrams in diagrams.values():
        for _, ref, _ in part_diagrams:
            content = content.replace(ref, "")
            
    content = re.sub(r'```?mermaid[\s\S]*?```?r?\n?', '', content)
    content = content.replace("``r", "")
    
    if filename in header_replacements:
        for old, new in header_replacements[filename]:
            content = content.replace(old, new)
            content = re.sub(r'(?m)^' + re.escape(old) + r'\s*$', new, content)
            
    if filename in diagrams:
        for header, ref, mermaid in diagrams[filename]:
            header_idx = content.find(header)
            if header_idx != -1:
                next_header_idx = content.find("## ", header_idx + len(header))
                if next_header_idx == -1: next_header_idx = len(content)
                part1 = content[:next_header_idx].rstrip()
                part2 = content[next_header_idx:]
                content = part1 + f"\n\n{ref}\n\n{mermaid}\n\n" + part2
                
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
print("done")
