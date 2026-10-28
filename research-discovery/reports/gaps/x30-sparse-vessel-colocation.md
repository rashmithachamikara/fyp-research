[← Research candidates](../research-candidates.md)

# Distinguishing sustained vessel co-location from chance satellite crossings

**ID:** X30 · **Area:** Multimodal ML — vessel encounter evidence · **Status:** Provisional opportunity; not qualified

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

Satellite encounter studies already detect nearby or side-by-side ships. A snapshot can also show ordinary navigation or anchoring, while sparse revisit times hide the duration of any co-location.

## 2. Research gap and question

**Question:** Can a cadence-aware model distinguish sustained co-location from transient proximity better than snapshot distance rules under explicitly sampled observation gaps?

**Tentative hypothesis:** A temporal evidence model using observation intervals improves sustained-proximity classification at a fixed false-positive budget.

**Rival explanation:** Improvements come from AIS-derived duration leakage, or the satellite sampling is too sparse for any model to recover duration.

**What is already addressed / what remains inferred:** Ship-to-ship activity detection is established. MOSA explicitly reports limited revisit and scarce event truth. The narrower proposal studies observability of sustained proximity; it cannot label cargo transfer or illegality without independent event evidence.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [MOSA satellite–AIS maritime observation framework (2026)](https://doi.org/10.3390/rs18030473) | Close vessels may be anchoring/navigation; limited revisit and scarce event truth prevent definitive transfer-performance claims. | Discussion: revisit cadence, paired vessels and event labels. Publisher-indexed discussion inspected. |
| [Detecting ship-to-ship activity from satellite imagery (IGARSS 2024)](https://arxiv.org/abs/2404.07607) | Image-based ship-to-ship activity detection exists; commercial imagery and derived event labels limit easy reproduction. | PlanetScope detection and AIS-derived event labels. Author full-text route and relevant methods inspected. |
| [Satellite mapping reveals extensive industrial activity at sea (2024)](https://doi.org/10.1038/s41586-023-06825-8) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1038/s41586-023-06825-8) | Reported size errors, small-vessel sensitivity and service/pleasure-craft confusion constrain interpretation; spatial splits and class-prior tests already exist. | Methods: length/fishing models, spatial splits; limitations. Full text and dataset documentation inspected. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Train a compact temporal model on existing AIS-derived proximity intervals, then downsample to satellite-like times. Hold out complete encounters/vessel pairs and contrast crossings/anchoring where existing metadata allow. Treat satellite-image pair detection as a separate appearance test.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

A free, licensed corpus pairing repeated satellite images with independent encounter-duration labels has not been secured. Published commercial imagery cases and AIS-derived event labels are not such a corpus. GFW analysis and UEIKAP provide adjacent data, not verified transfer events.

**Original sources:** [GFW Nature analysis data](https://doi.org/10.6084/m9.figshare.24309475); [UEIKAP author dataset](https://doi.org/10.5281/zenodo.18391027).

**Fallback and claim boundary:** Use an existing open AIS track subset for controlled cadence experiments. This supports reconstruction of AIS-defined sustained proximity only; it is an AIS-method study until satellite pairing is independently available.

**Unmeasured resource estimate:** Estimate: CPU temporal models, 16 GB RAM and 5–30 GB for selected tracks/features; optional frozen image features. Commercial satellite purchases are excluded.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: cadence-aware duration | Can a model account for irregular observation intervals? H: Interval-aware inference beats fixed-distance snapshots. | Train a compact temporal duration/proximity model. | Distance threshold and regular-grid sequence model; remove interval input. | Precision/recall for AIS-defined duration under sampled cadence. |
| B: confuser discrimination | Can existing motion context distinguish crossings and anchoring? H: Relative-motion features reduce transient positives. | Train a pairwise motion/context model. | Proximity-only classifier; remove motion/context. | False positives by supported encounter/confuser type. |
| C: evidence uncertainty | When should duration remain undecided? H: Cadence-conditioned uncertainty avoids confident conclusions from one image. | Train/calibrate event-probability intervals. | Global threshold and ordinary calibration; remove cadence conditioning. | Risk–coverage and observability curves. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** PR-AUC and recall at fixed precision for explicitly defined sustained proximity in held-out track pairs; satellite event accuracy only with independent paired truth.
- **Split:** Group complete vessel pairs/encounters and hold out times/regions. Define labels from reference tracks before subsampling; training features may use only sampled observations, not future reference duration.
- **Baselines:** Snapshot separation/heading rules, compact sequence model and irregular-time temporal head; Ballinger/MOSA are close satellite precedents, not assumed publicly reproducible event benchmarks.
- **Ablations:** Cadence input, relative motion and uncertainty separately; one snapshot versus repeated snapshots; ordinary crossings/anchoring controls when labels exist.
- **Uncertainty and error analysis:** Encounter/pair bootstrap; vary sampling pattern and duration threshold; analyse dense anchorage, missed detections and single-observation cases.
- **Useful findings without outperforming the strongest baseline:** Determine revisit intervals at which duration is unidentifiable, or show that stronger satellite claims require unavailable event truth.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 62.4/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

### Weighted rubric

Nine relative weights total 98; scores are normalised to 100. Decimal precision is arithmetic, not confidence.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: Specific failure is testable, but overlap with the cited neighbours remains unresolved; no certified novelty. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: Required independent labels or historical observations have not been secured. |
| Feasibility and learning curve | 14 | 2 | 5.6 | Low: The present satellite claim requires paired data not yet available. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: Losses, trainable fusion/state models or calibration are substantive ML investigations. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: Evaluation for the stronger real-world claim needs independent references; controlled tests support less. |
| Three-member structure | 12 | 4 | 9.6 | Medium: Three related model investigations can each use an unchanged common baseline; data dependencies remain explicit. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: A specific observation/identity error affects maritime research; operational benefits remain untested. |
| Compute/storage | 5 | 4 | 4.0 | Medium: Bounded subsets and occasional GPU use appear manageable; storage/time estimates are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **62.4** | **Not qualified.** |

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
| 8. Objective evaluation | Unknown | Independent outcome/reception/event references are not secured; only a narrower controlled endpoint is currently definable. |
| 9. 6–8 month feasibility | Unknown | Data prerequisites must be resolved before completion in 6–8 months can be supported. |
| 10. Three connected contributions | Pass | Each member has a question, trained intervention, baseline/ablation and attributable result; all can use unchanged common features/models. |
| 11. No specialised/continuous high-end compute | Pass | Core design excludes raw global ingestion, new hardware and continuous high-end or multi-GPU pretraining; estimates appear in section 5. |
| 12. Manageable data reuse | Unknown | Dataset imagery/API terms remain to verify for the exact intended subset. |
| 13. Useful negative findings | Pass | Section 7 defines useful findings if the intervention loses or the stronger claim is not identifiable. |

**Next decision point:** Require an existing licensed AIS subset and defensible proximity labels first. Reject the satellite-transfer claim if independent repeated observations cannot be obtained.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
