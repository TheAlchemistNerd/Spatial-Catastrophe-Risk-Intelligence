# Post-Approval Research and Delivery Roadmap

**Author:** Nevil Maloba  
**Affiliation:** Founder, Philtechent LTD  
**Research:** *Can Spatial Catastrophe Intelligence Improve Bank Credit-Risk Identification in Kenya? A Flood-and-Drought Empirical Framework*

## What approval activates

KBA approval should be converted immediately into a written delivery brief. The brief will record whether KBA is offering a Methodological Session, a Working Paper route, the next conference cycle, or a combination. It will also confirm the required date, reviewer process, policy-brief format, presentation expectations and whether KBA can facilitate banking-sector data or research introductions.

The research then moves through eight connected workstreams:

```{.mermaid #kba-post-approval-roadmap landscape="true" alt="Post-approval research and delivery roadmap"}
%%{init: {"theme": "base", "themeVariables": {"background": "#F7FAFC", "primaryTextColor": "#172B4D", "lineColor": "#3B5B92", "fontSize": "17px", "fontFamily": "Arial"}, "flowchart": {"curve": "basis", "nodeSpacing": 38, "rankSpacing": 48}}}%%
flowchart LR
  G1["1. KBA delivery brief<br/>route • dates • reviewers • outputs"]
  G2["2. Bank and data partnership<br/>outcome • sample • location • approvals"]
  G3["3. Pre-analysis protocol<br/>hypotheses • estimands • holdouts • metrics"]
  G4["4. Hazard reconstruction<br/>flood events • drought duration • point-in-time features"]
  G5["5. Analytical panel<br/>linkage • quality • missingness • exposure"]
  G6["6. Baseline and challenger<br/>calibration • robustness • subgroup performance"]
  G7["7. Banking translation<br/>PD • LGD • EAD • ECL • resilience finance"]
  G8["8. Publication and review<br/>paper • policy brief • presentation • revision"]

  G1 --> G2 --> G3 --> G4 --> G5 --> G6 --> G7 --> G8

  classDef mandate fill:#DCEEFF,stroke:#2C6E9F,stroke-width:2px,color:#102A43;
  classDef data fill:#DFF3E4,stroke:#2F855A,stroke-width:2px,color:#153E2C;
  classDef method fill:#FFF1CC,stroke:#B7791F,stroke-width:2px,color:#5F370E;
  classDef model fill:#E9E1F8,stroke:#6B46A3,stroke-width:2px,color:#32215B;
  classDef finance fill:#FDE2E2,stroke:#B64B4B,stroke-width:2px,color:#5A1E1E;
  classDef publication fill:#D8F3F0,stroke:#147D78,stroke-width:2px,color:#123C3A;

  class G1 mandate;
  class G2,G4,G5 data;
  class G3 method;
  class G6 model;
  class G7 finance;
  class G8 publication;
```

**Figure 1. The work activated by KBA approval.**

## 1. Confirm the KBA route and research contract

Within two working days of approval, prepare a one-page confirmation record covering:

- the accepted title and scope;
- whether the output is a conference method paper, empirical working paper or both;
- submission, review and presentation dates;
- page, word, citation and policy-brief requirements;
- KBA’s nominated research contact and review process;
- permitted use of the KBA name and event identity; and
- opportunities for a bank, KBA data platform or research collaborator.

The current proposal will then be versioned as the approved research protocol. Changes requested by KBA will be recorded rather than silently absorbed, preserving the origin and development of the SCRI research.

## 2. Secure a banking and data pathway

The first empirical meeting should involve a credit-risk owner, data steward and model-risk or research representative. The parties will select one primary outcome, such as entry into arrears, Stage 2/3 migration, restructuring, default or cure. They will then assess whether the available history contains usable borrower or collateral geography and overlaps suitable flood and drought periods.

The preferred route is a pseudonymised facility–month or facility–quarter panel analysed inside the bank or an approved trusted environment. An aggregated bank–sector–county panel provides a second route. The public-data methodological demonstrator can proceed while partnership approvals mature.

Deliverables are the signed study scope, data dictionary, lawful-use and security schedule, publication rules, and a sample/event-overlap feasibility table.

## 3. Freeze the pre-analysis protocol

Before fitting the main models, record:

