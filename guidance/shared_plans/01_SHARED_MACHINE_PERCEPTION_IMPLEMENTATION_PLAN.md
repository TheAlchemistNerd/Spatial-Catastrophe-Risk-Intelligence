# Shared Machine-Perception Implementation Plan

> **Status:** Shared project plan. The evaluation and implementation language below is preserved almost verbatim from the source assessment, with Markdown structure and tables normalised for project use.

## 1. Implementation status

The [implementation plan (line 1)](/C:/Users/Nevo/Downloads/Spatial Catastrophe Risk Intelligence/guidance/ULTRALYTICS_AND_VISION_TRANSFORMER_IMPLEMENTATION_PLAN.md:1) targets approximately 8,000–8,500 substantive words for Part 2. The current [Part 2 (line 1)](/C:/Users/Nevo/Downloads/Spatial Catastrophe Risk Intelligence/manuscripts/02_CROWD_AI_AND_OBSERVATION_ARCHITECTURE.md:1) contains approximately 1,592 words under the Pandoc plain-text count.

| Planned capability | Current status |
|---|---|
| Detection, instance segmentation and semantic segmentation | Present at introductory level |
| Confidence versus hazard probability | Present and conceptually sound |
| Model cards and event/geography holdouts | Present at summary level |
| Hybrid edge/cloud design | Present |
| Crowd duplication and propagation control | Present |
| Privacy and safe degradation | Present |
| Ultralytics as the broader workbench | Mentioned once, not developed |
| Explicit Vision Transformer strategy | Absent |
| RT-DETR challenger | Absent |
| SAM/SAM 2 promptable segmentation | Absent |
| ViT, Swin or SegFormer model roles | Absent |
| Multi-object and mask tracking | Absent |
| Oriented bounding boxes | Absent |
| Pose estimation | Absent |
| Monocular depth workflow | Only a caution about depth, not a capability design |
| Open-vocabulary perception | Absent |
| Kenyan dataset and annotation programme | Absent |
| Active learning | Absent |
| Model-agnostic perception-result contract | Absent |
| Hardware/export benchmarking | Absent |
| Licensing and dependency treatment | Absent |
| Perception-to-actuarial worked example | Absent |
| Product-interface narratives for perception | Absent |
| Supporting source and claim-register entries | Absent |

Therefore, the plan remains a valid implementation specification rather than a completed manuscript revision.

The preservation approach should be:

- Retain the present Part 2 opening and observation architecture.
- Retain the existing detection/segmentation distinction.
- Expand around those passages rather than replacing the chapter wholesale.
- Add the model portfolio, Kenyan data programme, uncertainty treatment and product narratives as deeper layers of the same story.
- Snapshot all manuscripts before implementation and record additions in the validation log.

## 2. Machine-perception evaluation

### What is already strong

The current paper makes several important distinctions correctly:

- A gauge measurement, satellite-derived mask, photograph and crowd report are treated as different evidence types.
- Detection boxes remain object observations; segmentation masks can become spatial surfaces after geospatial processing.
- Perception confidence remains separate from catastrophe probability.
- Flood depth is not inferred automatically from a water mask.
- Crowd repetition is separated from independent corroboration.
- Model outputs preserve time, geometry, provenance and model lineage.
- Edge and cloud processing have different operational roles.

Those foundations should remain. They prevent the expanded machine-perception section from becoming a catalogue of AI models.

### The required product architecture

The chapter should implement a complete perception chain:

```text
Raw image, video, drone or satellite scene
        ↓
Sensor, metadata and image-quality validation
        ↓
Task-specific perception model
        ↓
Boxes, masks, tracks, keypoints, depth or scene classes
        ↓
Calibration, georeferencing and geometry uncertainty
        ↓
Human review or independent corroboration
        ↓
Model-agnostic perception observation
        ↓
Probabilistic catastrophe-state inference
        ↓
Exposure, vulnerability and actuarial loss
```

Ultralytics currently documents detection, segmentation, semantic segmentation, depth estimation, classification, pose and OBB tasks, together with RT-DETR, SAM-family models, YOLO-World and YOLOE. The manuscript should describe these as current examples behind a version-neutral interface, since individual model versions will change faster than the book. Ultralytics task documentation, supported model families.

### Capability refinements

#### Detection

Use for countable, bounded objects: vehicles, livestock, people, locusts, flames, road obstructions and damaged components. Report class-specific recall and calibration, particularly where missing one object has a different cost from generating a false alarm.

#### Instance and semantic segmentation

