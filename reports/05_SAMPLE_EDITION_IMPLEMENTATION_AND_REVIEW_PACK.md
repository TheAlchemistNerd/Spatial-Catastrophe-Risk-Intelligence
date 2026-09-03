# Sample Edition Implementation and Independent-Review Pack

**Date:** 28 August 2026  
**Status:** Internal sample build; independent review not performed

## What this continuation implements

The sample edition advances five items identified in the critique without claiming that the book-scale manuscript is complete:

1. Part 1 now reconstructs the 2024 long-rains floods, the 2019-2020 locust invasion and the January 2026 Isiolo drought signal. It distinguishes historical impact totals from what was knowable at an earlier event cut-off.
2. Part 4 now carries a transparent synthetic Nzoia flood portfolio from exposure and damage through policy terms, gross insured loss, occurrence reinsurance and net retention.
3. Three generated figures add an evidence-geography orientation map, an NDMA indicator profile and synthetic AEP/OEP curves.
4. Part 5 follows one event through accumulation, claims, reserving and reinsurance interfaces while preserving decision authority.
5. Part 6 states the independent-review lanes, closure evidence and red-line questions required before any production-readiness claim.

## Evidence boundary

The 2024 flood figures are sourced to the Kenya Meteorological Department's State of the Climate Report for 2024. Locust figures are sourced to the World Bank's Kenya Locust Response Project account. Isiolo indicator values are transcribed from the NDMA January 2026 county bulletin.

The map uses approximate orientation points for evidence discussed in the manuscript. It is not a hazard, exposure or rating map. The actuarial portfolio and curves are synthetic. The fixed seed and assumptions are stored in `assets/figures/synthetic_flood_portfolio_results.json`; generation code is in `build/generate-sample-figures.py`.

## Reproducibility checks

- Re-run `build/generate-sample-figures.py` with the bundled Python runtime.
- Confirm the central ground-up, gross, recovery and retained values reconcile to KES 145.65m, KES 118.50m, KES 43.50m and KES 75.00m.
- Confirm event-loss P10, median, P90 and P95 are generated from the fixed seed rather than copied independently into a graphic.
- Confirm the annual process uses 100,000 synthetic years, a Poisson mean of 0.65 and the generated event-loss distribution.
- Confirm every figure caption states whether the underlying evidence is empirical, orientation-only or synthetic.

## Independent review assignments

| Lane | Minimum reviewer profile | Required output |
|---|---|---|
| Hydrology | Kenya basin/flood practitioner independent of model ownership | Written event-replay and physical-assumption findings |
| Drought/livelihoods | ASAL and NDMA-methodology expertise | Indicator interpretation and livelihood-pathway findings |
| Locust/agriculture | Pest surveillance/control and crop-loss expertise | Swarm, intervention and vulnerability findings |
| Actuarial | Fellow/qualified actuary with catastrophe and reinsurance experience | Reproducibility, terms, dependence, tail and use findings |
| Insurance operations | Claims, underwriting, reserving and reinsurance users | Task-based interface findings and conduct risks |
| Kenyan legal/privacy | Insurance, data-protection and public-authority counsel | Written authority, DPIA and contractual-use findings |
| Community/accessibility | Participatory research and accessible-service expertise | Contribution, exclusion, redress and accessibility findings |
| Security/continuity | Independent security and resilience practitioners | Threat, outage and recovery exercise findings |

No lane is complete merely because a reviewer has read the PDF. Findings must be logged, evidence-backed, assigned and dispositioned. Any unresolved high-severity mathematical, legal, privacy, customer-harm or institutional-authority issue prevents a production claim.

## Remaining work after this sample

- Historical point-in-time event replay using archived observation feeds.
- Licensed or open empirical hazard rasters and exposure overlays with spatial QA.
- Kenyan claims calibration, exposure normalisation and vulnerability functions.
- Product research with real insurer roles and customer/community participants.
- Peril-specific worked examples beyond flood.
- Accessibility, citation and copy-edit review at full book scale.
- All independent reviews listed above.

The sample PDF is therefore a design and authoring checkpoint. It demonstrates narrative and analytical integration while making the missing evidence impossible to mistake for completed validation.

## Sample build record

The sample was built through the repository's Pandoc pipeline with `mermaid-filter.lua` and XeLaTeX. The final internal sample contains 58 Letter-size pages and is stored at `output/pdf/SCRI_Sample_Expanded_Edition.pdf`. All pages were rendered with Poppler and inspected through five contact sheets; the newly added pages were also checked at full size. The final SHA-256 is `19BF724CA4E8D6B49E55C888B0FADE54CF7C62C6699F93D88A6E012047B95B2E`.

Visual QA corrected duplicate image captions and one Mermaid sequence syntax problem. No clipping, overlapping tables, missing figures or blank production pages remained. The PDF is not tagged, so accessibility remediation remains open before external publication.
