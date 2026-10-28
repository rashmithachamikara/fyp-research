[← Research candidates](../research-candidates.md)

# Reliable satellite–AIS vessel matching when reports are sparse and matches are ambiguous

**ID:** X21 · **Area:** Multimodal ML / satellite imagery and vessel trajectories · **Status:** Redesign/defer; none of the five proposed gaps is verified novel

**Evidence and scoring reviewed:** 28 October 2026. The initial seven FastTrack searches and three duplication searches were followed by a gap-specific audit: ten further scholarly searches (186 result occurrences), five duplication searches, older references, recent preprints, primary methods and author code. This is a bounded general-research audit, not a systematic review or a certification of novelty. The audit replaces the earlier priority recommendations.

## 1. Problem

A ship visible in a satellite image does not directly reveal its AIS identity. AIS reports and image acquisition times differ; several nearby vessels may be plausible matches. A wrong association contaminates the resulting vessel record, even when the ship detector itself is correct.

**Potential stakeholders:** Researchers building reliable maritime observation datasets and analysts reconciling image detections with vessel records. The bounded target is association reliability. An unmatched detection does not establish deliberate AIS shutdown, spoofing, an illegal act or a collision risk.

**Assessment:** The problem is real, but the five proposed directions do not yet establish an original contribution. Three broad capabilities already have direct prior work; one is established evaluation practice; the narrower final-decision calibration question remains unresolved. An unresolved question is not evidence of a research gap.

## 2. Research gap and question

**Verification verdict: no verified novel gap.** The earlier “highest priority” label for G1 and “high priority” label for G2 are withdrawn. “Already addressed” means the broad proposed capability has a concrete precedent; it does not mean the practical problem is completely solved.

| Original proposed gap | Verification verdict | Decisive evidence | What can legitimately remain |
|---|---|---|---|
| **G1: Confidence after global assignment** | Broad uncertainty-aware association is established; exact final-identity calibration question **unverified**. | Maritime JPDA updates competing identity probabilities (V1); rank-ordered SAR–AIS confidence exists (V2); MOT-CUP propagates conformal uncertainty through assignment (V3). | A narrowly specified failure of final accepted-pair calibration, demonstrated against these baselines. No priority or novelty claim yet. |
| **G2: Missing-candidate rejection** | **Already addressed. Reject as a standalone novelty claim.** | Kroodsma's acceptance rule includes non-broadcasting vessels and false detections (L1); Chen uses post-assignment cost/margin rejection (V6); Reggiannini evaluates no-match and wrong-identity outcomes (V12). | An incremental rejection method only if a new failure and advantage over these controls are demonstrated. |
| **G3: Useful uncertainty during reporting gaps** | **Broad proposal already addressed; narrower downstream benefit unverified.** | Gap-conditioned position rasters (L1), multimode uncertainty models (V7/V8), conformal vessel boundaries (L4) and calibrated gap imputation (V9). | A precise irregular-input or downstream-association failure; not another generic probabilistic trajectory model. |
| **G4: Separating movement and image-position error** | **Broad correction problem already addressed; proposed identifiable decomposition unverified.** | SAR velocity/azimuth compensation (V10), automatic compensation before matching (V2), geometric offset correction (V11) and optical spatial refinement (L3). | A demonstrably identifiable error model with reference data and an advantage beyond existing corrections. Current data do not establish this. |
| **G5: Realistic information/geographic shifts** | **Established evaluation requirement, not standalone novelty.** | Explicit before/after versus one-sided AIS processing (V10); vessel/time/region protocol audit on two AIS corpora (L5). | Evaluation of a specific reproducible association failure, with a substantive method or evidence contribution. |

### G1: What exactly has and has not been verified

The claim “association methods ignore competing identities or uncertainty” is false. Habtemariam et al. use joint probabilistic data association and Bayesian identity updates with other targets, although their setting is radar/AIS simulation rather than satellite imagery. Rodger and Guida rank global SAR–AIS alternatives and assign confidence from attribute agreement; those confidence levels are not demonstrated empirical probability calibration.

