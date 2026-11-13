# X48: additional literature, candidate gaps and three-member research plan

Review date: 13 November 2026. Status: evidence-bounded recommendations for a feasibility pilot, not established novelty or a replacement approved proposal.

Scope correction: the supervisor-approved simulation-first study is **not limited by the duration of available real satellite clips**. This revision removes that inherited restriction. Sequence duration follows the behaviour, source-data support and resource budget. Earlier short-burst recommendations in this report are superseded.

## 1. Recommendation

The project can plausibly support three independently assessable contributions, but **not merely by assigning three behaviour categories or three satellite styles to different students**. A stronger organising question is:

> How can vessel movement and interaction patterns be recognised reliably from variable-duration synthetic optical satellite sequences when image generation, incomplete observations and uncertain tracking can each corrupt the motion evidence?

Recommended packages:

1. **Motion-preserving image translation:** investigate and reduce distortion introduced when making rendered ship sequences look more realistic.
2. **Multi-timescale, observation-aware behaviour classification:** recognise individual movement patterns across local manoeuvres and longer episodes, while accounting for observation gaps and uncertainty.
3. **Association-aware interaction classification:** recognise pairwise movement and multi-stage interactions while accounting for uncertain track identities near crossings and interruptions.

These have different experimental interventions and endpoints. The first changes the training imagery; the second changes how individual motion is classified; the third changes how tracking ambiguity enters interaction inference. All can use the same source AIS, renderer and evaluation infrastructure. None requires real satellite video for its central **simulation-only** claim.

This is a conditional recommendation. Package 1 has the greatest compute and implementation risk; package 3 has the greatest encounter-data and association-modelling risk. Package 2 can start with cached tracks, but its novelty must go beyond longer input windows, confidence thresholds or missing-value masks. Longer-duration repeated-pattern modelling is also reopened as an alternative to the translation package; see Section 5.4. No fourth student or fourth mandatory contribution is proposed.

The proposal should say **AIS-free inference on simulated optical observations**, not demonstrated detection of illegal ships or demonstrated performance on real dark vessels. AIS-equipped source vessels also need not represent small non-AIS vessels.

## 2. Scope, criteria and review limitations

This extends the [simulation/translation review](x48-simulation-translation-literature-review-2026-11-13.md), and uses the [team criteria](../../../research-module-and-team-criteria.md). It does not silently revise the [main proposal](x48-satellite-vessel-behaviour-from-synthetic-sequences.md) or [revision-3 protocol](x48-simulation-first-workload-and-review-brief.md).

Selection criteria, applied qualitatively: precise difference from prior work; independent model investigation; testability without real video or new human annotations; public-data suitability; modest compute; useful null result; coherence with the shared objective. Unknown data suitability prevents a defensible numerical proposal score.

The supervisor's simulation-first decision is retained. Real video verification is optional later and does not set a maximum simulation duration. The project's specific waiver of the earlier crime-topic preference is respected, while keeping movement labels distinct from legality.

### Duration and observation policy

- Choose simulated episode lengths from the operational behaviour definition and supported AIS history. Short manoeuvres, repeated patterns and sustained interactions need not share one fixed duration. Select a bounded set of duration bands after the source audit; there is no mandatory 60–120-second cap.
- Distinguish **episode duration**, **observation cadence** and **model input window**. A long episode may be processed in chunks with persistent model state. Sparse images cannot establish every movement between observations, regardless of total episode length.
- Long continuous overhead observation is an explicit simulation assumption, not a claim that a particular satellite can deliver it. Include interruptions or alternative sampling schedules as experimental conditions. Real-data checks, if later available, apply only to their supported conditions.
- Longer source-backed motion requires adequate recorded AIS support. Interpolation does not confirm unobserved turns or stops. Keep purely procedural scenarios separate from AIS-supported episodes and state which results each supports.
- Longer sequences may cross the original field of view. Specify a larger scene, tiled coverage or a moving camera with known registration; use consistent world coordinates for motion evaluation. Do not silently keep ships centred and treat the resulting image coordinates as physical motion.

This is a scope correction to the existing literature synthesis, not a new completed search proving novelty for long-duration methods. Duration alone is not a contribution. The longer-pattern alternative needs its own focused comparison with prior sequence models before being selected.

