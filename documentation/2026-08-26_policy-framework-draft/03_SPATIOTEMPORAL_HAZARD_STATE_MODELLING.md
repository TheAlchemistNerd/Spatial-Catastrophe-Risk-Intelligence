# Spatiotemporal Hazard-State and Event Modelling for Kenya

## Abstract

Heterogeneous observations do not directly describe a catastrophe. They provide incomplete, delayed and sometimes contradictory evidence about a physical or latent environmental state. This paper defines a Kenya-first modelling engine that separates environmental regime, event occurrence, detection, intensity, footprint, propagation, duration and recovery. The separation is essential: a smoke detection is not an ignition probability; river level is not building damage; a drought stage is not a count of events; and a mobile locust swarm does not respect administrative grids.

The proposed engine combines transparent hazard-specific baselines with hierarchical probabilistic challengers. Spatial structure follows the process: directed river networks for flood, neighbourhood and wind/fuel relationships for fire, movement fields for locust, hillslope units for landslide, and urban or atmospheric neighbourhoods for storm and heat. Slow drought states require persistence and duration. Finite hidden Markov models, hidden semi-Markov models, switching state-space models, hierarchical Bayesian models and nonparametric iHMM/HDP-HMM formulations are compared rather than treated as a ladder of sophistication. Latent-regime models organise dependence; they do not replace process science, event-frequency models or severity distributions.

Validation uses event, spatial, temporal and source holdouts; probabilistic calibration; footprint, intensity, duration and lead-time metrics; extremes and failure scenarios; and champion-challenger gates. The paper concludes that one mathematical spine can link the hazards only if emission, transition, event and propagation components remain hazard-specific and uncertainty is decomposed for decision users.

**Research question.** How can Kenya infer evolving, spatially connected hazard states and event distributions from source-aware observations while respecting different physical processes, nonstationarity, operational constraints and uncertainty?

## 1. The state is not the sensor

At a river reach, one gauge is rising, a radar-derived surface suggests inundation, two crowd reports disagree and an upstream gauge is stale. None is the flood state. The state comprises water levels and flows across a connected system, local drainage, inundation probability, depth and potentially velocity and duration. Observations are emissions from this state through source-specific error processes.

For drought, the gap is larger. Rainfall deficit, vegetation condition, water access, livestock stress and market effects develop at different rates. A staged institutional classification summarises conditions for action but is not the underlying environmental process. Fire adds unobserved ignition and intervention; locust adds biological lifecycle and movement; landslide adds local threshold behaviour; heat adds exposure inside buildings and service dependence.

The modelling objective is a posterior distribution:

\[
p(Z_{1:G,1:T},E_{1:M}\mid Y_{1:S,1:G,1:T},X_{1:G,1:T},A_{1:G,1:T}),
\]

where \(Z\) is latent or physical state, \(E\) event objects, \(Y\) observations, \(X\) exogenous covariates and \(A\) recorded interventions. The posterior supports estimates and forecasts. It does not confer authority to issue a warning or execute a financial action.

## 2. Modelling principles

### 2.1 Start with a transparent baseline

Every hazard needs an interpretable baseline that can run with limited data, be reproduced by domain experts and remain available during advanced-model failure. Baselines provide honest comparisons and expose whether complexity adds value.

### 2.2 Separate the generative stages

The canonical factorisation is

\[
p(Y,D,O,I,F,U,Z\mid X,A)=p(Y\mid D,Z,q)\,p(D\mid O,q)\,p(O,I,F,U\mid Z,X,A)\,p(Z\mid X,A),
\]

**Figure 3.4 — Regime-to-event separation (factorised conceptual figure).** Observation, detection, occurrence, intensity, footprint and duration remain distinct.

where \(D\) is detection, \(O\) occurrence, \(I\) intensity, \(F\) footprint, \(U\) duration/recovery and \(q\) source quality. Exact factors change by hazard. The important discipline is that observation and occurrence are not collapsed.

### 2.3 Match topology to process

Administrative boundaries are useful for decisions but rarely define propagation. River direction, slope, wind, ecological continuity, road and service networks and atmospheric fields determine dependence. Models can aggregate to counties after respecting these structures.

### 2.4 Condition on intervention

Fire suppression, pest control, water release, drainage clearance, road closure and anticipatory action alter subsequent observations and impact. Treating action as random environmental behaviour biases learning. The state equation conditions on recorded intervention and acknowledges confounding where action targets severe states.

### 2.5 Report distributions and decomposed uncertainty

Point estimates are insufficient for thresholds, accumulation and extremes. The platform distinguishes observation, process, parameter, scenario, model-form and climate uncertainty. Where components cannot be identified separately, the limitation is stated.

## 3. Transparent baselines by hazard

### 3.1 Flood baseline

A flood baseline combines quality-controlled rainfall and gauge thresholds, terrain-based flow or susceptibility, and a simple inundation lookup or hydraulic relationship. River reaches use upstream lagged level or discharge. Urban cells use rainfall intensity, antecedent wetness, drainage capacity proxies and observed flood points. The output is a calibrated ordinal state or probability plus an empirical depth range.

The baseline can be expressed as logistic exceedance:

\[
\operatorname{logit}P(O_{g,t}=1)=\beta_0+\beta_1R_{g,t}^{(d)}+\beta_2S_{g,t-1}+\beta_3Q_{up,t-\ell}+\beta_4C_g,
\]

where rainfall accumulation \(R^{(d)}\), saturation \(S\), lagged upstream flow \(Q\) and capacity/susceptibility \(C\) have explicit units. It is not a substitute for hydraulic modelling but is auditable and operationally robust.

### 3.2 Drought baseline

A drought baseline standardises rainfall, vegetation, soil moisture and water-access indicators against stated climatologies, then combines them through published or expert-agreed weights and persistence rules. It retains each component so a green vegetation signal cannot hide water or livelihood deterioration. Duration since threshold exceedance is explicit.

\[
D_{g,t}=\sum_j w_j z_{j,g,t}, \qquad \sum_jw_j=1,
\]

with missing components reweighted only under an approved rule and marked. The baseline is compared with NDMA stages but does not relabel them.

### 3.3 Wildfire baseline

A baseline fire-danger score uses recent rainfall, temperature, humidity, wind, fuel/vegetation and seasonality. Candidate detection combines independent thermal or visual alerts. Spread uses a simple cellular or graph rule conditioned on wind, slope and fuel. The model separates ignition probability from detection and spread.

### 3.4 Locust/pest baseline

Structured verified sightings are moved forward using wind fields, feasible travel and lifecycle constraints, producing an envelope rather than a precise point. Habitat suitability uses rainfall and vegetation. Crop intersection is separate. FAO notes desert locust mobility and operational surveillance requirements [1]; Kenya's surveillance and control records are required for calibration [2].

### 3.5 Landslide baseline

Susceptibility from slope, geology, land cover and drainage is combined with rainfall intensity-duration and antecedent moisture. The output is threshold exceedance by hillslope unit. U.S. Geological Survey rainfall-threshold work provides comparative methodological guidance, not a Kenyan parameter source [3]. Local events, non-events and censoring are necessary for Kenyan thresholds.

### 3.6 Storm and heat baseline

Storm baselines use station/forecast exceedance for wind, rainfall or hail plus asset-specific exposure. Heat uses temperature-humidity or heat-index thresholds, nighttime persistence and local climatology; service and health consequences are modelled later. A national temperature threshold without acclimatisation or local baseline can misclassify risk.

## 4. A hierarchical spatial state

