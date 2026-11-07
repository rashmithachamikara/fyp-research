[← Research candidates](../research-candidates.md)

# Small/thin road-damage detection and missed-damage prediction on unseen countries

**ID:** X03 · **Area:** Computer vision / object detection · **Status:** Conditional candidate; baseline pilot, novelty comparison and compute validation required

**Document reconciled:** 7 November 2026, against proposal v8 and subsequent project discussion. **Historical scoring date:** 28 October 2026. This update is a reconciliation, not a new exhaustive literature search or a completed experiment. Reading limits are recorded below; the update date does not imply every source was reopened that day.

**Planning source:** [v8 proposal text extraction](../../../tmp/proposal/Road-Damage-Research-Proposal-v8.txt). Later discussion qualifies its motivation and resource assumptions; those qualifications are distinguished from original v8 specifications.

**In simple terms:** A changes how thin boxes receive training supervision. B encourages compatible predictions at different image scales. C trains a separate neural model to warn where damage may have been missed. A and B aim to improve detection; C evaluates failure prediction.

[Academic summary PDF](../../../output/pdf/road-damage-research-summary.pdf) · [Canvas visual note](../../../output/canvas-design/road-damage-canvas-note.pdf). These explain v8 but do not replace this report's later pilot and feasibility qualifications. The [earlier interactive visual](../road-damage-visual-note.html) is a legacy explanation that may retain the superseded annotation-tolerance/calibration scope.

## 1. Problem and evidence boundary

Road-damage detectors can lose performance between countries. Country groups changes in roads, cameras, viewpoint, lighting, class prevalence and potentially annotation practice; the detector does not recognise borders. Different countries may look similar, while conditions within a country can also shift substantially.

Every test image should be unseen. Randomly splitting all countries still exposes the model to those countries' conditions during training. A country holdout withholds one collection of conditions. The broad ambition is better generalisation; this experiment tests **source-only domain generalisation under country holdout**. Domain adaptation uses target-domain data and is a different access setting.

- **Documented:** cross-country road-damage degradation exists, and MAMDG already investigates source-only road-damage generalisation.
- **Not demonstrated locally:** ordinary COCO-initialised YOLO11 necessarily leaves a large or meaningful problem. A modern pooled-source baseline may already perform adequately.
- **Not demonstrated:** thin cracks cause the overall transfer loss or always fail first. Geometry, appearance, cameras and class distributions are rival explanations.
- **Not demonstrated:** shape statistics establish inconsistent annotation. Viewpoint and genuine damage differences can produce similar statistics. Synthetic perturbations test simulated variation only.
- **Proposed:** A/B/C are evidence-informed hypotheses, not proven necessities or guaranteed improvements. They do not address every possible source of shift.

**Stakeholders:** pavement-inspection researchers, road-image model developers and agencies considering imported detectors. No Sri Lankan performance is evaluated; benchmark results do not establish savings, safety improvement or deployment readiness.

## 2. Questions and novelty boundary

**Working question:** Without target-country training or tuning data, do short-side-relative assignment and small-object-anchored consistency improve detection, and do detector features add information for predicting missed small/thin damage beyond weak detections alone?

| Member | Principal comparison | Hypothesis / primary outcome |
|---|---|---|
| A | Short-side-relative Gaussian similarity versus equally tuned plain NWD, identical candidate eligibility, original labels | Higher country-macro held-out mAP50:95; geometry outcomes and assignment/weight logs explain the mechanism. |
| B | Small/thin consistency versus generic consistency with identical views, supervision and budget | Higher small-or-thin recall at source-selected thresholds, with false positives/image no more than 10% above generic consistency. |
| C | Features plus weak map versus a matched learned weak-map-only head | Higher country-macro cell-level AUPRC for missed small/thin centres, with positive-cell prevalence stated. |

**Rival explanations:** extra training exposure, augmentation, country balance, resolution, changed supervision mass, number of consistency objects, threshold changes, duplicate frames, or C merely reproducing weak detections.

**Novelty: partly covered and provisional for all three.** NWD, consistency, neural error monitoring and the setting have prior work. Stock DFL and task-aligned assignment are baseline components. A's exact normalisation has the most speculative justification; B has direct domain-generalisation neighbours; C has established failure-prediction precedents. No complete duplication clearance or “first ever” claim is established.

