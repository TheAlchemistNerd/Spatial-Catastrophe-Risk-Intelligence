# Governance, Validation, Operating Model and Phased Implementation

## Abstract

A catastrophe-intelligence platform cannot be authorised by technical performance alone. It processes sensitive location and event data, interprets uncertainty during emergencies and informs contracts, public decisions and capital allocation. This paper defines the operating model and staged path from Kenya-focused research to controlled multi-hazard use. It assigns data-controller, processor, steward, source owner, model owner, independent validator, product owner and decision owner roles; establishes human challenge, community rights, security, continuity and vendor-exit controls; and sets validation gates across hazards, places, institutions and vulnerable groups.

Implementation proceeds from mandate and prohibited-use definition through data permissions, transparent baselines, shadow-mode observation, dynamic state challengers, loss-intelligence pilots, bounded institutional decisions, independent financial-product testing and measured scale. Flood and drought provide contrasting initial cases. Wildfire and locust test perception and propagation; landslide and storm/heat test local sparsity, compounds and infrastructure/health consequence. Exact locations and partners require a published readiness assessment.

The roadmap names prerequisites, evidence, outputs, owners and stop conditions. It incorporates Kenyan data protection, insurance, climate, disaster-management, public-finance and evolving AI policy diligence while avoiding the claim that publication creates deployment authority. The definition of success is not a national dashboard. It is a governed capability whose estimates are reproducible, whose institutional actions remain accountable and whose benefits are demonstrated without unacceptable harm.

**Research question.** What governance, validation, operating model and stage gates would permit Kenya to research and, where justified, operate multi-hazard catastrophe intelligence safely, legitimately and sustainably?

## 1. Governance starts with the right to say no

During a flood, an insurer asks for access to community photographs collected for public warning. A county wants the model's risk level presented as an official alert. A vendor proposes an opaque upgrade whose historical score improves but whose remote-area calibration is worse. A financier asks to call modelled expected loss reduction “secured savings.”

A mature operating model must reject or constrain all four requests. Governance is not a committee that approves whatever technology produces. It defines purposes, evidence thresholds, accountable owners, prohibited uses, challenge and stop authority before pressure arrives.

The platform is a shared evidence service. It does not become a new meteorological, hydrological, plant-protection, insurance, fiscal or emergency authority. It publishes signed products that identify source and status. Decisions are recorded as downstream events owned by authorised institutions.

## 2. Institutional operating model

### 2.1 Role definitions

- **Source owner:** institution or contributor responsible for the originating system and conditions of supply.
- **Data controller/joint controller:** determines purpose and means of personal-data processing under applicable law.
- **Processor:** operates processing on documented controller instructions.
- **Data steward:** maintains quality, metadata, access and issue resolution for a domain dataset.
- **Platform operator:** runs ingestion, storage, lineage, compute, product delivery and continuity.
- **Model owner:** accountable for purpose, development, monitoring and change.
- **Independent validator:** challenges data, method, implementation, performance and limitations without reporting to the model owner for conclusions.
- **Product owner:** ensures an output is fit for a bounded workflow and users understand it.
- **Decision owner:** has legal, contractual or delegated authority to act.
- **Community governance forum:** represents contributor and affected-community interests in channel, use and safeguard design.
- **Risk and assurance forum:** reviews material model, data, security, legal and conduct risks and can stop use.

One organisation may hold several roles, but conflicts are disclosed and controls maintain independent challenge. A vendor is normally a processor/service provider, not the decision owner.

### 2.2 Three flows

```{.mermaid #fig-6-1 alt="Governance data authority and finance flows"}
flowchart LR
  subgraph DATA[Data flow]
    S[Source] --> ST[Steward and platform operator]
    ST --> M[Validated model]
    M --> PROD[Purpose-specific product]
  end
  subgraph AUTH[Authority flow]
    LAW[Mandate or contract] --> OWNER[Decision owner]
    OWNER --> ACT[Authorised action]
    ACT --> REVIEW[Review and redress]
  end
  subgraph FIN[Finance flow]
    FUND[Appropriation, policy or instrument] --> CALC[Calculation and approval]
    CALC --> PAY[Payment or allocation]
    PAY --> AUDIT[Financial audit]
  end
  PROD -. evidence, not authority .-> OWNER
  ACT -. recorded outcome .-> AUDIT
```

**Figure 6.1 — Governance and decision-rights model.** Data, authority and finance are linked for audit but never collapsed.

Shared identifiers connect the flows. They do not merge them. A payment record links to the evidence and authority that supported it while remaining distinct from the model estimate.

### 2.3 Governance forums

An executive steering forum owns scope, funding and inter-institution escalation. A scientific/model committee owns methodological standards. A data governance committee approves sources, permissions and retention. An operations group handles live service and discrepancy. A community/public-interest forum reviews accessibility, benefit and harm. Independent assurance reports to a governing body with authority to suspend.

Meeting cadence differs: live operations may meet daily during events; model changes quarterly or by release; strategy and independent assurance at defined stage gates. Emergency action cannot bypass later audit.

## 3. Kenyan legal and regulatory diligence agenda

This section frames research questions, not legal advice. Each pilot obtains current Kenyan counsel and regulator/agency engagement.

### 3.1 Data protection

The Data Protection Act governs personal data and provides safeguards concerning solely automated decisions with legal or similarly significant effects [1]. The General Regulations address transparency, human intervention and high-risk processing, including large-scale dataset combination, systematic monitoring of public areas, innovative technologies and vulnerable groups [2].

Required work includes controller/joint-controller allocation, lawful basis, privacy notice, data-protection impact assessment, processor terms, cross-border transfer, retention, rights workflow, breach response, children's/vulnerable-person data, biometrics/imagery and automated-decision safeguards. Emergency purpose does not become permanent general purpose.

### 3.2 Insurance and conduct

Insurance-product, claims, market-conduct, risk-management and capital guidance define separate obligations [3]–[6]. Diligence addresses whether a catastrophe model is used for underwriting, claims, reserve, reinsurance, capital or parametric product; actuarial approval; model/vendor governance; explanation and complaints; unfair discrimination; contract change; trigger/calculation; outsourcing; record retention and supervisory access.

Community or public data cannot be imported into individual decisions without lawful basis, accuracy and conduct assessment. Mid-event use is explicitly bounded.

### 3.3 Public alerts, disaster and climate mandates

Public-warning authority, emergency declaration, evacuation, county/national functions, plant protection, water, meteorology, forestry, health and infrastructure require a mandate map. Kenya's disaster-management function delineation and Climate Change Act provide relevant national/county context [7], [8]. The platform labels official, modelled and community information and establishes conflict escalation.

### 3.4 Public finance, procurement and financial markets