Let \(g\) index a spatial process unit and \(t\) time. A shared form is

\[
p(Z_{g,t}\mid Z_{g,t-1},Z_{\mathcal N(g),t-1},X_{g,t},A_{g,t}),
\]

where \(\mathcal N(g)\) is process-specific. Country and seasonal effects provide partial pooling; basin, ecological zone or urban area provides mid-level structure; local grids, reaches or slopes retain actionable detail.

Partial pooling matters where labels are scarce. A local parameter \(\theta_g\) may follow

\[
\theta_g\sim \mathcal N(\mu_{r[g]},\tau_{r[g]}^2),
\qquad
\mu_r\sim \mathcal N(\mu_0,\tau_0^2).
\]

This borrows strength while retaining local uncertainty. Pooling assumptions are validated; ecologically or structurally different areas should not be forced together merely because data are scarce.

Spatial support mismatch is handled explicitly. Point gauges, pixel classifications, road segments, catchments and county summaries observe different aggregates of the state. An observation operator \(\mathcal H_s\) maps latent field to source support:

\[
Y_{s,t}\sim p_s\left(Y\mid\mathcal H_s(Z_t),q_{s,t}\right).
\]

**Figure 3.1 — Hierarchical spatial latent-state model.** Country/region priors partially pool local process units while each source observes its native spatial support.

```{.mermaid #fig-3-2 alt="Hazard-specific transition topologies"}
flowchart TB
  ROOT[Common state interface: time, geometry, uncertainty and provenance]
  ROOT --> F1[Directed upstream reach]
  F1 --> F2[Downstream reach]
  F2 --> F3[Floodplain and drainage cell]
  ROOT --> W1[Wind, fuel and slope neighbourhood]
  W1 --> W2[Fire perimeter and intensity]
  ROOT --> L1[Lifecycle, wind and vegetation kernel]
  L1 --> L2[Locust trajectory envelope]
  ROOT --> S1[Susceptible and saturated hillslope]
  S1 --> S2[Runout, blockage and cascade]
  ROOT --> H1[Atmospheric and advection field]
  H1 --> H2[Local heat and storm modifier]
```

**Figure 3.2 — Hazard-specific transition topology.** Shared metadata does not imply shared physical adjacency.

This avoids pretending a county report occurred at a centroid or a pixel measures a whole farm.

## 5. Hazard-specific topology

### 5.1 Directed flood networks

Flood propagation follows directed river reaches and flow paths. A reach state depends on upstream flows with travel-time lags, local rainfall, storage and controls:

\[
Q_{r,t}=f_r(Q_{up(r),t-\ell_r},R_{r,t},S_{r,t},B_{r,t},A_{r,t})+\epsilon_{r,t}.
\]

Urban flooding also depends on drainage graphs that may reverse or surcharge. Surface cells connect through terrain and drainage capacity. A county border is an output overlay. Mass-balance or hydraulic constraints can regularise statistical estimates, and residual models can correct systematic process-model error without violating physical plausibility.

### 5.2 Fire neighbourhoods

Fire grids connect along wind, slope and fuel. Transition probability from unburned to burning depends on adjacent intensity and directional spread; burning to contained/extinguished depends on fuel and intervention. Ember transport may require longer-range edges. The model records whether perimeter contraction reflects containment, observation gap or classification change.

### 5.3 Locust movement fields

Locust state includes density, lifecycle and mobility. A movement kernel \(K(g'\mid g,W_t,V_t,k)\) maps current cell \(g\) to future cell \(g'\) using wind \(W\), vegetation \(V\) and stage \(k\). Reports update the posterior; control reduces density probabilistically. Boundary crossing triggers coordination but does not reset the event identity.

### 5.4 Landslide hillslopes

Hillslope units connect through drainage and runout, not generic adjacency. Susceptibility is largely static over short periods, while saturation and rainfall evolve. A slide may block a river or road, creating a separate cascade edge. Because failure is rare, the model needs careful negative sampling and should return wide intervals in uninstrumented slopes.

### 5.5 Heat and storm fields

Atmospheric variables form continuous fields with spatial covariance. Urban heat is modified by land cover, materials, elevation and ventilation; indoor conditions depend on buildings and power. Storm cells move, so time-lagged neighbourhoods follow advection. Compound rain-wind-hail effects may use a multivariate extreme or scenario model rather than independent probabilities.

## 6. Latent-regime model choices

### 6.1 Finite hidden Markov model

A finite HMM assumes discrete state \(Z_t\in\{1,\ldots,K\}\), Markov transitions and source emissions:

\[
P(Z_t=j\mid Z_{t-1}=i)=\pi_{ij},
\qquad Y_t\mid Z_t=k\sim p_k(Y).
\]

It is interpretable and computationally efficient. States can represent normal, watch, severe and recovery regimes, but labels emerge statistically unless constrained. The geometric duration implied by self-transition may be unrealistic for drought, and fixed transition probabilities miss season and covariate effects.

### 6.2 Sticky HMM

A sticky prior favours self-transition and reduces rapid switching. The sticky HDP-HMM formulation adds a self-transition parameter to Bayesian nonparametric state models [4]. It can stabilise regimes but can also hide genuine rapid change if stickiness is too strong. Hyperparameters are selected through predictive performance and duration calibration, not aesthetic smoothness.

### 6.3 Hidden semi-Markov model

An HSMM models state duration directly:

\[
U_n\mid Z_n=k\sim f_k(u),
\]

before transition to the next segment. This is attractive for drought and heat episodes, recovery states and possibly storm duration. Hydrometeorological applications have used semi-Markov duration modelling [5]. The price is greater inference complexity and the need to define duration distributions.

### 6.4 Switching state-space model

Continuous state \(x_t\) evolves under a regime-specific process:

\[
x_t=F_{Z_t}x_{t-1}+B_{Z_t}X_t+w_t,
\qquad
Y_t=H_{Z_t}x_t+v_t.
\]

This is suitable when river level, moisture, heat or perimeter are continuous but dynamics change by regime. Nonlinear physics may require extended/unscented filters, particle methods or simulation-based inference. The regime should have physical or operational interpretability.

### 6.5 Hierarchical Bayesian model

Hierarchical models share information across regions, hazards or exposure contexts while preserving local parameters. They are a framework rather than a single temporal assumption and can include spatial Gaussian processes, conditional autoregression, networks or mechanistic submodels. The challenge is computational scale, prior sensitivity and confounding between spatial smoothness and unobserved covariates.

### 6.6 iHMM/HDP-HMM

An infinite HMM places a nonparametric prior over a countably unbounded state set, allowing effective complexity to be learned from data. It is a candidate where regime number is genuinely unknown. It is not “infinite” operational complexity, nor proof of better forecasting. Sparse extremes can create unstable or uninterpretable states; computation and validation are harder; state labels may split by sensor artefact.

The iHMM belongs at the latent-regime layer. Conditional event frequency, severity, footprint and vulnerability remain separate. It is promoted only if it improves held-out calibration, duration, extremes, stability, decision value and feasibility over finite alternatives.

### 6.7 Selection by problem, not prestige

| Need | Plausible starting model | Key challenge |
|---|---|---|
| simple auditable stages | finite HMM | fixed states, geometric duration |
| persistent stages | sticky HMM | oversmoothing |
| explicit episode duration | HSMM | duration data and computation |
| continuous physical state with regime changes | switching state-space | nonlinear inference and identifiability |
| spatial sharing | hierarchical Bayesian | priors, scale and confounding |
| unknown regime count | iHMM/HDP-HMM challenger | stability and interpretability |

No single row wins across six hazards. Flood may combine a hydraulic/state-space model with event classification; drought may benefit from HSMM persistence; locust needs movement; landslide may use survival/threshold and spatial susceptibility; heat may use continuous fields and episode duration.

## 7. Covariate-dependent transitions and emissions

Transition probabilities should respond to weather, climate, soil, vegetation, season, terrain and intervention:

\[
P(Z_{g,t}=j\mid Z_{g,t-1}=i)=
\frac{\exp(\alpha_{ij}+X_{g,t}^{\top}\beta_{ij}+u_{g,ij})}
{\sum_{j'}\exp(\alpha_{ij'}+X_{g,t}^{\top}\beta_{ij'}+u_{g,ij'})}.
\]

