[← Research candidates](../research-candidates.md)

# Knowing when transparent-object boundaries are unreliable

**ID:** X12 · **Area:** Computer vision / transparent-object segmentation · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Glass and other transparent surfaces inherit much of their appearance from the background. Boundary and reflection methods already improve segmentation, yet weak reflective cues and glass-like opaque objects remain difficult. A useful model must identify unreliable masks as well as produce them.

**Potential stakeholders:** Researchers developing RGB perception for service environments; this is an offline image study, not a navigation or assistive safety system.

## 2. Research gap and question

**Tentative gap:** Investigate whether boundary/interior-specific training and a learned mask-quality predictor distinguish semantic confusion from localisation error when blur or compression weakens transparent cues. Hold inference cost fixed and compare learned quality with simple entropy and size/boundary controls.

**Documented limitation versus inferred opportunity:** TransCues documents confusion on glass-like objects and inadequate reflective signals. UncertSAM already evaluates uncertainty on transparency and finds that explicit uncertainty fusion adds little beyond a constant-map control. The proposed boundary/interior quality distinction is inferred; generic uncertainty estimation or adding boundary attention is not new.

**Research question:** Can boundary/interior-aware training and mask-quality prediction identify unreliable transparent-object masks under unseen corruption severities without increasing the inference budget?

**Hypothesis and rival explanation:** Separating contour and interior evidence improves boundary quality and error ranking over a shared mask head. Rival explanation: extra parameters, ensembling or boundary length alone explain the apparent uncertainty benefit.

