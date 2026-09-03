# Part 4: Actuarial Catastrophe Loss Intelligence

## The loss engine follows the policy from damage to recovery

When floodwater reaches a warehouse, depth and duration influence damage; construction and contents influence vulnerability; and replacement values establish the ground-up financial scale. Deductibles, limits, sublimits, exclusions, waiting periods, coinsurance and coverage interpretation then turn covered damage into an insured claim. Reinsurance terms determine how much of the portfolio loss remains with the insurer.

This sequence is the actuarial centre of Spatial Catastrophe Risk Intelligence (SCRI). Catastrophe modelling practice separates event, hazard, exposure, vulnerability and financial modules for a reason [1]. The state engine from Part 3 estimates the peril. The actuarial engine answers a different question: *given what is currently known about this event and this exact exposure snapshot, what distribution of ground-up, gross insured and net retained loss follows?*

For asset or coverage unit $i$ affected by event $e$ and hazard $h$:

$$
L^{GU}_{e,i}=V_i\,D_{h,c(i)}\!\left(I_{e,h}(g_i),M_i,\varepsilon_{e,i}\right).
\tag{4.1}
$$

where $V_i$ is the relevant value measure, $I_{e,h}(g_i)$ is the uncertain intensity at location $g_i$, $c(i)$ is the exposure class, $M_i$ contains secondary vulnerability modifiers and $\varepsilon_{e,i}$ represents residual damage uncertainty. The damage function $D$ is a bounded distribution where the physical quantity requires it, carrying both a mean damage ratio and variability. For a crop it may depend on inundation duration and crop stage; for a building, depth and construction; for livestock drought, the insured index or mortality mechanism; for business interruption, physical damage, access and restoration time.

A simplified occurrence-level insurance transform is:

$$
L^{INS}_{e,i}
=
q_i\,
\min\!\left[
\max\!\left(L^{COV}_{e,i}-d_i,0\right),
\ell_i
\right].
\tag{4.2}
$$

where $L^{COV}_{e,i}$ is the covered portion of ground-up loss after exclusions and sublimits, $d_i$ is the deductible, $\ell_i$ is the applicable limit and $q_i$ is the insured or coinsurance share. Real implementations also preserve policy aggregation, hours clauses, waiting periods, reinstatements and the order in which terms apply. The Oasis financial module illustrates why policy and reinsurance terms must be applied explicitly to ground-up samples to obtain gross and net perspectives [2]. Appendix F derives the moments of Equation (4.1), proves the piecewise policy transform in Equation (4.2), and shows how dependence enters portfolio aggregation.

```mermaid
flowchart TD
  H[Hazard intensity distribution] --> D[Damage distribution]
  E[Exposure value and characteristics] --> D
  D --> GU[Ground-up loss]
  P[Coverage, exclusions, deductible and limit] --> INS[Gross insured loss]
  GU --> INS
  INS --> RI[Reinsurance programme]
  RI --> NET[Net retained loss]
  INS --> CLM[Claims emergence and settlement]
  CLM --> RES[Case reserve and IBNR views]
```
**Figure 4.1: Physical damage, insured loss and accounting views are distinct**

The insured event total is $L^{INS}_e=\sum_i L^{INS}_{e,i}$, but the sum must retain dependence. Two adjacent buildings can share flood depth, construction practice, utility failure and access interruption. Crop policies may share the same weather and planting calendar. Motor, property and business interruption can accumulate around one blocked transport corridor. Independent asset simulations would understate the tail.

## A worked flood portfolio: from footprint to retained loss

The following **synthetic, reproducible Nzoia flood portfolio** makes every financial transformation inspectable before real exposure, claims and vulnerability evidence are introduced. Its counts, values, damage ratios, policy terms, event frequency and curve points are demonstration assumptions rather than Kenya market estimates.

The illustrative insurer has four groups exposed to the same flood footprint. The central scenario translates the posterior footprint into affected counts and one mean damage ratio for each group. Values and all losses are in KES millions.

| Segment | Policies | Value per unit | Total insured value | Central affected count | Mean damage ratio | Deductible | Limit | Insured share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dwellings | 120 | 4.00 | 480.00 | 72 | 18% | 0.10 | 2.50 | 100% |
| Small businesses | 80 | 8.00 | 640.00 | 36 | 22% | 0.25 | 5.00 | 100% |
| Crop plots | 300 | 0.30 | 90.00 | 210 | 35% | 0.03 | 0.27 | 80% |
| Vehicles | 50 | 2.00 | 100.00 | 15 | 28% | 0.10 | 1.50 | 100% |
| **Portfolio** | **550** | — | **1,310.00** | **333** | — | — | — | — |

