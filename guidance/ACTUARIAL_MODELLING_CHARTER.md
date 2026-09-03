# Actuarial and Insurtech Product Modelling Charter

**Status:** Reusable project standard  
**Version:** 1.0  
**Effective date:** 26 August 2026  
**Review cycle:** At least annually and after any material legal, regulatory, product, data, model, or accounting change  
**Companion research note:** [Bayesian Credibility and Exposure-Normalised Telematics Relativities Research Note](Bayesian_Credibility_and_Exposure_Normalised_Telematics_Relativities_Research_Note.md)

## 1. Purpose

This charter is the durable institutional memory for future actuarial and Insurtech product work. It preserves the practices developed through the Mwendo Pamoja research while remaining general enough for another motor, mobility, usage-based insurance, embedded-insurance, premium-finance, claims, credit, or portfolio-risk project.

The charter governs more than model construction. An innovative Insurtech product is a connected operating system of customer need, coverage, exposure, pricing, underwriting, data rights, claims, interventions, accounting, capital, reinsurance, technology, and accountable institutions. A statistically impressive model is only one component of that system.

The standing objective is:

> Design products that solve a recognisable customer problem, measure risk on an actuarially coherent basis, use advanced computation only where it adds stable value, preserve the authority of licensed institutions, and generate evidence that a customer, actuary, validator, auditor, investor, and regulator can challenge.

This charter is not legal advice, an actuarial opinion, an accounting policy, a rate filing, or regulatory approval. Applicable Kenyan law, executed contracts, regulator directions, approved institutional policies, and the judgement of authorised professionals prevail.

## 2. How to use this charter

At the beginning of a new project, the team should read this charter and the companion research note before drafting an architecture, writing model code, designing a tariff, or making a financial claim.

Every project should then create five local artefacts:

1. A product and customer-outcome brief.
2. A canonical definitions and notation register derived from Section 19.
3. A source-to-use data register.
4. A claim and evidence ledger.
5. A model, product, and operational validation plan.

The charter may be adopted in a project-level `AGENTS.md` through the following instruction:

```text
Before performing actuarial, Insurtech, insurance-pricing, embedded-finance,
telematics, underwriting, claims, capital, or model-governance work, read
ACTUARIAL_MODELLING_CHARTER.md and its linked research note completely.
Apply their terminology, evidence hierarchy, modelling separation, validation
gates, and narrative standards. Treat innovative formulae as testable candidate
mechanisms until calibrated and approved. Do not silently conflate insurance,
credit, accounting, capital, policy, or market-consistent valuation quantities.
```

Project instructions may add requirements but should not weaken applicable law, customer protection, professional standards, source discipline, or validation controls.

## 3. Governing hierarchy

The following order resolves conflicts:

1. Applicable law, subsidiary legislation, regulator directions, and court decisions.
2. Executed insurance, credit, servicing, data-sharing, financing, and security documents.
3. Approved insurer, lender, actuarial, accounting, risk, security, and product policies.
4. Adopted professional standards and codes.
5. This charter and the project's controlled specifications.
6. Narrative papers, commercial hypotheses, prototypes, and exploratory research notes.

The product should be designed within the Kenyan insurance-product lifecycle. Kenya's Insurance Products Guidelines require attention to customer needs, fair treatment, clear terms, a sound underwriting and actuarial basis, appropriate data or technical justification, capital, a business case, pilot testing, cost-benefit analysis, risk mitigation, implementation milestones, delegated approval, post-implementation review, and actuarial review [1]. Kenya's Market Conduct Guidelines place fair customer treatment within product development, distribution, monitoring, remediation, and institutional culture [2].

The Insurance Act preserves the insurer's legal role, requires premium-rate schedules or manuals for general insurance, permits regulatory requests for the supporting statistics, and governs the receipt of premium [3]. The actuarial function should advise on product design, pricing, reinsurance, technical provisions, data quality, experience analysis, capital, scenario testing, and internal models [4].

Innovation should therefore proceed through controlled testing rather than regulatory avoidance. The Insurance Regulatory Authority's description of its sandbox approach emphasises live testing within defined parameters while balancing innovation, policyholder protection, and market risk [5].

## 4. Product thesis before model thesis

Every project begins with the customer and the insured or financed economic activity. It must answer:

- Whose problem is being solved?
- What risk is transferred to an insurer?
- What financial obligation is created separately?
- What customer outcome should improve?
- What party has authority to issue, price, amend, service, or terminate each contract?
- What behaviour can the customer reasonably control?
- What risks remain when the measured activity stops?
- Who pays for a discount, holiday, reward, reserve, claim, or intervention?
- What evidence would show that the product helps rather than merely segments customers more finely?

The customer should not be reduced to a score. In mobility products, the driver is often a small operating business. Gross fare is not disposable income. Fuel, platform commission, maintenance, insurance, debt service, household sufficiency, idle time, and route availability compete for the same cash flow. Product design should recognise this operating cycle without converting financial hardship into an automatic insurance penalty.

An innovation hypothesis must be stated in falsifiable form. For example:

> A separately calibrated telematics relativity, applied to exposure-sensitive motor premium within approved floors, caps, and review rules, will improve claims-frequency calibration and encourage safer driving without producing unacceptable access, privacy, or subgroup outcomes.

The hypothesis must name its target population, comparison product, observation horizon, outcome measures, safety constraints, and decision owner. Marketing language must not be substituted for evidence.

## 5. Institutional and contractual boundaries

### 5.1 Insurance

The licensed insurer owns the insurance contract, coverage decision, filed or approved rating basis, claims obligation, actuarial basis, technical provisions, reinsurance, and insurance accounting. A technology platform may calculate governed evidence or provide an authorised interface, but it does not become the risk carrier by operating an algorithm.

The intermediary or embedded-distribution partner must disclose its role and relationship to the insurer. Premium movement must follow the applicable Kenyan structure. The platform must not treat insurer-owned premium cash as its own receivable or operating liquidity. Under section 156 of the Insurance Act, an insurer generally must receive the premium before assuming the risk, and an intermediary must not receive premium on behalf of the insurer [3].

### 5.2 Credit and premium finance

The licensed lender, bank, or authorised credit provider owns credit underwriting, affordability, contractual pricing, limit changes, collections, credit reporting, modification, and complaints within its mandate. Kenya's Digital Credit Providers Regulations require, among other matters, customer protection, appropriate credit-information handling, and accurate and timely information [6].

Insurance premium financing creates three distinct objects:

1. Premium payable to the insurer.
2. Funding advanced by the lender to pay that premium.
3. The resulting finance receivable owed by the customer to the lender.

The premium itself is not casually relabelled a loan asset. A financing SPV may purchase an eligible IPF finance receivable and validly assigned contractual rights where the originator owns and can transfer them. It should not purchase or treat insurer-owned, unremitted premium money as an ordinary receivable. Microloan, revolving-credit, and IPF finance receivables may share one vehicle only when legal advice, eligibility, subledgers, collections, risk treatment, and transaction documents support that structure. Kenya's asset-backed-securities framework should be addressed where receivables are transferred to an SPV [7].

### 5.3 Data roles