Covariates must be available at forecast time. A post-event damage feature cannot improve an onset forecast retrospectively. Highly correlated climate indices need shrinkage, causal restraint or dimension reduction. Seasonal terms should not absorb a secular trend silently.

Source-specific emissions express sensitivity, specificity, measurement error and support. Examples include:

\[
Y^{gauge}_{g,t}\mid x_{g,t}\sim t_\nu(x_{g,t}+b_s,\sigma_s),
\]

\[
Y^{crowd}_{s,g,t}\mid O_{g,t}\sim \operatorname{Bernoulli}
\left(\operatorname{logit}^{-1}(\alpha_s+\gamma O_{g,t}+\delta C_{g,t})\right),
\]

where \(C\) includes connectivity or opportunity to report. The crowd model is an observation model, not a moral judgement about contributors. Satellite segmentation may use a beta-binomial or calibrated pixel likelihood with cloud and land-cover quality. NLP-extracted categories retain extraction uncertainty.

**Figure 3.3 — Source-specific emission model (equations above).** Gauge, crowd, satellite and NLP evidence retain different measurement and detection errors.

Correlated sources share latent error terms or duplication clusters. Conditional independence is never assumed merely because records have different IDs. A common upstream weather product creates dependence among derived models; a messaging cascade creates dependence among posts.

## 8. Occurrence, frequency, intensity, footprint and duration

### 8.1 Event identity

An event is a versioned object with hazard, onset distribution, geometry history, intensity fields, duration/recovery, parent/child relations and evidence lineage. Split and merge rules are peril-specific. Two urban flood cells may belong to one storm but separate drainage events; a locust swarm can split; a fire can spot across a gap.

### 8.2 Conditional occurrence and count

Given state \(Z=k\), event counts can use Poisson, negative-binomial, hurdle, zero-inflated or point-process models:

\[
N_{g,t,h}\mid Z_{g,t}=k\sim \operatorname{NegBin}(\mu_{g,t,h,k},\phi_{h,k}).
\]

A Poisson model is a useful baseline if mean and variance are similar and events are conditionally independent. Overdispersion, clustering and unobserved heterogeneity motivate negative binomial or Cox-process alternatives. Declustering rules and exposure time are explicit. Drought may be modelled as episodes rather than daily counts.

### 8.3 Detection process

For source \(s\), detection probability depends on intensity, coverage, quality and conditions:

\[
P(D_{s}=1\mid O=1,I,q,C)=\operatorname{logit}^{-1}(a_s+b_sI+c_sq+d_sC).
\]

False detection is separately estimated. If only detected events enter training data, ignoring this process biases frequency low in poorly observed areas and may bias intensity upward.

### 8.4 Intensity and footprint

Intensity distributions are hazard-specific: flood depth/velocity, drought deficit/duration, fire intensity/spread, pest density, landslide volume or runout, wind/hail/temperature. Positive continuous values may use gamma, lognormal, generalised Pareto tails, quantile models or process simulation. Multivariate dependence matters where depth and duration jointly drive damage.

Footprints can be fields, polygons, networks or trajectories. Evaluation uses proper scores at the native support plus operational summaries. Sharp-looking polygons must not hide probabilistic boundaries. For each location, the product can report inundation probability and conditional depth distribution rather than a deterministic edge.

### 8.5 Recovery

Recovery is not simply hazard cessation. Water recession, vegetation recovery, road restoration, livestock rebuilding and heat-health effects have different clocks. State models can include recovery regimes, but economic recovery belongs partly in impact/loss models. The event object records both physical end and consequence milestones.

## 9. Process-model interfaces

Physics-informed design can take three forms.

1. **Process model as baseline:** hydraulic, fire-spread, crop or atmospheric model directly produces ensembles.
2. **Statistical emulation:** a surrogate approximates expensive simulation within a validated parameter domain.
3. **Residual correction:** a statistical model learns systematic discrepancy while the process model provides structure.

Data assimilation updates process state from observations. For ensemble members \(x_t^{(m)}\), an ensemble Kalman or particle approach adjusts weights/states according to observation likelihood. Highly nonlinear thresholds and multimodal states may require particles or simulation-based inference. The assimilation method must respect mass balance, nonnegative variables and action history.

Process models are not immune to error: terrain, drainage, fuel, soil and initial conditions can be wrong. The architecture preserves input versions and separates parameter from forcing uncertainty. A residual model is constrained against extrapolating beyond the process domain.

## 10. Nonstationarity and climate/land-use change

Kenya's climate observations and official state-of-climate reporting describe changing temperature and extreme conditions [6]. Urbanisation, drainage alteration, deforestation/restoration, agricultural change, infrastructure and observation systems also change loss-generating processes. Historical stationarity cannot be assumed.

Models address nonstationarity through time-varying covariates, change points, dynamic parameters, scenario-conditioned simulation and periodic recalibration. Climate-model projections inform scenarios and stress tests; they do not supply precise local event probabilities without bias correction, downscaling and uncertainty disclosure. Observation-network improvements can create apparent event increases through better detection.

Transportability is tested across time and place. A model trained in one basin or urban area may transfer poorly because rainfall-runoff, drainage and settlement differ. Hierarchical priors permit adaptation, but local data remain necessary. Scenario uncertainty is kept separate from current-event observation uncertainty so users know whether range reflects today's missing gauge or future emissions and model spread.

## 11. Compound and cascading hazards

Compound modelling begins by stating the relationship. Hazards may share a driver, occur sequentially, alter each other's probability or jointly affect one exposure. Drought, heat and wind can jointly condition fire; extreme rainfall can jointly drive river flood and landslide; storm can damage power while heat increases the consequence of outage. Locust suitability may depend on preceding rainfall and vegetation, while crop vulnerability depends on prior drought.

A multihazard state can use coupled components:

\[
p(Z^{(1)}_t,\ldots,Z^{(H)}_t\mid Z_{t-1},X_t,A_t)
=\prod_h p(Z^{(h)}_t\mid Pa_h(Z_{t-1},X_t,A_t)),
\]

where the parent graph is defined by plausible mechanisms. Fully joint state spaces quickly become intractable, so only supported dependencies are coupled. Scenario libraries capture rare combinations where data cannot estimate a flexible joint distribution.

Cascades are represented as event-to-event transitions: storm causes power outage; landslide blocks road; road blockage delays response; fire interrupts water infrastructure. Timing and conditional probability are retained. Later loss modelling prevents double counting by assigning consequences to shared nodes and reconciliation rules.

Attribution is not assumed. That a flood follows a storm does not establish that a particular infrastructure failure was caused by inundation. The event graph carries hypotheses and verification status.

## 12. Uncertainty decomposition and communication

Let a target \(T\) be predicted loss-driving intensity. Its predictive variance can be conceptually decomposed:

