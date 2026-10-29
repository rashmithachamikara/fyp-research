[← Research candidates](../research-candidates.md)

# Knowing when a satellite segmentation model should abstain

**ID:** X42 · **Area:** Computer vision — geospatial segmentation reliability

**Status:** Provisional; Defer; major overlap and a citation mismatch; not qualified · **Imported:** 30 October 2026

**Provisional score:** 51.4/100 · No model training or timing performed.

**In plain language:** Test reliable abstention after adapting a geospatial model; existing work already covers much of this question.

**Origin:** supplied shortlist, rank 9, page(s) 6. Its source verdict was “Weakest; topic to avoid”. This brief uses the team’s current criteria; the source rank and verdict are not our qualification decision. [Import record](../../metadata/pdf-shortlist-import.json).

## 1. Problem

A segmentation model marks pixels such as flooded ground or a landslide scar. In an unfamiliar region, confident errors can be hard to recognise. Abstaining means explicitly leaving some predictions undecided; it does not make the remaining map automatically safe.

## 2. Research gap and question

**Question:** After model adaptation, can a small reliability model identify errors in a new region better than standard uncertainty scores at the same retained mapping coverage?

**What is still uncertain:** The supplied PDF already places this among topics to avoid. SHRUG-FM describes uncertainty, out-of-distribution detection and selective prediction for flood and landslide segmentation, which strongly overlaps the broad idea. Also, arXiv:2606.14081 is a Clay-CNN landslide segmentation study, not the frozen-versus-LoRA calibration study described in the PDF. A distinct remaining contribution is not established.

**Hypothesis and alternative:** A reliability head trained on source-region errors could improve error ranking after adaptation. Alternatives are that standard uncertainty already suffices or that calibration fails under geographic shift.

## 3. Evidence from closest work

This is a bounded import check, not a complete novelty audit. “Checked” below refers to the stated abstract or source page, not a reproduction of the study. The supplied PDF’s wider search and verification claims are not independently certified.

