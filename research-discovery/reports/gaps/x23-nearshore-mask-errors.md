[← Research candidates](../research-candidates.md)

# Keeping nearshore ships when coastline masks are wrong

**ID:** X23 · **Area:** Computer vision — nearshore SAR detection · **Status:** Provisional opportunity; not qualified

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

Harbours contain bright structures that resemble SAR ships. Aggressive land masks remove false alarms, but a mask that is shifted or too conservative can hide genuine nearshore vessels.

## 2. Research gap and question

**Question:** Can a detector learn when to override an unreliable coastline mask while retaining a fixed harbour false-alarm budget?

**Tentative hypothesis:** A boundary-reliability gate preserves nearshore ship recall under mask errors better than hard exclusion and naive mask fusion.

**Rival explanation:** Gains are explained by adding coastal examples or loosening a threshold, not by learning mask reliability.

**What is already addressed / what remains inferred:** Sea–land guidance, filtering, scattering-aware fusion and hard-negative mining already exist. The narrower proposed test is the coupled cost of realistic mask errors and recovering masked ships; it remains an inferred opportunity.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [SLA-Net: sea–land-aware SAR detection (2025)](https://doi.org/10.3390/rs17213576) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/rs17213576) | Mask-guided backbone, feature pyramid and detection filtering already exist. | Hierarchical mask guidance and land-ratio filtering. Publisher-indexed method passages. |
| [Scattering–Semantic Collaborative Learning for Inshore SAR Ship Detection (2026)](https://doi.org/10.3390/rs18183110) | Inshore structural deterioration and feature confusion already motivate scattering-aware detection. | Section 3: asymmetric DINO, scattering branch and gated fusion. Publisher-indexed method excerpts; direct page returned 429. |
| [HRSID author dataset release](https://github.com/chaozhong2010/HRSID) | Lists 5,604 images, 16,951 ships and 400 pure-background chips; code licence alone does not settle imagery reuse. | README: dataset, inshore/outshore labels, negative samples and licence. Author README inspected; archives not downloaded. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Train a compact image detector with a mask-reliability branch, and an auxiliary boundary head using existing sea–land masks. Distinguish naturally uncertain boundaries from deliberately shifted/eroded masks; no new expert mask drawing.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

HRSID documents 5,604 images, 16,951 ship instances, inshore/outshore labels and 400 pure-background chips. SL-SSDD provides existing masks. Archives, shared acquisition identifiers and imagery reuse terms have not been verified; the repository's code licence is insufficient by itself.

**Original sources:** [HRSID author dataset release](https://github.com/chaozhong2010/HRSID); [SL-SSDD author sea–land masks](https://github.com/Han-Ke/SL-SSDD).

**Fallback and claim boundary:** Evaluate controlled mask errors on a reusable subset with existing masks. If no reliable shoreline alignment is recoverable, stop this topic rather than calling arbitrary pixel shifts real coastal errors.

**Unmeasured resource estimate:** Estimate: compact detector on an occasional 8–12 GB GPU, 16 GB RAM and 5–20 GB storage. A full dual-branch DINO reproduction is not a required training dependency.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: mask reliability | When should a detector override the coastline? H: A reliability gate reduces missed boundary ships. | Learn image/mask conflict features and a gating head. | Image-only and SLA-style hard/soft masking; remove reliability input. | Recall versus coastal false alarms across mask quality. |
| B: coastal confusers | Can existing background examples improve ship–structure separation? H: A contrastive loss reduces pier-like false detections. | Train a small coastal contrastive detector head. | Standard detection loss and negative mining; remove hard-negative contrast. | Error rates on held-out harbour/background chips. |
| C: uncertain boundaries | Can mask uncertainty be predicted from existing labels? H: A learned boundary distribution is safer than a fixed-width buffer. | Fit a probabilistic auxiliary boundary model. | Hard mask, dilated buffers and soft mask; remove uncertainty. | Coverage and detection cost near uncertain boundaries. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** Nearshore ship recall at a fixed false positives/background-chip budget; report AP and offshore recall as secondary outcomes.
- **Split:** Group source acquisitions and coastal regions where recoverable. If scene identifiers are missing, audit duplicates and limit claims to image-level benchmark testing; do not claim geographic generalisation.
- **Baselines:** Compact detector; SLA-Net mask-guidance/filtering; S-DINO as the strong recent methodological neighbour, with compute-matched controls if full reproduction is infeasible.
- **Ablations:** Hard/soft/learned mask; shift versus erosion; coastal negatives; same data/backbone/threshold budget. Report clean-mask performance too.
- **Uncertainty and error analysis:** Acquisition or image-group bootstrap, several seeds; inspect small boats, piers, bridges, islands and mask-distance bands. Simulated mask errors are a separate test set.
- **Useful findings without outperforming the strongest baseline:** Show that image-only detection is more reliable, or identify the mask-error level beyond which guidance becomes harmful.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 70.8/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

### Weighted rubric

Nine relative weights total 98; scores are normalised to 100. Decimal precision is arithmetic, not confidence.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: Specific failure is testable, but overlap with the cited neighbours remains unresolved; no certified novelty. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium-low: An original-source dataset route exists, but labels, access or evaluation support remain incomplete. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: Completion depends on resolving data or methodological prerequisites early. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: Losses, trainable fusion/state models or calibration are substantive ML investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: Explicit grouped evaluation, controls and uncertainty are defined, conditional on the documented data checks. |
| Three-member structure | 12 | 4 | 9.6 | Medium: Three related model investigations can each use an unchanged common baseline; data dependencies remain explicit. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: A specific observation/identity error affects maritime research; operational benefits remain untested. |
| Compute/storage | 5 | 4 | 4.0 | Medium: Bounded subsets and occasional GPU use appear manageable; storage/time estimates are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **70.8** | **Not qualified.** |

### Mandatory gates

Pass refers to the bounded proposal design; it is not a completed experiment. Unknown gates are not waived.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest sources identify a concrete observation or identity failure; benefit is not yet demonstrated. |
| 2. ML essential | Pass | The research question concerns learned prediction, representation or adaptation. |
| 3. Train/adapt models | Pass | Sections 4 and 6 specify models/objectives to train or adapt, not an external API-only application. |
| 4. Existing data accessible | Unknown | Section 5 identifies missing access, label, alignment or independent-reference requirements; adjacent public data do not resolve them. |
| 5. No unavailable human evaluation | Pass | The bounded proposal uses existing observations/labels. No new fieldwork, interviews or expert annotation is required; absent existing labels block selection. |
| 6. Precise research gap | Unknown | The distinction beyond close prior methods remains an inferred opportunity, not a verified novel gap. |
| 7. Beyond application assembly | Pass | Trainable methodological interventions and ablations go beyond assembling a vessel dashboard. |
| 8. Objective evaluation | Pass | Section 7 defines objective bounded endpoints, grouped splits and baseline/ablation controls; data limitations constrain claims. |
| 9. 6–8 month feasibility | Unknown | Data prerequisites must be resolved before completion in 6–8 months can be supported. |
| 10. Three connected contributions | Pass | Each member has a question, trained intervention, baseline/ablation and attributable result; all can use unchanged common features/models. |
| 11. No specialised/continuous high-end compute | Pass | Core design excludes raw global ingestion, new hardware and continuous high-end or multi-GPU pretraining; estimates appear in section 5. |
| 12. Manageable data reuse | Unknown | Dataset imagery/API terms remain to verify for the exact intended subset. |
| 13. Useful negative findings | Pass | Section 7 defines useful findings if the intervention loses or the stronger claim is not identifiable. |

**Next decision point:** Verify imagery terms, source acquisition groups and mask alignment before using coastal-transfer claims.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
