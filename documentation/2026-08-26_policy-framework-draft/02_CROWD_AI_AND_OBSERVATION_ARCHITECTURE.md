# Crowd Intelligence, AI Perception and the Observation Architecture

## Abstract

Catastrophe intelligence begins before modelling: it begins with deciding what counts as an observation, what the observation actually measures and what was knowable at a particular time. Kenya's flood, drought, rangeland fire, locust, landslide, storm and heat risks create radically different signals. A river gauge produces a calibrated time series; a resident's photograph records a partial scene; a radar classifier produces a derived feature; a claims file documents a contractual process; silence from a low-connectivity area says little about whether a hazard exists. Treating these records as interchangeable creates false precision and inequity.

This paper specifies a multimodal observation architecture in which authoritative data, earth observation, environmental sensors, crowd reports and institutional records are validated through source-specific controls. It defines a canonical interface, point-in-time semantics, spatial and unit conventions, contributor and sensor reliability, duplicate lineage, edge/cloud responsibilities, privacy boundaries and safe degradation. Artificial intelligence performs bounded perception and quality-control tasks. YOLO-style object detection is useful for locating discrete objects and damage indicators but is neither a surface-mapping method nor a hazard, catastrophe or actuarial model.

The paper's central claim is that admissible evidence must carry provenance and uncertainty from the raw signal into later state and loss models. Source confidence cannot simply be averaged; correlated repetition must not masquerade as corroboration; missing observation must not be read as no hazard; and personal data must not be repurposed across public-warning, claims, credit or investment uses. The result is a reproducible path from raw signal to a governed model observation.

**Research question.** How should Kenya collect, validate, reconcile and govern multimodal catastrophe observations so that each downstream estimate is point-in-time correct, privacy-preserving, uncertainty-bearing and fit for a stated institutional use?

## 1. A report is not yet evidence

A driver sends a photograph of water covering a road. The image is current, but its location was added manually and is wrong by two kilometres. Several social-media accounts repost it. A satellite pass classifies the true road as dry because the acquisition preceded the rainfall. A nearby gauge has not transmitted for three hours. What should the system believe?

It should first resist a premature binary answer. The photograph supports the proposition that flooding occurred somewhere within a location distribution at a stated time. Reposts inherit the same evidentiary lineage. The satellite observation describes an earlier surface with its own acquisition and processing uncertainty. The gauge is missing, not low. Together these facts can update a hazard-state model only if their times, locations and dependence remain visible.

This is why the observation layer is more than data ingestion. It performs five functions:

1. expresses heterogeneous inputs in source-appropriate schemas;
2. verifies integrity, time, geometry, units and permitted use;
3. estimates quality and dependence without pretending to know truth;
4. preserves raw-to-derived lineage and corrections;
5. delivers point-in-time snapshots to scientific, actuarial and operational consumers.

The output is an admissible observation. It may still be uncertain or contradictory. Contradiction is information for the state model and a possible prompt for human verification.

## 2. What each hazard requires us to observe

### 2.1 Flood

Useful flood signals include rainfall intensity and accumulation, river stage and discharge, reservoir or gate status, soil saturation, terrain, drainage capacity, surface-water extent, depth, velocity, duration and recession. Consequence signals include road passability, building waterlines, service interruption, displacement and crop inundation.

Gauge measurements can be frequent and quantitative but spatially sparse or stale. Weather radar and satellite synthetic-aperture radar provide broader footprints; Sentinel-1 radar is valuable because microwave sensing can operate through cloud and without daylight [1]. Terrain and drainage data constrain plausible flow but may miss informal or recently altered drainage. Community photographs identify local consequences and obstructions; they need depth references and geometry controls before quantitative use.

### 2.2 Drought

Drought is a sustained, multidimensional state rather than one image. Observations include rainfall anomaly, soil moisture, evapotranspiration, vegetation indices, forage condition, surface and groundwater availability, borehole functionality, travel time to water, livestock condition, crop development, market prices, nutrition and coping behaviour. NDMA's drought information system explicitly combines biophysical and socioeconomic indicators [2].

Remote sensing gives consistent spatial coverage, while field reports interpret livelihood meaning and local water access. Both can mislead: vegetation greenness may not equal edible forage; a functioning borehole may be inaccessible or crowded; market prices may reflect wider conditions. The observation schema must state the measured variable, unit, population and method rather than store a generic drought score.

### 2.3 Wildfire and rangeland fire

Observation needs include ignition candidates, smoke, flame, thermal anomaly, perimeter, fire radiative power or intensity proxies, wind, humidity, temperature, fuel moisture, vegetation type, slope, suppression activity and infrastructure at risk. Cameras and community reports offer rapid detection; satellites provide thermal and scar products with revisit and resolution constraints. Ranger observations add context on fuel, access and control operations.

Ignition time is not detection time. A camera's first smoke box establishes neither the cause nor exact onset. Smoke, night, glare, occlusion and rain shift vision performance. Suppression changes subsequent perimeter, so actions are timestamped observations of the physical process, not external notes.

### 2.4 Locust and catastrophic crop pests

Mobile biological hazards require species, lifecycle stage, density, area, direction, wind, breeding conditions, vegetation and crop-stage observations. Field officers, extension networks and farmers are essential because coarse imagery rarely identifies species directly. The Food and Agriculture Organization's eLocust3 system illustrates structured field capture and near-real-time transmission for survey and control information [3]. Kenya's plant-protection authority provides the national institutional context [4].

Reports must distinguish sighting, verified survey, modelled movement and treated area. A photograph may support species classification but not swarm density without scale and sampling method. Control activity, efficacy and re-observation are part of the state history.

### 2.5 Rainfall-induced landslide

Signals include rainfall intensity-duration, antecedent moisture, slope, geology, land cover, drainage, deformation, cracks, small precursor movement, debris, road blockage and utility disruption. Rainfall thresholds can support screening, but thresholds are location- and process-specific [5]. Ground sensors can be precise at instrumented slopes, while imagery and road reports expand coverage.

The key geometry may be metres wide. A mobile location uncertainty of hundreds of metres can associate a crack with the wrong hillslope. Because labels are sparse and non-events are under-recorded, absence of a report is particularly weak evidence.

### 2.6 Severe storm and extreme heat

Storm observations include rainfall, wind, hail, lightning, pressure and damage to roofs, crops, trees and networks. Heat requires temperature, humidity, radiant heat, nighttime persistence, indoor conditions, urban form, power availability, cooling access, health syndromic indicators and work exposure. A weather-station temperature cannot by itself represent household indoor heat or occupational burden.

