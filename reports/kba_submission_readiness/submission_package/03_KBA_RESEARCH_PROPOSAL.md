# Research Proposal

## Can Spatial Catastrophe Intelligence Improve Bank Credit-Risk Identification in Kenya?

### A flood-and-drought empirical framework

**Author:** Nevil Maloba  
**Affiliation:** Founder, Philtechent LTD  
**Qualification:** BSc Actuarial Science, University of Eldoret  
**Email:** nevillemaloba@gmail.com  
**Proposed KBA sub-theme:** Risk Identification and Management  
**Secondary contribution:** Methodological Session and bank credit-pricing dynamics

## Abstract

Flood and drought affect Kenyan banks through the economic activities, households, assets and infrastructure that support loan repayment. A flood may damage premises and collateral, interrupt transport and utilities, destroy inventory and delay customer activity. Drought accumulates through rainfall deficit, declining vegetation and water access, reduced crop or livestock production, changing market conditions and weaker household or enterprise income. Existing Kenyan research has demonstrated relationships among climate indicators, sector output, non-performing loans and banking stability. The next opportunity is to determine whether spatially and temporally resolved catastrophe evidence improves risk identification at the exposure level.

This study proposes a Kenya-specific framework for linking point-in-time flood and drought intelligence to borrower, collateral and portfolio credit outcomes. It will compare a transparent conventional credit-risk baseline with a Spatial Catastrophe Risk Intelligence (SCRI) challenger. The baseline will use borrower repayment history, facility characteristics, macroeconomic conditions, sector and coarse geography. The challenger will add hazard intensity, footprint, duration, exposure, vulnerability, insurance, resilience and recovery indicators constructed from authoritative environmental data, earth observation and other governed evidence. The preferred empirical unit is a pseudonymised loan, borrower or collateral observation; a bank–sector–county panel provides an aggregated alternative.

The study will test whether SCRI variables improve out-of-sample calibration, Brier score, log loss, discrimination, lead time and the identification of geographic or sectoral concentration. Flood will support an event-based analysis around one or more well-observed events, while drought will use duration-aware and distributed-lag methods. Where the data supports identification, event-study analysis will examine how exposed and comparable unexposed borrowers differ before and after a hazard. Insurance, verified resilience measures and anticipatory finance will be tested as potential moderators of distress and recovery.

The intended contribution is both empirical and practical. The research will show how physical risk can be linked to probability of default, loss given default, exposure at default, expected credit loss and portfolio stress while preserving the bank’s model governance. It will also examine how the same evidence can support resilience lending, climate-risk disclosure and the monitoring of adaptation outcomes. The result will be a transparent method for evaluating when granular catastrophe intelligence adds decision value to Kenyan banking and where further data, calibration or institutional development is required.

**Keywords:** physical climate risk; credit risk; flood; drought; geospatial data; banking resilience; expected credit loss; resilience finance; Kenya.

## 1. Motivation

On the same morning that floodwater crosses a road or enters a market, several banking variables begin to change. Business revenue may stop, inventory may be damaged, employees and customers may lose access, mobile and power services may weaken, and collateral may require inspection. Repayment stress may appear later, after savings and working-capital buffers are exhausted. During drought, the sequence is slower: rainfall and vegetation deteriorate, water and feed costs rise, livestock or crop production weakens, market behaviour changes, household consumption adjusts and borrowers make increasingly difficult liquidity choices.

The bank rarely observes this full physical and livelihood chain in one place. Conventional credit systems contain rich financial information but may represent climate risk through national weather variables, broad sector classifications, static collateral descriptions or county averages. Environmental institutions, satellites, infrastructure operators and communities observe different parts of the event. SCRI provides a method for converting these observations into time-stamped hazard and exposure variables that can be tested inside familiar credit-risk models.

The research is directly relevant to Kenya’s banking-policy context. CBK’s Guidance on Climate-Related Risk Management encourages institutions to identify material physical risks at portfolio, counterparty and, where appropriate, transaction level, including the locations of business operations and assets, supply-chain disruption and collateral implications [1]. The Kenya Green Finance Taxonomy expects adaptation activities to draw on physical climate-risk and vulnerability assessment, suitable geographic and temporal scales, uncertainty and measurable outcomes [2]. The revised Risk-Based Credit Pricing Model also places the borrower’s risk profile within the premium added to the common reference rate [3]. Together, these developments create a practical need for locally validated physical-risk information.

## 2. Existing evidence and research gap

Kenyan research has already established a strong macro and banking foundation. Kimundi and Wambui analyse temperature, precipitation, sectoral output and a banking-stability index, finding agriculture to be an important physical-risk transmission channel [4]. Odongo, Misati, Kageha and Wamalwa use a dynamic panel of 35 banks and report relationships among rainfall and temperature variability, bank stability and non-performing-loan risk [5]. Wamalwa, Kamau, Odongo and Misati examine bank credit as a factor that can support cereal production and adaptation under climate stress [6].

