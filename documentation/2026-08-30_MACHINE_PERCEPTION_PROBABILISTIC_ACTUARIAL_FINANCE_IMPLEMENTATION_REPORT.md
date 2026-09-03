# Machine-Perception, Probabilistic, Actuarial and Finance Implementation Report

**Implementation date:** 30 August 2026  
**Project:** Spatial Catastrophe Risk Intelligence (SCRI)  
**Author:** Nevil Maloba  
**Implemented plans:**

- `guidance/shared_plans/01_SHARED_MACHINE_PERCEPTION_IMPLEMENTATION_PLAN.md`
- `guidance/shared_plans/02_SHARED_PROBABILISTIC_ACTUARIAL_AND_FINANCE_EXPANSION_PLAN.md`

## 1. Preservation record

The pre-implementation edition was copied to:

`documentation/snapshots/2026-08-30_pre_machine_perception_probabilistic_actuarial_finance_expansion/`

The snapshot contains Parts 2–5, the appendices and the relevant controls. The implementation was additive: the existing distributed-sensor narrative, Nzoia actuarial example, four-desk insurance journey and resilience cash-flow bridge remain in place and now lead into deeper product, mathematical and institutional layers.

## 2. Machine-perception implementation

Part 2 now treats Ultralytics as a version-neutral machine-perception workbench rather than treating YOLO as the entire AI architecture. Vision transformers remain in the product portfolio. RT-DETR, SAM/SAM 2, ViT, Swin, SegFormer, YOLOE and comparable models are challengers behind a common result contract.

Implemented capabilities include:

- object detection;
- instance and semantic segmentation;
- multi-object and mask tracking;
- oriented bounding boxes;
- monocular-depth evidence with camera, terrain, gauge and hydraulic reconciliation;
- bounded pose-estimation use for rescue assistance;
- open-vocabulary discovery and promptable annotation;
- specialised SAR, multispectral, drone and change-analysis interfaces;
- a model-agnostic perception-result schema;
- a Kenya-specific dataset and annotation programme;
- event, geography, sensor, season and extreme-condition holdouts;
- active learning and origin-aware splitting;
- calibration, conformal prediction and six-part uncertainty treatment;
- edge, county-server and cloud deployment tiers;
- hardware, export, licence and dependency controls;
- decision-weighted validation and shadow-mode promotion;
- flood, drought, wildfire, locust, landslide, storm and heat adapters; and
- detailed wildfire and drought product-interface journeys.

Part 2 contains approximately 7,792 substantive Pandoc-counted words, close to the plan's 8,000–8,500-word range without adding repetitive text.

## 3. Probabilistic-inference implementation

Part 3 now specifies how SCRI constructs an operational posterior. The main update uses the full predictive prior and source-specific likelihoods. It models:

- gauge measurement and stale-data uncertainty;
- detector sensitivity, specificity and calibration;
- segmentation, satellite and institutional observations;
- missing-not-at-random reporting through access and connectivity;
- contextual, hierarchical source reliability;
- latent common origins for copied reports, frames and shared acquisitions;
- event time, knowledge time, filtering, fixed-lag smoothing and replay;
- change of support across points, lines, rasters, polygons and zones;
- action-dependent physical transitions;
- seasonal, county and structural nonstationarity;
- posterior sample delivery to the actuarial engine; and
- held-out predictive stacking and champion-challenger promotion.

Equations (3.1)–(3.14) are sequential. Appendix E extends the derivations through (A3.20).

## 4. Actuarial-modelling implementation

Part 4 retains the synthetic Nzoia worked example and adds:

- uncertain value, geocoding, occupancy, construction and condition;
- vulnerability-parameter uncertainty;
- no-damage and total-loss probability masses;
- censored and truncated claims;
- demand surge, inflation, leakage, fraud, salvage and subrogation;
- loss-adjustment expenses;
- business interruption, restoration and network effects;
- event-definition, clustering, hours-clause and collectability treatment;
- a catastrophe-informed reserve posterior;
- paid, RBNS, IBNER, IBNR, reopening, LAE and recoveries;
- chain-ladder, Bornhuetter–Ferguson, Cape Cod, Mack, bootstrap/GLM and claim-level baselines;
- IFRS 17 fulfilment-cash-flow translation;
- one-year economic-capital modelling;
- VaR and TVaR;
- regulatory capital, internal capital, IFRS 17 risk adjustment and transaction margin separation;
- Euler capital allocation, RAROC and reverse stress;
- reinsurance optimisation with capital and liquidity constraints; and
- explicit distinction between event percentiles and annual return periods.

