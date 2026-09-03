# Exposure, Vulnerability and Actuarial Catastrophe Loss Intelligence

## Abstract

A hazard footprint becomes a financial catastrophe only through exposure, vulnerability, response and financial terms. This paper specifies an actuarial loss-intelligence engine for Kenya's flood, drought, wildfire, locust, rainfall-induced landslide, severe storm and extreme-heat risks. It distinguishes people and household welfare, physical assets, infrastructure services, agriculture and livestock, businesses and supply chains, ecosystems, insured portfolios and public balance sheets. It also separates direct damage, interruption, uninsured loss, insured claim, reserve, fiscal cost, credit deterioration and investment consequence.

The engine consumes posterior hazard fields rather than deterministic polygons, intersects them with point-in-time exposure, applies peril- and class-specific vulnerability distributions and response scenarios, and then applies insurance or other financial terms in a separate layer. Event-loss tables drive annual simulations and occurrence/aggregate exceedance curves. Frequency-severity, heavy-tail and spatial-dependence treatment are explicit. Claims nowcasting and triage update event understanding without turning current information into an automatic tariff, reserve, capital or payout instruction.

Flood and drought illustrate fast physical damage and slow livelihood accumulation. Fire, locust, landslide, storm and heat test spread, mobile crop exposure, local severity and indirect consequence. The architecture supports insured, uninsured and fiscal reconciliation while preserving units, horizons, gross/net bases, valuation time and uncertainty. Avoided-loss estimates are treated as causal evaluations, not differences between successive forecasts.

**Research question.** How should uncertainty-bearing multi-hazard states be translated into reproducible physical, economic, insured, uninsured, fiscal and portfolio loss distributions for distinct institutional users in Kenya?

## 1. The same damaged road is not the same loss

A flood damages a county road, delays commuters, interrupts deliveries and contributes to a motor collision. The engineering repair cost is a direct physical loss. Lost business margin is interruption. Household travel cost is an economic consequence. A covered vehicle repair may become an insured claim after deductible and policy checks. County emergency works and reconstruction affect public expenditure. A lender may observe temporary revenue stress. Adding every figure would double-count shared consequences.

Actuarial loss intelligence begins with definitions and reconciliation, not an algorithm. Every quantity needs:

- peril and event;
- exposure population and version;
- valuation time and price basis;
- unit and currency date;
- horizon and whether event or annual;
- ground-up, gross, ceded or net basis;
- mean, quantile or exceedance probability;
- uncertainty and model/data version;
- accountable user and permitted use.

The engine creates a distribution conditional on evidence. It does not make an accounting entry or adjudicate responsibility.

## 2. Exposure taxonomy

### 2.1 People and households

Exposure includes population by time of day, dwelling, mobility, age-related or functional needs, livelihood, access to services and protective capacity. Individual-level vulnerability data are sensitive and often incomplete. Public products use minimum necessary aggregation; operational rescue can use precise information under authorised controls.

Household loss includes structure and contents damage, temporary accommodation, lost income, health and care costs, asset sales and longer-term livelihood effects. Monetary valuation cannot fully represent mortality, trauma, displacement or cultural loss. These remain separate indicators where monetisation would obscure ethics or evidence.

### 2.2 Buildings and contents

Required fields include geocoded footprint, occupancy, construction, storeys, floor height, roof/wall material, age/condition, replacement value, contents, protective measures and use. Informal structures and addresses create coverage challenges. Proxy attributes from imagery require validation and cannot silently determine individual insurance decisions.

Replacement value differs from market value and sum insured. Price indices and post-catastrophe demand surge need valuation dates. Exposure snapshots preserve additions, removals and corrections.

### 2.3 Infrastructure and public services

Roads, bridges, drainage, water, sanitation, power, telecommunications, health, schools and public buildings are networked service exposures. Asset replacement cost is only one dimension. Service criticality, redundancy, restoration time, dependency and users determine consequence.

A road segment is modelled with hazard intersection and engineering vulnerability, while a network model estimates accessibility and detour. A substation outage can cause heat or business consequence outside the physical footprint. Public exposure has owner and fiscal responsibility fields because county, national, utility or concession balance sheets differ.

### 2.4 Agriculture, livestock and ecosystems

Crop exposure needs crop, area, planting date, phenological stage, expected yield, farm-gate price, irrigation, input cost and harvest timing. Drought, flood, hail, heat and pests have stage-specific effects. Livestock exposure includes species, number, location/mobility, body condition, feed/water dependency and market value. Pastoral herds move, so a static farm centroid is misleading.

Ecosystems provide services—water regulation, forage, carbon, biodiversity, tourism and cultural value. Financial valuation is purpose-specific and should avoid adding overlapping service values. Ecological loss can persist beyond insured or fiscal horizons.

### 2.5 Businesses and supply chains

Fields include location, sector, revenue, gross margin, inventory, critical equipment, workforce, supplier/customer dependencies, insurance, recovery plan and maximum tolerable downtime. Small and informal enterprises are under-represented in administrative sources. Mobile surveys and sectoral models can estimate aggregate exposure with sampling uncertainty.

### 2.6 Insured portfolios

Policy-level exposure includes risk location, coverage, sums insured, limits, deductibles, exclusions, waiting periods, endorsements, inception/expiry, coinsurance, reinstatements and reinsurance attachment. Point-in-time correctness is strict: event time determines applicable contract version. Personally identifiable and commercially sensitive data remain segregated.

### 2.7 Government and county balance sheets

Public exposure includes owned assets, emergency response, social protection, transfers, contingent liabilities, reconstruction responsibilities, revenue loss and state-owned entities. Fiscal loss is not identical to national economic loss. Some household or infrastructure damage creates no immediate legal government liability but may generate policy response.

## 3. Exposure quality and geocoding

Exposure uncertainty can dominate hazard uncertainty. Addresses may map to parcel centroids; rural assets may lack formal addresses; mobile livestock and temporary settlements shift; crop maps can misclassify crop and stage; infrastructure inventories can be stale.

Geocoding stores source, method, precision and confidence. A policy postcode or town name is not converted into a point without an uncertainty geometry. Portfolio aggregation integrates over possible locations:

\[
E[L_i]=\int E[L_i\mid x]p_i(x)\,dx.
\]

Data-quality grades reflect completeness, positional accuracy, valuation freshness and attribute reliability. Missing attributes are imputed through documented distributions, not filled with unexplained averages. Imputation uncertainty propagates to loss.

Exposure normalisation supports historical comparisons. Past event losses are adjusted for inflation, exposure growth, asset mix and policy conditions before vulnerability calibration. Otherwise a recent large loss may reflect more assets rather than a more severe hazard.

## 4. Vulnerability and fragility

Vulnerability maps hazard intensity and exposure characteristics to damage or consequence. A mean damage ratio for asset \(i\) under intensity \(m\) is

\[
MDR_i(m)=E\left[\frac{D_i}{V_i}\mid m,C_i,R_i\right],
\]

where \(C_i\) is class/condition and \(R_i\) protective or response context. The full distribution, including probability of zero and total loss, is preferable to the mean.

### 4.1 Flood vulnerability

Building functions depend on depth, duration, velocity, contamination, floor height, construction and contents. Roads and bridges depend on overtopping, scour, debris and duration. Crops depend on depth, duration, flow, crop and stage. Functions may be empirical, engineering or expert-elicited and require Kenyan calibration.

### 4.2 Drought vulnerability

