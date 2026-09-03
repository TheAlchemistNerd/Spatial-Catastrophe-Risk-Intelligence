# Kenya's Multi-Hazard Catastrophe Intelligence and Financial-Resilience Thesis

## Abstract

Kenya's catastrophes are usually described by peril: flood, drought, wildfire, locust infestation, landslide, severe storm or extreme heat. Households, firms and public institutions experience them differently. A single event may simultaneously become a loss of life, a damaged road, a failed harvest, a business interruption, an insurance claim, a deterioration in loan performance, an emergency budget requirement and a reason to defer investment. The central problem is therefore not simply forecasting a physical hazard. It is creating a governed chain of evidence from observation to action while preserving the distinct authority of scientific agencies, county and national government, insurers, investors, financiers and communities.

This paper proposes a Kenya-first multi-hazard catastrophe intelligence capability that fuses authoritative observations, earth observation, environmental sensors, crowd intelligence, institutional records and historical loss experience. The capability estimates an evolving hazard state, intersects it with exposure and vulnerability, produces uncertainty-bearing loss distributions and prepares institution-specific decision products. It treats artificial intelligence as a collection of perception, classification, forecasting and fusion methods, not as an autonomous decision maker. It also distinguishes the value of better estimation from the stronger claim that information changes loss by enabling earlier action.

Flood and drought are the principal contrast cases: one can emerge quickly through connected catchments and drainage systems; the other accumulates over seasons through rainfall, vegetation, water, market and livelihood conditions. Wildfire, locust, landslide, severe storm and heat test whether the architecture transports across fire, mobile biological, geotechnical and atmospheric processes. The thesis is that a shared evidence infrastructure is feasible, but a universal hazard model or risk score is not. Common governance, provenance, interfaces and financial vocabulary must coexist with hazard-specific physics, vulnerability and decision rules.

**Master research question.** How can real-time crowd intelligence, artificial intelligence, earth observation, environmental sensors, institutional records and historical loss experience be fused to estimate evolving climate and ecological catastrophe regimes and their financial consequences across Kenya; how can that information reduce uncertainty and enable earlier loss-reducing action; and how can governed outputs support insurance, investment, public finance and climate-resilience finance without confusing model evidence with contractual or institutional authority?

## 1. One catastrophe, several balance sheets

Consider a household beside an urban watercourse after intense rainfall. Water enters the dwelling, interrupts electricity and prevents a wage earner from reaching work. The same water closes a county road, reduces customer access to a small business, damages an insurer's covered motor and property portfolio, impairs collateral at a lender and forces government to redirect crews and emergency funds. A health facility may remain physically undamaged yet lose access, supplies or cooling. The event is one physical process but not one financial quantity.

Now consider a pastoral household during a prolonged rainfall deficit. No single day necessarily declares the catastrophe. Pasture condition weakens; journeys to water become longer; livestock body condition and market prices deteriorate; school attendance and nutrition may be affected; and distressed sales change future earning capacity. The insurer, humanitarian agency, county department, bank and household need different indicators and act at different thresholds. A satellite vegetation anomaly may be useful evidence, but it is not itself a declaration, a claim or a payout instruction.

These examples reveal three coordination gaps. First, evidence is fragmented across agencies, sensors, communities and portfolios. Second, physical observations are often translated into consequences too late, inconsistently or without an explicit uncertainty trail. Third, the authority to act is easily blurred when a technically impressive model output is presented as if it were a public warning, contractual trigger or public-spending decision.

Kenya already has important pieces of the observation system. The Kenya Meteorological Department (KMD) publishes weather forecasts, warnings, county products and flood bulletins [1]. The Water Resources Authority (WRA) describes hydrological monitoring, flood and drought forecasting and an upgraded real-time network [2]. The National Drought Management Authority (NDMA) operates a drought early-warning system that combines biophysical and socioeconomic indicators and communicates staged drought status [3]. Plant-protection institutions conduct pest surveillance [4], while the Kenya Forest Service has a mandate for forest protection that includes fire [5]. These institutions should not be displaced by a new platform. The architecture should make their evidence more interoperable and make the chain from evidence to consequence more transparent.

The proposed capability is therefore an institutional coordination layer as much as a technical platform. It should answer, at a stated valuation time:

- What is known about the hazard, where and with what uncertainty?
- Which people, assets, services, livelihoods and financial portfolios are exposed?
- How vulnerable are they, and what response capacity is available?
- What range of direct, indirect, insured, uninsured and fiscal loss is plausible?
- Which actions are available, who owns them and what evidence is sufficient?
- What failed, arrived late or remains unknown?

## 2. Risk as an evolving state, not a static score

The Intergovernmental Panel on Climate Change frames risk as arising from interactions among hazard, exposure and vulnerability [6]. For operational catastrophe intelligence, response capacity and time must also be explicit. A useful representation is

\[
L_t = \mathcal{F}(H_t, E_t, V_t, R_t, A_t; \Theta, \mathcal{I}_t),
\]

where \(H_t\) is the hazard state; \(E_t\) the exposure snapshot; \(V_t\) vulnerability; \(R_t\) response capacity; \(A_t\) actions already taken; \(\Theta\) model parameters; and \(\mathcal{I}_t\) information legally and operationally available by time \(t\). The output \(L_t\) is a distribution, not a single certain loss.

This formulation prevents several common errors. A severe hazard need not cause a severe financial loss where exposure is low or protection is effective. A modest hazard can cause catastrophic household consequences where vulnerability is high. A more accurate current-event footprint does not automatically change a long-term tariff. And an absence of mobile reports may reflect weak connectivity rather than an absence of loss.