Heat shows why observation architecture must cover invisible consequence. Crowd and institutional reports on cooling, symptoms or service stress may be more relevant to impact than a photograph. These records can be sensitive health or location data and require stringent aggregation and access.

## 3. Source classes and evidentiary meaning

### 3.1 Authoritative and scientific sources

KMD forecasts, bulletins and station observations; WRA hydrological records; NDMA drought indicators; plant-protection surveys; forest-service observations; county emergency records; and other mandated sources carry institutional provenance [2], [4], [6]–[8]. Authority does not mean error-free. Sensors fail, methods change and releases can be corrected. It means the source has a defined mandate and controlled production process.

The platform stores both published authoritative products and underlying measurements where lawful and available. It never edits an official warning. A derived local layer is labelled as a model output and linked to, but distinguishable from, the official product.

### 3.2 Earth observation and geospatial foundations

Earth observation includes raw or processed radar, optical, thermal, soil-moisture, rainfall and vegetation products. Each record needs platform, instrument, orbit or acquisition time, processing level, algorithm, pixel size, coordinate reference system, cloud or quality mask and licence. A modelled rainfall estimate is not a gauge measurement. A classified water pixel is not a direct water-depth observation.

Geospatial foundations—digital elevation, river network, drainage, land cover, administrative areas and asset geometry—change more slowly but remain versioned. Resolution and positional accuracy must match use. A national land-cover grid may be appropriate for drought context but unsafe for property-level claims adjudication.

### 3.3 Environmental and infrastructure sensors

Gauges, weather stations, soil probes, borehole telemetry, cameras, power monitors and road sensors produce machine observations. Their metadata include calibration, maintenance, sampling interval, clock synchronisation, operating range, battery or communications status and quality flags. A flat time series can mean a stable state, a frozen sensor or a clipped maximum. Health telemetry enables the distinction.

### 3.4 Human and crowd reports

Reports may arrive through smartphone applications, WhatsApp, SMS, USSD, voice or call centres, web forms and offline field tools. Channels should accommodate text, structured menus, photographs, audio and geometry while minimising personal data. A call-centre operator can convert a narrative into structured fields and retain the recording only if lawful and necessary.

Reporter classes include open public contributors, trained volunteers, chiefs and local administrators, Red Cross or humanitarian personnel, rangers, farmers, pastoralists, transport operators, water associations and extension officers. Trust is task-specific. The architecture stores a pseudonymous source identifier where possible and separates identity management from model features.

### 3.5 Institutional and financial records

Claims, emergency calls, work orders, road closures, crop assessments, repair invoices, transaction interruption and portfolio exposure document consequences. They frequently arrive after event observations and may contain highly sensitive information. Their absence can reflect reporting or coverage gaps. Claims are generated by insurance contracts, not a census of damage.

Financial records enter through purpose-limited views. An image contributed for public hazard reporting is not automatically available to underwriting, credit or marketing. Derived aggregate features may be shared only where the legal basis and governance permit.

## 4. Canonical observation interface

Every admitted record implements the following logical contract:

```text
observation_id
hazard_type
source_type
source_id_or_pseudonym
event_time
knowledge_time
ingestion_time
geometry
geometry_uncertainty
observed_variable
value
unit
measurement_or_derivation_method
model_or_report_confidence
source_reliability
provenance
duplication_cluster
consent_and_permitted_use
quality_flags
correction_or_predecessor
schema_version
```

**Figure 2.1 — Multimodal observation pipeline contract (schema-form conceptual figure).** Every downstream feature remains linked to time, geometry, provenance, quality and permitted use.

`observation_id`, hazard, source type, event time, knowledge time, geometry or explicit `unknown`, observed variable, method, provenance, quality flags and schema version are mandatory. A numeric value requires a unit. Model-derived features require model version and input lineage. Human reports require a permitted-use record; identity is stored separately if operationally necessary.

Potential personal data include precise household or contributor location, images of identifiable people or property, telephone number, voice, device identifiers, claim details and free text. Geometry uncertainty is mandatory whenever location is inferred or manually entered. `source_reliability` is a time-stamped model input, not a permanent fact about a person.

Derived observations retain a directed lineage graph to raw evidence. If a segmentation model produces a flood polygon from radar, the polygon links to source scene, processing code, weights, thresholds and quality mask. If an analyst corrects the geometry, a successor record identifies the reviewer, reason and prior version.

## 5. Time: when it happened, when it was known

Three times are required:

- **event time:** when the physical state was measured or experienced;
- **knowledge time:** when the source first made the record available to the platform or responsible institution;
- **ingestion time:** when the platform successfully stored it.

A fourth, processing time, may track a derived result. These distinctions prevent future information leaking into historical evaluation. A claims photograph captured on Monday but uploaded Wednesday can inform a Wednesday nowcast; it cannot be credited to Monday's operational forecast. A corrected gauge reading changes today's reconstruction without rewriting what decision makers knew yesterday.

Point-in-time queries take both valid time and system time:

\[
\mathcal I(t_v,t_k)=\{y_j: event\_time_j\le t_v,\ knowledge\_time_j\le t_k\}.
\]

Replay uses the original schema, model and data available by \(t_k\). Backfills are clearly labelled. This is essential for lead-time evaluation, claims audit, causal studies and regulatory review.

## 6. AI perception: fit the method to the observable

### 6.1 Object detection

Object detectors such as the YOLO family return classes, bounding boxes and scores. Suitable catastrophe tasks include finding people, vehicles, livestock, isolated pest candidates, smoke plumes, flame, blocked culverts or visible damage indicators. Detection is helpful when the object is discrete and localisation matters.

The output is structured evidence:

```text
image_id | class | bounding_box | model_score | model_version | quality_context
```

It is not a peril probability or loss. A vehicle detected in floodwater says that at least part of a vehicle and water-like surface co-occurred within the image. Depth, operability, ownership, damage, policy coverage and event footprint require further evidence. Non-maximum suppression can remove overlapping boxes, but it does not deduplicate the same scene uploaded by several accounts.

Training and validation must reflect Kenyan conditions: device quality, road and building form, vegetation, clothing and livestock, smoke and dust, darkness, rain, glare and camera angle. Performance is reported by class, context and geography. Threshold choice is operational: a low threshold can increase early detection and verification workload; a high threshold can miss weak smoke or partially obscured people.

### 6.2 Semantic and instance segmentation

Segmentation assigns a label or probability to pixels and is generally better suited to continuous surfaces such as floodwater, burn scar, damaged roof, stressed vegetation or affected cropland. Instance segmentation separates individual objects while retaining their shape. Pixel probabilities still require geometric correction, quality masks and post-processing.