This paper advances the analysis from national or sector-level climate indicators to the hazard–exposure intersection. It asks whether a flood footprint of a given probability, depth band and duration—or a drought state of a given persistence and livelihood effect—contains information about borrower outcomes beyond existing credit and macroeconomic variables. It also introduces point-in-time control: a feature used for prediction must reflect what was knowable at that moment rather than a later reconstructed account of the event.

The international literature reinforces the need for this step. The Basel Committee notes that physical risk assessment requires granular exposure information, geospatial characteristics, hazard-specific damage relationships and integration with established financial-risk measures [7]. Recent BIS work proposes incorporating a physical-risk factor into credit models and highlights borrower assets, geolocation, hazard probabilities and damage functions as practical inputs [8]. SCRI brings that emerging approach into a Kenya-first empirical design with explicit observation quality, livelihood pathways and resilience interventions.

## 3. Research questions and hypotheses

The primary question is:

> Does the addition of spatially and temporally resolved flood and drought intelligence improve the out-of-sample identification and calibration of climate-related credit risk in Kenyan bank portfolios relative to conventional sectoral, county and macro-climate indicators?

Secondary questions examine transmission channels, the moderating effect of insurance and resilience measures, geographic and borrower heterogeneity, and applications across the credit life cycle.

The study will test:

- **H1:** Adding SCRI flood and drought features improves out-of-sample prediction and calibration of borrower distress relative to a conventional credit-risk baseline.
- **H2:** Hazard intensity, footprint and duration affect credit outcomes through observable cash-flow, downtime, production, access and collateral channels.
- **H3:** Insurance, functioning resilience measures and documented early action reduce conditional severity or shorten recovery time.
- **H4:** Fine-resolution exposure data changes estimated geographic and sectoral concentration relative to county-average climate variables.
- **H5:** Model performance and uncertainty vary by borrower segment and observation coverage, making coverage and subgroup calibration material to implementation.

## 4. Conceptual framework

The proposed causal and predictive chain is:

```{.mermaid #kba-proposal-transmission-framework alt="Physical-to-financial catastrophe transmission framework"}
%%{init: {"theme": "base", "themeVariables": {"background": "#F7FAFC", "primaryTextColor": "#172B4D", "lineColor": "#3B5B92", "fontSize": "17px", "fontFamily": "Arial"}, "flowchart": {"curve": "basis", "nodeSpacing": 38, "rankSpacing": 46}}}%%
flowchart LR
  OBS["Point-in-time observations<br/>rainfall • gauges • satellites<br/>community • institutions"]
  STATE["Hazard state<br/>probability • intensity<br/>footprint • duration"]
  INTERSECT["Exposure and vulnerability<br/>borrower • business • collateral<br/>infrastructure • livelihood"]
  CHANNELS["Economic channels<br/>revenue • production • access<br/>collateral • recovery time"]
  OUTCOME["Credit outcomes<br/>arrears • restructuring • stage migration<br/>default • cure • recovery"]
  CREDIT["Risk representation<br/>PD • LGD • EAD • ECL<br/>portfolio concentration"]
  PROTECTION["Protection and adaptive capacity<br/>insurance • resilient infrastructure<br/>liquidity • early action"]

  OBS --> STATE --> INTERSECT --> CHANNELS --> OUTCOME --> CREDIT
  PROTECTION -. "moderates impact and recovery" .-> CHANNELS

  classDef evidence fill:#DCEEFF,stroke:#2C6E9F,stroke-width:2px,color:#102A43;
  classDef hazard fill:#DFF3E4,stroke:#2F855A,stroke-width:2px,color:#153E2C;
  classDef exposure fill:#FFF1CC,stroke:#B7791F,stroke-width:2px,color:#5F370E;
  classDef finance fill:#E9E1F8,stroke:#6B46A3,stroke-width:2px,color:#32215B;
  classDef outcome fill:#FDE2E2,stroke:#B64B4B,stroke-width:2px,color:#5A1E1E;

  class OBS evidence;
  class STATE hazard;
  class INTERSECT exposure;
  class CHANNELS,CREDIT finance;
  class OUTCOME,PROTECTION outcome;
```

**Figure 1a. SCRI physical-to-financial transmission framework.**