Controller, joint-controller, and processor responsibilities are determined by actual purposes and means, not by labels in an architecture diagram. The source-to-use register must identify the lawful basis, purpose, subject, source, recipient, retention, transfer, security, model use, policy use, deletion, and customer-rights process for each field.

Kenya's Data Protection Act gives a data subject rights concerning solely automated decisions that produce legal or similarly significant effects [8]. The General Regulations require meaningful information about the logic and consequences, suitable procedures, prevention and correction of errors, attention to discriminatory effects, human intervention, and a DPIA for high-risk processing such as significant profiling, large-scale combination of datasets, or innovative technology [9]. Human review must be substantive, authorised, informed, and able to change the result.

### 5.4 Decision ownership

A model produces evidence. The relevant insurer, lender, servicer, platform, claims function, or other authorised body makes the decision. Every consequential action must record:

- the accountable owner;
- the legal, contractual, or policy authority;
- the model and policy versions;
- the material input and data-quality status;
- the reason communicated to the customer;
- any human review or override;
- the appeal or correction route;
- the effective period and exit rule; and
- the observed outcome.

## 6. Canonical product architecture

The reusable architecture is:

```text
Consented telematics, trip, policy, claims, payment, and context events
                                |
                 Event-time and feature services
                       /                    \
        Neural temporal representation     Explicit actuarial,
                                            exposure, and product features
                       \                    /
              Redundancy-controlled hierarchical
                    Bayesian or actuarial model
                                |
                 Product Policy and Compliance Gate
                                |
              Quote, underwriting, intervention, claim,
                    servicing, or review workflow
                                |
             Product ledger, accounting, monitoring,
                    customer notice, and audit evidence
```

The names of the branches may vary by product, but their responsibilities must remain distinct:

- **Raw event processing** establishes what happened and when it became knowable.
- **Explicit feature engineering** creates defined, interpretable actuarial and product variables.
- **Neural representation learning** extracts incremental temporal patterns from governed raw sequences.
- **Statistical inference** estimates a defined outcome and its uncertainty.
- **Policy and compliance** apply contract, law, mandate, affordability, eligibility, and safety rules.
- **Product operations** execute an authorised action and preserve customer and accounting consequences.

No model is permitted to collapse these layers merely because an end-to-end neural architecture could technically do so.

## 7. Product and model taxonomy

The following quantities require separate models or explicitly linked submodels:

- claim occurrence;
- claim count or frequency;
- claim severity;
- aggregate insured loss;
- reporting and settlement delay;
- lapse, cancellation, and reinstatement;
- fraud or anomaly likelihood;
- credit default probability;
- loss given default;
- exposure at default;
- utilisation or draw behaviour;
- payment and recovery timing;
- intervention response;
- customer retention or take-up;
- capital and reinsurance outcomes; and
- accounting measurements.

A single generic “risk score” must not stand in for all of them. A binary logistic model can estimate the probability of a defined event within a defined horizon. It does not estimate severity, expected aggregate loss, accounting provision, required capital, or commercial price unless those relationships are separately specified and validated.

Shared features or representations may support multiple model heads, but each head needs its own label, horizon, censoring treatment, calibration, loss function, governance, and validation.

## 8. Usage-based insurance actuarial standard

### 8.1 Separate exposure from risk per unit exposure

Let:

- (i) denote the insured risk or driver;
- (t) denote the observation or coverage period;
- (c(i)) denote a conventional tariff cell;
- (E_{it}) denote earned exposure, such as kilometres, insured driving hours, or trips;
- (N_{it}) denote claim count;
- (Y_{itk}) denote severity of claim (k); and
- (S_{it}=sum_{k=1}^{N_{it}}Y_{itk}) denote aggregate loss.

Usage must not be confused with behavioural risk. A driver who travels twice as far may generate more expected claims even when risk per kilometre is unchanged. Exposure should therefore normally enter a claim-frequency model as an offset or otherwise be modelled explicitly.

A candidate frequency model is:

$$
N_{it}\sim\operatorname{NegBin}(\mu_{it},\phi),
$$

$$
\log\mu_{it}
=
\log E_{it}
+\alpha_{c(i)}
+f(\mathbf x_{it})
+\boldsymbol\beta_h^{\mathsf T}\widetilde{\mathbf h}_{it}
+u_i+u_g+u_v+u_t,
$$

where (mathbf x_{it}) contains approved explicit variables, (widetilde{mathbf h}_{it}) is a residual neural representation, and the (u) terms are suitably identified hierarchical effects for driver, geography, vehicle, or time.

Conditional positive severity may use a Gamma, lognormal, or other validated heavy-tail model:

$$
Y_{itk}\mid N_{it}>0
\sim
F_{+}\left(\mu^{\mathrm{sev}}_{it},\vartheta\right),
$$

$$
\log\mu^{\mathrm{sev}}_{it}
=
\delta_{c(i)}
+g(\mathbf w_{it})
+\boldsymbol\gamma_h^{\mathsf T}\widetilde{\mathbf h}_{it}
+v_g+v_v+v_t.
$$

A Gamma likelihood is not used directly for periods containing zero aggregate claims. The alternatives include a separate frequency-severity model, a compound distribution, or a Tweedie model with an appropriate variance power. Zero-inflated or hurdle models require evidence of a separate structural-zero mechanism.

Telematics research supports distinguishing usage intensity from driving behaviour and testing whether specific behavioural variables actually predict claims [10]. It also warns that telematics can introduce privacy, cost, selection, interpretation, and rate-approval concerns [11]. Variables such as hard braking, night driving, cornering, phone motion, or speed are candidates, not intrinsically fair or causal measures.

### 8.2 Pure premium and modulating variables

Expected pure premium is:

$$
PP_{it}
=
E_{it}\lambda_{it}\mu^{\mathrm{sev}}_{it},
$$

where (lambda_{it}) is expected claim frequency per unit exposure and (mu^{\mathrm{sev}}_{it}) is expected positive severity.

The preferred actuarial modulating variables are separate frequency and severity relativities:

$$
M^{\mathrm{freq}}_{it}
=
\frac{\lambda_{it}}{\lambda_{0,c(i)}},
\qquad
M^{\mathrm{sev}}_{it}
=
\frac{\mu^{\mathrm{sev}}_{it}}
{\mu^{\mathrm{sev}}_{0,c(i)}}.
$$

The combined candidate relativity is:

$$
M^{\mathrm{loss}}_{it}
=M^{\mathrm{freq}}_{it}M^{\mathrm{sev}}_{it}.
$$

Within each approved base cell, calibrate the relativity so that its exposure-weighted mean is one:

$$
\bar M_c
=
\frac{\sum_{i\in c}E_{it}M^{\mathrm{loss}}_{it}}
{\sum_{i\in c}E_{it}},
\qquad
M^{\mathrm{cal}}_{it}
=
\frac{M^{\mathrm{loss}}_{it}}{\bar M_c}.
$$

This prevents the modulator from silently changing the portfolio-level rate indication when its intended role is to redistribute relativities within a base tariff. Any intended portfolio-level change must be identified and approved separately.

The applied relativity may include explicit credibility and transition control:

$$
\log M^{\mathrm{cred}}_{it}
=
Z_{it}\log M^{\mathrm{cal}}_{it},
\qquad 0\le Z_{it}\le1,
$$