\[
\operatorname{Var}(T\mid\mathcal I)
=U_{obs}+U_{process}+U_{param}+U_{model}+U_{scenario}+2\,Cov(\cdot),
\]

where covariance prevents a naive additive interpretation. Practical systems estimate components through ensembles, posterior draws, model ensembles and scenarios.

- **Observation uncertainty** includes sensor error, location, latency and missingness.
- **Process uncertainty** is irreducible variability conditional on state and forcing.
- **Parameter uncertainty** reflects limited calibration data.
- **Model-form uncertainty** reflects alternative structures and omitted mechanisms.
- **Scenario uncertainty** covers future forcing, intervention and socioeconomic paths.
- **Climate uncertainty** includes internal variability, model and emissions components at longer horizons.

Products show which component dominates. A current flood estimate may improve when imagery arrives; a 2050 investment scenario remains dominated by climate and exposure assumptions. A 90% interval is explained as model-conditional and not a guarantee of coverage under structural failure.

Decision thresholds use expected consequence, reversibility and risk appetite alongside probability. A low-probability, high-consequence slope failure may warrant inspection. The platform presents probability and consequence separately rather than encoding both in an undocumented colour.

## 13. Inference and computational feasibility

Operational inference must meet latency and resilience budgets. Filtering estimates current state as data arrive; smoothing reconstructs past state using later evidence; forecasting propagates forward. The three outputs are labelled distinctly.

Finite HMMs may use forward-backward and Viterbi algorithms. Linear Gaussian state-space models use Kalman filtering; nonlinear/non-Gaussian systems use extended, unscented, ensemble or particle methods. Bayesian hierarchical models can use Markov chain Monte Carlo for research and variational or sequential approximations for operations, provided approximation error is tested. iHMM/HDP-HMM inference may use Gibbs or variational methods and needs convergence/stability diagnostics.

Spatial scale creates trade-offs. A national one-metre grid is neither computationally feasible nor supported by observations. Multi-resolution modelling uses coarse national screening, hazard-relevant process units and local refinement around events. Tiling preserves overlap to avoid edge artefacts. Hot paths update active regions frequently while stable areas update more slowly.

An operational service maintains deterministic input snapshots, seeded simulation where possible, containerised or otherwise reproducible environments, model registry, resource monitoring and fallback. Posterior compression used for downstream loss modelling is validated so it does not erase tails.

## 14. Validation design

### 14.1 Baselines and splits

Each challenger is compared against climatology/persistence, hazard threshold and simple statistical baselines. Random row splitting is generally invalid because neighbouring times and pixels leak event information. Required splits include:

- complete-event holdout;
- future-period holdout;
- spatial or basin/ecozone holdout;
- source holdout to test network failure;
- extreme-state holdout or stress testing;
- intervention-policy holdout where feasible.

Training and evaluation use data available by historical knowledge time for operational claims.

### 14.2 Metrics

Occurrence probability uses reliability diagrams, Brier/log score, discrimination and threshold-specific false/missed event rates. Footprint uses probabilistic pixel scores, intersection-over-union, boundary distance and area bias. Intensity uses proper predictive scores, quantile coverage and tail diagnostics. Duration uses onset/end error and survival calibration. Movement uses trajectory and coverage probability. Lead time is measured at predefined usable accuracy.

Metrics are stratified by hazard, intensity, geography, season, observation coverage and vulnerable communities. Average success cannot conceal systematic failure in remote cells or extremes.

### 14.3 Hindcasting and prospective shadow mode

Hindcasts reconstruct historical operations with point-in-time data. They test repeatability across known events but risk selection and changing systems. Prospective shadow mode runs without controlling consequential decisions, records latency/outages and compares outputs with authorised observations and outcomes. Operators document whether products would have been actionable.

### 14.4 Calibration under rare extremes

Catastrophe tails contain few observations. Evaluation combines empirical holdout, process constraints, extreme-value diagnostics, synthetic stress and expert elicitation with clear labels. Synthetic events test failure but cannot prove real-world calibration. Tail parameter uncertainty is propagated to loss.

### 14.5 Champion-challenger gate

A challenger is promoted only when it satisfies all agreed conditions: improved proper score or justified non-inferiority; stable tail and subgroup behaviour; credible physical outputs; useful lead time; feasible cost/latency; interpretability for operators; reproducibility; and safe fallback. A gain in discrimination cannot compensate automatically for worse calibration. Promotion can be limited to a hazard, region or task.

```{.mermaid #fig-3-5 alt="Champion-challenger model validation pipeline"}
flowchart LR
  BASE[Transparent hazard-specific baseline] --> SPEC[Pre-registered challenger and metrics]
  SPEC --> BACK[Point-in-time hindcast]
  BACK --> HOLD[Event, spatial, time, source and extreme holdouts]
  HOLD --> IND[Independent scientific and statistical validation]
  IND --> SHADOW[Prospective shadow operation]
  SHADOW --> GATE{All promotion conditions met?}
  GATE -- Yes --> CHAMP[Bounded champion for named task]
  GATE -- No --> REJECT[Reject, remediate or narrow]
  REJECT --> BASE
  CHAMP -. drift, failure or incident .-> BASE
```

**Figure 3.5 — Champion-challenger validation pipeline.** Promotion is task-bounded and rollback-capable.

## 15. Six synthetic worked examples

All quantities below are illustrative, not calibrated Kenyan results.

### 15.1 Flood update

A river reach begins with a 20% threshold-exceedance probability. Upstream rainfall and gauge rise lift it to 55%. Two reports share one image and therefore contribute one lineage; an independent radar classification later lifts it to 78%, while the stale local gauge widens depth uncertainty. The model reports `P(inundation)=0.78` and conditional median depth with an interval. It does not report “78% image confidence,” and it does not issue the public warning.

### 15.2 Drought persistence

Three monthly indicator vectors suggest transition from normal to stress. A finite HMM switches back after one improved rainfall observation; an HSMM remains in stress because vegetation and water indicators and learned duration support persistence. Validation determines which reflects outcomes, rather than assuming smoothness is better. NDMA's stage remains separately observed.

### 15.3 Fire detection and spread

A camera smoke detection has calibrated 0.65 class probability. A thermal anomaly with an independent lineage arrives; the ignition posterior rises. Wind shifts, changing the forecast perimeter distribution. Suppression begins and enters the transition model. The first-detection time remains later than inferred ignition time, with an interval.

### 15.4 Locust trajectory

Verified field observations in two cells update a wind-conditioned movement kernel. The 48-hour product is a 50/80/95% envelope, not a deterministic arrow. Crop-stage data create an exposure overlay in Part 4. A control treatment reduces expected density but increases uncertainty because efficacy is locally unverified.

### 15.5 Landslide threshold

Antecedent saturation and rainfall exceed a local screening threshold on several hillslopes. One crack report is poorly located. The model allocates its likelihood across candidate slopes and returns a high-consequence inspection queue. It does not convert the crack's object-classifier score into slope-failure probability.

### 15.6 Heat/storm compound

Nighttime heat persistence and power outage state are jointly modelled; a storm cell raises wind-damage probability. The product presents a heat field, outage scenario and their conditional overlap. Health impact remains a separate exposure/vulnerability calculation.

## 16. Reproducibility and model records

Every production estimate records data snapshot, source-health state, code/model version, parameters or posterior identifier, spatial support, forecast origin, issue time, horizon, scenario, random-seed policy, compute environment and fallback status. Model cards document purpose, prohibited uses, training domain, metrics, limitations, owners and review date.

