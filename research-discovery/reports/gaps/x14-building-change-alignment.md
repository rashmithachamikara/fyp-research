[← Research candidates](../research-candidates.md)

# Separating real building changes from small image-alignment errors

**ID:** X14 · **Area:** Computer vision / remote-sensing change detection · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

A small offset between before/after overhead images can produce false building-change masks. Alignment-aware networks already address this problem, so a new project must examine the trade-off between suppressing displaced edges and erasing genuine small changes.

**Potential stakeholders:** Researchers supporting urban growth mapping and imagery-update workflows; this project does not infer illegal activity or certify disaster damage.

## 2. Research gap and question

**Tentative gap:** Measure and learn the alignment-tolerance versus true-change-retention trade-off under spatially separated evaluation. Distinguish a model that genuinely aligns evidence from one that merely smooths away small differences.

**Documented limitation versus inferred opportunity:** CASP explicitly addresses image misalignment using contextual and deformable feature alignment, with compact encoders and experiments on several datasets. SDA-Encoding also uses spatial/frequency information for change contours. The proposed trade-off and controlled no-change pairs are inferred opportunities; misregistration tolerance itself is already studied.

**Research question:** Can a compact building-change model suppress false changes from small registration errors without losing true small-building changes on spatially held-out image pairs?

**Hypothesis and rival explanation:** Change-preserving alignment supervision reduces offset-induced false positives while retaining small-object recall better than smoothing or unconstrained alignment. Rival explanation: lower recall and boundary smoothing create an apparent robustness improvement.

