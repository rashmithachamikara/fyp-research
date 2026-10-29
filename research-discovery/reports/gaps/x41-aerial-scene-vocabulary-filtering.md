[← Research candidates](../research-candidates.md)

# Choosing useful object names before searching aerial images

**ID:** X41 · **Area:** Computer vision — open-vocabulary aerial detection

**Status:** Provisional; Investigate; learned filtering gap and dataset route unresolved; not qualified · **Imported:** 30 October 2026

**Provisional score:** 64.3/100 · No model training or timing performed.

**In plain language:** Learn a per-image shortlist of possible object classes without using the correct test labels to choose it.

**Origin:** supplied shortlist, rank 8, page(s) 6. Its source verdict was “GO with reframing”. This brief uses the team’s current criteria; the source rank and verdict are not our qualification decision. [Import record](../../metadata/pdf-shortlist-import.json).

## 1. Problem

An open-vocabulary detector looks for objects described by words. Searching an aerial image for many similar class names can create false detections. Using the known correct classes makes the task easier, but those answers are not available for a new image.

## 2. Research gap and question

**Question:** Can a learned image-based class shortlist reduce false detections at a fixed vocabulary budget without hiding rare or unfamiliar aerial objects?

**What is still uncertain:** The cited evaluation reports serious aerial transfer problems and compares vocabulary settings. The proposed investigation is a learned, deployable vocabulary selector rather than an oracle that already knows the labels. Scene filtering and few-shot adaptation are not automatically new; SCORE, DisDop and RS-MPOD from the PDF need methods comparisons.

**Hypothesis and alternative:** A small scene-aware selector will reduce semantic confusion while retaining rare-class recall. An alternative is that it improves precision only by excluding difficult objects from consideration.

## 3. Evidence from closest work

This is a bounded import check, not a complete novelty audit. “Checked” below refers to the stated abstract or source page, not a reproduction of the study. The supplied PDF’s wider search and verification claims are not independently certified.