**Novelty status:** provisional. These are AI-assisted candidate opportunities for team and supervisor discussion. Neither sparse searches nor a suggested follow-up establish an original contribution.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [TransLab: Segmenting Transparent Objects in the Wild, 2020](https://xieenze.github.io/projects/TransLAB/TransLAB.html) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2003.13948) | Transparent-object benchmark and boundary-aware segmentation. | Boundary awareness is established; use it as a comparator. | Author project description, splits and repository; paper methods not fully inspected; Task, TransLab description and Data (X12-L1) |
| [TransCues: Power of Boundary and Reflection, WACV 2026](https://arxiv.org/html/2512.07034v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FWACV61042.2026.00328) | RGB-only boundary/reflection enhancement, multiple datasets and compact variants. | Test error-type separation and quality estimation beyond segmentation gains; keep added capacity controlled. | Full preprint text and author project; published conference record checked; Sections 3–4, 7.2 and project failure cases (X12-L2) |
| [Towards Integrating Uncertainty for Domain-Agnostic Segmentation, 2025](https://arxiv.org/html/2512.23427v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2512.23427) | UncertSAM includes Trans10K, post-hoc uncertainty and constant-map controls for refinement. | Use predicted masks without oracle box prompts and distinguish contour from interior errors; do not claim UQ on transparency is new. | Full text; NeurIPS 2025 workshop paper / arXiv version; Sections 2–3, Appendix A and Table 2 (X12-L3) |
| [RobustSAM, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_RobustSAM_Segment_Anything_Robustly_on_Degraded_Images_CVPR_2024_paper.html) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FCVPR52733.2024.00391) | Adapts SAM for degraded images using additional trainable components and a large degraded-image dataset. | Generic degradation robustness is already addressed; compare fixed-budget reliability and cue-specific errors. Full RobustSAM training is outside the modest-compute core. | Primary conference abstract only; Abstract (X12-L4) |

[Import these 4 literature records](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2003.13948,10.1109%2FWACV61042.2026.00328,10.48550%2FarXiv.2512.23427,10.1109%2FCVPR52733.2024.00391). Source claims, queries and access limits are recorded in the [evidence ledger](../../metadata/evidence-ledger.csv) and [CV search records](../../metadata/cv-expansion-records.json).

## 4. Proposed approach

Use an RGB-only compact segmentation encoder, an explicit contour objective and a mask-quality head trained from out-of-fold training predictions. Study a small boundary/interior reliability gate. A SAM comparator must use automatically predicted prompts; ground-truth boxes may appear only as a labelled oracle condition.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [Trans10K / TransLab author page](https://xieenze.github.io/projects/TransLAB/TransLAB.html) and [Trans10K-v2 author loader](https://github.com/xieenze/Trans2Seg). RGB images and masks require no depth or polarisation hardware. |
| Access and terms | Original download links were located; the train Drive page resolves to train.zip, but archive download/decoding was not verified. The original [project README](https://github.com/xieenze/Segment_Transparent_Objects) permits academic use and discusses Apache terms for the project. Dataset-specific image terms and their application to v2 remain unresolved; do not infer an image licence from a code licence. Gate 12 is Unknown. |
| Labels and reproducible split | Original Trans10K: 10,428 images with transparent things/stuff, split 5,000 train / 1,000 validation / 4,428 test and easy/hard subsets. The v2 loader uses fine-grained masks_12. Audit exact mapping and duplicates before choosing binary versus multiclass targets. |
| Bounded core / fallback | Use v2 collapsed to transparent/background first. The documented v1 easy/hard split is a reduced configuration if v2 loading is troublesome, subject to the same terms check. Additional datasets are optional and require separate source audits. |
| Resources, estimated | Occasional 8–12 GB GPU, 16 GB RAM and 10–20 GB working storage, pending actual archive sizes. Prefer a small encoder and 384–512 pixel inputs. Original multi-GPU training recipes are not assumed reproducible on the team's hardware. |
| Prototype | Image, mask, contour and predicted quality overlay; no robot, obstacle-avoidance or accessibility claim. |

Resource estimates are planning assumptions. No model training, image decoding, inference timing or benchmark reproduction was performed. Local checks were limited to the CCT20 annotation archive and LEVIR coordinate JSON; other loading routes were inspected in documentation.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: contour training | Does contour-specific supervision retain shape when cues weaken? H: A contour/interior objective improves boundary IoU at matched cost. | Train a lightweight separated contour/interior objective. | Ordinary cross-entropy/Dice and a standard boundary loss; remove the separation. | Boundary IoU and interior IoU by corruption severity. |
| B: quality prediction | Can mask failure be predicted without a true mask at inference? H: Out-of-fold learned quality ranks errors better than entropy or mask size. | Train an image/mask quality head on source training predictions. | Entropy, predicted area and boundary-length scores; remove image features. | Area under risk–coverage and quality-prediction error on fixed baseline masks. |
| C: cue reliability | Can a learned gate avoid overusing one degraded cue? H: Reliability-weighted boundary/interior fusion reduces glass-like false positives. | Train a small reliability gate with controlled training corruptions. | Equal-weight fusion and a parameter-matched gate; remove reliability supervision. | False-positive area and mask IoU on clean and held-out corruption families. |

All three address one shared problem and may share data, models and evaluation code. Evaluate each intervention against the unchanged common baseline before combining them, so every member can obtain findings if another method fails. Three projects or papers are not required; writing papers is optional.

## 7. Evaluation

- **Primary metric:** Transparent-foreground IoU averaged over preregistered clean and corruption settings; clean performance reported separately. Boundary IoU and risk–coverage are contribution-specific outcomes.
- **Split:** Retain official image splits, remove cross-split near-duplicates, and keep all corruptions of an image in its split. Select settings on validation; hold out corruption families/severities. This tests synthetic robustness, not a new-country distribution.
- **Baselines and code:** DeepLabV3+ or SegFormer-B0; [Trans4Trans](https://github.com/InSAI-Lab/Trans4Trans) has training code and author-linked checkpoints. Include TransCues as a recent comparator where reproducible: its inspected repository README links a project webpage and did not establish training-code availability. UncertSAM is a separate prompted comparator.
- **Ablations:** Baseline + A, + B, + C and combination; include constant-map, shuffled-quality and parameter-matched controls. Count all forward passes and prediction prompts when comparing inference cost.
- **Uncertainty and errors:** Three seeds for a bounded setup; paired bootstrap by original image, never by pixel or corrupted copy. Analyse contour versus interior errors, object area, easy/hard subset, blur/JPEG severity and glass-like false positives.
- **Useful result without winning:** Show that entropy or simple mask geometry identifies failures as well as the learned head, or that a boundary improvement fails to correct semantic confusion.
- **Interpretation limit:** Synthetic image degradation does not establish actual camera failure rates or safe navigation. Unknown scene IDs prevent strong scene-transfer claims.

## 8. Score and next decision

**Provisional score: 68.0/100.** This is a comparison of proposal designs, not measured model performance or qualification. Novelty is 3/5, below the required 4/5. 2 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low: both transparent cues and uncertainty have close prior work; the boundary/interior reliability distinction needs tighter checking. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium-low: official masks and split routes exist, but image-specific terms, v2 label mapping and archive access remain unchecked. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: legacy model environments and several reliability objectives increase the learning burden. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: separated objectives, learned quality and reliability gating are empirical model investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: image-level uncertainty and matched controls are suitable; scene metadata and final label mapping need checking. |
| Three-member structure | 12 | 4 | 9.6 | Medium: A changes masks, B predicts fixed-mask quality and C tests cue fusion independently. |
| Real-world significance | 9 | 3 | 5.4 | Medium: transparent surfaces challenge visual perception, but downstream user benefit is not measured. |
| Compute/storage | 5 | 3 | 3.0 | Medium-low: compact RGB route is plausible; nearest work includes much larger hardware and runtime has not been measured. |
| Prototype | 3 | 4 | 2.4 | Medium-high: offline image/mask viewer is straightforward. |
| **Normalised total / 100** | **98** | | **68.0** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means supported at bounded design level, not demonstrated execution. Unknown gates prevent qualification. Provisional scores retain the existing comparison convention; they do not override the rule to resolve gates before qualifying a topic.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the source comparisons document a specific visual-model failure; downstream benefits remain untested. |
| 2. ML essential | Pass | Training or systematically adapting visual models is essential to the research question. |
| 3. Train/adapt models | Pass | Sections 4 and 6 specify trainable objectives, modules or predictors using existing data. |
| 4. Existing data accessible | Pass | Section 5 records an original public release, existing labels and a documented loading route, with access-check limits. |
| 5. No unavailable human evaluation | Pass | All central outcomes use existing masks, boxes or category labels; no new participant or expert annotations. |
| 6. Precise research gap | Unknown | The extra value beyond TransCues, UncertSAM and other uncertainty-aware segmentation methods remains unverified. |
| 7. Beyond application assembly | Pass | The three interventions are evaluated through model-level baselines and ablations, not only a prototype. |
| 8. Objective evaluation | Pass | Section 7 specifies objective metrics, leakage controls, comparison baselines and uncertainty analysis. |
| 9. 6–8 month feasibility | Pass | The bounded configuration and reduced-method fallback are plausible in 6–8 months; this is an estimated design-level pass. |
| 10. Three connected contributions | Pass | Three related investigations each have an unchanged-baseline comparison and independently assessable outcome. |
| 11. No specialised/continuous high-end compute | Pass | The core uses existing RGB imagery and an occasional modest GPU; no new sensors or continuous high-end compute. |
| 12. Manageable responsible use | Unknown | The precise dataset-image terms, particularly for the v2 derivative and redistribution, are not explicit in the inspected original pages. |
| 13. Useful negative findings | Pass | Section 7 defines an informative negative result and alternatives to outperforming the strongest baseline. |

**Decision:** Lower-priority exploratory candidate until dataset terms and the distinction from uncertainty-aware methods are resolved.

**Next decision point:** Resolve the original dataset terms and load a small mask sample before investing in a method comparison. Discuss the evidence and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/cv-expansion-records.json).