where (Z_{it}) is an approved credibility weight or a defensible approximation to the hierarchical shrinkage effect. A new or data-poor driver is therefore drawn toward relativity one rather than treated as either perfectly safe or inherently dangerous.

A product may then apply approved floors, caps, and temporal smoothing:

$$
M^{\mathrm{applied}}_{it}
=
\operatorname{clip}
\left(
\exp\left[
\rho\log M^{\mathrm{applied}}_{i,t-1}
+(1-\rho)\log M^{\mathrm{cred}}_{it}
\right],
M_{\min},M_{\max}
\right).
$$

This is a candidate product mechanism, not a universal formula. The cadence, credibility, floor, cap, smoothing, observation window, and customer notice must be actuarially justified, contractually permitted, filed or approved where required, and monitored for customer and portfolio outcomes.

### 8.3 Commercial premium bridge

The commercial premium should make its components visible:

$$
P_{it}
=
B^{\mathrm{static}}_{it}
+PP_{it}
+C^{\mathrm{expense}}_{it}
+C^{\mathrm{reinsurance}}_{it}
+C^{\mathrm{capital/profit}}_{it}
+T_{it},
$$

where (B^{\mathrm{static}}) covers approved non-driving exposure or fixed coverage cost and (T) contains taxes and levies. A vehicle can retain theft, fire, weather, catastrophe, third-party, and administrative exposure while parked. A zero usage charge therefore does not imply a zero insurance premium.

The bridge must prevent double counting:

- Exposure already used as an offset is not again treated as an unexplained behavioural penalty.
- Expected loss is not loaded again under a different label.
- Uncertainty, capital, reinsurance, and profit are separately governed.
- The IFRS 17 risk adjustment is an accounting measurement, not automatically a tariff loading.
- A customer willingness-to-pay model is not mislabelled an actuarial risk model.
- A credit-liquidity signal is not inserted into motor premium unless its insurance-risk relevance, legality, fairness, stability, and customer meaning are demonstrated.

### 8.4 Pricing cadence and intervention cadence

Near-real-time observation does not require near-real-time repricing. The product should distinguish:

- **Observation cadence:** How often authorised evidence is received.
- **Risk-estimation cadence:** How often the model state is updated.
- **Safety-intervention cadence:** How quickly a proportionate safety action may occur.
- **Tariff cadence:** When a filed or approved premium may change.
- **Contract cadence:** When the policy permits a change or renewal.
- **Accounting cadence:** When liability and performance measurements are updated.

A fatigue signal might prompt a rest suggestion or human review without changing the customer's premium. A short burst of hard braking should not automatically reprice the next kilometre. Dynamic pricing requires stability, notice, controllability, exposure alignment, fairness, and protection against feedback loops.

## 9. Credibility and hierarchical modelling

Hierarchical Bayes extends rather than abolishes actuarial credibility. Classical credibility combines individual experience with collective experience. A hierarchical model implements the same broad idea through partial pooling and can accommodate nonlinear predictors, multiple levels, uncertainty, and richer likelihoods. Jewell's hierarchical credibility work shows the longstanding connection between hierarchical models and credibility [12].

Use partial pooling when groups are heterogeneous and some have limited experience. The hierarchy should follow genuine data-generating and operational structure, such as policy, vehicle, corridor, platform, cohort, or time. It should not create thousands of decorative random effects that the data cannot identify.

Standing rules are:

1. Define the estimand, outcome, exposure, horizon, and grouping before choosing priors.
2. Use weakly informative or substantively informed priors on a scale linked to the outcome and design matrix.
3. Perform prior predictive checks.
4. Consider centred and non-centred parameterisations rather than assuming one is always superior.
5. Constrain or centre hierarchical effects to separate them from the global intercept.
6. Report the practical effect of shrinkage, not only the posterior mean.
7. Do not interpret an HDI as a credibility factor.
8. Do not price automatically at an HDI endpoint.
9. Do not assume uncertainty declines simply because calendar time or exposure increased.
10. Preserve an interpretable baseline and a safe fallback.

Model governance must be proportionate to the harm that an incorrect result could cause. International actuarial guidance emphasises intended purpose, data quality, documentation, reproducibility, validation, limitations, change control, and independent review where proportionate [13], [14]. These standards are adopted only to the extent applicable through the relevant professional or institutional framework, but they provide a strong practice baseline.

## 10. Neural representations and redundancy control

### 10.1 Feature ownership

Each engineered feature has one canonical owner. Raw events may be available to more than one governed process, but the same engineered metric is not silently recreated in several branches.

For an embedded-finance underwriting model, CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and approved financial interactions belong to the Explicit Liquidity Feature Path. For an insurance model, distance, insured duration, trip count, vehicle state, claim history, and defined behavioural measures require their own feature-ownership register.

Feature definitions must state:

- formula;
- unit;
- sign;
- time window;
- event-time and knowledge-time cutoff;
- missingness rule;
- correction rule;
- permitted products and purposes;
- owner and source system;
- expected range and boundary treatment;
- version; and
- retirement process.

### 10.2 Residualisation before optional whitening

Let (mathbf q_i) denote the explicit design, (mathbf m_i) approved metadata, and (mathbf h_i) the low-dimensional neural embedding. The neural block entering a downstream regression is:

$$
\widetilde{\mathbf h}_i
=
\mathbf h_i
-
\widehat{\mathbb E}_{-k(i)}
\left[
\mathbf h_i\mid\mathbf q_i,\mathbf m_i
\right].
$$

The projection is trained without the validation fold containing observation (i). This cross-fitted residualisation reduces the neural branch's ability to reproduce the explicit block and count the same economic information twice. Cross-fitting is a recognised device for reducing overfitting and regularisation bias in orthogonal estimation, although the use here is a prediction-governance adaptation rather than a claim that the whole model is a formal double-machine-learning estimator [15].

Whitening, when diagnostics support it, is fitted only on training data and applied unchanged to validation, test, and production observations. PCA whitening creates training-sample components with approximately unit covariance under its convention, but it does not establish statistical independence, causal separation, future-regime orthogonality, or interpretability [16].

The standard control stack is:

1. Explicit feature ownership.
2. A deliberately narrow neural bottleneck.
3. Cross-fitted residualisation against the explicit design and approved metadata.
4. Optional fold-fitted whitening or another documented conditioning transform.
5. Separate priors for explicit, neural, hierarchy, interaction, and metadata blocks.
6. Strong heredity for interactions.
7. Posterior correlation and condition diagnostics.
8. Explicit-only, neural-only, and combined ablations.
9. Out-of-time and out-of-group incremental-value testing.
10. An explicit-only fallback when the neural block does not earn deployment.

No document should claim that this process eliminates all multicollinearity. It reduces avoidable duplication and improves identifiability. The result must still be diagnosed under new populations and regimes.

### 10.3 Shrinkage priors

The regularized horseshoe is a candidate for a genuinely sparse, high-dimensional residual block. It uses global-local shrinkage while imposing finite regularisation on large coefficients. Its global scale and slab width must reflect a prior view of sparsity and plausible effect size [17].

The horseshoe does not:

- make correlated predictors orthogonal;
- perform exact variable deletion;
- guarantee identifiable attribution among substitutes;
- repair data leakage;
- replace feature ownership; or
- remove the need for sensitivity and ablation tests.

Low-dimensional, interpretable blocks may be better served by regularised normal or Student-(t) priors. Prior choice is block-specific, not a branding decision.

## 11. Bayesian computation and predictive validation

### 11.1 Computational faithfulness

Every approved Bayesian model should undergo:

- prior predictive checks;
- unit and property tests for likelihood and transformations;
- simulation recovery tests;
- simulation-based calibration where appropriate for validating the inference implementation;
- multiple-chain diagnostics;
- rank-normalised split and folded (widehat R);
- bulk and tail effective sample size;
- Monte Carlo standard error;
- divergence, energy, and tree-depth review;
- sensitivity to parameterisation and prior scale; and
- reproducible seeds, environments, code, data references, and configuration.

Posterior predictive checks compare observations with replicated data generated by the fitted model and should target features that matter to the decision, including counts, zeros, tails, calibration, subgroup behaviour, time patterns, and dependence [18]. They test whether the model reproduces relevant aspects of the data. They do not prove that the model is true.

An internal target such as (widehat R<1.01) may be adopted, but no scalar diagnostic is sufficient. Effective sample size and Monte Carlo error must be assessed for the actual estimands, especially tail probabilities and high quantiles [19]. Faster hardware or a JAX sampler does not cure poor posterior geometry.

### 11.2 Predictive design

Validation splits must reflect deployment:

- **Out of time:** Later periods test drift and regime transportability.
- **Out of driver or policy:** Repeated observations from one subject do not leak across folds.
- **Out of group:** New platforms, geographies, partners, vehicles, or cohorts are tested where expansion requires transportability.
- **Out of event:** Claim development and late labels respect the information available at cutoff.
- **Stress periods:** Fuel, weather, platform, repair-cost, market, cyber, or operational disruptions are represented through observed or governed hypothetical scenarios.

Random row-level cross-validation is not sufficient when records repeat over time or entity.

Evaluate at least:

- calibration-in-the-large and calibration slope;
- calibration plots and observed-to-expected ratios;
- Brier score and log score;
- discrimination where relevant;
- decision value under the actual loss or utility function;
- frequency and severity fit;
- tail and large-loss behaviour;
- interval or predictive coverage;
- stability by time, platform, geography, vehicle, and product;
- subgroup and intersectional performance;
- operational latency and fallback frequency; and
- economic and customer outcomes.

A superior AUC does not justify deployment if calibration, stability, fairness, explanation, product value, or operational resilience deteriorates materially.

### 11.3 Champion-challenger discipline

The transparent actuarial or explicit-only model is the initial champion unless evidence supports another choice. Neural, copula, dynamic, or alternative likelihood components begin as challengers.

A challenger is promoted only if it demonstrates:

- stable incremental out-of-time value;
- material decision or customer value, not merely statistical significance;
- acceptable calibration and uncertainty;
- manageable fairness and conduct effects;
- reproducible implementation;
- operational resilience and fallback;
- intelligible reasons at the product layer;
- proportionate cost; and
- approval by the accountable model and product owners.

Complexity is removable. Rollback is part of the design, not an admission of failure.

## 12. Point-in-time data and event truth

Every material event should carry:

- immutable event identifier;
- source and source-record identifier;
- subject, policy, claim, vehicle, facility, and account identifiers as relevant;
- valid or economic event time;
- source-recorded time;
- ingestion time;
- processing time;
- amount, currency, sign, unit, and measurement basis;
- schema and feature version;
- quality, consent, and permitted-use status;
- correction, reversal, and predecessor links; and
- integrity metadata.

If (t_i^{\mathrm{known}}) is the earliest time the system could lawfully and operationally have known event (i), and (t_d) is the reconstructed decision time, a training input is eligible only when:

$$
t_i^{\mathrm{known}}\le t_d.
$$

This condition is applied to revised macroeconomic data, late wallet settlements, corrected trips, backfilled claims, recoveries, cancellations, and customer information. A valid economic date alone is not enough.

The data-quality programme covers:

- identity resolution and effective dating;
- source reconciliation;
- completeness, accuracy, uniqueness, timeliness, and validity;
- units, signs, currencies, calendars, and time zones;
- missingness mechanisms;
- device and platform changes;
- duplicate and replay handling;
- late events and corrections;
- label definition, maturity, censoring, and leakage;
- online-offline feature consistency;
- representativeness and selection;
- proxy and subgroup coverage;
- retention and deletion; and
- lineage from source to decision and report.

Missingness is not automatically adverse customer behaviour. It may result from consent withdrawal, device failure, connectivity, battery saving, platform outage, schema change, or data-supply inequality. The model must represent missingness carefully, and the policy gate must use a safe fallback where evidence is inadequate.

## 13. Fairness, customer agency, and causal humility

Fairness is an end-to-end product property. Removing protected attributes from production features is not sufficient because geography, device quality, work schedule, vehicle, platform, route, and missingness can act as proxies.

The programme should measure, where lawful and meaningful:

- data coverage and missingness;
- quote, approval, decline, price, limit, and coverage outcomes;
- false-positive and false-negative consequences;
- calibration and error by group;
- claim and intervention outcomes;
- complaints, appeals, reversals, and overrides;
- customer comprehension and ability to act;
- selection and attrition; and
- intersectional effects.

No single metric proves fairness. Equalized odds, demographic parity, calibration, disparate-impact ratios, counterfactual analysis, and representation diagnostics answer different questions and can conflict. Thresholds imported from another jurisdiction are comparative conventions unless Kenyan authority or adopted policy makes them applicable.

The platform must distinguish prediction from causation. A variable can predict loss without being an appropriate intervention target. Hard braking may reflect driver behaviour, but it may also reflect poor roads, unsafe dispatch, congestion, passenger actions, or avoiding a collision. A higher premium may alter driving hours, route choice, maintenance, liquidity, and future data, creating a feedback loop.

Intervention effectiveness should therefore be evaluated through a defensible causal design where practical, such as randomised encouragement, phased rollout, matched comparison, interrupted time-series analysis, or another pre-specified design. The experiment must include safety, customer, fairness, and spillover outcomes, not only collections or loss ratio.

The Credit or Product Policy and Compliance Gate should prefer proportionate, reversible, and supportive actions when compatible with the contract and risk. It should record uncertainty and permit human challenge. A thin data history is not itself evidence of dangerous behaviour.

## 14. Pricing, probability measures, capital, and accounting

### 14.1 Physical and market-consistent measures

Use the physical measure (mathbb P) for forecasting actual claim frequency, severity, default, lapse, recovery, and cash-flow outcomes. A risk-neutral or market-consistent measure (mathbb Q) is used only for a defined valuation purpose with a defensible numeraire, stochastic process, calibration basis, and treatment of non-hedgeable risk.

Primary insurance losses are usually not perfectly replicable through traded assets. In incomplete markets there is generally no unique risk-neutral price without an additional pricing principle [20]. Girsanov's theorem does not by itself convert an actuarial forecast into a commercial motor premium. A formula such as (mu_{\mathbb Q}=\mu_{\mathrm{HDI}}+\sigma\gamma) is not accepted without a fully specified process and calibration.