MOT-CUP is especially close to the proposed mechanism: calibrated detection uncertainty enters motion prediction and an NLL-based assignment stage, with threshold rejection. Its simulated road-traffic setting differs from maritime identity association. It therefore defeats a generic “calibrate positions and feed them into assignment” novelty claim, while not establishing that the exact proposed MMSI decision-calibration task has been solved.

An inspected public implementation, Darkwatch (V13), also fits probability calibration for SAR–AIS fusion. Its calibrated output concerns contact categories, not verified correctness of individual identity pairs after a scene-wide one-to-one assignment. The inspected association function loops over contacts independently. Its small partly in-sample evaluation is not strong independent scientific validation, but its implementation prevents claiming that merely adding Platt calibration to SAR–AIS fusion is new.

**Residual question, still unverified:** Does calibrating the selected identity decision after constrained assignment improve reliability under candidate competition and changing AIS completeness? Answering it needs full GR-PTA comparison, appropriate structured-association baselines and independent identity labels. Neither an empty search nor the absence of a calibration term in an abstract answers this.

### G2: Why rejection is not a gap by itself

Kroodsma et al. explicitly compare a true AIS match with a non-broadcasting vessel or a false detection when choosing acceptance thresholds. Chen et al. reject costly or ambiguous assignments, including a best-versus-second-best margin test. Reggiannini et al. distinguish no match, wrong identity, missed match and spurious match against expert references. These are direct task precedents, not merely analogies from another application.

**Correction to the original proposal:** A null option, an unmatched output, a margin feature, or a tunable rejection threshold is baseline functionality. A learned rejection head is not automatically a research contribution. A new error-control target could be investigated, but general conformal risk control already exists (V5), so even that requires a specific technical or empirical distinction.

### G3: Which uncertainty claims survive comparison

Kroodsma's empirical position rasters already depend on vessel class, speed and elapsed time. Capobianco models predictive uncertainty; Jia models multiple motion modes and changing process noise. These papers establish strong prior mechanisms, but their resampled trajectory evaluations do not by themselves prove robustness to irregular raw inputs or calibrated identity decisions.

Jurkus provides conformal vessel regions. The AISFlow workshop submission explicitly reports split-conformal marginal bands for long missing intervals, using both pre-gap and post-gap states. Its Sections 5.5 and 7 were read through indexed original-PDF passages; direct PDF retrieval was blocked. Workshop acceptance and named authors were not verified, so this is submission-level evidence. Marginal coordinate bands are not joint two-dimensional, whole-trajectory or final-match guarantees.

**Residual boundary:** A past-only short-horizon association experiment differs from retrospective long-gap imputation, but changing that setting alone does not establish novelty. The original generic “multiple plausible locations plus calibrated regions” contribution is already covered.

### G4: Why separating error sources needs more than a new loss term

Graziano et al. explicitly connect matching errors to both AIS interpolation uncertainty and SAR motion-induced azimuth offsets. Rodger and Guida compensate the offset before association; Song et al. correct image positioning using AIS references. These defeat the broad implication that image error is routinely treated only as trajectory uncertainty.

GR-PTA is an **optical** remote-sensing method using short-horizon observations from two strips, not a single SAR snapshot. Its spatial refinement is relevant adjacent work, but SAR Doppler displacement models must not be transferred to those optical images.

**Residual boundary:** Estimating separate trajectory, timing and image-error distributions from their combined residual is generally not justified without identifying information, reference observations or defensible assumptions. Existing corrections are not proof that every uncertainty decomposition is solved; equally, proposing a decomposition without those data is not a feasible verified gap. Keep correction as a control; defer a decomposition contribution.

### G5: Why realistic evaluation is necessary but not new

The inspected 2026 AIS protocol preprint explicitly isolates vessel, chronological and geographic split effects and studies oracle-decoding bias. Graziano already distinguishes interpolation from one-sided extrapolation. Thus “use past-only data and geographic holdouts” is not a new method.

