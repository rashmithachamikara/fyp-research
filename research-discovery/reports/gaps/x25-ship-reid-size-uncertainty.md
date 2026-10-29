[← Research candidates](../research-candidates.md)

# Recognising the same ship when image-derived size is unreliable

**ID:** X25 · **Area:** Computer vision — optical/SAR vessel re-identification · **Status:** Provisional opportunity; not qualified

[View the HTML infographic](../x25-vessel-size-infographic.html).

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

TransOSS already uses crop dimensions and ground sampling distance to approximate physical size. Its paper notes that crops are not exact hull boundaries. An identity model may over-trust those approximate measurements.

## 2. Research gap and question

**Question:** Can uncertainty-aware size fusion improve cross-modal re-identification under crop/scale error without sacrificing discrimination between similarly sized vessels?

**Tentative hypothesis:** Reliability-weighted size embeddings are less brittle than deterministic size fusion at a matched visual backbone.

**Rival explanation:** Size-blind visual features already solve the problem, or the apparent gain comes from easier gallery composition.

**What is already addressed / what remains inferred:** Physical-size embeddings, modality alignment, scale-invariant features and identity prototypes already exist. The inferred opportunity is a controlled test of unreliable size information and same-size confusers, not adding size or alignment for the first time.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [Cross-modal Ship Re-Identification via Optical and SAR Imagery (ICCV 2025)](https://arxiv.org/abs/2506.22027) | TransOSS already uses approximate crop/GSD physical size; crop bounds are not exact hull dimensions. | Section 4.2 size embedding; Table 1 dataset. Full HTML methods inspected. |
| [MOS: modality alignment for optical–SAR ship re-identification (2025 preprint)](https://arxiv.org/abs/2512.03404) | Denoising/alignment and generated pseudo-SAR fusion already exist; published heavy training is unsuitable as a mandatory team dependency. | Methods and implementation settings. Full HTML inspected. |
| [SDF-Net cross-modal ship re-identification (2026 preprint)](https://arxiv.org/abs/2603.12588) | Structure/appearance disentanglement and cross-modal identity prototypes are established neighbouring methods. | Disentanglement, identity prototypes and batch construction. Full HTML inspected. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Reuse released TransOSS features/weights and train a compact uncertainty-aware size fusion head. Check actual TIFF/GSD fields before treating metadata as measurements. Include size-blind and matched-size galleries.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

The 82.9 MB HOSS archive was downloaded and parsed. Its main train/query/gallery directories contain 1,063/176/593 images; extra protocol folders duplicate crops. Identity/sequence/frame/modality filename fields and CC BY 4.0 terms were checked. Pixels, TIFF GSD fields and checkpoint loading were not checked. Visual identity labels do not establish MMSI or registry identity.

**Original sources:** [HOSS author dataset](https://doi.org/10.5281/zenodo.15860212); [HOSS/TransOSS author code and model route](https://github.com/Alioth2000/Hoss-ReID).

**Fallback and claim boundary:** Use crop padding/scale perturbations with explicit synthetic-error claims, and a visual-only model if usable size metadata cannot be reconstructed. Do not equate changed image pixels with a change in true vessel dimensions.

**Unmeasured resource estimate:** Estimate: cached features and small heads on CPU; optional 8–12 GB GPU fine-tuning; 2–10 GB including one checkpoint/cache. Reuse weights instead of the authors' multi-GPU pretraining.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: uncertain size fusion | Can size uncertainty prevent wrong identity matches? H: A learned variance gate improves robustness. | Train probabilistic size embeddings and a fusion head. | TransOSS deterministic size and size-blind head; remove variance. | Retrieval change across size-error levels. |
| B: same-size discrimination | Does a structure-focused loss distinguish size-matched ships? H: Matched-size hard negatives improve identity discrimination. | Train an identity/metric head with controlled hard-negative sampling. | Standard triplet/contrastive loss and SDF-style features; remove matching constraint. | Performance on same-size versus mixed-size galleries. |
| C: trustworthy match confidence | Can match confidence reflect crop/scale reliability? H: Reliability-aware calibration reduces wrong confident matches. | Fit a pair-confidence model on development identities. | Distance threshold and global calibration; remove quality features. | Risk–coverage curve under crop/scale changes. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** Cross-modal rank-1 retrieval accuracy on a fixed gallery, with mAP and same-size-gallery performance secondary; confidence research additionally reports false-match risk versus coverage.
- **Split:** Preserve identity-disjoint train/development/test groups and keep all crops/protocol copies of an image together. Check sequence overlap; a new geographic claim is unsupported by the present metadata.
- **Baselines:** TransOSS author code/weights, conventional visual embedding plus metric head, and available SDF-Net/MOS feature controls. Heavy generative pretraining is excluded; incomplete code access must be reported.
- **Ablations:** Size-blind/deterministic/uncertain size; crop padding versus resizing; same-size negative sampling; calibration alone. Keep backbone and gallery composition fixed.
- **Uncertainty and error analysis:** Bootstrap test identities with repeated gallery sampling; report small/large ships, RGB→SAR and SAR→RGB, distractors and similar-sized confusions.
- **Useful findings without outperforming the strongest baseline:** Show that deterministic size dominates, that size uncertainty offers no benefit, or that reported gains disappear with matched-size confusers.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 76.7/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

### Weighted rubric

Nine relative weights total 98; scores are normalised to 100. Decimal precision is arithmetic, not confidence.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: Specific failure is testable, but overlap with the cited neighbours remains unresolved; no certified novelty. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: HOSS archive and CC BY 4.0 terms inspected; metadata details and model loading remain untested. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: Cached features/compact models fit a bounded design; execution remains estimated. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: Losses, trainable fusion/state models or calibration are substantive ML investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: Explicit grouped evaluation, controls and uncertainty are defined, conditional on the documented data checks. |
| Three-member structure | 12 | 4 | 9.6 | Medium: Three related model investigations can each use an unchanged common baseline; data dependencies remain explicit. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: A specific observation/identity error affects maritime research; operational benefits remain untested. |
| Compute/storage | 5 | 4 | 4.0 | Medium: Bounded subsets and occasional GPU use appear manageable; storage/time estimates are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **76.7** | **Not qualified.** |

### Mandatory gates

Pass refers to the bounded proposal design; it is not a completed experiment. Unknown gates are not waived.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest sources identify a concrete observation or identity failure; benefit is not yet demonstrated. |
| 2. ML essential | Pass | The research question concerns learned prediction, representation or adaptation. |
| 3. Train/adapt models | Pass | Sections 4 and 6 specify models/objectives to train or adapt, not an external API-only application. |
| 4. Existing data accessible | Pass | HOSS is downloadable and licensed; its identity-labelled crops support the bounded benchmark claim. Size fields/pixels remain to inspect. |
| 5. No unavailable human evaluation | Pass | The bounded proposal uses existing observations/labels. No new fieldwork, interviews or expert annotation is required; absent existing labels block selection. |
| 6. Precise research gap | Unknown | The distinction beyond close prior methods remains an inferred opportunity, not a verified novel gap. |
| 7. Beyond application assembly | Pass | Trainable methodological interventions and ablations go beyond assembling a vessel dashboard. |
| 8. Objective evaluation | Pass | Section 7 defines objective bounded endpoints, grouped splits and baseline/ablation controls; data limitations constrain claims. |
| 9. 6–8 month feasibility | Pass | The cached-feature or compact-model route is a plausible 6–8 month design, not a demonstrated completion/runtime guarantee. |
| 10. Three connected contributions | Pass | Each member has a question, trained intervention, baseline/ablation and attributable result; all can use unchanged common features/models. |
| 11. No specialised/continuous high-end compute | Pass | Core design excludes raw global ingestion, new hardware and continuous high-end or multi-GPU pretraining; estimates appear in section 5. |
| 12. Manageable data reuse | Pass | The bounded public-data route uses a verified CC BY 4.0 release; source attribution and label interpretation remain required. |
| 13. Useful negative findings | Pass | Section 7 defines useful findings if the intervention loses or the stronger claim is not identifiable. |

**Next decision point:** Decode a few existing TIFFs, verify the size feature route and load a released checkpoint; then reproduce a size-blind versus deterministic-size control.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
