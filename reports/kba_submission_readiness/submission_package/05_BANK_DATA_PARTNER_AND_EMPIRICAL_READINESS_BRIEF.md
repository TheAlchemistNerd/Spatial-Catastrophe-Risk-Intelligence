# Bank Data-Partner and Empirical Readiness Brief

## Purpose

This brief defines the minimum partnership and data conditions needed to test whether Spatial Catastrophe Risk Intelligence improves flood- and drought-related credit-risk identification in Kenya. It is designed for an initial discussion with a bank, KBA, a research institution or a regulated data host. It supports research design and does not request direct customer identifiers.

## Proposed study decision

The research will compare:

- a transparent baseline using existing borrower, facility, macroeconomic, sector and coarse-geography variables; and
- an SCRI challenger that adds point-in-time flood or drought hazard, exposure, vulnerability, insurance, resilience and recovery variables.

The primary test is whether the challenger improves out-of-sample calibration and useful early identification of a defined credit outcome. The partner and research team will select one primary outcome and horizon before model estimation.

## Preferred unit and sample

The preferred analytical unit is a pseudonymised facility–month or facility–quarter observation. Borrower- or collateral-level panels are also suitable. A viable sample should cover at least one well-observed flood period, a meaningful drought progression, adequate pre-event repayment history and sufficient post-event outcome time. The final sample size will be determined through an event-overlap and outcome-incidence study.

An aggregated route can use bank–sector–county–quarter cells. This route should preserve enough variation to compare affected and less-affected locations and distinguish acute flood from persistent drought.

## Minimum banking fields

| Field family | Preferred variables | Research purpose |
|---|---|---|
| Keys and time | Pseudonymous borrower and facility keys; observation date; origination; maturity; closure | Panel construction and censoring |
| Exposure | Outstanding balance, undrawn commitment where relevant, currency, product, repayment schedule | EAD and facility controls |
| Performance | Instalment due/paid, days past due, arrears balance, stage, restructure, default, write-off, cure | Credit outcomes and transitions |
| Recovery | Recovery amount and date, enforcement stage, time to resolution | LGD and recovery-time analysis |
| Pricing | Reference rate, customer premium, fees, repricing dates where approved | Secondary pricing analysis |
| Borrower | Sector, legal form, enterprise size, income or turnover band, livelihood/business type | Transmission and heterogeneity |
| Location | Approved coordinates, grid, ward, postal/branch or county key for business and collateral | Hazard linkage |
| Collateral | Type, valuation date and amount, location, insurance and post-event reassessment | LGD and impairment channel |
| Protection | Relevant insurance, guarantee, relief, moratorium or resilience measure | Moderation and recovery |
| Operations | Branch/service disruption where available | Bank operational channel |

Direct names, national identity numbers, telephone numbers and account numbers are outside the research extract. The partner can create stable pseudonymous keys and perform sensitive linkage inside its controlled environment.

## Hazard and contextual fields

Flood variables will be constructed at the approved exposure location and time: rainfall accumulation, rainfall anomaly, river or drainage level where available, inundation probability, footprint intersection, depth band, duration, road or service disruption, confidence and source quality.

Drought variables will include rainfall deficit, vegetation condition, soil moisture, water-point status, crop or livestock condition where available, market-access signal, declared or modelled state, duration and trend. The analysis will preserve the difference between an authoritative drought phase and a model-derived feature.

Macroeconomic controls can include inflation, exchange-rate conditions, sector output, applicable interest-rate benchmark and county economic indicators. The data dictionary will state the unit, spatial resolution, frequency, release lag, revision treatment and permissible use of each variable.

## Proposed outcomes

The partner should select one primary outcome based on operational relevance and data quality:

1. entry into a specified days-past-due threshold within three or six months;
2. Stage 1 to Stage 2/3 migration within a defined horizon;
3. restructuring or moratorium following flood or drought exposure;
4. regulatory or internal default;
5. cure within a defined period after distress; or
6. realised recovery severity or recovery time for collateralised exposures.

Secondary outputs can include expected credit loss, exposure concentration, affected collateral, review prioritisation and lead time. Each outcome will use the bank’s documented definition and effective dates.

## Study design and validation

The initial descriptive phase will measure event overlap, missing geography, outcome incidence, sector composition and exposure concentration. The baseline and SCRI challenger will then use the same training and holdout samples. Temporal holdouts test performance on later events; geographic holdouts test transport to locations not used for fitting.

Core metrics are calibration intercept and slope, calibration curves, Brier score, log loss, discrimination, sensitivity at a defined review capacity and lead time. The study will show whether a performance change is statistically and operationally meaningful. PD, LGD and EAD will be modelled or evaluated separately before combining them as:

**ECLᵢ,ₜ = PDᵢ,ₜ × LGDᵢ,ₜ × EADᵢ,ₜ. (1)**

An event-study or matched comparison may estimate flood effects when affected and comparison exposures have credible pre-event similarity. Drought analysis will use duration and lag structures. Resilience and insurance effects will be estimated where intervention timing, coverage and implementation are sufficiently documented.

## Data protection and operating model

Before data movement, the parties should agree:

- research purpose, lawful basis and approved uses;
- data controller, processor, steward, model owner and publication owner roles;
- minimum geography and aggregation required;
- linkage procedure and whether analysis stays inside the bank or a trusted environment;
- role-based access, encryption, logging and incident process;
- retention, deletion and derived-data treatment;
- publication disclosure controls and minimum cell sizes;
- customer and geographic fairness review; and
- ownership and permitted use of code, features, trained parameters and research outputs.

The analysis should begin with a privacy-preserving feasibility table rather than a complete data transfer. The table can show counts by month, sector, geography, product and outcome without revealing identities.

## Feasibility questions for the first partner meeting

1. Which credit-risk outcome is most valuable and consistently recorded?
2. What spatial keys exist for borrowers, businesses and collateral, and at what historical quality?
3. Which flood and drought periods overlap the usable loan history?
4. Can insurance, guarantees, restructures and resilience measures be identified?
5. Can linkage and modelling occur within the bank’s environment?
6. Which committees own research approval, model validation, data protection and publication review?
7. What results may be published, aggregated or shared with KBA?
8. Which decision would the bank pilot if the challenger improves calibration or lead time?

## Partnership outputs

The research partnership will produce:

- signed study scope and governance schedule;
- data dictionary and point-in-time feature catalogue;
- sample and event-overlap feasibility report;
- baseline and challenger model cards;
- validation and subgroup-calibration report;
- KBA Working Paper and policy brief;
- bank-specific confidential findings; and
- an implementation recommendation tied to evidence.

## Go-forward gate

The empirical study begins when the partner confirms a defined outcome, usable time history, sufficient spatial linkage, at least one flood and one drought exposure window, an approved research environment and a publication route. A public-data demonstrator can proceed in parallel and will remain clearly labelled until partner outcomes support empirical conclusions.