The event catalogue is versioned. Analysts can reproduce what was estimated operationally and compare it with a later best-available reconstruction. Corrections never overwrite the audit record. Interfaces expose uncertainty samples or sufficient representations to the loss engine, not merely a rounded risk band.

## 17. Limitations

Rare-event inference remains data-limited. Observation networks are preferentially located. Detection changes over time. Physical models have uncertain inputs; flexible statistical models can fit artefacts. Interventions are confounded by severity. Compound extremes are especially sparse. A latent state may be mathematically identifiable but operationally meaningless.

The framework does not claim that every hazard requires an HMM or Bayesian model. Nor does it derive public thresholds. Models are bounded to their training/process domain and return wider uncertainty or abstain outside it. Expert judgement remains documented evidence, not an invisible parameter adjustment.

## 18. Flood model specification and diagnostics

### 18.1 State vector and scales

A basin implementation can define reach state \(x_{r,t}=(Q,H,S)\) for discharge, stage and storage and cell state \(w_{g,t}=(p_{wet},d,v,u)\) for inundation probability, depth, velocity and duration. Rainfall forcing has accumulation intervals; gauge stage uses a named datum; terrain and roughness versions are fixed. Urban submodels add inlet/drain capacity, imperviousness and known obstruction states.

Filtering assimilates gauge likelihoods and radar/crowd emissions. A gauge at one reach observes stage, not the entire cell field. Radar observes wet/dry surface with land-cover-dependent confusion. A photograph can emit water presence or protocol-based depth. Upstream observations update downstream forecasts through travel time, but downstream water can backwater upstream under defined topology.

### 18.2 Event and boundary logic

Event onset is a distribution around threshold/connected inundation emergence. The catalogue may create subevents for disconnected urban drainage systems under the same meteorological parent. Footprint polygons are probability contours with boundary uncertainty. Recession ends physical inundation; road/service restoration remains consequence state.

### 18.3 Diagnostics

Hydrographs are checked for timing, peak and volume. Reliability is assessed by lead time. Depth validation uses marks/surveys and separates geometry error. Footprint metrics stratify open water, urban shadow and vegetation. Mass-balance residual, negative depth, discontinuous upstream/downstream state and improbable expansion generate physics flags. Gauge-removal tests expose dependence on a single station.

## 19. Drought model specification and diagnostics

### 19.1 Multidimensional latent state

Drought state can comprise meteorological deficit \(M\), soil/crop moisture \(A\), vegetation/forage \(V\), hydrological availability \(W\), livelihood stress \(L\) and duration \(U\). These components need not deteriorate together. A dynamic factor or switching state-space model allows shared climate forcing and component-specific lag:

\[
x_{g,t}=F_kx_{g,t-1}+B_kX_{g,t}+w_{g,t},\quad Z_{g,t}=k.
\]

Institutional drought stage is an observed/action classification linked to, but not equated with, \(Z\). Reporting/market indicators have feedback: distressed sales can lower livestock price even as rainfall improves. Model outputs therefore show component trajectories alongside regime probability.

### 19.2 Episode, duration and recovery

An HSMM can define entry, persistence and recovery duration. Episode definition uses an approved multi-indicator rule and sensitivity alternatives. Short rainfall relief may improve meteorology without restoring water, vegetation or herds. Recovery can be slower than onset and conditioned on successive shocks.

### 19.3 Diagnostics

Hindcasts hold out whole seasons and arid/semi-arid areas. Metrics assess stage/component calibration, onset lead, duration and recovery, not just correlation with vegetation. Ground observations evaluate water access and forage meaning. Quiet reporting areas are stress-tested by withholding community sources. The model is rejected if it merely reproduces seasonality or observation density.

## 20. Fire model specification and diagnostics

### 20.1 Ignition, detection and spread

Ignition is a point-process candidate conditioned on fuel, weather, human/lightning proxies and season. Detection has camera, thermal and human likelihoods. Spread state uses burning intensity, fuel and direction. A simplified transition for cell \(g\) is

\[
P(B_{g,t+1}=1)=1-\prod_{j\in\mathcal N(g)}
\left[1-p_{jg}(W,S,F)B_{j,t}\right],
\]

conditioned on suppression and long-range spotting. This is a baseline/challenger component, not a substitute for fire-behaviour science.

### 20.2 Intervention and counterfactual

Suppression dispatch is confounded by perceived severity. Model training records start, resource, access and containment rather than attributing smaller fires to detection alone. Counterfactual spread ensembles compare action timings under the same weather/fuel draws and disclose behavioural assumptions.

### 20.3 Diagnostics

Evaluate first-detection delay, false alarms by smoke/dust/cloud, perimeter calibration, rate/direction of spread, final area and extreme wind cases. Hold out fires, sensors and ecological zones. Night, smoke, glare and network outage form dedicated strata. A model that improves average perimeter but misses fast spread fails tail promotion.

## 21. Locust and pest model specification and diagnostics

### 21.1 Biological state and movement

State includes species verification, lifecycle stage, density, breeding suitability and movement. A state-transition kernel combines maturation, reproduction/mortality, wind-assisted movement and vegetation attraction. Survey observation depends on search effort:

\[
P(D_{g,t}=1\mid density,effort,visibility)=1-\exp[-\lambda(density)\,effort\,q].
\]

Ignoring survey effort makes well-surveyed areas look more infested. Treatment is an intervention with coverage and efficacy distributions. Treated area is not assumed pest-free.

### 21.2 Cross-boundary event identity

Particle/ensemble trajectories retain one event across county borders and link to international surveillance where lawful. Administrative summaries integrate trajectory probability. Alerts and control remain owned by relevant plant-protection authorities. Crop exposure is joined only after biological state estimation.

### 21.3 Diagnostics

Evaluate envelope coverage, directional error, density/stage classification, lead to field verification and treatment-adjusted persistence. Hold out swarms, survey teams and regions. Sensitivity tests wind product, movement limit, vegetation and under-reporting. False species classification is reviewed separately because control consequence is high.

## 22. Landslide model specification and diagnostics

### 22.1 Susceptibility, trigger and movement

Long-term susceptibility \(S_g\) uses slope, geology, land cover, drainage and modification. Dynamic trigger \(T_{g,t}\) uses intensity-duration and antecedent moisture. Failure probability may use survival or threshold formulation:

\[
\lambda_{g,t}=\lambda_0(t)\exp(\beta_SS_g+\beta_RT_{g,t}+u_g).
\]

The model distinguishes initiation from runout. Runout intersects roads/buildings and can create dam/blockage cascade. Very local geometry means input positional error is propagated.

### 22.2 Rare labels and censoring

Event catalogues overrepresent damaging/accessibile slides and underrecord non-damaging failures. Background sampling is not true non-event data. Case-control likelihood, occupancy/detection models or carefully defined observation windows address sampling. Expert-mapped susceptibility is a prior or comparator, not ground truth without uncertainty.

### 22.3 Diagnostics

Spatial holdout occurs by slope system, not random pixels. Evaluate calibration, top-k inspection value, onset window, runout overlap and high-consequence misses. Stress includes a communications-blocking slide and rainfall beyond training. A high-resolution map is not published where input resolution cannot support it.

## 23. Severe storm and heat model specification

### 23.1 Storm cells and extremes

Storm tracking identifies cells and advection; observations include gauges/stations, satellite/radar and damage reports. Wind, rainfall and hail have joint dependence. Marginal extreme distributions plus a dependence structure or physically consistent ensemble estimate joint severity. Reporting-process modelling prevents damage density from becoming storm intensity.