| Source | What it supports | Reading limit |
|---|---|---|
| [Do Open-Vocabulary Detectors Transfer to Aerial Imagery?](https://arxiv.org/abs/2601.22164) | The abstract reports strong semantic confusion and vocabulary-sensitive performance on aerial images. Oracle vocabulary results do not demonstrate an achievable learned-selector gain. | Primary abstract checked; methods not reviewed. |
| [Nearest methods and data leads in supplied shortlist](file:///C:/Users/rashm/Downloads/FYP_Topic_Shortlist.pdf) | The PDF names SCORE, DisDop, RS-MPOD and LAE-80C; these leads need exact records, methods and release terms. | Supplied PDF read; named method/data releases not independently inspected. |

## 4. Proposed approach

Freeze one detector initially and train a small class-ranking head using training images only. Pass the same number of candidate names to each detector. Then test a limited few-shot adaptation on separate training examples. Include a full-vocabulary run so the selector cannot hide its missed classes.

**Prototype:** demonstrate the same research pipeline on held-out existing examples, showing its output, errors and uncertainty. The interface is supporting work, not an individual research contribution.

## 5. Data and resources

**Data and access:** The cited paper names LAE-80C. Its downloadable images, licence, annotation mapping and train/test groups have not been inspected. A second aerial benchmark is a fallback lead only after class mapping and reuse terms are verified. True classes in test images may be used for scoring, never for selecting the allowed vocabulary.

**Resources:** Estimate only: cached image features and a small selector should limit training, but detector inference at high aerial resolution may be costly. Start with one model and a bounded image subset; measure peak memory before adding methods.

**Fallback:** Use a fixed training-derived class prior or coarse scene classifier at the same vocabulary budget. If rare-class recall collapses or close methods already cover the idea, abandon the proposed selector contribution.

These are feasibility estimates, not demonstrated training costs. The PDF’s resource allowance does not establish this team’s actual GPU or paid-service access.

## 6. Three-member contributions

All members address the shared question in section 2. Each investigation starts from the same unchanged baseline so that another member’s proposed improvement is not a prerequisite.

| Member | Question and hypothesis | Method, comparison and removal test | Independently assessable result |
|---|---|---|---|
| A: Learned class shortlist | Can scene features select classes without an oracle? H: a trained selector beats a fixed frequency prior. | Compare full vocabulary, random/frequency shortlists and a learned head; remove scene features. | Detection AP and rare-class recall at the same vocabulary budget. |
| B: Confusion-aware decisions | Can calibration reduce similar-name false positives? H: learned confusion correction helps beyond filtering. | Train on unchanged detector outputs; compare raw scores and classwise thresholds; remove confusion features. | False-positive reduction at matched object recall, including classes omitted by the selector. |
| C: Few-shot recovery | Can small adaptation recover rare classes missed by filtering? H: a limited adapter helps on held-out scenes. | Compare no adaptation and equal-budget few-shot adaptation; remove rare-class reweighting. | AP by label budget and rare class, with vocabulary settings held fixed. |

Shared data access is a common prerequisite. A failed proposed method can still produce an interpretable comparison. Papers are optional; the work must remain attributable through experiments and removal tests. Where the gate table marks the team structure Unknown, the shared data barrier prevents treating this as an execution-ready split.

## 7. Evaluation

- **Primary measure:** Bounding-box AP over the full target class set, with rare-class recall and false detections per image. Also report class-shortlist recall so omitted classes remain visible in the results.
- **Keep data separate:** Hold out scenes, geographic areas and overlapping source tiles where metadata permit. Keep few-shot examples in training only; explicitly separate known-class and genuinely unseen-class claims.
- **Baselines:** A conventional closed-set detector as a reference, OWLv2 or Grounding DINO with full vocabulary, fixed class priors and the nearest scene-filtering approaches. An oracle vocabulary is an upper-bound diagnostic only.
- **Removal tests:** use the member-specific tests above; keep data, tuning effort and inference budgets comparable.
- **Uncertainty, error analysis and useful negative findings:** Analyse rare objects, similar class names, object size and unseen scenes. Bootstrap by scene and use three training seeds. Useful findings include no improvement over a fixed prior or a precision gain purchased by lost recall.
- **Claim limit:** benchmark findings support the stated task and conditions. They do not establish reliable real-world deployment or a guaranteed benefit for users.

## 8. Score and next decision

**Provisional score: 64.3/100; not qualified.** Investigate; learned filtering gap and dataset route unresolved. Ratings assess the imported proposal and access risks, not achieved results. Unknown gates block qualification; failed gates reject the current design regardless of score.

### Weighted rubric

The existing nine weights total 98. Scores are normalised to 100; decimals reflect arithmetic, not certainty. These comparison scores follow the existing provisional-scoring policy and do not override the gates.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: a clear non-oracle contrast exists, but recent filtering methods may overlap. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: dataset download, rights and grouping are not inspected. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: a small selector is manageable; detector reproduction needs checking. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: selection, calibration and few-shot adaptation involve learned methods. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: fair full-class metrics are specified but grouping metadata are unverified. |
| Three-member structure | 12 | 4 | 9.6 | Medium: selector, correction and few-shot recovery can each use unchanged base outputs. |
| Real-world significance | 9 | 4 | 7.2 | Medium: reducing aerial semantic confusion is useful; no deployment improvement is established. |
| Compute/storage | 5 | 3 | 3.0 | Low-medium: cached features help, but high-resolution detector cost is unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: showing selected classes and missed objects gives a bounded demonstration. |
| **Normalised total / 100** | **98** | | **64.3** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 defines a concrete failure and affected users; its local magnitude is not measured. |
| 2. ML essential | Pass | The shared question concerns learned predictions rather than only an interface. |
| 3. Train/adapt models | Pass | The bounded design includes training or systematic model adaptation. |
| 4. Existing data accessible | Unknown | LAE-80C images, labels, licence and scene grouping have not been inspected. |
| 5. No unavailable human evaluation | Pass | The retained plan uses existing labels and excludes new participants or expert labelling. |
| 6. Precise research gap | Unknown | SCORE, DisDop and RS-MPOD require comparison; future work does not prove novelty. |
| 7. Beyond application assembly | Pass | The proposal specifies learning experiments, comparisons and removal tests. |
| 8. Objective evaluation | Unknown | Geographic groups and full target-class scoring require dataset inspection. |
| 9. 6–8 month feasibility | Unknown | A small detector/selector reproduction must establish runtime and data preparation effort. |
| 10. Three connected contributions | Pass | Three connected research questions have separate comparisons and attributable results. |
| 11. No specialised/continuous high-end compute | Pass | The retained scope starts with small models or cached features and no dedicated hardware. |
| 12. Manageable data reuse | Unknown | The exact combination of data, model and derivative-output reuse terms is not verified. |
| 13. Useful negative findings | Pass | Section 7 identifies useful findings even if the proposed method does not improve performance. |

**Next decision:** Inspect LAE-80C access and the nearest filtering methods before asking the supervisor to approve a specific selector experiment.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source and import limits](../../metadata/pdf-shortlist-import.json)
