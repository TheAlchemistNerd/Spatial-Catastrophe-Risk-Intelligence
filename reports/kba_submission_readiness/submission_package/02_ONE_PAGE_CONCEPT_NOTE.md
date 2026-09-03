# One-Page Research Concept Note

## Can Spatial Catastrophe Intelligence Improve Bank Credit-Risk Identification in Kenya?

### A flood-and-drought empirical framework

**Author:** Nevil Maloba, Founder, Philtechent LTD  
**Qualification:** BSc Actuarial Science, University of Eldoret  
**Email:** nevillemaloba@gmail.com  
**KBA theme:** Banking Amidst Macroeconomic Policy Reforms: Emerging Risks and Opportunities  
**Primary sub-theme:** Risk Identification and Management  
**Secondary route:** Methodological Session

### The problem

A flood is experienced first as water entering a business, cutting a road, damaging stock or interrupting customers. Drought develops through rainfall deficit, declining vegetation and water access, weaker crop or livestock production, market stress and reduced household income. A bank experiences these physical processes through borrower cash flow, repayment behaviour, collateral condition, restructuring, default, recovery, liquidity and portfolio concentration.

Kenyan banking studies have established that temperature and rainfall variability can affect sector output, non-performing loans and bank stability. Spatial Catastrophe Risk Intelligence (SCRI) extends that work to the event and exposure level. It asks whether a bank can identify emerging credit stress more accurately by knowing the hazard intensity, footprint, duration and recovery conditions affecting a borrower, business location or collateral asset.

### Research question

> Does adding spatially and temporally resolved flood and drought intelligence improve the out-of-sample identification and calibration of climate-related credit risk in Kenyan bank portfolios relative to conventional sectoral, county and macro-climate indicators?

### Contribution

The research creates a point-in-time evidence chain:

```{.mermaid #kba-concept-note-framework alt="Point-in-time catastrophe evidence translated into bank and resilience decisions"}
%%{init: {"theme": "base", "themeVariables": {"background": "#F7FAFC", "primaryTextColor": "#172B4D", "lineColor": "#3B5B92", "fontSize": "16px", "fontFamily": "Arial"}, "flowchart": {"curve": "basis", "nodeSpacing": 34, "rankSpacing": 42}}}%%
flowchart LR
  OBS["Flood and drought evidence<br/>sensors • earth observation • community • institutions"]
  STATE["Probabilistic hazard state<br/>intensity • footprint • duration • confidence"]
  EXP["Borrower, business and collateral exposure<br/>location • sector • vulnerability • dependencies"]
  IMP["Financial transmission<br/>cash flow • production • downtime • collateral • recovery"]
  CREDIT["Credit-risk translation<br/>PD • LGD • EAD • expected loss • concentration"]
  ACTION["Bank and resilience applications<br/>monitoring • stress testing • finance • disclosure"]
  PROTECT["Protection and resilience<br/>insurance • infrastructure • early action • adaptation finance"]

  OBS --> STATE --> EXP --> IMP --> CREDIT --> ACTION
  PROTECT -. "moderates impact and recovery" .-> IMP

  classDef evidence fill:#DCEEFF,stroke:#2C6E9F,stroke-width:2px,color:#102A43;
  classDef hazard fill:#DFF3E4,stroke:#2F855A,stroke-width:2px,color:#153E2C;
  classDef exposure fill:#FFF1CC,stroke:#B7791F,stroke-width:2px,color:#5F370E;
  classDef finance fill:#E9E1F8,stroke:#6B46A3,stroke-width:2px,color:#32215B;
  classDef decision fill:#D8F3F0,stroke:#147D78,stroke-width:2px,color:#123C3A;
  classDef protection fill:#FDE2E2,stroke:#B64B4B,stroke-width:2px,color:#5A1E1E;

  class OBS evidence;
  class STATE hazard;
  class EXP exposure;
  class IMP,CREDIT finance;
  class ACTION decision;
  class PROTECT protection;
```

**Figure 1. Point-in-time catastrophe evidence translated into bank and resilience decisions.**

The study will compare a transparent credit-risk baseline with an SCRI challenger. The baseline uses borrower history, facility terms, macroeconomic variables, sector and coarse geography. The challenger adds point-in-time flood or drought intensity, exposure, vulnerability, insurance, resilience and recovery indicators. Performance will be evaluated using calibration, Brier score, log loss, discrimination, lead time, geographic holdouts and operational value.

### Data route

The preferred unit is a pseudonymised loan, borrower or collateral observation linked through approved geography. Outcomes include days past due, arrears, restructuring, stage migration, default, cure, write-off and recovery. An aggregated bank–sector–county panel provides a second route. A public-data demonstrator using transparent or synthetic banking exposure can establish the method while a partner dataset is secured.

Flood variables may combine rainfall, river levels, radar-derived extent, depth bands, duration and access disruption. Drought variables may combine precipitation deficit, vegetation condition, soil moisture, water-point and crop or livestock indicators, market access and state duration. Every feature will be aligned to the information that was available at the prediction date.

### Banking and resilience relevance

The research can support credit monitoring, geographic and sector concentration, scenario analysis, collateral review, expected credit loss, borrower engagement and climate-risk disclosure. It can also identify where a resilience loan, functioning infrastructure, insurance or anticipatory finance is associated with lower disruption or faster recovery. This connects physical-risk management with investable adaptation while retaining the bank’s established credit governance.

### Intended outputs

The project will deliver a KBA-style empirical working paper, a two-page policy brief, a reproducible methodology, a data dictionary and a conference presentation. The resulting evidence will show where spatial catastrophe variables add predictive value, where uncertainty remains material and how banks can incorporate the information proportionately across the credit life cycle.

### Selected sources

- KBA 2026 Call for Papers: https://www.kba.co.ke/wp-content/uploads/2026/03/KBA-Call-for-Papers-2026-Advert-3.pdf
- CBK Guidance on Climate-Related Risk Management: https://www.centralbank.go.ke/wp-content/uploads/2021/10/Guidance-on-Climate-Related-Risk-Management.pdf
- KBA, *Sustainable Financing, Climate Change Risks and Bank Stability in Kenya*: https://www.kba.co.ke/wp-content/uploads/2023/06/WPS-71-Maureen-et-al.pdf
- KBA, *Climate Change and Banking Sector (In)Stability in Kenya*: https://www.kba.co.ke/wp-content/uploads/2023/06/WPS-66-Kimundi.pdf
- BIS, *Incorporating Physical Climate Risks into Banks’ Credit Risk Models*: https://www.bis.org/publ/work1274.htm