Detection and segmentation answer different questions. A detector may locate a smoke plume quickly; segmentation may estimate its visible extent; neither predicts the fire perimeter without weather, fuels and spread modelling. A flood segmentation may estimate extent but depth needs terrain, water level, hydraulic relationships or validated visual references.

### 6.3 Time-series, anomaly and forecasting models

Environmental time series contain seasonality, autocorrelation, gaps, drift and extremes. Anomaly models can flag implausible jumps or emerging departures. Forecast models can produce distributions for rainfall, river level, heat or vegetation condition. Quality-control models must not erase genuine extremes simply because they are rare. Every automated correction is reversible and retains the raw observation.

Multivariate consistency is powerful: river rise should be interpreted with upstream rainfall, reservoir operations and neighbouring gauges; borehole telemetry with usage and maintenance; heat with humidity and station exposure. The model can issue a sensor-health alert separately from a hazard alert.

### 6.4 Natural-language processing

Messages may use Kiswahili, English, local languages and code-switching, abbreviations and place nicknames. NLP can classify hazard, extract time, place, severity phrase, affected object, need and uncertainty. Geocoding returns candidates with probability, not a forced coordinate. Translation and classification models need evaluation with local speakers, especially for urgent negation and uncertainty—“road is not flooded” must not become “road flooded.”

Large language models may help structure narratives, but their output remains derived and traceable to the original message. They may not fill missing quantities. Sensitive free text is minimised, access-controlled and redacted before broad analytical use.

### 6.5 Observation confidence is not hazard probability

Let \(c_j\) be a classifier score for observation \(j\). Even after calibration, it estimates something like

\[
P(label_j=1\mid image_j, model, domain),
\]

not \(P(H_{g,t}=h\mid \mathcal I_t)\). The latter also incorporates source dependence, location, time, physical constraints and prior state. The state model may down-weight a high-confidence but stale or poorly located detection and up-weight a moderate visual score corroborated by independent sensors.

## 7. Reliability, credibility and correlated repetition

### 7.1 Reliability as a dynamic latent property

Source reliability \(q_{s,v,t}\) varies by source \(s\), variable \(v\) and time. A gauge can be reliable within its range but clip during extreme stage. A contributor can be accurate about road closure but estimate depth poorly. A satellite classifier can transfer well in open rangeland and fail in dense urban shadow.

A Bayesian formulation starts with a conservative prior and updates it on verified outcomes:

\[
q_{s,v}\sim \operatorname{Beta}(a_{s,v},b_{s,v}),
\qquad
q_{s,v}\mid verification \sim \operatorname{Beta}(a+TP,b+FP),
\]

for a simplified binary task. Real implementation accounts for uncertain truth, sampling, class imbalance and time decay. Reliability is never shown as a moral rating and is not used for unrelated eligibility or surveillance.

### 7.2 Duplication and propagation graphs

Near-identical text, perceptual image hashes, shared URLs, metadata and temporal propagation create duplication clusters. A cluster contains observations that may descend from one original source. The system identifies a likely root, transformations and independent captures. It retains all records for communication analysis but discounts dependent evidence in hazard fusion.

```{.mermaid #fig-2-3 alt="Corroboration and duplicate-control workflow"}
flowchart LR
  ROOT[Original photograph] --> A[Direct repost]
  ROOT --> B[Cropped repost]
  B --> C[Caption copy]
  ROOT --> D[Screenshot]
  ROOT --> CLUSTER[One duplication cluster and one evidentiary lineage]
  A --> CLUSTER
  B --> CLUSTER
  C --> CLUSTER
  D --> CLUSTER
  G[Independent gauge] --> FUSE[Corroborated evidence]
  P[Independent second photograph] --> FUSE
  CLUSTER --> FUSE
```

**Figure 2.3 — Corroboration and duplicate-control workflow.** Repetition within one lineage is not independent evidence.

Independence is probabilistic. Two field officers may use the same briefing; two sensors may share a power supply; several cameras may run the same model. The provenance graph includes shared upstream dependencies so a single outage or bias is not counted repeatedly.

### 7.3 Misinformation, manipulation and fraud

Controls can flag mismatched metadata, reverse-seen imagery, implausible sun or weather context, impossible travel, coordinated accounts and mismatch with terrain. Flags prompt review; they are not proof of fraud. Authentic disaster imagery often loses metadata through messaging services or is reposted for legitimate warning. Accusations require a different evidentiary and due-process standard from statistical down-weighting.

Claims fraud controls remain separated from public reporting. A community report should not silently become adverse evidence about a policyholder. Access, purpose and retention are enforced technically and contractually.

## 8. Spatial architecture, geometry and units

All geometry has a coordinate reference system, positional accuracy and representation type. Points may include error ellipses; lines represent roads or rivers; polygons represent footprints or administrative areas; rasters carry cell size, alignment and nodata semantics; networks carry directed topology.

Storage should preserve an authoritative geometry and derive indexed representations for computation. A national equal-area grid may support aggregation; catchment and river-reach identifiers support hydrology; ecological corridors support fire or locust movement; administrative codes support governance. Crosswalks are versioned because boundaries and asset maps change.

Spatial joins propagate uncertainty. If a point's error circle intersects two road segments, the system retains alternatives. It does not assign the nearest feature silently. Raster resampling records method; categorical land cover should not be averaged like rainfall. Areas and distances use projected coordinates appropriate to scale.

Units are explicit and preferably SI: rainfall in millimetres over a stated interval, river stage in metres relative to a named datum, discharge in cubic metres per second, temperature in degrees Celsius with measurement context, wind in metres per second or clearly converted convention, area in square metres or hectares, currency in Kenyan shillings with valuation date. Anomaly values state baseline period and standardisation method.

Resolution must match decision. A 10-metre water classification is useful for neighbourhood situational awareness, not proof of inundation at a particular threshold inside a building. Aggregation never increases underlying accuracy.

## 9. Edge, cloud and hybrid inference

### 9.1 Edge responsibilities

Edge devices and field applications support offline forms, timestamping, basic validation, compression, redaction, simple inference and cached guidance. They reduce bandwidth and latency and can protect privacy by sending structured features instead of raw imagery. They operate with constrained power, storage and model-update capability.

An offline field application should store encrypted, signed records; show whether time and location are device-derived or entered; validate units; queue upload; and preserve original capture. It must not tell a contributor that submission is complete before durable storage. Safety guidance should discourage dangerous photography near floodwater, fire, unstable slopes or active control operations.

### 9.2 Cloud or central responsibilities