Use (mathbb Q), where justified, for hedgeable interest-rate, FX, asset-linked, guarantee, or investor-valuation components. Keep the operational insurance and credit models under (mathbb P) unless the model purpose explicitly requires otherwise.

### 14.2 Distinct pricing quantities

Never treat the following as synonyms:

- expected claim cost or pure premium;
- commercial insurance premium;
- credit expected loss;
- customer lending rate;
- KESONIA reference rate;
- risk-based credit premium;
- SPV note margin;
- liquidity or funds-transfer charge;
- reinsurance cost;
- cost of capital;
- accounting risk adjustment;
- regulatory capital;
- investor hurdle or discount rate; and
- economic value.

Each quantity requires its own owner, purpose, unit, horizon, legal basis, and reconciliation.

For applicable Kenyan variable-rate lending, the contract and pricing system should follow the current CBK benchmark framework and document KESONIA publication, observation, compounding, day count, correction, and fallback conventions [21]. The insurance tariff remains under insurer and actuarial ownership and is not derived from KESONIA merely because premium finance is attached.

### 14.3 Accounting boundaries

IFRS 17 measures insurance-contract groups using fulfilment cash flows, a risk adjustment for non-financial risk, and the contractual service margin where applicable. The risk adjustment is conceptually separate from expected cash flows and discount rates and should not be double-counted [22]. It is not automatically the tariff's uncertainty loading.

IFRS 9 expected credit loss belongs to the holder of the financial asset and uses probability-weighted cash shortfalls, reasonable and supportable information, and the entity's approved staging methodology [23]. A credit PD may be an input. It is not, by itself, an IFRS 9 stage or journal entry.

The model must not collapse insurance claims, credit defaults, accounting provisions, and capital into one probability or one reserve. Accounting follows contract classification, reporting entity, evidence, policy, and approval.

## 15. Dependence, stress, capital, and reinsurance

Marginal models must be calibrated before a dependence model is trusted. Linear correlation is insufficient for many tail questions, but a copula family is not selected from narrative intuition alone.

Candidate dependence models may include independence, Gaussian, Student-(t), Clayton, survival or rotated families, Gumbel, mixtures, common-shock models, and scenario overlays. Compare:

- held-out likelihood or scoring rules;
- lower- and upper-tail fit;
- parameter stability;
- sensitivity to marginal miscalibration;
- economic interpretability;
- regime behaviour;
- sample adequacy; and
- relevance to cash, claims, reinsurance, or capital decisions.

Dependence evidence should feed scenario analysis, aggregation, reinsurance, liquidity, and capital. It should not automatically change an individual customer's price.

Posterior predictive loss distributions may inform capital analysis, but a selected quantile is not automatically regulatory capital. Capital requires the applicable legal framework, balance-sheet scope, horizon, dependencies, diversification, reinsurance, market and credit risk, operational risk, and management actions.

Reinsurance must be modelled as a contract with attachment, limit, reinstatement, exclusions, basis risk, counterparty credit, timing, collateral, and cost. A pricing model that ignores reinsurance and large-loss behaviour is incomplete for product approval.

## 16. AI and model-risk governance

The model inventory should include statistical models, neural systems, rule engines, spreadsheets, pricing services, external vendor models, exposure transforms, claims triage, anomaly detection, and material manual overlays. Risk classification depends on use and impact, not whether a component is marketed as AI.

The governance cycle follows four continuous questions:

1. **Govern:** Who is accountable, what is the risk appetite, and what rules apply?
2. **Map:** What customer, product, data, partner, and failure context surrounds the system?
3. **Measure:** What evidence demonstrates performance, uncertainty, fairness, robustness, and harm?
4. **Manage:** What is approved, restricted, mitigated, monitored, rolled back, or retired?

This reflects the NIST AI Risk Management Framework's Govern, Map, Measure, and Manage structure [24]. Insurance-specific comparative guidance also emphasises proportional governance, consumer interest, fairness, roles, data, documentation, human oversight, and lifecycle risk management [25], [26]. These materials are comparative where they are not adopted in Kenya.

The minimum governance roles are:

- product owner;
- licensed insurance or credit decision owner;
- actuarial owner;
- model developer;
- independent validator;
- data owner and data-protection officer;
- compliance and legal reviewer;
- security and resilience owner;
- finance and accounting owner;
- operations and complaints owner; and
- change-approval committee.

Development, validation, approval, deployment, and monitoring should be separated proportionately. SR 11-7 remains a useful comparative description of conceptual soundness, ongoing monitoring, benchmarking, outcomes analysis, governance, and validation, but it is not Kenyan insurance law [27].

Every model version requires a model card containing:

- purpose and prohibited uses;
- accountable owners;
- population, product, outcome, horizon, and exposure;
- data sources and cutoff;
- features and ownership;
- methodology and priors;
- training and validation design;
- performance and uncertainty;
- subgroup and fairness results;
- assumptions and limitations;
- explanation and reason-code mapping;
- thresholds and policy dependencies;
- fallback, override, and appeal;
- monitoring and recalibration triggers;
- implementation and environment;
- approvals; and
- change history.

## 17. Security, resilience, and safe degradation

Insurance and financial decisions require confidentiality, integrity, availability, authenticity, recoverability, and traceability. Apply a lifecycle covering governance, identification, protection, detection, response, and recovery, consistent with the NIST Cybersecurity Framework 2.0 as a comparative control structure [28].

Required practices include:

- least privilege and role separation;
- managed identities and strong authentication;
- encryption in transit and at rest;
- key, secret, and certificate lifecycle management;
- network and data-zone segmentation;
- secure software supply chain and dependency review;
- immutable or tamper-evident logs where justified;
- backup, restoration, recovery-point, and recovery-time testing;
- monitoring of privileged activity and data exfiltration;
- incident response and customer-impact assessment;
- vendor exit and service-continuity planning; and
- tested manual and explicit-model fallbacks.

Cryptography can protect data and provenance. It cannot prove that source data are accurate, a model is fair, an accounting entry is correct, or an action is lawful. Those conclusions require the wider control framework.

Safe degradation rules are explicit:

- Missing or stale telematics do not automatically become adverse evidence.
- A failed neural service falls back to an approved explicit model or manual process.
- A failed benchmark feed invokes the contractual fallback and exception process.
- A failed customer-notification channel blocks actions that require notice.
- An unreconciled ledger or premium movement enters an exception queue rather than being forced through.
- Material drift triggers investigation and proportionate restriction, not automatic retraining.

## 18. Source and evidence policy

### 18.1 Evidence hierarchy

Use sources in this order:

1. Kenyan legislation, subsidiary legislation, regulator publications, official methodologies, and court decisions.
2. Applicable IFRS standards and adopted actuarial or professional standards.
3. Primary international standard setters and supervisors, clearly labelled as comparative when not locally binding.
4. Peer-reviewed original research and established actuarial research.
5. Official technology documentation for implementation claims.
6. High-quality professional commentary for context.
7. Media, vendor marketing, social posts, aggregators, and search artefacts only for leads, market colour, or explicitly qualified examples.

An inaccessible or unread source does not support a substantive claim. A secondary summary should not override available primary authority.