Static maps remain useful for planning, but they are insufficient for rapidly evolving or cumulative conditions. Exposure changes with settlement, land use, crop stage, market activity and infrastructure condition. Vulnerability changes with maintenance, soil saturation, household reserves, previous shocks and response readiness. Observation quality changes during the event itself. The architecture must preserve the exposure version, event time, knowledge time and valuation time behind every estimate.

### 2.1 Occurrence, detection, impact and loss

Catastrophe occurrence and catastrophe detection are different random processes. Let \(O_{g,t,h}\) indicate whether hazard \(h\) occurs in grid or network unit \(g\) at time \(t\), and let \(D_{s,g,t,h}\) indicate whether source \(s\) detects it. Then

\[
P(D=1) = P(D=1\mid O=1)P(O=1)+P(D=1\mid O=0)P(O=0).
\]

The first conditional term is sensitivity; the second is a false-positive rate. A copied social-media claim can increase the number of posts without increasing independent evidence. A failed gauge can reduce detection without reducing the flood. Smoke, darkness or cloud can degrade one sensor while leaving another informative. Therefore the platform models source-specific observation processes instead of treating every record as a direct measurement of truth.

After occurrence, intensity, footprint, duration and recovery still vary. Physical impact depends on the intersection with exposure and vulnerability. Financial loss then depends on valuation conventions and, for insurance, policy terms. The causal sequence is:

```{.mermaid #fig-1-2 alt="Occurrence-to-decision catastrophe causal chain"}
flowchart TB
  ENV[Physical and social environment] --> OBS[Multimodal observations]
  OBS --> STATE[Inferred hazard state]
  STATE --> EVENT[Occurrence intensity footprint and duration]
  EVENT --> EXPO[Exposure vulnerability and response capacity]
  EXPO --> IMPACT[Physical and social impact]
  IMPACT --> LOSS[Economic and financial loss distributions]
  LOSS --> RULES[Contractual fiscal and investment interpretation]
  RULES --> DECISION[Institution owned decision]
  DECISION --> AUDIT[Action outcome and audit evidence]
```

**Figure 1.2 — Occurrence-to-decision causal chain (conceptual).** Each arrow is an auditable inference, financial transformation or authorised decision; the diagram is not an empirical model.

Each arrow is a model, rule or decision that must be named. No arrow may be hidden inside a generic "AI risk score."

## 3. Crowd intelligence as a distributed, unequal sensor network

People encounter conditions that formal networks cannot observe everywhere: water crossing a road, a blocked drain, livestock concentrating around a failing borehole, smoke behind a ridge, pests changing direction, a new slope crack, an overheated classroom or an inaccessible clinic. Community reports can improve spatial coverage, provide photographs and narrative context, and reveal consequences before they enter administrative or claims systems.

Yet a crowd is not automatically wise. Participation is spatially and socially unequal. Reports may be stale, mistaken, coordinated, copied or strategically manipulated. Images can be recycled from earlier events. A location may be inferred from a mobile tower rather than measured at the scene. Trusted local knowledge can also contradict a remote-sensing classification for good reasons: canopy, terrain, cloud, revisit time or the difference between surface appearance and experienced impact.

The correct abstraction is a distributed sensor network with heterogeneous reliability. Each report needs provenance, event time, geometry, observed variable, confidence, permitted use and a duplication cluster. Reporter history can inform a reliability prior, but identity and reputation must not become a permanent social score. Reliability should be source- and task-specific: a transport operator may be highly informative about road passability but not water depth; a pastoralist may observe grazing conditions better than a coarse satellite cell; a camera model may detect flame better in daylight than smoke at night.

Corroboration must reflect conditional independence. Ten reposts of one photograph are one evidentiary lineage. Three independently captured images, a gauge rise and a radar footprint are stronger because their failure modes differ. A practical fusion model therefore estimates both quality \(q_s\) and dependence among sources. Sparse participation is missingness, not negative evidence.

## 4. Artificial intelligence has bounded roles

In this architecture, artificial intelligence comprises bounded analytical functions:

1. **Perception:** object detection locates people, vehicles, smoke, flame, pests or damage indicators; segmentation estimates water, burn scar, damaged roof or stressed vegetation area.
2. **Language processing:** multilingual and code-switched messages are classified, geolocated where possible and converted into candidate structured observations.
3. **Time-series analysis:** anomaly and forecasting models identify unusual gauge, rainfall, temperature, soil-moisture or vegetation behaviour.
4. **Fusion and state estimation:** probabilistic models reconcile heterogeneous observations with physical and spatial constraints.
5. **Loss analytics:** statistical and actuarial models connect hazard intensity to vulnerability and financial terms.
6. **Quality control:** models identify duplicates, improbable coordinates, manipulated imagery and distribution drift for human review.

YOLO and related object detectors occupy only the first role. A bounding box around smoke is neither proof of ignition time nor a fire-spread forecast. A detected vehicle in water does not estimate the entire flood footprint, the vehicle's repair cost or policy liability. Segmentation is generally more appropriate for continuous surfaces; process or state models are needed for propagation; actuarial models are needed for loss.

AI outputs must retain model version, input lineage, confidence, uncertainty and known limitations. Confidence scores often are not calibrated probabilities and can shift across device types, regions, seasons and weather conditions. Consequential actions need explicit human and institutional review. Kenya's Data Protection Act regulates solely automated decisions that significantly affect a person and provides safeguards including notification and reconsideration [7]. The observation architecture should therefore minimise personal data and avoid using visual or location data for unrelated surveillance.