Contingency funds, credit, insurance, securities or results-based finance require appropriation, debt, procurement, audit, disclosure, market and consumer diligence. The current Disaster Risk Financing Strategy supplies policy context [9]. Vendor and partnership procurement must include data rights, security, continuity, open export and termination assistance.

### 3.5 AI policy and professional standards

Kenya's National AI Strategy 2025–2030 and implementation roadmap provide policy direction [10]. The project tracks current policy and standards as of each gate. It also applies actuarial, engineering, geospatial, cybersecurity and research ethics standards. A strategy document does not displace enacted law or sector regulation.

## 4. Decision-rights matrix

| Output/action | Model/platform role | Decision owner | Mandatory control |
|---|---|---|---|
| official warning | supply derived evidence; display authoritative product | mandated agency | source/status label, discrepancy escalation |
| emergency action | exposure and scenario support | authorised national/county incident structure | human command, action log, review |
| pest control | surveillance/movement support | plant-protection authority | species verification, environmental/safety protocol |
| claim triage | prioritisation recommendation | insurer claims owner | human review, open reporting, complaints |
| claim payment/denial | evidence package only | insurer delegated authority | contract, due process, reason, appeal |
| tariff/product change | portfolio analysis | insurer governance/regulator as applicable | actuarial basis, approved timing, conduct |
| parametric payout | publish independent input if designated | contractual parties | fixed formula, fallback, calculation audit |
| public fund allocation | need/layer analysis | authorised public finance institution | appropriation, equity, procurement, audit |
| credit/investment action | physical scenario | lender/investment committee | separate financial model, review, explanation |
| resilience finance | baseline/outcome evidence | financier/sponsor/authority | additionality, contract, safeguards, verification |

The system denies any request that lacks a named decision owner and legal/contractual basis. Emergency read access is time-limited, logged and reviewed.

## 5. Community participation and redress

Community participation spans problem definition, indicator design, reporting channel, safety, interpretation, governance, benefit and evaluation. Consultation after technical design is inadequate. Pastoral, informal-settlement, disability, language, gender, age and low-connectivity perspectives require deliberate inclusion without treating any group as homogeneous.

Contributors receive clear purpose and safety instructions, acknowledgement, useful return information and accessible rights. Sustained trusted reporters receive training, equipment support and fair compensation where appropriate. No incentive should encourage entry into floodwater, fire zones, unstable slopes or pesticide operations.

The platform offers correction, withdrawal/deletion where applicable, complaint and appeal channels through SMS/voice and in-person routes as well as web. Retaliation and surveillance risks are assessed. Public maps aggregate or obscure sensitive locations. Community evidence used in a consequential institutional process triggers stronger notification and review.

Representation monitoring compares report/sensor coverage with population, vulnerability and geography. Low visibility increases uncertainty and outreach; it never means low risk by default. Benefits—warnings, investment, claims service and finance—are audited for distribution.

## 6. AI and model-risk governance

### 6.1 Model inventory and tiering

The inventory includes perception, NLP, quality, hazard state, vulnerability, loss, trigger-support, prioritisation and monitoring models. Each record names owner, purpose, prohibited uses, inputs, outputs, users, materiality, version, dependencies, validation, approvals, monitoring and retirement.

Models are tiered by consequence, scale, opacity, novelty and substitutability. A public map styling rule is lower risk than a claim-triage or emergency prioritisation model. Higher tiers require independent validation, more frequent review, human challenge and stronger fallback.

### 6.2 Model cards and product cards

A model card documents intended domain, data, architecture, metrics, calibration, subgroup results, limitations, uncertainty, failure modes and change history. A product card adds interpretation, decision owner, timing, refresh, permitted/prohibited use, fallback and user training. Technical excellence cannot compensate for a product with no legitimate decision path.

### 6.3 Human review and challenge

Human review is meaningful only if the reviewer has evidence, time, competence, authority and a usable alternative. Interfaces expose drivers, contradictions, uncertainty and data age. Overrides record reason and outcome; frequent patterned overrides trigger investigation. Review is not a rubber stamp.

### 6.4 Change and retirement

Changes are classified: data/schema, code, weights, threshold, spatial resolution, use or institution. Material changes undergo validation and approval. Emergency fixes are narrow, reversible and retrospectively reviewed. Models retire when performance, data, law, purpose or support no longer suffices; outputs retain reproducibility.

## 7. Security, provenance and continuity

Security design covers identity, least privilege, segmentation, encryption, secrets, secure development, dependency risk, logging, monitoring, backup, recovery and incident response. High-risk raw imagery, identity and portfolio data are segregated. Administrators use strong authentication and controlled break-glass access.

Provenance uses signed ingestion, checksums, immutable version records, model artefact signing and tamper-evident audit. It proves what the system received and produced, not that the real-world observation was true. Supply-chain controls cover devices, edge models, satellite processors and vendors.

Continuity identifies maximum tolerable outage and recovery targets by product. Official warnings are consumed from authoritative channels even if analytical services fail. Edge capture, store-and-forward, cached maps, radio/manual workflows and transparent baselines form the fallback. Disaster exercises include simultaneous power, network, cloud and staffing loss.

Vendor exit requires open schemas, periodic export tests, documentation, source/weights access where contractually appropriate, escrow or continuity arrangements for critical proprietary components, and transition support. No irreplaceable service may be discovered only during an emergency.

## 8. Validation programme

Validation covers data, models, products, decisions and outcomes.

### 8.1 Data validation

Source onboarding tests schema, timing, geometry, unit, quality flags, licence, personal data, coverage bias and failure. Ongoing monitoring checks freshness, drift, duplication and incidents. Point-in-time replay is sampled.

### 8.2 Model validation

Transparent baselines precede challengers. Event, future-time, spatial and source holdouts test transfer and failure. Metrics include calibration, lead time, footprint/intensity/duration skill, tail stability, subgroup performance, latency and resource cost. Independent reviewers examine code, implementation and conceptual fit.

### 8.3 Product and human-factors validation

Users must correctly interpret probability, confidence, official status, time and loss basis. Simulation and tabletop exercises test action under conflicting and missing data. Accessibility, language and workload are measured. A model can pass statistics and fail product validation.

### 8.4 Decision and outcome validation

The programme records whether evidence reached owner, action occurred, timing, override, complaint, finance and outcome. Claims, anticipatory action, public allocation and investment have separate outcome measures. Avoided-loss claims require counterfactual design.

### 8.5 Fairness and data inequality

Performance and benefit are disaggregated using legitimate, privacy-preserving categories. Tests include coverage, false alarms/misses, calibration, triage, complaints and finance. A model with improved aggregate discrimination but worse subgroup calibration fails promotion unless the use and mitigation justify it through explicit review.

## 9. Stage 0 — Mandate and problem definition

**Purpose.** Establish why the capability exists before collecting new data.