Drought loss depends on cumulative water deficit, timing, irrigation, soil, seed, crop stage and farm practice. Livestock effects depend on forage, water, mobility, disease and market response. Household consequence is mediated by savings, diversification, social protection and repeated prior shocks. A single vegetation threshold cannot serve every outcome.

### 4.3 Fire vulnerability

Property damage depends on flame/heat, ember exposure, construction, defensible space, access and suppression. Rangeland/ecosystem consequence depends on vegetation type, intensity, season and recovery. Smoke exposure affects health and operations over a different footprint.

### 4.4 Locust/pest vulnerability

Expected crop damage depends on pest density, feeding duration, species/lifecycle, crop type and stage, control timing and yield potential. Reported affected area is not necessarily lost production. Vulnerability functions incorporate control and replanting scenarios.

### 4.5 Landslide vulnerability

Impact depends on runout depth/velocity/volume, direct intersection, construction, occupancy and warning. Infrastructure can fail through burial, undermining or blockage. Mortality models are ethically sensitive and highly uncertain; life-safety decisions should not wait for monetised loss.

### 4.6 Storm and heat vulnerability

Wind/hail damage depends on roof, cladding, openings, crop and asset condition. Heat consequence depends on temperature/humidity/persistence, indoor environment, work, age/health, cooling and power. Productivity, health and equipment failures have distinct functions.

### 4.7 Function uncertainty

For a damage ratio \(R\in[0,1]\), a beta, zero/one-inflated beta or ordinal damage-state model can represent variability:

\[
R_i\mid m,C_i\sim \operatorname{Beta}(\alpha(m,C_i),\beta(m,C_i)).
\]

Structural uncertainty is represented by alternative curve sets and weights. Extrapolation beyond observed intensity is a tail assumption disclosed to users.

## 5. Event loss calculation

For event \(e\), posterior hazard sample \(b\), exposure \(i\) and peril \(h\):

\[
L^{(b)}_{e}=\sum_i V_{i,t}\,R^{(b)}_{i,e,h}+BI^{(b)}_{i,e}+C^{(b)}_{i,e},
\]

where \(V\) is exposed value, \(R\) damage ratio, \(BI\) business interruption and \(C\) separately defined consequence. Samples jointly draw footprint, intensity, location, vulnerability and response. Shared random effects preserve spatial correlation.

The event-loss table records event, location, hazard state, exposure, damage state, ground-up loss and uncertainty. It remains at appropriate granularity for audit, then aggregates by county, sector, portfolio or financing layer under privacy controls.

An illustrative building example: a synthetic KES 5 million replacement value has a posterior 60% probability of inundation. Conditional damage ratio is logit-normal with median 0.15 and broad interval. Expected physical loss is not simply `5m × 0.60 × 0.15` if occurrence and severity are dependent; simulation draws the joint state. No claim value exists until terms and verified interest are applied.

## 6. Direct, indirect and cascading loss

Direct physical damage occurs at the asset-hazard intersection. Business interruption is a flow over time and normally uses lost contribution rather than gross revenue, plus extra expense and mitigation. Agricultural loss compares attainable yield/value under event and counterfactual, net of saved costs. Public-service disruption measures users and duration before optional monetary valuation.

Indirect economic effects propagate through suppliers, transport, labour, demand and services. Input-output, network, computable general equilibrium or agent models can explore them, but each has assumptions about substitution, prices and recovery. They should not be added mechanically to insured direct loss. Macroeconomic “loss” may include foregone growth or welfare and uses a different horizon.

The consequence graph assigns each node a stock or flow, owner, unit and time. Reconciliation rules prevent a repair invoice and the associated modelled asset damage being counted twice; business revenue and supplier loss are checked for transfer; public transfer is a fiscal outflow but not necessarily an additional national economic loss.

## 7. Frequency-severity and annual loss

Event risk and annual portfolio risk are connected through simulation. For year \(y\), hazard \(h\):

\[
S_{y,h}=\sum_{j=1}^{N_{y,h}}L_{y,h,j},
\]

where count \(N\) is generated conditional on climate/regime and event loss \(L\) includes footprint, exposure and vulnerability dependence. Compound distributions can be evaluated analytically in simple cases, by recursion or through Monte Carlo. Multi-hazard annual loss is not automatically the sum of independent peril simulations; shared climate states and cascades induce dependence.

Frequency models include Poisson baselines, negative binomial for heterogeneity, point processes for time/space clustering and episode models for drought. Severity can use lognormal/gamma bodies with generalised Pareto or other validated tails. Distributions are chosen through calibration, tail plausibility and decision performance, not convenience.

Annual simulation records event sets, not just annual totals. This permits occurrence terms, reinstatements, aggregate deductibles, funding-layer exhaustion and intervention scenarios. Simulation weights may represent current climate, historical climate or future scenarios; the basis is labelled.

## 8. Heavy tails, dependence and accumulation

Catastrophe loss is heavy-tailed because hazard intensity, footprint, exposure concentration and vulnerability can align. Extreme-value theory can model threshold exceedances, but threshold choice and sparse Kenyan data create substantial uncertainty. Process-model ensembles and regional information can inform tails only with transportability review. Cross-disciplinary catastrophe-model guidance emphasises the need to understand model components, uncertainty and intended risk-management use [3]–[5].

Dependence appears at several levels:

- spatially correlated intensity in one event;
- common construction or infrastructure vulnerability;
- multiple policies at one location;
- event clustering within a season;
- compound hazards and shared climate drivers;
- economic inflation and demand surge;
- common reinsurance or public funding constraints.

Copulas, shared latent factors, spatial random fields, event sets and process simulation are alternatives. Linear correlation is inadequate for tail dependence. Diversification credit is tested under extreme scenarios: separated assets can still fail together through a shared power, road, port, market or reinsurer.

Accumulation mapping overlays posterior event footprints with insured values and critical services. Maps display data-quality and location uncertainty. A precise heat map based on town-centroid policies can mislead; uncertain geocodes are distributed probabilistically.

## 9. Exceedance curves and risk measures

For annual aggregate loss \(S_y\), the aggregate exceedance probability is

\[
AEP(x)=P(S_y>x).
\]

For maximum single-event loss \(M_y=\max_jL_{y,j}\), occurrence exceedance probability is

\[
OEP(x)=P(M_y>x).
\]

The event-loss table is sampled into years; losses are sorted to estimate curves. Simulation error is reported, especially at long return periods. A “1-in-100” loss is a quantile under a stated model and horizon, not an event expected exactly once per century.

**Annual average loss (AAL)** is \(E[S_y]\) and supports long-term pricing, risk budgeting and benefit-cost analysis. **Probable maximum loss** is ambiguous unless the quantile, OEP/AEP basis and horizon are specified. **VaR** at \(p\) is the \(p\)-quantile. **TVaR** is expected loss beyond VaR and better reflects tail magnitude but remains model-sensitive. Scenario loss conditions on a named event or assumptions and is not a probability statement unless a probability is separately supported.

Owners differ: underwriting may use AAL and marginal accumulation; reinsurance uses OEP/AEP and layer loss; capital uses regulatory/internal definitions; government uses fiscal layer and liquidity; investors use downtime and cash-flow stress. The platform produces ingredients and governed reports, not universal interpretations.

## 10. Insurance financial terms

Policy terms are applied after ground-up damage:

\[
L_i^{insured}=\min\{\max(L_i^{covered}-d_i,0),\ell_i\}\times c_i,
\]