Retrospective matching may legitimately use later AIS reports if they are available when the association is made. That is not leakage merely because the reports follow image acquisition. A real-time or acquisition-time forecasting claim requires a corresponding information cutoff; receipt timestamps are needed to establish actual operational availability. Compare equivalent information access and separate the two tasks.

**Residual boundary:** A specific downstream association audit could yield useful evidence. Its novelty would lie in a demonstrated previously unresolved failure and experimental result, not simply adopting standard splits. No such result has been demonstrated here.

**Question retained only for further validation:** Can a compact learned satellite–AIS model improve calibration of selected identity pairs under candidate competition and missing candidates beyond probabilistic association, global attribute matching and simple post-hoc calibration?

**Hypothesis and rival explanations:** Improvements could come from modelling assignment context, or merely from rejecting more cases, looser candidate filtering, future AIS, generated labels or data leakage. This is an experimental hypothesis, not a verified contribution. None of G1–G5 is currently ready to be presented to the supervisor as an established novel gap.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Kroodsma et al., 2022: probabilistic SAR–AIS matching](https://doi.org/10.1038/s41598-022-23688-7) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1038/s41598-022-23688-7) | Empirical position probability rasters, before/after AIS, pair scores, greedy matching and analyst-reviewed acceptance thresholds; ambiguous matches are explicitly discussed. | Compare against this probabilistic baseline. Test final decision calibration and selective matching, rather than claiming the first probabilistic approach. | Full-text matching-method paragraphs via Europe PMC XML and author README (AIS-L1). |
| [Li et al., 2025: optical/SAR multi-feature association](https://doi.org/10.3390/rs17132201) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/rs17132201) | Oriented detections, position/size/course costs and improved JVC global assignment. Authors identify limited geographic coverage. | Learned decision reliability under ambiguity and missing candidates; same detector outputs and equivalent information access. | Indexed publisher methods and conclusions; direct page rate-limited. Complete formula-by-formula replication not checked (AIS-L2). |
| [Du et al., 2026: GR-PTA](https://doi.org/10.1016/j.isprsjprs.2026.07.005) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1016/j.isprsjprs.2026.07.005) | Point-to-trajectory similarity, short-horizon motion, one-to-one graph assignment, structural filtering and spatial refinement across five regions. | Must demonstrate an additional calibration/rejection experiment beyond this framework. Its abstract cannot establish that those features are absent. | Publisher abstract, indexed section snippets and author repository; complete methods still unavailable. The sensor is optical with two-strip observations, not SAR (AIS-L3). |
| [Jurkus et al., 2025: vessel prediction boundaries](https://doi.org/10.3390/s25051365) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/s25051365) | LSTM trajectory predictions with several uncertainty boundaries, including conformal regions, evaluated for collision scenarios. | Final image-to-identity assignment is a different target; ordinary conformal position regions alone are already covered. | Indexed publisher methods, experiment and data-availability sections (AIS-L4). |
| [Raisi and Nazarzehi Had, 2026 preprint: leakage-aware AIS evaluation](https://arxiv.org/abs/2609.25827) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550/arXiv.2609.25827) | Vessel/time/region splits and decoder effects in AIS forecasting; reports code and split release. | Apply controls to association and confidence, rather than claiming the first leakage-safe trajectory benchmark. | Full HTML methods Sections 4.3–4.4 and results/protocol Sections 5–6 inspected during the audit; preprint results not independently reproduced (AIS-L5). |


### Additional nearest methods checked during the verification audit

IDs below are prefixed **AIS-** in the evidence ledger. “Direct” means satellite–AIS association; adjacent work constrains a general novelty claim without proving the exact maritime task is solved.

| Evidence | Task, data and method already covered | Relevance and reading limit |
|---|---|---|
| **V1:** [Habtemariam et al., 2015](https://doi.org/10.1016/j.sigpro.2014.07.029) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1016/j.sigpro.2014.07.029) | AIS/radar fusion on simulated tracking data; joint probabilistic association updates uncertain identities using measurements and other targets. | Adjacent to G1/G2, not satellite SAR. Publisher abstract and bibliographic record checked; full methods unavailable. |
| **V2:** [Rodger and Guida, 2021 issue; online 30 December 2020](https://doi.org/10.3390/rs13010104) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/rs13010104) | English Channel and Solent SAR/AIS cases; interpolation and azimuth compensation; m-best global alternatives with attribute-based confidence. | Direct G1/G4 precedent. Indexed primary Sections 2.2, 2.4 and 4 read. Rule-based confidence is not demonstrated probability calibration; direct PDF blocked. |
| **V3:** [MOT-CUP, 2024](https://doi.org/10.1109/LRA.2024.3364450) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109/LRA.2024.3364450) | V2X-Sim road-traffic simulation; conformal coordinate uncertainty enters Kalman prediction, NLL/Hungarian association and rejection. | Adjacent G1/G2 precedent. Author full-text Sections III-D/E, Algorithms 1–2 and IV inspected. Evaluates tracking/localisation uncertainty; not a demonstrated guarantee for selected maritime identity probabilities. |
| **V4:** [Towards PAC Multi-Object Detection and Tracking, 2022 preprint](https://arxiv.org/abs/2204.07482) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550/arXiv.2204.07482) | COCO and MOT17; calibrated prediction sets for detections and tracking edges, composed into system-level coverage results. | Adjacent G1 precedent. Full HTML Sections 4–6 inspected. Edge-set coverage differs from precision of one selected global identity assignment. |
| **V5:** [Conformal Risk Control, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550/arXiv.2208.02814) | General prediction tasks; expected bounded monotone-loss control, with worked vision/language examples. | Adjacent G1/G2 methodology. Original proceedings abstract and paper introduction/theorem framing read. Does not automatically control selective identity error after reassignment. |
| **V6:** [Chen et al., 2026](https://doi.org/10.3390/rs18132223) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/rs18132223) | SAR classification-label construction using multi-feature global association followed by cost and ambiguity-margin rejection; controlled distractor tests. | Direct G2 and G1-baseline precedent. Indexed primary association Equations 8–10, adjacent margin rule and discussion read. High-confidence label filtering is not equivalent to calibrated identity probability. |
| **V7:** [Capobianco et al., 2022 preprint / 2023 journal](https://doi.org/10.1109/TAES.2022.3216823) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109/TAES.2022.3216823) | Danish tanker trajectories; Bayesian recurrent prediction with aleatoric/epistemic uncertainty and optional intention information. | G3 precedent. Complete relevant preprint pages extracted; Sections II–IV inspected. Evaluation uses regular resampling, not proof of irregular-input or satellite-association performance. |
| **V8:** [Jia et al., online 2024 / issue 2025](https://doi.org/10.1109/TAES.2024.3491053) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109/TAES.2024.3491053) | Yangtze AIS plus simulated motion; multiple Kalman–GRU modes and learned changing process noise, tested across input lengths/horizons. | G3 precedent. Author PDF methods/experiments extracted and read, including preprocessing on page 7 and uncertainty discussion on page 9. Resampling and model confidence do not establish final-match calibration. |
| **V9:** [AISFlow, 2026 workshop submission](https://openreview.net/pdf?id=FhNvZOMekI) | Danish AIS long-gap imputation using pre/post-gap context; ensemble generation and split-conformal marginal uncertainty bands. | G3 precedent with a different information regime. Indexed original-PDF Sections 5.5/7 and first page read; direct PDF blocked. Acceptance and named authors not verified; no claim of joint trajectory coverage. |
| **V10:** [Graziano et al., 2019](https://doi.org/10.3390/rs11192196) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/rs11192196) | TerraSAR-X/AIS case in the Gulf of Naples; image-derived velocity improves compensation for movement-related positional displacement. | Direct G4/G5 precedent. Indexed primary Sections 2–3 and abstract read; direct PDF blocked. A correction method does not establish identifiable separation of every error component. |
| **V11:** [Song et al., 2023](https://doi.org/10.1109/LGRS.2023.3253775) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109/LGRS.2023.3253775) | Uses AIS and detected ship locations to estimate and mitigate SAR geometric offsets. | Direct G4 precedent. Author-institution abstract and registered record checked; full method unavailable. Do not infer a complete uncertainty decomposition. |
| **V12:** [Reggiannini et al., 2024](https://doi.org/10.3390/rs16030557) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/rs16030557) | Satellite/AIS fusion returns identity or no match and confidence; experts evaluate 299 targets from five images, separating wrong identities from false/missed matches. | Direct G1/G2 precedent. Indexed primary Section 7 read. Threshold selection from confidence scores is not an independent guarantee of calibrated probabilities. |
| **V13:** [Darkwatch author code](https://github.com/satyamdas03/darkwatch) | Per-contact SAR/AIS scoring with a no-match alternative and learned per-class Platt calibration; README discusses geographic transfer problems. | Implementation evidence only. `associate.py` lines 362–376/549–606, `calibration.py` and fitting script inspected at recorded Git SHAs. Calibrated categories differ from exact identity confidence; no replication or peer-review claim. |

**Distinctions that prevent another false gap claim:** Geometric calibration is not probability calibration. A model-derived posterior is not automatically empirically calibrated. Coordinate/edge-set coverage is not accepted-match precision. Generic conformal risk control assumes a suitable loss and sampling conditions; selected-match error and reassignment need not be monotone as a threshold changes. A method's application to SAR–AIS must establish that distinction, not simply rename a known technique.

[Import all 16 literature records with DOIs](https://literature.researchfasttrack.com/zotero?ids=10.1038/s41598-022-23688-7,10.3390/rs17132201,10.1016/j.isprsjprs.2026.07.005,10.3390/s25051365,10.48550/arXiv.2609.25827,10.1016/j.sigpro.2014.07.029,10.3390/rs13010104,10.1109/LRA.2024.3364450,10.48550/arXiv.2204.07482,10.48550/arXiv.2208.02814,10.3390/rs18132223,10.1109/TAES.2022.3216823,10.1109/TAES.2024.3491053,10.3390/rs11192196,10.1109/LGRS.2023.3253775,10.3390/rs16030557). AISFlow and the code repository are linked separately.

**Audit limits:** GR-PTA's complete methods remain inaccessible. Publisher-indexed passages are marked as such; they are not claimed as complete article reads. The bibliographic checks confirm registered records, not scientific validity. Ten scholarly searches returned many irrelevant records; all raw results are retained, and lack of an exact hit is not used as evidence of novelty. No methods were reproduced and no new model results were generated. [Detailed validation records](../../metadata/source-checks/satellite-ais-gap-validation.json).

Additional context: [Paolo et al., Nature 2024](https://doi.org/10.1038/s41586-023-06825-8) extends probability-raster matching at large scale; its matching-method paragraphs and author data documentation were inspected (AIS-L6). Its fishing-classification score calibration is a different target from identity-match calibration. This active literature supports relevance, not guaranteed novelty or citations. [Evidence ledger](../../metadata/evidence-ledger.csv) · [Search/access records](../../metadata/satellite-ais-records.json).

## 4. Proposed approach

**Design retained for comparison, not approved as novel:** Freeze the satellite detector or use existing target centres first. Train a compact trajectory distribution model and a learned match-confidence model; compare them with kinematic/probabilistic baselines. Feed position, time-gap and available shape/course information into the association cost. Use one-to-one assignment with explicit unmatched options, then test calibration of accepted identity decisions.

**Important distinction:** A spatial density, whose value depends on units and region size, is not automatically a probability that an identity is correct. A usable match-confidence model must consider alternatives, the null match and selection by assignment. Rejecting a pair may change other assignments, so evaluate the complete procedure after rejection/reassignment.

Maintain two labelled protocols: **past-only association** using reports timestamped no later than acquisition, and **retrospective association** allowing before/after reports. If receipt timestamps are unavailable, the former establishes timestamp-causal processing only; it does not demonstrate real-time AIS availability. Never give one method future AIS while withholding it from another.

Use fixed, documented detection and candidate pools for the main comparisons. Keep natural missingness separate from artificial message thinning, candidate removal and injected sensor errors. Simulated perturbations test controlled robustness, not operational rates.

## 5. Data and resources

| Source / resource | Verified position and limitation |
|---|---|
| **GR-PTA author subset (optical)** | [Author repository](https://github.com/Du-Jinjin/GR-PTA) describes imagery, raw/conditioned AIS and manually checked `matched`/`rs_only` labels, with a [Drive download route](https://drive.google.com/drive/folders/1PtvOHHNyPEx9gEGv2YwbRM1mm40643lH). Actual imagery and identity-label files were not retrieved. Sufficient independent examples, label provenance and reuse terms remain unverified. |
| **Bounded GR-PTA check** | The inspected `GR-PTA/metadata.csv` is actually a 10,596-byte Excel workbook. It contains eight ROI entries across five region IDs; some ROIs share an AIS file and acquisition times seconds apart. Its `ais_file` schema differs from the README's raw/QC file columns. Eight rows are not eight independent acquisition events. Root-level label/metadata paths and the inspected licence paths returned 404; this does not prove files or permissions are absent elsewhere. |
| **GFW Nature training data** | [Original Figshare training release](https://doi.org/10.6084/m9.figshare.24309469) exposes a CC BY 4.0 manifest and a 142,908,413-byte detection-tile archive. README describes 11,965 dual-channel 80×80 tiles with presence/length targets; these do not establish identity-matching truth. |
| **GFW processed association outputs** | [Original analysis release](https://doi.org/10.6084/m9.figshare.24309475) documents scene/time, detection coordinates, MMSI and a generated matching score. These outputs are another algorithm's associations, not independent identity labels. A downloaded 72,959-byte `vessels_test.csv.zip` contained 3,172 presence/length rows without identity histories. The archive was parsed; no imagery was decoded. |
| **xView3** | [Dataset paper](https://papers.nips.cc/paper/2022/file/f4d4a021f9051a6c18183b059117e8b5-Paper-Datasets_and_Benchmarks.pdf) documents detection/classification labels and probabilistic AIS-derived annotations. Suitable for detector work, but not verified here as a complete identity-association benchmark with history and independent truth. Avoid the full-scene download for an initial pilot. |
| **AIS-only fallback** | [Danish authority](https://www.dma.dk/safety-at-sea/navigational-information/ais-data) confirms freely downloadable historical CSV archives. Useful for trajectory pretraining or withheld-position tests; reuse terms, dates and matching image coverage still need checking. AIS-only results cannot validate satellite identity matching. |
| **Compute, estimated** | Fixed detections, CPU kinematic/assignment baselines and small trajectory/confidence models; target 16–32 GB RAM, 20–100 GB bounded working storage and occasional 8–12 GB GPU access. These are planning estimates, not measured requirements. Large global raster reproduction is outside scope. |
| **Prototype** | Offline map showing image targets, candidate trajectories, uncertainty regions and accepted/rejected matches, with known errors available for replay. Backend and frontend are shared engineering support. |

**Selection blocker:** Obtain enough existing paired scenes, usable AIS history and independently supported identity labels for training, calibration and locked testing, with explicit reuse rights. A public README or generated MMSI column is insufficient. Do not create new expert labels to bypass the team's constraints. If the author subset is too small, it may support a smoke test only; an AIS-only fallback changes the central claim and must be reassessed.

[Bounded source audit](../../metadata/source-checks/satellite-ais-data-checks.json) records file manifests, parsed CSV schemas, metadata rows and article passages. No baseline was trained; storage, runtime and statistical power are not demonstrated.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Independently assessable result |
|---|---|---|---|---|
| A: position distributions | Can a compact model represent gap-dependent manoeuvre uncertainty usefully? H: A learned local-offset mixture improves sharpness at comparable coverage and improves matching with a fixed association rule. | Train a small GRU/mixture-density or comparable distribution model; condition on elapsed time. | Constant velocity/Kalman and empirical raster; remove gap conditioning or replace mixture with one mode. | Held-out coverage/area and identity outcomes using the unchanged common matcher. |
| B: decision calibration | Does confidence remain reliable after candidate competition? H: A calibration model using assignment margin, competing scores and gap information reduces accepted-match miscalibration. | Fit a held-out match calibrator or structured confidence model; compare position-only and assignment-aware information. | Global scalar/isotonic calibration on fixed baseline outputs; remove competition features and vary calibration grouping. | Brier/log loss and reliability after assignment, without requiring A's model to improve. |
| C: selective association | Can learned rejection handle absent true candidates without discarding most valid matches? H: A null-match/abstention model improves correct-match retention at a fixed error tolerance. | Train a null-match scorer or selective objective, with assignment-aware acceptance/reassignment. | Distance cutoff, score threshold and margin threshold on the common baseline; remove null option or missing-candidate training. | Locked-test precision–retention and unmatched-case errors using fixed baseline forecasts/calibration. |

The following structure remains a conditional experimental work division, not three verified new contributions. One shared problem, three independently assessable research investigations. Each runs independently against the same baseline inputs; combining all methods is a later ablation. Calibration is assessable research rather than a subordinate implementation task. Papers are optional. If suitable labels cannot support B and C, the proposed team structure is not empirically feasible yet.

## 7. Evaluation

- **Primary metric:** Correct-identity recall among all labelled matchable detections at a validation-selected false-association tolerance, accompanied by actual test precision, retained fraction and confidence intervals. Choose a defensible tolerance from available independent sample size; do not claim a 99% guarantee from a tiny subset. Report the full risk–retention curve so rejecting every match cannot appear successful.
- **Other outcomes:** Wrong-identity rate, false association of verified `rs_only` targets, false-unmatched rate, candidate-generation recall and assignment F1. Report detector recall separately from association conditional on supplied targets; selected ROI labels may not support exhaustive whole-scene recall.
- **Split:** Separate training, calibration/threshold selection and locked testing by acquisition event and vessel where feasible; retain a later-time and unseen-region test. ROIs seconds apart, overlapping crops and shared AIS histories stay together. If five regions/eight inspected ROIs cannot supply enough independent calibration/test events, restrict the claim or reject the dataset; random pair-level splitting is not a solution.
- **Baselines:** Nearest position; constant-velocity/Kalman plus global assignment; probabilistic raster matching; multi-feature JVC; and GR-PTA as the strongest directly relevant methodological comparator. Also include rank-ordered attribute confidence, a null/margin rejection baseline, simple post-hoc calibration and an explicitly adapted MOT-CUP-style uncertainty/assignment comparator. GR-PTA reproduction/code availability and the full method remain unresolved; a simplified reconstruction must be labelled as such, not reported as the authors' result. A compact learned trajectory model is the trainable baseline.
- **Ablations:** Deterministic versus probabilistic position; uncalibrated versus position-calibrated versus decision-calibrated; pairwise versus one-to-one matching; null/rejection off versus on; gap/competition features; past-only versus retrospective AIS. Fix detector and candidate generator, compare at equal retention, and report coverage with region area so inflated uncertainty cannot hide failure.
- **Uncertainty:** Vessel-/acquisition-block bootstrap and paired comparisons; repeated learned-model seeds if feasible. Report position-region coverage at several levels and area, final match Brier/log loss, reliability curves, and selective error with counts. Temporal dependence and domain shift mean ordinary conformal assumptions cannot be treated as automatic guarantees.
- **Error analysis:** AIS gap, manoeuvres, vessel separation, candidate count, true-candidate absence, ship size, image location error and region. Separate genuinely absent candidates from ambiguous annotation. Error-component identifiability needs reference information; residuals alone cannot tell motion error from SAR displacement.
- **Useful findings without winning:** Show that calibrated position regions worsen identity precision in crowds, that a simple threshold matches learned rejection, that gains vanish with event-disjoint splits, or identify the reporting-gap range beyond which association should abstain.
- **Interpretation limit:** Benchmark association reliability does not demonstrate reduced accidents, ecological harm or illegal activity. Do not train and evaluate against GFW-generated identities and then claim independent correctness. Any AIS-assisted spatial correction must use only permitted inputs, not held-out identity labels.

## 8. Score and next decision

**Provisional score after verification: 64.5/100** (previously 67.8). Novelty is reduced from 3/5 to 2/5 because the audit found substantial prior mechanisms and no verified distinct contribution. Other ratings retain their design-level interpretation. Five mandatory gates remain Unknown, including gate 7, which is changed from Pass to Unknown. Not qualified; redesign/defer.

### Weighted rubric

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | Medium: direct and adjacent prior work covers the broad claims; the exact remaining calibration question is unverified. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: author data leads exist; sufficient independent identity labels and reuse rights remain unverified. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: fixed detections bound the workload, but paired data and SAR interpretation threaten completion. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: learned distributions, decision calibration and selective matching are substantive empirical ML. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: event-disjoint controls and selective metrics are appropriate; adequate independent sample size is unresolved. |
| Three-member structure | 12 | 4 | 9.6 | Medium: three research interventions can each use unchanged common baseline inputs. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: reliable identity reconciliation matters for maritime datasets; operational benefit is untested. |
| Compute/storage | 5 | 4 | 4.0 | Medium: compact models and fixed detections plausibly fit modest resources; no timings measured. |
| Prototype | 3 | 4 | 2.4 | Medium-high: historical map replay fits team engineering skills. |
| **Normalised total / 100** | **98** | | **64.5** | **Redesign/defer; no verified novel gap.** |

### Mandatory gates

Pass refers to the bounded design. Provisional scoring follows the existing comparison convention; unknown gates are not waived.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Original matching studies document asynchronous reports, ambiguous correspondences and rejection difficulties. |
| 2. ML essential | Pass | Learned position distributions, confidence and selective models are central to the question. |
| 3. Train/adapt models | Pass | Sections 4 and 6 define trainable models and empirical adaptations. |
| 4. Existing data accessible | Unknown | Enough paired histories and independent identity labels for distinct train/calibration/test events are not verified. |
| 5. No unavailable human evaluation | Pass | Design relies on existing author-validated labels; no new expert annotation, recruitment or fieldwork is assumed. |
| 6. Precise research gap | Unknown | The five broad claims do not establish novelty; a narrower final-identity calibration distinction still needs decisive comparison. |
| 7. Beyond application assembly | Unknown | The proposed components have close precedents; an advance beyond implementing and combining them has not been established. |
| 8. Objective evaluation | Pass | Section 7 defines identity, rejection and uncertainty outcomes with leakage-safe controls, conditional on suitable data. |
| 9. 6–8 month feasibility | Unknown | Adequate existing paired data and a reproducible strong baseline must be established first. |
| 10. Three connected contributions | Pass | Position modelling, decision calibration and selective association share one question and baseline. |
| 11. No specialised/continuous high-end compute | Pass | Fixed detections and compact models avoid satellite hardware or continuous large-GPU training. |
| 12. Manageable responsible use | Unknown | Author-subset licence and image/AIS reuse terms are not established; public visibility is insufficient permission. |
| 13. Useful negative findings | Pass | Calibration failures, threshold equivalence and split sensitivity yield useful bounded findings. |

**Next decision:** Take the corrected audit to the supervisor as a redesign decision, explicitly stating that no novel gap is verified. If G1 is retained for further investigation, the remaining decisive work is a full-method comparison and an independent labelled-data check before a bounded pilot. Do not commit to the previous five-gap framing or claim originality for the baseline capabilities.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric)