| Source | What it supports | Reading limit |
|---|---|---|
| [SHRUG-FM: Reliability-Aware Foundation Models for Earth Observation](https://meetingorganizer.copernicus.org/EGU26/EGU26-9940.html) | This conference abstract explicitly covers uncertainty, rejection and selective prediction for flood and landslide segmentation. It is strong overlap evidence, not a full methods review. | Primary conference abstract checked; full methods/code not reviewed. |
| [Clay-CNN Hybrids](https://arxiv.org/abs/2606.14081) | The actual abstract concerns Clay-assisted landslide segmentation and LoRA, not the calibration comparison attributed to this identifier in the supplied PDF. | Primary abstract checked; methods not reviewed. |

## 4. Proposed approach

If reopened, choose one task, such as post-event landslide segmentation. Compare a conventional model, a frozen foundation encoder with a learned decoder and a small adapter. Evaluate standard uncertainty before proposing another head. Do not expand simultaneously to floods, fires and landslides.

**Prototype:** demonstrate the same research pipeline on held-out existing examples, showing its output, errors and uncertainty. The interface is supporting work, not an individual research contribution.

## 5. Data and resources

**Data and access:** Landslide4Sense is named by the Clay-CNN paper, but its actual files, reuse terms and event/geographic group metadata have not been inspected in this import. Suitable masks and groups are prerequisites. X02 also concerns satellite confidence, but this candidate concerns pixel-level hazard segmentation rather than land-cover classification.

**Resources:** Estimate only: one task and cropped images may fit occasional GPU access. Multiple full-fine-tuning runs could exceed available memory and time. Full-model adaptation is an optional comparison only after a measured pilot.

**Fallback:** Keep the idea parked unless full-method comparison exposes a specific unanswered failure. A narrow repeat of frozen versus adapter versus full fine-tuning is not automatically enough novelty for the project.

These are feasibility estimates, not demonstrated training costs. The PDF’s resource allowance does not establish this team’s actual GPU or paid-service access.

## 6. Three-member contributions

All members address the shared question in section 2. Each investigation starts from the same unchanged baseline so that another member’s proposed improvement is not a prerequisite.

| Member | Question and hypothesis | Method, comparison and removal test | Independently assessable result |
|---|---|---|---|
| A: Adaptation and confidence | Does adaptation change error confidence? H: the best mask model need not have the best error ranking. | Compare frozen decoder training and limited adaptation with unchanged data; remove adaptation. | Mask F1/IoU and error-ranking quality in held-out regions. |
| B: Error prediction | Does a small reliability head add value beyond standard scores? H: learned error prediction improves selective risk. | Compare entropy, ensemble uncertainty and a trained head; remove context features. | Risk–coverage curves against the same segmentation outputs. |
| C: Calibration under shift | Does calibration survive a new event or region? H: spatially grouped calibration transfers better than random pixels. | Compare no calibration, temperature scaling and learned scaling; remove spatial grouping. | Calibration error and retained-region error, at matched coverage. |

Shared data access is a common prerequisite. A failed proposed method can still produce an interpretable comparison. Papers are optional; the work must remain attributable through experiments and removal tests. Where the gate table marks the team structure Unknown, the shared data barrier prevents treating this as an execution-ready split.

## 7. Evaluation

- **Primary measure:** Area under the risk–coverage curve with full-coverage segmentation F1/IoU and class-specific recall. Report how many positive hazard pixels are rejected; abstention can hide the difficult cases.
- **Keep data separate:** Hold out whole geographic areas/events. Separate training, calibration and testing by source tile/event; nearby overlapping crops cannot appear on both sides.
- **Baselines:** A conventional U-Net, a foundation-model decoder/adapter baseline, entropy and ensemble uncertainty, and SHRUG-FM where its code permits. Exact code and calibration-method availability remain unchecked.
- **Removal tests:** use the member-specific tests above; keep data, tuning effort and inference budgets comparable.
- **Uncertainty, error analysis and useful negative findings:** Bootstrap by event/region and repeat training with three seeds. Analyse small affected areas, boundaries and region shift. Useful negative findings include standard entropy matching the trained head or adaptation improving masks while harming confidence.
- **Claim limit:** benchmark findings support the stated task and conditions. They do not establish reliable real-world deployment or a guaranteed benefit for users.

## 8. Score and next decision

**Provisional score: 51.4/100; not qualified.** Defer; major overlap and a citation mismatch. Ratings assess the imported proposal and access risks, not achieved results. Unknown gates block qualification; failed gates reject the current design regardless of score.

### Weighted rubric

The existing nine weights total 98. Scores are normalised to 100; decimals reflect arithmetic, not certainty. These comparison scores follow the existing provisional-scoring policy and do not override the gates.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 1 | 3.2 | Medium-high: SHRUG-FM strongly overlaps the broad proposal; the other citation is misdescribed. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: masks, licences and geographic groups are not inspected. |
| Feasibility and learning curve | 14 | 2 | 5.6 | Low: a demanding training comparison remains without a precise contribution. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: segmentation adaptation and error-model training have ML depth. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: metrics are suitable, but data grouping and baseline code remain unresolved. |
| Three-member structure | 12 | 3 | 7.2 | Low-medium: three questions can be framed, but substantial novelty for the shared scope is weak. |
| Real-world significance | 9 | 4 | 7.2 | Medium: reliable hazard maps matter; this is not an operational warning study. |
| Compute/storage | 5 | 2 | 2.0 | Low: repeated segmentation/full-model adaptation may exceed modest resources. |
| Prototype | 3 | 4 | 2.4 | Medium: an uncertainty-overlay viewer is feasible once models work. |
| **Normalised total / 100** | **98** | | **51.4** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 defines a concrete failure and affected users; its local magnitude is not measured. |
| 2. ML essential | Pass | The shared question concerns learned predictions rather than only an interface. |
| 3. Train/adapt models | Pass | The bounded design includes training or systematic model adaptation. |
| 4. Existing data accessible | Unknown | Reusable masks and geographic/event splits have not been inspected. |
| 5. No unavailable human evaluation | Pass | The retained plan uses existing labels and excludes new participants or expert labelling. |
| 6. Precise research gap | Unknown | SHRUG-FM covers much of the proposal; no distinct remaining gap is established. |
| 7. Beyond application assembly | Pass | The proposal specifies learning experiments, comparisons and removal tests. |
| 8. Objective evaluation | Unknown | Region/event labels and calibration/test separation are not verified. |
| 9. 6–8 month feasibility | Unknown | The scope and training budget remain unresolved. |
| 10. Three connected contributions | Unknown | The three questions may overlap too much once existing reliability work is reproduced. |
| 11. No specialised/continuous high-end compute | Unknown | Repeated full-model adaptation has not been shown to fit available hardware. |
| 12. Manageable data reuse | Unknown | The exact combination of data, model and derivative-output reuse terms is not verified. |
| 13. Useful negative findings | Pass | Section 7 identifies useful findings even if the proposed method does not improve performance. |

**Next decision:** Keep this candidate deferred and discuss it with the supervisor only if a full nearest-neighbour comparison reveals a specific unanswered question.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source and import limits](../../metadata/pdf-shortlist-import.json)