**Novelty status:** provisional. These are AI-assisted candidate opportunities for team and supervisor discussion. Neither sparse searches nor a suggested follow-up establish an original contribution.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [CASP: Exploring Context Alignment and Structure Perception, 2025](https://crabwq.github.io/pdf/2025%20CASP_Final.pdf) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FTGRS.2025.3540013) | Bidirectional context alignment, deformable difference alignment and structure perception; compact-backbone comparisons. | Misalignment handling is covered. Test the false-change/small-change trade-off under controlled offsets and geographic holdouts. | Author full PDF; methods and experimental setup; Sections II–IV; Table V and misalignment examples (X14-L1) |
| [Spatial-Frequency Decoupling Alignment Encoding, 2026](https://pubmed.ncbi.nlm.nih.gov/41902146/) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390%2Fs26061979) | Transformer features, wavelet decomposition and spatial/frequency fusion for change detection. | Edge/frequency fusion is established; compare error mechanisms rather than claiming another fusion block is new. | Primary indexed abstract and full-text Section 3.2; full methods not completely inspected; Abstract, Section 3.2 and benchmark figure captions (X14-L2) |
| [Remote Sensing Image Change Detection with Transformers (BIT), 2021](https://arxiv.org/abs/2103.00208) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FTGRS.2021.3095166) | Transformer change detection with public training, evaluation and demonstration code. | Use a reproducible strong baseline; train it again for the new spatial split. | Author abstract and repository; full paper methods not inspected; Abstract and README training/dataset instructions (X14-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FTGRS.2025.3540013,10.3390%2Fs26061979,10.1109%2FTGRS.2021.3095166). Source claims, queries and access limits are recorded in the [evidence ledger](../../metadata/evidence-ledger.csv) and [CV search records](../../metadata/cv-expansion-records.json).

## 4. Proposed approach

Start from an early-fusion or Siamese model and BIT. Learn bounded offset correction, a change-preserving objective and an alignment-failure score. Synthetic shifts create a controlled stress test; canonical change masks remain in the declared reference grid and invalid border pixels are excluded consistently.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [LEVIR-CD author page](https://justchenhao.github.io/LEVIR/): 637 RGB before/after pairs, 1,024 × 1,024 pixels, 0.5 m resolution and binary building-change masks from 20 Texas regions. |
| Access and terms | Academic, non-commercial use only; Google Earth terms also apply. Provider links and [BIT sample/loading route](https://github.com/justchenhao/BIT_CD) were inspected; the complete image archives and their sizes were not verified. |
| Spatial metadata, checked | [Author coordinate file](https://github.com/justchenhao/STANet/blob/master/LEVIR_CD_spatial_info/LEVIR_CD_name_coords.json) was fetched and parsed: 637 filename-to-bounding-coordinate entries. This supports geographic grouping; it does not establish independent regions without an overlap audit. |
| Bounded core / fallback | Use 256-pixel training crops grouped by full image and geographic cluster. Keep the 637-pair release as the core; an aligned-only model plus controlled shifts is the fallback. LEVIR-CD+ is a later extension, not an assumed audited substitute. |
| Resources, estimated | Occasional 8–12 GB GPU, 16 GB RAM and 10–25 GB working storage. Paired encoders and alignment operations increase implementation difficulty; benchmark runtime and full archive size remain unmeasured. |
| Prototype | Before/after image slider, predicted change overlay and alignment-sensitivity display; no operational planning or damage-assessment claim. |

Resource estimates are planning assumptions. No model training, image decoding, inference timing or benchmark reproduction was performed. Local checks were limited to the CCT20 annotation archive and LEVIR coordinate JSON; other loading routes were inspected in documentation.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: bounded alignment | Can offset correction improve robustness without destroying local change? H: A bounded learned correction improves false-change rates over unconstrained matching. | Train a bounded offset/correspondence module on source pairs and simulated shifts. | No correction and conventional phase-correlation registration; remove offset bounds. | False-positive area versus offset, plus clean small-building recall. |
| B: change preservation | Can training preserve small true changes despite alignment noise? H: A change-preserving contrastive objective limits over-smoothing. | Train changed/unchanged region contrastive or consistency supervision. | Ordinary change loss, standard jitter and parameter-matched smoothing; remove change preservation. | Recall by true-change component size at matched false-positive rate. |
| C: failure prediction | Can unreliable change masks be identified before accepting them? H: Forward/reverse alignment disagreement predicts false-change masks better than entropy. | Train a pair-level or region-level quality head from out-of-fold source predictions. | Entropy and raw image correlation; remove disagreement features. | Risk–coverage and quality error on the unchanged baseline, with rejected cases still counted in main metrics. |

All three address one shared problem and may share data, models and evaluation code. Evaluate each intervention against the unchanged common baseline before combining them, so every member can obtain findings if another method fails. Three projects or papers are not required; writing papers is optional.

## 7. Evaluation

- **Primary metric:** Change-class IoU averaged over a fixed clean/offset stress grid, with clean IoU and small-change recall reported separately. False-positive area on known no-change pairs is a key diagnostic.
- **Split:** Cluster full-pair bounding coordinates into geographically separated train/validation/test groups with a spatial buffer. All crops, augmentations and shifted versions of a pair stay together. Report official-split results separately; never use a published LEVIR-trained checkpoint to claim a newly held-out geography.
- **Baselines and code:** Image differencing plus threshold/phase correlation; early-fusion U-Net; [BIT training and checkpoints](https://github.com/justchenhao/BIT_CD). Compare against CASP/SDA-Encoding if reproducible. The inspected CASP README does not establish a usable training implementation; reimplementation is an explicit risk.
- **Ablations:** Baseline + A, + B, + C, then combination. Keep encoder, pixels, augmentation, pretraining and steps matched. Include identical-frame pairs with zero-change masks, real changed pairs, and smoothing controls. Do not tune offset severity on the final test.
- **Uncertainty and errors:** Three training seeds; paired bootstrap by original full-image/geographic cluster, with separate cluster results. Analyse offset magnitude, changed-object size, shadows and unchanged building edges. Quality rejection must report retained coverage and all-image metrics.
- **Useful result without winning:** Demonstrate whether apparent robustness mainly removes small true changes, or whether a simple registration front-end matches complex feature alignment.
- **Interpretation limit:** Synthetic translations are not all real registration errors. A Texas image benchmark cannot establish worldwide geographic transfer, urban policy benefit or reliable disaster assessment.

## 8. Score and next decision

**Provisional score: 73.9/100.** This is a comparison of proposal designs, not measured model performance or qualification. Novelty is 3/5, below the required 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: CASP and related alignment methods are close; the change-preservation trade-off needs a more complete methods comparison. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: original masks, academic terms and 637 coordinate entries are available; image downloads and geographic overlap still need checking. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: paired networks, coordinate-safe perturbations and incomplete recent code add learning and reproduction risks. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: bounded alignment, change-preserving objectives and quality learning support substantive ML research. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: spatial grouping, no-change controls and recall/false-positive trade-offs can discriminate rival explanations. |
| Three-member structure | 12 | 4 | 9.6 | Medium: alignment, change retention and fixed-mask quality each have independent baseline experiments. |
| Real-world significance | 9 | 4 | 7.2 | Medium: avoiding false changes matters for image-based mapping; planning outcomes are not observed. |
| Compute/storage | 5 | 4 | 4.0 | Medium: compact paired models are plausible on modest GPUs; aligned fallback bounds the risk. |
| Prototype | 3 | 4 | 2.4 | Medium-high: a before/after viewer is straightforward. |
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
| 6. Precise research gap | Unknown | The added value beyond CASP and other registration-aware change detectors needs fuller comparison. |
| 7. Beyond application assembly | Pass | The three interventions are evaluated through model-level baselines and ablations, not only a prototype. |
| 8. Objective evaluation | Pass | Section 7 specifies objective metrics, leakage controls, comparison baselines and uncertainty analysis. |
| 9. 6–8 month feasibility | Pass | The bounded configuration and reduced-method fallback are plausible in 6–8 months; this is an estimated design-level pass. |
| 10. Three connected contributions | Pass | Three related investigations each have an unchanged-baseline comparison and independently assessable outcome. |
| 11. No specialised/continuous high-end compute | Pass | The core uses existing RGB imagery and an occasional modest GPU; no new sensors or continuous high-end compute. |
| 12. Manageable responsible use | Pass | Original non-commercial/academic or permissive data terms support bounded offline research; source attribution and image-specific conditions remain applicable. |
| 13. Useful negative findings | Pass | Section 7 defines an informative negative result and alternatives to outperforming the strongest baseline. |

**Decision:** Useful but technically demanding; narrow the work to small offsets and small true changes.

**Next decision point:** Build a coordinate-grouped manifest and run BIT under small synthetic offsets before designing an alignment module. Discuss the evidence and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/cv-expansion-records.json).