### 18.2 Claim ledger

Every material claim should be classified as one of:

- legal or regulatory requirement;
- contractual requirement;
- professional practice;
- internal policy;
- empirical finding;
- model assumption;
- calibrated parameter;
- derived calculation;
- scenario input;
- design proposal;
- illustrative example; or
- unresolved diligence item.

The claim ledger records the statement, source, jurisdiction, as-of date, owner, status, affected document or model, conflicting evidence, and required verification.

### 18.3 Citation policy

- Use IEEE numerical citations in order of first appearance within each standalone paper.
- Give every reference its own paragraph.
- Link directly to the supporting page or document, not a search-results page.
- Include author or organisation, title, publication, date, URL or DOI, and access date for mutable web material.
- Place citations beside the claim they support.
- Do not cite a source for a stronger proposition than it establishes.
- Label foreign supervisory guidance as comparative unless applicable through a named institution or contract.
- Give time-sensitive claims an as-of date.
- Keep quotations short and preserve exact wording only where legally or analytically necessary.
- Rebuild reference numbering after substantive editing so the list follows body appearance.

### 18.4 Quantitative provenance

Every material number should disclose:

- definition and formula;
- source or assumption status;
- unit and currency;
- gross or net basis;
- exposure and population;
- valuation, observation, and publication dates;
- nominal or real basis;
- pre-tax or post-tax basis;
- scenario and confidence level where relevant;
- owner; and
- replacement or review requirement.

Unsupported precision is avoided. Illustrative assumptions remain visibly illustrative until replaced.

## 19. Canonical notation register

Projects may extend this register but should not reuse a symbol for an unrelated concept.

| Symbol | Canonical meaning |
|---|---|
| (i) | Individual insured, driver, borrower, policy, or exposure unit, defined per model |
| (t) | Observation, decision, accident, development, or coverage period, explicitly defined |
| (c(i)) | Conventional tariff or credibility cell for unit (i) |
| (p) | Product identifier |
| (E_{it}) | Earned insurance exposure in stated units |
| (N_{it}) | Claim count during the stated period |
| (Y_{itk}) | Positive severity of claim (k) |
| (S_{it}) | Aggregate insured loss during the period |
| (lambda_{it}) | Expected claim frequency per unit exposure under (mathbb P) |
| (mu^{\mathrm{sev}}_{it}) | Expected positive claim severity under (mathbb P) |
| (PP_{it}) | Expected pure premium or expected claim cost |
| (M^{\mathrm{freq}}_{it}) | Frequency relativity to an approved base cell |
| (M^{\mathrm{sev}}_{it}) | Severity relativity to an approved base cell |
| (M^{\mathrm{loss}}_{it}) | Combined expected-loss relativity |
| (M^{\mathrm{applied}}_{it}) | Credibility-adjusted, smoothed, and bounded product relativity |
| (Z_{it}) | Explicit credibility weight when one is defined |
| (B^{\mathrm{static}}_{it}) | Fixed or non-driving insurance premium component |
| (P_{it}) | Commercial insurance premium, not probability |
| (PD_i^{(p)}) | Probability of a defined credit default over a stated horizon |
| (LGD_i^{(p)}) | Loss given default under a stated recovery and timing convention |
| (EAD_i^{(p)}) | Exposure at default under a stated product convention |
| (EL_i^{(p)}) | Credit expected loss, normally (PD\times LGD\times EAD) with compatible horizons |
| (mathbf z_i) | Explicit engineered feature vector before basis expansion |
| (mathbf q_i) | Centred and conditioned explicit design, such as a QR spline basis |
| (mathbf h_i) | Neural embedding before redundancy control |
| (widetilde{\mathbf h}_i) | Cross-fitted residual neural embedding |
| (oldsymbol\psi_i) | Pre-registered interaction design satisfying heredity rules |
| (mathbf m_i) | Approved metadata and data-quality terms |
| (mathcal U_i) | Defined model-uncertainty measure, not a generic risk load |
| (mathbb P) | Physical or real-world probability measure |
| (mathbb Q) | Risk-neutral or market-consistent measure for a justified valuation purpose |
| (K_{\mathrm{RBCP}}) | Customer risk-based credit-pricing premium under the applicable CBK framework |
| (K_{\mathrm{cap}}) | Regulatory capital amount, if this symbol is used |
| (m_A,m_B) | SPV note margins for Class A and Class B |
| (RA) | IFRS 17 risk adjustment for non-financial risk |
| (CSM) | IFRS 17 contractual service margin |
| (OC) | Overcollateralisation ratio with an explicit denominator |
| (CRA) | SPV cash reserve account, distinct from a driver reserve |

Variable names should preserve units and horizons. A probability, rate, amount, balance, relativity, and index should never share an ambiguous label.

## 20. Documentation and narrative standard

Technical consistency should strengthen rather than flatten the human story. A publication should normally move through:

1. A recognisable customer or market situation.
2. The microeconomic or actuarial mechanism.
3. The limitation of the conventional response.
4. The product insight.
5. The mathematical or computational formulation.
6. A visual explanation.
7. The operating, insurance, credit, and financial consequence.
8. The assumptions, limitations, and evidence required.
9. A transition to the next question.

Good mathematical narration:

- introduces the question before the equation;
- defines every material symbol;
- states unit, horizon, sign, and cutoff;
- explains what the equation reveals;
- distinguishes identity, estimator, hypothesis, assumption, and approved rule;
- retains innovative formulae when dimensionally coherent;
- states calibration and validation status; and
- avoids presenting elegant notation as empirical proof.

Good diagrams:

- show causality, sequence, ownership, or institutional boundaries;
- separate data flow, cash flow, contractual rights, and decision authority;
- use short but meaningful labels;
- preserve enough density to reward inspection;
- remain legible in the final medium;
- use consistent colour semantics;
- receive a numbered caption and narrative explanation; and
- avoid guarantees or unsupported claims inside nodes.

Root narrative papers may be rich, discursive, and mathematically ambitious. Controlled specifications should separately state exact interfaces, owners, tests, failure modes, and acceptance conditions. Neither form should be forced to perform the other's full role.

## 21. Product and model validation checklist

### 21.1 Product validity

- [ ] The target customer and unmet need are defined.
- [ ] The coverage and non-coverage are intelligible.
- [ ] The target market and foreseeable vulnerable groups are identified.
- [ ] The customer-value hypothesis is falsifiable.
- [ ] The insurer, intermediary, lender, platform, and servicer roles are distinct.
- [ ] Premium, credit, fee, and collection cash flows are legally and operationally separated.
- [ ] Policy wording, marketing, application, claims, complaints, and cancellation journeys agree.
- [ ] The business case includes customer, insurer, distributor, and partner economics.
- [ ] Capital and reinsurance consequences are assessed.
- [ ] Pilot, rollback, and post-implementation review are defined.

### 21.2 Data validity

