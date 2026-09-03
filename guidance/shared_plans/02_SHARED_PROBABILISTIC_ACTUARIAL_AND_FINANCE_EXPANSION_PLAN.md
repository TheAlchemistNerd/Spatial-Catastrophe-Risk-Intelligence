# Shared Probabilistic, Actuarial and Finance Expansion Plan

> **Status:** Shared project plan. The evaluation, mathematical proposals and preservation-first sequence below are preserved almost verbatim from the source assessment, with Markdown structure and tables normalised for project use.

## 3. Probabilistic-inference evaluation

The current [Part 3 (line 1)](/C:/Users/Nevo/Downloads/Spatial Catastrophe Risk Intelligence/manuscripts/03_SPATIOTEMPORAL_HAZARD_STATE_MODELLING.md:1) and [Appendix E (line 281)](/C:/Users/Nevo/Downloads/Spatial Catastrophe Risk Intelligence/manuscripts/07_APPENDICES.md:281) establish a useful foundation:

- Bayesian prediction and update.
- Hazard-specific spatial neighbourhoods.
- Directed flood dependence.
- Explicit drought duration.
- Occurrence versus detection.
- Detection and response latency.
- Posterior uncertainty propagation.
- Transparent baselines and challenger models.

The current treatment is mathematically correct at an introductory level, but it lists candidate filters without specifying how SCRI would construct an operational posterior.

### Refinements required

#### 1. Use the full predictive prior

The main evidence-fusion equation should use:

\[
p(Z_t\mid Y_{1:t-1},X_t)
\]

rather than conditioning directly on an unknown \(Z_{t-1}\). Appendix E already performs the required marginalisation; Part 2 should match it.

#### 2. Define source-specific likelihoods

Each source needs an actual likelihood family:

- Gauge: measurement error, rating-curve uncertainty and stale-data model.
- Segmentation: probabilistic mask or boundary-error model.
- Detector: class sensitivity, false-positive rate and calibration curve.
- Crowd report: reporting probability, truthfulness, geolocation error and duplication origin.
- Satellite: acquisition coverage, sensor error and processing uncertainty.
- Institutional record: reporting delay and revision process.

A confidence score becomes statistically useful only after it has been connected to such a likelihood.

#### 3. Model the observation process

Sparse crowd reporting can arise because:

- No hazard occurred.
- Connectivity failed.
- A community lacks reporting access.
- People prioritised safety over reporting.
- A trusted reporter was unavailable.
- The event affected communications.

SCRI therefore needs a reporting or detection process:

\[
P(R_{s,g,t}=1\mid Z_{g,t},A_{g,t},C_{g,t},q_s),
\]

where access and connectivity help distinguish “no report” from “evidence of no event.”

#### 4. Replace simple reliability scores with contextual reliability

The Beta-Binomial model in Appendix D is a transparent baseline. Production reliability should be hierarchical and conditional on:

- Hazard.
- Geography.
- Device or sensor type.
- Lighting and weather.
- Reported variable.
- Verification method.
- Time since observation.
- Contributor experience.

This permits partial pooling without assigning one universal credibility score to a person or community.

#### 5. Model common evidence origins

The effective-sample-size derivation for copied reports is a valuable diagnostic. The operational model should add a latent origin:

```text
Original event observation
        ↓
Copying, forwarding and platform propagation
        ↓
Many visible reports
```

One origin can then generate several correlated manifestations. The model can also treat frames from one video, tiles from one satellite acquisition and detections from the same model run as correlated evidence.

#### 6. Handle asynchronous and corrected evidence

Catastrophe evidence arrives out of order. The state engine needs:

- Online filtering for operational use.
- Fixed-lag smoothing for delayed reports.
- Full retrospective smoothing for event reconstruction.
- Versioned correction and replay.
- Explicit treatment of out-of-sequence measurements.

#### 7. Add change-of-support modelling