## 5. The canonical multi-hazard architecture

The shared architecture contains seven layers.

### 5.1 Physical and social environment

The real system includes atmosphere, catchments, soils, vegetation, slopes, pests, built infrastructure, markets, households and response organisations. Models are partial representations of this system. They do not create the hazard state they estimate.

### 5.2 Observation and ingestion

Authoritative sensors, earth observation, community reports, claims and institutional records enter through source-specific interfaces. Every record preserves event time, knowledge time and ingestion time. Corrections create a new version linked to the predecessor rather than silently overwriting history.

### 5.3 Validation and provenance

Validation covers calibration, plausible units, location, duplication, manipulation, timeliness, consent and permitted use. The result is an admissible observation with uncertainty—not a declaration of truth.

### 5.4 Dynamic hazard state

The platform estimates physical or latent variables appropriate to each peril. Flood state may include depth, extent, velocity and duration. Drought state includes rainfall anomaly, soil moisture, vegetation, water access and duration. Fire includes ignition likelihood, perimeter, intensity, fuel and spread direction. Locust includes lifecycle stage, density, direction and crop intersection. Landslide includes slope saturation, susceptibility, deformation and blockage. Storm and heat include rainfall, wind, hail, temperature, humidity and persistence.

### 5.5 Exposure, vulnerability and response

An event footprint is intersected with time-versioned people, buildings, infrastructure, crops, livestock, businesses, ecosystems, insured assets and public services. Vulnerability functions reflect construction, crop stage, condition, livelihood dependence and protective measures. Response capacity and actual intervention records remain separate inputs.

### 5.6 Loss intelligence

The loss engine produces distributions for ground-up physical damage, business interruption, insured loss, uninsured loss and fiscal consequences. It creates event loss tables, annual simulations, exceedance curves and scenario comparisons. Financial terms are applied by version and jurisdiction.

### 5.7 Decision products and authority

Each institution receives an output fit for its mandate. KMD or another authorised agency owns official warnings within its mandate; an insurer owns claims decisions under contracts and regulation; government owns emergency declarations and public allocations; an investor owns diligence and capital allocation; a development financier owns eligibility and results-based payment. The platform records the evidence and decision without impersonating the owner.

```{.mermaid #fig-1-1 alt="End-to-end Kenya multi-hazard catastrophe intelligence architecture"}
flowchart TB
  subgraph SOURCES[Evidence sources]
    A[KMD, WRA, NDMA, PP&FSD and KFS]
    B[Earth observation and environmental sensors]
    C[Communities and trusted field networks]
    D[Exposure, claims and institutional records]
  end
  A --> V[Validation, provenance, duplication control and uncertainty]
  B --> V
  C --> V
  D --> V
  V --> H[Dynamic hazard-specific state]
  H --> X[Exposure, vulnerability and response capacity]
  X --> L[Physical, insured, uninsured and fiscal loss distributions]
  L --> I[Insurance and reinsurance]
  L --> N[Investment and lending]
  L --> P[Public disaster-risk finance]
  L --> R[Climate-resilience finance]
  I --> G[Separately authorised decisions, actions and audit]
  N --> G
  P --> G
  R --> G
```

**Figure 1.1 — End-to-end Kenya multi-hazard catastrophe-intelligence architecture (conceptual).** Shared evidence and state estimation feed purpose-specific financial views without transferring institutional authority.

## 6. Six hazards, one evidence discipline

Common interfaces should not be mistaken for common physics. The architecture transports by preserving the same questions—what was observed, what state is inferred, what is exposed, how vulnerable is it, what loss follows, and who can act—while changing the state equations and data-generating assumptions.

| Hazard | Operational state | Dominant time/space issue | Consequence emphasis |
|---|---|---|---|
| Flood | depth, extent, velocity, duration, river/drainage state | rapid onset; directed upstream/downstream and urban flow | asset damage, displacement, access, claims, fiscal response |
| Drought | rainfall deficit, soil moisture, vegetation, water, duration | slow onset; cumulative and threshold-ambiguous | yield/livestock/livelihood loss, food and credit stress |
| Wildfire | ignition, fuel, smoke, flame, perimeter, intensity, spread | detection versus ignition; rare extreme propagation | ecosystem, property, health, infrastructure and suppression loss |
| Locust/pests | lifecycle, density, location, movement, crop stage | mobile biological process crossing boundaries | crop loss, food-system and control costs |
| Landslide | susceptibility, saturation, deformation, movement | highly local thresholds and sparse labels | mortality, property, road blockage and service isolation |
| Storm/heat | rain, wind, hail, temperature, humidity, persistence | compound effects and spatial inequality | roofs, crops, health, productivity, grids and cooling |

**Table 1.1 — Multi-hazard comparison.** The common interface preserves distinct physical state, topology, timing and consequence.

Flood and drought are valuable anchors because their contrast prevents the platform from becoming a rapid-event system disguised as multi-hazard. Locust prevents administrative borders from defining event motion. Landslide tests whether a national platform can respect metre-to-hillslope-scale vulnerability. Heat tests whether a visually dramatic footprint is necessary for serious loss. Wildfire tests detection, spread and intervention effects.

## 7. Compound and cascading risk