```{.mermaid #kba-proposal-validation-framework alt="Empirical baseline and SCRI challenger validation framework"}
%%{init: {"theme": "base", "themeVariables": {"background": "#F7FAFC", "primaryTextColor": "#172B4D", "lineColor": "#3B5B92", "fontSize": "17px", "fontFamily": "Arial"}, "flowchart": {"curve": "basis", "nodeSpacing": 42, "rankSpacing": 48}}}%%
flowchart LR
  BASE["Transparent baseline<br/>repayment • facility • macroeconomy<br/>sector • coarse geography"]
  SCRI["SCRI challenger<br/>baseline + hazard • exposure<br/>vulnerability • protection • recovery"]
  HOLDOUT["Common holdouts<br/>temporal • geographic • event"]
  METRICS["Performance and value<br/>calibration • Brier • log loss<br/>lead time • concentration"]
  USES["Governed applications<br/>monitoring • collateral review • stress testing<br/>expected loss • resilience finance • disclosure"]

  BASE --> HOLDOUT
  SCRI --> HOLDOUT
  HOLDOUT --> METRICS --> USES

  classDef baseline fill:#E2E8F0,stroke:#4A5568,stroke-width:2px,color:#1A202C;
  classDef challenger fill:#E9E1F8,stroke:#6B46A3,stroke-width:2px,color:#32215B;
  classDef validation fill:#FFF1CC,stroke:#B7791F,stroke-width:2px,color:#5F370E;
  classDef decision fill:#D8F3F0,stroke:#147D78,stroke-width:2px,color:#123C3A;

  class BASE baseline;
  class SCRI challenger;
  class HOLDOUT,METRICS validation;
  class USES decision;
```

**Figure 1b. Empirical test of SCRI’s incremental banking value.**

For borrower or facility i at prediction time t and outcome horizon h, a conventional baseline can be expressed as:

**P(Yᵢ,ₜ₊ₕ = 1) = F(Bᵢ,ₜ, Cᵢ,ₜ, Mₜ, Sᵢ, Gᵢ). (1)**

Here, Y is a defined distress outcome; B is borrower repayment and financial history; C contains facility and collateral characteristics; M represents macroeconomic conditions; S is sector; and G is coarse geography. The SCRI challenger adds point-in-time hazard H, exposure and vulnerability V, and resilience/response R:

**P(Yᵢ,ₜ₊ₕ = 1) = F(Bᵢ,ₜ, Cᵢ,ₜ, Mₜ, Sᵢ, Gᵢ, Hᵢ,ₜ, Vᵢ,ₜ, Rᵢ,ₜ). (2)**

The empirical test is the incremental out-of-sample value of H, V and R. Where the bank maintains independently validated credit components, the financial translation follows:

**ECLᵢ,ₜ = PDᵢ,ₜ × LGDᵢ,ₜ × EADᵢ,ₜ. (3)**

PD, LGD and EAD will be examined separately because flood or drought can influence repayment capacity, collateral recovery and utilisation through different pathways.

## 5. Data

The preferred sample is a pseudonymised panel of loans, borrowers or collateral assets. Outcome variables may include days past due, arrears entry, restructuring, Stage 2 or Stage 3 migration where available, default, cure, write-off, recovery amount and recovery time. Facility variables include origination, maturity, outstanding balance, product, rate structure, collateral, insurance and payment history. Borrower characteristics include sector, type, size and an approved spatial key at the minimum resolution required for hazard linkage.

An aggregated alternative will use bank–sector–county–quarter cells containing credit outstanding, new lending, non-performing loans, provisioning, restructures and pricing where available. A public-data demonstrator can use a transparent synthetic portfolio to establish the method while the empirical partnership is completed.

Flood features may include antecedent and event rainfall, gauge level, radar-derived inundation probability, extent, depth band, duration, road or service disruption and recession time. Drought features may include rainfall deficit, vegetation condition, soil moisture, water-point status, crop or livestock indicators, market access and time spent in each drought state. Candidate sources include KMD, WRA, NDMA, Copernicus Sentinel observations, CHIRPS rainfall, ERA5 reanalysis, county records and governed community evidence. Source, event time, knowledge time, geometry, revision and quality are retained for every feature.

Controls will include the applicable interest-rate benchmark, inflation, exchange-rate or sector-output conditions, facility structure and prior repayment behaviour. Exposure linkage will be performed in a controlled environment, with direct identifiers retained by the participating bank.

## 6. Methodology

The baseline model will be a regularised logistic regression, discrete-time survival model or stage-transition model selected according to the outcome. Its purpose is to establish a credible, interpretable credit benchmark. The SCRI challenger will add hazard and vulnerability variables and may use hierarchical effects to pool evidence across counties and sectors while retaining local differences.

Flood analysis will use one or more well-observed events. An event-study specification will compare outcome paths for exposures intersecting the hazard footprint with appropriately matched or weighted comparison exposures. Pre-event trends, common support and alternative footprint definitions will be tested. Drought will use distributed lags, duration variables or a state-duration model to capture the gradual accumulation of livelihood and business effects.