SCRI fuses points, lines, pixels, polygons, basin values and livelihood-zone indicators. The model must relate each observation to its spatial support rather than assigning all observations directly to one grid cell.

#### 8. Add intervention-aware transitions

Where suppression, drainage operation, pest control or water allocation changes the physical process:

\[
p(Z_t\mid Z_{t-1},X_t,A_t)
\]

should include the intervention \(A_t\). This creates the mathematical bridge between value of information and value of action.

#### 9. Strengthen nonstationarity

Part 3 should model:

- Seasonal transitions.
- Climate covariates.
- Urbanisation and land-use change.
- Changing exposure and reporting coverage.
- Time-varying vulnerability and response capacity.
- Parameter drift and structural breaks.

#### 10. Propagate posterior samples

The actuarial engine should receive posterior samples or weighted scenarios:

\[
Z_t^{(m)}\sim p(Z_t\mid Y_{1:t}),
\]

then calculate loss for each sample. Means and covariance approximations remain useful reconciliations, but full samples preserve nonlinearities, thresholds and policy terms.

### Recommended appendix additions

Appendix D/E should add derivations for:

- Contextual source reliability.
- Missing-not-at-random reporting.
- Latent evidence-origin dependence.
- Out-of-sequence updates.
- Change-of-support integration.
- Controlled state transitions.
- Posterior predictive checks.
- Bayesian model averaging or stacking.
- Full posterior-to-loss Monte Carlo propagation.
- Nonstationary and hierarchical county effects.

## 4. Actuarial-modelling evaluation

The current [Part 4 (line 1)](/C:/Users/Nevo/Downloads/Spatial Catastrophe Risk Intelligence/manuscripts/04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md:1) is presently the strongest technical part.

### Existing strengths

It already contains:

- Hazard–exposure–vulnerability–financial separation.
- Unit-level deductible and limit application.
- Ground-up, gross and net loss.
- A synthetic Nzoia flood portfolio.
- Occurrence reinsurance.
- Event and annual modelling clocks.
- Negative Binomial frequency.
- Compound annual loss.
- OEP and AEP.
- Heavy-tail treatment.
- Spatial and cross-line dependence.
- Claims-emergence modelling.
- Avoided-loss causality.
- Mathematical derivations in Appendix F.

### Loss-modelling expansion

Add explicit treatment of:

- Exposure-value and geocoding uncertainty.
- Occupancy, construction and condition misclassification.
- Vulnerability-curve parameter uncertainty.
- Zero-damage probability and total-loss mass.
- Censored and truncated claims.
- Demand surge and post-event inflation.
- Business interruption and restoration time.
- Contingent business interruption and infrastructure networks.
- Claims leakage, fraud, salvage and subrogation.
- Loss-adjustment expense.
- Reinsurance collectability.
- Event clustering and hours-clause definitions.
- Multi-peril annual catalogues and compound events.
- Uninsured, livelihood, infrastructure and fiscal loss.

The synthetic example should label percentiles and return periods unambiguously. “P10” should mean the tenth loss percentile, while “1-in-10-year” should mean a 10% annual exceedance probability.

### Reserving requires a dedicated model

The present reserving treatment is one reporting-count model at [Part 4, line 183 (line 183)](/C:/Users/Nevo/Downloads/Spatial Catastrophe Risk Intelligence/manuscripts/04_ACTUARIAL_CATASTROPHE_LOSS_INTELLIGENCE.md:183). It is useful for claims nowcasting but does not yet constitute a complete reserve model.

SCRI should combine the catastrophe nowcast as a prior with emerging claims evidence:

\[
p(U_e\mid C_{e,1:k},H_{e,t})
\propto
p(C_{e,1:k}\mid U_e,\theta)\,
p(U_e\mid H_{e,t},E,V,F),
\]

where \(U_e\) is ultimate event loss, \(C_{e,1:k}\) is observed claims development, and the prior comes from hazard, exposure, vulnerability and financial terms.