Peril catalogues are administrative conveniences. Real losses cross them. Prolonged drought can reduce vegetation moisture and increase fire potential; heat can raise power demand while lowering worker productivity; an intense storm can trigger flooding and rainfall-induced landslides; floodwater can interrupt sanitation, healthcare and transport; drought and vegetation conditions can shape locust breeding and food-system vulnerability. Infrastructure networks transmit effects far beyond the initial footprint.

The platform therefore needs both event objects and consequence graphs. An event object records the peril, time, footprint, intensity and lineage. A consequence graph connects affected nodes—road, substation, water plant, clinic, market, household, insured location—through physical, service, financial and social dependencies. This does not mean every indirect effect can be valued in real time. It means the system records the mechanism and uncertainty instead of summing unlike quantities without attribution.

For two hazards \(H_1\) and \(H_2\), compound loss generally is not

\[
L(H_1,H_2)=L(H_1)+L(H_2).
\]

Saturated soil may make storm damage nonlinear; prior drought may reduce household reserves; a power failure can amplify heat mortality; a blocked road can lengthen restoration. Interaction terms must be estimated from evidence or represented as scenarios. Where evidence is weak, the platform reports a range and dependence assumption rather than inventing precision.

Cascades also create ownership questions. A physical agency may estimate a hazard while a utility assesses service restoration, a health authority interprets health consequences and Treasury assesses liquidity. The shared platform can carry linked identifiers and timestamps; it should not collapse expert interpretation into one organisation.

## 8. From value of information to value of action

Better information has at least four potential benefits:

- **Estimation value:** narrower or better-calibrated uncertainty about the event and loss.
- **Timing value:** earlier awareness at similar accuracy.
- **allocation value:** better targeting of scarce crews, relief, adjusters, water, pest-control or finance.
- **loss-reduction value:** a changed action causes a lower realised loss than a credible alternative.

Only the fourth is avoided loss. Suppose the expected loss before new evidence is \(E[L\mid\mathcal I_t]\), and after evidence is \(E[L\mid\mathcal I_{t+1}]\). Their difference is a revision, not a benefit:

\[
\Delta \widehat L = E[L\mid\mathcal I_{t+1}]-E[L\mid\mathcal I_t].
\]

Avoided loss instead compares potential outcomes under an intervention \(a\) and a counterfactual \(a_0\):

\[
AL = E[L(a_0)-L(a)\mid X].
\]

Credible estimation requires evidence that information changed action, action occurred in time, action altered exposure or vulnerability, and the comparison is defensible. Evacuation may reduce mortality but not building damage. Clearing a drain may change local depth. Pre-positioning an adjuster may reduce settlement delay but not ground-up loss. Early pest control may change crop loss but must be distinguished from favourable weather. These are separate outcomes.

A platform evaluation should therefore measure calibration and lead time first, operational action second, and causal avoided loss only where study design permits it. Suitable designs include matched comparisons, phased roll-outs, discontinuity around action thresholds, process-based simulation and, rarely, randomised operational interventions. Every estimate should disclose spillovers, selection, model uncertainty and who bears costs.

## 9. Institutional products without an institutional super-score

Shared catastrophe evidence has economies of scope. The same posterior flood footprint can inform an emergency operations centre, claims triage, a lender's site review and a contingent-finance estimate. The interpretation cannot be shared indiscriminately.

### 9.1 Insurance and reinsurance

Insurers need event identification, exposure accumulation, expected claims ranges, policy-term application and fraud investigation leads. Before an event, hazard and loss models support portfolio design, underwriting and reinsurance. During an event, revised footprints support notification, reserve scenarios and operational deployment. After an event, claims and repair data improve vulnerability calibration.

Contract terms remain controlling. A model cannot retrospectively introduce an exclusion, cancel cover or change a price because an event is developing. An event loss distribution is not automatically a booked reserve or capital number; each has actuarial, accounting, solvency and governance requirements. Kenya's insurance-product guidance requires sound actuarial bases, customer treatment, risk assessment, approval and post-implementation review [8]. New parametric mechanisms therefore require product-specific approval and basis-risk evidence.

### 9.2 Lending and investment

Lenders and investors need site hazard, expected downtime, supply-chain dependencies, adaptation options and stress paths. Physical catastrophe intelligence may feed a separate credit model, but it is not probability of default by itself. Collateral impairment, revenue interruption, borrower liquidity and sponsor support require additional data and governance.

For infrastructure, the useful unit is often a service, not merely an asset. A bridge's resilience value includes traffic diversion, access to markets and emergency services. Investment appraisal should compare lifecycle costs and probabilistic benefits under stated climate scenarios, while avoiding claims that modelled expected loss reduction is guaranteed cash flow.

### 9.3 Public and climate-resilience finance

Government needs affected-population estimates, emergency liquidity, fiscal-loss distributions and funding-layer exhaustion. Disaster-risk financing commonly layers budgetary retention, reserves, contingent credit, insurance/reinsurance and market instruments by frequency, severity, speed and cost [9]. Kenya's published Disaster Risk Financing Strategy 2026–2030 provides the current national policy context [10], while the Climate Change Act establishes national and county climate-governance and finance functions [11].

Climate-resilience finance needs a transparent theory of change: capital funds a measure; the measure changes a physical or social parameter; changed parameters reduce loss or improve recovery; monitoring verifies delivery and outcomes. A drainage project, wetland restoration, cool-roof programme, borehole reliability measure or slope-stabilisation project requires different metrics. The catastrophe platform supplies baselines, scenarios and monitoring evidence, not automatic eligibility.

### 9.4 Communities and humanitarian organisations