Central services handle heavier geospatial processing, satellite ingestion, cross-source deduplication, model registry, national state estimation, portfolio-safe aggregation, audit and replay. They maintain access controls, data-quality dashboards, schemas and resilient backups. Central inference can use richer context but depends on connectivity and shared infrastructure.

### 9.3 Hybrid design

The preferred pattern is store-and-forward hybrid operation:

```{.mermaid #fig-2-2 alt="Edge and cloud hybrid observation architecture"}
flowchart LR
  subgraph EDGE[Device and field edge]
    CAP[Safe capture and offline form]
    CHECK[Basic checks, redaction and local inference]
    CACHE[Cached official guidance with expiry]
    CAP --> CHECK
  end
  subgraph QUEUE[Resilient handoff]
    ENC[Encrypted store-and-forward queue]
    RETRY[Retry, idempotency and delivery receipt]
    ENC --> RETRY
  end
  subgraph CENTRAL[Regional and central services]
    ING[Authenticated ingestion and schema validation]
    FUSION[Cross-source lineage, fusion and replay]
    REG[Model and schema registry]
    PROD[Signed purpose-specific products]
    ING --> FUSION
    REG --> FUSION
    FUSION --> PROD
  end
  CHECK --> ENC
  RETRY --> ING
  PROD --> CACHE
```

**Figure 2.2 — Edge/cloud hybrid architecture.** Capture and approved guidance degrade locally; central services perform cross-source fusion and replay.

Model updates are signed, versioned and rollback-capable. The device reports model and schema version with every derived feature. If an edge model is stale, the central service may reprocess retained inputs where permitted. If the cloud is unavailable, the edge continues approved capture and displays cached official information with age and expiry.

Technology choices—stream broker, object store, geospatial database, lakehouse or model-serving framework—are replaceable. Functional contracts, open export, lineage and recovery matter more than a named vendor.

## 10. Functional data platform

The platform separates raw, validated, analytical and product zones.

**Raw evidence** is immutable, encrypted and access-restricted. **Validated observations** conform to schemas and carry quality flags. **Analytical state** contains reproducible model inputs and outputs. **Decision products** are purpose-specific, approved and retained with delivery receipts. Personal identifiers sit in a segregated identity vault where needed.

Streaming responsibilities include authentication, schema validation, idempotency, event-time windows, late data, dead-letter handling and backpressure. Batch responsibilities include satellite scenes, historical replay, exposure snapshots and model training. A catalogue records owner, legal basis, licence, sensitivity, resolution, latency, retention and downstream uses.

Point-in-time joins use versioned features. A model trained in June cannot use a claim correction first learned in August unless labelled retrospective. Training, validation and operational datasets are separated. Synthetic data are visibly marked and never enter empirical performance claims.

## 11. Privacy, consent and permitted-use separation

```{.mermaid #fig-2-5 alt="Privacy and permitted-use boundary"}
flowchart TB
  ID[(Segregated identity vault)] -.-> RAW[Restricted raw evidence]
  RAW --> MIN[Minimisation, redaction and purpose enforcement]
  MIN --> FEATURE[Validated environmental feature with lineage]
  FEATURE --> WARN[Public-warning support]
  FEATURE --> AGG[Aggregate hazard and loss analysis]
  FEATURE -.-> CLAIM[Claim-specific review under a separate lawful basis]
  BLOCK[Prohibited: unrelated underwriting, credit, marketing or surveillance]
  FEATURE -.-> BLOCK
```

**Figure 2.5 — Privacy and permitted-use boundary.** A shared raw source does not imply shared downstream permission.

Kenya's Data Protection Act establishes principles including lawful, fair and transparent processing, purpose limitation, data minimisation, accuracy, storage limitation and safeguards for transfers [9]. The General Regulations identify high-risk contexts relevant to catastrophe intelligence, including large-scale combination of datasets, systematic monitoring of public areas, innovative technologies and processing involving vulnerable groups [10]. A data-protection impact assessment is therefore an architecture prerequisite, not a final compliance attachment.

### 11.1 Data classification

Four operational classes are useful:

1. **Open environmental:** lawfully open, non-personal measurements such as aggregated rainfall, subject to licence and integrity.
2. **Controlled operational:** infrastructure status, detailed hazard geometry or partner data whose disclosure could create safety or contractual risk.
3. **Personal:** phone number, precise contributor location, identifiable image, voice, household or claim record.
4. **Highly restricted:** health information, children, injury imagery, identity documents, financial account or claims investigation material.

Classification follows content, not source label. A public social-media post remains personal data when it identifies a person. Public availability is not unlimited permission for insurance or credit use.

### 11.2 Consent and lawful basis

Interfaces explain who controls data, purpose, required and optional fields, recipients, retention, rights and emergency limitations in concise language. Consent, where used, must be specific and as easy to withdraw as to give. Public-interest or vital-interest grounds may be relevant in defined emergencies, but they do not authorise indefinite retention or unrelated reuse.

The permitted-use field expresses machine-enforceable categories such as `public_warning_support`, `scientific_state_estimation`, `emergency_response`, `aggregate_loss_analysis` or `claim_specific_review`. Cross-purpose release needs an approved rule and audit. Data contributed for community warning are not automatically used for individual underwriting or lending.

### 11.3 Minimisation and protection

The application defaults to approximate rather than precise public display; strips unnecessary metadata; blurs faces and number plates where raw identity is not needed; separates contact details; and limits free text. Role- and attribute-based access, strong authentication, encryption, tamper-evident logs and purpose-aware export protect retained data. Access to raw distress imagery is exceptional and monitored.

Retention is source- and purpose-specific. Derived, de-identified statistics may outlive raw personal content if re-identification risk is assessed. Deletion or withdrawal propagates through lineage where legally required, while an audit tombstone records that a governed removal occurred without retaining the deleted content.

### 11.4 Data-subject access and correction

A contributor can request access, correct location or time, challenge a derived assertion, withdraw where applicable or request deletion. Correction creates lineage, triggers recalculation where material and notifies downstream product owners. If a claim or public decision relied on the record, the decision owner—not the observation service—handles substantive reconsideration under its process.

## 12. Source-to-use controls

Admissibility depends on intended use. The same source can be adequate for situational awareness and inadequate for contractual adjudication.

| Source | Suitable initial uses | Important restrictions |
|---|---|---|
| KMD/WRA/NDMA/authorised products | official context, baseline and state-model input | preserve attribution, version and official status; do not edit warning |
| satellite-derived footprint | broad detection, mapping and state estimation | acquisition lag, processing uncertainty, licence and resolution |
| open crowd report | candidate detection, verification targeting | consent, location uncertainty, dependence, safety; not sole denial/payout evidence |
| trained field report | structured local measurement and impact validation | protocol adherence, calibration, worker safety and role scope |
| camera AI feature | screening and state-model emission | model/domain calibration; raw imagery privacy; not hazard state by itself |
| claim record | loss calibration and claim-specific workflow | coverage selection, privacy, contractual context, delayed development |
| mobile/network aggregate | mobility or communication disruption context | legal agreement, aggregation, re-identification and representativeness |

