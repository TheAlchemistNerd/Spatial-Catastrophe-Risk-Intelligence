# Validation and Review Log

## Current revision status

**Revision date:** 29 August 2026  
**Revision:** Positive product-narrative and diagram-legibility implementation  
**Status:** Revised PDF built and visually validated; empirical calibration and independent review are the next release gates

| Review | Current status | Evidence or remaining work |
|---|---|---|
| Pre-revision preservation | Completed | Current pre-implementation manuscripts and critique copied to `documentation/2026-08-28_pre-critique-implementation/` |
| Product thesis and tone | First pass completed | Founder-led, human-to-financial narrative retained; policy-led and promotional language reduced |
| Six-hazard livelihood treatment | First pass completed | Part 1 now distinguishes basin flood, persistent drought, wildfire, locust, landslide, severe storm and heat pathways |
| Observation architecture | Reconstructed | Canonical schema, three clocks, provenance, duplicate clusters, source quality, edge/cloud fallback and privacy boundaries added |
| AI-role separation | Reconstructed | Detection, instance segmentation, semantic segmentation, physical-unit conversion and state estimation separated |
| Hazard-state modelling | Reconstructed | Polygon-as-model error removed; baselines, challengers, hazard-specific neighbourhoods and probabilistic state interfaces added |
| iHMM contradiction | Resolved | iHMM is an optional research challenger; no live-path dependency or categorical rejection remains |
| Actuarial dimensional consistency | Reconstructed | Event state, long-term occurrence, stochastic damage, policy terms, reinsurance, claims emergence and annual loss separated |
| Exposure double counting | Resolved in equations | Expected count and unit-rate formulations are explicitly alternative formulations |
| Tail and dependence claims | Reconstructed | Distribution choice is empirical; GPD threshold requirements stated; Gaussian and Student-$t$ copulas correctly characterised |
| Contractual decision boundary | Reconstructed | Continuous intelligence is separated from mid-event repricing, policy changes, claims authority and treaty changes |
| Parametric basis risk | Reconstructed | Elimination claim removed; contractual trigger and fallback requirements stated |
| Resilience-finance logic | Reconstructed | Avoided loss now requires a counterfactual; financing requires an issuer/borrower and lawful repayment source |
| Kenyan privacy treatment | Reconstructed | Data Protection Act, General Regulations, DPIA, roles, rights, retention and re-identification risk addressed |
| Governance and stage gates | Reconstructed | Owners, evidence gates, stop conditions, safe degradation and rollback added |
| Bibliography integrity | High-risk placeholders removed | All six reference lists were replaced with identifiable official, legal, primary or established professional sources; full source-by-source editorial audit remains required |
| Shared notation | Reconciled | Event/exposure indices, hazard neighbours, occurrence offset, stochastic damage and financial terms aligned with appendices |
| Mermaid architecture | Expanded | 22 substantive diagrams now express causality, model boundaries, financial transforms and stage gates |
| Pandoc parse | Completed for first pass | Full series parsed to HTML and LaTeX through the project filters |
| Citation/reference reconciliation | Completed for first pass | All six numbered reference sections match their in-text citation sequences; named placeholder sources are absent from current manuscripts |
| Mermaid rendering | Completed for first pass | All 22 Mermaid blocks rendered successfully through `mermaid-filter.lua` |
| PDF sample build and visual review | Completed | 58-page sample built with Pandoc/XeLaTeX; all pages inspected through five contact sheets, with full-size checks of new event, actuarial, product and review pages |
| Independent expert review | Not performed | Required before external research, actuarial or commercial claims |
| Kenyan event reconstructions | Expanded sample completed | 2024 floods, 2019-2020 locust invasion and January 2026 Isiolo drought; point-in-time replay still pending |
| Worked actuarial example | Synthetic demonstrator completed | Fixed assumptions, unit-level policy transform, occurrence layer, Monte Carlo quantiles and EP curves; empirical calibration pending |
| Data-grounded figures | Sample completed | Isiolo bulletin indicator profile and Kenya evidence-geography orientation map; empirical hazard raster/footprint still pending |
| Product-interface narrative | Expanded sample completed | Four insurer desks and shared evidence/version boundary; user research and usability testing pending |
| Independent review pack | Defined, not executed | Review lanes, red-line questions and disposition control added to Part 6 and report 05 |
| Positive narrative brief | Completed | Governing plan saved under `guidance/POSITIVE_PRODUCT_NARRATIVE_AND_DIAGRAM_LEGIBILITY_PLAN.md` |
| Narrative polarity audit | First pass completed | Defensive constructions reduced from 168 to 22; remaining instances concentrate in technical distinctions, permission tables and stop conditions |
| Product-led rewrite | First pass completed | Parts 1-6 now lead with capability, user workflow and accountable ownership before limitations |
| Diagram typography | Source changes completed | Mermaid source font increased from 18 px to 22 px; node/rank spacing and raster resolution increased |
| Dense diagram redesign | Completed and visually verified | Long chains use page-oriented layouts; product journey, stage gates, review loop and canonical architecture use the full text width |
| Landscape diagram support | Available in build system | Current accepted figures fit legibly in portrait; the filter retains landscape support for future genuinely wide assets |
| Positive product-narrative PDF | Completed | 65-page edition built with Pandoc/XeLaTeX and Mermaid Lua filter; all 65 pages inspected at 110 dpi, with full-size checks of dense diagrams |
| Positive product-narrative PDF checksum | Recorded | `8295219F2D9DDF12FEB6CF83D058BF92237B9A17CDD4E42D7ECBF13CCCDBDF4F` |
| Reference URL coverage | Completed | All 37 numbered reference entries across Parts 1-6 contain an explicit HTTPS source location; DOI-only and book-only entries were upgraded to resolver or publisher URLs |