For a resident, the priority product is intelligible action: what may happen, when, how confident the warning is, what route or protection is available and where assistance or claim information can be obtained. A system designed solely for portfolios can be technically accurate and socially unsuccessful. Two-way reporting must return value to contributors, accommodate non-smartphone and offline users, provide correction and redress, and avoid exposing vulnerable people.

## 10. Decision rights and accountable boundaries

The architecture distinguishes data flow, finance flow and decision authority.

| Decision | Evidence prepared by platform | Accountable authority |
|---|---|---|
| public weather or hazard warning | observed and forecast hazard state, confidence, affected area | legally mandated public agency |
| evacuation or emergency declaration | warning, exposure, access and scenario evidence | authorised national/county emergency authority |
| claim payment | event, exposure and damage evidence; policy-term calculation | insurer under contract, law and delegated controls |
| parametric payout | independently maintained trigger value and contract calculation | contractually identified calculation/payout parties |
| portfolio action | accumulation and scenario loss | insurer/investor governance body |
| public funding allocation | affected population, fiscal need, equity and layer analysis | authorised public finance and disaster institutions |
| resilience investment | avoided-loss range, beneficiaries, costs and uncertainty | project sponsor, financier and relevant authority |

**Figure 1.3 — Institutional ownership map (table-form conceptual figure).** Data flow, financial interpretation and decision authority remain separate.

Conflicting signals are inevitable. A model may show a high local flood probability while the authoritative agency maintains a lower warning level. The user interface must show both, identify the official source and escalate discrepancy; it must not silently relabel the model as an official warning. Likewise, an insurer may use a model to prioritise inspections but should not deny a claim solely because the model did not map the location as flooded.

## 11. Equity, legitimacy and the geography of missing data

Digital visibility is uneven. Urban smartphone users may generate dense imagery; remote pastoral and low-income communities may appear quiet. If report density is used naively, connected places gain confidence and finance while under-observed places look artificially safe. This is both a statistical missing-data problem and a distributive-justice problem.

Mitigations include stratified trusted-reporter networks, USSD/SMS/call-centre channels, offline capture, language support, deliberate sensor investment, uncertainty inflation in sparse areas and coverage audits against population and vulnerability. Funding formulas should never treat lower reporting as lower need without independent evidence. Model performance must be disaggregated by geography, connectivity, gender-relevant use cases, livelihood and other contextually justified groups while protecting privacy.

Community participation is not free data acquisition. Governance should explain the purpose, permitted uses, retention and possible institutional consequences; offer correction and withdrawal where applicable; protect identities; and return useful information. Compensation may be appropriate for sustained field roles. Photographs of homes, injured people or children require stricter minimisation and access controls than a rainfall measurement.

## 12. Failure is part of the architecture

Catastrophes are precisely when power, connectivity, cloud services, roads, satellites, sensors and partners may fail. Safe degradation must be designed before optimisation.

The platform should maintain source-health telemetry, locally cached maps and procedures, store-and-forward reporting, alternative communication channels, manual forms, defined stale-data thresholds and a visible degraded-mode banner. No stale observation should masquerade as current. If an advanced model fails, a transparent baseline with wider uncertainty should remain available. If all digital channels fail, institutional manuals and human command structures continue.

The following cases are required acceptance tests: a copied false report; authentic evidence with poor geolocation; satellite/local contradiction; failed flood gauge; remote reporting sparsity; camera degradation in smoke or rain; ambiguous drought onset; cross-border locust movement; communications loss after landslide; compound heat-fire-power stress; both sides of parametric basis risk; attempted mid-event contractual misuse; conflicting official/model warnings; cloud outage; data-subject correction; subgroup calibration deterioration; challenger failure; unsupported avoided-loss claims; and a financing proposal that treats an expectation as cash.

## 13. Research propositions and falsification

The series advances five testable propositions.

**P1 — Fusion.** Source-aware fusion improves hazard-state calibration, footprint skill or useful lead time relative to authoritative-only and crowd-only baselines. It fails if apparent gains vanish under event, spatial or source holdout.

**P2 — Operational relevance.** Improved state estimates improve at least one bounded workflow—such as claims triage, road-access assessment or anticipatory targeting—without unacceptable false-alarm, exclusion or latency costs. It fails if operators cannot act on the output or if harms exceed benefits.

**P3 — Financial reconciliation.** A common physical event representation can support consistent but distinct insured, uninsured, fiscal and investment views. It fails if valuation time, terms or ownership cannot be reconciled.

**P4 — Multi-hazard transport.** Common interfaces and governance transport across all six hazards while hazard-specific models retain superior scientific validity. It fails if the shared schema erases required state, timing or uncertainty.

**P5 — Community legitimacy.** Two-way participation improves coverage and local usefulness without disproportionate privacy, surveillance or exclusion harm. It fails if participation is extractive, unrepresentative or unsafe.

These propositions require prospective and retrospective evaluation. Publication alone supports none of them.

## 14. Worked cross-hazard narratives

The following cases are synthetic. They demonstrate architecture and decision boundaries; they are not forecasts, loss estimates or descriptions of actual Kenyan events.

### 14.1 Rapid urban flood

At 05:40, intense rainfall appears in gauge and forecast feeds. At 06:05, several residents report water overtopping a road. Two posts share the same video; lineage analysis correctly treats them as one source. A third image, captured independently, contains a recognisable junction but no trustworthy depth reference. Radar imagery arrives later and identifies a broader wet surface. A drainage sensor is stale.

