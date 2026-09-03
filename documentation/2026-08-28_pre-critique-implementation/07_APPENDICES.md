# Part 7: Appendices

## Appendix A: Shared Notation and Definitions

This section standardises the mathematical notation and definitions used across the continuous catastrophe underwriting architecture, ensuring strict consistency whether variables appear in the optical perception model, the hazard state engine, or the financial pricing equations.

### 1. Space and Time Domains
| Symbol | Definition |
| :--- | :--- |
| $t, \Delta t$ | A specific discrete time step (e.g., a day or a remote-sensing orbital pass), and the latency between observation and underwriting action. |
| $s, \mathcal{D}$ | A spatial location or coordinate within the geographic domain, and the complete spatial domain (e.g., a national bounding box). |
| $j, i$ | An index denoting a specific insured property/portfolio risk, and an index denoting a specific catastrophe event. |

### 2. Observation and Perception Layer
| Symbol | Definition |
| :--- | :--- |
| $O_t$ | The raw observation vector at time $t$ (e.g., a satellite image, a YOLO classification, or a crowd report). |
| $R_k, C_t$ | The dynamic reliability score assigned to crowd participant $k$, and the aggregated crowd-sourced evidence vector at time $t$. |
| $V_t$ | The machine-vision output (e.g., a YOLO bounding-box confidence score) at time $t$. |

### 3. Hazard State and Loss Engines
| Symbol | Definition |
| :--- | :--- |
| $H_t$ | The latent physical hazard state at time $t$ (e.g., flood depth, fire perimeter, or drought index). |
| $I(s,t)$ | The conditional physical intensity of the hazard at location $s$ and time $t$. |
| $N_{h,g,t}$ | Event count under a stated period and event definition for hazard $h$ and geometry $g$. |
| $L^{GU}_e, L^{INS}_e$ | Ground-up physical loss for event $e$, and the insured event loss after stated policy terms. |

## Appendix B: Canonical Systems Architecture

The following diagram illustrates the continuous data flow from the raw multi-modal observation layer, through the Bayesian statistical representation, down to the final commercial underwriting logic.

## Appendix C: Mathematical and Statistical Formulations

### 1. Bayesian Observation and State Transitions
The observation model operates across source-specific vectors. The probability of an observation $Y$, given the latent environmental hazard regime $Z$ and source quality $q$, is denoted as:
$$
Y_{s,g,t}\mid Z_{g,t},q_{s,g,t}
\sim p_s\!\left(Y\mid Z_{g,t},q_{s,g,t}\right)
$$
The hazard state transitions dynamically across a physically defensible spatial dependency graph $\mathcal N(g)$ (such as an ecological corridor or upstream river network):
$$
p\!\left(Z_{g,t}\mid Z_{g,t-1},Z_{\mathcal N(g),t-1},X_{g,t}\right)
$$

### 2. Overdispersed Catastrophe Frequency
To account for extreme spatial overdispersion and shifting climate frequency (abandoning strict Poisson limitations), event counts $N_{it}$ are modeled via a Negative Binomial distribution:
$$
N_{it}\sim\operatorname{NegBin}(\mu_{it},\phi)
$$
Where the expected count $\mu_{it}$ is defined by:
$$
\log\mu_{it}
=
\log E_{it}
+\alpha_{c(i)}
+f(\mathbf x_{it})
+\boldsymbol\beta_h^{\mathsf T}\widetilde{\mathbf h}_{it}
+u_i+u_g+u_v+u_t
$$
Here, $E_{it}$ is the earned exposure, $\mathbf x_{it}$ represents approved explicit variables, $\widetilde{\mathbf h}_{it}$ is the residual neural representation (e.g., from Vision Transformers), and the $u$ variables are hierarchical effects for geography, time, and hazard specificities.

### 3. Conditional Severity and Tail Risk
Catastrophic severity is strictly heavy-tailed. Conditional on a positive event occurrence ($N_{it} > 0$), severity $Y_{itk}$ is modeled using a Gamma, Lognormal, or Generalized Pareto Distribution (GPD) framework:
$$
Y_{itk}\mid N_{it}>0
\sim
F_{+}\left(\mu^{\mathrm{sev}}_{it},\vartheta\right)
$$
$$
\log\mu^{\mathrm{sev}}_{it}
=
\delta_{c(i)}
+g(\mathbf w_{it})
+\boldsymbol\gamma_h^{\mathsf T}\widetilde{\mathbf h}_{it}
+v_g+v_v+v_t
$$

### 4. Pure Premium and Aggregate Loss
The expected pure premium ($PP_{it}$) dynamically synthesizes frequency and severity across the continuous hazard state:
$$
PP_{it}
=
E_{it}\lambda_{it}\mu^{\mathrm{sev}}_{it}
$$
Ultimately, the physical ground-up event-loss ($L^{GU}_e$) resolves by intersecting the modeled spatial intensity $I_{e,h}(g_i)$ with the exposure value $V_i$ and its mean damage ratio (MDR):
$$
L^{GU}_e
=
\sum_{i\in\mathcal E_e}
V_i\,MDR_h\!\left(I_{e,h}(g_i),A_i\right)
$$