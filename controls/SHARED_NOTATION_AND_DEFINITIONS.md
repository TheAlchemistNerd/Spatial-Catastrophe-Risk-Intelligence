# Shared Notation and Definitions

## 1. Canonical concepts

**Hazard** is the potential occurrence of a physical or ecological event or trend that may cause adverse consequences. A rainfall anomaly, river level, or temperature is a physical variable; it becomes part of risk when it can affect exposed and vulnerable people, assets, services, livelihoods, or ecosystems.

**Exposure** is the presence and value of people, livelihoods, buildings, infrastructure, crops, livestock, ecosystems, services, revenues, or financial interests in places and periods that could be affected.

**Vulnerability** is the propensity of an exposed element to suffer harm, including physical susceptibility, sensitivity, coping capacity, preparedness, maintenance, and ability to recover.

**Risk** is a distribution of uncertain consequences arising from the interaction of hazard, exposure, and vulnerability. It is not synonymous with the hazard variable alone.

**Observation** is a time- and location-linked measurement or report produced by a sensor, person, institution, or model. An observation is evidence about a state; it is not the state itself.

**Detection** is an inference that a defined phenomenon is present. Detection probability is conditional on the phenomenon and the observation system. It must not be confused with occurrence probability.

**Authoritative alert** is a warning issued by a body with the applicable public mandate. A platform-generated probability or community report is not an authoritative alert unless adopted through an approved process.

**Hazard state** is a physical or latent representation of environmental conditions at a location and time. A latent regime is a statistical construct whose interpretation must be validated; its label is not an observed fact.

**Event** is a bounded realization of a hazard under a documented spatial, temporal, and peril definition. Slow-onset drought may require a duration- and threshold-based episode definition rather than a single onset time.

**Footprint** is the spatial distribution of event intensity, such as flood depth, fire intensity, vegetation anomaly, wind speed, heat index, or landslide probability.

**Impact** is a realized consequence on people, assets, livelihoods, ecosystems, or services before or apart from contractual financial treatment.

**Physical or ground-up loss** is the monetary value of modeled damage before insurance terms. It is not necessarily the total welfare or development impact.

**Insured loss** is the modeled or settled amount after policy terms and before or after reinsurance as explicitly stated.

**Uninsured loss** is not simply ground-up loss minus insured loss unless both quantities share scope, valuation basis, population, and timing.

**Fiscal loss** is the effect on public revenue, expenditure, assets, liabilities, and contingent obligations under a defined government scope.

**Avoided loss** is a counterfactual difference between loss under a specified intervention and loss under a credible comparison scenario. A lower revised forecast is not proof of avoided loss.

**Continuous risk estimation** is frequent updating of a risk state or loss distribution. It does not imply continuous repricing, cancellation, payout, capital recognition, or accounting entry.

**Decision product** is a governed output designed for a named user and purpose, with stated limitations, authority, cadence, and challenge process.

## 2. Indices and sets

| Symbol | Meaning |
|---|---|
| $h\in\mathcal H$ | Hazard type: flood, drought, wildfire, locust/crop pest, landslide, storm/heat |
| $g\in\mathcal G$ | Spatial unit: point, grid, catchment, county, corridor, or other defined geometry |
| $t\in\mathcal T$ | Event, observation, decision, or valuation time, explicitly stated |
| $s\in\mathcal S$ | Observation source or source class |
| $i\in\mathcal E$ | Exposure unit, such as person, building, road segment, crop parcel, or policy |
| $e\in\mathcal C$ | Catastrophe event or simulated event identifier |
| $k\in\mathcal K$ | Latent regime index |

## 3. Observation and hazard notation

| Symbol | Meaning |
|---|---|
| $Y_{s,g,t}$ | Observation from source $s$ at location $g$ and time $t$ |
| $q_{s,g,t}$ | Source quality/reliability state, not a hazard probability |
| $Z_{g,t}$ | Latent environmental or hazard regime |
| $X_{g,t}$ | Exogenous or contextual covariates known at the stated cutoff |
| $D_{1:t}$ | Evidence lawfully and operationally known by time $t$ |
| $H_{h,g,t}$ | Physical hazard intensity or state for peril $h$ |
| $N_{h,g,y}$ | Long-term event count under a stated annual period and event definition |
| $I_{e,h}(g)$ | Spatial intensity of event $e$ and hazard $h$ at location $g$ |
| $T^{ign}$ | Ignition or physical onset time where that concept applies |
| $T^{det}$ | Detection time under an explicit clock |
| $T^{response}$ | Effective response or intervention time under an explicit clock |
| $R_{s,g,t}$ | Indicator that a reporting or detection opportunity produced an observation |
| $O_c$ | Latent original evidence item shared by copied reports, frames, tiles, or repeated derivations |
| $A_t$ | Physical or operational intervention capable of changing the state transition |
| $f,d$ | Machine-perception model and deployment device/tier |
| $Se_s,Sp_s$ | Context-specific sensitivity and specificity for source or detector $s$ |

