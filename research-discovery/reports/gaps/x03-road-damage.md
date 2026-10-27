[← Research candidates](../research-candidates.md)

# Small road-damage detection across countries and annotation variation

**ID:** X03 · **Area:** Computer vision / object detection · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

[Read the visual explanation](../road-damage-visual-note.html): worked box-overlap example, shared contributions and country-held-out evaluation.

## 1. Problem

Road-image detectors lose accuracy across countries and camera conditions. Recent multi-source adaptation and domain-generalisation models already address this transfer problem; aggregate improvements may still hide small-crack misses and sensitivity to box annotation choices.

**Potential stakeholders:** Pavement-inspection teams and road-image model developers.

## 2. Research gap and question

**Tentative gap:** Investigate annotation-tolerant training and source-only reliability under a held-out-country protocol. Real annotation noise is not established by RDD2022; controlled box perturbations must be described as simulations.

**Research question:** Can annotation-tolerant assignment and small-damage training preserve held-out-country recall without relying on target-country labels or adaptation?

**Hypothesis and rival explanation:** A size-aware, box-tolerant objective will improve small-damage recall beyond multi-source empirical risk minimisation. Rival explanation: benefits arise from higher image resolution, country balance or duplicate road frames.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [MSDA-RDD, 2026](https://ieeexplore.ieee.org/abstract/document/11655917) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FTCSVT.2026.3723926) | Multi-source road-damage adaptation, feature alignment and teacher pseudo-labels. | Source-only training and controlled annotation sensitivity need comparison; do not claim cross-scene adaptation is new. | Publisher abstract; full methods not inspected; Abstract (X03-L1) |
| [Multi-Adversarial Metric-Constrained Domain Generalization, 2026](https://www.sciencedirect.com/science/article/pii/S0262885626002805) | Multi-source domain-generalisation for road damage. | A source-only setting alone is insufficient novelty; distinguish the annotation-tolerance and reliability objectives. | Primary indexed publisher sections; methods incomplete; Indexed abstract and dataset sections (X03-L2) |
| [Bridging Data Distribution Gaps, 2024](https://doi.org/10.3390/app142411974) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390%2Fapp142411974) | Test-time adaptation for cross-scenario pavement detection. | Test-time adaptation is an optional comparator, not a required source of target feedback. | Scholarly abstract; methods not inspected; FastTrack X-CV-S3 result (X03-L3) |

[Import these 2 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FTCSVT.2026.3723926,10.3390%2Fapp142411974). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Train a compact detector from generic-image weights. Study box-tolerant target assignment, small-defect consistency and validation-only score calibration. Each method must also run against the same unchanged source-only detector.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [RDD2022 author repository](https://github.com/sekilab/RoadDamageDetector), with country ZIP links, Pascal VOC training labels and a four-class challenge mapping. |
| Access and licence | CC BY-SA 4.0 images. Author README specifies Japan 1,022.9 MB, India 502.3 MB, Czech 245.2 MB and US 423.8 MB ZIPs. These are published sizes; archives not acquired. |
| Evaluation labels | Use country-held-out portions of the labelled training release. Official challenge test images have no public labels and cannot be the core local evaluation. |
| Bounded core / fallback | Japan, India, Czech and US; exclude drone imagery and the much larger Norway archive initially. Reduce source countries or image count while retaining a labelled held-out country. |
| Resources, estimated | Occasional 8–12 GB GPU, 16 GB RAM and 10–25 GB storage for the bounded core. Training time and VRAM unmeasured. |
| Prototype | Road-image boxes and confidence display; no maintenance-priority or safety certification. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: box tolerance | Can training resist plausible bounding-box variation? H: Box-tolerant assignment reduces sensitivity to plausible annotation variation. | Train robust target assignment or localisation loss. | Ordinary assignment; remove perturbation tolerance. | AP and localisation error versus controlled box perturbations. |
| B: small damage | Can size-aware consistency recover small cracks without added pixels? H: Consistency improves small-crack recall without extra pixels. | Train a small-region consistency term. | Same resolution/augmentations; remove size term. | Small-damage recall and false positives. |
| C: transfer confidence | Can source-only calibration flag unreliable target detections? H: Conditional calibration improves selective reliability across countries. | Learn class/size-conditional confidence with held-out source countries. | Global calibration; remove size/country pooling. | Risk–coverage and worst-country reliability. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Macro-average AP50:95 across held-out countries, with small-damage AP and recall reported separately.
- **Split:** Leave one country out; reserve another source grouping for selection. Remove exact/perceptual duplicates across partitions; keep identifiable capture sequences grouped. Unknown route IDs limit route-level claims.
- **Baselines and code:** Faster R-CNN, compact [YOLO11](https://github.com/ultralytics/ultralytics), multi-source training and MAMDG/MSDA-RDD as nearest methods. Do not use an RDD-trained checkpoint on a claimed held-out country.
- **Ablations:** Box tolerance, small-region term and calibration; match country weighting, resolution, optimiser and generic pretraining.
- **Uncertainty and errors:** Multiple training seeds; image/capture-group bootstrap within each country; report country results individually because four countries are too few for precise geographic population inference.
- **Useful result without winning:** Show whether small-crack performance is driven more by resolution, source selection or annotation sensitivity than architecture changes.
- **Interpretation limit:** Artificial box perturbations do not prove genuine annotation error. No deployment or automated road-safety benefit follows from benchmark AP.

## 8. Score and next decision

**Provisional score: 76.7/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 3/5; the required rating is 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Low-medium: cross-country adaptation and generalisation are established; the annotation-tolerance distinction needs full methods checking. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: author releases, country sizes, labels and licence are documented; image decoding and duplicate analysis are pending. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: four small country archives and compact detectors bound the work; transfer-learning skills and runtime need a pilot. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: target assignment, consistency objectives and calibration support model-level experiments. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: labelled country holdouts and matched budgets are objective; capture metadata may be incomplete. |
| Three-member structure | 12 | 4 | 9.6 | Medium: three distinct investigations share one detector and each has a standalone baseline comparison. |
| Real-world significance | 9 | 4 | 7.2 | Medium: cross-country road-image failures are documented; actual inspection cost and safety outcomes are not measured. |
| Compute/storage | 5 | 4 | 4.0 | Medium: bounded archives fit storage and small models fit occasional modest GPU access; workload not timed. |
| Prototype | 3 | 4 | 2.4 | Medium-high: an image-box viewer matches the team's implementation strengths. |
| **Normalised total / 100** | **98** |  | **76.7** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Pass | Section 5 records an original public release or author-documented loading route, existing labels and the access-check limit. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Unknown | The extra value beyond recent source-only domain-generalisation methods is not established. |
| 7. Beyond application assembly | Pass | Section 6 investigates learned interventions with baseline comparisons and ablations, rather than application assembly. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Pass | The bounded core and fallback in Section 5 are plausible within the team window; training costs remain estimates. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Pass | Section 5 records source terms and a bounded offline use; no deployment or high-stakes benefit is assumed. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** A worthwhile vision lead for closer checking; not a qualified novelty claim.

**Next decision point:** Inspect MAMDG and MSDA-RDD methods, verify the challenge label mapping in a small labelled country sample, then time one compact detector. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