**Prerequisites.** Executive sponsors from intended public and institutional users; initial community engagement; legal and ethical scoping; funding for research controls.

**Actions.** Define each bounded use case, user, decision, current process, pain point, acceptable latency, consequence of error and prohibited use. Build the decision-rights matrix. Freeze six in-scope hazards and cascading consequences. Define success and harm measures. Record that the benchmark white paper and actuarial charter are methodological guidance only.

**Outputs.** Programme charter; source-role statement; stakeholder map; prohibited-use list; high-level threat/privacy assessment; preliminary hazard and decision map; funding/accountability plan.

**Owners.** Steering forum with named public, scientific, actuarial, data, community and financial representatives.

**Gate.** Every use has an accountable decision owner and plausible benefit; no unresolved mandate conflict.

**Stop conditions.** The project is being positioned as an unauthorised warning agency; a participant requires unrestricted secondary use; no community/public-interest representation; or no sustainable owner.

## 10. Stage 1 — Data and permissions

**Purpose.** Build an admissible evidence foundation and manual reporting pathway.

**Actions.** Complete the source-to-use register; negotiate agreements; identify controller/processor roles; perform DPIA and security architecture; set licences and retention; implement canonical schemas, time and geometry; establish consent/notice and rights routes; design offline/SMS/voice/manual reporting; define identity separation, raw/derived zones and audit.

Each source undergoes a sample profile for coverage, missingness, latency, calibration, historical changes and representation. Exposure and claims sources receive heightened confidentiality control. Data-sharing agreements name outage and correction responsibilities.

**Outputs.** Approved source register; agreements; DPIA; threat model; data catalogue; schema registry; lineage design; manual forms; community safety/participation protocol; test datasets.

**Owners.** Controllers and source owners, data-protection officer, security lead, stewards and community forum.

**Gate.** A reviewer can trace purpose, legal basis, owner, permitted use, retention and quality for every pilot field. Rights requests and deletion/correction are tested.

**Stop conditions.** Unlawful or disproportionate processing; no safe reporting pathway; location/identity cannot be protected; essential source licence forbids use; or critical historical data cannot support even a baseline.

## 11. Stage 2 — Transparent baselines

**Purpose.** Create reproducible hazard and loss workflows before AI challengers.

**Actions.** Implement peril-specific thresholds or simple models; manual source verification; versioned exposure intersection; simple vulnerability and policy calculators; scenario and uncertainty templates. Reconstruct historical events with point-in-time discipline. Prepare baseline dashboards that distinguish official/modelled information.

Flood baseline uses rainfall/gauge/terrain and manual footprint. Drought uses published indicators and persistence. Fire uses danger and verified detections. Locust uses survey/movement envelope. Landslide uses susceptibility and rainfall thresholds. Storm/heat uses observed/forecast exceedance and persistence.

**Outputs.** Baseline model cards, code and data snapshots; historical performance; manual event-loss report; operator runbook; known gaps.

**Owners.** Hazard scientists and actuarial leads, independently reviewed.

**Gate.** Baselines are reproducible, calibrated as far as evidence permits, operationally interpretable and capable of safe manual operation.

**Stop conditions.** Units or event definitions cannot be reconciled; model performance is misleading; or users cannot interpret the product.

## 12. Stage 3 — Observation pilot in shadow mode

**Purpose.** Test community channels, AI perception and source reliability without consequential automation.

**Actions.** Deploy bounded channels and trained reporter network; add object detection, segmentation, NLP and anomaly challengers; implement deduplication and source-health telemetry; calibrate scores; run edge/cloud failure exercises; monitor privacy, safety and representation.

AI detections queue verification. Operators compare them with baseline evidence; no automatic official, claim or finance action occurs. Contributor feedback explains receipt and status without promising response.

**Outputs.** Observation model cards; calibration and coverage report; duplication graph metrics; false/missed report review; privacy/security incident report; user research; revised safeguards.

**Owners.** Observation product owner, community forum, model owners, data/security officers and independent validator.

**Gate.** Demonstrated incremental coverage or lead time at acceptable false-alarm, latency, subgroup and safety levels; reliable rollback and manual continuation.

**Stop conditions.** Contributor harm; systematic surveillance creep; poor subgroup performance without mitigation; unsafe field behaviour; or AI adds no value over manual/baseline process.

## 13. Stage 4 — Dynamic hazard-state challenger

**Purpose.** Test hierarchical spatial and latent-state models against transparent baselines.

**Actions.** Fit process-specific topology; source emissions; detection/occurrence separation; event identity; intensity/footprint/duration; intervention covariates; uncertainty decomposition. Compare finite, duration-aware, state-space or nonparametric candidates only where justified. Conduct event, spatial, time, source and extreme holdouts.

**Outputs.** Challenger model cards, posterior interface, validation report, compute/latency benchmark, stress tests, operator interpretation and fallback.

**Owners.** Hazard/model teams with independent scientific and statistical review.

**Gate.** Challenger meets pre-agreed calibration, physical plausibility, lead-time, transfer, subgroup, stability and operational thresholds and improves decision-relevant performance.

**Stop conditions.** It fails to outperform baseline; states are unstable/uninterpretable; physical constraints fail; latency is excessive; or uncertainty is understated. The baseline remains champion.

## 14. Stage 5 — Loss-intelligence pilot

**Purpose.** Produce event footprints, exposure at risk and loss ranges without automated financial action.

**Actions.** Build exposure snapshots and quality grades; local vulnerability priors; event-loss simulation; insured/uninsured/fiscal separation; claims-delay nowcasts; OEP/AEP and stress reports; reconciliation; sensitivity and independent actuarial review.

Financial terms use test or approved historical contracts in controlled environments. Personally identifiable exposure is segregated. Synthetic cases test rare combinations and are labelled.

**Outputs.** Canonical loss interface; event report; portfolio and fiscal summaries; uncertainty attribution; historical back-tests; review report; clear non-use statements.

**Owners.** Actuarial model owner, exposure stewards, finance/public owners and independent actuarial validator.

**Gate.** Every quantity has unit, horizon, valuation time, basis, uncertainty and owner; holdout calibration is acceptable for stated use; no output is mistaken for reserve, capital, payout or accounting.

**Stop conditions.** Exposure uncertainty makes granularity misleading; vulnerability has no defensible basis; financial terms cannot be versioned; or users repeatedly misinterpret outputs.

## 15. Stage 6 — Bounded institutional decision pilots

**Purpose.** Test whether intelligence improves real workflows under human authority.

Candidate pilots include claims readiness/triage, road-access verification, anticipatory action targeting, portfolio accumulation monitoring or resilience project prioritisation. Only one or a small number proceed per site so causality and accountability remain observable.

**Actions.** Define product contract, threshold, owner, user training, human review, complaint, override, action log, fallback, outcome metrics and evaluation design. Run tabletop and controlled live use. Independent observers monitor conduct and community effect.