The source-to-use register has an owner who reviews legal basis, data quality, latency, spatial resolution, retention and licence. A new use case cannot inherit approval merely because the field already exists in the platform.

## 13. Safe degradation and continuity

```{.mermaid #fig-2-4 alt="Point-in-time event and knowledge timeline"}
timeline
  title Event time, knowledge time and immutable issue history
  0600 : Physical event begins
  0604 : Source captures observation
        : Event time recorded
  0606 : Platform receives observation
        : Knowledge time recorded
  0610 : Product version 1 issued
        : Evidence cutoff fixed
  0820 : Correction arrives
        : Successor observation and product version 2
  Later : Best-available reconstruction
        : Does not rewrite the 06:10 operational record
```

**Figure 2.4 — Point-in-time event timeline.** Later correction improves reconstruction without changing what was knowable at the earlier issue.

The observation layer assumes partial failure.

### 13.1 Source failure

Every feed has freshness, completeness and plausibility indicators. A stale gauge changes from `observed_normal` to `unavailable`; last observation remains visible with age. A satellite delay widens footprint uncertainty. A failed crowd channel prompts alternative SMS, voice, radio or field routes. Models receive missingness and source-health variables instead of forward-filled values that look current.

### 13.2 Connectivity and power failure

Field tools cache schemas, official safety messages and map tiles; store encrypted observations; and retry with idempotent identifiers. Regional operations retain printable forms, radio procedures and contact trees. Central services run across failure domains and test restoration. A cloud outage cannot be allowed to remove the only copy of official operating procedures.

### 13.3 Model and vendor failure

Model monitoring detects latency, input drift, output collapse and service error. The fallback hierarchy is: current validated model; previous approved model; transparent rule or physical baseline; manual expert workflow. The product clearly names degraded mode and widens uncertainty. Open schemas and exportable models/data support vendor exit. Contracts define emergency access, incident reporting and assisted migration.

### 13.4 Security incident

During suspected compromise, ingestion can quarantine a source or model without erasing evidence. Incident response identifies affected data, preserves forensic records, rotates credentials, informs controllers and authorities as required and validates recovery. An adversarial flood of reports is handled with rate controls and lineage clustering, not wholesale closure of community channels.

## 14. Observation-layer validation

Validation starts with a declared task and reference process. “Image accuracy” is too vague. A useful test might be: detect visible floodwater in georeferenced road images within 15 minutes, with calibration measured under day, night and heavy-rain strata, for verification prioritisation only.

### 14.1 Data and annotation validity

Annotation protocols define classes, ambiguous cases, spatial scale and adjudication. Multiple qualified annotators, inter-rater measures and expert review are used for difficult fire, pest and landslide labels. Train/test leakage is prevented at event, location, contributor and image-family levels. Near-duplicate frames remain in one split.

### 14.2 Perception performance

Detection uses precision-recall, class-specific average precision and calibration; segmentation uses intersection-over-union, boundary error and area bias; time series use probabilistic calibration and extreme-event performance; NLP uses intent/entity measures plus critical error review. Operational threshold evaluation includes verification workload and missed-event consequence.

Performance is stratified by hazard, geography, device, weather, light, language and coverage group. An improved global score with worse remote-area calibration is not an acceptable promotion. Uncertainty and abstention are evaluated: a model should be able to say “insufficient quality.”

### 14.3 Source reliability and fusion preparation

Reliability models are back-tested against independently verified events. Tests examine whether high-reliability bins are truly more accurate, whether feedback loops privilege already instrumented areas and whether adversaries can manufacture history. Priors and update rates receive sensitivity tests. A contributor never needs a high historical score for an urgent report to be displayed to a human verifier.

### 14.4 Point-in-time correctness

For sampled events, auditors reconstruct exactly what the pipeline knew at each decision time, including late records, corrections, model versions and outages. Lead-time claims use knowledge time. Historical improvements caused by later imagery are labelled reconstruction skill, not operational skill.

### 14.5 Promotion gates

A new observation model is a challenger. Promotion requires better or non-inferior calibration and task performance; acceptable subgroup results; latency and cost within limits; privacy/security review; explainable failure modes; rollback; and operator acceptance. Novelty is irrelevant. Failure to beat a transparent baseline results in rejection or continued research.

## 15. Twenty required safety scenarios

The following scenarios form part of acceptance testing.

1. **Copied false report:** propagation clustering limits evidentiary weight; human verification receives the cluster.
2. **Authentic, mislocated report:** geometry uncertainty remains explicit; the source is not punished for a device or entry error.
3. **Satellite/local contradiction:** acquisition time, cloud/quality and field provenance are compared; both remain visible.
4. **Stale flood gauge:** the model receives missingness and wider uncertainty, not a false stable level.
5. **Remote silence:** low coverage triggers uncertainty and outreach, not a “safe” classification.
6. **Poor vision conditions:** camera model abstains or lowers calibrated reliability in smoke, darkness, glare or heavy rain.
7. **Ambiguous drought onset:** continuous indicators and institutional stages remain distinct; no artificial start is invented.
8. **Cross-border locust movement:** event geometry and wind-driven movement cross county/national boundaries; ownership is escalated.
9. **Landslide isolation:** offline capture, radio/manual routes and cached procedures operate.
10. **Heat-drought-fire-power compound:** shared dependencies are represented; consequence is not double-counted.
11. **Trigger without local loss:** the observation layer supplies independent trigger and impact evidence; contract dispute rules govern outcome.
12. **Loss without trigger:** local evidence is retained; contractual non-payment does not erase observed impact.
13. **Impermissible insurer use:** purpose controls block reuse of mid-event community data for cancellation or retrospective restriction.
14. **Official/model disagreement:** display identifies the official level and separate model estimate; escalation is logged.
15. **Cloud/vendor outage:** edge capture, manual workflow and baseline products continue with visible staleness.
16. **Access/correction/deletion request:** identity is verified, lineage traced and lawful action propagated.
17. **Better discrimination, worse subgroup calibration:** promotion fails pending remediation.
18. **Advanced model loses to baseline:** baseline remains champion.
19. **Apparent avoided loss:** observation improvement is not labelled causal benefit.
20. **Expected loss presented as cash:** metadata states distribution, horizon and non-guaranteed status.

## 16. Hazard-specific admissibility examples

