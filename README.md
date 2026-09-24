# Spatial Catastrophe Risk Intelligence

**Status:** Positive product-narrative and diagram-legibility edition built and visually verified  
**As-of date:** 29 August 2026  
**Geographic focus:** Kenya  
**Primary hazards:** flood, drought, wildfire and rangeland fire, locust and catastrophic crop pests, rainfall-induced landslide, severe storm and extreme heat

**Author:** Nevil Maloba

## Series question

How can real-time crowd intelligence, YOLO and other artificial-intelligence perception, earth observation and environmental sensors be converted into actuarial modelling that helps a Kenyan insurer understand catastrophe risk continuously, act earlier, settle losses more intelligently and manage portfolio accumulation without confusing a changing risk estimate with permission to rewrite an insurance contract?

The working product is an insurer-facing continuous catastrophe-underwriting capability. It observes an evolving event, estimates the physical state, converts that state into insured portfolio loss and supports underwriting, claims, accumulation and reinsurance workflows. Public and resilience uses remain adjacent applications rather than the centre of every chapter.

## Workspace layout

- `manuscripts/` — the six substantive parts and appendices used in the compiled volume.
- `sources/project/` — the two original project-nucleus Markdown files.
- `guidance/` — methodological and narrative guidance that is not manuscript subject matter.
- `controls/` — notation, evidence, hazard-coverage, figure and validation registers.
- `reports/` — tone diagnosis, PDF-production notes and detailed criticism.
- `references/` — the benchmark white paper used for narrative and production comparison.
- `build/` — the supported Pandoc script, Lua filters and PDF configuration.
- `documentation/` — preserved earlier editions and snapshots.
- `output/` — generated deliverables.
- `tmp/` — disposable build intermediates.

## Manuscripts

1. [The Kenya Insurtech Product and the Livelihoods It Protects](manuscripts/01_KENYA_MULTI_HAZARD_INTELLIGENCE_THESIS.md)
2. [The Distributed Sensor Network](manuscripts/02_CROWD_AI_AND_OBSERVATION_ARCHITECTURE.md)
3. [The Catastrophe State Engine](manuscripts/03_SPATIOTEMPORAL_HAZARD_STATE_MODELLING.md)
4. [Actuarial Modelling](manuscripts/04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md)
5. [Continuous Catastrophe Underwriting](manuscripts/05_INSURANCE_INVESTMENT_AND_RESILIENCE_FINANCE.md)
6. [Building the Product](manuscripts/06_GOVERNANCE_VALIDATION_AND_IMPLEMENTATION.md)
7. [Appendices](manuscripts/07_APPENDICES.md)

The [product-narrative redesign brief](guidance/PRODUCT_NARRATIVE_REDESIGN.md) and the [positive product-narrative and diagram-legibility plan](guidance/POSITIVE_PRODUCT_NARRATIVE_AND_DIAGRAM_LEGIBILITY_PLAN.md) control the current edition. The previous governance-led edition is preserved under [documentation/2026-08-26_policy-framework-draft](documentation/2026-08-26_policy-framework-draft/SNAPSHOT.md).

## Reports

The [reports index](reports/README.md) links the implementation and review records kept outside the manuscript, including:

1. [Tone and product-narrative diagnosis](reports/01_TONE_AND_PRODUCT_NARRATIVE_DIAGNOSIS.md)
2. [PDF production and formatting report](reports/02_PDF_PRODUCTION_AND_FORMATTING_REPORT.md)
3. [Detailed white-paper critique](reports/03_DETAILED_WHITE_PAPER_CRITIQUE.md)
4. [Critique implementation log](reports/04_CRITIQUE_IMPLEMENTATION_LOG.md)
5. [Sample edition implementation and review pack](reports/05_SAMPLE_EDITION_IMPLEMENTATION_AND_REVIEW_PACK.md)
6. [Positive narrative and diagram-legibility implementation](reports/06_POSITIVE_NARRATIVE_AND_DIAGRAM_LEGIBILITY_IMPLEMENTATION.md)

## Compiled PDF

The current reviewed publication, [Spatial Catastrophe Risk Intelligence White Paper](output/pdf/Spatial_Catastrophe_Risk_Intelligence_White_Paper.pdf), is generated reproducibly with Pandoc, XeLaTeX and the local Mermaid Lua filter. The reader edition is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/), except where otherwise noted:

```powershell
.\build\build-pdf.ps1
```

The filter renders executable Mermaid snippets to publication graphics during the Pandoc build; the Markdown remains the editable source of truth. One-off repair scripts are retained in `build/legacy/` for provenance but are not part of the supported build.

## Edition target

The edition targets one integrated, approximately 160–170-page white paper. Each part contains a small number of substantial chapters rather than a catalogue of micro-sections. Part 1 supplies the narrative and commercial template; Parts 2–6 inherit its product vocabulary, Kenyan livelihood grounding and chapter rhythm.

## How to read the series

Part 1 states the common thesis and institutional problem. Part 2 defines what counts as admissible, point-in-time evidence. Part 3 turns observations into hazard states and event distributions. Part 4 converts hazard into physical and financial loss. Part 5 assigns those outputs to insurance, investment, public-finance and resilience-finance decisions. Part 6 defines authority, controls, validation, pilots and safe scale.

The papers are independently citable. Each repeats the minimum definitions needed to stand alone, while links and a shared notation register prevent important concepts from drifting across the series.

## Project boundaries

The substantive starting points are [the Kenya flood architecture](sources/project/kenya-flood-loss-intelligence-architecture.md) and [the crowd/AI actuarial workshop](<sources/project/How can crowd intelligence (wisdom of crowds) and Artificial Intelligence, YOLO etc be used for carlifornia wildfires combine with actuarial loss.md>). California examples in the workshop are hypotheses and analogies, not Kenyan evidence.

[The Actuarial Modelling Charter](guidance/ACTUARIAL_MODELLING_CHARTER.md) and the [Mwendo Pamoja benchmark](references/Mwendo_Pamoja_Continuous_Underwriting_White_Paper.pdf) are quality references only. This series does not extend their motor, credit, premium-finance, ERP, KESONIA or gig-driver project.

The series is research. It is not an official warning, actuarial opinion, rate filing, insurance contract, investment recommendation, accounting policy, legal opinion, regulatory approval or authority to automate a consequential decision.

## Shared controls

- [Notation and definitions](controls/SHARED_NOTATION_AND_DEFINITIONS.md)
- [Source-to-use register](controls/SOURCE_TO_USE_REGISTER.md)
- [Claim and evidence ledger](controls/CLAIM_AND_EVIDENCE_LEDGER.md)
- [Hazard coverage matrix](controls/HAZARD_COVERAGE_MATRIX.md)
- [Figure and table register](controls/FIGURE_AND_TABLE_REGISTER.md)
- [Reference URL audit](controls/REFERENCE_URL_AUDIT.md)
- [Validation and review log](controls/VALIDATION_AND_REVIEW_LOG.md)

## Citation and evidence policy

Each manuscript uses IEEE-style numerical references in order of first appearance. Kenyan law, official agencies, regulators and official methodologies take priority. International standards and supervisory materials are labelled comparative where they do not bind in Kenya. Peer-reviewed research supports scientific and statistical propositions. Vendor material and media are not used for substantive claims unless clearly labelled.

Time-sensitive claims are stated as of their documented research date. Illustrative quantities and synthetic cases are marked as such.