**Outputs.** Decision protocol; product card; training and simulation results; operational/action data; customer/community feedback; outcome and harm report.

**Gate.** Evidence reaches users on time, is interpreted correctly, improves a bounded outcome relative to baseline and causes no unacceptable legal, safety, conduct or equity harm.

**Stop conditions.** Unauthorised use; adverse individual decisions without due process; excessive false alarms/workload; failure to act despite product; or no measurable benefit.

## 16. Stage 7 — Financial-product testing

**Purpose.** Consider parametric or other risk-transfer structures only after independent data and basis-risk validation.

**Actions.** Define insured interest/financial need, trigger, payout, data/calculation/fallback, historical and synthetic basis risk, premium/capital/reinsurance, customer testing, approval path, contract wording, dispute, data continuity and pilot limits. Separate marketing from research.

**Outputs.** Product feasibility and actuarial report; legal/regulatory diligence; basis-risk distribution; operational continuity test; customer disclosure; capital/reinsurance assessment; stop rules.

**Owners.** Licensed/authorised financial institution and regulator as applicable; independent calculation/data roles; actuarial and legal owners.

**Gate.** Full approval, clear value, sustainable economics, tolerable/explained basis risk, tested continuity and fair customer outcomes.

**Stop conditions.** No insurable/financial interest, unaffordable or misleading product, weak trigger continuity, unacceptable basis/conduct risk, missing capacity or approval.

## 17. Stage 8 — Measured multi-hazard scale

**Purpose.** Expand only where evidence supports transportability and community benefit.

**Actions.** Apply readiness score to new hazard/location/institution; repeat data and validation gates; localise language and vulnerability; test interoperability; fund operations and maintenance; publish performance and limitations; conduct periodic post-implementation review.

Scale is modular. Observation channels may transport while hazard models do not. A drought livelihood product does not gain approval because a flood claims pilot worked. Material new uses return to Stage 0/1.

```{.mermaid #fig-6-3 alt="Measured multi-hazard pilot expansion sequence"}
flowchart LR
  READY[Readiness scoring: mandate, data, community, action and validation]
  READY --> FD[Flood and drought contrast pilots]
  FD --> REVIEW1{Evidence and benefit pass?}
  REVIEW1 -- Yes --> WL[Wildfire and locust perception and propagation tests]
  REVIEW1 -- No --> NARROW1[Remain in research, remediate or stop]
  WL --> REVIEW2{Transport and safeguards pass?}
  REVIEW2 -- Yes --> LH[Landslide and storm or heat sparsity and compound tests]
  REVIEW2 -- No --> NARROW2[Narrow or stop]
  LH --> SCALE[Repeat local readiness, validation and authority before scale]
```

**Figure 6.3 — Pilot expansion sequence.** Hazard relevance and evidence, not manuscript order, determine actual progression.

**Outputs.** Expansion dossier; local validation; revised source and model inventory; financing/service plan; community agreement; public transparency report.

**Gate.** Sustained calibration, actionability, rights protection, resilience and financing; independent approval for new scope.

**Stop conditions.** Benefit erodes, drift or inequity persists, operating funds fail, vendor exit is impossible, mandate changes or community harm outweighs benefit.

## 18. Pilot sequencing and readiness score

Flood and drought are initial contrasts, not predetermined locations. A candidate is scored 0–4 on hazard relevance, authoritative data, community partnership, exposure quality, decision owner, actionability, connectivity/manual fallback, validation truth, legal readiness and sustainability. Weights and evidence are published. A high technical score cannot offset a zero in mandate, safety or community legitimacy.

Wildfire and locust follow where surveillance/action partners can test perception and propagation. Landslide and storm/heat follow where local ground truth, infrastructure/health owners and compound-risk relevance exist. Parallel research can continue, but consequential pilots respect capacity.

Pilot design includes comparison geography or workflow where ethical, pre-period baseline, event sample expectations, quantitative and qualitative measures and minimum duration. Rare catastrophes may require multi-season shadow operation; absence of an event is not success or failure.

## 19. Monitoring and safe degradation

An operational dashboard tracks source freshness/coverage, schema errors, model calibration/drift, spatial/subgroup performance, false alarms/misses, latency, compute, user action, override, complaints, privacy/security, trigger basis, claims error and intervention outcomes. Alert thresholds have owners and playbooks.

```{.mermaid #fig-6-4 alt="Monitoring and safe degradation workflow"}
flowchart TB
  MON[Monitoring detects failure or drift] --> CLASS[Classify source, model, product, security or rights incident]
  CLASS --> CONTAIN[Contain affected component]
  CONTAIN --> FALL[Switch to approved baseline, manual or offline fallback]
  FALL --> NOTICE[Notify product and decision owners]
  NOTICE --> DISPLAY[Display degraded status, unavailable components and data age]
  DISPLAY --> RESTORE[Restore service and reconcile missed data]
  RESTORE --> VALIDATE[Validate outputs and affected decisions]
  VALIDATE --> REVIEW[Incident review, corrective action and closure evidence]
  REVIEW -. unresolved high severity .-> CONTAIN
  REVIEW -. closed and verified .-> MON
```

**Figure 6.4 — Monitoring and safe-degradation workflow.** Failure creates a visible fallback state, owner notification and reconciled recovery.

Safe degradation never silently substitutes one meaning for another. A modelled rainfall product cannot replace a contractual gauge unless predefined. A previous official warning remains visible with expiry, not presented as current. Manual procedures are exercised, staffed and supplied.

## 20. Skills, staffing and procurement

Core capability includes programme/product leadership; hydrology, drought/agriculture, fire/ecology, pest, landslide and weather/heat science; remote sensing/geospatial; data/platform/ML engineering; catastrophe modelling and actuarial science; insurance claims/product/reinsurance; public and climate finance; legal/data protection; cybersecurity/continuity; human-centred design/accessibility; community engagement; monitoring/evaluation; and independent validation/editorial communication.

Not every specialist must be permanent, but ownership cannot be outsourced entirely. Knowledge transfer, documentation, paired teams and succession are contractual deliverables. On-call emergency staffing, duty of care and psychological support for distress imagery are planned.

Procurement evaluates open standards, point-in-time reproducibility, data portability, security evidence, domain performance, total lifecycle cost, local support, model transparency, audit rights, outage commitments and exit. Demonstrations on selected data are not accepted as validation. Vendors disclose training/processing constraints and material subcontractors.

## 21. Review forums and definitions of done