with deductible \(d\), limit \(\ell\) and coinsurance/share \(c\), before other clauses. Coverage determination also considers peril definition, exclusions, sublimits, waiting periods, valuation, occurrence wording and policy dates. Aggregate and occurrence terms need event definition.

Reinsurance applies treaties in contractual order: quota share, surplus, per-risk excess, catastrophe excess, aggregate protections and reinstatements as applicable. Gross, ceded and net loss distributions are retained. Counterparty credit and timing are separate from ceded technical recovery.

Parametric contracts use an independently defined index and formula. The modelled local loss can assess basis risk but does not replace the trigger. Trigger data source, calculation agent, fallback, correction and dispute terms must be fixed before risk inception.

Kenya's insurance product and market-conduct guidance requires sound product design, actuarial basis, customer treatment and controls [1], [2]. This engine supports that work but cannot authorise a product.

## 11. Claims nowcasting, triage and reserving

During an event, reported claims represent a delayed and selective sample. Let ultimate count \(N^*\), reported count \(N_t\), reporting delay \(G(d\mid x)\) and severity development \(H\). A claims nowcast combines exposure/hazard estimates with reporting models:

\[
E[N^*\mid N_t,H_t,E_t]=N_t+E[N_{unreported}\mid H_t,E_t,G].
\]

Frequency and severity may be modelled separately by claim type, region and reporting channel. Catastrophe conditions change delay: access, network failure, awareness and surge capacity matter. Historical delay curves are not blindly reused.

Triage ranks cases for contact, emergency assistance or inspection using consequence and uncertainty. It does not rank claimants' worth. A location outside a provisional footprint remains eligible for reporting and review. Fraud indicators prompt investigation and due process; they do not generate automatic denial.

A modelled expected insured loss is not automatically a reserve. Case reserves, incurred-but-not-reported estimates, risk adjustment/margin, accounting measurement and solvency capital have separate methods, ownership and standards. The interface delivers ranges and drivers to authorised actuarial and finance functions. Changes are reconciled into new event information, exposure correction, claims emergence, financial-term interpretation and model change.

## 12. Continuous risk estimation versus repricing

The platform may update current-event loss every hour as observations arrive and long-term risk periodically as exposures, vulnerability and climate evidence change. This is continuous risk estimation. Contractual pricing, renewal, cancellation and coverage changes occur only under policy, law and approved governance.

During an active catastrophe, model output can support operational staffing, accumulation monitoring and reinsurance notification. It must not enable opportunistic mid-event repricing, cancellation or retroactive restriction. For new or renewed business, pricing evidence uses approved as-of dates, uncertainty and conduct review. Individual community reports are not repurposed secretly.

Portfolio monitoring also distinguishes signal from action. A new hazard estimate may change internal economic exposure while accounting or capital values change only after authorised processes. The event audit stores all versions.

## 13. Insured, uninsured and fiscal reconciliation

For a defined exposure universe:

\[
L^{ground}=L^{insured\ ground}+L^{uninsured\ property}+L^{other\ economic},
\]

but insured payout is ground-up covered loss after terms, and fiscal loss can overlap economic beneficiaries. Reconciliation therefore uses a ledger rather than a single identity.

| Layer | Typical unit/horizon | Key boundary |
|---|---|---|
| physical damage | KES replacement cost, event | asset damage before finance |
| insured loss | KES, event/ultimate | covered interest after terms |
| uninsured loss | KES or welfare indicators, event/recovery | non-covered or underinsured consequence |
| fiscal loss | KES cash/accrual by budget period | government-owned assets, response, transfers, liabilities |
| credit loss | ECL/impairment under separate horizon | borrower default/exposure/recovery model |
| investment loss | cash-flow/value impact by horizon | project/portfolio assumptions |

The protection gap can be reported as uninsured economically insurable loss, affected people without coverage, or difference between modelled need and finance. Each definition is stated. Informal and intangible loss makes a simple insured/total ratio incomplete.

## 14. Historical claims calibration

Claims supply valuable severity, repair, policy and delay evidence but are selected by coverage, underwriting, reporting and settlement. Calibration links claim to event, hazard intensity, exposure attributes, contract terms and development. Closed-without-payment and denied claims are interpreted carefully; they may reflect coverage rather than no physical damage.

Event reconstruction harmonises hazard state and exposure as of event date. Losses are trended to a common price basis; exposure and terms are normalised; demand surge and claim handling changes are considered. Data splits hold out complete events. Vulnerability calibration uses ground-up estimates where possible instead of fitting covered payment directly.

Credibility and hierarchical models combine sparse Kenyan experience with engineering or regional priors. Prior transfer is disclosed and posterior predictive checks examine local fit. Large events receive qualitative review for hidden aggregation or policy changes.

## 15. Avoided loss and value of information

An updated estimate is not an avoided loss. Suppose a flood-loss mean falls after imagery shows a smaller footprint. No physical outcome necessarily changed. Avoided loss requires intervention and counterfactual:

\[
AL(a)=E[L(0)-L(a)\mid X],
\]

where \(L(a)\) and \(L(0)\) are potential outcomes with and without action. The intervention can reduce hazard (pest control), exposure (evacuation of movable assets), vulnerability (temporary barrier), duration (rapid drainage/repair) or financial consequence (timely liquidity).

An evaluation records message delivery, comprehension, decision, action time, coverage, compliance, cost and outcome. Process simulation can estimate physical counterfactuals; statistical designs can compare matched or phased settings. Confounding by indication is central: response is usually strongest where risk is greatest, so naive comparisons may make intervention look harmful.

Value of information includes loss reduction plus operational and financial benefits net of cost:

\[
VOI=E[\max_a U(a\mid\mathcal I_{new})]-E[\max_a U(a\mid\mathcal I_{old})]-C_{info}.
\]

Utility can include lives, service, equity and liquidity, not only monetary loss. A claims triage improvement may create customer and expense value without avoiding ground-up damage. These outcomes are labelled separately.

## 16. Canonical loss interface

```text
event_id
hazard_type
valuation_time
scenario_or_posterior_state
exposure_snapshot_version
currency_and_price_date
loss_horizon
gross_physical_loss_distribution
insured_loss_distribution
uninsured_loss_distribution
fiscal_loss_distribution
business_interruption_distribution
mean
quantiles
exceedance_probabilities
uncertainty_components
financial_terms_version
model_version
data_quality_status
permitted_use
```

Mandatory metadata prevent orphan numbers. Quantiles name probability; exceedance probabilities name threshold and OEP/AEP; insured output names gross/ceded/net and policy universe; fiscal output names accounting/cash horizon. Distribution representations may be samples, parametric families or quantile grids, with conversion error documented.

A downstream credit or investment system references the loss interface and adds its own borrower/project model. It must not rename physical expected loss as expected credit loss.

## 17. Hazard-specific synthetic event-loss examples

The examples are architectural demonstrations with synthetic inputs.

### 17.1 Flooded commercial corridor

A posterior flood field contains joint depth and duration across a road-linked commercial zone. Building, contents and road functions generate ground-up samples. Business interruption uses access and restoration scenarios. Policy terms produce insured samples; county-owned road cost and emergency works produce fiscal samples. The outputs share event identity but are not summed into one “total” without reconciliation.

The provisional footprint misses an insured premise that later provides verified water marks. The event posterior and exposure intersection are corrected; the claim is not rejected because the earlier polygon was wrong. The change log attributes estimate movement to new hazard evidence.

### 17.2 Multi-season drought

