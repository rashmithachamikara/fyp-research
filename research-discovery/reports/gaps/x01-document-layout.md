[← Research candidates](../research-candidates.md)

# Small document regions under combined scan and layout shifts

**ID:** X01 · **Area:** Computer vision / document AI · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Small captions, footnotes and page numbers can disappear from a layout detector's output when documents are degraded. This can leave a digitisation pipeline with confident but incomplete page structure. Existing robustness and layout-evaluation papers establish the general failure; the proposed interaction study is still an inferred opportunity.

**Potential stakeholders:** Digitisation teams and document-processing developers; downstream benefits would need separate validation.

## 2. Research gap and question

**Tentative gap:** Study whether training for combined degradations preserves small-region recall and calibrated detection confidence on document genres excluded from training. Robust layout detection and corruption benchmarks already exist; another generic robustness benchmark is insufficient.

**Research question:** Can size-aware consistency learning reduce small-region omissions under compound scan corruption and held-out document genres without increasing false detections?

**Hypothesis and rival explanation:** Size-aware consistency will help small regions more than ordinary augmentation at matched resolution. Rival explanation: any gain comes from higher resolution or additional training images rather than the objective.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [RoDLA, CVPR 2024](https://arxiv.org/html/2403.14442) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FCVPR52733.2024.01473) | Corruption taxonomy, robustness metrics and a robust detector. | Appendix G.1 leaves combined perturbations untested; test their interaction with small regions and held-out genres. | Full text; methods and limitations; Sections 3–5; Appendix G.1 (X01-L1) |
| [DocLayout-YOLO, October 2026 preprint](https://arxiv.org/html/2610.28171v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2610.28171) | Synthetic pretraining, layout attention and corruption evaluation. | Compound-corruption confidence and genre holdouts need a direct comparison; do not claim synthetic layout robustness is new. | Full text; robustness appendix; Section 5; Appendix C.2 (X01-L2) |
| [The COTe score, 2026 preprint](https://arxiv.org/html/2603.12718v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2603.12718) | Decomposes coverage, overlap and semantic-boundary errors. | Use a supplementary error analysis, not a claim to invent a layout metric. | Full text; Sections 3, 6–8 (X01-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FCVPR52733.2024.01473,10.48550%2FarXiv.2610.28171,10.48550%2FarXiv.2603.12718). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Use one small detector with a generic-image pretrained backbone. Compare size-aware feature consistency, learned region-level uncertainty and a bounded multi-scale sampling policy. Keep pixel budgets and corruption exposure matched. Do not use DocLayNet-fine-tuned checkpoints when claiming an unseen-genre test.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [DocLayNet](https://github.com/DS4SD/DocLayNet), 80,863 pages, 11 classes; original README and licence inspected. |
| Labels and grouping | COCO boxes; document name, collection, category and page number support document-grouped splits. Corruptions are simulated, not real scan histories. |
| Access and licence | Official 28 GiB core ZIP and Hugging Face route; CDLA-Permissive 1.0. README examples inspected; image archive not downloaded. |
| Bounded core / fallback | 5,000–10,000 source pages, one held-out genre, compact detector; reduce to three layout classes if needed, with a narrower claim. |
| Resources, estimated | One occasional 8–12 GB GPU; 16 GB host RAM; 40–80 GB storage. Timing, decoding and peak VRAM unmeasured. |
| Prototype | Local page overlay showing regions, small-region warnings and confidence; no claim to complete document understanding. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: small regions | Does size-aware consistency improve small-region recall? H: Size-aware consistency raises small-region recall at the same resolution. | Add a scale-normalised consistency objective. | Ordinary augmentation; remove size weights. | Recall versus box size at matched pixels. |
| B: uncertainty | Does region-aware calibration identify missing or unreliable regions? H: Localisation-aware confidence better identifies unreliable regions. | Fit localisation-aware confidence from validation detections. | Temperature scaling; remove size/quality features. | Detection reliability and review coverage. |
| C: sampling | Does a learned sampling policy outperform fixed corruption mixtures? H: A learned mixture improves compound-corruption robustness at matched exposure. | Train a bounded corruption/scale scheduler. | Fixed schedule; matched total images and pixels. | Robustness versus exposure and training cost. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Small-region AP averaged over predeclared compound corruptions and held-out genres; define small-area bins on training data.
- **Split:** Group by document and collection before augmentation; reserve a whole genre; source-only validation and confidence fitting. Never place versions of one page in different splits.
- **Baselines and code:** Faster R-CNN and a compact RT-DETR ([official code](https://github.com/lyuwenyu/RT-DETR)); RoDLA and DocLayout-YOLO as methodological references. Retrain on permitted source documents.
- **Ablations:** Size weighting, confidence head and sampling policy separately; also compare single versus combined corruptions at fixed severity and pixel budget.
- **Uncertainty and errors:** Three development seeds, five headline seeds; document-cluster bootstrap; omission/duplication errors by class, box area, genre and severity. Report overall mAP and calibration beside the primary metric.
- **Useful result without winning:** Find corruption combinations where a higher overall mAP hides more missing footnotes or captions.
- **Interpretation limit:** Synthetic scan corruption supports controlled robustness claims, not production OCR completeness or accessibility benefits.

## 8. Score and next decision

**Provisional score: 72.9/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 3/5; the required rating is 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Medium-low: a documented compound-perturbation limitation supports a precise question, but the method must be distinguished from 2026 layout training. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: source licence, grouping fields and download routes are documented; payload decoding remains pending. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: the page cap bounds scope, but detection training and three investigations are demanding for the team's experience. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: learned objectives, confidence fitting and sampling-policy experiments provide model-level work. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: document grouping, matched pixel budgets and size-specific errors provide objective comparisons; no runs yet. |
| Three-member structure | 12 | 4 | 9.6 | Medium: loss, confidence and training-policy contributions share a detector and have separate controls. |
| Real-world significance | 9 | 4 | 7.2 | Medium: omitted document regions affect extraction completeness; downstream user benefit is unmeasured. |
| Compute/storage | 5 | 3 | 3.0 | Low-medium: storage fits, but high-resolution extraction and GPU time have not been profiled. |
| Prototype | 3 | 4 | 2.4 | Medium-high: an annotated page viewer is bounded and matches backend skills. |
| **Normalised total / 100** | **98** |  | **72.9** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Pass | Section 5 records an original public release or author-documented loading route, existing labels and the access-check limit. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Unknown | Novelty beyond RoDLA and October 2026 layout methods remains unresolved. |
| 7. Beyond application assembly | Pass | Section 6 investigates learned interventions with baseline comparisons and ablations, rather than application assembly. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Pass | The bounded core and fallback in Section 5 are plausible within the team window; training costs remain estimates. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Pass | Section 5 records source terms and a bounded offline use; no deployment or high-stakes benefit is assumed. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** Investigate after the smaller CPU-first candidates; novelty and detection workload need refinement.

**Next decision point:** Compare the exact compound-corruption and confidence protocols of the three neighbours, then time a 500-page baseline before expanding. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
