[← Research candidates](../research-candidates.md)

# Keeping rare waste materials from disappearing during semi-supervised segmentation

**ID:** X15 · **Area:** Computer vision / waste-material segmentation · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Recycling-stream images contain deformable, translucent and overlapping objects. Limited mask labels encourage semi-supervised learning, but uneven class support and inaccurate pseudo-labels can suppress less common materials. Existing work already combines augmentation, consistency and class-weighted losses.

**Potential stakeholders:** Researchers developing image-based recycling analysis; no conveyor belt, robot or industrial partnership is required.

## 2. Research gap and question

**Tentative gap:** Investigate how pseudo-label acceptance and training losses affect rare-material retention under a fixed labelled-data budget. Separate genuine use of unlabelled images from simple class reweighting, duplicated conveyor frames and confidence-induced class exclusion.

**Documented limitation versus inferred opportunity:** NUNI-Waste documents poor performance and low representation for metal and rigid plastic and already studies adaptive weighting and augmentation. VisDA demonstrates facility/season shift but uses target-domain access. The proposed rare-class pseudo-label precision/recall investigation is inferred and must be checked against general semi-supervised methods.

**Research question:** Can class-conditional pseudo-label quality learning preserve rare waste-material IoU in cluttered images when only a small fixed fraction of existing masks is used for training?

**Hypothesis and rival explanation:** Quality-aware pseudo-label selection and noise-tolerant rare-class learning improve minority-material IoU beyond reweighting and standard consistency at the same label and compute budget. Rival explanation: favourable labelled subsets, class oversampling or near-duplicate frames cause the gain.