This is a targeted critical literature review, not an exhaustive systematic review. Searches covered publisher pages, conference proceedings, author PDFs, arXiv and dataset records. Representative additional queries included `maritime vessel behavior recognition track identity uncertainty probabilistic event recognition`, `early classification maritime trajectory behavior uncertainty missing observations`, `satellite video ship tracking identity switches behavior classification uncertainty`, `synthetic data domain randomization counterfactual invariance sim to real object detection ships`, and exact-title searches for the studies below. Search silence is not evidence of novelty.

Consensus's previous requested review was blocked by its usage allowance before returning research. It was not retried and supplies no results here. No model experiments or dataset-content audits were conducted during this review. Published dates were distinguished from crawler dates; a future-issue record is flagged below.

Evidence labels: **M** = relevant full-text methods inspected; **A** = primary abstract/indexed publisher excerpts; **P** = primary project/repository record. Not every appendix or implementation was inspected.

## 3. Additional literature that narrows the gap

| Study | Input and established contribution | Implication for X48 | Evidence |
| --- | --- | --- | --- |
| [Guo et al., Ship encounter identification from compressed trajectories: A high-efficiency framework, Ocean Engineering, 2026](https://doi.org/10.1016/j.oceaneng.2026.125198) | AIS compression, encounter extraction and Bayesian reliability analysis; evaluates behavioural fidelity and risk consistency | Sparse encounter recognition and uncertainty evaluation already exist. A stronger distinction is image-induced identity ambiguity, not simply reducing trajectory samples. | M, indexed full text and author record |
| [Mantenoglou, Artikis and Paliouras, Online Event Recognition over Noisy Data Streams, IJAR, 2023](https://cer.iit.demokritos.gr/publications/papers/2023/opiec-ijar.pdf) | Probabilistic interval event recognition; maritime rendezvous and tugging experiments using Brest AIS | Uncertainty-aware maritime events are established, including on your proposed source data. A new package must compare against probabilistic reasoning, not only deterministic thresholds. | M |
| [Singh et al., Leveraging Graph and Deep Learning Uncertainties to Detect Anomalous Trajectories, 2021 preprint, revised 2022](https://arxiv.org/abs/2107.01557) | Graph representation and evidential neural models for AIS prediction, unusual turns and signal loss | Adding uncertainty to vessel movement analysis is not new. Image-observation sufficiency is a narrower research question. | A |
| [Al-Falouji et al., Representation Learning for Maritime Vessel Behaviour: A Three-Stage Pipeline for Robust Trajectory Embeddings, JMSE, 2026](https://www.mdpi.com/2077-1312/14/5/507) | Six architectures; masked/grouped representation learning, risk extrapolation, denoising and evidential baselines | Generic robust maritime embeddings and feature-group regularisation are already studied. Clustering and ship-type probes are not identical to your proposed movement labels. | M |
| [Che et al., Recurrent Neural Networks for Multivariate Time Series with Missing Values, Scientific Reports, 2018](https://www.nature.com/articles/s41598-018-24271-9) | GRU-D incorporates masks, elapsed time and learned decay | Missing timestamps, confidence inputs or a modified GRU alone are insufficient novelty. Include a missingness-aware baseline. | A |
| [Geifman and El-Yaniv, SelectiveNet, ICML 2019](https://arxiv.org/abs/1901.09192) | Joint classification and rejection; evaluates risk versus coverage | Abstention itself is established. Investigate whether observable image/track quality improves selective decisions under unseen degradation. | A |
| [Schäfer and Leser, TEASER: early and accurate time series classification, DMKD, 2020](https://doi.org/10.1007/s10618-020-00690-z) | Learns when to classify using partial sequences, balancing time and accuracy | Early classification is not a new idea. Observation quality and reliable decisions across variable-duration episodes are narrower candidate questions. | M, indexed methods |
| [Zhang et al., ByteTrack, ECCV 2022](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136820001.pdf) | Associates low- as well as high-confidence detections for multi-object tracking | Recovering weak detections is established. Package 3 should study event errors caused by residual association ambiguity, not claim invention of tracking. | A |
| [Joint Adjustment Image Stabilization Method Based on Trajectories of Maritime Multi-Target Detection and Tracking, Applied Sciences, 2026](https://www.mdpi.com/2076-3417/16/8/4029) | Maritime GEO image detection/tracking and multi-target trajectory-based stabilisation | Ship trajectories and inter-target geometry have already been used for maritime satellite stabilisation. Camera correction alone is not a strong new package. | A, indexed methods |
| [Less is more: A semi-supervised fine-grained object detection for satellite video, Engineering Applications of AI](https://www.sciencedirect.com/science/article/abs/pii/S0952197624017676) | Appearance/motion feature fusion with first-frame supervision; SAT-MTB-DET experiments | Low-label satellite-video detection already has direct precedent. Ship-type classes are not movement classes. | A |
| [Yue et al., Domain Randomization and Pyramid Consistency, ICCV 2019](https://openaccess.thecvf.com/content_ICCV_2019/papers/Yue_Domain_Randomization_and_Pyramid_Consistency_Simulation-to-Real_Generalization_Without_Accessing_Target_ICCV_2019_paper.pdf) | Simulation-to-real segmentation through domain randomisation and consistency | Appearance-invariant synthetic learning is established generally; a counterfactual movement study needs a more specific intervention and test. | A |

Important carried-forward competitors include [LoPIT](https://doi.org/10.1109/TGRS.2022.3211517), [Syn2Real aerial ship detection](https://doi.org/10.3390/app14114558), [SPAM-ControlNet](https://doi.org/10.1016/j.jag.2025.104996), and [Video ControlNet](https://arxiv.org/abs/2305.19193). They establish ship-image translation, controlled generation or temporal/geometry preservation. Video ControlNet also examines tracking outcomes; evaluating tracking after translation is therefore not sufficient novelty by itself. Details and access limitations are in the earlier review.

**Watch-list, excluded from time-bounded conclusions:** [Ou et al., A vessel trajectory abnormal behavior classification method for cross-domain generalization and local motion pattern similarity mitigation](https://doi.org/10.1016/j.ress.2026.113742) appears in the live publisher index with a March 2027 issue date and describes dual-branch classification plus few-shot cross-domain adaptation. The first-online date was not verified. Do not cite it as an established 2026 publication without resolving that metadata; check it before submission because it may further constrain cross-domain novelty.

## 4. Candidate gaps and decisions

All entries below are **proposed questions**, not located findings that these failures necessarily occur in your data.

| Candidate | Narrow question beyond established work | Main challenge or rival explanation | Decision |
| --- | --- | --- | --- |
| G1: Motion fidelity during translation | Can vessel-local geometric constraints preserve tiny-object displacement and interaction geometry while improving appearance? | Generic temporal consistency and label preservation already exist; apparent success may simply mean avoiding any appearance change. | Shortlist as package 1; higher risk |
| G2: Observation sufficiency | Can a classifier distinguish insufficient motion evidence from a supported movement label under unseen resolution/cadence/dropout combinations? | Selective classification, early classification and uncertainty already exist; gains may come only from rejecting more cases. | Shortlist as package 2 |
| G3: Identity ambiguity in interactions | Does retaining limited alternative track associations reduce false interaction events compared with committing to one track identity? | Probabilistic events and multi-hypothesis tracking are established; benefits may come entirely from a stronger tracker. | Shortlist as package 3; encounter-data gate |
| G4: Shortcut-resistant simulation training | Can paired renders of identical motion with different irrelevant appearance improve behaviour robustness to held-out rendering conditions? | Domain randomisation and consistency are established; more training data may explain the gain. | Lower-compute replacement candidate for package 1 |
| G5: Uncertain AIS-to-image supervision | Does weighting approximate render/real pairs by alignment uncertainty improve translation without moving the ship? | Requires reliable matching and appropriate image resolution; registration-aware translation already exists. | Defer until a matching-data pilot succeeds |
| G6: Behaviour-preserving stabilisation | Can correction remove camera jitter without removing true turns or relative movement? | A direct maritime satellite stabilisation precedent exists; sea-only scenes can make camera/object motion unidentifiable. | Include as stress test; weak standalone novelty currently |
| G7: Longer-duration repeated-pattern modelling | Can a compact temporal hierarchy distinguish isolated manoeuvres from sustained patterns despite gaps and chunk boundaries? | Longer inputs and hierarchical sequence models are established ideas; gains may come solely from extra history or compute. | Reopened alternative to package 1; independent-pattern data and focused literature gates |

Another useful question is **how uncertain AIS-derived labels affect learning**, particularly near rule thresholds and gaps. It is not recommended as an additional package now: generating several rule labels and voting is not independent truth, and it would expand an already demanding plan. Threshold sensitivity and source-support flags should be shared evaluation controls.

## 5. Three independently assessable packages

### Member 1 — Motion-preserving translation

**Research question:** For small vessels, can a bounded translator adaptation reduce geometric distortion relative to a credible temporal translator while retaining useful appearance adaptation?

**Proposed method:** start from an existing image translator and add a small temporal/consistency adaptation. Use simulator instance masks and known motion to weight vessel-local consistency rather than letting the large water background dominate. Investigate a bounded subset of centroid/displacement and inter-vessel-distance constraints. These are candidate mechanisms, not a claim that a new loss automatically constitutes novelty.

**Hypothesis:** vessel-local constraints reduce trajectory and event-label corruption at comparable appearance quality, training data and compute. An identity translator is a necessary control: perfect motion preservation without adaptation does not answer the research question.

**Independent experiments:** plain rendering; domain randomisation; framewise translation; an affordable temporal-consistency baseline; proposed adaptation. Run the same held-out source motions through each. Measure visible-vessel omission, centroid/displacement error, heading-change error where observable, pair-distance distortion, and fixed downstream model degradation. Separately compare downstream models trained with each data variant on the **same** held-out test set.

Evaluate these over increasing episode lengths, including accumulated trajectory drift, appearance/identity consistency and discontinuities between translated chunks. Compare stateful and independently processed chunks if supported by the chosen method. A short training window may be a compute choice, but it is not a maximum evaluation duration. Known simulator motion should anchor evaluation so drift cannot be hidden by frame-by-frame realignment.

Measure metres as well as pixels, stratified by vessel pixel size. Mask positions alone do not prove that translated pixels still depict the vessel. Use an evaluation detector distinct from any detector used in the training constraint and inspect generated failure cases. Respect deliberately modelled occlusion: a valid method must not force a hidden vessel to remain visible.

**Ablations:** no temporal term; background-dominated versus vessel-weighted consistency; no geometry term. Report appearance, motion fidelity and compute together. Real still-image evaluation, if undertaken, supports only that imaging/detection endpoint, not real behaviour recognition.

**Deliverables:** trained/adapted model, distortion benchmark, controlled ablations, failure analysis and reproducible compute account. Renderer implementation alone does not satisfy this package.

**Failure condition:** if translation causes no material motion distortion in the pilot, or simple randomisation performs as well at far lower cost, do not invent a need for a large translator. Investigate G4 instead, subject to its own baseline pilot. Neither route is pre-approved as novel.

### Member 2 — Multi-timescale, observation-aware movement classification

**Research question:** Can quality-conditioned temporal aggregation recognise individual movement across different durations more reliably than fixed-window models given the same observation history?

**Proposed method:** a compact causal GRU or temporal CNN with quality-conditioned aggregation across local and longer windows; an abstention head is a secondary reliability mechanism. Input observed positions/displacements, time gaps, visibility and track-quality estimates. Train across controlled degradation, episode lengths and arbitrary observation starting points. Do not provide true AIS speed, true vessel identity, renderer quality settings or future observations at inference.

**Hypothesis:** quality-conditioned use of multiple timescales improves recognition and calibration under held-out duration/gap combinations compared with equally tuned fixed-window and full-history models. Include the same history and quality inputs in strong competing models to isolate the aggregation mechanism; test selective performance at matched coverage separately.

**Targets:** source-supported transit, turning, deceleration-to-stop and sustained stationary motion; add a bounded subset of repeated turns or circling where independent episodes and adequate observations exist. Define duration requirements and multi-label or mutually exclusive rules, including overlapping turn/deceleration cases. Geometric circling is not automatically loitering: any operational loitering label must satisfy its full duration/context definition, with required context available to the model or explicitly excluded from the target.

**Independent experiments:** keep detector/tracker and renderer fixed. Vary spatial resolution, frame interval, episode duration and missing observations in a bounded design. Compare observed-track rules with smoothing/persistence, feature-based learning, GRU-D-style missingness handling, tuned single-window and full-history temporal models, and a SelectiveNet-style reliability baseline. Compare multi-scale aggregation against a simple multi-window ensemble. An early-decision experiment is optional, not another mandatory subsystem.

**Metrics:** macro-F1 on the full task; risk–coverage curves; class-specific retained coverage; calibration; error at matched coverage. Report detection failures and abstentions separately. For early decisions, compare equal observed histories and include decision delay; confidence on a full sequence is not a fair online competitor.

**Ablations:** temporal scales, quality conditioning, retained state across chunks, selection objective and training degradation coverage. Include unseen duration/corruption combinations to test whether the model learned useful relations rather than memorising simulator settings. Separate improvement from additional history from improvement due to the proposed method.

**Deliverables:** trained temporal model, equal-history timescale comparison, observation-gap analysis, selective evaluation and per-class failure boundaries. A longer input window or confidence threshold added to an otherwise standard classifier is too small by itself.

**Failure condition:** no benefit over strong equal-history models, or classes remain indistinguishable under the chosen observations. A carefully measured observability or efficiency limit can still be valuable, but an underpowered comparison is inconclusive rather than a demonstrated limit.

### Member 3 — Interaction classification under uncertain association

**Research question:** Can an interaction model avoid false closing/co-moving/passing events when tracking identities become ambiguous?

**Proposed method:** use a fixed tracker and retain a small, bounded set of alternative local associations around ambiguous crossings. Train a compact pairwise temporal model that aggregates predictions using estimated association weights. Compare this with taking only the best association. This adapts established probabilistic reasoning; it does not invent multi-hypothesis tracking.

Use only observed candidate tracks and permissible detection/association features. Ground-truth identities are available for training supervision and evaluation, never as inference inputs. Candidate weights need calibration or explicit treatment as heuristic scores; raw matching costs are not automatically probabilities.

**Hypothesis:** propagating association ambiguity reduces false interaction alerts without unacceptable loss of event recall, beyond both a stronger fixed tracker and a deterministic model with the same confidence features.

**Independent experiments:** freeze renderer, detector and candidate-pair policy. Compare oracle identities as a diagnostic upper bound, ordinary hard association, hard association with quality features, a probabilistic event baseline, and the proposed bounded alternative-association model. Test both controlled identity swaps/fragmentation and naturally occurring tracker errors on rendered images; the former alone is a narrower experiment.

Extend evaluation to multi-stage episodes and recovery after gaps. Bound the retained association alternatives so longer sequences do not cause combinatorial growth. Compare the same available history and memory/compute budget, and measure how errors accumulate with interruption length and episode duration.

**Targets:** closing, separating, passing and approximately co-moving, plus a bounded multi-stage pattern such as approaching → remaining nearby → separating when supported by the source episode. Define stages, duration requirements and overlaps. Do not call these verified ship-to-ship transfer, collaboration or illicit intent. Pure pair distance can be invariant to swapping the two members of an isolated pair; include third-vessel distractors and identity-dependent temporal features so the tested failure is actually relevant.

**Metrics:** event precision/recall/F1, false alerts per scene-time, candidate-pair recall, missed-event counts, calibration and runtime. Report association quality separately, including identity switches. Evaluate the hypothesis at matched recall or matched false-alert rate rather than claiming success from suppressing all difficult alerts.

For multi-stage events, predeclare interval matching and boundary tolerance; report stage order errors, onset/end timing, duplicate alerts and recovery after interruptions. Count complete source events rather than treating every overlapping window as a new independent event.

**Ablations:** number of alternative assignments; aggregation without learned weights; confidence-only control; oracle versus estimated weights. Use the same tracker outputs for the main classifier comparison.

**Deliverables:** trained interaction model, association-error stress suite, independent ablations and an end-to-end error account.

**Failure condition:** too few independent encounters, no meaningful identity ambiguity, or gains disappear when the baseline tracker improves. Do not compensate for missing independent events by creating thousands of overlapping windows from a few encounters.

### 5.4. Reopened alternative — A behaviour-focused three-member allocation

If the team prefers three behaviour-model contributions, replace member 1's translation investigation with **longer-duration repeated-pattern modelling**. Keep basic rendering shared and learned image translation optional. In this allocation:

| Member | Distinct research focus | Main independent test |
| --- | --- | --- |
| A | Local manoeuvre recognition under observation degradation; narrow package 2 to local evidence and quality-aware selection | Recognition and risk–coverage under held-out observation conditions |
| B | Pairwise multi-stage interaction under association ambiguity; package 3 | Event errors and recovery with identity uncertainty |
| C | Hierarchical temporal modelling of sustained/repeated individual patterns | Long-pattern recognition under gaps and chunk boundaries at equal history and compute |

Member C's candidate method aggregates learned local-motion embeddings with a compact stateful episode-level model. Its hypothesis is that explicit local-to-episode structure preserves ordering and duration information more robustly than a flat model or simple pooling. Compare tuned rules, aggregate-feature learning, flat full-history GRU/TCN, pooling and a basic hierarchical baseline. Ablate ordering, duration features, state retention and the proposed mechanism. Evaluate episode-level macro-F1, temporal boundaries where applicable, generalisation across durations and memory/runtime.

To make this independent of A, freeze a shared baseline local encoder for C's main comparison; A's improved model is only an integration experiment. To distinguish it from merely assigning different classes, C must test a temporal modelling mechanism against equal-history competitors. Do not give C's model a longer observation history and present the resulting advantage as architectural novelty.

This alternative is now eligible because real clip duration no longer excludes sustained behaviours. It is **not yet a stronger established gap**: existing AIS pattern classifiers and general hierarchical temporal models must be checked against the exact target. Source-position plots, supported durations and independent vessel/episode counts remain gates. Select either this allocation or the translation-inclusive allocation after the pilot; do not combine both into four major workloads.

## 6. Why the packages are independently assessable

| Item | Member 1 | Member 2 | Member 3 |
| --- | --- | --- | --- |
| Intervention | Translation/adaptation objective | Multi-timescale classification and quality conditioning | Association-conditioned interaction inference |
| Frozen comparison components | Source scenes and downstream evaluator | Renderer and detector/tracker | Renderer, detector, tracker and pair policy |
| Main endpoint | Motion fidelity and drift over episode duration | Equal-history recognition across durations and observation quality | Interaction and stage errors under association ambiguity |
| Can begin without the others' proposed model? | Yes: baseline motion evaluator | Yes: plain renderer and cached tracks | Yes: plain renderer and baseline associations |
| Individual evidence | Adaptation ablations, distortion and chunk-drift analysis | Timescale/quality ablations and coverage curves | Association ablations and episode-level event-error analysis |

Shared work: AIS ingestion, licences, source audit, renderer, label definitions, grouped splits, baseline detector/tracker, cache format and demo. Attribute this engineering effort, but do not use it as a substitute for any member's experiments.

For integration, freeze the individual methods first. Test the complete pipeline and remove each contribution in turn. Individual evaluations remain essential because a better final pipeline does not reveal which student's method helped.

## 7. Data and evaluation gates

| Resource | Role | What remains unverified |
| --- | --- | --- |
| [Brest original AIS release](https://zenodo.org/records/1167595) | Source trajectories and concurrent encounters; record lists a 201.4 MB AIS archive | Actual task-specific cadence, independent manoeuvre/encounter counts, full metadata and licence suitability; landing-page access is not a content audit |
| [Composite Maritime Events](https://zenodo.org/records/2557290) and [Pitsikalis et al.](https://arxiv.org/abs/1903.03078) | Existing operational event definitions and weak/reference labels; longer simulation can accommodate their required histories | Alignment with source observations, full duration/context requirements and usable independent counts; rule events do not establish independently verified intent or provide every desired movement class |
| [UnityShip](https://doi.org/10.3390/rs13244999) and shared procedural renderer | Appearance references and controlled images | Asset redistribution rights, practical rendering cost and usable source models |
| [Finnish Sentinel-2 ship dataset](https://zenodo.org/records/15019034) | Optional real still-image detection/appearance test | Scale compatibility and annotation conventions; not real-video behaviour validation |
| [AIS-associated Sentinel-2 dataset](https://zenodo.org/records/20179706) | Optional alignment/translation investigation | Approximately 39.1 GB release; suitability of matching metadata and raw AIS access require inspection; not a core dependency |

Retain revision 3's task-specific source-support rules. Sparse stationary AIS should not be rejected using a universal underway-cadence rule, nor treated as confirmed continuous stationarity through interpolation. Require observations to support window boundaries and report retention by behaviour and vessel category. Store interpolation assumptions separately from observations.

Use recorded concurrent encounters for claims about AIS-derived encounter distributions. Procedurally assembled interactions can expand a controlled stress test, but label them as such; they do not establish their natural prevalence or operational realism.

Partition vessels first with a documented fixed seed and retain only scenes whose participating vessels belong to the same partition, as specified in revision 3. Report cross-partition encounters discarded. Keep all overlapping windows and renders together. For uncertainty, resample connected source groups formed by shared vessel/episode dependencies, not independent frames; report resulting component counts and any giant component.

Hold out source motions and appearance assets; also reserve degradation combinations. Do not call a held-out random render from the same scene an independent test. Source AIS/rule labels are privileged offline references, not inference features. Evaluate any learned method against tuned rules operating on the same noisy observations; clean-source rules are an oracle diagnostic.

Simulator test results establish performance under the stated rendering, sensor and corruption assumptions. They do not establish generalisation to actual satellite sequences. Real still images cannot fill that temporal evidence gap. Sentinel-2-like resolution and frequent high-resolution video should be treated as separate imaging configurations, not blended into a physically unsupported sensor claim.

## 8. Bounded pilot and resource plan

Start with a two-to-three-week pilot before finalising all three contributions:

1. Audit existing AIS: source timestamps, supported episode lengths, repeated-pattern examples, concurrent multi-stage encounters and independent split-group counts. Produce position plots with recorded points visible.
2. Render a small, reproducible set of single-vessel and multi-vessel scenes across bounded duration bands; cache detections and tracks. Check target observability, field-of-view handling and chunk boundaries.
3. Member 1 tests whether an affordable translator changes motion geometry over time and whether domain randomisation already suffices. Also screen G7's data and baseline feasibility before choosing the final allocation.
4. Member 2 tests quality-conditioned temporal aggregation against equal-history baselines, with selective classification as a secondary evaluation.
5. Member 3 tests whether association ambiguity causes interaction/stage mistakes and whether a strong tracker already removes them.
6. Record GPU memory, wall-clock training/rendering time, disk footprint and variance across available seeds. Choose the full experiment size from those measurements and the remaining project time.

No invented universal minimum sample count is imposed. Report independent counts per class and split, inspect learning curves and pilot uncertainty, then predeclare acceptable precision and a feasible experiment budget. If a key class cannot support a meaningful held-out comparison, narrow or replace that package before commitment.

Use one rendering engine, one optical family, one fixed baseline detector/tracker and compact temporal models. Cache tracks/features so members 2 and 3 do not repeatedly train vision backbones. Avoid foundation-model training, several sensor-specific generators, simultaneous SAR simulation and an unrestricted end-to-end video transformer.

Long episodes need not be loaded as full-resolution video tensors. Stream rendering and detection, cache compact features, and train with bounded chunks while retaining the state needed for the research question. Record how state is carried or reset. All chunks from one source episode remain in the same split. Estimate frame/storage costs from episode duration × sampling rate before scaling; lowering frame rate changes available motion evidence and must be evaluated explicitly.

If translator training exceeds available resources, the fallback is G4: train a compact visual/temporal model with matched-motion, varied-appearance consistency and test against equally sized domain-randomised training. Preserve valid physical cues such as wakes when defining label-preserving changes. Test held-out assets and appearance–label correlation reversals. This fallback still needs a specific demonstrated failure and comparison with existing consistency methods; ordinary augmentation is not automatically a contribution.

## 9. Verdict against the team criteria

**Plausible structure; feasibility remains unconfirmed.** The three packages contain separately attributable model investigations and share one coherent objective. They fit simulation-first evaluation and avoid unavailable expert annotations. Compact downstream models make most experiments compatible with limited GPU access, while translation remains conditional on a measured pilot.

There is no real-footage-duration gate. The revised choice is between a translation-inclusive allocation and a behaviour-focused allocation with an independent longer-pattern method. Longer simulation enlarges the testable scope; it does not itself establish novelty, create independent source examples or demonstrate actual satellite acquisition capability.

Do not yet declare the public-data, exact-gap, compute or three-member feasibility gates fully passed. The review narrows plausible contributions; it does not supply the missing cadence audit, class counts or baseline results. The useful next commitment is the pilot, followed by a frozen three-package proposal based on observed failures.

No first-ever claim is recommended. A defensible claim would be a specific method and controlled evaluation of one failure mechanism, with its closest competitors acknowledged and its simulation-only limits stated.

## Review provenance

Candidate generation and critique were AI-assisted using the scientific-brainstorming and scientific-critical-thinking skills. The team and supervisor retain the selection decision. Following the brainstorming skill's attribution requirement: Kassis, T., Agarwal, V., He, Y., Patel, D., and Brueckner, A. M. (2026), [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://doi.org/10.48550/arXiv.2609.00065). This is a workflow reference, not evidence for the maritime gap claims.