| Review | Definition of done |
|---|---|
| scientific | process and assumptions plausible; limitations and comparisons complete |
| actuarial | exposures, terms, distributions, tail, reconciliation and uses defined |
| data/AI | lineage, point-in-time, calibration, drift, subgroup and rollback tested |
| legal/privacy | authority, basis, DPIA, rights, contracts and retention approved |
| security/continuity | threat, access, recovery, incident and vendor exit exercised |
| community | channels safe/accessibile, purpose legitimate, benefit and redress credible |
| operational | trained users act correctly under normal, conflicting and failed data |
| finance | structure, accounting, liquidity, basis/counterparty and approval separated |
| independent | severe findings closed or accepted by authorised body with rationale |

**Table 6.1 — Roles and definitions of done.** No single discipline can close an interdisciplinary stage gate alone.

Review comments enter a validation log with severity, owner, due date, disposition, evidence and affected versions. “Noted” is not closure. High-severity legal, safety, privacy, mathematical or authority issues block the gate.

## 22. Required scenario exercises

Exercises cover all twenty series scenarios: copied misinformation; bad geolocation; satellite/local conflict; stale gauge; remote silence; adverse camera conditions; ambiguous drought onset; border-crossing locust; landslide isolation; heat-drought-fire-power compound; both parametric basis directions; insurer misuse; public/model warning conflict; cloud/vendor outage; rights request; subgroup calibration reversal; challenger loss to baseline; false avoided-loss claim; and expected loss treated as cash.

Each exercise records detection, escalation, responsible decision, communication, fallback, affected people, recovery and learning. At least one exercise removes the cloud and one removes a key institution, because continuity cannot depend on everyone being available. Community participants review whether messages were understandable and safe.

## 23. Post-implementation review

After each event/season and annually, the programme reviews calibration, source changes, actions, harm, finance, cost, availability, complaints and distribution of benefit. It compares pre-specified outcomes with baseline and documents unintended uses. Models and products are renewed, constrained or retired.

Public transparency reports aggregate performance and material incidents without exposing security or personal data. Independent reviews occur at defined intervals and after severe failure. Research publications distinguish retrospective reconstruction, shadow operation and live decision evidence.

Scale decisions consider marginal benefit and operating cost. A capability can remain a successful local service rather than become national. A failed pilot can be a valuable result if stopped safely and documented honestly.

## 24. Limitations

Institutional mandates, law, policy and market conditions evolve. Interagency data sharing can be slow. Rare events delay validation. County capacities differ. Skilled staff and long-term funding are constrained. Community representation is imperfect. Security and privacy risks cannot be eliminated. Vendor and satellite dependencies remain.

The roadmap is a research architecture, not an implementation authorisation, procurement specification, legal opinion or financial-product approval. Exact partners and locations are deliberately unresolved until readiness and authority are verified.

## 25. Governance artefact set

The operating model is implemented through controlled artefacts rather than policy prose alone.

### 25.1 Programme and use-case charters

The programme charter records purpose, hazards, institutions, funding, governance, duration and non-goals. Each use-case charter narrows the user, decision, current process, model role, error consequence, data purposes, metrics and prohibited action. A material change in user or decision creates a new use-case review, even when it reuses the same model endpoint.

### 25.2 Data and processing records

The source-to-use register, data inventory, controller/processor record, DPIA, retention schedule, access matrix and transfer register remain linked. The DPIA is revisited when precise location, public-area camera, claims, health/vulnerable-group data, automated prioritisation or dataset combination changes. Evidence of consultation and mitigations is versioned.

### 25.3 Model and product records

The inventory links model card, validation plan/report, training/data snapshot, code/artefact, change approvals, monitoring and incidents. Product cards link model outputs to user interface, decision rights, training and fallback. A model can serve several products, but each product has separate fitness and permitted-use review.

### 25.4 Operational records

Runbooks cover feed failure, model failure, warning discrepancy, misinformation surge, privacy/security incident, rights request, emergency access, manual fallback and restoration. Decision logs record evidence version, authorised owner, action, override and rationale. After-action reviews distinguish technical, human, institutional and external causes.

### 25.5 Public accountability records

The programme publishes accessible descriptions of purpose, sources by category, safeguards, performance, material limitations, complaints and independent review. It avoids exposing attack surfaces or personal data. Communities receive local-language summaries and opportunities to challenge whether reported benefit matches experience.

## 26. Detailed legal and regulatory question set

Before each pilot, counsel and accountable institutions answer a written diligence set.

**Authority:** Which statute, regulation, delegation, contract or policy permits each collection, model product and action? Which agency's official warning or classification must be preserved? What happens when national and county responsibilities overlap?

**Personal data:** Who determines purpose/means; which lawful basis applies to every source/use; is consent valid and withdrawable; are children, health, biometric or vulnerable-group data involved; is precise geometry necessary; what are rights and response deadlines; are transfers or subcontractors involved; is automated significant decision-making proposed?

**Insurance:** Is the use product design, underwriting, pricing, claims, reserve, capital, reinsurance or marketing? What actuarial/board/regulatory approval applies? Are contract, disclosure, claims reason, complaint and record controls sufficient? Could a source create unfair discrimination or mid-event conduct harm?

**Public finance and procurement:** Who can appropriate, commit, trigger and pay; what audit/procurement/debt rules apply; can funds be used before declaration; how are county/national transfers governed; can an external calculation agent bind the public body; what are transparency requirements?

**Financial markets and investment:** Does a proposed instrument create securities, disclosure, trustee, listing, fiduciary or market-conduct obligations? Are expected loss and cash flow distinguished? Who verifies resilience claims and manages conflicts?

**Hazard and sector mandates:** What rules govern meteorology, water, plant protection/pesticide control, forestry/fire, health, environmental assessment, land use, emergency command and critical infrastructure? A model recommendation never bypasses operational/safety licensing.

**Research and publication:** Is ethical review required; how are participants recruited/compensated; what can be published; how is re-identification controlled; who owns foreground/background IP; can independent reviewers access enough evidence?

Answers include citations and as-of date. “To be confirmed” is a blocking diligence item where it affects authority or rights.

## 27. RACI by lifecycle

The following is a template; named institutions are assigned only after mandate confirmation.

| Lifecycle activity | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|
| approve use/purpose | steering body/controller | programme lead | legal, community, decision owner | partners/public as appropriate |
| onboard source | data-governance body | steward/platform | source, privacy, security, model owner | users |
| develop model | model owner | science/engineering team | domain experts, community where labels/context | validator/product owner |
| validate model | assurance body | independent validator | model owner, operators | governing body |
| approve product | product/decision authority | product owner | model, risk, legal, users | affected users |
| issue official alert | mandated authority | designated operations | platform/scientists | public/institutions |
| make claim/funding decision | contractual/statutory owner | delegated handler/official | evidence specialists | claimant/beneficiary/audit |
| manage incident | risk/security authority | incident commander/team | controllers, source/product owners | affected parties/regulator as required |
| approve scale/retirement | governing body | programme/model/product owners | independent and community forums | all users |