- primary and secondary outcomes;
- prediction dates and horizons;
- flood and drought event definitions;
- sample inclusion, exclusion and censoring rules;
- baseline and challenger specifications;
- hypotheses H1–H5;
- temporal, geographic and event holdouts;
- primary calibration and decision metrics;
- subgroup and data-coverage tests; and
- conditions for causal, predictive and resilience claims.

This protocol gives reviewers a clear view of what was planned before results were known and supports reproducibility.

## 4. Reconstruct the flood and drought evidence

The flood workstream should select one or more events with credible rainfall, river or drainage, remote-sensing and impact observations. The 2024 long-rains floods are a strong candidate, subject to compatible banking history and exposure geography. Outputs will include versioned footprints, depth or intensity bands, duration, access disruption, observation confidence and recovery dates.

The drought workstream should select a period with sufficient NDMA, rainfall, vegetation, water, livestock, crop or market information. Its features will represent duration and progression rather than one event date. All variables will preserve event time, knowledge time, spatial support, revision status and source.

A hydrologist or flood specialist and a drought/livelihood specialist should review the feature definitions before financial linkage.

## 5. Build and quality-assure the analytical panel

The banking and hazard datasets will be joined using the approved spatial key. The research team will produce:

- a flow of the sample from raw records to the final panel;
- missingness and geocoding-quality tables;
- event and drought exposure counts;
- outcome incidence by time, sector and geography;
- balance and overlap diagnostics for affected and comparison observations;
- leakage tests confirming that future information has not entered past predictions; and
- disclosure-control rules for publication.

The feasibility gate is passed when the selected outcomes, hazard exposure and holdout samples support meaningful estimation. Where one design is sparse, the study can prioritise the stronger hazard empirically and retain the second as a methodological comparison.

## 6. Estimate the transparent baseline and SCRI challenger

The baseline will use repayment history, facility terms, borrower segment, macroeconomic variables, sector and coarse geography. The challenger will add hazard intensity, footprint, duration, exposure, vulnerability, insurance, resilience and recovery variables.

Both models will use the same holdouts. The results pack will include calibration curves, Brier score, log loss, discrimination, sensitivity at a defined review capacity, lead time and geographic performance. Robustness analysis will vary hazard thresholds, buffers, lags, event windows, missing-location assumptions and comparison groups. Subgroup calibration and observation coverage will be reported alongside average performance.

The advancement criterion is practical: the SCRI variables should add stable calibration, lead time, concentration insight or another pre-specified decision benefit that remains visible on genuine holdouts.

## 7. Translate results into banking and resilience decisions

The empirical results will be translated into separate PD, LGD and EAD pathways before expected credit loss is considered:

**ECLᵢ,ₜ = PDᵢ,ₜ × LGDᵢ,ₜ × EADᵢ,ₜ. (1)**

The paper will show which features support early warning, collateral review, portfolio concentration, scenario analysis and expected-loss review. A risk-pricing illustration can be included if the partner confirms the applicable governance and variables.

Resilience and insurance variables will be examined as potential moderators of disruption and recovery. Where project and intervention records are sufficiently strong, the analysis can support resilience-loan appraisal and monitoring. The four SCRI ledgers—risk, intervention, finance and evidence—will provide the bridge from an estimated loss reduction to an investable structure and verified community benefit.

## 8. Complete independent review and publication

The draft will move through six reviews:

1. banking credit-risk and operational usefulness;
2. econometric design and inference;
3. flood and drought science;
4. actuarial and financial translation;
5. data protection, fairness and publication control; and
6. community access and financial-inclusion implications.

Each comment will be logged with its disposition. The final package will include the 8,000–10,000-word paper, two-page policy brief, presentation, data dictionary, model cards, methodological appendix and reproducibility statement. KBA feedback will be integrated into a versioned revision suitable for its Working Paper Series.

## Immediate decisions after approval

The first approval call should resolve four matters:

- Which KBA route and deadline apply?
- Can KBA introduce a participating bank or approved aggregate dataset?
- Which banking outcome has the greatest research and industry value?
- Is the immediate output a methodological demonstration, a completed empirical paper, or a staged combination?

Once these four decisions are recorded, the project can begin data feasibility and hazard reconstruction in parallel.