For dwellings, the central ground-up loss is $72\times4.00\times0.18=51.84$. The insured amount per affected dwelling is $\min[\max(4.00\times0.18-0.10,0),2.50]=0.62$, giving KES 44.64 million. The same order of operation is repeated for each segment; applying a portfolio-average deductible after aggregation would be wrong.

| Segment | Ground-up loss | Gross insured loss | Difference created by terms |
|---|---:|---:|---:|
| Dwellings | 51.84 | 44.64 | 7.20 |
| Small businesses | 63.36 | 54.36 | 9.00 |
| Crop plots | 22.05 | 12.60 | 9.45 |
| Vehicles | 8.40 | 6.90 | 1.50 |
| **Central scenario** | **145.65** | **118.50** | **27.15** |

Suppose, for this demonstration, that a catastrophe excess-of-loss layer pays losses above KES 75 million up to KES 100 million. At the central gross loss of KES 118.50 million, the illustrative recovery is $\min[\max(118.50-75,0),100]=43.50$ million and the insurer’s event retention is KES 75.00 million. A production extension would add reinstatement premium, aggregate terms, exclusions, collectability, loss-adjustment expense and the timing of cash recovery.

The simulation expands the central scenario into a loss distribution. It treats affected share and mean damage ratio as uncertain beta variables, applies policy terms at unit level and preserves one common event draw within each segment. Across 60,000 event simulations, gross insured loss has a P10 of KES 83.51 million, a median of KES 115.86 million, a P90 of KES 155.58 million and a P95 of KES 168.83 million. The deterministic central case differs from the median because deductibles, limits and stochastic affected counts make the transform nonlinear.

```mermaid
flowchart TD
  POST[Posterior flood footprint] --> AF[Segment affected shares]
  AF --> MDR[Stochastic damage ratios]
  MDR --> UNIT[Unit-level ground-up loss]
  UNIT --> TERMS[Deductibles, limits and shares]
  TERMS --> GROSS[Gross event-loss samples]
  GROSS --> XOL[Illustrative occurrence layer]
  XOL --> NET[Net retained-loss samples]
  GROSS --> AUDIT[Change attribution and audit]
```
**Figure 4.2: Calculation path for the synthetic worked example**

To demonstrate the annual clock, a second simulation samples 100,000 synthetic years with a Poisson mean of 0.65 events per year and the event-loss distribution above. It produces an illustrative annual average gross insured loss of KES 76.36 million. The model’s three-year AEP and OEP points are KES 110.36 million and KES 107.06 million respectively; at 100 years they are KES 386.83 million and KES 188.17 million. The widening gap is expected: AEP includes every event in a year, whereas OEP uses only the largest event.

![](assets/figures/synthetic_flood_ep_curves.png){ width=94% }

**Figure 4.3: Synthetic aggregate and occurrence exceedance curves.** The fixed seed, assumptions and generated values are stored with the manuscript. These curves demonstrate the interface; production pricing, reserving, reinsurance and capital use begins after empirical calibration and independent review.

The next evidence layer upgrades the demonstration into an empirically calibrated model. Policy records establish location, coverage, values and terms. Claims and engineering evidence calibrate vulnerability by depth, duration and asset type. Historical event catalogues and climate assumptions support frequency. Reinsurance contracts are encoded and independently reconciled. Until those steps are complete, the product label remains **demonstration**.

## Current-event loss and long-term catastrophe risk

SCRI operates on two clocks. The **event clock** updates the unfolding catastrophe. New gauges, imagery and reports change the posterior intensity and footprint, which change the event-loss distribution. The **portfolio clock** governs annual expected loss, tariff support, risk appetite, reinsurance purchase and capital. It changes only through a controlled model version using an event catalogue, exposure assumptions, vulnerability calibration and financial terms appropriate to that horizon.

For the long-term catalogue, event count in hazard $h$, region $g$ and year $y$ may use a Poisson, Negative Binomial, point-process, renewal or state-duration model. A Negative Binomial is a candidate when conditional counts remain overdispersed after relevant covariates:

$$
N_{h,g,y}\sim\operatorname{NegBin}(\mu_{h,g,y},\phi_h).
\tag{4.3}
$$

$$
\log\mu_{h,g,y}
=
\log E_{h,g,y}+\eta_{h,g,y}.
\tag{4.4}
$$