- [ ] A source-to-use register exists.
- [ ] Lawful basis and purpose are documented for every material field.
- [ ] A DPIA has been completed where required.
- [ ] Data-subject notices and rights processes are operational.
- [ ] Identity and effective dating are controlled.
- [ ] Event time, knowledge time, ingestion time, and corrections are retained.
- [ ] Labels, censoring, maturity, and recovery are defined.
- [ ] Point-in-time training reconstruction has been tested.
- [ ] Missingness and data-supply inequality have been analysed.
- [ ] Source, ledger, and cash reconciliations pass.
- [ ] Training and production feature calculations agree.
- [ ] Retention, deletion, transfer, and access controls are tested.

### 21.3 Actuarial and statistical validity

- [ ] Exposure, frequency, severity, and aggregate loss are separated or coherently combined.
- [ ] Fixed and usage-sensitive premium components are distinguished.
- [ ] Relativities are calibrated to an approved base.
- [ ] Credibility, floors, caps, smoothing, and cadence are justified.
- [ ] Deductibles, limits, inflation, large losses, delays, and reinsurance are reflected.
- [ ] Priors and likelihoods are justified and tested predictively.
- [ ] Hierarchies correspond to real structure and are identifiable.
- [ ] Neural and explicit feature ownership is documented.
- [ ] Residualisation and any whitening are fold-fitted.
- [ ] Shrinkage does not substitute for feature governance.
- [ ] Marginal calibration precedes dependence modelling.
- [ ] The physical and market-consistent measures are separated.
- [ ] Uncertainty is not double-counted across premium, capital, and accounting.

### 21.4 Computational validity

- [ ] Unit, property, and simulation-recovery tests pass.
- [ ] Prior and posterior predictive checks are decision-relevant.
- [ ] MCMC diagnostics are acceptable for material estimands.
- [ ] No unexplained divergences or severe geometry failures remain.
- [ ] Out-of-time and out-of-group tests pass approved thresholds.
- [ ] Calibration, discrimination, scoring, and economic value are reported together.
- [ ] Ablations show the incremental contribution of every complex block.
- [ ] Results are reproducible from controlled data, code, configuration, and environment.
- [ ] A challenger has not been promoted on one metric alone.

### 21.5 Fairness and customer validity

- [ ] Protected and vulnerable groups are considered under a lawful audit design.
- [ ] Proxy pathways and structural constraints are investigated.
- [ ] Coverage, missingness, errors, calibration, price, limits, interventions, and complaints are compared.
- [ ] No single fairness statistic is presented as proof.
- [ ] Customer-facing reasons map to stable, material product factors.
- [ ] Human intervention can genuinely reconsider a significant automated decision.
- [ ] Appeal, correction, and complaint processes are tested.
- [ ] Intervention effects are measured rather than assumed causal.
- [ ] The product does not punish customers for platform, device, or infrastructure failures outside their control.

### 21.6 Operational and financial validity

- [ ] Decision rights and delegated authorities are approved.
- [ ] The product ledger is authoritative for contract detail.
- [ ] Premium, claims, credit, receivables, and accounting events reconcile.
- [ ] Exceptions remain visible until resolved.
- [ ] Fallback, rollback, recovery, and manual operation are tested.
- [ ] Model, policy, price, and accounting versions are linked.
- [ ] Monitoring has owners, thresholds, diagnoses, and proportionate actions.
- [ ] Contractual covenants are distinguished from dashboard alerts.
- [ ] Insurance accounting, credit accounting, capital, and investor reporting remain separate.
- [ ] Security and business-continuity exercises include partner and vendor failure.

### 21.7 Publication quality

- [ ] Claims are classified and sourced.
- [ ] References follow first appearance and every entry is cited.
- [ ] Foreign guidance is labelled comparative.
- [ ] Time-sensitive claims state an as-of date.
- [ ] Equations define symbols, units, horizons, and status.
- [ ] Tables reconcile and show denominators.
- [ ] Figures are numbered, referenced, and legible.
- [ ] Narrative, technical specification, and commercial claims do not contradict one another.
- [ ] Guarantees have been replaced by conditional, testable statements.
- [ ] A knowledgeable customer, actuary, engineer, and decision owner can each understand their part.

## 22. Stage gates

### Gate 0: Problem and mandate

Pass only when the customer problem, product owner, legal entities, target market, intended outcomes, prohibited uses, research plan, and regulator-engagement path are clear.

### Gate 1: Data and contractual authority

Pass only when the source-to-use register, data agreements, DPIA, customer notices, identity model, event contracts, policy wording, and product cash flows are sufficiently defined for controlled development.

### Gate 2: Transparent baseline

Pass only when an interpretable actuarial baseline, product rules, exposure definitions, reason codes, manual workflow, and reconciliation can operate in shadow mode.

### Gate 3: Advanced challenger

Pass only when hierarchical, neural, dynamic, or dependence components demonstrate stable incremental value, computational validity, fairness evidence, documentation, fallback, and independent challenge.

### Gate 4: Controlled pilot

Pass only when the pilot has bounded customers, exposure, geography, duration, losses, authority, support, monitoring, funding, complaints, and stop conditions. Required regulator no-objection or sandbox arrangements must be in place.

### Gate 5: Accounting and operational landing

Pass only when product ledgers, premium and claims systems, journals, actuarial processes, reinsurance, reports, security, resilience, customer notices, and exception management reconcile.

### Gate 6: Measured scale

Pass only when real cohort evidence supports expansion by product, geography, platform, vehicle, and customer segment. Scale is reversible and conditional on continuing performance and customer outcomes.

### Gate 7: Post-implementation review

Review actual versus expected claims, exposure, price, selection, customer value, fairness, complaints, operational incidents, capital, reinsurance, model drift, and commercial performance. Revise, restrict, or retire the product where evidence requires it.

## 23. Definition of done

An innovative actuarial or Insurtech product is ready for its approved stage only when:

- the customer proposition is intelligible and useful;
- the licensed and accountable institutions own their decisions;
- premium, credit, insurance risk, and cash rights are structurally distinct;
- exposure and risk per unit exposure are not confused;
- the actuarial model is calibrated, credible, reproducible, and monitored;
- advanced models add stable value beyond the transparent baseline;
- uncertainty informs decisions without becoming a disguised duplicate loading;
- customers receive meaningful notice, human challenge, and correction rights;
- privacy, fairness, security, and resilience controls operate in practice;
- contracts, ledgers, accounting, capital, and reinsurance agree with the model's role;
- claims and commercial statements are supported by indexed evidence; and
- the product can fail safely, roll back, and improve from observed outcomes.

The standard is not mathematical perfection. It is a product whose assumptions are visible, whose innovation is testable, whose decisions are owned, whose cash and data reconcile, and whose value can be demonstrated without sacrificing the people it is intended to serve.

## References

[1] Republic of Kenya, “The Insurance (Products) Guidelines, 2022,” *Kenya Law*, Gazette Notice No. 3641, Mar. 29, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3641/eng@2022-03-29. Accessed: Aug. 26, 2026.

[2] Republic of Kenya, “The Insurance (Market Conduct) Guidelines, 2022,” *Kenya Law*, Gazette Notice No. 3642, Mar. 29, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3642/eng@2022-03-29. Accessed: Aug. 26, 2026.

[3] Republic of Kenya, *Insurance Act*, Cap. 487, rev. Dec. 11, 2023. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/1985/1/eng@2023-12-11. Accessed: Aug. 26, 2026.