Equations (4.1)–(4.20) are sequential. Appendix F extends the actuarial derivations through (A4.32).

## 5. Investment, sustainable-finance and resilience-finance implementation

Part 5 preserves the one-flood/four-desks story and implements a finance engine with four linked ledgers:

1. risk;
2. intervention;
3. finance; and
4. monitoring, reporting and verification.

The investment layer now includes hazard-adjusted operating cash flow, downtime, restoration, CFADS, DSCR, conditional PD/LGD/EAD translation, NPV, IRR, portfolio dependency and staged-adaptation option value.

Eight finance-product journeys are developed:

- resilience loan;
- green or adaptation bond;
- sustainability-linked finance;
- parametric insurance;
- contingent credit;
- resilience bond;
- blended or results-based finance; and
- county or sovereign disaster-risk finance.

The Kenyan institutional pathway now references the CBK Green Finance Taxonomy and Climate Risk Disclosure Framework, CMA green-bond guidance, IRA Principles of Sustainable Insurance and Kenya Disaster Risk Financing Strategy 2026–2030. Every numbered reference contains an explicit HTTPS URL.

Equations (5.1)–(5.6) are sequential. Appendix G extends the finance derivations through (A5.20).

## 6. Controls and mathematical supplements

The following controls were reconciled:

- `SOURCE_TO_USE_REGISTER.md`: exact new technical, actuarial and Kenyan finance sources, URLs, intended uses and limitations;
- `CLAIM_AND_EVIDENCE_LEDGER.md`: new claims CE-035 through CE-047;
- `FIGURE_AND_TABLE_REGISTER.md`: new perception, posterior and finance diagrams;
- `HAZARD_COVERAGE_MATRIX.md`: peril-specific perception, observation-process, posterior-to-loss, reserve/capital and four-ledger coverage;
- `SHARED_NOTATION_AND_DEFINITIONS.md`: new observation, perception, reserve, capital, credit and ledger notation; and
- `VALIDATION_AND_REVIEW_LOG.md`: implementation status, word counts and remaining gates.

Appendices D–G now contain sequential derivations for contextual reliability, missing reporting, common origins, conformal coverage, delayed evidence, change of support, controlled transitions, posterior Monte Carlo, nonstationarity, stacking, uncertain loss, reserve posteriors, IFRS 17 cash flows, TVaR, Euler allocation, reinsurance optimisation, finance-ledger reconciliation, DSCR breach probability, credit loss, real options and performance-linked verification.

## 7. Validation completed

- A pre-change snapshot exists.
- Parts 2–5 and the appendices parse through Pandoc.
- Mermaid blocks in the modified manuscripts render through `build/pandoc/mermaid-filter.lua`.
- New diagrams use coloured fills/backgrounds and 22 px source typography.
- The widest new promotion diagram was redesigned into a two-row layout for normal-scale reading.
- Main equations are sequential in Parts 2–5.
- Appendix equation series A2, A3, A4 and A5 contain no gaps or duplicate tags.
- All in-text numbered citations in Parts 2–5 resolve to a reference entry.
- All 42 reference entries in Parts 2–5 include explicit HTTPS URLs.
- The current seven-part manuscript set contains approximately 31,543 substantive Pandoc-counted words.

## 8. Publication and validation gates that remain

The targeted implementation is complete at manuscript-design level. The original 48,000–52,000-word book-scale boundary remains a later editorial objective. The strongest next additions are empirical rather than repetitive:

- point-in-time Kenyan event reconstructions for additional perils;
- Kenya-specific perception benchmark datasets and field protocols;
- claims-linked vulnerability and reserve calibration;
- economic-capital calibration inside participating insurers;
- lender-owned PD/LGD/EAD validation;
- worked financing transactions with real sponsors, repayment sources and verifier terms;
- community, legal, regulatory, actuarial, hazard-science and investment review; and
- a complete PDF rebuild and page-by-page visual review after those cross-part additions are reconciled.

The present implementation supplies the coherent product spine required for that work:

> Pixels become calibrated observations; observations become posterior catastrophe states; catastrophe states become loss, reserve and capital distributions; those distributions become institution-specific insurance, investment and resilience-finance products.