Diagnostics measure field calibration, track/lead, peak/tail and compound rain-wind outcomes. Station siting and instrument limits are examined. Damage validation remains separate from meteorological truth.

### 23.2 Heat episodes and local inequality

Heat state includes dry-bulb temperature, humidity, nighttime minimum/persistence, radiant/urban modifiers and indoor/service conditions. Episodes use locally calibrated climatology and health/operational thresholds owned by authorised institutions. A spatial hierarchical model combines stations and remote sensing while avoiding the assumption that land-surface temperature equals human air exposure.

Indoor and occupational observations are source emissions with privacy and selection bias. Power/cooling availability changes vulnerability rather than meteorological heat. Diagnostics include nighttime, urban/rural, station-sparse and outage strata; outcomes can be health/service indicators with separate ethical controls.

## 24. Model identifiability, leakage and debugging

Latent models can exchange labels, split one physical regime or absorb source failure as a new hazard state. Diagnostics include posterior state occupancy, transition stability across seeds/samples, label alignment, dwell distributions, emission separation and sensitivity to priors. A state is named only after domain interpretation; otherwise it remains an indexed statistical state.

Leakage audits trace every feature's event and knowledge time. Derived claims/damage features cannot enter hazard forecasts issued before damage. Spatial leakage checks shared satellite tiles, river connectivity and duplicate images. Target leakage can occur when an institutional stage—partly based on the same inputs—is used both as a feature and truth.

Debugging begins at generative components: observation likelihood, source health, transition, process forcing, event extraction and post-processing. Global score improvement cannot justify a component that violates units or physics. Posterior predictive checks simulate observations and compare distribution, missingness, persistence and extremes with reality.

## 25. Decision-value validation

Scientific skill and decision value are related but not identical. For action \(a\) with loss/cost function \(C(a,H)\), compare policies using posterior forecasts:

\[
V=E[C(a_{baseline},H)-C(a_{model},H)].
\]

The evaluation predefines feasible actions and deadlines. A five-minute lead gain after roads are already closed has no operational value. A modest calibration improvement near an evacuation threshold can matter greatly. Value is stratified by geography and consequence so improvements do not systematically benefit only highly observed assets.

Decision-value simulation does not prove realised avoided loss. It tests whether forecasts could improve choices under stated cost assumptions. Prospective pilots then record actual use, while causal evaluation addresses outcomes.

## 26. Minimum hazard-model output contract

Every output contains hazard, event/version, forecast origin, issue/knowledge time, horizon, native geometry/support, state definition, occurrence probability, conditional intensity/footprint/duration distributions as applicable, observation/source-health summary, uncertainty components, scenario/intervention assumptions, model/data versions, validation domain, degraded status, official/model label and permitted use.

If a quantity is not modelled, it is absent rather than zero. If state is ordinal, categories and calibration are supplied. If samples are compressed, tail preservation is validated. Downstream consumers acknowledge the version and cannot infer finer resolution than native support.

## 27. End-to-end synthetic hindcast protocol

This protocol is a template and contains no empirical Kenyan result. It demonstrates what must be fixed before comparing models.

### 27.1 Study frame

For each hazard, the team defines spatial support, observation interval, forecast origins, horizons, event catalogue cutoff and operational use. Flood might use river reaches and urban cells at hourly intervals with 0–48-hour horizons; drought might use livelihood zones monthly with one- to three-month horizons; fire may use sub-hourly grids; locust daily trajectories; landslide hillslopes during rainfall; heat daily/episode fields. The decision deadline is stated alongside horizon.

Historical sources are reconstructed by knowledge time. Current network coverage is not projected backward. Corrected final observations form a separate best-available reference. Exposure and damage are excluded from hazard inputs unless the task is explicitly impact nowcasting.

### 27.2 Fold construction

An outer loop holds out complete events and regions. A temporal fold tests later years; a geographic fold tests untrained basins/ecozones; a source-ablation fold removes a major feed. Inner folds tune parameters. Duplicate imagery, shared storm systems and connected river events stay within one fold. Evaluation reports sample sizes and event-intensity distribution.

The transparent baseline, current operational method if any, and each challenger receive identical available evidence. A process model may have different inputs only when this reflects a realistic operational configuration, and the difference is disclosed.

### 27.3 Pre-registered metrics and thresholds

Primary metrics are limited to those matching use: calibrated occurrence at decision horizon; useful lead time; probabilistic footprint/intensity; or episode duration. Secondary metrics diagnose. Promotion thresholds specify both overall and critical strata. For example, a challenger may require lower Brier score with non-inferior severe-event recall, calibration slope/intercept within agreed bounds, no material remote-area deterioration, latency below deadline and successful gauge-outage fallback.

Thresholds are not adjusted after observing results without a labelled exploratory phase. Statistical uncertainty uses event-level bootstrap or posterior comparison that respects dependence. Practical significance accompanies p-values.

### 27.4 Error review

Every severe miss and disruptive false alarm receives a case file: evidence available, source health, baseline/challenger posterior, physical evolution, operator interpretation and consequence. Errors are classified as observation, representation, process, parameter, post-processing, interface or use. Corrective action targets the class; retraining is not the default answer.

### 27.5 Prospective confirmation

Hindcast success permits shadow mode, not decision automation. Prospective operation records true latency, outage, user comprehension and emergent source patterns. The model is frozen for an evaluation period except safety fixes. A final report separates retrospective, shadow and live evidence.

## 28. Synthetic multi-hazard numerical walk-through

The following values are deliberately illustrative and cannot be used for pricing, warning or site selection.

### 28.1 Observation likelihood

Suppose one grid cell has prior flood occurrence 0.10. An independent gauge threshold has sensitivity 0.85 and false-positive probability 0.05; it is positive. Ignoring other evidence, Bayes' rule gives

\[
P(O=1\mid D=1)=\frac{0.85(0.10)}{0.85(0.10)+0.05(0.90)}\approx0.65.
\]

Two reposts of the same photograph are not two additional independent tests. If incorrectly multiplied, they would create unjustified certainty. Instead their root image supplies one likelihood, adjusted for uncertain location and capture time. An independent radar observation adds evidence through a land-cover-calibrated emission. The posterior remains conditional on the simplified model and is not an official warning.

### 28.2 Regime transition

A synthetic drought cell has transition probabilities from normal to stress of 0.08 in neutral conditions and 0.25 under severe rainfall/vegetation covariates. Once in stress, an HSMM duration distribution gives median persistence four months. One improved rainfall month changes meteorological state but the joint recovery probability remains lower because water and livelihood indicators lag. The model shows these components; it does not overwrite an institutional drought stage.

### 28.3 Event count and severity

In a synthetic fire season, latent regime `extreme-dry-windy` raises conditional count mean and spread-tail scale. The annual event set samples regime path, ignition counts, detection, footprints and suppression. The iHMM, if used, proposes regimes; it does not directly generate financial loss. Part 4 applies exposure and vulnerability to each footprint.

### 28.4 Movement

A locust particle ensemble begins around a verified survey geometry. Wind-conditioned kernels move particles; lifecycle and mortality weights evolve; a treatment polygon reduces particle weights by sampled efficacy. At 24 and 48 hours, quantile envelopes are calculated. A later survey outside the 95% envelope triggers error review rather than automatic deletion as an outlier.

### 28.5 Local threshold

A landslide hillslope has high static susceptibility but no trigger exceedance; another has moderate susceptibility and extreme antecedent rainfall. Their posterior probabilities can cross. An uncertain crack report overlaps both. The output retains high consequence and uncertain probability separately, allowing an inspector to prioritise without claiming deterministic failure.