Use instance masks for individual buildings, roofs, crop plots or isolated damage regions. Use semantic segmentation for continuous water, burn, vegetation or debris surfaces.

The chapter should explain the conversion from pixel mask to physical quantity:

1. Georeference or orthorectify the image.
2. Preserve pixel and boundary uncertainty.
3. Convert the mask to area or geometry.
4. Reconcile sensor resolution with exposure resolution.
5. Pass a probability surface—not merely a hard polygon—to state inference.

#### Tracking

Tracking is valuable but requires careful physical interpretation:

- Tracking a vehicle through floodwater is a temporal object-association problem.
- Tracking a smoke plume is better treated through temporal segmentation, optical flow or advection modelling than through a conventional rigid-object tracker.
- Tracking close-range locusts does not establish regional swarm movement.
- Camera motion must be separated from physical movement.

Multiple frames from one camera or drone flight should enter as a correlated evidence sequence, not hundreds of independent observations.

SAM 2 provides a useful candidate for promptable image and video segmentation, but its outputs still require Kenyan domain validation. SAM 2 paper.

#### Oriented bounding boxes

OBB is appropriate for bounded rotated objects such as roofs, vehicles, fallen poles or particular aerial infrastructure. Roads, floodplains, fields and irregular landslide scars are usually represented more faithfully through polylines, polygons or segmentation.

#### Monocular depth

Monocular depth should provide relative geometry or provisional metric evidence. A defensible flood-depth estimate normally requires some combination of:

- Camera calibration.
- Known reference objects.
- Terrain elevation.
- Waterline detection.
- Gauge observations.
- Hydraulic constraints.
- Uncertainty from scale and camera position.

The output contract should distinguish relative depth from metric water depth.

#### Pose estimation

Pose can support bounded rescue-assistance workflows, such as identifying a potentially fallen or signalling person. Its treatment should include necessity, image quality, occlusion, consent, human confirmation and a narrow permitted purpose. It should remain a specialised capability rather than a prominent catastrophe-loss feature.

#### Open-vocabulary and promptable perception

These are excellent discovery and annotation tools:

- Open-vocabulary models can search for an emerging damage concept.
- SAM-family models can accelerate mask creation.
- Analysts can identify Kenyan classes missing from the production taxonomy.

Their unverified outputs should enter a candidate-review queue. A recurrent concept becomes production evidence after taxonomy definition, annotation and closed-set validation.

#### Vision Transformers

Vision Transformers should remain. Their strongest candidate roles are:

- Contextual scene classification.
- Semantic segmentation.
- High-resolution aerial and satellite interpretation.
- Pre/post-event change detection.
- Promptable segmentation.
- Open-vocabulary perception.
- Global contextual discrimination between smoke, cloud, dust and haze.

Compact YOLO-family models remain strong edge candidates; RT-DETR, ViT, Swin, SegFormer and SAM-family models become challengers where context or promptability may add value. This is a portfolio strategy, not a permanent choice between YOLO and transformers.

### Missing geospatial considerations

The expanded section must also acknowledge that catastrophe imagery is more than ordinary RGB photography:

- Sentinel-1 SAR requires speckle, backscatter and acquisition-geometry treatment.
- Multispectral imagery carries bands beyond RGB.
- Pre/post-event comparison requires co-registration and sensor harmonisation.
- Drone imagery may require camera calibration, mosaicking and orthorectification.
- Ground sample distance determines the smallest defensible observation.
- Cloud, shadow, smoke, glare and vegetation can generate peril-specific errors.

The Ultralytics workbench can serve many visual tasks, while specialised geospatial and remote-sensing models continue behind the common interface.

### Perception uncertainty

The current chapter discusses calibration but should explicitly separate:

- **Aleatoric uncertainty:** ambiguity inherent in smoke, water boundaries, darkness or occlusion.
- **Epistemic uncertainty:** limited Kenyan training examples or unfamiliar construction types.
- **Domain-shift uncertainty:** new county, sensor, season or viewing geometry.
- **Annotation uncertainty:** disagreement over the correct mask or damage class.
- **Geometric uncertainty:** pixel-to-world projection, coordinate accuracy and raster resolution.
- **Operational uncertainty:** dropped frames, compression, stale imagery or partial uploads.

Calibrated probabilities, ensembles and conformal prediction can be evaluated. Recent work has extended conformal uncertainty sets to instance segmentation, although coverage assumptions must be checked under event and geographic shift. Conformal prediction sets for instance segmentation.