Crop yield loss is modelled by crop/stage and water deficit; livestock loss includes mortality, body condition and distressed-sale scenarios; household welfare indicators remain alongside money. An index insurance trigger is calculated separately from loss. A payout can occur with low farm loss or fail with high farm loss; both are basis-risk outcomes.

Annual aggregation considers consecutive-season dependence. The model avoids counting asset sale proceeds as reduced loss without considering depletion of future productive assets.

### 17.3 Rangeland fire

Fire perimeter samples intersect grazing, ecological service, structures and a power line. Direct insured property, suppression cost, smoke-related interruption and ecosystem recovery use different footprints/horizons. Prior drought is a hazard driver and vulnerability context, not a second claim automatically added.

### 17.4 Locust infestation

Movement and density samples intersect crop maps by phenological stage. Control scenarios change feeding duration and density. Yield loss is valued at a documented price basis net of saved harvest cost; food-security consequence is reported separately. Survey uncertainty dominates cells with unverified sightings.

### 17.5 Landslide and access loss

Runout samples produce a bimodal outcome: no direct road intersection versus severe blockage. Expected loss alone hides this. The product reports probability of blockage, repair distribution and isolation duration scenario. A clinic's access consequence is not valued as physical clinic damage.

### 17.6 Heat, storm and outage

Heat productivity, health-service demand and equipment stress overlap with storm-driven power outage. A consequence graph prevents counting the same shutdown twice. Parametric heat coverage, if any, follows its trigger; employer or public-health decisions use separate thresholds.

## 18. Validation and independent actuarial review

### 18.1 Component validation

Exposure is checked against field samples, imagery, inventories and financial totals. Hazard-to-damage functions are validated by peril/class/intensity. Policy calculators are tested against contract examples. Claims delay and severity are back-tested by event and development age. Reinsurance calculations use independent treaty test cases.

### 18.2 End-to-end validation

Complete events are held out. Predicted event loss distributions are compared with developed ground-up and insured outcomes, allowing observation and coverage uncertainty. Metrics include bias, mean absolute error, continuous ranked probability score, quantile coverage and calibration by peril, geography and exposure class. Tail results use exceedance and stress diagnostics.

Aggregate accuracy is insufficient. Overprediction in urban formal assets can offset underprediction of rural livelihood loss. Validation therefore includes distribution and equity views and acknowledges where truth is not measurable.

### 18.3 Sensitivity and stress

Sensitivity tests hazard footprint, vulnerability curves, location, values, demand surge, reporting delay, tail distribution, dependence, climate weights and terms. Stress cases include simultaneous basin flood, repeated drought, compound heat/fire/power, locust movement during crop sensitivity and infrastructure-network failure. Outputs identify the assumptions driving decisions.

### 18.4 Governance

The actuarial model owner is distinct from independent validator and financial decision owner. Material changes have documented rationale, validation and approval. A champion remains available for rollback. Expert adjustments are versioned with effect and sunset date. Model limitations accompany every product.

Professional review assesses whether methods, data, assumptions, uncertainty and communication are fit for purpose. It does not certify the physical hazard model outside reviewer competence; interdisciplinary sign-off is required.

## 19. Why the outputs are not interchangeable

An event mean estimates the centre of a conditional distribution; an AAL averages annual simulations; an OEP quantile describes maximum event loss; an AEP quantile describes annual aggregate; a case reserve estimates a claim; an IBNR estimate addresses unreported claims; regulatory capital follows prescribed/approved risk measures; a parametric payout follows a formula; an accounting entry follows standards and governance. Similar units do not create equivalence.

A simple handoff rule applies: each output must name the decision it informs and the transformation still required. If an executive dashboard shows “KES 10 billion,” it must say whether this is current-event expected ground-up damage, an upper quantile, insured gross loss, fiscal need or something else. Undefined catastrophe numbers are rejected at the interface.

## 20. Limitations

Kenyan exposure and claims data may be fragmented, non-geocoded or commercially restricted. Informal assets and livelihoods are undercounted. Engineering curves can lack local evidence. Catastrophe tails and compound events are sparse. Indirect economic models are assumption-heavy. Climate, urbanisation, asset values and construction change. Insurance coverage is selective. Government response can be discretionary.

Accordingly, loss ranges may be broad and model-form uncertainty material. The engine does not monetise every consequence, does not substitute for field assessment, and does not determine claim liability, reserve, capital, credit status or investment approval. It supports those owners with reproducible evidence.

## 21. Exposure data model and stewardship protocol

The exposure store uses effective-from/effective-to and knowledge-time versioning. A building record separates geometry, use, construction, value and insurance interest because each can change independently. Infrastructure separates physical component from service node and owner. Agricultural records separate field geometry, crop season/stage and farmer/financial interest. Portfolio records link to exposure through governed pseudonymous keys.

Each attribute carries source, observation date, method, unit, quality grade and permitted use. A roof material inferred by imagery is stored as a probability vector with model/version, not as surveyed fact. Replacement values state valuation method and index. Missingness categories distinguish not collected, unknown, not applicable, withheld and failed join.

Stewards reconcile portfolio control totals, geospatial counts and sampled field truth. Duplicate buildings/policies use entity resolution while retaining uncertainty. Public infrastructure inventories are reconciled with operator records and condition inspections. Crop maps are refreshed by season. Mobile herds use trajectories or livelihood-zone distributions rather than false static points.

Exposure change logs support event reconstruction. If a building geometry is corrected after flood, the loss run can show operational estimate and restated estimate. No correction silently changes an earlier decision record.

## 22. Vulnerability development protocol

### 22.1 Evidence hierarchy

Vulnerability evidence combines Kenyan claims/assessments, engineering studies, field surveys, process/crop models, regional evidence and expert elicitation. Sources are not pooled without matching intensity definition, construction/crop class, valuation and selection. Foreign curves become priors or scenarios, not local fact.

### 22.2 Statistical formulation

A hurdle model separates no damage from positive ratio:

\[
P(R_i>0)=\operatorname{logit}^{-1}(f_h(m_i,C_i)),
\quad
R_i\mid R_i>0\sim \operatorname{Beta}(\alpha_i,\beta_i),
\]

with monotonicity imposed where physically justified. Hierarchical effects pool related classes/regions. Censoring by deductibles and limits is handled rather than fitting paid loss as ground-up. Measurement error in intensity is integrated where material.

### 22.3 Expert elicitation

Experts receive common definitions and synthetic asset/intensity cases. They provide quantiles, not only means, and explain mechanisms. Calibration questions and aggregation reduce overconfidence. Disagreement becomes model-form alternatives. Independent review checks incentives and representativeness.

### 22.4 Updating

After events, claims and surveys update curve posteriors only after exposure/terms normalisation and event holdout evaluation. A single event does not rewrite long-term tails. Change notes show affected portfolios and validation. Champion curves remain for comparison and rollback.

## 23. Event-loss table construction in detail

For each stochastic event sample, the engine performs:

1. sample/retain correlated hazard intensity and footprint;
2. select point-in-time exposure and integrate location uncertainty;
3. sample exposure attributes/imputed values;
4. map each exposure to vulnerability class;
5. sample correlated damage states and protection/intervention effect;
6. calculate repair/replacement and time-dependent consequence;
7. reconcile service/supply-chain cascades;
8. apply policy and reinsurance terms in separate calculators;
9. aggregate by required view with privacy thresholds;
10. store uncertainty attribution and reproducibility metadata.

