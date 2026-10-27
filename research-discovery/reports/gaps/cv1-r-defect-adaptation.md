[← Research candidates](../research-candidates.md)

# Learning when to adapt an industrial defect detector

**ID:** CV1-R · **Area:** Computer vision / anomaly detection / adaptation · **Status:** Verify data and gap

**Evidence reviewed:** 27 October 2026

## 1. Problem

Changes in lighting or viewpoint can make normal products look defective to a visual inspection model. Adapting to incoming images may reduce false alarms, but can also absorb actual defects into the model's normal reference.

The project would investigate this trade-off on existing labelled datasets, without claiming validated factory safety or deployment benefit.

## 2. Research gap and question

**Established:** few-image calibration under distribution shift and contamination sensitivity have already been studied.

**Gap to investigate:** learning when and where to adapt from an unverified batch while retaining evidence of small defects.

**Research question:** Can a learned reliability gate avoid harmful feature corrections and preserve defect localisation when an incoming batch contains both shifted normal images and defects?

**Novelty status:** unresolved. Repeating a contamination sweep or adding a routine gating module is insufficient.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [SPARC, August 2026](https://arxiv.org/html/2608.18585v1) | Few-normal-image shift calibration and contaminated-support experiments | Learned adaptation decisions using unverified batches | Full text |
| [AnomalyDINO, 2024 / WACV 2025](https://arxiv.org/html/2405.14529v1) | Strong small-backbone, few-shot patch matching | Adaptation reliability rather than another backbone or memory tweak | Full text |
| [AeBAD and reconstruction baseline, 2023](https://arxiv.org/html/2304.02216v1) | Real lighting/view shifts and a learned response | Choosing whether correction is beneficial | Full text |
| [IM-IAD, 2024](https://doi.org/10.1109/TCYB.2024.3357213) | Few-shot, noisy-supervision and efficiency benchmarking | A distinct method and controlled adaptation decision | Abstract |

SPARC explicitly leaves calibration from an unfiltered stream unevaluated. That limitation motivates investigation; it does not establish originality for the proposed gate.

SPARC also identifies a specific harm mechanism: feature removal can suppress intrinsic normal variation or defect signal. Whether a trained gate prevents that harm remains an untested hypothesis.

## 4. Proposed approach

Use a fixed anomaly detector and small pretrained feature encoder. Investigate support-image weighting, a defect-preserving feature correction and a learned option to decline adaptation.

Train the small components on separate auxiliary products. Evaluate each independently against the same unchanged detector before combining them.

## 5. Data and resources

| Item | Current position |
|---|---|
| Real-shift data | [MVTec AD 2](https://www.mvtec.com/research-teaching/datasets/mvtec-ad-2) and [AeBAD](https://github.com/zhangzilongc/MMR) |
| Auxiliary/fallback data | [VisA](https://github.com/amazon-science/spot-diff): images, labels, masks and documented S3 download |
| Verified access | Source pages, documented download routes and licence terms inspected |
| Payload access | Real-shift image archives not acquired or inspected |
| Licences | MVTec AD 2: CC BY-NC-SA 4.0; AeBAD and VisA: CC BY 4.0 |
| Compute | Frozen small encoder, capped feature memories and small learned heads |
| Fallback | Selected products and a small backbone; synthetic shifts only support a narrower corruption study |
| Unverified | Archive sizes, image loading, feature-extraction cost and full training workload |

MVTec AD 2 has public and private test portions; the core evaluation must use available public labels. The datasets do not establish genuine production chronology, so constructed batches must be described as simulations.

MVTec AD 2 documents eight scenarios and over 8,000 images; its download form was not submitted. VisA documents 10,821 images, masks and split CSVs, but does not replace real lighting-shift validation. The AeBAD shared archive was not inspected. Image decoding, extraction time and peak memory remain unmeasured.

**Prototype:** local image inspection with defect heatmaps and the adaptation decision. A full high-resolution segmentation study must not be assumed CPU-cheap.

## 6. Three-member contributions

| Member | Research question | Method investigation | Assessable result |
|---|---|---|---|
| A: support selection | Can learned support weights resist contaminated calibration images? | Feature-based selector compared with trimming and robust estimation | Sensitivity to contamination and normal diversity |
| B: representation | Can small corrections preserve defect evidence? | Compact adapter with a defect-preservation objective | Localisation performance by defect size and shift |
| C: adaptation decision | Can a model predict when adaptation is harmful? | Risk/benefit predictor with a no-adaptation option | Decision quality and regret versus never adapting |

The selector and decision gate may overlap. Specify contribution-specific experiments and ablations so each member's work is independently assessable within the shared detector. Shared components are acceptable; separate projects or papers are not required.

## 7. Evaluation

- **Primary metric:** per-category localisation average precision under predefined shift and contamination settings.
- **Secondary metrics:** image AUROC, AU-PRO, small-defect recall and false alarms at preselected thresholds.
- **Baselines:** simple texture/image anomaly model, PatchCore, AnomalyDINO and the closest shift-calibration method.
- **Split:** different auxiliary products for learning/selection and final testing; disjoint calibration and query images, grouped by capture/scene where metadata permits.
- **Ablations:** support weighting, defect-preservation objective and adaptation gate.
- **Stress tests:** multiple shifted batches with 0/8, 1/8, 2/8 and 4/8 contaminated support images.
- **Uncertainty:** repeated batch selections and category-clustered confidence intervals.
- **Useful negative result:** establish when adaptation harms localisation or cannot outperform declining adaptation.

The evaluator may use labels to construct contamination scenarios; the method must not receive those labels.

Match encoder, image resolution, feature-memory budget and support access when comparing methods. Include never-adapt and unconditional-correction controls. Select operating thresholds without final-test labels; good ranking metrics alone do not establish a reliable threshold.

## 8. Score and next decision

**Provisional score: 67.3/100.** Scored for comparison at the team's request before gate clearance. Gates 4, 6, 7, 9 and 10 remain Unknown; this is not a qualified shortlist score. Overall assessment confidence is low because dataset payloads, training cost and the methodological distinction remain unverified.

### Weighted rubric

Scoring updated: **28 October 2026**. The nine weights total **98**; weighted points below are out of 98 and the total is normalised to 100.

Ratings assess the current proposal using the module's revised nine-category rubric. Unknowns reduce the relevant ratings; they are not assumed to pass. The team-structure concern is overlap between contributions, not a requirement for separate projects or papers.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---:|---:|---:|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Medium-low: SPARC documents the unfiltered-stream limitation and correction harm in section 3, but a distinct learned gate or correction method is not yet established |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium-low: section 5 documents real-shift benchmarks, public-label portions and licences; suitable image payload access and loading are not verified |
| Feasibility and learning curve | 14 | 3 | 8.4 | Low: frozen features bound the proposal, but patch-level adaptation, auxiliary-product training and resolution choices need a workload pilot |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: learned support weighting, a defect-preserving objective and adaptation decisions offer model-level investigations; distinct novelty remains unresolved |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: section 7 defines disjoint support/query batches, matched budgets, contamination controls and category uncertainty; capture grouping depends on accessible metadata |
| Three-member structure | 12 | 3 | 7.2 | Medium-low: section 6 connects all three to one detector, but support selection and the adaptation decision still overlap; attributable comparisons need clarification |
| Real-world significance | 9 | 4 | 7.2 | Medium: section 3 documents lighting/view failures and loss of defect signal in industrial inspection; benchmark improvements would not establish factory safety |
| Compute/storage | 5 | 3 | 3.0 | Low: cached small-encoder features and selected products are plausible, but high-resolution extraction, memory and archive sizes remain unmeasured |
| Prototype | 3 | 4 | 2.4 | Medium-high: local image input, heatmaps and an adaptation decision form a bounded demonstration |
| **Normalised total / 100** | **98** | | **67.3** | **Provisional only: novelty, dataset, feasibility and team structure are below 4/5; five gates are unresolved** |

### Mandatory gates

Pass means a bounded design is supported by current evidence; it is not a completed experimental result. Unknown gates prevent qualification, even when a provisional comparison score is provided.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | documented within-task lighting/view failures |
| 2. ML essential | Pass | learned anomaly adaptation |
| 3. Train/adapt models | Pass | train auxiliary selectors/adapters |
| 4. Existing data accessible | Unknown | real-shift payload/access not inspected |
| 5. No unavailable human evaluation | Pass | existing masks/labels, subject to access |
| 6. Precise research gap | Unknown | distinction from recent calibration/gating work incomplete |
| 7. Beyond application assembly | Unknown | gate/selector could be a routine add-on |
| 8. Objective evaluation | Pass | public-mask, disjoint-support protocol if data acquired |
| 9. 6–8 month feasibility | Unknown | three-method learning and high-resolution workload not bounded by a pilot |
| 10. Three connected contributions | Unknown | contribution-specific evidence for support selection and gating still needs an assessment plan |
| 11. No specialised/continuous high-end compute | Pass | capped cached-feature design; full-scale extensions optional |
| 12. Manageable responsible use | Pass | research-only image use under documented source terms, contingent on access |
| 13. Useful negative findings | Pass | adaptation harm and localisation failure conditions |

**Decision:** retain as a discussion reserve requiring meaningful refinement. Raising novelty alone from 3/5 to 4/5 would yield only 70.6; data suitability, execution scope and individual assessment boundaries also need improvement. These arithmetic scenarios do not resolve any gate.

**Next decision point:** acquire and inspect a suitable real-shift dataset, then resolve novelty, workload and the overlap between support selection and adaptation gating.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Evidence ledger](../../metadata/evidence-ledger.csv).