### 28.6 Compound scenario

A heat field and feeder-outage probability overlap a clinic service area. The meteorological and infrastructure models share storm covariates, so multiplying marginal probabilities would be wrong. A coupled scenario draws the common driver, then conditional heat/outage states. Health consequence is calculated only after patient/service vulnerability enters downstream.

## 29. Climate and scenario stress library

A governed stress library complements probabilistic catalogues. Scenarios are severe but plausible narratives with reproducible parameter changes. They are not assigned return periods unless evidence supports them.

**Flood stresses** include gauge network loss during a spatially extensive rainfall event; urban drainage blockage concurrent with river rise; and consecutive events before recession/repair. **Drought stresses** include multi-season deficit, temporary rainfall false recovery and concurrent market/water infrastructure stress. **Fire stresses** include drought-conditioned fuels, extreme wind, night detection degradation and suppression-access failure. **Locust stresses** include rapid boundary crossing, simultaneous survey gaps and control efficacy uncertainty. **Landslide stresses** include rainfall beyond calibration, multiple road blockages and river damming. **Storm/heat stresses** include night heat, wind damage and extended power/telecommunications outage.

Each scenario records driver, state transitions, source failures, interventions, affected output components and model limitations. Baseline and challenger run identically. Scientific reviewers can reject implausible combinations. Users receive a scenario narrative, not a spurious probability.

## 30. Transportability decision framework

Transport to a new location begins with causal similarity, not geographic distance. The team compares hazard physics, climate/seasonality, terrain/river/fuel/ecology, observation process, intervention, exposure context and outcome definition. It maps which parameters are structural, shareable, locally adaptable or unknowable.

Four transport levels are available:

1. **Interface only:** schema and governance transfer; model rebuilt locally.
2. **Prior transfer:** parameters supply weak priors updated with local data.
3. **Calibrated transfer:** representation transfers, with local calibration and validation.
4. **Direct application:** rare, requiring strong equivalence and holdout evidence.

Performance is reported before and after local adaptation. If labels are too sparse, the product remains screening with wider uncertainty and human verification. Transfer cannot be justified by a national average score.

## 31. Operational model report template

Every issue contains an executive statement in plain language: what may be happening, spatial/time horizon, important uncertainty, changed evidence, authoritative-status relationship and usable actions. Technical annex gives posterior summaries, source coverage, diagnostics, model and fallback. Machine interface supplies samples/quantiles and metadata.

The report explicitly lists contradictions: for example, radar indicates water while local verified reports indicate a passable elevated road; model probability is high while official warning remains unchanged; drought environmental state improves while livelihood stress persists. Contradictions are not averaged away.

An update note attributes movement to new observations, model correction, exposure-independent process evolution or scenario change. Silent retrospective smoothing is forbidden in operational reports. A later forensic reconstruction has a separate label and identifier.

## 32. Online updating and late evidence

At each cycle, the filter ingests observations whose knowledge time falls since the last watermark, along with correction and source-health events. Idempotent IDs prevent repeated processing. Late observations can update current state and trigger a bounded lookback recomputation, but the originally issued product remains immutable.

A nowcast uses all admissible evidence at issue time. A short forecast propagates weather/process ensembles and state uncertainty. A smoother, run later, reconstructs the event for science and claims calibration. Products name `filter`, `forecast` or `smoother`. Performance credits only evidence available operationally.

Out-of-sequence measurements require care in state-space filters. Options include fixed-lag smoothing, particle-history reweighting or replay from checkpoint. The method and maximum lookback are chosen for latency/cost. A very late record may enter forensic reconstruction only. Corrections that materially affect a live product notify the product owner.

Online adaptation of parameters is more constrained than state updating. Model weights normally remain frozen through an event to avoid feedback and instability. Calibrated reliability/source-health can update under bounded rules, while full retraining follows governance. Novel conditions widen uncertainty or trigger expert override rather than silent learning.

## 33. Missingness, censoring and observation-network change

Missingness has mechanisms: scheduled absence, communications/power, sensor failure, unsafe/unreachable field, lack of contributors, cloud/occlusion or institutional delay. The model includes missingness indicators and, where necessary, an observation-opportunity model. Forward filling is allowed only for variables and durations justified by process and labelled as imputation.

Censoring occurs when gauges exceed range, cameras saturate, surveys record only “above threshold” or damage systems cap categories. Likelihoods encode lower/upper/interval censoring. Treating a clipped extreme as its maximum recorded value biases tails downward.

Network expansion creates nonstationary detection. Event catalogues include observation effort and source availability. Frequency models can use offsets or detection submodels. Comparisons across years separate physical change from improved detection. Removing a source during validation estimates reliance and reveals whether a seemingly robust model is an echo of one upstream product.

## 34. Prior construction and expert knowledge

Priors encode physical bounds, plausible persistence, spatial scale and scarcity. They are documented with elicitation source and sensitivity. Weakly informative priors regularise; informative priors from foreign studies require transport rationale. A prior cannot be selected solely because it produces a preferred warning frequency or financial result.

Experts can specify order constraints—higher rainfall should not reduce flood probability within an appropriate conditional range—or plausible duration and movement. Constraints are checked for interactions and exceptions. Prior predictive simulation asks whether the model generates physically possible event counts, intensities and footprints before seeing data.

Posterior sensitivity varies priors and model structures. When tail or sparse-region results remain prior-dominated, the report says so. Expert disagreement becomes alternative priors/scenarios with weights justified, not an average that hides distinct mechanisms.

## 35. Ensemble and model-form uncertainty

An ensemble can combine process, statistical and latent-state models, but weights are estimated on proper scoring and stability with event holdouts. Bayesian model averaging, stacking or simple robust weighting are candidates. The platform avoids performance double counting when models share data or code.

Ensemble disagreement is informative. If flood hydraulic and remote-sensing statistical models diverge, the product may widen uncertainty and request verification. A weighted mean polygon can be physically incoherent; sampling full model members preserves shapes. For rare extreme scenarios, equal/plausibility weighting may be more honest than unstable empirical optimisation.

Weights are versioned and may vary by hazard, horizon, geography and condition only with sufficient validation. A global ensemble score cannot conceal that one model dominates a region outside its domain. The transparent baseline remains visible even if not included in the operational ensemble.

## 36. Computational assurance

Numerical tests cover probability normalisation, nonnegative/physical bounds, spatial indexing, network direction, unit conversion, time zones, daylight-saving irrelevance/local EAT display, missing/censored likelihoods, deterministic replay and seeded stochastic tolerance. Synthetic micro-cases have known posterior or qualitative response.

Performance tests use peak event volume and source outage/recovery. Backpressure prioritises source integrity over dropping records silently. Approximate inference is compared with a higher-fidelity reference on manageable subsets. Particle degeneracy, MCMC convergence and variational under-dispersion have monitored diagnostics.

Model service outputs contain checksum and health. If inference diverges or resource limits truncate ensembles, the run fails/degrades visibly; it does not return incomplete samples as full posterior.

## 37. Hazard-state governance checklist

Before use, the model owner shows: physical/latent state definition; native support and horizon; observation and detection process; transition/propagation; event extraction; intervention handling; uncertainty; priors; baselines; holdouts/metrics; subgroup and extreme results; compute/latency; failure/fallback; model card and owner. Domain reviewers confirm units and topology.

The model fails acceptance when a confidence score becomes occurrence probability, frequency and severity collapse, administrative adjacency substitutes for process, future/post-event data leak, duration is implicit and wrong, source silence becomes safety, intervention is ignored, extreme behaviour is implausible, or novelty is the principal promotion argument.