RACI does not dilute statutory accountability. “Consulted” experts may have technical stop criteria. Emergency delegation is documented and time-bound.

## 28. Monitoring metrics and escalation thresholds

### 28.1 Data plane

Metrics include feed availability/freshness, missing intervals, geolocation uncertainty, schema errors, duplicate-root ratio, coverage per target area/population, correction rate, access violations and rights-request completion. Thresholds reflect source cadence. A drought monthly feed and flood minute gauge cannot share one freshness rule.

### 28.2 Model plane

Metrics include calibration, discrimination, interval coverage, footprint/intensity/duration, lead time, abstention, input/output drift, latency, compute failure, model disagreement and subgroup/geographic performance. Delayed truth creates provisional and mature views. Threshold breaches can widen uncertainty, restrict use, revert or suspend.

### 28.3 Product and decision plane

Monitor receipt, user acknowledgement, interpretation tests, action/override, missed deadline, false/missed escalation, claims triage error, settlement, complaints, parametric basis outcomes, funding delay and operational workload. An accurate model whose products are ignored or misunderstood is an operating failure.

### 28.4 Outcome and legitimacy plane

Track coverage/benefit distribution, action reach, service restoration, household/community feedback, safety incidents, misuse, intervention delivery and credible avoided-loss studies. Trust is measured qualitatively and quantitatively without collecting unnecessary identity.

Severity definitions specify containment. A material personal-data or unauthorised-decision incident can suspend a use even if availability/performance is strong. Repeated lower-severity patterns escalate.

## 29. Tabletop and live exercise programme

A quarterly tabletop assigns participants the roles they hold in reality. Inputs arrive at simulated event/knowledge time; facilitators introduce a stale gauge, copied report, cloud outage or official/model conflict. Teams must identify authoritative status, use manual fallback, make/log decisions, communicate uncertainty and process a rights/complaint issue. Observers score time, correctness, escalation and safety.

Technical recovery exercises restore from backups, rotate compromised credentials, reprocess an event and prove output checksums. Vendor-exit exercises export data/model/configuration into an independent environment. Field exercises test store-and-forward, radio/voice and safe capture without exposing participants to hazard.

Live shadow exercises run during real seasons but do not control consequential actions. Operators compare model products with existing procedures and log hypothetical decisions. If a bounded live pilot begins, there is an incident commander, rollback trigger and independent observer. Communications clearly distinguish pilot evidence from official instructions.

Exercises end with an after-action report: expected behaviour, actual behaviour, root causes, owners, dates and evidence of closure. A repeated unresolved high-severity issue blocks scale.

## 30. Staffing and service design in practice

The programme needs a small accountable core and federated domain teams. The core includes programme/product, platform/data, geospatial, model risk, security/continuity, privacy/legal, actuarial/loss, monitoring/evaluation and community/accessibility leadership. Domain cells add the relevant Kenyan institutional scientists and field partners per hazard. Financial users maintain their own product/claims/investment owners.

An on-call rota covers event operations with escalation and maximum hours. Roles handling distress media receive restricted exposure, tooling and wellbeing support. Communities are not unpaid standby labour. Training includes probabilistic communication, data rights, safety, manual procedures and institutional boundaries.

Service levels name hours, update cadence, maximum data age, expected restoration and support. Higher availability costs are justified by action deadlines. Research services may be business-hours and clearly non-operational; a live warning-support feed requires stronger continuity. Funding includes maintenance, calibration, field networks, security, independent review and exit—not only development.

## 31. Procurement evaluation scorecard

Procurement uses weighted evidence: functional fit; hazard/domain validation; interoperability/open schema; point-in-time and lineage; security/privacy; resilience/offline; model transparency and audit; local support/knowledge transfer; accessibility; lifecycle cost; data/IP/exit; and demonstrated conduct safeguards. Mandatory failures—unexportable data, no security disclosure, no correction/audit, hidden secondary use—cannot be offset by feature scores.

Bid evaluations use representative, governed test cases and failure scenarios. Vendor-provided benchmark results are leads, not acceptance. Contracts include service measurement, incident notification, vulnerability remediation, subcontractor control, model/data change notice, audit, assistance at termination and return/deletion certification.

Open-source components also require ownership, maintenance, licence and supply-chain controls. Avoiding a vendor does not avoid operational responsibility.

## 32. Research and authoring-to-operation handoff

The manuscripts, notation, evidence ledger and registers become inputs to Stage 0, not requirements frozen forever. The implementation team converts research propositions into use-case requirements and opens unresolved diligence. Every empirical or legal claim is refreshed to the pilot as-of date. Synthetic examples are excluded from calibration.

Independent reviewers confirm that the original two project notes were expanded without importing the charter's motor/credit/telematics subject or the benchmark's gig-driver and capital mechanics. California wildfire examples remain comparative concepts only. Any later change that reintroduces excluded scope receives explicit approval rather than being smuggled through a data source.

## 33. Programme-level stop and exit plan

The programme stops or narrows if mandate disappears, benefits cannot be demonstrated, rights/safety harm persists, critical data become unavailable, model uncertainty makes products misleading, funding cannot maintain minimum service, or an institution uses outputs beyond approved purpose. A pause can retain research data where lawful while disabling products.

Exit notifies users and contributors, preserves official alternatives, settles contractual obligations, exports and archives reproducibility records, returns/deletes data, revokes access, retires models/endpoints and publishes a proportionate explanation. Financial products require run-off/claims continuity independent of platform research. Community reporting routes are not withdrawn during an active emergency without a safe substitute.

Success can also trigger transition: a validated service may move to a mandated institution under documented handover, staffing, budget and assurance. The research programme then monitors or closes rather than retaining ambiguous authority.

## 34. Eighteen-week research-to-pilot preparation schedule

This schedule prepares a controlled research package; it does not compress deployment approval into eighteen weeks.

### Weeks 1–3: mandate and evidence refresh

The steering group confirms use cases, owners and prohibited uses. Legal researchers refresh every time-sensitive Kenyan claim and complete the mandate map. Data stewards inventory candidate sources and sample their quality. Community partners review problem statements, channels and benefit. The technical team converts manuscript interfaces into test schemas. Deliverables are signed charters, diligence register, readiness longlist and updated evidence ledger.

### Weeks 4–6: permissions and baselines

Controllers agree roles and DPIA; security designs trust boundaries; source agreements and retention are drafted. Hazard teams implement/reproduce transparent baselines and historical point-in-time event frames. Actuaries build a manual exposure/vulnerability/loss workbook or service with defined quantities. Operators write manual runbooks. Gate review rejects any use lacking safe data or an interpretable baseline.

### Weeks 7–9: observation prototype