The state model raises inundation probability and widens depth uncertainty because the failed drainage sensor removes a useful constraint. The official warning remains the KMD-issued product. County operations use the model layer to prioritise verification and road-control teams. An insurer intersects the provisional footprint with its portfolio to prepare call-centre capacity, not to deny claims outside the polygon. A lender identifies two potentially interrupted business sites but makes no automated credit change.

By afternoon, survey-grade marks and claims photographs improve the depth surface. Loss estimates increase because the new evidence reaches a dense commercial strip; this change is an information revision. If a road closure prevented vehicles from entering deep water, avoided motor loss would require evidence of traffic exposure, compliance, timing and a counterfactual—not the mere fact that later loss estimates were lower than an earlier worst case.

### 14.2 Slow pastoral drought

Over several months, rainfall, vegetation, water-point and market indicators deteriorate. Community reporters describe longer water journeys and changing livestock condition, but reporting density is lowest in the areas with weakest connectivity. The platform does not interpret quiet cells as normal. It increases epistemic uncertainty, requests structured field observations and flags geographic representation risk.

The latent drought state can worsen without a discrete onset day. NDMA's authorised drought stages remain the public institutional classification. A livelihood insurer may calculate an independently defined contractual index; a county may prepare water logistics; a financier may assess whether pre-agreed anticipatory funds meet eligibility conditions. These are linked to the same environmental evidence but have separate thresholds, timing and owners.

If water delivery protects livestock, the impact evaluation compares mortality, body condition, distances and household costs against a credible alternative. If rains arrive unexpectedly, attribution must separate the intervention from weather. A timely payout may improve liquidity even if it does not change the hazard. This is a valuable outcome, but it is not physical hazard reduction.

### 14.3 Mobile locust threat

Field officers and farmers submit reports of hopper bands. A vision model marks candidate insects, but species and lifecycle uncertainty remain. Wind and vegetation covariates support a movement envelope that crosses two counties. Administrative aggregation alone would truncate the process, so the event maintains a continuous geometry and records county intersections for coordination.

Plant-protection authorities validate the outbreak and own control decisions. Crop exposure is time-sensitive: the same swarm density can create different loss at different crop stages. A control operation changes the subsequent biological process, so the state transition conditions on intervention time, coverage and efficacy. Insurers may use the verified footprint in claims investigation; government records control cost and potential production loss; food-security actors evaluate livelihood consequences. No computer-vision confidence score becomes a pesticide-deployment order.

### 14.4 Hillslope failure after rainfall

A model identifies susceptible saturated slopes after prolonged rain. A community report describes a crack near a road, but the phone location is imprecise. The system retains the reported uncertainty instead of snapping the observation to the nearest mapped slope. A second trusted reporter supplies an offline form when connectivity returns. Meanwhile, a local official closes the road using established authority.

After movement occurs, imagery shows a blockage but not the condition of buried utilities. The initial loss range includes road clearance and access interruption scenarios. It does not invent utility damage. Sparse historical labels keep the landslide-probability interval wide even though the potential consequence is high. The operational response can be precautionary because decision thresholds incorporate consequence and reversibility, not because the probability is falsely precise.

### 14.5 Heat, fire and power stress

A heat episode raises health and grid stress. Dry vegetation and wind increase fire spread potential; a local camera detects smoke with low nighttime confidence. Power interruption removes cooling from a clinic. The consequence graph links the weather state, fire candidate, feeder outage, clinical service and vulnerable population. Separate owners validate each link.

The system avoids double-counting the same business interruption under heat, power and fire. It reports attribution ranges and a joint scenario. Community warnings use plain-language protective actions and accessible channels. Portfolio users see concentration and service-dependency risk. The example shows why compound risk needs an event graph rather than the sum of six independent hazard scores.

## 15. Stakeholder architecture and incentives

A technically shared platform will fail if participants have no reason to provide timely, high-quality evidence or fear how it will be used. The operating proposition must therefore be reciprocal.

Communities receive warnings, action guidance, confirmation that reports were received, and information about assistance and claims. Field contributors receive training, safety procedures and, where roles are sustained, fair compensation. Scientific agencies retain attribution and authority. Counties receive locally actionable views and exportable records. Insurers gain better accumulation and claims readiness but accept permitted-use boundaries. Investors receive diligence evidence but not personally identifiable event narratives. Regulators receive model and conduct assurance. Researchers gain governed, de-identified datasets only under approved purposes.

Incentives can conflict. A claimant may benefit from a high damage estimate; an insurer may benefit from a low one; a project sponsor may prefer a large avoided-loss claim; an authority may fear reputational harm from a missed warning. This does not invalidate their evidence, but it requires separation of observation, verification and adjudication. The platform records who asserted what, what independent signals agreed, and who made the final decision.

Institutional sustainability also depends on cost. Continuous satellite acquisition, connectivity, model operation, field networks, exposure maintenance, security and validation are recurrent services, not one-off software purchases. A shared-service arrangement can reduce duplication, but funding and service-level agreements must protect public-interest functions from the withdrawal of one commercial participant.

## 16. Evaluation framework

Evaluation follows the causal chain rather than a single accuracy number.

### 16.1 Observation metrics

Coverage is measured by geography, time, hazard, source and relevant population—not raw report count. Quality measures include timestamp error, geolocation error, duplicate rate, calibration, completeness and correction frequency. False-content detection is evaluated with the cost of wrongly rejecting authentic reports. Privacy and consent incidents are first-class performance failures.

### 16.2 Hazard-state metrics

