[← Research candidates](../research-candidates.md)

# Recognising wildlife when animal crops are incomplete at new camera locations

**ID:** X13 · **Area:** Computer vision / wildlife-image classification · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Camera-trap datasets help ecological monitoring but generate large image-review workloads. Cropping to detected animals can improve species classification, while poor or missing detections discard evidence and background context can become a shortcut at unfamiliar camera locations.

**Potential stakeholders:** Biodiversity researchers and camera-trap image-review tool developers; no new cameras, fieldwork or expert labelling are needed.

## 2. Research gap and question

**Tentative gap:** Test detection-quality-aware crop/context learning using a detector trained only on source locations. Jointly account for partial crops and entirely missed animals, while keeping the test camera locations and sequences out of model selection.

**Documented limitation versus inferred opportunity:** Gadot et al. show an overall crop benefit but explicitly leave when/where cropping helps and optimal crop padding to follow-up work; they also flag pretrained-detector overlap. Dussert et al. already use multi-crop context and discuss remaining detector misses. A new crop/context selector is a tentative opportunity, not proof that adaptive fusion is novel.

**Research question:** Can crop-quality-aware classification and source-only detector training preserve species macro-F1 at unseen camera locations when animal detections are incomplete or absent?

**Hypothesis and rival explanation:** A learned quality gate and context-resistant representations reduce false species and false-empty predictions relative to crop-only or fixed fusion. Rival explanation: gains come from target-location exposure in a pretrained detector or from processing more pixels.