## 38. Validation report structure

The validation report starts with the task, operational baseline and decision deadline. It describes event catalogue, observation-network evolution, knowledge-time reconstruction, spatial support, missing/censored data and interventions. It shows model equations/topology, priors, inference and event extraction at enough detail for independent replication.

Results are presented in layers. Observation fit does not substitute for state validation. Occurrence calibration is shown with reliability and proper scores; intensity/footprint with interval/field metrics; duration and movement with their own diagnostics; extremes with case and stress review. Results are stratified by event severity, geography, season, source availability and relevant coverage groups. Latency, compute and degraded-mode results are included.

The report compares baseline and challenger on identical folds and explains practical significance. It lists every severe miss and disruptive false alarm, physical implausibility, operator misunderstanding and source/model dependency. Model-form alternatives and prior sensitivity are visible. An executive summary states precisely which hazard, geography, horizon and product the model is fit for—and prohibited uses.

## 39. Forecast verification under changing thresholds

Operational authorities can change warning classifications or thresholds. The scientific forecast should be validated against physical/observational reference and operational decision outcomes separately. Otherwise a model can appear to degrade when policy changed or merely imitate the authority used as its label.

Threshold evaluation uses cost-loss curves across probabilities and actions. A single chosen cutoff is reported with false/missed events, lead and workload, but the underlying calibrated probabilities remain. If authorities set a new cutoff, the platform can remap decisions without retraining the physical model, subject to approval.

Rare-action thresholds need uncertainty and qualitative case review. Back-testing many cutoffs and selecting the best on the same extremes is overfitting. Prospective shadow mode confirms alert frequency and human response.

## 40. Cross-hazard consistency tests

The shared interface is tested using one synthetic event per hazard. Each must expose occurrence/detection separately, native topology, intensity/footprint/duration as applicable, intervention, source health and uncertainty. Unit and time checks ensure flood depth, drought anomaly, fire intensity, pest density, landslide probability/runout and heat temperature/persistence cannot be mixed.

Compound tests draw common driver once and verify that child hazards are conditionally consistent. Cascades preserve parentage and do not rewrite the primary event. Administrative aggregation sums/integrates fields correctly without changing event trajectory. Downstream loss samples reproduce the hazard posterior rather than using only a median map.

The consistency test passes when the common contract transports metadata and uncertainty while the peril modules remain physically distinct. It fails if a universal severity band becomes the modelling engine.

## 41. Operational example report

A synthetic flood bulletin-support report might say: “Issued 08:00 EAT for 0–12 hours. Model—not official warning. Inundation probability exceeds 0.7 on specified reaches/cells; conditional depth median and intervals are attached. Upstream gauges are current; one urban drainage sensor has been stale since 06:10. Crowd evidence contains three independent roots and nine reposts. Radar acquisition is pending. Main uncertainty is local drainage/depth. Consult linked KMD/WRA and county products.”

The machine product carries samples and lineage. At 10:00 radar narrows extent but a verified local report adds one pocket. The update note decomposes both changes. A later smoother revises onset earlier; the operational lead-time score remains based on the 08:00 issue.

A drought counterpart reports component trajectories and regime duration, NDMA stage as separate authoritative observation, sparse coverage areas, forecast horizon and recovery uncertainty. Neither report expresses financial loss; Part 4 consumes its posterior.

## 42. Priority model-development experiments

The first experiment compares authoritative-only, crowd-only and fused flood state under complete-event and gauge-removal holdout. It asks whether fusion improves calibration or usable lead time and where crowd evidence is genuinely independent. It reports footprint and depth separately.

The second compares finite HMM, HSMM and continuous/state-space drought models against component baselines. It focuses on persistence, false recovery and transfer between livelihood zones. Institutional drought status is an external/action reference, not a hidden target copied by the model.

The third tests fire detection under daylight, darkness, smoke, dust, glare and network loss, then connects validated detections to a process-informed spread challenger. Detection and perimeter improvements are reported separately; suppression history is retained.

The fourth models locust survey effort and movement. It compares administrative-cell extrapolation with wind/lifecycle particle envelopes and tests withheld survey routes and boundary crossings. Crop loss remains downstream.

The fifth builds a rainfall/susceptibility landslide baseline and tests whether local deformation/report evidence adds value without false spatial precision. It prioritises high-consequence misses and access interruption.

The sixth estimates heat episodes with station/remote-sensing/local context and tests compound outage scenarios. It distinguishes meteorological heat from indoor/health vulnerability. Severe storm tracking is evaluated jointly and separately for rain, wind and hail.

Across all experiments, source opportunity, point-in-time replay, physically plausible stress, calibration and subgroup geography are mandatory. A negative result narrows the architecture productively: it can establish that a simple baseline is the appropriate champion or that new field evidence is needed before modelling.

The experimental record must also state computational and institutional feasibility. A scientifically superior posterior that arrives after the action deadline or depends on data an authorised operator cannot access is not the operational champion. A faster approximation can be preferred if its uncertainty is honest and its decision performance is non-inferior. Likewise, a model suited to retrospective reconstruction may remain valuable for vulnerability research even when it is unsuitable for live warning support. Fitness attaches to task and horizon, not to the model name.

All promotion decisions preserve the baseline output for an agreed comparison period. Operators can see disagreement, and validators can determine whether the challenger improved the cases that mattered or merely redistributed error. Retirement occurs only after rollback, documentation and training are complete.

## 43. Conclusion

Hazard-state intelligence is a disciplined inference problem. It connects source-specific observations to a process-specific state, then separately models occurrence, detection, intensity, footprint, duration and recovery. Transparent baselines anchor performance and continuity; hierarchical and latent-regime challengers add value only when validation proves it.

The shared spine is mathematical, not physical uniformity. Directed catchments, drought duration, fire spread, locust movement, hillslope thresholds and heat fields need different topology and dynamics. Their posterior outputs can nevertheless share version, time, geometry and uncertainty interfaces. Part 4 intersects those outputs with exposure and vulnerability to build financial loss distributions.

## References

[1] Food and Agriculture Organization of the United Nations, “Desert locust frequently asked questions,” accessed Aug. 26, 2026. [Online]. Available: https://www.fao.org/locusts/faqs/en/

[2] Plant Protection and Food Safety Directorate, *Contingency Plan for Management of Desert Locust in Kenya*, 2025. [Online]. Available: https://kilimo.go.ke/wp-content/uploads/2025/03/CONTINGENCY-PLAN-FOR-MANAGEMENT-OF-DESERT-LOCUST-IN-KENYA.pdf

[3] U.S. Geological Survey, “THRESH—Software for tracking rainfall thresholds for landslide and debris-flow occurrence,” accessed Aug. 26, 2026. [Online]. Available: https://www.usgs.gov/publications/thresh-software-tracking-rainfall-thresholds-landslide-and-debris-flow-occurrence-user

[4] E. B. Fox, E. B. Sudderth, M. I. Jordan and A. S. Willsky, “A sticky HDP-HMM with application to speaker diarization,” 2009. [Online]. Available: https://arxiv.org/abs/0905.2592

[5] “A hidden semi-Markov model for rainfall data,” *Journal of Applied Probability*. [Online]. Available: https://www.cambridge.org/core/product/identifier/S0021900200112744/type/journal_article

[6] Kenya Meteorological Department, *State of the Climate Report 2025*, 2026. [Online]. Available: https://meteo.go.ke/documents/3009/State_of_the_Climate_Report_2025.pdf