Shared damage random effects can represent common workmanship/material or demand surge. Correlation is not added after aggregation; it arises in joint sampling. The table retains zero-loss exposed assets for calibration and policy terms. Unexposed assets need not be expanded row-wise but their totals remain in denominators.

## 24. Detailed peril-loss mechanisms

### 24.1 Flood

Depth-duration-velocity samples map to building and contents ratios. Floor elevation shifts effective depth. Contamination creates cleaning/replacement scenarios. Motor damage depends on vehicle presence and immersion. Road/bridge models separate surface, embankment, scour and closure. Business interruption follows physical/access/service restoration, capped by recovery assumptions.

Uncertainty tests terrain, drainage and geocoding. A deterministic footprint is avoided near boundary. Demand surge affects repair price and time. Mortality/displacement indicators are reported with dedicated models and ethical review rather than casually monetised.

### 24.2 Drought

Crop production counterfactual uses weather/yield model and stage. Loss is attainable minus event yield times price, net of saved/extra costs. Price effects can offset producer physical loss while worsening consumer welfare; they are not combined blindly. Livestock models track mortality, weight/condition, reproduction and distressed sale. Rebuilding herd/livelihood extends beyond season.

Household loss/welfare uses income, food, water time/cost and coping indicators with sampling uncertainty. Insurance loss applies index/indemnity separately. Repeated seasons require state dependence; resilience depletion increases later vulnerability.

### 24.3 Fire

Property models use flame/heat/ember and smoke/soot components. Firefighting/suppression is public/owner expense and affects perimeter. Business/service interruption can extend through evacuation and utility failure. Rangeland/ecological recovery uses area/intensity/vegetation and horizon. Carbon, biodiversity and forage values overlap and are disclosed separately.

### 24.4 Locust and pests

Density, feeding duration and stage produce crop damage/yield samples. Movement couples farm losses spatially. Control cost and environmental externality are separate. Replanting reduces ultimate yield loss but adds cost and depends on remaining season. Market/food-security consequence is scenario-based.

### 24.5 Landslide

Direct intersection can create near-binary destruction, making expected loss insufficient. Runout and burial depth drive fragility. Road blockage generates restoration and accessibility distributions; alternate routes reduce consequence. River blockage introduces secondary flood scenario without double counting the slide.

### 24.6 Storm and heat

Wind/hail/rain drive roofs, crops and equipment. Heat affects health, work productivity, livestock/crops and equipment/service through separate exposure clocks. Indoor and outage conditions change vulnerability. Compound simulation shares drivers and reconciles downtime.

## 25. Claim and loss-development diagnostics

Claims triangles remain useful but catastrophe cohorts may violate stable development. Diagnostics stratify notification, inspection, payment and closure delay; reopenings; large losses; coverage disputes; access/network outages; channel and event phase. Calendar effects include inflation, repair capacity and operational change.

Nowcast evaluation freezes each historical knowledge date and predicts ultimate count/severity. It reports interval coverage and bias by peril/location/claim type. The hazard-based prior is strongest early; claims evidence gains weight as reporting matures. Credibility weights are learned or governed, not arbitrary.

Reserve handoff includes reconciliation waterfall: prior estimate, new event footprint, exposure correction, new reports, case development, term interpretation, inflation and model change. Finance/actuarial owners approve booked implications. The platform retains its technical estimate even when the booked value differs for legitimate reasons.

## 26. Tail and dependence validation protocol

Tail validation combines threshold plots, stability, mean excess, return-level uncertainty, posterior predictive extremes and process plausibility. Alternative thresholds/families form model uncertainty. Apparent tail fit with few events is not presented as precise long return-period capital.

Spatial dependence is checked against historical joint intensity/loss and process simulation. Event sets preserve basin/storm/fire/locust footprint. Cross-hazard dependence uses shared regimes/scenarios where evidence is weak. Reinsurance and fiscal layer results are stress-tested under stronger tail dependence than the central model.

Simulation convergence is measured for AAL and quantiles; tail effective sample size is reported. Variance-reduction or importance sampling is validated for unbiased weighting. Numerical caps are disclosed and tested above decision layers.

## 27. Model-output reconciliation example

Assume a synthetic flood produces ground-up median KES 8.0 billion and 90% interval KES 3–20 billion for a defined exposure universe. Insured gross median might be KES 2.1 billion after coverage and terms; reinsurance recovery KES 0.7 billion; insurer net KES 1.4 billion. Uninsured property/livelihood estimate may be KES 4.5 billion, while county/national fiscal cash need over six months is KES 1.2 billion.

These numbers can overlap: public grants may compensate uninsured households; fiscal reconstruction may repair assets included in ground-up; reinsurance is a financing recovery, not reduced physical damage. The reconciliation ledger tags each flow and stock. Summing `8.0 + 2.1 + 0.7 + 4.5 + 1.2` would be meaningless.

If later imagery changes ground-up median to KES 7.2 billion, the KES 0.8 billion difference is estimate revision. If timely road closure prevented an independently estimated KES 0.1–0.3 billion of motor damage, that avoided-loss range uses a separate counterfactual record. If accounting books KES 1.6 billion reserve, it records its standards/judgement and links to, but does not overwrite, the event distribution.

## 28. Actuarial product acceptance checklist

A loss product is accepted only if event/peril, exposure universe, valuation time, horizon, currency/price date, gross/net basis, financial terms, statistic, uncertainty, data quality, model version, owner and permitted use are visible. Event and annual quantities are clearly separated. Samples preserve dependence and tails. Reconciliation prevents double counting.

It fails if policy selection masquerades as population loss; a mean is called maximum; return period is unqualified; claims payment is fitted as ground-up without terms/censoring; geocoding uncertainty is hidden; reinsurance is treated as damage reduction; expected loss becomes reserve/capital/credit/payout automatically; or avoided loss lacks action/counterfactual.

## 29. Annual simulation architecture

An annual catalogue simulation is generated in layers so that users can audit where dependence enters.

### 29.1 Year and regime

Each simulation year draws climate/environmental regime variables appropriate to the basis: historical-current, conditioned seasonal outlook or future scenario. The basis and weights are fixed. Common variables can drive multiple hazards, for example rainfall/temperature anomalies, but the model does not force dependence unsupported by process or evidence.

### 29.2 Event generation

Conditional occurrence models generate floods, fires, pest movements, landslides and storms. Drought and heat may be episode states with onset/duration rather than independent daily events. Event clusters and secondary events retain parent identifiers. Policy event-definition remains separate from scientific parentage.

### 29.3 Hazard and intervention

For every event, the simulator draws footprint/intensity/duration posterior or conditional ensemble and applies baseline intervention assumptions. Alternative response scenarios reuse common random draws so avoided-loss comparisons have lower simulation noise. Failed source networks affect forecast/operational scenarios but not necessarily the true physical catalogue; these layers are distinguished.

### 29.4 Exposure and loss

The correct exposure projection/snapshot is selected, then vulnerability and financial terms apply. Cross-event repair, exhausted household reserves, crop stage and insurance reinstatements carry state through the year. Annual aggregate therefore captures repeated events rather than summing independent catalogue means.

### 29.5 Output and convergence

The engine stores year, event list, hazard sample, exposure version, damage, financial layers and weights. Convergence plots show AAL and selected OEP/AEP quantiles with Monte Carlo error. Tail estimates that do not converge at the requested return period are not reported as stable numbers; more simulation or a lower supported horizon is required.

## 30. Policy and reinsurance calculation controls