Required reserving layers include:

- Reported-but-not-settled claims.
- IBNR.
- IBNER.
- Reopened claims.
- Count development.
- Paid and incurred severity development.
- Claims inflation.
- Settlement and closure time.
- Salvage and subrogation.
- Direct and indirect loss-adjustment expense.
- Reinsurance recoveries.
- Reserve uncertainty by event and portfolio.

Transparent baselines should include:

- Chain ladder.
- Bornhuetter–Ferguson.
- Cape Cod.
- Mack distribution-free uncertainty.
- Bootstrap/GLM reserving.
- Claim-level reporting and settlement survival models.

The catastrophe-informed Bayesian reserve becomes the challenger. Validation should use point-in-time historical events, ultimate-loss back-testing, interval coverage and one-year reserve deterioration.

IFRS 17 should then be introduced as a separate accounting translation. Its fulfilment cash flows incorporate probability-weighted expected cash flows, timing and a risk adjustment for non-financial risk. This is distinct from the catastrophe nowcast and from economic capital. IFRS 17 overview, IFRS 17 key terms.

### Economic-capital modelling is the largest actuarial gap

Economic capital should become a major Part 4 section, with derivations in Appendix F.

Define a one-year loss in available capital or net asset value:

\[
X_{1y}=-\Delta NAV_{1y}.
\]

A simple internal economic-capital measure is:

\[
EC_\alpha
=
VaR_\alpha(X_{1y})-\mathbb E[X_{1y}],
\]

with TVaR/expected shortfall presented as an alternative tail measure.

The model should combine:

- Catastrophe underwriting risk.
- Attritional premium risk.
- Reserve deterioration risk.
- Reinsurance credit and collectability risk.
- Market and asset risk.
- Operational and model risk.
- Liquidity risk.
- Concentration by county, basin, peril and counterpart.
- Compound and cross-peril climate scenarios.

It should distinguish four quantities:

| Quantity | Purpose |
|---|---|
| Kenya regulatory risk-based capital | Regulatory solvency requirement |
| Internal economic capital | Management view of capital needed for the risk profile |
| IFRS 17 risk adjustment | Compensation for non-financial uncertainty in insurance-contract cash flows |
| Reinsurance/transaction risk margin | Commercial pricing or transaction component |

Kenya’s regulatory framework calculates risk-based capital across insurance, market, credit and operational risk, and general insurers hold capital against fluctuations in premium and claims reserves. Kenyan technical-provision and RBC regulations.

The paper should also add:

- Capital allocation by peril, county and line using an Euler or marginal contribution approach.
- Risk-adjusted return on capital.
- Reinsurance optimisation subject to capital and liquidity constraints.
- Reverse stress testing.
- Multi-year climate and business-plan scenarios.
- Parameter and model-form uncertainty.
- Capital relief attributable to validated resilience interventions.

## 5. Institutional, resilience and sustainable finance

The current [Part 5 (line 1)](/C:/Users/Nevo/Downloads/Spatial Catastrophe Risk Intelligence/manuscripts/05_INSURANCE_INVESTMENT_AND_RESILIENCE_FINANCE.md:1) has a strong insurer-facing narrative. Its four-desk Nzoia journey is one of the manuscript’s best product passages.

The resilience-finance section establishes NPV, benefit-cost ratio, risk layers and a cash-flow bridge. It now needs to become an operational SCRI finance engine.

### Four linked finance ledgers

SCRI should maintain:

1. **Risk ledger:** AAL, OEP/AEP, expected downtime, uninsured loss, fiscal gap and tail risk.
2. **Intervention ledger:** intervention cost, mechanism, useful life, maintenance, beneficiaries, avoided-loss distribution and residual risk.
3. **Finance ledger:** sponsor, borrower, repayment source, tenor, covenants, triggers, cash flows and risk allocation.
4. **MRV ledger:** baseline, implementation evidence, physical performance, outcome evidence, verification and correction history.

