import os
import re

diagrams = {
    "01_KENYA_MULTI_HAZARD_INTELLIGENCE_THESIS.md": [
        ("## Hydrological and Climate Vulnerabilities", "As illustrated in the process flow below, this architecture fundamentally shifts catastrophe response from a lagging, reactive indemnification process into a proactive, continuous intelligence lifecycle.", "```mermaid\ngraph LR\n  E1[Disaster Event] --> L1[Lagging Detection]\n  L1 --> C1[Manual Triage]\n  C1 --> P1[Delayed Payout]\n  E2[Disaster Event] --> D2[Observation Mesh]\n  D2 --> H2[Dynamic Inference]\n  H2 --> U2[Instant Assessment]\n```\n**Figure 1.1: Reactive vs. Continuous Intelligence Framework**"),
        ("## Telemetry and Actuarial Observation Gaps", "The diagram below demonstrates how disparate observation methodologies are spatially and temporally fused to construct a unified hazard map.", "```mermaid\ngraph TD\n  S[Satellite Sensors] --> F(Bayesian Fusion Engine)\n  C[Crowd Telemetry] --> F\n  V[IoT Weather Stations] --> F\n  F --> H[Dynamic Hazard Polygon]\n```\n**Figure 1.2: Multi-Modal Observation Fusion**"),
        ("## Socio-Economic and Agricultural Exposure", "The sequence below illustrates the cascading economic degradation occurring when an acute trigger evolves into a systemic livelihood crisis.", "```mermaid\ngraph TD\n  A[Precipitation Deficit] --> B[Soil Moisture Depletion]\n  B --> C{Agricultural Viability}\n  C --> D[Yield Reduction]\n  C --> E[Total Crop Failure]\n  E --> F[Distress Livestock Sales]\n  F --> G[Systemic Market Collapse]\n```\n**Figure 1.3: Cascading Economic Degradation Model**")
    ],
    "02_CROWD_AI_AND_OBSERVATION_ARCHITECTURE.md": [
        ("## Distributed Intelligence and Sensor Networks", "The network topology mapped below showcases the hierarchical ingestion of data from the physical environment into the centralized processing mesh.", "```mermaid\ngraph TD\n  S[Satellites] --> N[Regional Nodes]\n  D[Drones] --> N\n  C[Smartphones] --> N\n  N --> Core[Core Processing Matrix]\n  Core --> Act[Actuarial Engine]\n```\n**Figure 2.1: Hierarchical Data Ingestion Topology**"),
        ("## Machine Perception and Crowd Integration", "The flowchart below details how raw optical feeds are algorithmically transformed into actionable, geometric damage representations.", "```mermaid\ngraph LR\n  I[Raw Optical Image] --> V[Vision Transformer]\n  V --> Y[YOLOv8 Detection]\n  Y --> B[Bounding Box Regression]\n  B --> P[Semantic Damage Polygon]\n  B --> R[Crowd Corroboration Request]\n```\n**Figure 2.2: Deep Learning Perception Pipeline**"),
        ("## Bayesian Evidence Aggregation", "This directed acyclic graph visualizes the rigorous filtering mechanism isolating only the statistically significant ground-truth signal.", "```mermaid\ngraph TD\n  Raw[Unfiltered Crowd Reports] --> F1[Spatial Density Clustering]\n  Raw --> F2[Temporal Sequencing]\n  F1 --> iHMM{Hidden Markov Model}\n  F2 --> iHMM\n  iHMM --> Drop[Discard Noise]\n  iHMM --> Post[Posterior Credible Interval]\n```\n**Figure 2.3: Bayesian Filtering of Social Propagation**")
    ],
    "03_SPATIOTEMPORAL_HAZARD_STATE_MODELLING.md": [
        ("## Dynamic Spatial Polygon Processing", "The state diagram below illustrates the autoregressive spatial-temporal framework used to process expanding hazard boundaries.", "```mermaid\ngraph TD\n  B[Baseline Ecological State] --> E[Expanding Hazard Polygon]\n  E --> E\n  E --> S[Stable Remediation Phase]\n  S --> B\n```\n**Figure 3.1: Autoregressive Spatial-Temporal State Transitions**"),
        ("## Mobile Perils and Isolated Hazards", "The flowchart below maps the multi-dimensional kinetic modeling approach used for tracking biological catastrophes like locust swarms.", "```mermaid\ngraph TD\n  W[Wind Vectors] --> M[Movement Algorithm]\n  V[Vegetation Density] --> M\n  L[Biological Lifecycle] --> M\n  M --> T[Directional Velocity Vector]\n  T --> P[Future Hazard Footprint]\n```\n**Figure 3.2: Multi-Dimensional Kinetic Tracking**"),
        ("## Actuarial Digital Twins and Intensity Metrics", "This architecture diagram shows how physical hazard manifestations are computationally mapped against insured exposures.", "```mermaid\ngraph LR\n  H[Dynamic Hazard Polygon] --> I[Intersection Engine]\n  E[Exposure Database] --> I\n  I --> D[Damage Ratio Curve]\n  D --> L[Expected Loss Computation]\n```\n**Figure 3.3: Actuarial Digital Twin Intersection**")
    ],
    "04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md": [
        ("## Financial Severity and Negative Binomial Overdispersion", "The process flow below demonstrates how overdispersed event frequencies are parameterized within the continuous loss engine.", "```mermaid\ngraph TD\n  E[Earned Exposure] --> M[Mean Estimation]\n  O[Overdispersion Parameter] --> N[Negative Binomial Frequency]\n  M --> N\n  N --> S[Stochastic Event Generation]\n```\n**Figure 4.1: Overdispersed Frequency Parameterization**"),
        ("## Copulas and Tail Risk Quantification", "The structural mapping below visualizes how asymmetric copulas synchronize disparate marginal loss functions into a joint probability space.", "```mermaid\ngraph LR\n  M1[Property Loss] --> C{Gaussian / Student-t Copula}\n  M2[Agricultural Loss] --> C\n  M3[Business Interruption] --> C\n  C --> J[Joint Exceedance Probability]\n  J --> T[Tail Value at Risk]\n```\n**Figure 4.2: Asymmetric Copula Synchronization**"),
        ("## Operational Abstracting and Latency Dynamics", "This diagram highlights how structural detection latency fundamentally alters the physical trajectory and severity of the catastrophic event.", "```mermaid\ngraph LR\n  I[Ignition Event] --> D[Detection Latency]\n  D --> R[Response Time]\n  R --> S[Severity Escalation]\n```\n**Figure 4.3: Structural Latency and Severity Dynamics**")
    ],
    "05_INSURANCE_INVESTMENT_AND_RESILIENCE_FINANCE.md": [
        ("## Continuous Underwriting and the Renewal Cycle", "The circular flowchart below contrasts the continuous underwriting feedback loop against the fractured timeline of traditional annual renewals.", "```mermaid\ngraph TD\n  T[Traditional Annual Renewal] --> L[Lagging Historical Pricing]\n  C[Continuous Real-time Telemetry] --> U[Dynamic Premium Adjustment]\n  U --> P[Proactive Capital Allocation]\n```\n**Figure 5.1: Continuous Underwriting Feedback Loop**"),
        ("## Reinsurance Capital and Prospective Pricing", "This diagram tracks the flow of real-time intelligence up the financial stack to optimize reinsurance treaty negotiations.", "```mermaid\ngraph LR\n  L[Localized Severity Intelligence] --> A[Accumulation Dashboard]\n  A --> R[Reinsurance Treaty Structuring]\n  R --> O[Optimized Capital Efficiency]\n```\n**Figure 5.2: Reinsurance Intelligence Flow**"),
        ("## Resilience Finance and Parametric Accuracy", "The feedback loop modeled below demonstrates how underwriting savings are securitized to fund critical municipal climate adaptation.", "```mermaid\ngraph TD\n  D[Detection Savings] --> B[Resilience Bond Issuance]\n  B --> M[Municipal Infrastructure Investments]\n  M --> V[Decreased Exposure Vulnerability]\n  V --> D\n```\n**Figure 5.3: Securitized Resilience Finance Loop**")
    ],
    "06_GOVERNANCE_VALIDATION_AND_IMPLEMENTATION.md": [
        ("## Regulatory Compliance and Algorithmic Privacy", "The architecture diagram below outlines the bifurcated data environment ensuring that highly sensitive telemetry is securely segregated from pricing algorithms.", "```mermaid\ngraph TD\n  R[Raw Telemetry] --> E[Encryption Gateway]\n  E --> P[Perception Layer]\n  P --> A[Anonymized Hazard State]\n  A --> U[Underwriting Pricing Logic]\n```\n**Figure 6.1: Segregated Data Privacy Architecture**"),
        ("## Shadow-Mode Actuarial Validation", "This process flow illustrates the dual-track validation pipeline required to explicitly prove the AI model's superiority prior to national scale-up.", "```mermaid\ngraph LR\n  T[Live Telemetry] --> N[New AI Engine]\n  T --> L[Legacy Static Model]\n  N --> C[Comparative Loss Analysis]\n  L --> C\n  C --> A[Regulatory Approval Gate]\n```\n**Figure 6.2: Dual-Track Shadow-Mode Validation**"),
        ("## Cloud Architecture and Systemic Scaling", "The infrastructure diagram below details the highly available cloud topology necessary to process extreme observation volatility during active disasters.", "```mermaid\ngraph TD\n  I[Ingestion APIs] --> L[Load Balancers]\n  L --> K[Kubernetes Processing Cluster]\n  K --> D[Distributed Actuarial Database]\n  D --> R[Real-time Underwriting Dashboards]\n```\n**Figure 6.3: Highly Available Cloud Topology**")
    ]
}

for filename in os.listdir("."):
    if not filename.endswith(".md") or not filename.startswith("0"): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove old diagrams and captions
    # Previously I might have injected some diagrams, we need to strip them.
    # We strip ```mermaid ... ```
    content = re.sub(r'```mermaid[\s\S]*?```', '', content)
    # Strip any old "**Figure x.x: ...**"
    content = re.sub(r'\*\*Figure \d+\.\d+:.*?\*\*\n?', '', content)
    
    # Strip old reference text
    for part_diagrams in diagrams.values():
        for _, ref, _ in part_diagrams:
            content = content.replace(ref, "")
            
    # Clean up excess newlines created by stripping
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Fix References spacing: Ensure [X] starts on a new line and has a blank line before it if it's in a list
    # The safest way is to find ## References and ensure everything after it is double-spaced.
    ref_idx = content.find("## References")
    if ref_idx != -1:
        part1 = content[:ref_idx]
        part2 = content[ref_idx:]
        # replace single newlines between references with double newlines
        part2 = re.sub(r'(\[\d+\] [^\n]+)\n(?=\[\d+\])', r'\1\n\n', part2)
        content = part1 + part2
            
    # Inject new diagrams
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