The methods fit **small/thin-damage robustness and miss prediction under country shift** better than a broad claim to solve country transfer. If the pilot identifies lighting, texture or class balance as the important weakness, revise the relevant questions before confirmatory evaluation.

## 3. Literature and reading limits

The [original evidence ledger](../../metadata/evidence-ledger.csv) retains discovery searches and X03-L1–L3. Added sources below were discussed during the v8 review; this does not imply all were entered into that older ledger or read in full. This is not a bibliography certification or an unrecorded comprehensive search.

| Work | Relevant evidence | Reading boundary / consequence |
|---|---|---|
| Arya et al. (2020), [Transfer Learning-based Road Damage Detection for Multiple Countries](https://arxiv.org/abs/2008.13101) | SSD MobileNet, 300 × 300, 16 models/30 scenarios; Japan-only, local and mixed-country training. Ja_10k D00 F1 is 0.308 on Japan versus 0.051 on India, Table 3. | Relevant methodology, Table 3 and discussion read in supplied paper. SSD evidence, not YOLO11 evidence; remedies often include labelled target data. Predates RDD2022. |
| Arya et al. (2024), [RDD2022: A multi-national image dataset for automatic road damage detection](https://doi.org/10.1002/gdj3.260), Geoscience Data Journal | Public six-country data and four classes. | Publisher dataset/annotation sections and proposal counts consulted; local decoding/count/duplicate audit pending. Cite journal version. |
| Chen et al. (2026), [Multi-Adversarial Metric-Constrained Domain Generalization for road damage detection](https://doi.org/10.1016/j.imavis.2026.106173), Image and Vision Computing (MAMDG) | Source-only generalisation; domain discriminators encourage shared features and FAB triplets preserve class separation. Introduction identifies CSPDarknet53. | Abstract, introduction, snippets and supplied publisher preview read; full numerical tables/protocol not inspected. Same setting, different interventions. Listed Cityscapes/Sim10k are not road-damage datasets. Recheck code availability; v8's October empty-repository observation is historical. |
| [MSDA-RDD: Multi-Source Domain Adaptation for Cross-Scene Road Damage Detection](https://ieeexplore.ieee.org/abstract/document/11655917) (2026), IEEE TCSVT; [DOI](https://doi.org/10.1109/TCSVT.2026.3723926) | Indexed IEEE abstract describes YOLO11 adaptation, spatial/frequency feature decoupling, pixel/class alignment and teacher pseudo-labels; US/Japan/China experiments. | Publisher-indexed abstract retrieved after original note; direct access inconsistent. Full target-data protocol and numerical baseline comparisons still require inspection. No exact ordinary-YOLO11 transfer drop inferred. |
| Xiao et al., [Self-Supervised Visual Prompting for Cross-Domain Road Damage Detection](https://arxiv.org/abs/2511.12410), WACV 2026 (PROBE; preprint 2025) | Prompts use unlabelled target data and source–target alignment. | Author abstract/acceptance checked. Target access distinguishes it from source-only evaluation. |
| Wang et al. (2021, revised 2022), [A Normalized Gaussian Wasserstein Distance for Tiny Object Detection](https://arxiv.org/abs/2110.13389) | Gaussian box similarity addresses tiny-object overlap sensitivity on AI-TOD; A's comparator. | Author abstract checked. Does not establish short-side normalisation benefits YOLO11 or country transfer. |
| Li et al. (2024), [CrackTinyNet: A novel deep learning model specifically designed for superior performance in tiny road surface crack detection](https://doi.org/10.1049/itr2.12497), IET ITS | YOLOv7 tiny-crack model combines NWD, attention and modified downsampling. | Publisher method/discussion excerpts checked; not proof that thinness causes country loss. |
| Danish et al. (2024), [Improving Single Domain-Generalized Object Detection: A Focus on Diversification and Alignment](https://arxiv.org/abs/2405.14497), CVPR | Source diversification and cross-view classification/localisation alignment under shift. | Author/CVF abstracts and accessible paper text consulted. Strong B neighbour; geometry selection and controls carry the distinction. |
| Rahman, Sünderhauf and Dayoub (2019), [Did You Miss the Sign? A False Negative Alarm System for Traffic Sign Detectors](https://doi.org/10.1109/IROS40897.2019.8968525), IROS; [author version](https://arxiv.org/abs/1903.06391) | Separate false-negative predictor uses internal traffic-sign-detector features. | Author abstract checked. C does not invent feature-based prediction of missed objects. |
| Yatbaz et al. (2024), [Run-time Introspection of 2D Object Detection in Automated Driving Systems Using Learning Representations](https://doi.org/10.1109/TIV.2024.3385531), IEEE T-IV; [author version](https://arxiv.org/abs/2403.01172) | Activation-based frame-level monitoring on KITTI/BDD, including dataset-shift adaptability. | Author abstract/institutional record checked. Dense missed-centre prediction is different; transfer success is not inherited. |
| Zimmermann, Holzbach and Lerch (2026), [Knowledge-Guided Failure Prediction: Detecting When Object Detectors Miss Safety-Critical Objects](https://arxiv.org/abs/2603.25499), CVPR Workshops | Detector/foundation-model representations flag likely misses under shift (KGFP). | Author/CVF abstracts checked. Different architecture and image-level task. |
| Chen et al. (2026), [DSE-YOLO11: Dynamic feature adaptation for key traffic element detection in complex road scenes](https://doi.org/10.1371/journal.pone.0350328), PLOS ONE | Section 4.4.4 reports poor zero-shot RAD→BDD100K transfer for YOLO11n and DSE-YOLO11. | Publisher external-validation/discussion read. Overlapping traffic categories, not four-country RDD2022 cracks; no guaranteed gap for this baseline. |
| Hou et al. (2024), [Bridging Data Distribution Gaps](https://doi.org/10.3390/app142411974), Applied Sciences | Test-time pavement adaptation. | Original discovery abstract only (X03-L3). Full methods not inspected; separate target-access accounting required. |

**Unresolved leads:** SimD/RFLA, other assignment methods, Guo et al.'s scale-consistency adaptation, federated road models and calibration methods need full-method comparison if retained. Do not present incomplete references as verified findings. V8's VALA/DIFEDA leads remain unverified here.

## 4. Dataset, baseline and protocol

### Data

Use the [RDD2022 author release](https://github.com/sekilab/RoadDamageDetector), VOC XML converted reproducibly to YOLO, and D00 longitudinal / D10 transverse / D20 alligator crack / D40 pothole labels. Published licence: CC BY-SA 4.0; retain attribution and check share-alike requirements for released derived data.

| Country | Labelled training images reported in v8 |
|---|---:|
| Japan | 10,506 |
| India | 7,706 |
| United States | 4,805 |
| Czech Republic | 2,829 |
| **Total** | **25,846** |

These are proposal/data-paper counts, not a local recount. V8 reports only 68 Indian D10 and 135 US D40 instances; flag sparse conclusions. Official challenge test labels are unavailable; score labelled training-release holdouts. Empty annotation files are negatives; missing annotations are not assumed to mean no damage.

Norway and China, including drone imagery, are outside the core. Author ZIP sizes total roughly 2.2 GB for these four countries; compressed size is not working storage. Preserve originals/checksums and record invalid images, missing labels and conversion decisions.

### Detector and geometry

- V8 selects **YOLO11s**, COCO weights, 640 px, with **YOLO11n as the resource fallback**. Use one size for every confirmatory method. Nano screening does not establish small-model mechanisms without confirmation.
- V8 specifies Ultralytics **8.4.192 / commit 922563e**. Verify installed tag, archive actual source/configs and test assignment behaviour. This is the proposal's pin, not fresh tag verification or a recommendation to silently use the latest package.
- Standard DFL/TAL are not contributions. Avoid road-damage-pretrained weights containing a claimed held-out country.
- At a fixed 640 px reference, **small** = area below 32 × 32 px; **thin** = short side below 16 px. Primary small-or-thin population is their union, each box counted once. Keep bins across resolutions. Geometry does not measure physical crack width or severity.
- Match all labels before subgroup scoring and ignore out-of-bin matched objects correctly; deleting large labels can make their correct detections false positives.

### Source-only splits

Four outer country holdouts. Fixed inner countries in v8: Japan target→US inner; India target→Czech inner; US target→Japan inner; Czech target→India inner.

| Phase | Data roles |
|---|---|
| Development | Two sources: about 80% fitting / 20% selection; third source is simulated unseen inner country. |
| Final detector | About 70% of each of three sources for fitting; 10% for selection/operating thresholds. |
| Final C | Separate about 10% fitting / 10% selection source splits, unused for detector fitting or checkpoint selection. |
| Final test | Held-out country; no training, tuning, calibration, thresholds or redesign feedback from it. |

Keep exact/perceptual duplicate groups and recoverable sequences whole. Freeze similarity thresholds and disclose unrecoverable sequence dependence. Countries are sources in some folds and targets in others: fix global architecture, bins, trial grids and analysis before fold feedback; fit parameters within folds. Log repairs/scope changes. A global freeze cannot retrospectively remove earlier cross-fold information transfer; post-result redesign is exploratory or requires fresh evaluation.

**Unresolved v8 development-count issue:** four settings × three values gives 12 screening runs. Two values per method × four methods × four folds would require **32 further runs**, if confirmed separately, not the stated eight. Reconcile the 20–30 development-run allowance with a fold-by-fold ledger. Selecting a global shortlist on one fold may use a country later treated as unseen elsewhere; prevent or acknowledge this dependence.

## 5. Three member studies

### A: short-side-relative assignment and weighting

Let d be the length of (dx, dy, dw/2, dh/2) between Gaussian box representations, and s_g the label short side. Plain NWD uses S = exp(-d/C); A uses S = exp(-d/(kappa × s_g)). Declare coordinates and finite handling of tiny/degenerate boxes.

Replace TAL's overlap term with S. It affects positives and target-score normalisation: **assignment and weighting**, not only localisation. Keep eligibility identical to plain NWD and give C/kappa equal source-only tuning. V8 reports built-in candidate widening; verify 6, 12 and 20 px sides in the pinned code rather than claiming stock widening as new.

A is stricter on thin boxes for the same displacement. It may help or harm and is not automatically annotation-tolerant. Plot similarity curves; log positives/label, zero-positive rates and supervision mass by geometry. Principal runs use original labels. Assignment-only and widening-off checks are optional mechanism studies. Noise robustness is an extension.

**Assessable research:** implementation, matched NWD comparisons, parameter/geometry diagnostics, held-out results and interpretation.

### B: small-object-anchored scale consistency

The student gets ordinary supervised 640 px training plus a half-size consistency pass. An EMA teacher sees the full-size view without gradients. Compare up to three eligible predictions per label/view using v8's TAL rule, weighted means, per-class Bernoulli KL and normalised-box L1. Preserve ordinary supervision and average consistency over included boxes.

Restrict the added loss to small-or-thin labels. Exclude boxes below 4 px short side at half-size (8 px at reference), reporting exclusions and zero-match skips. The very thinnest subgroup receives no direct B consistency. Teacher/student agreement can reinforce an error.

Principal control: identical consistency on **all eligible boxes**, same views/mask/budget. A count-matched random subset is a one-seed secondary control. Weighting-only and 960 px comparisons are extensions; report accuracy against measured compute.

**Assessable research:** view matching, teacher/loss implementation, visibility diagnostics, controls and recall–false-positive interpretation. Highest implementation/training risk.

### C: likely missed small/thin damage

Freeze the detector and its source-selected operating threshold. A miss is a small-or-thin label unmatched by same-class, score-ordered, one-to-one IoU ≥ 0.5 matching. IoU 0.3/centre-inside checks are sensitivity analyses.

A positive cell in a 40 × 40 grid contains a missed-box centre, not crack extent; report multiple-centre collisions. The weak map uses post-NMS predictions scoring from 0.05 up to the threshold, maximum score per centre cell. Suppressed boxes are absent. If the threshold is ≤ 0.05, disclose the empty weak map.

Pool P3 to 40 × 40, concatenate P4/weak map and train v8's CNN: 1 × 1 to 32 channels, two 3 × 3 ReLU layers and one output logit/cell. Use weighted BCE, fitting-split weights, AdamW and source-selection AUPRC. Approximate 50,000 parameters depends on input channels.

**Principal control:** matched learned weak-map-only head. Raw weak map and features-only head are additional controls. Account for capacity/budget differences. Source head data must be excluded from detector fitting and selection; training-image errors can misrepresent deployment failures.

Baseline-detector heads across folds/seeds are primary. One-seed A/B heads are secondary and predict each detector's own misses; they do not show a monitor transferring across detectors. Calibration is supporting work. C predicts warnings, not recovered boxes or higher detector mAP.

**Assessable research:** miss-target creation, neural head design/training, learned controls, imbalance/matching sensitivity and held-out prediction. Lower GPU cost does not imply no research depth.

Shared conversion, evaluation/bootstrap code, APIs, UI and other engineering do not count toward individual research contributions. Each member needs substantive model experiments and their own interpretation.

## 6. Pilot and go/no-go decisions

A notebook/scripts plus a results report suffice; no demo app is needed for initial validation.

1. Validate labels/negatives, group duplicates, fix development manifests and preserve final evaluation results from iterative feedback.
2. Train stock YOLO11 on two development countries, with source selection and the third source as simulated unseen. Run 2–3 epochs for execution, then roughly 30–50 meaningful epochs, extending if learning has not stabilised. One seed screens; repeat unexpected findings.
3. Report mAP50:95, class/geometry recall, precision, false positives/image, missed boxes and positive cells/images. Save predictions and failure examples.
4. Interpret source/inner-country differences cautiously: class prevalence, difficulty and training exposure differ. A raw gap does not isolate a causal country effect. Add a matched local-domain development reference if needed/affordable.
5. Record GPU, batch size, sustained epoch time, peak VRAM, I/O and checkpoint resumption. Inspect A assignment/weights, B scale/visibility and C features/target viability before full runs.
6. Agree meaningful weaknesses and improvement criteria with the supervisor before examining diagnostic outcomes. Benchmark mAP alone does not define deployment adequacy.

| Study | Evidence needed | If absent |
|---|---|---|
| A | Problematic thin-label supervision and plausible changes from the rule; low recall alone is insufficient. | Reconsider mechanism; shape histograms do not prove annotation noise. |
| B | Scale instability for visible small/thin objects and enough eligible objects after masking. | Reconsider scale consistency; target the measured weakness instead. |
| C | Sufficient positive targets and a plausible learned signal beyond weak detections. | V8 week-8 fallback: neural image-level miss prediction. If both tasks lack viability, redesign; calibration alone is not an equivalent automatic replacement. |
| Overall | Meaningful baseline weakness and valid grid fitting committed compute. | Narrow/redesign rather than manufacture a need for A/B/C. |

**Pilot allowance:** about 1–2 calendar weeks and provisionally 10–30 GPU-hours for a few baseline runs, not measured RTX 4050/Kaggle timings. A baseline-only pilot cannot validate A/B; the full-method runtime check must include B's real passes.

**Kaggle:** reasonable for this compact pilot. Disable GPU for preparation/CPU analysis and preserve outputs. At the last platform check, [GPU guidance](https://www.kaggle.com/docs/efficient-gpu-usage) described roughly 30 weekly hours and [notebook documentation](https://www.kaggle.com/docs/notebooks) listed 12-hour sessions/20 GB saved output. Check displayed allocation and accelerators; no future entitlement is guaranteed. Do not assume P100 availability after its [retirement announcement](https://www.kaggle.com/discussions/product-announcements/735239). Preserve last.pt and verify [resume behaviour](https://docs.ultralytics.com/modes/train) against the pinned package. Pilot suitability does not establish full-grid capacity.

**Execution status:** no road-damage training, dataset audit, timing or reproduction was found in materials inspected for this update. Bicycle/JPEG Kaggle results in this workspace concern another candidate and do not validate X03.

## 7. Evaluation and interpretation

- **A:** country-macro mAP50:95; each-country/geometry results and mechanism logs.
- **B:** small-or-thin recall, precision and false positives/image at source-chosen thresholds. H2 requires higher recall with false positives ≤ 10% above generic consistency; define zero-comparator behaviour beforehand.
- **Threshold:** highest source-selection recall reaching precision ≥ 0.7; ties choose the higher threshold. Best-F1 fallback if unreachable, disclosed. No promise of 0.7 held-out precision. Freeze before C labels/fitting.
- **C:** cell-level AUPRC with positive prevalence, AUPRC/prevalence, zero-positive cases, false-alarm points and matching sensitivity. Image-level controls belong to the image-level task.
- **Statistics:** three principal seeds. Paired bootstrap whole images/duplicate groups jointly; compute method differences per seed then average. No unintended ensemble by pooling seed predictions, and no independent C-cell bootstrap. Show seed spread and residual sequence dependence.
- **Limited countries:** show all countries, country-macro and worst-country outcomes. Four wins give two-sided sign-test p = 0.125 under the simple four-independent-country sign model; image intervals do not create independent countries or worldwide evidence.
- **Support:** flag groups with fewer than 30 labels; list absent groups omitted from averages. C relies on annotation completeness.
- **Controls:** stock pooled-source YOLO, plain NWD, generic/count-matched consistency, strong augmentation, country balance and C learned/raw weak-map and features-only controls. Faster R-CNN optional. Reproduce MAMDG only with matched settings/code; adaptation methods require separate target-access accounting.
- **Negative findings:** require validated implementation and completed predeclared controls. Inconclusive is not equivalent; failure to win alone is not a contribution.

Optional noise experiments score unchanged labels, separate clean performance/noise robustness, separate corruption/training seeds and hold out a perturbation family from tuning. Three seeds sharing one corruption measure training variation, not corruption variation. V8 uses a predeclared −1.0 mAP-point clean-preservation margin; crossing intervals are inconclusive. Synthetic results cannot establish actual annotation habits.

## 8. Compute, storage and feasibility

### Training grid

| Configuration | Seeds/fold | Final trainings | Cost |
|---|---:|---:|---|
| Ordinary baseline | 3 | 12 | Ordinary |
| A, original labels | 3 | 12 | Ordinary |
| Plain NWD, original labels | 3 | 12 | Ordinary |
| B anchored | 3 | 12 | Extra views |
| B generic | 3 | 12 | Extra views |
| Random-subset consistency | 1 | 4 | Extra views |
| Country-balanced reference | 1 | 4 | Ordinary |
| Strong-augmentation reference | 1 | 4 | Ordinary |
| **Core** | | **72** | **44 ordinary + 28 extra-view** |
| Optional AB | 3 | +12 | Extra views |
| Noise/other extension bundle | Mixed | +48 | ≈53 ordinary equivalents, including 960 px control |

Core+AB is 84; adding the extension bundle gives 132 final detector trainings. Development, C heads and 16 optional severity trainings are additional. Resolve the development-count issue before accepting v8's 20–30-run allowance.

Let t = measured ordinary full-run GPU-hours, r = B multiplier, D = development in ordinary-run equivalents, and H_C = extraction/head hours:

**Core hours = 1.30 × [(44 + 28r + D)t + H_C].**

30% is contingency. B includes full student training, half-size training and teacher forward computation. V8 assumes r = 1.5; later planning considered 1.5–2.2, not benchmarks. Final core training alone is thus 86–106 ordinary equivalents.

Illustrative totals below use **r = 1.7, D = 15 equivalents, H_C = 10 hours**, including contingency. D is an assumed shortened-development budget, not a claim that 20–30 arbitrary runs equal 15 full runs.

| Ordinary full run t | Core, no AB/no noise | Core + AB | Core + AB + extension bundle |
|---|---:|---:|---:|
| 3 GPU-hours | ≈430 | ≈510 | ≈720 |
| 6 GPU-hours | ≈845 | ≈1,005 | ≈1,420 |
| 10 GPU-hours | ≈1,400 | ≈1,665 | ≈2,350 |

Columns are alternative scopes, not additive; optional severity sweeps excluded. No row is an RTX 4050/T4 measurement. V8 assumed 3–9 hours/run at about 10,700–16,100 fitting images/fold and 50 epochs. Convergence, sustained power, batches, I/O and implementation affect runtime. GPU-hours on different hardware do not imply equal work.

### C, hardware and storage

C has about **36 core learned-head fits** (three variants × four folds × three detector seeds) and about eight secondary A/B fits before tuning. V8 estimates 3–6 hours; initially reserve **5–20 GPU-hours** for extraction/fitting/tuning, ten used above. Measure it.

Try the local RTX 4050 6 GB for nano development with mixed precision/small batches, measuring memory/sustained speed. B may need smaller batches or sequential scheduling. Do not assume two GPUs pool VRAM or YOLO11n halves runtime.

V8 estimates pooled FP16 features at roughly 1.2 MB/image, about 5 GB per baseline detector/fold and **60 GB** across baseline folds/seeds. Actual channels/splits determine it; secondary A/B caches add space unless processed sequentially. Reserve **100–200 GB working storage** for data copies, caches, checkpoints, predictions and logs. Old 10–25 GB estimates conflict with the cache estimate. Manage cloud output quotas and preserve required results before removing intermediates.

At **845 hours**, 20 reliable hours/week requires ≈42 GPU-access weeks; 30/week ≈28; 40/week ≈21. These are not full-project calendar guarantees. Occasional 15–25-hour access is not a comfortable core commitment unless measured runs approach the optimistic end.

### Cuts and milestones

1. Drop noise and AB before principal contrasts.
2. Defer C's secondary A/B heads.
3. Switch every method to YOLO11n if required and document it.
4. Bound development trials without cross-fold feedback.
5. Following v8, defer country balancing before strong augmentation or B's count-matched control; disclose the limitation.
6. Keep resolution, extra noise severities and further architectures exploratory.

Do not quietly drop an outer country, principal comparator or confirmatory seeds, or cap images indiscriminately and erase rare classes. If the valid core still cannot fit, formally redesign with the supervisor.

V8 milestones: protocol/data/literature weeks 1–3; implementation/runtime pilot by week 6; C viability by week 8; source-only development and rolling frozen runs; global freeze around week 22; finish/score around weeks 23–27. Confirm module dates/compute. Final predictions remain unscored/uninspected until the required freeze.

## 9. Research balance, demonstration and limits

All members train/adapt neural models: A/B retrain detectors; C trains a CNN on frozen features. Equal assessable research does not require equal GPU-hours or code length; it requires substantive methods, comparisons, diagnostics and interpretation. Demo/shared engineering does not balance research.

B has the highest implementation/training risk; A's mechanism is especially uncertain; C has target-definition, imbalance and transfer risks. A later FastAPI/web demo may show boxes and estimated warnings. Verify C's intermediate-feature availability on export; ordinary detector export need not include its monitor. No new photos or human study are needed.

Four countries do not represent all conditions; geometry is not severity; consistency can reinforce errors; the monitor can fail under shift; incomplete labels affect both tasks. No safety, economic or Sri Lankan deployment claim follows automatically.

## 10. Historical score and current decision

**Historical score: 76.7/100 on 28 October 2026**, for the earlier annotation-tolerance/calibration scope. Not a current v8 score, model result or qualification. Original ratings: novelty 3/5, others 4/5; weights 16/15/14/12/12/12/9/5/3 total 98. No fresh score is assigned merely for rewriting. Demo engineering is not individual research credit.

| Gate | Current assessment | Reason |
|---|---|---|
| 1. Specific real problem | Pass in literature; local severity pending | Baseline diagnosis missing. |
| 2. ML essential | Pass at design level | Assignment, consistency and neural monitoring central. |
| 3. Train/adapt | Pass at design level | All three have neural work; no paid inference API. |
| 4. Data accessible | Pass for documented release; local audit pending | No acquisition/decoding result recorded here. |
| 5. No unavailable human evaluation | Pass | Existing labels, no new collection/user study. |
| 6. Precise gap | **Unknown** | Exact overlap and added value unresolved. |
| 7. Beyond app assembly | Pass if executed | Methods and controls, not app-only work. |
| 8. Objective evaluation | Pass at design level; corrections pending | Reconcile trial budget and decision leakage. |
| 9. Six-to-eight-month feasibility | **Unknown** | Runtime, trial accounting and access unmeasured. |
| 10. Three connected contributions | Pass at design level; adequacy conditional | Retain substantive C study or formally redesign. |
| 11. Compute sufficient | **Unknown** | Model fit alone does not establish grid capacity. |
| 12. Responsible use | Pass for bounded benchmark | Licence and interpretation limits recorded. |
| 13. Useful negative findings | Conditional | Motivation, correct implementation and completed controls required. |

**Decision:** conditional candidate, not validated novelty/feasibility. Run the source-only baseline diagnostic pilot, then take weaknesses, full-method timing and closest-method comparisons to the supervisor before committing the grid. If stock YOLO works adequately or thinness is irrelevant, revise the scope rather than assume all three interventions are needed.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Original search records](../../metadata/expansion-records.json)
