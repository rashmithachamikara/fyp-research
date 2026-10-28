[← Research candidates](../research-candidates.md)

# Knowing when a ship wake is usable evidence

**ID:** X27 · **Area:** Computer vision — SAR hull/wake analysis · **Status:** Provisional opportunity; not qualified

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

Wake detection can add movement evidence when a hull is small or ambiguous. SAR wake visibility depends on the observation conditions, so wake absence alone is not evidence of a stationary or absent vessel.

## 2. Research gap and question

**Question:** Can a learned wake-usability model improve hull detection or wake association under poor visibility compared with ordinary joint hull/wake fusion?

**Tentative hypothesis:** Visibility-aware fusion limits harmful wake evidence while retaining gains on clearly visible wakes.

**Rival explanation:** Joint detection with more negative examples is sufficient; the visibility head learns only sensor/dataset shortcuts.

**What is already addressed / what remains inferred:** Joint hull/wake detection, environmental wake modelling and synthetic wake generation are established. The narrower inferred question concerns reliability when wake cues are absent, misleading or assigned to the wrong nearby ship.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [UEIKAP: annotated optical/SAR ship wakes (2026)](https://doi.org/10.1016/j.apor.2026.105245) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1016/j.apor.2026.105245) | SAR wake visibility is condition-dependent; the project already uses wake/hull labels and environmental information. | Abstract and author ESA poster. Publisher abstract and author poster inspected; not full journal methods. |
| [Non-Linear Modeling of Detectability of Ship Wake Components (2021)](https://doi.org/10.3390/rs13020165) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/rs13020165) | Wake visibility modelling using vessel, sensor and environmental variables predates this proposal. | Detectability model and influencing variables. Publisher method passages inspected. |
| [Towards real-time detection of ships and wakes with lightweight deep learning (2022)](https://doi.org/10.1016/j.rse.2022.113345) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1016/j.rse.2022.113345) | Joint hull/wake detection is established; absence of visibility treatment cannot be inferred from the abstract. | Abstract: joint ship/wake detection. Scholarly abstract only; complete methods not inspected. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Train a compact hull/wake model and a learned usability/association head using existing labels. Keep directly annotated wake presence separate from physical wake generation; do not invent absent-wake truth.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

UEIKAP's CC BY 4.0 licence, README and manifests were checked. SAR and optical archives are about 1.57 GB and 11.96 GB; AIS directories exist. Imagery labels, negative coverage, vessel linking and reproducible splits were not parsed. Optical TIFFs are listed as a placeholder; modalities are not assumed simultaneous pairs.

**Original sources:** [UEIKAP author dataset](https://doi.org/10.5281/zenodo.18391027).

**Fallback and claim boundary:** Start with the SAR archive and existing labels only. If representative no-wake/background examples are absent, restrict the endpoint to labelled-wake delineation under observed quality, or stop the reliability claim.

**Unmeasured resource estimate:** Estimate: 8–12 GB GPU, 16 GB RAM and 10–40 GB storage including extracted subset/caches. No new sea trials or hydrodynamic simulation is necessary.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: wake usability | Can a learned quality score identify harmful wake evidence? H: Gating beats unconditional fusion. | Train a small usability gate. | Hull-only and joint hull/wake model; remove gate. | Hull/wake performance by recorded image quality. |
| B: wake-to-ship association | Can geometry and learned appearance reject a neighbouring ship's wake? H: Learned association reduces wrong pairings. | Train a pairwise association head using existing linked annotations. | Nearest-axis/angle rule and pair MLP; remove learned geometry. | Association error if links exist; otherwise explicitly unavailable. |
| C: negative-evidence calibration | How should absence affect confidence? H: Visibility-conditioned calibration avoids confident absence conclusions. | Fit a reliability model on existing positive/negative observations. | Global threshold/calibration; remove visibility conditioning. | Calibration and false-positive cost on supported negative exposure. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** Hull recall at fixed false alarms and wake-mask F1/IoU on annotated images; wake association accuracy only if the released labels provide links and adequate negatives.
- **Split:** Group acquisition, sensor and vessel/sequence when IDs permit. Prevent nearby chips and repeated observations crossing splits; test SAR/optical separately before any cross-modal claim.
- **Baselines:** Hull-only compact detector; ordinary joint ship/wake model; published lightweight joint detection and visibility-regression approaches as close controls.
- **Ablations:** Usability gate, association and calibration separately; real quality groups versus artificial corruption; matched negative coverage.
- **Uncertainty and error analysis:** Acquisition-block intervals; analyse low contrast, sea clutter, overlapping wakes, stationary-looking hulls and incorrectly linked wake axes.
- **Useful findings without outperforming the strongest baseline:** Show that wake cues cannot reliably help on this corpus, or that annotation/negative coverage cannot support absence-based reasoning.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 69.8/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

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
| Compute/storage | 5 | 3 | 3.0 | Medium-low: Scene extraction and multiple detector runs may exceed the initial resource estimate. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **69.8** | **Not qualified.** |

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
| 12. Manageable data reuse | Pass | The bounded public-data route uses a verified CC BY 4.0 release; source attribution and label interpretation remain required. |
| 13. Useful negative findings | Pass | Section 7 defines useful findings if the intervention loses or the stronger claim is not identifiable. |

**Next decision point:** Inspect label JSONs, negatives and hull–wake linkage before promising three empirical investigations; replace or reject member B if links are unavailable.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