Probabilistic calibration, Brier or log scores, footprint intersection-over-union, depth or intensity error, onset lead time, duration error and extreme-event recall are compared with transparent baselines. Evaluation holds out complete events and locations to expose leakage and weak transfer. A model that improves mean error while missing extremes is not automatically acceptable.

### 16.3 Impact and loss metrics

Loss evaluation includes bias and calibration by peril, geography, exposure class and loss layer; prediction-interval coverage; claims-development accuracy; exceedance-curve stability; and tail sensitivity. Exposure-data error is reported separately from hazard and vulnerability error. The aim is actionable uncertainty, not merely a close aggregate total that hides offsetting local errors.

### 16.4 Operational metrics

Lead time is only useful if it is available before a decision deadline. Evaluation therefore records the fraction of cases in which evidence reached an authorised owner, an action was considered, an action occurred, the intended recipient received it and the system remained available. False alarms, missed events, workload and manual overrides are examined together.

### 16.5 Financial and social outcomes

Insurance outcomes include notification and settlement time, triage accuracy, complaints, leakage and customer treatment. Public-finance outcomes include speed, targeting and layer adequacy. Investment outcomes include whether resilience measures were implemented and performed. Social outcomes include reach, comprehension, accessibility, trust, protection of contributors and distribution of benefit. Monetary benefit never cancels a serious rights or safety failure.

## 17. Research programme and readiness

The project begins as research and controlled shadow operation. Readiness is evaluated across hazard relevance, authoritative mandate, source availability, community partnership, connectivity, exposure quality, ability to validate, operational actionability and legal permission. Flood and drought pilots provide the strongest initial contrast, but exact locations should be chosen only after scoring and consultation.

A pilot site is not selected because it offers the easiest success story. It should expose meaningful uncertainty while retaining safe comparison and response capacity. For flood, a candidate needs gauge/rainfall or remote-sensing evidence, exposure variation and a responsible operational partner. For drought, it needs multi-month indicators, livelihood representation and clear separation between institutional status and model state. Both require a manual baseline.

Progression requires predefined gates: admissible data; baseline performance; shadow-mode reliability; independent validation; operational usability; legal and community review; and evidence of benefit without disproportionate harm. Failure at a gate triggers remediation, narrowed use or stop. A sophisticated challenger that does not outperform the baseline is archived, not rationalised.

## 18. Limitations and boundary conditions

This architecture cannot replace missing gauges, exposure surveys, claims discipline, institutional mandates or trusted communication. Models trained on sparse historical disasters will carry large tail uncertainty. Climate and land-use nonstationarity limit extrapolation. Indirect and intangible losses resist rapid valuation. Informal assets and livelihoods are easily undercounted. County capability and connectivity vary. International methods may not transfer without Kenyan calibration.

The scope excludes earthquake, volcanic, tsunami, conflict, cyber, pandemic and technological disasters as primary perils. Disease, displacement, food insecurity, livelihood collapse and infrastructure interruption enter as consequences of the six in-scope hazards, not as fully modelled independent perils. The project does not authorise a platform, product, payout or automated decision.

The California wildfire notes that helped shape the distributed-sensor and reliability concepts are hypotheses, not Kenyan evidence. The actuarial charter supplies quality principles, and the benchmark white paper supplies a standard of integration and narrative density; neither defines this project's product or institutions.

## 19. Conclusion

Kenya does not need a single opaque catastrophe score. It needs a common, auditable evidence spine that can preserve differences among hazards and institutions. Authoritative systems, communities, satellites, sensors and portfolios contribute observations; source-aware models estimate evolving hazard; exposure and vulnerability convert physical states to loss distributions; and named institutions make decisions under law, mandate and contract.

The central discipline is separation: occurrence from detection, confidence from probability, hazard from consequence, event loss from annual risk, estimation from avoided loss and evidence from authority. With those separations, real-time intelligence can improve preparedness, response, financial protection and investment. Without them, technical integration can amplify error and obscure accountability.

### 19.1 What a successful capability would look like

Success would be visible in ordinary institutional behaviour. A county operator would see the age and source of a flood layer, compare it with the official warning and know whom to call when they conflict. A community contributor would understand why a report was requested, receive useful information in return and have a practical route to correct its location. A hazard scientist could replay an estimate using only evidence available at the time. An actuary could trace each loss quantile to event, exposure and terms. A claims manager could use a queue without treating it as an adjudication. A Treasury analyst could see which financing layer is likely to exhaust and which assumptions drive the estimate. An investor could distinguish physical downtime from probability of default. An independent reviewer could reproduce the result and stop use when uncertainty or rights controls fail.

Success would also include disciplined non-use. The system would decline to publish a high-resolution map that exposes vulnerable households; refuse to turn a copied post into ten confirmations; retain a transparent baseline when a complex model fails; and state that a drought onset date is ambiguous. It would preserve a valid severe-loss report even when a parametric trigger did not activate. It would not claim avoided loss without intervention and counterfactual evidence.

These behaviours are the practical meaning of resilience intelligence. The platform becomes valuable not because every institution shares one answer, but because each receives evidence whose lineage, uncertainty and authorised interpretation are explicit.

### 19.2 The series as a research contract

The six papers form a research contract among disciplines. Hazard science may reject a convenient statistical topology; communities may reject an unsafe data channel; actuaries may reject an undefined financial quantity; lawyers may constrain reuse; operators may reject latency; financiers may require a clearer cash mechanism. Those challenges are intended. Interdisciplinary integration is not agreement by dilution. It is a chain in which every transformation is strong enough to be challenged by the discipline that owns it.

