# Validation and Review Log

## Review status

| Review | Status | Evidence |
|---|---|---|
| Project-source boundary | Completed internally | The two project files are substantive sources; charter/PDF are guidance only |
| Kenya institutional evidence | Completed for manuscript drafting | Official KMD, WRA, NDMA, PP&FSD, KFS, Treasury, Kenya Law, ODPC/MICDE sources |
| Hazard completeness | Completed internally | Automated term audit confirmed all six hazards in every manuscript; `HAZARD_COVERAGE_MATRIX.md` reconciled |
| Mathematical notation | Completed internally | Shared indices, time semantics, observation/state/event/loss equations and quantity boundaries checked against `SHARED_NOTATION_AND_DEFINITIONS.md` |
| Actuarial separation | Completed internally | Event/annual, ground-up/insured/uninsured/fiscal, reserve/capital/credit/payout and estimate/avoided-loss distinctions checked across Parts 4–5 |
| Citations and links | Completed internally | Every manuscript has an independent numerical reference section; cited reference identifiers reconcile; local series/control links resolve |
| Required structure | Completed internally | All six manuscripts contain abstract, research question, narrative/technical core, limitations, conclusion and references |
| Required conceptual visuals | Completed internally | Numbered Markdown/ASCII figures and tables reconcile to `FIGURE_AND_TABLE_REGISTER.md`; all are labelled conceptual where not empirical |
| Mermaid source and rendering | Completed with Pandoc filter | 20 executable Mermaid snippets across all six manuscripts rendered successfully through `mermaid-filter.lua` |
| Compiled PDF | Completed with Pandoc/XeLaTeX | 166-page A4 volume produced; cover, contents, part openings, representative diagrams/tables, running matter and closing references visually inspected after rendering to PNG |
| Source-boundary leakage | Completed internally | Only explicit boundary statements mention California or the benchmark project's excluded concepts; no foreign example is presented as Kenyan evidence |
| Word counts | Completed with Pandoc | Parts: 7,042; 8,253; 8,705; 8,754; 8,307; 7,826. Total: 48,887; every part within ±5% and total within 48,000–52,000 |
| Independent expert review | Not performed in this workspace | Required before operational or publication claims |

## Required independent review

The manuscripts require review by Kenyan or regionally experienced specialists in hydrology, drought/rangelands, pest management, wildfire, landslide, severe weather/heat, remote sensing, community engagement, actuarial catastrophe modelling, insurance/reinsurance, investment/climate finance, data protection, public law, cybersecurity, and emergency operations.

No internal drafting check substitutes for independent professional review, legal advice, regulatory engagement, calibration, or field validation.

## Safety-scenario disposition template

| Scenario | Manuscript location | Control | Residual risk | Owner | Status |
|---|---|---|---|---|---|
| Correlated false crowd report | Part 2 | Provenance, clustering, corroboration | Coordinated manipulation | Data/model owner | Drafted |
| Stale authoritative sensor | Parts 2–3 | Freshness, health state, fallback | Blind interval | Source/operations owner | Drafted |
| Data-poor community | Parts 2, 6 | Missingness model, offline channel, no-adverse-default | Persistent exclusion | Product/public owner | Drafted |
| Parametric basis risk | Part 5 | Independent data, back-test, disclosure, dispute route | Unmatched loss/payout | Insurer/product owner | Drafted |
| Impermissible mid-event action | Parts 4–6 | Contract/policy gate and human authority | Conduct harm | Licensed decision owner | Drafted |
| Unsupported avoided-loss claim | Parts 1, 4–6 | Counterfactual and causal evaluation | Attribution error | Research/finance owner | Drafted |