Financial-term code is a separate, versioned rules service with unit tests based on reviewed wording examples. It handles currency, policy dates, insured interest, occurrence aggregation, waiting period, franchise/deductible, limit, sublimit, coinsurance, aggregate term, reinstatement and order of coverage. Ambiguous wording is a referral, not a guessed formula.

Test portfolios include zero loss, below/at/above deductible, multiple coverages, multiple locations, event spanning inception/expiry edge cases, exhaustion, reinstatement and missing terms. Expected results are approved by claims/underwriting/legal or treaty specialists. Round-off and currency conversion are explicit.

Reinsurance tests cover occurrence grouping, hours clauses where applicable, attachment/exhaustion, aggregate, franchise, reinstatement premium and allocation. The platform reports technical recoverable under assumed interpretation; authorised finance/reinsurance functions confirm collectability and accounting. Treaty confidentiality limits views.

## 31. Uninsured and livelihood loss protocol

Uninsured loss cannot be computed as `economic loss minus insured claims` unless populations, valuations and timing align. The uninsured study defines target population and sampling frame. Household surveys, building/agriculture mapping, public assessments and market data are combined with survey weights and nonresponse models. Insurance status/adequacy is sampled or linked only with consent/authority.

For informal assets without market replacement records, valuation uses transparent quantity-cost schedules and uncertainty. Livelihood effects can be reported in natural units—livestock units, yield tonnes, income-days, water travel hours, displaced household-days—alongside monetary scenarios. Food insecurity and mortality are never treated as simple unpriced zeros.

Protection-gap reports show multiple denominators: affected households without any cover; ground-up insurable property not covered; insured sums relative to replacement; rapid liquidity relative to need; and public funding gap. Each supports a different policy question. Spatial maps include observation/exposure-quality shading so data poverty is not interpreted as protection.

## 32. Fiscal-loss protocol

Fiscal exposure is classified by direct government asset ownership, response cost, statutory/contractual liability, policy-contingent assistance, transfers to counties/entities and revenue impact. The valuation horizon differentiates immediate cash need, annual budget and multi-year reconstruction. Economic loss borne by citizens is not automatically a government liability, though it can create an explicit scenario.

For every loss item, the ledger records responsible level/entity, appropriation/fund source, timing, whether new expenditure or reallocation, transfer versus resource cost, and overlap with insurance/credit/grant. Financing flows are applied after fiscal need. Borrowing provides cash and creates liability; insurance recovery finances but does not reduce physical public damage.

The fiscal engine supports layer exhaustion and liquidity-gap curves. It does not issue appropriation. Discretionary assistance is modelled as policy scenarios and stress-tested for political/equity implications rather than assumed from past averages.

## 33. Business interruption and network consequence

For firm \(i\), a simplified interruption loss is

\[
BI_i=\int_0^{T_i}\left[GM_i(t)(1-r_i(t))+EE_i(t)-SC_i(t)\right]dt,
\]

where gross margin \(GM\), residual production fraction \(r\), extra expense \(EE\), and saved cost \(SC\) vary through restoration. Revenue is not automatically loss. Recovery paths depend on physical repair, access, utilities, workforce, suppliers, demand and mitigation.

Network models identify critical nodes and alternate routes. A component outage becomes service loss only if redundancy/operation cannot compensate. Consequence is allocated carefully to avoid summing every downstream firm's gross sales. Input-output models are scenario tools with substitution assumptions. Insured business-interruption follows coverage/waiting/indemnity-period terms separately.

Infrastructure downtime outputs include probability of service interruption, users affected, restoration distribution and critical-function threshold. These can matter more than asset repair mean for government and investment.

## 34. Mortality, health and displacement boundaries

Life-safety metrics are produced for action without requiring monetisation. Mortality/injury models use exposure, intensity, warning, mobility, building and response, with wide uncertainty and ethical review. They must not determine whose rescue is valuable. Health records are aggregated/protected. Heat and smoke syndromic signals require clinical/public-health interpretation.

Displacement records people/households, voluntary/forced status where known, duration, destination capacity and return constraints. Shelter/support cost is fiscal/economic; lost home/contents is physical; wellbeing and protection risks remain separate. Double counting is controlled through person/event identifiers under privacy-preserving governance.

Where benefit-cost analysis monetises mortality/morbidity risk, the chosen public methodology, ethical limits and sensitivity are explicit. The catastrophe platform does not create a bespoke value of life to make a project attractive.

## 35. Model-change impact assessment

Every material change is run on a fixed reference portfolio/event set and recent events. The report decomposes effect by hazard, region, exposure class, financial layer, mean and tail. It compares old/new calibration and explains whether change arises from data, hazard, vulnerability, dependence, terms or simulation.

Downstream impacts include pricing indication, accumulation, reinsurance, reserve support, fiscal gap and resilience appraisal, but each owner decides adoption. Parallel run and rollback period are defined. A change with better aggregate fit but destabilising tail or underserved-area results can be limited or rejected.

Historic reports remain tied to their original model unless restated with a new identifier. Restatement is not presented as what was known at the time.

## 36. Communication examples

Good: “As of 14:00 EAT, the posterior median gross insured flood loss for portfolio version P17 is KES X, with 10th–90th percentiles Y–Z. The largest uncertainty is unverified urban depth; this is an operational estimate, not a booked reserve.”

Poor: “AI says losses are KES X.”

Good: “The current-climate AEP 1% quantile under model M4 and 2026 exposure is KES X gross of reinsurance; simulation and model-form uncertainty are shown separately.”

Poor: “The 100-year maximum loss is KES X.”

Good: “The intervention scenario reduces modelled AAL by KES X–Y relative to the maintained-without-project baseline; this expected benefit is uncertain and is not project cash flow.”

Poor: “The project guarantees KES X annual savings.”

## 37. Independent replication package

Subject to privacy and commercial restrictions, reviewers receive data dictionaries and aggregate/test data, event/exposure/terms versions, model specification and code, vulnerability sources, priors, random-seed policy, event samples or reproducible generator, validation folds, metrics, sensitivity and change log. Confidential data can be accessed in a controlled environment; restrictions and their effect on validation are disclosed.

Replication requires reproducing representative event means/quantiles, annual AAL/OEP/AEP within Monte Carlo tolerance, financial-term test cases and reconciliation. Independent code or alternative implementation is used for critical term/tail checks. Findings enter the validation log and high-severity errors block use.

## 38. Uncertainty attribution and decision sensitivity

Loss uncertainty is decomposed experimentally by fixing or resampling components. One analysis fixes hazard and varies exposure location/value; another fixes exposure and varies vulnerability; others vary terms, dependence, reporting and tail. Because components interact, Shapley-style variance allocation or ordered sensitivity can supplement simple one-at-a-time results. The method and residual interaction are reported.

Decision sensitivity asks whether uncertainty changes action. If all plausible loss samples exhaust a working layer, precise mean refinement may add little. If reinsurance attachment lies inside the interval, hazard/exposure improvement can materially affect operations. If a resilience project benefit-cost conclusion reverses under vulnerability or discount assumptions, more evidence or robust design is needed.

The product highlights dominant reducible uncertainty and the cost/time of reducing it. A field depth survey, improved geocoding, contract data cleanup or claims sample may be more valuable than a more complex hazard model. Irreducible and scenario uncertainty remain visible.

## 39. Data and model adequacy by use

