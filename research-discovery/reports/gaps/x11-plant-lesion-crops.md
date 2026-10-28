[← Research candidates](../research-candidates.md)

# Finding small plant lesions without knowing their location in advance

**ID:** X11 · **Area:** Computer vision / plant-lesion segmentation · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Field-image lesion segmentation is difficult when symptoms occupy a small part of a cluttered image. A recent PlantSeg study reports benefits from annotation-guided cropping, but its guided crops use the evaluated image's ground-truth lesion positions. That measures an oracle upper bound rather than an automatic full-image pipeline.

**Potential stakeholders:** Agricultural image-analysis researchers and developers of crop-monitoring tools; this project evaluates image masks, not treatment advice.

## 2. Research gap and question

**Tentative gap:** Test whether train-only lesion crops and a learned, budget-constrained region selector recover small symptoms on complete unseen images. Compare against uniform tiling and an oracle crop to separate genuine learning from privileged localisation or simply processing more pixels.

**Documented limitation versus inferred opportunity:** Natij et al. explicitly identify oracle test-time cropping as their principal limitation and propose train-only cropping or a learned proposer. GARDEN already investigates lesion boundaries and scale variation. The new opportunity is an inferred experimental design around this documented limit, not a claim to invent lesion-aware cropping.

**Research question:** Can a compact lesion segmenter recover small disease regions on full images through train-only crop consistency and learned region selection at a matched inference-pixel budget?

**Hypothesis and rival explanation:** Learned crop allocation plus crop-to-full-image consistency will improve small-region recall over uniform resizing and equal-budget tiling. Rival explanation: extra inference pixels, excluded hard images or near-duplicate web images explain the gain.

