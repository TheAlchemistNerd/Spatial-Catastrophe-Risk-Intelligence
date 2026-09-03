# Hazard Coverage Matrix

This matrix is both a design control and final acceptance test. `Required` means the manuscript must contain substantive treatment, not a passing mention.

| Layer | Flood | Drought | Wildfire/rangeland fire | Locust/crop pests | Landslide | Severe storm/heat |
|---|---|---|---|---|---|---|
| Human and institutional narrative | Required | Required | Required | Required | Required | Required |
| Authoritative observations | KMD/WRA/county | KMD/NDMA/WRA | KMD/KFS/county | PP&FSD/FAO/county | KMD/county/road/environment bodies | KMD/health/county |
| Community observations | Water depth, access, damage | Water, livestock, pasture, markets | Smoke, flame, perimeter, access | Swarm, crop stage, damage | Cracks, movement, blockage | Wind, hail, heat stress, outage |
| EO/AI perception | SAR/segmentation | Vegetation/soil/time series | Thermal/smoke/fire segmentation | Detection/movement/crop condition | InSAR/change/terrain | Nowcast/damage/heat surface |
| Machine-perception adapter | Water surface, passability, waterline, depth evidence and affected objects | Protocol-led crop, water, livestock and asset condition | Edge smoke/flame cue, temporal masks, thermal evidence and perimeter | Survey detection/counting, lifecycle, tracking and crop condition | Pre/post change, scar/debris segmentation, blockage and bounded OBB | Roof/tree/pole damage; visible heat-vulnerability attributes |
| Perception model portfolio | YOLO/RT-DETR objects; semantic/instance segmentation; transformer/geospatial challengers | Field-vision models plus EO/time-series state engine | Compact edge baseline plus contextual ViT and temporal segmentation challengers | Detection/tracking baseline plus open-vocabulary discovery | Segmentation/change baseline plus transformer and InSAR interfaces | OBB/segmentation for storm damage; heat remains sensor/time-series led |
| Perception uncertainty | Boundary, georeferencing, camera scale, cloud/SAR artefacts | Sampling, representativeness, protocol, season and domain shift | Smoke/cloud/dust ambiguity, night, wind, camera motion | Occlusion, survey area, scale, lifecycle class and sampling | Co-registration, parallax, shadow, local support and sparse labels | Pre-existing damage, view quality, heat-vulnerability interpretation |
| Temporal character | Rapid/episodic | Slow/persistent | Ignition/spread | Lifecycle/mobile | Threshold/rapid movement | Short extreme/persistent heat |
| Spatial topology | Basin/upstream/drainage | Livelihood/ecological zones | Fuel/topography/wind | Transboundary corridor | Slope/catchment/road | Weather field/urban heat |
| Transparent baseline | Threshold/hydrology | Standard indices/phases | Fire-danger/detection | Surveillance/lifecycle | Susceptibility + rainfall threshold | Official forecast/threshold |
| Advanced challenger | State-space/network | HSMM/HMM | Spread/state-space | Movement/state model | Spatial survival/classifier | Spatiotemporal extremes |
| Observation process | Gauge freshness, acquisition, connectivity and flood-dependent reporting | Access, monthly sampling, connectivity and slow reporting | Camera coverage, visibility, field access and copied alerts | Surveillance effort, field access, campaign and transboundary reporting | Access/communications failure and post-event ascertainment | Station/camera coverage, outage and health/infrastructure reporting |
| Posterior-to-loss path | Sampled depth/extent/duration through exposure and terms | Sampled persistent states through livelihood/agricultural vulnerability | Sampled ignition/spread/intensity through property/ecosystem exposure | Sampled density/movement/control through crop stage and yield | Sampled local footprint/blockage through assets and network loss | Sampled intensity/persistence through property, crop, health and service effects |
| Exposure | Buildings, roads, crops, people | Livelihoods, livestock, crops, water | Forests, homes, utilities, ecosystems | Crops, food systems, livelihoods | People, roads, buildings | People, crops, roofs, power |
| Vulnerability | Depth-damage/coping | Sensitivity/adaptive capacity | Fuel/structure/response | Crop stage/control access | Slope/building/access | Health/building/crop sensitivity |
| Loss and tails | Direct/BI/claims/fiscal | Cumulative livelihood/agricultural | Heavy-tail property/ecosystem | Yield/control/livelihood | Local severe/transport cascade | Health/crop/property/outage |
| Reserve and capital relevance | Event nowcast, IBNR/IBNER, occurrence/aggregate capital and liquidity | Agricultural/index emergence, livelihood protection and cross-peril capital | Claims emergence, accumulation, reinsurance and compound drought/fire capital | Seasonal crop emergence, basis risk and public/agricultural layers | Sparse severe claims, infrastructure interruption and accumulation | Property/agriculture emergence and compound outage/market stress |
| Insurance use | Property/agriculture/parametric | Livestock/crop/index | Property/forestry | Crop/meso protection | Property/engineering | Agriculture/property/health riders |
| Finance use | Resilient infrastructure | Water/rangeland/adaptive protection | Detection/restoration | Surveillance/control capacity | Slope/road resilience | Cooling/grid/crop resilience |
| Four-ledger application | Baseline loss, drainage/road intervention, financing and event MRV | Livelihood/water baseline, intervention life, repayment/public benefit and outcome MRV | Detection/fuel/access investment, residual risk, insurance link and MRV | Surveillance/control investment, beneficiaries, blended finance and verified outcomes | Road/slope works, service continuity, finance terms and post-rainfall MRV | Roof/grid/cooling adaptation, cash-flow continuity, finance and performance MRV |
| Basis/failure case | Gauge/footprint mismatch | Index/livelihood mismatch | Detection false alarm | Report/control lag | Sparse labels | Station/impact mismatch |
| Governance | Alert/claims/data | Phase/action/data | Fire authority/safety | Control/environment/transboundary | Warning/evacuation/land use | Alert/health/workplace |

## Cross-hazard cascades to test

1. Drought dries fuels, elevating wildfire risk and reducing firefighting water.
2. Severe rainfall produces flood and rainfall-induced landslide in the same event window.
3. Flood interrupts roads, power, health, water, markets, and claims access.
4. Drought changes vegetation and food systems, affecting locust susceptibility and livelihood vulnerability.
5. Heat compounds drought, health stress, power demand, crop loss, and fire danger.
6. Response to one hazard can move exposure or vulnerability elsewhere; maladaptation must be tested.
