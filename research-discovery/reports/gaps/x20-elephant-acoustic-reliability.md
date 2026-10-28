[← Research candidates](../research-candidates.md)

# Detecting elephant calls with reliable false-alarm rates in unfamiliar soundscapes

**ID:** X20 · **Area:** Audio ML / Sri Lankan elephant-call event detection · **Status:** Conditional opportunity; local outcome data not secured

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

A sound classifier can score highly on selected clips yet fail on new recordings. Monitoring requires useful event recall, detection latency and false alarms over long recordings, rather than balanced-clip accuracy alone.

**Potential stakeholders:** Bioacoustic researchers and offline monitoring-tool developers; no field warning network is proposed.

## 2. Research gap and question

**Tentative gap:** Test nuisance-resistant causal detection with recording/day/site holdouts and authentic negative exposure. A detected call is not a measurement of elephant location, movement direction or impending conflict.

**Documented versus inferred:** Living with elephants already demonstrates Sri Lanka–Malaysia transfer loss. Learning to rumble already detects/endpoints calls and discusses contextual noise. The remaining reliability design is inferred; elephant-call classification and cross-country transfer are established.

**Research question:** Can nuisance-resistant and latency-bounded learning retain call recall at a fixed false-alarm rate on held-out Sri Lankan recordings without recorder/background shortcuts?

**Hypothesis and rival explanation:** Recording-aware training and causal context improve event recall at fixed false alarms/hour. Rival explanation: recorder identity, call-enriched sampling or future context inflate results.