where $E_{h,g,y}$ is an exposure-to-occurrence measure such as years, area-time or another definition established for that hazard. When $\mu$ contains the exposure offset, it already represents the expected count for that observation cell and enters the pure-premium calculation once. Appendix F derives the mean-variance relationship for Equation (4.3) and the rate interpretation of the exposure offset in Equation (4.4).

Frequency modelling follows each hazard. A drought episode may be represented by a persistent regime and duration. A wildfire catalogue may distinguish ignitions from escaped fires. Locust outbreaks may be conditioned on regional biological and climate regimes. A Poisson or empirical-frequency baseline makes the challenger’s improvement measurable. Real-time reports update the current event record, while the annual catalogue changes through a separate controlled event-definition process.

Annual aggregate loss is generated from the catalogue:

$$
S_y=\sum_{e=1}^{N_y}L^{NET}_{e,y}.
\tag{4.5}
$$

with event clustering, cross-peril relationships and policy/reinsurance terms applied in the correct order. Simulated year-loss tables or equivalent analytical outputs support:

- annual average loss, $\mathbb E[S_y]$;
- occurrence exceedance probability, based on the largest event loss in a year;
- aggregate exceedance probability, based on total annual loss;
- selected quantiles such as VaR at a stated probability;
- TVaR or expected shortfall beyond a stated quantile;
- scenario losses and uncertainty ranges.

“Probable maximum loss” is reported with its definition. It may refer to a quantile of occurrence loss, aggregate annual loss or a deterministic scenario; the probability, horizon, gross/net basis, currency, exposure date and model version accompany it.

```mermaid
flowchart TD
  CAT[Long-term event catalogue] --> Y[Simulated policy year]
  CUR[Current-event posterior] --> NOW[Event-loss nowcast]
  Y --> EVENTS[Occurrence, intensity and footprint samples]
  EVENTS --> LOSS[Financial loss engine]
  NOW --> LOSS
  LOSS --> ELT[Event-loss table]
  LOSS --> YLT[Year-loss table]
  ELT --> OEP[Occurrence EP curve]
  YLT --> AEP[Aggregate EP curve]
  NOW --> OPS[Claims and liquidity operations]
```
**Figure 4.4: Event nowcasting and annual risk use related but different clocks**

## Severity, tails and dependence are empirical choices

SCRI evaluates candidate bulk distributions such as Gamma, Lognormal, Weibull or mixtures; asset-level loss may instead emerge from stochastic vulnerability functions. Selection uses exposure- and inflation-normalised data, censored and truncated likelihoods where required, diagnostic plots, proper scoring rules and out-of-sample validation.

If a peaks-over-threshold model is used, exceedances above threshold $u$ may follow a Generalized Pareto distribution:

$$
L-u\mid L>u
\sim
\operatorname{GPD}(\xi,\beta_u).
\tag{4.6}
$$

Threshold choice is a model decision with a bias-variance trade-off. The analysis states the exceedance count, threshold diagnostics, parameter stability, continuity or splicing method, treatment of limits and inflation, and uncertainty. Research on insurance-loss modelling likewise treats threshold selection and bootstrap uncertainty as substantive parts of the method [3], while standard quantitative-risk texts place tail estimates inside a wider framework of model and parameter uncertainty [4]. Where the Kenyan tail sample is sparse, documented external data, engineering scenarios and expert judgement support wider and more transparent uncertainty ranges. Appendix F derives compound annual-loss moments, OEP and AEP relationships and the tail-quantile expression implied by Equations (4.5)-(4.6).

Dependence receives the same discipline. A Gaussian copula is symmetric and has no asymptotic tail dependence; a conventional Student-$t$ copula has symmetric tail dependence. Where upper- and lower-tail behaviour differs, candidates may include appropriate Archimedean families, vines, factor models, max-stable or spatial-process approaches [5]. Model selection considers dimensionality, data volume, physical mechanism and tail diagnostics. For many catastrophe portfolios, shared event and intensity fields already induce dependence, so any residual copula is calibrated to the dependence remaining after the hazard simulation.

```mermaid
flowchart TD
  SH[Shared event and intensity field] --> P1[Property marginal loss]
  SH --> P2[Agriculture marginal loss]
  SH --> P3[Business-interruption marginal loss]
  P1 --> DEP[Residual dependence model if required]
  P2 --> DEP
  P3 --> DEP
  DEP --> JOINT[Joint portfolio-loss distribution]
  JOINT --> DIAG[Tail and scenario diagnostics]
```
**Figure 4.5: Dependence begins with the common physical event**

## Claims nowcasting, reserves and the value of intervention