**Novelty status:** provisional. These are AI-assisted candidate opportunities for team and supervisor discussion. Neither sparse searches nor a suggested follow-up establish an original contribution.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [To crop or not to crop, 2024](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/cvi2.12318) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1049%2Fcvi2.12318) | Whole-image, detector-crop and ensemble comparisons; overall benefits from cropping; detector-overlap caveat. | Analyse incomplete and missed crops at held-out locations with a source-trained detector and matched image budget. | Full text; methods, discussion and future work; Sections 2.3, 4–6 (X13-L1) |
| [Paying attention to other animal detections improves camera trap classification models, 2026](https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210x.70260) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1111%2F2041-210x.70260) | Attention across crop embeddings improves classification; discusses overconfidence, context limits and animal-detector misses. | Multi-crop context alone is covered; compare against it and test explicit crop reliability and no-detection failures. | Publisher full-text discussion; detailed methods not fully inspected; Section 4 Discussion (X13-L2) |
| [Towards Zero-Shot Camera Trap Image Categorization, 2024 preprint / 2025 proceedings](https://arxiv.org/abs/2410.12769) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2410.12769) | MegaDetector plus classifiers or DINOv2/FAISS evaluated on CCT20 and other datasets. | A detector-plus-classifier application is insufficient; isolate learned crop-quality and background interventions. | Author abstract; methods not inspected; Abstract (X13-L3) |
| [WildIng, 2026](https://arxiv.org/abs/2601.00993) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2601.00993) | Combines species text descriptions with image representations for geographic shift. | Geographic invariance is covered; isolate crop failure and source-detector provenance rather than a generic invariance claim. | Author preprint abstract; journal record found but publisher inaccessible; Abstract (X13-L4) |

[Import these 4 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1049%2Fcvi2.12318,10.1111%2F2041-210x.70260,10.48550%2FarXiv.2410.12769,10.48550%2FarXiv.2601.00993). Source claims, queries and access limits are recorded in the [evidence ledger](../../metadata/evidence-ledger.csv) and [CV search records](../../metadata/cv-expansion-records.json).

## 4. Proposed approach

Train a compact animal detector on source-location box annotations from generic-image weights. Cache predicted crops and whole-image embeddings; study a learned crop-quality gate, context-resistant classifier training and miss-aware detector sampling. A missing crop must trigger a defined whole-image prediction, not removal of the image.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [CCT20 benchmark on LILA](https://lila.science/datasets/caltech-camera-traps), derived from Caltech Camera Traps. The benchmark image archive is published as 6 GB; use it rather than the 105 GB parent archive. |
| Access and licence | Original source states the permissive Community Data License Agreement. A 2,997,071-byte author-linked annotation archive was downloaded into memory and parsed; no images or weights were acquired. |
| Labels and metadata, checked | Five JSON files parsed: 13,553 training images, 3,484 cis-validation, 1,725 trans-validation, 15,827 cis-test and 23,275 trans-test. Category lists have 16 entries. Image records include location, seq_id, frame_num and date_captured; box fields are present in inspected training/trans records. Full box coverage and category overlap need auditing. |
| Bounded core / fallback | Start with labelled single-category frames and an explicit empty class, fixing this subset from annotations before training; report excluded multi-category frames separately. Keep all detector-miss images. Cached ResNet/DINOv2 features and a small learned head provide a fallback to full fine-tuning. |
| Resources, estimated | Occasional 8–12 GB GPU for detector/classifier fine-tuning; CPU heads on cached features; 16 GB RAM and 15–30 GB working storage. Training time and VRAM are unmeasured. No wildlife hardware or ecological field expertise is assumed. |
| Prototype | Image, predicted crop, species score and fallback explanation. Avoid publishing identifying human images or precise animal-location metadata; no population or conservation-outcome claim. |

Resource estimates are planning assumptions. No model training, image decoding, inference timing or benchmark reproduction was performed. Local checks were limited to the CCT20 annotation archive and LEVIR coordinate JSON; other loading routes were inspected in documentation.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: crop-quality gate | When should crop or whole-image evidence be trusted? H: A trained quality gate beats crop-only and fixed averaging on partial or missing crops. | Learn a fusion gate from source-location predictions and controlled crop perturbations. | Crop-only, whole-image and fixed-average fusion; remove quality inputs. | Species macro-F1 by crop quality and missing-detection status. |
| B: context resistance | Can classification resist familiar backgrounds while preserving useful context? H: Context dropout and crop/full consistency reduce location shortcuts. | Train background/context suppression and consistency using source training boxes. | Ordinary augmentation and fixed crop padding; remove context consistency. | Held-out-location macro-F1 and background-sensitivity error analysis. |
| C: missed animals | Can source-trained detection reduce false-empty frames without more pixels? H: Small-animal/miss-aware sampling improves recall at a fixed false-positive budget. | Train detector loss/sampling focused on small animal boxes and hard empty frames. | Same compact detector with ordinary sampling; remove hard-negative or size component. | Animal recall and false-empty rate on new locations; fixed baseline classifier downstream. |

All three address one shared problem and may share data, models and evaluation code. Evaluate each intervention against the unchanged common baseline before combining them, so every member can obtain findings if another method fails. Three projects or papers are not required; writing papers is optional.

## 7. Evaluation

- **Primary metric:** Species macro-F1 on the locked trans-test location split for the predefined category set. Report empty-frame errors, animal recall and per-location results separately; a missed crop remains in the denominator.
- **Split:** Preserve published cis/trans partitions for comparability; audit seq_id and location intersections, then group bursts and near-duplicates where necessary. Select hyperparameters only on train/cis-validation/trans-validation. A redesigned split must be reported separately.
- **Baselines and code:** Frozen ResNet features + logistic regression; fine-tuned compact crop/whole-image classifier and fixed fusion. [TorchVision detection](https://github.com/pytorch/vision/tree/main/references/detection) supports a generic-image-initialised source detector. Multi-crop attention and DINOv2/FAISS are strong relevant comparisons. CCT20-trained MegaDetector/species checkpoints cannot establish source-only location generalisation.
- **Ablations:** Baseline + gate, + context objective, + detector sampling, then combination. Control crop padding, detector threshold, encoder, number of views, training steps and total processed pixels. Treat ground-truth crops as an oracle.
- **Uncertainty and errors:** Three seeds for small heads and the bounded fine-tuning run; sequence bootstrap within locations and individual location results. Analyse small animals, partial boxes, no boxes, empty frames, class imbalance and day/night where metadata or image-derived proxies support the distinction.
- **Useful result without winning:** Show where a crop-only method fails, whether fixed padding matches learned selection, or whether claimed new-location gains disappear after removing detector training overlap.
- **Interpretation limit:** Closed-set benchmark labels do not establish unknown-species detection, wildlife abundance estimates or field monitoring effectiveness.

## 8. Score and next decision

**Provisional score: 76.7/100.** This is a comparison of proposal designs, not measured model performance or qualification. Novelty is 3/5, below the required 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: crop benefits and context methods are established; reliability-aware fusion and miss-aware learning need closer duplication checking. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: original images/terms and small benchmark route documented; annotation fields locally parsed, but images and complete box coverage unverified. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: compact source detector and cached classifier heads bound the work; manageable with a staged pilot. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: learned gating, representation objectives and detector sampling give assessable ML investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: existing location/sequence metadata supports objective splits; pretraining provenance and burst overlaps need audit. |
| Three-member structure | 12 | 4 | 9.6 | Medium: each method has its own unchanged-baseline comparison; the gate and context head can run with the common detector. |
| Real-world significance | 9 | 4 | 7.2 | Medium: source papers document wildlife-image review and location-transfer problems; ecological outcomes remain outside scope. |
| Compute/storage | 5 | 4 | 4.0 | Medium: small heads and a compact detector plausibly fit occasional modest GPU access; full timings pending. |
| Prototype | 3 | 4 | 2.4 | Medium-high: crop and confidence viewer fits backend/web skills. |
| **Normalised total / 100** | **98** | | **76.7** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means supported at bounded design level, not demonstrated execution. Unknown gates prevent qualification. Provisional scores retain the existing comparison convention; they do not override the rule to resolve gates before qualifying a topic.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the source comparisons document a specific visual-model failure; downstream benefits remain untested. |
| 2. ML essential | Pass | Training or systematically adapting visual models is essential to the research question. |
| 3. Train/adapt models | Pass | Sections 4 and 6 specify trainable objectives, modules or predictors using existing data. |
| 4. Existing data accessible | Pass | Section 5 records an original public release, existing labels and a documented loading route, with access-check limits. |
| 5. No unavailable human evaluation | Pass | All central outcomes use existing masks, boxes or category labels; no new participant or expert annotations. |
| 6. Precise research gap | Unknown | The added value beyond crop/whole-image fusion, multi-crop attention and recent camera-trap generalisation work is unverified. |
| 7. Beyond application assembly | Pass | The three interventions are evaluated through model-level baselines and ablations, not only a prototype. |
| 8. Objective evaluation | Pass | Section 7 specifies objective metrics, leakage controls, comparison baselines and uncertainty analysis. |
| 9. 6–8 month feasibility | Pass | The bounded configuration and reduced-method fallback are plausible in 6–8 months; this is an estimated design-level pass. |
| 10. Three connected contributions | Pass | Three related investigations each have an unchanged-baseline comparison and independently assessable outcome. |
| 11. No specialised/continuous high-end compute | Pass | The core uses existing RGB imagery and an occasional modest GPU; no new sensors or continuous high-end compute. |
| 12. Manageable responsible use | Pass | Original non-commercial/academic or permissive data terms support bounded offline research; source attribution and image-specific conditions remain applicable. |
| 13. Useful negative findings | Pass | Section 7 defines an informative negative result and alternatives to outperforming the strongest baseline. |

**Decision:** Best initial feasibility lead among these five, subject to detector-provenance and novelty checks.

**Next decision point:** Audit box coverage and sequence/location overlaps, then compare a source-only crop classifier with whole-image and fixed-fusion baselines. Discuss the evidence and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/cv-expansion-records.json).