## Pandoc word-count record

The expanded sample manuscript contains approximately 14,317 substantive plain-text words under the project’s Pandoc conversion rule:

| Part | Words |
|---|---:|
| Part 1 | 2,875 |
| Part 2 | 1,694 |
| Part 3 | 1,614 |
| Part 4 | 2,450 |
| Part 5 | 2,183 |
| Part 6 | 2,588 |
| Appendices | 913 |
| **Total** | **14,317** |

This is an expanded sample, not completion of the book-scale target. The sample now includes three Kenyan event reconstructions, one synthetic actuarial example, data-grounded figures, synthetic curves and a product workflow. Additional peril reconstructions, empirical hazard surfaces, claims calibration, field validation and independent review still require substantial work. No page-count or 48,000–52,000-word acceptance claim is made for this revision.

## Required independent review

The manuscripts require review by Kenyan or regionally experienced specialists in hydrology, drought and rangelands, pest management, wildfire, landslide, severe weather and heat, remote sensing, community engagement, actuarial catastrophe modelling, insurance and reinsurance, investment and climate finance, data protection, public law, cybersecurity and emergency operations.

No internal drafting check substitutes for independent professional review, legal advice, regulatory engagement, calibration or field validation.

## Sample PDF production record

- Output: `output/pdf/SCRI_Sample_Expanded_Edition.pdf`
- Pages: 58, US Letter
- Author metadata: Nevil Maloba
- SHA-256: `19BF724CA4E8D6B49E55C888B0FADE54CF7C62C6699F93D88A6E012047B95B2E`
- Rendering QA: 58 of 58 pages rendered with Poppler at 110 dpi; five contact sheets inspected
- Full-size QA: cover/contents; empirical indicator and evidence-geography figures; actuarial tables and curves; product sequence and workspace table; independent-review matrix and diagram
- Corrections during QA: one Mermaid sequence-parser error fixed; duplicate automatic raster captions removed; Part 6 reference flow corrected
- Remaining accessibility issue: the PDF is not tagged and therefore is not yet an accessible publication artefact

## Safety-scenario disposition

| Scenario | Manuscript location | Control | Residual risk | Owner | Status |
|---|---|---|---|---|---|
| Copied false crowd report | Part 2 | Provenance, perceptual/text clustering and independent corroboration | Coordinated manipulation | Data/model owner | Designed; test pending |
| Authentic report with inaccurate location | Part 2 | Accuracy radius, metadata and correction chain | Mislocated exposure match | Data steward | Designed; test pending |
| Satellite/local contradiction | Parts 2–3 | Source-specific likelihood and human review | Unresolved state ambiguity | Hazard-model owner | Designed; test pending |
| Stale gauge | Parts 2–3 | Freshness flag, wider uncertainty and fallback | Blind interval | Source/operations owner | Designed; test pending |
| Data-poor community | Parts 2 and 6 | Coverage monitoring, assisted channel and no-adverse-default rule | Persistent exclusion | Product/community owner | Designed; field validation pending |
| Poor vision performance in smoke, darkness, glare or rain | Parts 2 and 6 | Error slices, model card and degraded mode | Missed or false detection | AI-model owner | Designed; benchmark pending |
| Slow drought with no clean onset | Parts 1 and 3 | Persistent state and duration model | Phase ambiguity | Drought-model owner | Designed; calibration pending |
| Locust movement across borders | Parts 1 and 3 | Corridor state, wind and surveillance uncertainty | Observation and authority gaps | Hazard/institution owner | Designed; coordination pending |
| Landslide blocks access and communications | Parts 1, 3 and 6 | Access-impact scenario and manual fallback | Local blind interval | Operations owner | Designed; exercise pending |
| Compound heat, drought, fire and power failure | Part 3 | Separate states with explicit dependencies | Model-form risk | Hazard-model committee | Conceptual; quantitative work pending |
| Parametric payout without local loss | Part 5 | Basis-risk analysis and contract disclosure | Negative basis risk | Product owner | Designed; product test pending |
| Severe loss without trigger | Part 5 | Basis-risk analysis, predefined fallback and dispute route | Protection gap | Product owner | Designed; product test pending |
| Impermissible mid-event underwriting action | Parts 5–6 | Decision-moment permissions and human authority | Conduct harm | Licensed decision owner | Prohibited in design |
| Model and public warning conflict | Parts 1 and 6 | Authority separation and evidence labelling | Confusion or delayed action | Public/product owner | Designed; protocol pending |
| Cloud or vendor outage | Parts 2 and 6 | Edge queue, baseline, manual fallback and exit plan | Reduced coverage | Technology owner | Designed; exercise pending |
| Contributor access, correction or deletion request | Parts 2 and 6 | Rights workflow and lineage-preserving correction | Operational complexity | Data controller | Designed; DPIA/process test pending |
| Better average discrimination but worse subgroup calibration | Part 6 | Subgroup gate and rollback | Unequal harm | Model-risk owner | Explicit stop condition |
| Challenger fails to beat baseline | Parts 3 and 6 | Champion-challenger gate | Unjustified complexity | Model owner | Baseline retained |
| Avoided loss lacks credible counterfactual | Parts 1, 4 and 5 | Causal evidence requirement | Attribution error | Research/finance owner | Claim prohibited |
| Financing treats expected loss reduction as cash | Part 5 | Repayment-source and transaction bridge | Unbankable structure | Finance owner | Claim prohibited |