The central predictive comparison will use temporal and geographic holdouts. Metrics include calibration intercept and slope, calibration curves, Brier score, log loss, area under the receiver-operating-characteristic curve, sensitivity at a fixed operational review capacity, lead time and stability across borrower groups. The analysis will also measure portfolio concentration and the change in expected loss produced by the additional variables.

Robustness tests will vary flood thresholds, spatial buffers, drought definitions, time lags, missing-location assumptions, event windows and comparison groups. Performance will be reported by sector, county, borrower size and digital-observation coverage. Insurance and verified resilience features will enter as interaction or stratification variables, subject to sufficient sample size and credible implementation records.

The study will distinguish predictive uplift from causal estimates. Predictive validity follows from holdout performance. An avoided-loss or resilience effect will be estimated where a defensible comparison group, intervention timing and pre-intervention record are available.

## 7. Expected contribution and relevance

The paper will contribute a tested way to connect physical catastrophe evidence with established banking-risk concepts. For credit teams, it may improve early identification, review prioritisation, collateral inspection and borrower engagement. For portfolio and risk committees, it may reveal geographic and sectoral concentration and support scenario analysis. For finance and model-risk teams, it can provide transparent evidence for PD, LGD, EAD and expected-loss review. For sustainability teams, it can connect location-specific physical-risk assessment with disclosure and adaptation monitoring.

The resilience-finance contribution is equally practical. A lender considering a water, drainage, transport, agricultural or business-continuity investment can compare baseline and intervention hazard-loss scenarios, test debt-service resilience and track physical performance. Communities may access the resulting asset through utilities, cooperatives, community enterprises, county programmes, insurance or project benefit-sharing structures. The study will examine the evidence required to connect those benefits with a viable repayment or public-finance mechanism.

## 8. Research governance and outputs

The study will use data minimisation, pseudonymisation, role-based access, purpose limitation and documented retention. Research outputs will use aggregation and disclosure-control thresholds appropriate to the dataset. Model validation will include point-in-time integrity, calibration, drift, geographic coverage and subgroup performance. The participating bank remains the owner of its credit policy and customer decisions.

The outputs will be an 8,000–10,000-word KBA-style working paper, a two-page policy brief, a data dictionary, a methodological appendix, a reproducibility statement and a conference presentation. Independent review will cover banking credit risk, econometrics, hazard science, actuarial modelling, data protection and community or financial-inclusion implications.

## References

[1] Central Bank of Kenya, *Guidance on Climate-Related Risk Management*, Oct. 2021. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2021/10/Guidance-on-Climate-Related-Risk-Management.pdf. [Accessed: Sep. 2, 2026].

[2] Central Bank of Kenya, *Kenya Green Finance Taxonomy*, Apr. 2025. [Online]. Available: https://www.centralbank.go.ke/kenya-green-finance-taxonomy-climate-risk-disclosure-framework/. [Accessed: Sep. 2, 2026].

[3] Central Bank of Kenya, *Revised Risk-Based Credit Pricing Model*, Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf. [Accessed: Sep. 2, 2026].

[4] G. Kimundi and R. Wambui, “Climate Change and Banking Sector (In)Stability in Kenya: A Vulnerability Assessment,” KBA Working Paper WPS/03/23, May 2023. [Online]. Available: https://www.kba.co.ke/wp-content/uploads/2023/06/WPS-66-Kimundi.pdf. [Accessed: Sep. 2, 2026].

[5] M. Odongo, R. Misati, C. Kageha and P. Wamalwa, “Sustainable Financing, Climate Change Risks and Bank Stability in Kenya,” KBA Working Paper WPS/08/23, May 2023. [Online]. Available: https://www.kba.co.ke/wp-content/uploads/2023/06/WPS-71-Maureen-et-al.pdf. [Accessed: Sep. 2, 2026].

[6] P. Wamalwa, A. Kamau, M. Odongo and R. Misati, “Does Bank Credit Mitigate Nature and Climate Change Effects in Cereal Production,” KBA Working Paper WPS/07/25, Mar. 2025. [Online]. Available: https://www.kba.co.ke/wp-content/uploads/2025/04/WPS-92-Wamalwa-et-al.pdf. [Accessed: Sep. 2, 2026].

[7] Basel Committee on Banking Supervision, *Climate-Related Financial Risks—Measurement Methodologies*, Apr. 2021. [Online]. Available: https://www.bis.org/bcbs/publ/d518.pdf. [Accessed: Sep. 2, 2026].

[8] V. Pozdyshev, A. Lobanov and K. Ilinsky, “Incorporating Physical Climate Risks into Banks’ Credit Risk Models,” BIS Working Papers No. 1274, Jul. 2025. [Online]. Available: https://www.bis.org/publ/work1274.htm. [Accessed: Sep. 2, 2026].