The observation model is source-specific:

$$
Y_{s,g,t}\mid Z_{g,t},q_{s,g,t}
\sim p_s\!\left(Y\mid Z_{g,t},q_{s,g,t}\right).
$$

The generic state transition is:

$$
p\!\left(Z_{g,t}\mid Z_{g,t-1},Z_{\mathcal N_h(g),t-1},X_{g,t},\theta_h\right),
$$

where $\mathcal N_h(g)$ may be a geographic neighbourhood, upstream network, ecological corridor, or another physically defensible dependency graph for hazard $h$.

## 4. Exposure, vulnerability, and loss notation

| Symbol | Meaning |
|---|---|
| $V_i$ | Monetary value or other stated value basis for exposure $i$ |
| $A_i$ | Attributes of exposure $i$, including occupancy, construction, crop stage, or livelihood class |
| $D_{h,c(i)}(I,M_i,\varepsilon_i)$ | Stochastic damage-ratio function for hazard $h$ and exposure class $c(i)$ |
| $d_i,\ell_i,q_i$ | Deductible, applicable limit, and insured or coinsurance share |
| $L^{GU}_e$ | Ground-up physical loss for event $e$ |
| $L^{INS}_e$ | Insured event loss after stated policy terms |
| $L^{NET}_e$ | Insurer loss after stated reinsurance terms |
| $L^{UN}_e$ | Uninsured loss under a reconciled scope |
| $L^{FISC}_e$ | Fiscal loss under a defined public-sector scope |
| $AAL$ | Annual average loss under a defined event set, exposure snapshot, and financial perspective |
| $OEP(x)$ | Annual probability that the largest occurrence loss exceeds $x$ |
| $AEP(x)$ | Annual probability that aggregate annual loss exceeds $x$ |
| $VaR_q(L)$ | Loss quantile at confidence $q$ under a stated distribution |
| $TVaR_q(L)$ | Mean loss conditional on exceeding $VaR_q$, when defined |
| $U_e$ | Ultimate insured loss for catastrophe event $e$ under a stated gross/net basis |
| $C_{e,1:k}$ | Claims-development evidence available through development period $k$ |
| $FCF_t$ | IFRS 17 fulfilment cash-flow measure under the entity's accounting basis |
| $RA_t$ | IFRS 17 risk adjustment for non-financial risk under the entity's method |
| $X_{1y}$ | Adverse one-year change in available capital or net asset value |
| $EC_\alpha$ | Internal economic capital at confidence level $\alpha$ under a stated basis |
| $CFADS_t$ | Cash flow available for debt service under a financing definition |
| $DSCR_t$ | Debt-service coverage ratio, $CFADS_t/DebtService_t$ |
| $PD,LGD,EAD$ | Probability of default, loss given default, and exposure at default in a separately governed credit model |

## 4.1 Finance-ledger definitions

**Risk ledger** records baseline and residual catastrophe distributions, downtime, uninsured loss, fiscal exposure, model version and uncertainty.

**Intervention ledger** records the change mechanism, location, cost, useful life, maintenance, beneficiaries, avoided loss, residual risk and spillovers.

**Finance ledger** records sponsor or borrower, capital sources, repayment, tenor, pricing, covenants, triggers and risk allocation.

**MRV ledger** records the baseline, delivery, physical performance, outcomes, verification and correction history used for monitoring, reporting and verification.

The basic ground-up event-loss calculation is:

$$
L^{GU}_e
=
\sum_{i\in\mathcal E_e}
V_i\,D_{h,c(i)}\!\left(I_{e,h}(g_i),M_i,\varepsilon_{e,i}\right).
$$

This identity is a modelling scaffold. Real implementations must address zero damage, uncertainty, secondary modifiers, repair inflation, demand surge, downtime, network effects, and valuation scope.

## 5. Time and provenance

| Field | Meaning |
|---|---|
| `event_time` | When the observed condition occurred in the physical world |
| `source_recorded_time` | When the source device or reporter recorded it |
| `knowledge_time` | Earliest time the system could lawfully and operationally have known it |
| `ingestion_time` | When the receiving platform accepted it |
| `processing_time` | When a transformation or model processed it |
| `decision_time` | When an authorised decision was made |
| `valuation_time` | Time at which exposure, terms, assumptions, and prices are fixed for a loss estimate |

A training or reconstructed decision input is eligible only if its knowledge time is no later than the decision time. Corrections do not erase the original history; they link to it.

## 6. Quantity separation rules

- Observation confidence is not hazard probability.
- Hazard probability is not loss probability without exposure and vulnerability.
- Expected loss is not a premium, reserve, capital amount, payout, or investment value.
- A model threshold is not an official alert or contractual trigger.
- A contractual trigger is not proof of damage.
- A physical scenario is not a market-consistent valuation.
- A portfolio risk estimate is not an individual customer reason.
- Missing evidence is not adverse evidence unless a valid data-generating mechanism establishes that meaning.