### Investment modelling

For banks, investors and project financiers, add:

- Hazard-adjusted operating cash-flow distributions.
- Downtime and revenue interruption.
- Debt-service coverage ratio under catastrophe scenarios.
- Conditional PD, LGD and EAD where separately validated.
- Collateral-value and recovery-time effects.
- Resilience-capex alternatives.
- Project NPV and internal rate of return.
- Real-option value of staged adaptation.
- Portfolio concentration and correlated infrastructure failure.
- Physical-risk stress tests at asset and portfolio level.

### Finance-product narratives

Part 5 needs a worked narrative for each major financial mechanism:

| Structure | SCRI contribution |
|---|---|
| Resilience loan | Baseline risk, capex effect, covenant monitoring and residual risk |
| Green/adaptation bond | Project screening, use-of-proceeds evidence and impact reporting |
| Sustainability-linked finance | KPI baseline, calibration, monitoring and verification |
| Parametric insurance | Trigger design, basis-risk testing and data-continuity evidence |
| Contingent credit | Funding-layer exhaustion and drawdown evidence |
| Resilience bond | Risk reduction, insurance economics and repayment mechanism |
| Blended/results-based finance | Additionality, beneficiary outcomes and performance evidence |
| County or sovereign financing | Fiscal gap, risk layering, vulnerable populations and liquidity timing |

Kenya’s Green Finance Taxonomy and Climate Risk Disclosure Framework should be incorporated into the bank-facing product. CBK legislation and guidelines. CMA’s green-bond guidance belongs in the capital-markets pathway. CMA policy guidance. IRA’s Principles of Sustainable Insurance should inform the insurer pathway. IRA sustainable-insurance circular.

Most importantly, the 2026–2030 Kenyan Disaster Risk Financing Strategy now provides a current national architecture. It explicitly promotes risk reduction, retention and transfer, prearranged finance, county mechanisms and financial resilience. SCRI can position itself as the analytical and MRV infrastructure supporting that architecture. National Treasury DRF Strategy 2026–2030.

## 6. Preservation-first implementation sequence

When implementation begins, I recommend this order:

1. **Freeze the current edition.** Create a timestamped snapshot under `documentation/` before changing manuscripts.
2. **Expand Part 2 additively.** Preserve its present narrative and add approximately 6,500–7,000 words covering the model portfolio, data programme, uncertainty, deployment and product interfaces.
3. **Strengthen Part 3.** Add operational likelihoods, observation-process modelling, asynchronous updates, spatial support, nonstationarity and posterior-sample propagation.
4. **Expand Part 4.** Preserve the worked flood example and add loss uncertainty, catastrophe-informed reserving and a full economic-capital section.
5. **Expand Part 5.** Preserve the four-desk flood story and cash-flow bridge, then add sustainable-finance classification, investment analytics, finance-product narratives and MRV.
6. **Extend the appendices.** Add numbered derivations for perception uncertainty, hierarchical inference, reserve posteriors, IFRS 17 translation, economic capital, capital allocation and reinsurance optimisation.
7. **Update controls.** Add every new technical, regulatory and financial source—with its URL—to the source register and claim ledger.
8. **Rebuild diagrams.** Use coloured backgrounds, fewer nodes per figure and half-page or full-page placement where required for reading at 100% zoom.
9. **Rebuild the PDF only after cross-part reconciliation.** Verify equation numbering, references, source URLs, figure legibility, word count and preservation of the existing positive product tone.

The central recommendation is to keep the manuscript’s present narrative spine and deepen the transformations between layers:

> Pixels become calibrated observations; observations become posterior catastrophe states; catastrophe states become loss, reserve and capital distributions; those distributions become institution-specific insurance, investment and resilience-finance products.

That is the expansion that will make SCRI read as a coherent Insurtech and catastrophe-finance product rather than a policy framework or collection of AI techniques.