An event-loss nowcast supports operations before all claims are reported. It estimates a range of ultimate insured loss from the current footprint, exposure, vulnerability and financial terms. A claims emergence model then connects that ultimate view to reported counts and paid amounts:

$$
N^{rep}_{e,k}\mid N^{ult}_e
\sim
\operatorname{Binomial}\!\left(N^{ult}_e,F_N(k\mid x_e)\right).
\tag{4.7}
$$

where $k$ is elapsed development time and $F_N$ is a reporting curve conditional on event and operational characteristics. Severity development, reopening, salvage, loss-adjustment expense and claims inflation require separate treatment. The nowcast enters the reserving process as evidence, while the insurer’s actuarial and finance functions own case reserves, IBNR and accounting entries under the applicable basis.

Detection latency enters the model only where an intervention pathway exists. Let $A_e$ record whether a response was available and implemented, and $\tau_e$ the effective response delay. Conditional severity may include:

$$
\mathbb E[L^{GU}_e\mid I_e,X_e,A_e,\tau_e]
=
m_h(I_e,X_e)+\delta_h(A_e,\tau_e).
\tag{4.8}
$$

Here $\delta_h$ is a causal effect estimated from evidence. Confounding is substantial: severe events may be detected earlier because they are visible, while easier-to-reach events may receive faster intervention and also cause less loss. Credible estimation may require matched events, quasi-experimental designs, randomised operational trials where ethical, or structured scenario analysis. The output is an avoided-loss range conditional on assumptions. Appendix F derives the reporting-count moments in Equation (4.7), an ultimate-count estimator, and the causal contrast associated with Equation (4.8).

The canonical loss record makes every financial quantity auditable:

```text
event_id and hazard_type
valuation_time and observation cut-off
scenario or posterior-state version
exposure snapshot and currency basis
ground-up loss distribution
gross insured loss distribution
net retained loss distribution
reported and ultimate claims views
mean, quantiles and exceedance probabilities
occurrence or aggregate horizon
policy and reinsurance terms versions
uncertainty decomposition
model version and data-quality status
accountable user and permitted use
```

| Output | Meaning | Typical owner | Not interchangeable with |
|---|---|---|---|
| Event-loss nowcast | Current estimate of ultimate loss from one unfolding event | Catastrophe analytics / claims | Booked reserve |
| Gross insured loss | Covered loss after direct policy terms | Actuarial / underwriting | Ground-up economic loss |
| Net retained loss | Gross loss after reinsurance recoveries | Reinsurance / capital | Available cash |
| AAL | Mean annual loss over the model horizon | Pricing / portfolio / capital | Current-event loss |
| OEP / AEP | Annual occurrence or aggregate exceedance relationship | Reinsurance / capital | Deterministic forecast |
| Case reserve / IBNR | Accounting estimate under the insurer’s reserving basis | Reserving actuary / finance | Parametric payout trigger |

The architecture shortens the distance between physical evidence and a financially defined, revisable distribution. It shows why that distribution changed, which policies drove it, which uncertainty remains and which institution owns the next decision. Speed and traceability together make the estimate operationally useful.

\newpage

## References

[1] Institute and Faculty of Actuaries, “Catastrophe Modelling Working Party Report,” 2006. [Online]. Available: https://actuaries.org.uk/media/z0hahpz3/catreport2006.pdf. Accessed: Aug. 28, 2026.

[2] Oasis Loss Modelling Framework, “Oasis Financial Module,” 2016. [Online]. Available: https://oasislmf.org/application/files/9117/1624/0856/Financial_Module.pdf. Accessed: Aug. 28, 2026.

[3] Y. Hou, S. K. Kang, C. C. Lo and L. Peng, “Three-step risk inference in insurance ratemaking,” *Insurance: Mathematics and Economics*, vol. 105, pp. 1–13, 2022, doi: 10.1016/j.insmatheco.2022.03.005. [Online]. Available: https://doi.org/10.1016/j.insmatheco.2022.03.005. Accessed: Aug. 29, 2026.

[4] A. J. McNeil, R. Frey and P. Embrechts, *Quantitative Risk Management: Concepts, Techniques and Tools*, revised ed. Princeton, NJ, USA: Princeton University Press, 2015. [Online]. Available: https://press.princeton.edu/books/hardcover/9780691166278/quantitative-risk-management. Accessed: Aug. 29, 2026.

[5] H. Joe, *Dependence Modeling with Copulas*. Boca Raton, FL, USA: CRC Press, 2014, doi: 10.1201/b17116. [Online]. Available: https://doi.org/10.1201/b17116. Accessed: Aug. 29, 2026.