For flood, a geotagged waterline photograph can become a depth observation only when camera geometry, ground reference and timestamp meet a protocol; otherwise it is presence evidence. For drought, a pastoral report of livestock condition is a structured ordinal observation tied to species, sample and locality, not a direct monetary loss. For fire, a thermal anomaly is a candidate active-fire feature conditioned on sensor quality, not confirmed ignition cause. For locust, an image classifier's species label remains provisional until survey validation where control action is consequential. For landslide, a crack report retains location uncertainty and does not become a probability without terrain and rainfall context. For heat, a symptom report may support aggregated situational awareness but requires health-data controls and cannot diagnose an individual.

These distinctions are intentionally conservative. They preserve the information content of imperfect reports while preventing downstream systems from assigning more meaning than the source can support.

## 17. Operating responsibilities

The observation-service owner maintains schemas, ingestion, lineage and source health. Dataset stewards manage quality and access for their domains. Source institutions retain ownership and attribution. The data controller determines purposes and rights; processors operate documented services. The model owner maintains perception models; independent validators challenge them. Product owners decide whether an observation class is fit for a particular workflow.

A cross-institution data-governance forum approves source onboarding, schema change, use expansion and retention. An emergency operations forum handles live discrepancies without changing long-term policy. Community representatives participate in channel and safeguard design. Security and data-protection officers possess stop authority for serious incidents.

## 18. Limitations

No schema eliminates ambiguity. Calibration truth is often delayed or contested. Remote sensing has revisit and resolution limits; field networks have safety and representation constraints; telecommunications can fail; multilingual NLP resources are uneven; exposure and institutional records can be incomplete. Privacy-preserving aggregation can reduce local analytical utility. Strong identity controls can exclude anonymous yet valuable reporters.

Trade-offs must be explicit and use-specific. High-stakes claim or public decisions require stronger evidence than early verification queues. The architecture cannot make an unsafe collection task acceptable. It cannot turn a selective claims portfolio into a population loss census. It cannot infer absence from silence.

## 19. Detailed channel and field protocol

### 19.1 Smartphone and messaging submission

The first screen identifies the authorised programme and emergency limitations. The contributor selects hazard and observable condition rather than estimating institutional severity. A flood form might ask whether water is on a road, entering buildings or moving rapidly; a fire form asks smoke/flame and direction; a pest form asks insect form and affected vegetation. Optional media follows a safety reminder. The interface records whether location/time are automatic, edited or unknown and allows an uncertainty description such as “near the market.”

Before submission, a concise permission panel states uses. The application creates a local UUID, encrypts payload and displays queued/sent/received status. A receipt is not validation or promise of response. Moderation and model results never publicly identify the contributor. Urgent life-safety content is routed under a predefined escalation protocol with an explicit statement that the channel is not a replacement for emergency contact.

WhatsApp or comparable messaging uses a verified institutional account and conversational state machine. Media are copied into the governed store only after notice/choice appropriate to the purpose. The system minimises group ingestion because group membership and unrelated messages create disproportionate collection. Forwarded-message metadata informs lineage but is not treated as dishonesty.

### 19.2 SMS, USSD and voice

SMS uses compact codes plus free-text fallback. The parser returns a confirmation summarising interpreted location and condition so the contributor can correct it. USSD supports structured menus without persistent handset data, but session limits require progressive save. Neither channel assumes GPS. Place dictionaries include formal and locally used names with human-maintained aliases.

Voice and call centres serve literacy, language, disability and connectivity needs. Operators use scripts that distinguish observation from inference, read back critical fields and avoid asking for unnecessary identity. Translation is recorded as a derived layer; original meaning and uncertainty remain. Audio retention is short unless required for a stated purpose, while structured records can be retained longer.

### 19.3 Trusted reporter and field measurement

Training is hazard- and role-specific: safe observation positions, standard depth references, rainfall or vegetation protocols, pest sampling, slope warning signs, heat/health escalation, device/time checks and consent for photographs. Field kits identify calibration and custody. A report records protocol version and deviations.

Supervision uses supportive quality review. A reporter who flags uncertainty is not penalised. Deliberate fabrication follows a separate due-process path; routine error informs retraining. Rotating coverage and stratified recruitment reduce geographic and social bias. No reporter is tasked to enter restricted or dangerous areas to improve model coverage.

### 19.4 Institutional bulk feeds

Machine feeds use mutual authentication, schema contract, event-time watermark, checksum and service-level metadata. The producer controls authoritative correction; the platform creates a successor version. Batch files include manifest, record count, time coverage, coordinate system, units and licence. Reconciliation compares expected and received counts and creates a source incident for unexplained gaps.

## 20. Data-quality rulebook

Quality rules are declarative, versioned and source-specific.

**Conformance** checks required fields, enumerations and parsable time/geometry. **Plausibility** checks ranges and rates of change, while allowing physically possible extremes. **Consistency** compares unit, geometry and related variables. **Freshness** compares expected cadence. **Completeness** measures missing intervals/attributes. **Uniqueness** uses both record key and content lineage. **Representativeness** compares coverage with target geography and population. **Integrity** verifies signatures/checksums and transformation chain.

Rules produce flags and actions: accept, accept with uncertainty, quarantine, request correction or reject. Rejection never deletes raw evidence. For example, a rainfall value of `120` without unit is quarantined for quantitative use but could remain visible to the steward. A crowd image with no location remains a candidate event signal, not a spatial observation. A gauge beyond its rated range is censored/flagged rather than clipped silently.

Quality scores are vectors, not one average. A record can have excellent timing and poor geometry. Downstream models select relevant dimensions. A public-warning product might value timeliness; property-level assessment requires stronger geometry. Weighted scores are permitted only when weights and use are documented.

Data-quality incidents have severity, owner, containment, affected products, time window and remediation. Products built during the window are marked and, if material, reissued. The catalogue displays historical reliability so planners can prioritise network investment without punishing communities.

## 21. AI model lifecycle at the observation layer

### 21.1 Problem and dataset definition

The model owner specifies observable, decision-support task, eligible inputs, label ontology, latency, abstention and prohibited use. Dataset documentation covers geography, events, source, capture conditions, consent/licence, annotation, imbalance, preprocessing and known gaps. Images from the same event/location/contributor family remain in one split.

### 21.2 Training and calibration

Augmentation reflects plausible optics without inventing physically misleading scenes. Class imbalance is addressed with sampling/loss and reported prevalence. Hyperparameter search is contained within training/validation. A final event/location holdout is untouched. Raw detector scores undergo calibration on representative data; calibration uncertainty is reported.