One or two bounded channels are prototyped with consent, offline capture and contributor safety. AI perception challengers run on held-out/local samples; deduplication and source health are tested. No consequential action follows. Field/user research measures interpretation, accessibility and reporting burden. Security and rights workflows are exercised.

### Weeks 10–12: hazard challenger and loss interface

The modelling team fits only candidates justified by the evidence. Complete-event, spatial and source holdouts compare baseline/challenger. Posterior output drives a synthetic or historical loss run. Independent hazard and actuarial reviewers test the observation-state-loss chain. The product team builds a dashboard/report clearly separating official/modelled status.

### Weeks 13–15: institutional simulation

Claims, county operations, public finance or resilience users run tabletop cases using fixed historical/synthetic evidence. They make and log decisions through existing authority. Community/public-interest reviewers inspect messages and distribution. Continuity exercises remove cloud/source. Findings produce product revisions and stop conditions.

### Weeks 16–18: independent gate and next-stage recommendation

Legal/privacy/security, scientific, actuarial, operational and community reviews close or block findings. The programme publishes a research report with performance, failures, unresolved evidence and a recommendation: stop, continue shadow, narrow, collect data or seek authority for a bounded pilot. No default progression exists.

## 35. Stage-gate evidence dossier template

Each gate dossier has an executive decision, scope/version, evidence since prior gate, requirements, results, incidents, open findings, risk acceptance, independent opinions, community response, resources and recommendation. Appendices contain source/model/product records and reproducibility artefacts.

Gate decisions are `pass for named next scope`, `conditional pass with dated restrictions`, `remain in stage`, `narrow`, or `stop`. A pass does not approve uses beyond its wording. Conditions have owners and cannot remain indefinitely. Dissenting independent/community opinions are preserved rather than summarised away.

For model promotion, the dossier includes baseline comparison, calibration/lead/tail/subgroup, physical plausibility, latency/cost, operator comprehension, fallback and model-change impact. For decision pilot, it adds authority, human review, complaints, action/outcome and harm. For product testing, it adds actuarial/legal/regulatory/capital, trigger basis and customer research.

## 36. Safety scenario expected controls

The copied-report exercise passes when records cluster to one lineage, corroboration does not inflate, the candidate is routed for verification and no contributor is publicly accused. Bad geolocation passes when uncertainty remains, correction works and decisions avoid false precision. Satellite/local contradiction passes when acquisition/method are compared, both remain visible and a domain owner resolves or retains uncertainty.

A stale gauge exercise passes when freshness alarms, state uncertainty widens, fallback follows predefined hierarchy and the product displays degradation. Remote silence passes when coverage audit raises missingness, field/manual alternatives activate and finance/risk is not lowered. Poor-camera conditions pass when model abstains/downweights and human/other sources continue.

Ambiguous drought onset passes when component state and institutional stage stay separate. Locust boundary crossing passes when event identity persists and authorities coordinate. Landslide isolation passes when offline/radio/manual work. Compound heat-fire-power passes when shared dependencies and separate owners are visible.

Both parametric basis cases pass when contractual result is calculated exactly, local loss evidence is preserved, explanation/dispute route works and no retroactive trigger change occurs. Insurer misuse passes when access/use control blocks or records/escalates it. Official/model warning conflict passes when the official product remains unambiguous.

Cloud/vendor outage passes when fallback meets minimum service and recovery/reconciliation succeeds. Rights request passes when identity, lineage, lawful action and downstream notification are completed. Subgroup calibration reversal and challenger baseline loss pass when promotion stops. Avoided-loss and financing-cash errors pass when reviewers reject the claim and correct language/analysis.

## 37. Independent review commissioning

Terms of reference give reviewers full scope, evidence access, independence/conflict declaration, methods, deliverables and direct reporting route. Hydrology, drought/agriculture, fire/ecology, pest, landslide/weather/heat, remote sensing/AI, actuarial/reinsurance, insurance operations, investment/climate finance, Kenyan law/privacy/public administration, security and community/accessibility perspectives are covered.

Reviewers distinguish fatal flaw, high, medium, low and advisory. Management responds with accept/remediate/dispute plus evidence. Only the authorised assurance body accepts residual high risk; legal/authority/safety blockers may not be accepted by project convenience. Reviewer inability to access proprietary material is a limitation and can block high-impact use.

Independent editorial/mathematical review checks notation, dimensional consistency, citations and cross-document claims. Community review is compensated and accessible, and its conclusions are not reduced to user-interface preferences.

## 38. Sustainability and financing of the capability

The operating budget covers data agreements, field networks, devices, communications, compute/storage, staff/on-call, calibration/maintenance, security, privacy/rights, user support, independent validation, exercises and vendor exit. Capital grant funding without recurrent commitment is insufficient for an emergency service.

A mixed funding model can separate public-interest observation/warning support from commercial portfolio analytics. Cross-subsidy and access rules are transparent so commercial withdrawal does not switch off public safety. Data contributors are not paid through opaque incentives tied to hazard severity. Procurement forecasts lifecycle and currency risk.

Value measurement includes estimation/lead/action outcomes, avoided loss where credible, operational cost, public benefit and rights/safety. If benefits accrue across institutions, a cost-sharing governance model may be appropriate. No participant buys institutional authority through funding.

## 39. Final definition of operational readiness

Operational readiness exists only for a named hazard, geography, product, decision and period when mandate and data rights are current; authoritative relationships are agreed; sources and fallback meet service; models beat/meet baseline and are validated; outputs are interpretable; users are trained; human challenge/redress operate; security/continuity are exercised; funding/staffing sustain service; community participation is legitimate; and independent blockers are closed.

Readiness expires. Material data/model/use/legal changes, severe incident or prolonged performance breach trigger reassessment. “National platform ready” is not a meaningful blanket state.

## 40. Stage owner and evidence summary

| Stage | Accountable owner | Minimum evidence | Primary deliverable | Hard stop example |
|---|---|---|---|---|
| 0 mandate | steering/decision authorities | mandate, need, participation | charters and prohibited uses | no lawful decision owner |
| 1 data | controllers/data governance | basis, quality, DPIA, agreements | governed observation foundation | disproportionate processing |
| 2 baseline | hazard/actuarial owners | point-in-time hindcast | reproducible manual baseline | undefined units/event/loss |
| 3 observation | product/community/model owners | shadow calibration/coverage/safety | admissible multimodal observations | contributor harm/no added value |
| 4 state | hazard model owner | baseline comparison/holdouts | posterior hazard interface | physically implausible/loses baseline |
| 5 loss | actuarial owner | exposure/vulnerability/terms validation | loss distributions/reconciliation | misleading granularity/undefined quantity |
| 6 decision | institutional decision owner | simulation/live bounded outcome | approved product workflow | unauthorised/adverse automation |
| 7 finance | licensed/statutory owner | product, basis, continuity, approval | bounded financial mechanism | unfair/unaffordable/unapproved |
| 8 scale | governing body/local owners | transport and sustained benefit | expansion dossier | inequity, drift or unsustainable service |