This is an AI-assisted research opportunity, not certified novelty. Sri Lankan geography alone is not an original contribution. Seasonal ranging, local passage, habitat suitability, reported conflict and migration are different targets.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Living with elephants, 2025](https://www.sciencedirect.com/science/article/pii/S000632072500309X) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1016%2Fj.biocon.2025.111272) | CNN sound classification drops when transferring between Sri Lankan and Malaysian recordings. | Cross-country transfer already studied; test recording-level separation and authentic negative audio. | Indexed full-text data collection/access sections and publisher abstract; Sections 2.2.1–2.2.2, Abstract and Data availability (X20-L1) |
| [Learning to rumble, 2025](https://www.tandfonline.com/doi/full/10.1080/09524622.2025.2487099) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1080%2F09524622.2025.2487099) | Frame-level detection, classification and endpointing using an audio spectrogram transformer. | A new detector alone is insufficient; compare causal context, nuisance controls and calibrated event false alarms. | Primary indexed full-text sections and author code README; Section 5.2, results/discussion and official AERD repository (X20-L2) |
| [Elephants and algorithms, 2023](https://doi.org/10.1098/rsif.2023.0367) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1098%2Frsif.2023.0367) | Review of AI elephant-monitoring methods. | Technology integration alone is insufficient research or evidence of reduced conflict. | Retrieved review abstract; full text inaccessible; Abstract; HEC-S2 discovery (X20-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1016%2Fj.biocon.2025.111272,10.1080%2F09524622.2025.2487099,10.1098%2Frsif.2023.0367). The supplied 63-page review informed discovery; selected original sources were checked, not all 50 references. [Evidence ledger](../../metadata/evidence-ledger.csv) · [Search, access and review records](../../metadata/elephant-expansion-records.json).

## 4. Proposed approach

Use log-mel/CNN or cached pretrained audio features with an event head. Study nuisance invariance, causal context and source-validation calibration offline. No new sensors or raw-waveform foundation-model training.

## 5. Data and resources

| Item | Current position |
|---|---|
| Sri Lankan corpus lead | [LDC Asian Elephant Vocalizations](https://catalog.ldc.upenn.edu/LDC2010S05): 57.5 hours, 31.25 annotated, Udawalawe 2006–2007. A user agreement and login-dependent fee/access route apply; free university access is unconfirmed. |
| Negative-exposure limitation | LDC describes recordings largely initiated around calls during daytime park observations. This is not a demonstrated unattended nighttime village sample; no-call spans may not support operational false alarms/hour. |
| Other sources / code | [Living with elephants](https://doi.org/10.1016/j.biocon.2025.111272) offers data on request. [AERD author code/weights](https://github.com/CMGeldenhuys/AERD_inference) are public under GPL-3.0. Public weights do not grant audio access or guarantee a clean recording holdout. |
| Bounded core / fallback | With licensed audio, begin with recording-held-out call detection. If authentic negative exposure is absent, report archived-recording performance and drop field alert-rate claims. Foreign audio can test methods but cannot validate Sri Lankan performance. |
| Resources, estimated | CPU feature caching; optional 8–12 GB GPU, 16 GB RAM and 20–60 GB storage depending on licensed format/subset. Actual download size, VRAM and runtime unmeasured. |
| Prototype | Offline waveform/spectrogram with events, latency and confidence; no live wildlife-location publishing or community alerts. |

**Access is a selection dependency.** No institutional partnership, free licensed local outcome corpus or author permission is assumed. No data-access request was sent. Resource figures are estimates; no model training or timing experiment ran. The bounded supplement audit inspected an archive listing and two GeoPackage schemas, not a complete ecological dataset.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: nuisance resistance | Can training avoid recorder/background shortcuts? H: Recording-aware training improves unseen-recording detection. | Train nuisance-resistant compact embeddings/losses. | Feature logistic regression and compact CNN; remove nuisance objective. | Event recall on unfamiliar recordings. |
| B: causal context | How much future audio is required? H: Causal context retains useful recall with bounded look-ahead. | Train causal versus bidirectional temporal heads. | Framewise and AST/AERD-style context; remove future frames. | Recall–latency trade-off at matched feature/model budget. |
| C: calibrated events | Can thresholds transfer without test-recorder tuning? H: Source-group calibration stabilises event reliability. | Fit confidence calibration and event thresholds on source validation only. | Global threshold/temperature scaling; remove grouping. | Calibration and eligible false alarms/hour, or archived-recording error if negative exposure is unsuitable. |

One shared problem, three independently assessable contributions. Each intervention runs against an unchanged common baseline, so another member's method need not succeed first. Shared data/code/models are allowed; papers are optional. The team design is conditional on adequate existing data, not a reason to start new fieldwork.

## 7. Evaluation

- **Primary metric:** Event recall at a predefined false-alarm budget/hour only with representative continuous negatives; otherwise event PR-AUC/Brier with an archived-sample interpretation.
- **Split:** Complete sessions/days and recorder/sites where possible; keep overlapping windows and channels together. Remove spoken field-note channels and audit sample rates.
- **Baselines and code:** Band-energy/feature logistic regression, compact CNN/CRNN and [AERD/AST](https://github.com/CMGeldenhuys/AERD_inference). Released LDC-trained weights may contain held-out sessions; use generic audio initialisation and retraining for clean new splits.
- **Ablations:** Nuisance objective, causal context and calibration separately; match negative sampling, event-merging rule and look-ahead. Synthetic mixtures are not sole evidence of real soundscape transfer.
- **Uncertainty and errors:** Session/day block bootstrap and small-head seeds. Analyse low-SNR/overlapping calls, nuisance sources where labelled and recorder changes. Unannotated spans are not automatically negatives.
- **Useful result without winning:** Show that recording leakage or future context explains a gain, or that the corpus cannot estimate unattended-warning false alarms.
- **Interpretation limit:** Silent elephants remain undetectable acoustically. Calls do not establish migration, elephant-presence sensitivity, distance, imminent conflict or reduced harm.

## 8. Score and next decision

**Provisional conditional score: 67.8/100.** This compares the current proposal design and access risks. It is not qualification or achieved model performance. Novelty is 3/5; dataset suitability and/or feasibility are below required thresholds. Four mandatory gates remain Unknown.

### Weighted rubric

Nine relative weights total 98; the final score is normalised to 100. Unresolved gates prevent qualification regardless of arithmetic.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: event detection/transfer have close work; the new reliability question needs narrowing. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: local audio is licensed/request-only and suitable negative exposure is unverified. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: compact modelling is manageable if data are secured; field-representative evaluation may remain impossible. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: nuisance learning, causal sequence modelling and calibration are substantive ML. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: session splits and event outcomes are suitable; exposure design controls allowable claims. |
| Three-member structure | 12 | 4 | 9.6 | Medium: three independent experiments share common features and baseline recordings. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: acoustics relates to coexistence monitoring, but call detection is indirect evidence of conflict. |
| Compute/storage | 5 | 4 | 4.0 | Medium: caching and compact models plausibly fit occasional modest GPUs. |
| Prototype | 3 | 4 | 2.4 | Medium-high: offline audio visualisation fits the team. |
| **Normalised total / 100** | **98** | | **67.8** | **Not qualified; data access and gap verification required.** |

### Mandatory gates

Pass is supported at bounded design level only. The same provisional-comparison convention used in the existing table applies; unknown gates are not waived and these entries are not admitted as qualified projects.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the Sri Lankan source studies establish a concrete problem; proposed benefits remain untested. |
| 2. ML essential | Pass | Learning or adapting a predictive model is central, not an optional app feature. |
| 3. Train/adapt models | Pass | Sections 4 and 6 define trainable models/objectives; no paid inference service is required. |
| 4. Existing data accessible | Unknown | No free licensed local corpus with adequate labels and representative negative exposure is secured. |
| 5. No unavailable human evaluation | Pass | The bounded design uses existing observations/annotations, without new questionnaires, fieldwork or expert labelling; access is assessed separately. |
| 6. Precise research gap | Unknown | The specific methodological distinction needs checking beyond the cited local studies and broader ecological ML work. |
| 7. Beyond application assembly | Pass | Model-level investigations and ablations go beyond integrating a detector or producing a map. |
| 8. Objective evaluation | Pass | Section 7 specifies an objective conditional evaluation, baseline controls and grouped uncertainty; it is not evidence those outcomes are currently available. |
| 9. 6–8 month feasibility | Unknown | Completion in 6–8 months depends on obtaining adequate existing data early; no partnership or access guarantee exists. |
| 10. Three connected contributions | Pass | Three related contributions can each run against a common unchanged baseline; no separate papers required. |
| 11. No specialised/continuous high-end compute | Pass | The bounded design uses CPU/cached features or an occasional modest GPU; new collars, cameras, microphones and field infrastructure are not required. |
| 12. Manageable responsible use | Unknown | LDC agreement or author permission is required; reuse and location-sharing terms remain unresolved. |
| 13. Useful negative findings | Pass | Section 7 defines useful negative results and limits when a proposed model is not better. |

**Decision:** Manageable ML only after access is resolved; currently not a confirmed no-cost public-data project.

**Next decision point:** Confirm legitimate no-cost access, then inspect session annotations and negative exposure before choosing an alert-rate endpoint. Then discuss the evidence, ecological interpretation and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Data feasibility audit](../../metadata/source-checks/elephant-data-checks.json).