The immediate output is therefore not a procurement list. It is a falsifiable architecture, shared notation, evidence ledger, hazard matrix and stage-gated implementation proposition. Future pilots should narrow scope, name owners and produce evidence that either supports or refutes the propositions. Learning that a crowd channel adds no incremental lead time, that an advanced state model is unstable or that a finance structure has unacceptable basis risk is a legitimate result.

### 19.3 Priority research agenda

The first research priority is an observation audit: where authoritative and community evidence exists, where it fails during events, which groups and places are under-observed and what minimum new collection is justified. The audit should compare flood and drought to expose rapid and slow knowledge-time problems. It should not begin by purchasing cameras or training a detector.

The second is a point-in-time event benchmark. Selected historical events should be reconstructed using only evidence available at each operational time, alongside a later best-available reconstruction. This dataset enables honest lead-time, calibration and claims-nowcast evaluation. Legal, licence and privacy restrictions must be built into its design.

The third is a Kenyan exposure and vulnerability programme. It should prioritise high-consequence, underrepresented building, infrastructure, crop, livestock and livelihood classes; normalise past loss; combine engineering, field and claims evidence; and publish uncertainty rather than transplant foreign curves invisibly.

The fourth is decision experimentation in shadow mode. County, insurer, community and finance users should operate realistic exercises and record whether evidence changed a feasible action before measuring loss reduction. Human interpretation, workload, connectivity and fallback are part of the experiment.

The fifth is public-interest governance research: trusted reporting arrangements, compensation, language and accessibility, permitted-use enforcement, redress and benefit distribution. A technically better model that weakens trust or excludes less-connected communities is not a successful catastrophe capability.

The sixth is financial translation research. It should test the same event posterior through insured, uninsured, fiscal and project views and identify where definitions diverge. Parametric or resilience instruments should follow only after data continuity, basis, cash mechanism, authority and customer or public value are evidenced.

These priorities create a sequence from what can be known, through what can be estimated, to what institutions can legitimately do. They also produce useful intermediate outputs even if a national platform is never built.

### 19.4 Boundary tests for future proposals

Any proposed extension should answer five questions. First, does it strengthen the shared evidence chain or introduce a materially different peril and decision system? Earthquake, conflict, pandemic, cyber and technological events require separate scope approval; their appearance in a consequence graph does not add them automatically. Second, does it preserve project focus on catastrophe intelligence rather than revive motor telematics, premium finance, gig work or another reference project's product? Third, is the Kenyan institutional and empirical case verified rather than inferred from California or other foreign examples? Fourth, does the proposal add a source/model, or claim authority to alert, pay, price, allocate or invest? The latter requires a separately accountable owner. Fifth, could the same benefit be achieved through a simpler baseline, field capacity or data-quality improvement?

These tests protect coherence while allowing learning. New perils or users may eventually fit the architecture, but they must demonstrate physical topology, observation process, exposure/vulnerability, financial meaning, legal authority and validation. The platform is extensible because its interfaces are explicit—not because “multi-hazard” removes the need for boundaries.

The strongest near-term proposition remains modest: improve what Kenyan institutions and communities can know about six catastrophe processes, show how uncertainty travels into loss, and test whether better evidence improves bounded action. Expansion follows evidence rather than ambition.

Part 2 defines the observation architecture needed to make heterogeneous evidence admissible. Parts 3 and 4 develop hazard-state and loss models. Parts 5 and 6 govern financial use and staged implementation.

## References

[1] Kenya Meteorological Department, “Weather forecasting services,” accessed Aug. 26, 2026. [Online]. Available: https://meteo.go.ke/Services/weather-forecasting/

[2] Water Resources Authority, “Surface water assessment and monitoring,” accessed Aug. 26, 2026. [Online]. Available: https://wra.go.ke/surface-water-assesment-monitoring/

[3] National Drought Management Authority, “Drought information,” accessed Aug. 26, 2026. [Online]. Available: https://ndma.go.ke/drought-information/

[4] Plant Protection and Food Safety Directorate, “Desert locust,” accessed Aug. 26, 2026. [Online]. Available: https://plantprotection.kilimo.go.ke/desert-locust/

[5] Kenya Forest Service, “Forest protection and security,” accessed Aug. 26, 2026. [Online]. Available: https://www.kenyaforestservice.org/forest-protection-and-security/

[6] Intergovernmental Panel on Climate Change, “Annex II: Glossary,” in *Climate Change 2022: Impacts, Adaptation and Vulnerability*, 2022. [Online]. Available: https://www.ipcc.ch/report/ar6/wg2/chapter/annex-ii/

[7] Republic of Kenya, *Data Protection Act*, No. 24 of 2019, sec. 35. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24

[8] Insurance Regulatory Authority, *Insurance (Insurance Products) Guidelines, 2022*, Kenya Gazette Legal Notice. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3641/eng%402022-03-29/source

[9] World Bank, “Disaster risk finance and insurance,” accessed Aug. 26, 2026. [Online]. Available: https://www.worldbank.org/ext/en/topic/financial-sector/disaster-risk-finance-and-insurance

[10] National Treasury and Economic Planning, *Kenya Disaster Risk Financing Strategy 2026–2030*, 2026. [Online]. Available: https://www.treasury.go.ke/sites/default/files/Latest%20updates/Kenya%20Disaster%20Risk%20Financing%20Strategy%202026%20-%202030.pdf

[11] Republic of Kenya, *Climate Change Act*, No. 11 of 2016, rev. 2023. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2016/11/eng%402023-09-15