**Figure 6.2 — Research-to-operation stage gates (table-form conceptual figure).** Every stage has an owner, evidence package, deliverable and hard stop.

The accountable owner cannot delegate the decision to the platform vendor. Independent validators provide conclusions directly to the gate authority. Community/public-interest review is evidence, not ceremonial attendance.

## 41. Implementation deliverable catalogue

The technical package includes source adapters, schema registry, identity separation, lineage and point-in-time store, source health, baseline and challenger models, event catalogue, exposure/loss engine, purpose-specific product interfaces, monitoring and reproducible deployment/fallback. Documentation includes data/model/product cards, runbooks, architecture/threat, test cases and recovery.

The institutional package includes mandates and agreements, DPIA/notices/rights, decision matrix, product/financial approvals, claims/public-finance procedures, community protocols, training, complaints, procurement/vendor exit and public transparency. The evaluation package includes pre-registration, historical/shadow/live evidence, action logs, independent review, safety exercises and outcome/counterfactual plan.

A deliverable is done only when its owner, version, approval, test evidence, retention and review/expiry are recorded. Software completion alone is not stage completion.

## 42. Communication during uncertainty and conflict

Operational communications state source, issuer, issue/expiry, location/horizon, official/model/community status, confidence/uncertainty, actionable guidance and contact. They avoid probabilistic jargon without explanation. Translations are reviewed for negation, urgency and place.

When model and authority disagree, the platform displays the authoritative message unchanged, labels its own estimate and routes discrepancy to named scientific/operations owners. Public channels never create competing unlabeled colours. When data fail, messages say what is unavailable and which fallback informs guidance.

Financial communications state contractual result separately from experienced loss. A non-triggered payout does not deny catastrophe impact. Claim/customer/public reasons and appeal routes remain available. Internal model disagreements are documented before an authorised owner decides.

## 43. Ethical research safeguards

Research recruitment minimises coercion, especially where agencies/insurers provide essential services. Consent distinguishes research from emergency assistance, claims and public benefits. Refusal does not affect entitlement. Compensation reflects time/cost without rewarding severe reports. Publication protects identity and sensitive sites.

The team anticipates dual use: cameras/location can enable surveillance; fraud tools can suppress genuine claims; risk maps can stigmatise neighbourhoods; investment screening can withdraw capital. Prohibited uses and access/aggregation counter these risks, while an ethics/community forum can suspend data collection.

Researchers report negative findings and incidents. Synthetic examples are labelled; exploratory results are not operational claims. Independent community feedback can remain dissenting in the final report.

## 44. Synthetic readiness comparison

Assume three fictional candidates: an urban flood area with strong rainfall data but incomplete drainage/exposure; a pastoral drought area with mature institutional indicators but sparse connectivity; and a landslide corridor with high consequence but few verified events. The readiness panel scores evidence, mandate, community partnership, action, fallback and validation—not only hazard severity.

The flood candidate may proceed to observation shadow mode if county/KMD/WRA relationships, manual workflow and contributor protections are established. It cannot proceed to property-level financial decisions because exposure/geocoding are weak. Its first product is broad footprint, road-access verification and aggregate claims-readiness.

The drought candidate may score strongly on authoritative process and need but require offline/trusted reporting and multi-season evaluation. Its first product can compare component state and action targeting while NDMA classification remains authoritative. A financial product is not assumed.

The landslide candidate may remain baseline/research because sparse labels prevent calibrated probabilities. It can still improve rainfall/susceptibility screening, field protocol and road contingency. High consequence justifies precaution and data investment, not false precision.

The governing body records why one candidate advances and another remains in research. A lower total numeric score with a zero in legal authority or participant safety cannot advance. Scores are refreshed; readiness can decline when a source, partner or funding disappears.

## 45. First-year operating review agenda

Monthly review covers source health, rights/incidents, model/product performance, user actions and backlog. Seasonal review covers complete-event calibration, representation, community experience, cost and staff/vendor capacity. Annual independent review examines mandates, DPIA/security, model inventory, outcomes, financial/public use and whether benefits justify continuation.

The governing body must answer: Did the system add independent information? Did it reach authorised users before deadlines? Which actions changed? Who benefited or was missed? Were official, model and contract boundaries maintained? Did fallback work? Which uncertainty is worth reducing? Which use should stop?

The review publishes a proportionate transparency summary and updates every gate condition. Scale is a decision supported by this evidence, not a reward for completing the software roadmap.

## 46. Conclusion

Governance makes catastrophe intelligence useful by defining who can use what evidence for which decision, under what safeguards, and what happens when the system is wrong or unavailable. The staged programme begins with mandate and rights, proves transparent baselines, tests AI and state challengers in shadow mode, introduces loss intelligence without financial automation, and permits bounded decisions or products only after independent evidence.

The implementation is successful only if all six hazards retain scientific integrity, communities receive benefit and redress, institutional authority remains intact, financial quantities remain defined, failure modes are survivable and measured outcomes justify scale. Publication of this series satisfies none of those gates by itself; it provides the common specification against which future proposals can be challenged.

## References

[1] Republic of Kenya, *Data Protection Act*, No. 24 of 2019. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24

[2] Republic of Kenya, *Data Protection (General) Regulations*, Legal Notice No. 263 of 2021. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng%402022-12-31

[3] Insurance Regulatory Authority, *Insurance (Insurance Products) Guidelines, 2022*. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3641/eng%402022-03-29/source

[4] Insurance Regulatory Authority, *Insurance (Claims Management) Guidelines, 2022*. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3638/eng%402022-03-29

[5] Insurance Regulatory Authority, *Insurance (Market Conduct) Guidelines, 2022*. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3642/eng%402022-03-29

[6] Insurance Regulatory Authority, *Insurance (Risk Management and Control Functions) Guidelines, 2022*. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3643/eng%402022-03-29

[7] Republic of Kenya, *Delineation of Disaster Management Functions*, Legal Notice No. 86 of 2021, rev. 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2021/86/eng%402022-12-31

[8] Republic of Kenya, *Climate Change Act*, No. 11 of 2016, rev. 2023. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2016/11/eng%402023-09-15

[9] National Treasury and Economic Planning, *Kenya Disaster Risk Financing Strategy 2026–2030*, 2026. [Online]. Available: https://www.treasury.go.ke/sites/default/files/Latest%20updates/Kenya%20Disaster%20Risk%20Financing%20Strategy%202026%20-%202030.pdf

[10] Ministry of Information, Communications and the Digital Economy, “Kenya AI Strategy 2025–2030,” accessed Aug. 26, 2026. [Online]. Available: https://www.ict.go.ke/node/641