Situational event estimation can tolerate aggregate exposure and wide ranges. Portfolio accumulation needs reliable locations and sums but may not need household attributes. Pricing requires representative long-term hazard/loss and approved classes. Claim-specific automation requires much stronger asset, damage, terms and due-process evidence. Fiscal planning needs public/household exposure and policy scenarios. Resilience appraisal needs counterfactual intervention mechanics.

The adequacy matrix rates data/model against use; it never labels a model simply “validated.” An output can be approved for claims staffing and prohibited for denial; acceptable for county scenario planning and insufficient for a bond metric. Materiality and reversibility influence threshold.

## 40. Synthetic portfolio case study

A fictional portfolio contains 10,000 property risks, 2,000 motor risks and 300 small-business interruption covers across several Kenyan settings. Twenty percent of property locations are parcel-grade, half are building/road-level and the rest town/area-level. Replacement values have varying freshness. The case is illustrative and supplies no market result.

A flood posterior is sampled 20,000 times. Location uncertainty is integrated; town-centroid risks are distributed using an approved exposure prior. Depth-duration vulnerability draws share construction-class effects. Policy terms apply by event-time version. Business interruption follows access/power/repair scenarios and waiting periods. Reinsurance is calculated separately.

The report might show a broad loss interval dominated early by depth and poor locations. After radar and verified depth arrive, hazard uncertainty falls; after policy-location cleanup, exposure uncertainty falls. Claims reports later shift severity/reporting uncertainty. A reconciliation waterfall attributes each revision.

Operational decisions differ: claims prepares staffing from the report-count distribution; reinsurance reviews notification thresholds; finance develops but does not copy the model into reserve; underwriters make no mid-event change. After development, the event enters vulnerability calibration as a held-out validation event first. Poor rural geocoding prompts data improvement, not automatic premium penalty.

## 41. Drought livelihood and insurance case study

A fictional livelihood zone contains rain-fed crop households, pastoral herds, traders and public water assets. The drought posterior includes rainfall, vegetation, water access and duration. Crop-stage/yield and herd-condition models produce production and asset-change distributions. Household survey weights estimate income/water/food consequence. An index insurance contract uses its fixed vegetation/rainfall formula.

The analysis reports physical production loss, household welfare indicators, indexed payout, indemnity if applicable, public emergency cost and financing gap separately. Some cells experience high loss without trigger and others payout with lower loss. Basis maps inform product review and complementary targeting, but do not retrospectively change claims.

Repeated-season simulation carries reduced herd/assets and debt, exposing nonlinear vulnerability. A water/anticipatory intervention scenario changes mortality and access assumptions; avoided loss requires delivery and comparison evidence. Improved model estimation alone is not credited.

## 42. Reconciliation control totals

At each aggregation, automated controls compare exposure count/value before/after join; event loss sum across locations to portfolio; coverage transformations; gross to ceded/net; reported/IBNR to ultimate model; fiscal need to financing sources/gap; and scenario before/after intervention. Differences have named reconciling items.

Rounding occurs only for presentation. Currency conversion uses rate/date/source. Privacy suppression in reports preserves aggregate control totals while marking hidden cells. No negative loss appears except explicitly modelled recoveries/offsets in a financing ledger.

## 43. Actuarial governance report

The periodic report states purpose and users, model inventory/change, data quality, performance by hazard/class/geography, event experience, assumption/tail/dependence, uncertainty, financial impacts, limitations, overrides, incidents and actions. It distinguishes management recommendation from technical result. Independent validation findings and disagreements are included.

The accountable actuary or model owner does not certify disciplines outside competence; hazard, engineering, legal, claims, finance and community specialists own their components. Sign-off means fit for the named use at that time, not truth or approval for every downstream decision.

## 44. Event loss report specification

The first page states event/hazard, issue and valuation time, evidence cutoff, exposure/financial-term version, currency basis, scope and intended users. It gives mean and selected quantiles for ground-up, insured gross and other approved layers, never a single unlabelled total. It identifies the dominant uncertainty, degraded sources and change since previous issue.

The hazard section shows probabilistic footprint, conditional intensity/duration and official/model status. The exposure section shows counts/values and data-quality grades. The vulnerability section names curve sets and material assumptions. The loss section shows distributions and spatial/sector contributions with privacy aggregation. The finance section applies terms and reconciliation; the action section lists allowed operational uses and required owner.

Appendices contain methodology, samples or distribution representation, sensitivity, event-loss table controls, policy/reinsurance tests, validation domain, limitations and source/model versions. A revision note attributes movement; a restatement is separate from the operational series.

## 45. Quality-control suite

Pre-run controls check source freshness, hazard sample completeness, exposure effective dates, duplicate entities, values/units/currency, term versions and model approvals. Run controls check sample counts, nonnegative/finite values, vulnerability bounds, spatial joins, policy identities, aggregation and convergence. Post-run controls reconcile totals and compare with prior/run expectations.

Reasonableness diagnostics include loss-to-value by class, affected/unaffected exposure, severity distribution, top contributors, geographic discontinuities, insured-to-ground-up and gross/ceded/net. Unexpected results are investigated; they are not manually forced to historical ratios. Overrides are explicit, reasoned and time-limited.

Independent calculators reproduce representative deductibles/limits, event loss and reinsurance. Unit tests cover boundary cases. A production run fails closed or visibly degraded when a required term/source is missing; it does not assume zero deductible, unlimited cover or no loss.

## 46. Portfolio and public data confidentiality

Policy/claim/exposure detail is segregated by institution and purpose. Shared hazard and aggregate loss products use minimum cells/count thresholds and contractual confidentiality. Secure computation or controlled clean-room approaches may support pooled industry/systemic views, but methodology and leakage risk require validation.

Public uninsured/fiscal analyses cannot expose household circumstance. Suppression, noise or aggregation effects are disclosed so totals remain interpretable. Model developers use de-identified/test datasets where possible; access to raw claims is exceptional and logged.

Confidentiality cannot justify unverifiable high-stakes models. Independent reviewers receive controlled access or the limitation blocks the use. Published results separate synthetic, aggregate and empirical evidence.

## 47. Climate-conditioned loss and exposure scenarios

Long-horizon catastrophe loss combines hazard, exposure, vulnerability and adaptation scenarios. The engine does not adjust historical AAL with one climate multiplier. It samples scenario-consistent event regimes/fields and projected exposure/values, then applies vulnerability and adaptation assumptions. Urbanisation and maintenance can dominate local outcomes.

Results are conditional: 2030/2050 under named climate and development/adaptation paths, with current-price or nominal basis. They support stress and robust investment, not precise tariff or accounting values decades ahead. Scenario spread, climate-model/form, downscaling and exposure uncertainty are shown separately.

Near-term current-event estimates do not rewrite climate trend after one catastrophe. Periodic long-term model review incorporates accumulated evidence. A climate-conditioned catalogue and a current operational posterior retain different version/horizon metadata.

## 48. Final reproducibility checklist

An independent analyst must be able to identify event catalogue and evidence cutoff, exposure/terms, intensity-vulnerability mapping, financial transformations, dependence/tail, random samples/weights, currency, aggregation and all adjustments. Reported statistics must reproduce within documented numerical tolerance. Every external/local curve and parameter has provenance and applicability.

If any transformation cannot be traced, the output remains exploratory. Reproducibility is necessary but not sufficient: scientific, actuarial, conduct and institutional fitness still require review.

## 49. Visual synopsis

