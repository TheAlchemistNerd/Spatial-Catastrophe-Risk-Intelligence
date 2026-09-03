# Hazard Coverage Matrix

This matrix is both a design control and final acceptance test. `Required` means the manuscript must contain substantive treatment, not a passing mention.

| Layer | Flood | Drought | Wildfire/rangeland fire | Locust/crop pests | Landslide | Severe storm/heat |
|---|---|---|---|---|---|---|
| Human and institutional narrative | Required | Required | Required | Required | Required | Required |
| Authoritative observations | KMD/WRA/county | KMD/NDMA/WRA | KMD/KFS/county | PP&FSD/FAO/county | KMD/county/road/environment bodies | KMD/health/county |
| Community observations | Water depth, access, damage | Water, livestock, pasture, markets | Smoke, flame, perimeter, access | Swarm, crop stage, damage | Cracks, movement, blockage | Wind, hail, heat stress, outage |
| EO/AI perception | SAR/segmentation | Vegetation/soil/time series | Thermal/smoke/fire segmentation | Detection/movement/crop condition | InSAR/change/terrain | Nowcast/damage/heat surface |
| Temporal character | Rapid/episodic | Slow/persistent | Ignition/spread | Lifecycle/mobile | Threshold/rapid movement | Short extreme/persistent heat |
| Spatial topology | Basin/upstream/drainage | Livelihood/ecological zones | Fuel/topography/wind | Transboundary corridor | Slope/catchment/road | Weather field/urban heat |
| Transparent baseline | Threshold/hydrology | Standard indices/phases | Fire-danger/detection | Surveillance/lifecycle | Susceptibility + rainfall threshold | Official forecast/threshold |
| Advanced challenger | State-space/network | HSMM/HMM | Spread/state-space | Movement/state model | Spatial survival/classifier | Spatiotemporal extremes |
| Exposure | Buildings, roads, crops, people | Livelihoods, livestock, crops, water | Forests, homes, utilities, ecosystems | Crops, food systems, livelihoods | People, roads, buildings | People, crops, roofs, power |
| Vulnerability | Depth-damage/coping | Sensitivity/adaptive capacity | Fuel/structure/response | Crop stage/control access | Slope/building/access | Health/building/crop sensitivity |
| Loss and tails | Direct/BI/claims/fiscal | Cumulative livelihood/agricultural | Heavy-tail property/ecosystem | Yield/control/livelihood | Local severe/transport cascade | Health/crop/property/outage |
| Insurance use | Property/agriculture/parametric | Livestock/crop/index | Property/forestry | Crop/meso protection | Property/engineering | Agriculture/property/health riders |
| Finance use | Resilient infrastructure | Water/rangeland/adaptive protection | Detection/restoration | Surveillance/control capacity | Slope/road resilience | Cooling/grid/crop resilience |
| Basis/failure case | Gauge/footprint mismatch | Index/livelihood mismatch | Detection false alarm | Report/control lag | Sparse labels | Station/impact mismatch |
| Governance | Alert/claims/data | Phase/action/data | Fire authority/safety | Control/environment/transboundary | Warning/evacuation/land use | Alert/health/workplace |

## Cross-hazard cascades to test

1. Drought dries fuels, elevating wildfire risk and reducing firefighting water.
2. Severe rainfall produces flood and rainfall-induced landslide in the same event window.
3. Flood interrupts roads, power, health, water, markets, and claims access.
4. Drought changes vegetation and food systems, affecting locust susceptibility and livelihood vulnerability.
5. Heat compounds drought, health stress, power demand, crop loss, and fire danger.
6. Response to one hazard can move exposure or vulnerability elsewhere; maladaptation must be tested.