**Novelty status:** provisional. These are AI-assisted candidate opportunities for team and supervisor discussion. Neither sparse searches nor a suggested follow-up establish an original contribution.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [ZeroWaste: Towards Deformable Object Segmentation in Cluttered Scenes, CVPR 2022](https://ai.bu.edu/zerowaste/) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2106.02740) | Cluttered waste benchmark, fully/unlabelled subsets and published baselines. | The dataset and semi-supervised setting are established; a waste-sorting demonstration alone is insufficient. | Author project, dataset table and implementation README; full paper methods not inspected; Abstract, Dataset and repository semi-supervised instructions (X15-L1) |
| [NUNI-Waste, 2024](https://cerv.aut.ac.nz/wp-content/uploads/2024/01/NUNI-WasteQi-JianChun.pdf) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1007%2Fs11042-024-18265-1) | Non-uniform augmentation, adaptive class weighting and consistency on ZeroWaste; discusses rare metal/rigid plastic. | Compare with these mechanisms, then isolate pseudo-label correctness and minority retention rather than claiming class balance or augmentation is new. | Author full manuscript; method, experiments and ablations; Sections 3, 4 and 5.2–5.3 (X15-L2) |
| [VisDA 2022 Challenge: Domain Adaptation for Industrial Waste Sorting, PMLR volume 220](https://proceedings.mlr.press/v220/bashkirova23a.html) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2303.14828) | Real/synthetic waste segmentation and adaptation between facilities/seasons using target-domain data. | The bounded core is label-budget robustness within the verified release; do not claim cross-facility transfer without separately checking target data and labels. | Proceedings abstract and linked PDF abstract; detailed methods not inspected; Abstract and challenge task (X15-L3) |
| [Robustness of sparse instance segmentation models under synthetic distribution shifts, 2026](https://www.nature.com/articles/s41598-026-72216-4) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1038%2Fs41598-026-72216-4) | Corruption and pruning evaluation on steel-scrap imagery; material/size sensitivity. | Generic corruption robustness is covered and this is a different task/data source; it is supporting context, not direct evidence of ZeroWaste pseudo-label failure. | Publisher early-release abstract only; Abstract; published 25 September 2026 (X15-L4) |
| [UniMatch V2, TPAMI 2025](https://arxiv.org/abs/2410.10777) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2410.10777) | Stronger pretrained encoders and simplified weak-to-strong consistency; code, weights and logs. | Separate new selection/loss benefits from an encoder upgrade and compare under matched label and compute budgets. | Author abstract and official implementation README; full methods not inspected; Abstract and README (X15-L5) |

[Import these 5 literature records](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2106.02740,10.1007%2Fs11042-024-18265-1,10.48550%2FarXiv.2303.14828,10.1038%2Fs41598-026-72216-4,10.48550%2FarXiv.2410.10777). Source claims, queries and access limits are recorded in the [evidence ledger](../../metadata/evidence-ledger.csv) and [CV search records](../../metadata/cv-expansion-records.json).

## 4. Proposed approach

Start with a compact semantic segmenter and a standard teacher/student setup. Hide labels only in a predefined training partition; final evaluation retains all existing masks. Learn a robust minority-class objective, spatially coherent consistency and a pseudo-label quality selector. The actual pseudo-label failure must first be demonstrated on a labelled validation audit.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [ZeroWaste author page](https://ai.bu.edu/zerowaste/) and [official implementation](https://github.com/dbash/zerowaste). ZeroWaste-f: 4,503 labelled frames / published 7.0 GB ZIP; ZeroWaste-s: 6,212 unlabelled frames / 9.9 GB ZIP. Four materials: cardboard, soft plastic, rigid plastic and metal, plus background. |
| Access and licence | CC BY-NC 4.0 stated on the original page and author repository. Zenodo download routes were located; complete archives were not acquired or decoded. The initially found Trash-AI repository route returned 404; the correct author route is dbash/zerowaste. |
| Labels, metadata and split | Use released masks and split manifests; verify class mapping, temporal/frame groups and duplicate overlap before training. Capture/sequence identifiers were not locally inspected, so the release does not yet support a new-facility or unseen-capture claim. |
| Bounded core / fallback | Begin with ZeroWaste-f only: use 1/8 and 1/4 of training masks, treating the remainder of training images as unlabelled. Never use validation/test images for pseudo-labelling. Add ZeroWaste-s only after provenance/duplicate checks. Supervised rare-class losses on the same label budgets are the fallback. |
| Resources, estimated | Occasional 8–12 GB GPU, 16 GB RAM and 20–40 GB working storage. Teacher/student inference and repeated label subsets increase workload; use a compact encoder, 384–512 pixel crops and two label budgets. Training time and VRAM remain unmeasured. |
| Prototype | Waste-material masks with rare-class errors and pseudo-label confidence overlays; no material-sorting throughput or recycling-rate claim. |

Resource estimates are planning assumptions. No model training, image decoding, inference timing or benchmark reproduction was performed. Local checks were limited to the CCT20 annotation archive and LEVIR coordinate JSON; other loading routes were inspected in documentation.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: rare-class noise tolerance | Can learning retain minorities without amplifying incorrect pseudo-labels? H: A noise-tolerant class objective improves rare IoU beyond weighting alone. | Train a minority-aware robust loss with bounded influence for uncertain pixels. | Cross-entropy, class-weighted/focal losses and NUNI-style weighting; remove noise tolerance. | Metal/rigid-plastic IoU and pseudo-label error at fixed label budget. |
| B: spatial consistency | Can consistency preserve coherent material regions in clutter? H: Region-coherent augmentation reduces label fragmentation compared with pixelwise consistency. | Train region/boundary-consistent teacher/student objectives using training masks and predicted regions. | Standard weak/strong consistency and ClassMix; remove region constraint. | Minority-region recall, boundary errors and foreground IoU independently of A/C. |
| C: pseudo-label quality | Which pseudo-labels should be accepted without discarding rare classes? H: Learned class-conditional quality improves acceptance precision/recall over one confidence cutoff. | Train a selector using out-of-fold labelled training predictions, then apply it to unlabelled training frames. | Global and per-class confidence thresholds; remove learned quality features. | Accepted-label precision/recall by class and downstream IoU using the unchanged baseline loss. |

All three address one shared problem and may share data, models and evaluation code. Evaluate each intervention against the unchanged common baseline before combining them, so every member can obtain findings if another method fails. Three projects or papers are not required; writing papers is optional.

## 7. Evaluation

- **Primary metric:** Mean foreground IoU over the four materials, averaged over predefined label budgets and repeated labelled subsets. Report metal/rigid-plastic IoU separately so background or common classes cannot hide minority collapse.
- **Split:** Respect official train/validation/test first; group near-duplicate and adjacent identifiable frames before selecting labelled training subsets. Keep all crops of a frame together. If official splits contain connected frame groups, publish a separate grouped sensitivity result. No target test images enter teacher training.
- **Baselines and code:** Fully supervised compact U-Net/DeepLabV3+, class-weighted loss, ReCo via the [ZeroWaste code](https://github.com/dbash/zerowaste), and [UniMatch](https://github.com/LiheYoung/UniMatch). The [UniMatch-V2 author implementation](https://github.com/LiheYoung/UniMatch-V2), checkpoints and logs were located and should supply a stronger modern comparison, subject to a small-encoder pilot. NUNI-Waste is the nearest task-specific comparison.
- **Ablations:** Baseline + robust loss, + region consistency, + quality selector, then combination. Match labelled frames, pseudo-label candidates, augmentation, encoder and total steps. Include an oracle-correct pseudo-label diagnostic on held-out labelled training images, never on test data.
- **Uncertainty and errors:** Three labelled-subset seeds; repeat small-model training seeds where affordable. Bootstrap by identifiable source/frame group. Analyse rare-material support, thin/folded regions, adjacency to background, pseudo-label acceptance by class and false material positives; foreground fraction is only a clutter proxy, not an occlusion annotation.
- **Useful result without winning:** Show that standard weighting or thresholds match the proposed selector, or identify the label budget where extra pseudo-labels hurt rare materials despite better aggregate accuracy.
- **Interpretation limit:** Visible-material masks do not establish recyclability, contamination chemistry, robot picking success or recycling-plant outcomes. Synthetic corruptions and within-release splits do not prove facility transfer.

## 8. Score and next decision

**Provisional score: 75.7/100.** This is a comparison of proposal designs, not measured model performance or qualification. Novelty is 3/5, below the required 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: NUNI-Waste already covers imbalance/consistency and generic class-conditional SSL is crowded; distinct pseudo-label quality value remains unverified. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium: original masks, unlabelled data, archive sizes and non-commercial terms are documented; decoding and sequence provenance remain unchecked. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: two bounded label budgets and an established pipeline are plausible; teacher/student debugging is still a learning risk. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: robust objectives, spatial consistency and learned selection support model-level comparisons. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: label-budget controls, rare-class metrics and acceptance diagnostics separate several confounders; grouping metadata needs auditing. |
| Three-member structure | 12 | 4 | 9.6 | Medium: each intervention has a common-baseline experiment and interpretable result even if another fails. |
| Real-world significance | 9 | 4 | 7.2 | Medium: source studies document cluttered recycling imagery and rare-material errors; actual recycling benefits are not observed. |
| Compute/storage | 5 | 3 | 3.0 | Medium-low: repeated semi-supervised runs multiply GPU use and archive footprint; reduced-data fallback is needed. |
| Prototype | 3 | 4 | 2.4 | Medium-high: masks and pseudo-label overlays are easy to demonstrate offline. |
| **Normalised total / 100** | **98** | | **75.7** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means supported at bounded design level, not demonstrated execution. Unknown gates prevent qualification. Provisional scores retain the existing comparison convention; they do not override the rule to resolve gates before qualifying a topic.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the source comparisons document a specific visual-model failure; downstream benefits remain untested. |
| 2. ML essential | Pass | Training or systematically adapting visual models is essential to the research question. |
| 3. Train/adapt models | Pass | Sections 4 and 6 specify trainable objectives, modules or predictors using existing data. |
| 4. Existing data accessible | Pass | Section 5 records an original public release, existing labels and a documented loading route, with access-check limits. |
| 5. No unavailable human evaluation | Pass | All central outcomes use existing masks, boxes or category labels; no new participant or expert annotations. |
| 6. Precise research gap | Unknown | A precise distinction from NUNI-Waste, newer UniMatch variants and class-conditional pseudo-label methods has not been established. |
| 7. Beyond application assembly | Pass | The three interventions are evaluated through model-level baselines and ablations, not only a prototype. |
| 8. Objective evaluation | Pass | Section 7 specifies objective metrics, leakage controls, comparison baselines and uncertainty analysis. |
| 9. 6–8 month feasibility | Pass | The bounded configuration and reduced-method fallback are plausible in 6–8 months; this is an estimated design-level pass. |
| 10. Three connected contributions | Pass | Three related investigations each have an unchanged-baseline comparison and independently assessable outcome. |
| 11. No specialised/continuous high-end compute | Pass | The core uses existing RGB imagery and an occasional modest GPU; no new sensors or continuous high-end compute. |
| 12. Manageable responsible use | Pass | Original non-commercial/academic or permissive data terms support bounded offline research; source attribution and image-specific conditions remain applicable. |
| 13. Useful negative findings | Pass | Section 7 defines an informative negative result and alternatives to outperforming the strongest baseline. |

**Decision:** Promising bounded data route, but the semi-supervised method distinction is still provisional.

**Next decision point:** Load ZeroWaste-f and compare supervised, weighted-loss and standard semi-supervised baselines at one fixed label budget before adding a selector. Discuss the evidence and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/cv-expansion-records.json).