```{.mermaid #fig-4-1 alt="Hazard exposure vulnerability and loss chain"}
flowchart LR
  H[Posterior hazard samples] --> E[Point-in-time exposure snapshot]
  E --> V[Peril and class vulnerability distributions]
  V --> G[Ground-up physical and interruption loss]
  G --> T[Coverage and policy terms]
  T --> I[Insured gross loss]
  I --> R[Reinsurance terms]
  R --> N[Insurer net loss]
  G --> U[Uninsured and welfare consequences]
  G --> F[Fiscal consequence ledger]
```

**Figure 4.1 — Hazard–exposure–vulnerability–loss chain.** Financial terms apply after ground-up physical consequence.

```{.mermaid #fig-4-2 alt="Event loss table and exceedance curve construction"}
flowchart LR
  ELT[Event loss table with joint hazard and loss samples] --> YEARS[Simulated years and event sets]
  YEARS --> MAX[Maximum event in each year]
  YEARS --> SUM[Aggregate loss in each year]
  MAX --> OEP[Occurrence exceedance probability curve]
  SUM --> AEP[Aggregate exceedance probability curve]
  SUM --> AAL[Annual average loss]
  YEARS --> CHECK[Convergence, tail and dependence diagnostics]
```

**Figure 4.2 — Event-loss table and exceedance-curve construction.** OEP uses annual maximum event; AEP uses annual aggregate.

```{.mermaid #fig-4-3 alt="Spatial catastrophe accumulation concept"}
flowchart TB
  FP[Probabilistic event footprint] --> JOIN[Joint spatial intersection]
  LOC[Uncertain asset locations] --> JOIN
  VAL[Time-versioned values and sums insured] --> JOIN
  DEP[Shared vulnerability and network dependencies] --> JOIN
  JOIN --> ACC[Portfolio accumulation distribution]
  ACC --> MAP[Quality-shaded spatial view]
  ACC --> TAIL[Tail and concentration metrics]
```

**Figure 4.3 — Spatial accumulation concept.** Location and shared-dependency uncertainty remain in the portfolio view.

```{.mermaid #fig-4-4 alt="Continuous risk estimation timeline"}
timeline
  title Continuous estimation with fixed contractual authority
  Before event : Approved long-term model and policy terms
  Forecast : Portfolio preparedness and accumulation
  Event nowcast : Revised footprint and loss distribution
                : No retrospective contract change
  Claim emergence : Claims owner and reserving process
  Ultimate reconstruction : Developed event and loss evidence
  Model review : Prospective recalibration and approval
```

**Figure 4.4 — Continuous risk-estimation timeline.** Updating event evidence is not continuous contractual repricing.

```{.mermaid #fig-4-5 alt="Insured uninsured and fiscal loss reconciliation"}
flowchart LR
  P[Physical and economic damage] --> C[Covered ground-up loss]
  P --> U[Uninsured and welfare loss]
  P --> F[Fiscal responsibility and cash need]
  C --> I[Insured gross after policy terms]
  I --> CEDED[Ceded recovery]
  I --> NET[Insurer net]
  F --> FIN[Budget, reserves, credit and transfer]
  U -. assistance can overlap .-> F
  CEDED -. financing, not damage reduction .-> P
```

**Figure 4.5 — Insured, uninsured and fiscal reconciliation.** Financing flows and overlapping responsibilities are not additive damage.

## 50. From event experience to long-term actuarial assumption

A new catastrophe provides evidence but should not mechanically reset pricing or capital. The review first distinguishes observation improvement from physical extremity, exposure growth, vulnerability, repair inflation, coverage/terms, claims practice and chance. The event is normalised and compared with the stochastic catalogue and vulnerability predictive distribution.

If the event lies outside calibration, the team tests whether the cause is missing peril mechanism, tail/dependence, land-use/climate trend, exposure error or reporting. One event can expose structural flaw but rarely estimates a new return period reliably. Process science, wider regional evidence and successive events inform a governed model change with uncertainty.

Tariff indication then uses the approved long-term basis, expense, reinsurance, capital, product and conduct—not the event nowcast. Renewal changes use prospective approved data and communication. Existing event claims retain their contract. Capital and accounting owners apply their standards. The model-change impact report shows old/new portfolio and customer distribution.

Historical claims incorporated for vulnerability are separated into training and future event validation. A major event can remain a holdout until a predeclared validation is complete, preventing the model from claiming success after fitting the result. Only then may a later version use it, with performance assessed on other events or prospective evidence.

This discipline allows learning without volatility theatre. A severe event is neither dismissed as an outlier nor treated as conclusive proof of a new climate regime. The actuarial response is proportional to evidence, transparent about model-form/tail uncertainty and bounded by contract and institutional authority.

## 51. Minimum useful outputs under data scarcity

Where exposure or vulnerability is weak, the system can still report probabilistic hazard footprint, exposure counts/ranges, affected-service indicators and scenario loss bands. It may aggregate geography, use engineering ranges and flag dominant unknowns. Claims triage can remain human and inclusive. A detailed property loss or long-return-period curve may be withheld.

Data scarcity is itself an output for investment: geocoding, valuation, field survey, gauge or claims normalisation can have measurable information value. The model should recommend evidence collection only where it can change a named decision. It never converts lack of data into zero loss or unjustified risk loading.

A minimum product still preserves reconciliation. It states whether counts/values cover insured assets, all mapped buildings, sampled households or public assets; gives natural-unit impacts where money is weak; and refuses to add incomparable layers. It can show scenario bands rather than probabilistic return periods. As evidence improves, the same identifiers and versions support refinement without pretending earlier estimates were more precise. This staged honesty is preferable to a complete-looking catastrophe model whose detail exceeds the observations.

The decision owner is told what additional evidence would make the next refinement defensible and whether it could arrive within the decision window. Where it cannot, the appropriate response is a conservative scenario, manual review or no quantitative use—not an undocumented assumption.

Every such limitation is machine-readable in the loss interface and repeated in the human report, so a downstream system cannot silently promote an exploratory range into a contractual or accounting number.

## 52. Conclusion

Actuarial catastrophe intelligence is the controlled translation of hazard, exposure and vulnerability into distributions whose meaning survives institutional handoff. Its disciplines are point-in-time exposure, peril-specific vulnerability, joint uncertainty, frequency-severity separation, spatial dependence, contractual layering and financial reconciliation.

The system's value lies partly in faster estimates and partly in making differences visible: physical versus insured, event versus annual, expected versus tail, economic versus fiscal and estimate revision versus avoided loss. Part 5 uses these outputs to design bounded insurance, investment, public-finance and resilience-finance decisions.

## References

[1] Insurance Regulatory Authority, *Insurance (Insurance Products) Guidelines, 2022*. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3641/eng%402022-03-29/source

[2] Insurance Regulatory Authority, *Insurance (Market Conduct) Guidelines, 2022*. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3642/eng%402022-03-29

[3] Society of Actuaries, Canadian Institute of Actuaries and Casualty Actuarial Society, *Incorporation of Flood Catastrophe Models into Risk Management Practices*, 2018. [Online]. Available: https://www.soa.org/globalassets/assets/files/resources/research-report/2018/incorporation-flood-catastrophe.pdf

[4] National Association of Insurance Commissioners, “Catastrophe models (property),” accessed Aug. 26, 2026. [Online]. Available: https://content.naic.org/cipr-topics/catastrophe-models-property

[5] International Actuarial Association, *Catastrophe Risk*, 2025. [Online]. Available: https://actuaries.org/app/uploads/2025/10/IAARiskBook_CatastropheRisk_2025_10.pdf