For multilingual NLP, native speakers review critical intents, negation, uncertainty and place extraction. For anomaly models, genuine extremes are protected through event review. Segmentation masks receive boundary and inter-rater analysis. Model performance is compared with human/manual and simple threshold baselines.

### 21.3 Deployment and monitoring

The registry stores artefact checksum, code, environment, schema, threshold, calibration, training snapshot and approval. Canary/shadow deployment compares outputs without controlling action. Runtime monitoring includes input drift, image quality, class frequency, calibration proxies, abstention, latency, hardware, geographic coverage and incident reports.

Ground truth arrives late, so immediate monitoring uses proxy health while delayed labels update performance. Drift does not automatically trigger retraining; it triggers diagnosis. A change in report pattern can reflect a new hazard or channel campaign rather than model decay.

### 21.4 Retraining, rollback and retirement

Retraining has a declared reason and versioned data. New data affected by prior model decisions are checked for feedback loops. Promotion repeats subgroup, privacy, security and operator review. Rollback restores model, calibration and threshold together. Retirement removes live use while preserving audit artefacts and retention rules.

## 22. Worked provenance records

### 22.1 Derived flood polygon

`OBS-RADAR-1042` references Sentinel scene acquisition at 18:02 UTC, processor ingestion at 18:31, terrain correction, quality mask and segmentation `FSEG-3.2`. Its polygon geometry is probabilistic, resolution 10 m, with water class calibration by land-cover stratum. At 19:10 an analyst removes a known permanent water body using versioned mask `PW-2026-04`. The successor retains both lineages. A state model run at 18:45 cannot use the correction; a 19:20 run can.

### 22.2 Crowd road report

`OBS-CROWD-881` records event time 06:12 from device, knowledge time 06:14, location accuracy radius 180 m, photograph hash and permitted use `public_warning_support`. Four reposts form cluster `DUP-55` rooted in the same media. NLP extracts “road impassable” with uncertainty, while the image model detects water/vehicle. A verifier confirms the road name by telephone and issues successor geometry. The raw phone number stays outside analytical storage.

### 22.3 Stale drought sensor

`OBS-BORE-77` normally reports hourly water level. Source health shows battery decline and no transmission after day 4. The last level is not forward-filled. Missingness is emitted with sensor-health reason; the drought model widens water-access uncertainty and requests a field check. When data reconnect, event times preserve the original measurements while knowledge times show delay.

### 22.4 Locust field survey

A trained officer submits species candidate, lifecycle stage, transect, approximate density, wind and treatment status under protocol `LOC-2`. Vision classification is stored as derived support, not the primary species record. The plant-protection authority later verifies and corrects stage; the event trajectory is replayed for evaluation without pretending the correction was known operationally.

## 23. Interoperability and alert boundaries

External interfaces use stable schemas, explicit version negotiation and machine-readable quality. Hazard products can use the Common Alerting Protocol for distribution where an authorised alerting institution adopts it; WMO describes CAP as a standard format for all-media public warning [11]. The intelligence platform does not assign itself as alert originator. It can package a model advisory for internal use and link to the authoritative CAP message.

APIs support as-of queries, spatial/temporal subsets, lineage, uncertainty and revocation. Bulk export includes manifest and permitted-use terms. Rate limits and aggregate privacy prevent portfolio or household reconstruction. Consumers acknowledge product version and expose stale/degraded status.

## 24. Observation architecture acceptance checklist

A source is production-admissible only when owner, purpose, legal basis, method, unit, time, geometry, quality, lineage, permitted use, retention, correction, outage and fallback are documented. A perception model is admissible only when task, domain, calibration, subgroup performance, abstention, version, monitoring and rollback are documented. A derived feature is admissible only when input and transformation lineage are recoverable.

A product fails if it averages confidence without a generative interpretation, treats reposts as independent, reads missingness as safety, hides acquisition/knowledge time, uses a model beyond resolution, exposes a contributor, repurposes data without approval, silently replaces an official source or cannot operate in degraded mode.

## 25. Coverage and representativeness audit

An observation network is audited against the population and physical process it aims to observe. The denominator is not “people who opened the app.” For flood it includes catchments, drainage settings, roads and exposed settlements; for drought, livelihood zones and seasonal mobility; for fire, fuel/ecology and response access; for locust, survey routes and cropping; for landslide, susceptible hillslopes; for heat/storm, station/urban/service and vulnerable exposure.

Coverage metrics include probability of at least one source within a decision window, source diversity, effective independent observations, latency, location precision and field-verification access. They are stratified by connectivity, remoteness and relevant community characteristics under privacy control. Dense reposting does not increase effective coverage.

A missingness model estimates reporting opportunity using network, population/activity, channel awareness and source health. The hazard model consumes opportunity separately from hazard evidence. Targeted sensor/field investment is prioritised where uncertainty and consequence are both high; report-count incentives do not substitute for representative design.

Audit results are shared with communities and source owners so apparent gaps can be challenged. A place can be physically observable by field networks despite low smartphone density. Conversely, many posts can describe the same visible road while hinterland impacts remain unknown.

## 26. Observation incident playbooks

**False-content surge:** quarantine suspect clusters from automated fusion, keep independent feeds live, route expert verification, communicate only through authorised channels, preserve evidence and avoid public attribution until due process.

**Clock or coordinate defect:** mark affected device/source/time range, transform only under verified correction, replay derived products, notify owners and retain original. If correction is uncertain, geometry/time remains a distribution.

**Sensor calibration failure:** stop quantitative use, retain qualitative/outage status, switch predefined fallback, assess products/decisions, repair/recalibrate and backfill only with correct knowledge-time labels.

**Personal-data exposure:** contain access/export, preserve forensic log, notify controller/security/privacy owners, assess affected persons and legal notification, rotate credentials, remove public copies where possible and review purpose/minimisation.

**Model collapse or drift:** disable derived feature or revert approved version, widen state uncertainty, preserve raw/manual observations, inform product users and investigate domain shift before retraining.

**Vendor/cloud outage:** activate edge/manual queue and alternative authoritative feeds, display degraded service, capture delivery receipts, restore from tested backup, reconcile idempotently and run post-incident review.

## 27. Annotation and verification operations

Verification queues are prioritised by potential consequence, information gain, source uncertainty and operational deadline—not by likely financial value alone. A high-consequence remote report can outrank many easy urban images. Queue policies are documented and audited for geography.

Annotators see only necessary data and are trained in hazard ontology, uncertainty, privacy and distress content. Interfaces permit `uncertain`, `not visible`, `wrong task` and escalation. Gold/adjudication samples estimate drift and agreement. Productivity targets cannot encourage forced labels. Sensitive imagery has tighter teams, viewing controls and wellbeing support.