[4] Republic of Kenya, “The Insurance (Risk Management and Control Functions) Guidelines, 2022,” *Kenya Law*, Gazette Notice No. 3643, Mar. 29, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/gn/2022/3643/eng@2022-03-29. Accessed: Aug. 26, 2026.

[5] Insurance Regulatory Authority of Kenya, *Insurance Industry Annual Report 2023*. [Online]. Available: https://www.ira.go.ke/assets/file/Insurance_Industry_Annual_Report_2023.pdf. Accessed: Aug. 26, 2026.

[6] Central Bank of Kenya, *The Central Bank of Kenya (Digital Credit Providers) Regulations, 2022*, Legal Notice No. 46, Mar. 2022. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2022/03/L-.N.-No.-46-Central-Bank-of-Kenya-Digital-Credit-Providers-Regulations-2022.pdf. Accessed: Aug. 26, 2026.

[7] Republic of Kenya, *The Capital Markets (Asset-Backed Securities) Regulations, 2007*, Legal Notice No. 184, rev. Dec. 31, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2007/184/eng@2022-12-31. Accessed: Aug. 26, 2026.

[8] Republic of Kenya, *Data Protection Act*, No. 24 of 2019, rev. Dec. 31, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24/eng@2022-12-31. Accessed: Aug. 26, 2026.

[9] Republic of Kenya, *The Data Protection (General) Regulations, 2021*, Legal Notice No. 263, rev. Dec. 31, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng@2022-12-31. Accessed: Aug. 26, 2026.

[10] Casualty Actuarial Society, *Balancing Risk Assessment and Social Fairness: An Auto Telematics Case Study*, CAS Research Paper Series on Race and Insurance Pricing, 2024. [Online]. Available: https://www.casact.org/sites/default/files/2024-08/Balancing_Risk_Assessment_and_Social_Fairness_an_Auto_Telematics_Case_Study.pdf. Accessed: Aug. 26, 2026.

[11] National Association of Insurance Commissioners, “Telematics/Usage-Based Insurance,” Center for Insurance Policy and Research, updated Oct. 26, 2023. [Online]. Available: https://content.naic.org/cipr_topics/topic_telematicsusage_based_insurance.htm. Accessed: Aug. 26, 2026.

[12] W. S. Jewell, *The Use of Collateral Data in Credibility Theory: A Hierarchical Model*, International Institute for Applied Systems Analysis, Research Memorandum RM-75-024, 1975. [Online]. Available: https://pure.iiasa.ac.at/id/eprint/492/?template=default_internal. Accessed: Aug. 26, 2026.

[13] International Actuarial Association, *ISAP 1: General Actuarial Practice*, Dec. 2018. [Online]. Available: https://actuaries.org/publications/international-standards-of-actuarial-practices/. Accessed: Aug. 26, 2026.

[14] International Actuarial Association, *ISAP 1A: Governance of Models*, Dec. 2018. [Online]. Available: https://actuaries.org/app/uploads/2025/04/ISAP_1A_Final_December2018_Web-1.pdf. Accessed: Aug. 26, 2026.

[15] V. Chernozhukov, D. Chetverikov, M. Demirer, E. Duflo, C. Hansen, W. Newey, and J. Robins, “Double/Debiased Machine Learning for Treatment and Causal Parameters,” *The Econometrics Journal*, vol. 21, no. 1, pp. C1-C68, 2018, doi: 10.1111/ectj.12097. [Online]. Available: https://arxiv.org/abs/1608.00060. Accessed: Aug. 26, 2026.

[16] Scikit-learn Developers, “PCA,” *Scikit-learn Documentation*. [Online]. Available: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html. Accessed: Aug. 26, 2026.

[17] J. Piironen and A. Vehtari, “Sparsity information and regularization in the horseshoe and other shrinkage priors,” *Electronic Journal of Statistics*, vol. 11, no. 2, pp. 5018-5051, 2017, doi: 10.1214/17-EJS1337SI. [Online]. Available: https://www.projecteuclid.org/journals/electronic-journal-of-statistics/volume-11/issue-2/Sparsity-information-and-regularization-in-the-horseshoe-and-other-shrinkage/10.1214/17-EJS1337SI.pdf. Accessed: Aug. 26, 2026.

[18] Stan Development Team, “Posterior and Prior Predictive Checks,” *Stan User's Guide*. [Online]. Available: https://mc-stan.org/docs/stan-users-guide/posterior-predictive-checks.html. Accessed: Aug. 26, 2026.

[19] Stan Development Team, “Posterior Analysis,” *Stan Reference Manual*. [Online]. Available: https://mc-stan.org/docs/reference-manual/analysis.html. Accessed: Aug. 26, 2026.

[20] H. Niederau and P. Zweifel, “Quasi Risk-Neutral Pricing in Insurance,” *ASTIN Bulletin*, vol. 39, no. 1, pp. 317-337, 2009, doi: 10.2143/AST.39.1.2038067. [Online]. Available: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2A5E0315BBE20FFF6073A7DF2650A524/S0515036100000143a.pdf/quasi_riskneutral_pricing_in_insurance.pdf. Accessed: Aug. 26, 2026.

[21] Central Bank of Kenya, “KESONIA Interest Rate Benchmark.” [Online]. Available: https://www.centralbank.go.ke/kesonia/. Accessed: Aug. 26, 2026.

[22] IFRS Foundation, *IFRS 17 Insurance Contracts*, paras. B86-B92, 2022 issued standards. [Online]. Available: https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2022/issued/part-a/ifrs-17-insurance-contracts.pdf?bypass=on. Accessed: Aug. 26, 2026.

[23] IFRS Foundation, *IFRS 9 Financial Instruments: Project Summary*, July 2014. [Online]. Available: https://www.ifrs.org/content/dam/ifrs/project/fi-classification-and-measurement/ifrs-standard/published-documents/project-summary.pdf. Accessed: Aug. 26, 2026.

[24] E. Tabassi, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, National Institute of Standards and Technology, Jan. 2023, doi: 10.6028/NIST.AI.100-1. [Online]. Available: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10. Accessed: Aug. 26, 2026.

[25] European Insurance and Occupational Pensions Authority, *Opinion on Artificial Intelligence Governance and Risk Management*, Aug. 6, 2025. [Online]. Available: https://www.eiopa.europa.eu/publications/opinion-artificial-intelligence-governance-and-risk-management_en. Accessed: Aug. 26, 2026. Comparative guidance; not Kenyan law.

[26] International Actuarial Association, *Artificial Intelligence Governance Framework*, 2025. [Online]. Available: https://actuaries.org/app/uploads/2025/12/AITF_Governance_Framework_Paper_Final_Approved.pdf. Accessed: Aug. 26, 2026.

[27] Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency, *Supervisory Guidance on Model Risk Management*, SR Letter 11-7, Apr. 2011. [Online]. Available: https://www.federalreserve.gov/supervisionreg/srletters/sr1107a1.pdf. Accessed: Aug. 26, 2026. Comparative guidance; not Kenyan law.

[28] National Institute of Standards and Technology, *NIST Cybersecurity Framework 2.0: Resource and Overview Guide*, NIST SP 1299, 2024. [Online]. Available: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1299.pdf. Accessed: Aug. 26, 2026.