**Novelty status:** provisional. These are AI-assisted candidate opportunities for team and supervisor discussion. Neither sparse searches nor a suggested follow-up establish an original contribution.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Preprocessing strategies on PlantSeg, 2026](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1835997/full) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3389%2Ffrai.2026.1835997) | Compares six preprocessing strategies and explicitly labels test-annotation-guided crops as oracle conditions. | Train-only crops and predicted proposals; evaluate every original image, including failed proposals. | Full text; methods and limitations; Sections 3.3–3.4 and 5.5.1–5.5.2 (X11-L1) |
| [GARDEN: gradient-guided boundary-aware selective scanning, 2025](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1727075/full) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3389%2Ffpls.2025.1727075) | Multi-scale context and boundary-conditioned scanning for lesion masks. | Boundary enhancement alone is covered; isolate resolution allocation and crop failure. | Full text; method and experimental setup; Sections 3.2–3.3 and 4 (X11-L2) |
| [A Large-Scale In-the-wild Dataset for Plant Disease Segmentation, 2026](https://doi.org/10.1038/s41597-025-06513-4) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1038%2Fs41597-025-06513-4) | PlantSeg masks, metadata and segmentation benchmarks. | Use the established task; do not treat a new backbone as the gap. | Primary indexed full-text data sections plus author README; publisher blocked; Metadata, Data Records and baseline table (X11-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.3389%2Ffrai.2026.1835997,10.3389%2Ffpls.2025.1727075,10.1038%2Fs41597-025-06513-4). Source claims, queries and access limits are recorded in the [evidence ledger](../../metadata/evidence-ledger.csv) and [CV search records](../../metadata/cv-expansion-records.json).

## 4. Proposed approach

Start with a compact full-image mask model. Learn from paired full images and training-only lesion crops, then investigate a small crop-allocation head and a boundary-preserving training objective. Every evaluated image must be processed without its label, including images where no crop is proposed.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [PlantSeg Zenodo v7](https://zenodo.org/records/17719108) and [author implementation](https://github.com/tqwei05/PlantSeg). The author repository reports 7,774 images and disease-region masks; this is not the unrelated cell-segmentation package also named PlantSeg. |
| Access and licence | Public 1.1 GB ZIP, published size. The dataset paper states CC BY-NC 4.0 and per-image source/licence metadata. Audit those records before redistributing examples; archives and image decoding were not checked locally. |
| Labels and split | JPEG images, PNG masks, image source URLs, host/disease fields and a published 70/10/20 split. Source URL and duplicate groups can support a stronger split; they are not farm or camera identifiers. |
| Bounded core / fallback | Begin with binary lesion/background masks across a preregistered subset of supported host–disease classes; retain multiclass evaluation as an extension. If the learned selector fails, train-only crop consistency versus full-image training remains testable. |
| Resources, estimated | Occasional 8–12 GB GPU, 16 GB RAM and 8–15 GB working storage. Cap total inference pixels and crop count. The two-stage learning curve makes this riskier than a single mask model; no timing or VRAM was measured. |
| Prototype | Full-image lesion overlays with selected crop regions and missed-region examples; no disease diagnosis or severity/treatment claim. |

Resource estimates are planning assumptions. No model training, image decoding, inference timing or benchmark reproduction was performed. Local checks were limited to the CCT20 annotation archive and LEVIR coordinate JSON; other loading routes were inspected in documentation.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: train-only crop learning | Does crop-to-full consistency improve small-lesion recall? H: Training-only crop consistency transfers lesion detail to full-image inference. | Learn a crop/full-image consistency objective with training labels only. | Same model and augmentations; remove consistency and compare random-crop training. | Small-lesion recall and all-image mask quality without an inference cropper. |
| B: learned pixel allocation | Can a learned selector beat uniform tiling at the same pixel budget? H: Predicted region allocation reduces wasted pixels without hiding proposal failures. | Train a crop-ranking or allocation head using training-mask coverage and a pixel-cost penalty. | Uniform grid, random proposals and oracle crops; remove the cost term. | End-to-end recall versus processed pixels, counting no-proposal cases as failures. |
| C: boundary preservation | Can detail supervision resist downsampling losses? H: A scale-conditioned boundary objective preserves thin symptoms beyond ordinary Dice loss. | Train boundary/detail supervision on the common full-image baseline. | Dice/cross-entropy and an established boundary loss; remove scale conditioning. | Boundary IoU and false-positive area by lesion size, independently of A and B. |

All three address one shared problem and may share data, models and evaluation code. Evaluate each intervention against the unchanged common baseline before combining them, so every member can obtain findings if another method fails. Three projects or papers are not required; writing papers is optional.

## 7. Evaluation

- **Primary metric:** Foreground lesion IoU on every full test image at a fixed total inference-pixel budget; also report small-connected-region recall at a preregistered overlap cutoff and boundary IoU.
- **Split:** Publish the official-split result, then group exact/perceptual duplicates and source-image families before assigning train/validation/test. Use metadata source groups only where adequate class support remains; make no unseen-farm claim.
- **Baselines and code:** U-Net/DeepLabV3+; compact YOLO11-seg or SegNeXt through the [author code](https://github.com/tqwei05/PlantSeg). Compare to uniform tiling and the 2026 preprocessing study. An oracle crop is an upper bound, never the main baseline.
- **Ablations:** Baseline + A, + B, + C, then combination; match encoder, full-image resolution, processed pixels, training steps and class sampling. Do not remove test cases whose crops contain no lesion.
- **Uncertainty and errors:** Three seeds for the bounded core; paired bootstrap over duplicate/source groups. Stratify small/peripheral lesions, class support, image resolution and empty/missed proposals; threshold selection uses validation only.
- **Useful result without winning:** Measure how much apparent crop gain disappears without test annotations, or show that uniform tiling gives a better accuracy–cost trade-off than learned allocation.
- **Interpretation limit:** Pixels labelled as disease do not establish pathogen identity, disease progression, yield loss or treatment benefit.

## 8. Score and next decision

**Provisional score: 73.9/100.** This is a comparison of proposal designs, not measured model performance or qualification. Novelty is 3/5, below the required 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: a precise oracle limitation is documented, but train-only crops and learned proposals are already suggested; an original method distinction remains unverified. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium: public masks, terms and compact archive are documented; source provenance and actual decoding remain to be audited. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: manageable data size, but crop selection and end-to-end accounting add substantial learning and integration work. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: consistency learning, learned allocation and boundary objectives support model-level research. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: full-image evaluation and equal-pixel controls isolate privileged crops and resolution; provenance grouping needs a pilot. |
| Three-member structure | 12 | 4 | 9.6 | Medium: each method runs on the same unmodified baseline and has its own metric and ablation. |
| Real-world significance | 9 | 4 | 7.2 | Medium: small lesion localisation is relevant to crop-image analysis; agronomic benefit is outside the labels. |
| Compute/storage | 5 | 4 | 4.0 | Medium: compact models and limited crops plausibly fit a modest GPU; training unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium-high: mask/crop overlays fit existing web-development skills. |
| **Normalised total / 100** | **98** | | **73.9** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means supported at bounded design level, not demonstrated execution. Unknown gates prevent qualification. Provisional scores retain the existing comparison convention; they do not override the rule to resolve gates before qualifying a topic.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the source comparisons document a specific visual-model failure; downstream benefits remain untested. |
| 2. ML essential | Pass | Training or systematically adapting visual models is essential to the research question. |
| 3. Train/adapt models | Pass | Sections 4 and 6 specify trainable objectives, modules or predictors using existing data. |
| 4. Existing data accessible | Pass | Section 5 records an original public release, existing labels and a documented loading route, with access-check limits. |
| 5. No unavailable human evaluation | Pass | All central outcomes use existing masks, boxes or category labels; no new participant or expert annotations. |
| 6. Precise research gap | Unknown | A distinct contribution beyond published train-only cropping, learned proposal and boundary methods still needs verification. |
| 7. Beyond application assembly | Pass | The three interventions are evaluated through model-level baselines and ablations, not only a prototype. |
| 8. Objective evaluation | Pass | Section 7 specifies objective metrics, leakage controls, comparison baselines and uncertainty analysis. |
| 9. 6–8 month feasibility | Pass | The bounded configuration and reduced-method fallback are plausible in 6–8 months; this is an estimated design-level pass. |
| 10. Three connected contributions | Pass | Three related investigations each have an unchanged-baseline comparison and independently assessable outcome. |
| 11. No specialised/continuous high-end compute | Pass | The core uses existing RGB imagery and an occasional modest GPU; no new sensors or continuous high-end compute. |
| 12. Manageable responsible use | Pass | Original non-commercial/academic or permissive data terms support bounded offline research; source attribution and image-specific conditions remain applicable. |
| 13. Useful negative findings | Pass | Section 7 defines an informative negative result and alternatives to outperforming the strongest baseline. |

**Decision:** Investigate the oracle-to-automatic gap; narrow the selector scope before choosing this topic.

**Next decision point:** Load a labelled sample and compare full-image resizing, train-only crops and equal-budget tiling before developing a new selector. Discuss the evidence and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/cv-expansion-records.json).