Verification truth has levels: source integrity verified; location/time verified; visible class verified; field/authoritative condition confirmed; consequence confirmed. One level is not silently promoted to another. An image can be authentic and still irrelevant or misinterpreted.

Feedback to contributors distinguishes received, under review, corroborated and routed. Public response never reveals a reporter's reliability score. Corrections are welcomed, linked and propagated.

## 28. Functional non-vendor reference flow

The implementation can be expressed without mandating technology:

1. channel adapters authenticate and create immutable raw envelopes;
2. privacy/safety service separates identity, redacts and enforces permitted use;
3. schema/time/geometry/quality service creates validated records;
4. lineage service clusters duplicates and records derivations;
5. perception services create versioned candidate features;
6. human/scientific verification creates successor evidence;
7. event stream and point-in-time store expose admissible observations;
8. catalogue/monitoring records ownership, quality and incidents;
9. signed product delivery sends only purpose-appropriate views;
10. replay/archival reconstructs operational and best-available histories.

Each boundary supports export and independent testing. Identity need not enter analytical compute. Raw evidence can have shorter retention than validated environmental features. A named lakehouse, queue, cloud or detector is replaceable if these behaviours hold.

## 29. Minimum pilot data package

A pilot begins with source samples across normal and event conditions, metadata/quality history, authoritative product archive, geospatial foundations, event catalogue, verification truth, community/channel research and explicit observation gaps. It includes no production personal or claim data until permission and environment are ready.

The package supports six micro-tests: flood presence/depth/location; drought component and reporting opportunity; fire smoke/flame under adverse optics; locust species/stage/movement report; landslide crack/blockage geometry; storm/heat multilingual consequence. These tests validate schemas and failure modes, not a national model.

Exit criteria are measurable: acceptable schema/lineage completeness; calibration for the stated AI task; independent-coverage gain; safe participation; rights and incident workflows; fallback; and evidence that downstream state modelling can consume uncertainty. Failure results in channel/model revision or stop, not relaxed truth definitions.

## 30. Operational event-time walkthrough

At preparedness time, stewards verify source health, reporter coverage, model versions, retention and fallback. Official forecast feeds enter with attribution. The platform does not solicit risky field observations merely because an event is possible. Product owners confirm which users are on duty and when cached material expires.

At first detection, adapters create raw envelopes and quality services validate time, geometry and source status. Duplicate clustering prevents propagation inflation. AI features enter as candidates. A human or scientific verifier receives high-consequence/uncertain cases. The state model consumes admitted observations with source-specific likelihoods and explicit missingness.

As the event evolves, late data update current products according to lookback rules; issued versions remain immutable. Contradictions are displayed and escalated. The operator sees effective independent roots, not post count. Community contributors receive receipt and useful authorised information, while identity remains separated. Raw distress media are not broadcast to institutional consumers.

During feed failure, source-health changes immediately; last value shows its age; fallback activates. A satellite delay or cloud problem widens state uncertainty. Store-and-forward captures offline evidence. If the platform itself fails, official channels and manual operating procedures continue. Restoration reconciles idempotently and identifies products affected during outage.

After physical conditions recede, observation continues for duration, damage and recovery under separate purposes. Claims or survey evidence does not leak backward into operational detection scores. Best-available reconstruction is built as a new product. Contributors can correct or withdraw under applicable rules, and corrections propagate through lineage.

Finally, stewards close the event with source/coverage/calibration, privacy/security, user and community review. Data are retained or deleted by schedule. Model errors are classified before retraining. The event becomes a holdout or calibration candidate only under an approved dataset process. This lifecycle makes the observation layer a governed memory of what was seen and known, not a mutable collection of convenient facts.

The handoff to Part 3 is therefore a contract, not a bulk export. It contains admissible observations and explicit gaps at native time/geometry, plus source-health, dependence and permitted-use metadata. Downstream modelling may reinterpret likelihood but cannot erase provenance, invent absent variables or expand the legal purpose. A state-model correction that reveals an observation problem returns through the steward workflow instead of overwriting raw evidence.

## 31. Conclusion

The observation architecture turns raw signals into admissible evidence by preserving what was measured, when, where, how, by whom or what, with what quality, under which permission and through which transformations. Crowd intelligence expands coverage but remains unequal and dependent. AI structures evidence but does not create institutional truth. Edge/cloud design supports continuity, while point-in-time lineage makes evaluation and audit possible.

The key output is not a cleansed fact table stripped of doubt. It is a reproducible, uncertainty-bearing observation layer. Part 3 uses that layer to estimate hazard states, occurrence, footprint, intensity and duration without confusing source confidence with physical probability.

## References

[1] European Space Agency, “Sentinel-1 focuses on floods,” accessed Aug. 26, 2026. [Online]. Available: https://sentinels.copernicus.eu/web/success-stories/-/sentinel-1-focuses-on-floods

[2] National Drought Management Authority, “Drought information,” accessed Aug. 26, 2026. [Online]. Available: https://ndma.go.ke/drought-information/

[3] Food and Agriculture Organization of the United Nations, “eLocust3K,” accessed Aug. 26, 2026. [Online]. Available: https://www.fao.org/locust-watch/activities/dlis-home/elocust3k/en

[4] Plant Protection and Food Safety Directorate, “Desert locust,” accessed Aug. 26, 2026. [Online]. Available: https://plantprotection.kilimo.go.ke/desert-locust/

[5] U.S. Geological Survey, “Overview of rainfall-induced landslides,” accessed Aug. 26, 2026. [Online]. Available: https://www.usgs.gov/programs/landslide-hazards/science/overview-rainfall-induced-landslides

[6] Kenya Meteorological Department, “Weather forecasting services,” accessed Aug. 26, 2026. [Online]. Available: https://meteo.go.ke/Services/weather-forecasting/

[7] Water Resources Authority, “Surface water assessment and monitoring,” accessed Aug. 26, 2026. [Online]. Available: https://wra.go.ke/surface-water-assesment-monitoring/

[8] Kenya Forest Service, “Forest protection and security,” accessed Aug. 26, 2026. [Online]. Available: https://www.kenyaforestservice.org/forest-protection-and-security/

[9] Republic of Kenya, *Data Protection Act*, No. 24 of 2019. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24

[10] Republic of Kenya, *Data Protection (General) Regulations*, Legal Notice No. 263 of 2021. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng%402022-12-31

[11] World Meteorological Organization, “WMO Common Alerting Protocol,” accessed Aug. 26, 2026. [Online]. Available: https://wmo.int/site/wmo-common-alerting-protocol/about-cap
