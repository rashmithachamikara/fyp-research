# X48: Simulation-first vessel movement behaviour recognition

**Purpose:** Self-contained handoff for another agent to review and improve the project scope, research contribution, workload distribution and evaluation.

**Updated:** 10 November 2026, revision 3 after a targeted follow-up review
**Stage:** Proposed research design; no implementation results are claimed.  
**Supervisor direction, as reported by the team:** Start with simulation only; move to real-satellite verification later if possible.

> **Scope precedence:** This document records the latest direction. Earlier X48 notes and the four-page PDF treated real-footage evaluation as an initial go/no-go requirement. That requirement is superseded for the approved simulation-first starting scope. Real-data access is now an optional extension, while accessible simulation inputs and a defensible synthetic evaluation remain essential.

**Revision summary:** Retain the three behaviour families, but make A a quality-aware recognition and recoverability investigation, B an observed-pair and identity-error investigation, and C a partial-pattern investigation constrained by the observation duration. Prefer the original Brest AIS positions together with Composite Maritime Events. Add a declared observation contract, matched rendering comparisons, causal evaluation, complete event denominators and explicit decision criteria. See the [review decision log](x48-review-response-and-revision-log.md) for suggestions adopted, modified or declined.

**Revision 3 changes only:** Replace the universal dense-AIS screen with task-specific source support; require recorded-point evidence and independent-group counts for C; specify vessel-disjoint partitioning and the dependent-group resampling procedure together. The scope remains a bounded feasibility pilot.

## 1. Project in plain language

AIS (Automatic Identification System) broadcasts vessel positions and movement information. The project would use recorded AIS paths to create computer-rendered optical satellite-style image sequences. Models would learn to recognise observable vessel movement from those images or from tracks extracted from them.

At prediction time, the intended input is an image sequence, with timestamps and any explicitly assumed camera calibration. The vessel's AIS messages are not supplied to the classifier. The simulator retains reference positions and labels separately for evaluation.

Three students would investigate different behaviour families using one shared simulator and experimental pipeline:

1. Short-window movement of an individual vessel.
2. Relative movement and interactions between vessels.
3. Patterns requiring more history within a finite observation burst, such as repeated direction changes rather than a single turn.

The intended application is eventually screening vessels visible in satellite imagery, including vessels without a reliable AIS match. Simulation alone cannot establish accuracy on real AIS-silent vessels, actual intent or illegal activity.

## 2. Approved direction versus design choices

| Status | Item |
|---|---|
| Confirmed by the user | The supervisor supports starting with simulation and attempting real verification later if possible. |
| Confirmed project context | Three students; one coherent research project; substantial individual contributions; existing datasets; limited/occasional GPU access; approximately 6-8 months of implementation within one year. |
| Proposed here | Shared data generation and infrastructure, with research responsibilities divided by behaviour family. |
| Still to establish | Usable Brest subsets and event alignment, precise class definitions, simulation fidelity, supported observation durations, model choices, experimental budget and novelty of each investigation. |
| Optional extension | Verification on real satellite footage, with separate labels and a suitable held-out test. |

The team's earlier preference to avoid crime-related topics was explicitly waived for this project. The proposed prediction targets nevertheless remain observable movement rather than illegality.

## 3. Objective and research question

**Working objective:** Develop and evaluate vessel movement behaviour classifiers using AIS-driven synthetic optical satellite image sequences under varied observation conditions.

**Working research question:** Under a declared finite-burst simulated observation model, when do quality-aware, pairwise and multi-scale temporal models improve recovery of operational vessel movement patterns over tuned rules and feature models given the same observations?

These are working formulations for review, not established novelty claims. A useful outcome could identify conditions where simple rules are sufficient, where learning helps, or where the behaviour cannot be recovered reliably.

## 4. Shared pipeline and information boundaries

```text
Existing AIS records
    -> clean and group complete voyages / simultaneous vessel groups
    -> assign train / development / test partitions
    -> derive reference movement labels from explicit definitions
    -> render timestamped optical satellite-style sequences
    -> detect and track vessels / extract observed positions
    -> three behaviour models
    -> evaluate against separately stored simulation references
```

**Shared work:** AIS preparation, coordinate conversion, renderer, assets/backgrounds, reference labels, detector/tracker, dataset manifests, splits, metrics, experiment logging and demonstration interface.

**Reference information:** Full-resolution AIS paths, simulator coordinates, true identities and reference labels are available to the generator and evaluator. They must not silently enter the classifier inputs. Explicit oracle experiments may use them, but must be reported separately.

**Observed information:** Predicted positions, estimated track IDs, timestamps and observable image features. Pairwise models receive two or more simultaneously observed tracks. Metre-based speeds/distances require declared calibration; image-plane results alone should not be presented as physical speeds/distances.

Start with **2D compositing**: top-down ship sprites on sea backgrounds, with consistent appearance across frames, blur/downsampling, simple wakes and documented omissions. A pretrained small detector and a lightweight tracker are shared components; do not train a detector from scratch. Blender/Unity are optional only if a measured failure requires them. Generative AI is unnecessary. A simulated error must be described as injected unless the image pipeline itself actually produces it.

### 4.1 Observation contract: specify the camera before claiming a behaviour

The core setting is a **short optical satellite-video-like burst**, not continuous global surveillance or Sentinel-2 video. Planet documents SkySat video collections of **30-120 seconds**; this supports the burst-duration choice, not the realism of our entire renderer. The proposed pixel scales below are experimental settings, not claims about SkySat video resolution. [Planet documentation](https://docs.planet.com/data/imagery/skysat/)

| Item | Proposed starting specification and required check |
|---|---|
| Physical duration | A 60-second scene initially; extend to at most 120 seconds for the core if compute and event coverage permit. Evaluate shorter observed prefixes. Preserve physical time; do not speed up a long AIS voyage to fit. |
| Source cadence | Inspect original Brest dynamic-message timestamps before selecting events. Record gap distributions and maximum gaps for every retained segment. Interpolated positions are assumed motion, not additional recorded evidence. |
| Source support | Apply task-specific evidence requirements, not a universal six-points/ten-second-gap filter. Require recorded positions to bracket the scene boundaries, with task-specific limits on distance in time to each boundary and internal gaps. Counts alone are insufficient. Record exactly which motion between samples is interpolated. See Section 7 for retention and stationary-target rules. |
| Rendered / observed cadence | Initially one frame per second; test 2- and 5-second frame intervals on matched scenes. A denser render does not increase the AIS source's information content. |
| Spatial sampling and field of view | Start at 2 m/pixel over a fixed 1,024 m square field, giving 512 x 512 pixels. A 1/2/4 m-per-pixel sweep must preserve the same physical field and report changed raster sizes; account for any later detector resizing. Pixel spacing alone is not effective optical resolution: blur and contrast are separate factors. |
| Camera and calibration | A fixed, registered view with known pixel-to-metre mapping first; an explicitly perturbed registration as a stress test. No automatically vessel-centred camera without adding or estimating its motion. Reference camera motion is oracle information unless deliberately supplied as an assumption. |
| Coverage and gaps | Specify maximum visible gap and minimum evidence per task using development data. A vessel leaving the field is a censored observation; retain its impact on end-to-end coverage. Do not move the camera silently to keep it visible. |
| Prediction timing | Primary task: classify the currently observed trailing window. Optional online event detection uses trailing data only, causal filtering and no future-assisted track repair. Whole-clip retrospective classification is reported separately. |

The core must not assume hours of uninterrupted orbital video. Longer continuous simulations may be useful **hypothetical sensor/track stress experiments**, but are outside demonstrated finite-burst applicability. Ordinary Sentinel-2 snapshots, nominally separated by days, cannot supply these short-frame sequences. [Copernicus mission documentation](https://sentiwiki.copernicus.eu/web/s2-mission)

## 5. Proposed individual workload

The following are candidate research packages. Each needs its own hypothesis, method investigation, baseline comparisons, experiments and attributable result. Different labels alone do not establish distinct research contributions.

| Student | Behaviour family and candidate outputs | Research problem | Candidate model investigation | Individual experimental result |
|---|---|---|---|---|
| **A: Individual movement and recoverability** | Transit; deceleration-to-stop; turning. Sustained near-stationary motion is a separate candidate target, conditional on source support. | Which combinations of visible history, pixel scale and observation quality support reliable local-state recognition? Does model access to estimated quality help? | One compact GRU or 1D-CNN with/without observable quality inputs, such as elapsed time, missingness mask and tracker confidence. Give quality variables to a feature baseline too. | Empirical performance/coverage curves and the quality-input ablation versus tuned filtered-track rules. Report selection/retention by behaviour and vessel category. A method-dependent recoverability map, not a universal physical observability limit. |
| **B: Vessel interactions and identity errors** | Closing/separating; co-moving; passing encounters when enough of the event is visible. | Can relative temporal modelling distinguish an observed interaction from chance proximity under fragmentation and identity errors? | Relative-motion rules, a feature classifier and one compact pairwise temporal model. All use identical candidates selected from observed tracks. No graph model in the core. | Candidate-pair recall, end-to-end event recall, false alerts and sensitivity to identity swaps, merged detections and unrelated nearby vessels. |
| **C: Partial pattern recognition** | Repeated direction changes or back-and-forth movement versus an isolated turn/through-transit; a completed loop only if observable within the declared burst. | Does combining two temporal scales improve classification of partial patterns at the same available history and decision time? | A two-scale temporal model versus a single-scale model given the **same maximum history**, with comparable capacity; include a trajectory-shape baseline where applicable. | Accuracy/coverage versus visible prefix length; false repeated-pattern alerts and optional detection delay. Do not assign 30-minute loitering truth to an uninformative 60-second fragment. |

### Boundaries between the contributions

- **A** owns the quality-input comparison and local-state recoverability measurements; constructing a heatmap alone does not replace a model investigation.
- **B** studies relationships between simultaneous tracks; success cannot be assessed from a single vessel alone.
- **C** owns partial-pattern and temporal-scale comparisons within the supported history; an isolated turn must not automatically become a looping/loitering label. Do not manufacture this workload by assuming an unavailable long video feed.
- A vessel may turn while approaching another vessel and also be part of a longer looping pattern. The three outputs therefore need not be mutually exclusive.
- Within each family, specify whether labels are mutually exclusive, hierarchical or multi-label. For example, turning and slowing can happen together; closing and co-moving may also overlap.
- No student should be assigned only rendering, annotation, backend or frontend development. Shared engineering can be allocated fairly, but does not replace individual experiments.

### Individual deliverables

Each student owns a short task specification, one explicit hypothesis, baseline implementations, one bounded model/representation investigation, an experiment matrix, error analysis and an individual results section. The shared final report should identify these contributions through separate comparisons and ablations, without requiring three independent systems or papers.

**C's specific pilot evidence:** Plot original positions with timestamps and candidate labels for representative positives, isolated-turn negatives and ambiguous fragments. Show that each claimed repeated heading change/reversal is supported by successive recorded displacements, not introduced by interpolation. Report distinct vessels, voyages, source manoeuvres and final independent resampling groups per label and partition. Overlapping windows or repeated renders of one manoeuvre do not increase those counts. Retain C only if these distinct within-burst examples support its primary comparison; otherwise narrow/revise C after inspecting the data, without inventing a replacement package in advance.

**Dependency control:** All three begin with the same small coordinate-observation interface while the shared renderer is developed. They do not wait for final rendering assets. Image-derived tracking replaces that interface progressively, keeping the task and test partitions unchanged.

## 6. Labels: operational definitions rather than confirmed activities

Agree on definitions before final model experiments. Do not let easy simulation examples determine overly convenient labels.

| Family | Definition elements to settle | Important ambiguity |
|---|---|---|
| Individual movement | Speed/displacement thresholds; heading-change measure; minimum duration; treatment of transitions. | Near-stationary does not prove anchoring or mooring; small direction changes can be measurement noise. |
| Interactions | Relative distance trend; heading similarity; duration; pair selection; definition of a complete passing event. | Being close is not proof of a meeting, cargo transfer or coordinated intent. |
| Within-burst patterns | Repetition/reversal count, loop closure if relevant, spatial extent and required visible duration. | Curved routes and a single turn can resemble the beginning of a repeated pattern; a long-event definition may be unobservable in a short burst. |

Threshold values are deliberately not fixed here. Select and justify them from the task definition and inspected AIS examples, then freeze them before final testing. Test sensitivity to reasonable alternative definitions.

Labels derived from rules are **weak/operational labels**. Scores against them measure recovery of those definitions under the simulated observation process. They do not independently establish semantic understanding. If rules applied to perfect reference tracks define the labels, their agreement is an oracle sanity check, not a meaningful competitor to outperform.

Separate the movement labels from **abstention** (declining a prediction). Reference annotations should flag incomplete or ambiguous visibility; a learned confidence/quality policy determines whether to answer. Report error versus answered fraction (coverage), including coverage by class. Do not count every abstention as a correct extra movement class. Full-path context must not silently change a short-window target into a forecasting or hidden-activity task.

## 7. Training data and generation plan

| Source | Intended role | Check before relying on it |
|---|---|---|
| **Preferred: original Brest AIS positions**, [Ray et al. dataset](https://zenodo.org/records/1167595) | Recorded paths and simultaneous groups from the same six-month setting as the composite-event study. The record lists a separate AIS archive. | Published availability is established; successful local download/parsing, dynamic-message cadence, cleaning and retained class counts still require a pilot. Inspect `nari_dynamic.csv` rather than relying only on compressed synopses. |
| **Paired candidate: [Composite Maritime Events](https://zenodo.org/records/2557290)** and its [paper](https://arxiv.org/abs/1903.03078) | Existing operational event intervals and definitions to locate relevant Brest track segments. Prefer joining these to the original Brest positions before seeking unrelated sources. | Validate vessel IDs, timestamps/time zones, preprocessing and interval boundaries. Long loitering/rendezvous labels and metadata-dependent definitions are not automatically the proposed short-burst motion labels. Labels are rule-derived, with selected expert checks, not complete independent truth. |
| [US Marine Cadastre AIS](https://marinecadastre.gov/ais/) | Optional broad-track/long-window background source, not the default short-burst manoeuvre source. | The [2025 product documentation](https://catalog.data.gov/dataset/nationwide-automatic-identification-system-2025) says records are filtered to **one-minute frequency**. It cannot establish second-level manoeuvres by interpolation. Audit any other year's processing separately. |
| [Danish Maritime Authority historical AIS](https://www.dma.dk/safety-at-sea/navigational-information/ais-data) | Fallback if usable Brest subsets are inadequate. | Download, terms, actual per-vessel update rates and simultaneous-event support remain untested here. Do not assume uniformly dense records from the existence of an archive. |
| Procedurally constructed trajectories | Controlled stress cases and rare geometries. | Mark them separately from recorded AIS. Report results for each provenance; a procedural-only study would require changing the AIS-driven claim. |

For genuine interactions, preserve vessels that were recorded in the same area at the same time. Artificially pairing unrelated AIS tracks creates a simulated encounter, which must be identified as such. Interpolation fills a computational path, not verified movement through missing intervals; exclude large gaps or test interpolation uncertainty explicitly.

The [Brest dataset paper](https://doi.org/10.1016/j.dib.2019.104141) links the original data and the derived event ecosystem. Thus, the concern is no longer whether an underlying AIS archive exists; it is whether the downloaded subsets satisfy this experiment's timing and class requirements. Use a small region/time subset and record component licences before redistributing derived data.

### Task-specific source support and selection bias

AIS reporting cadence is related to movement. The [US Coast Guard Class A documentation](https://www.navcen.uscg.gov/ais-class-a-reports) describes 2-10 second underway reports and three-minute reports at anchor. These transmission intervals are not guaranteed received intervals in Brest, nor a rule for every AIS device class. They identify a plausible selection mechanism: one dense-data filter could remove stationary examples disproportionately. Whether this happens in Brest must be measured.

- **Transit/turning/deceleration-to-stop:** Require recorded displacements before and after the claimed change, scene-boundary support and a maximum gap appropriate to the transition's duration. Develop the exact limits on inspected development examples, then freeze them; do not use the old dense screen as a universal population definition.
- **Sustained near-stationary:** Assess separately from deceleration-to-stop. Sparse agreeing endpoints do not confirm continuous stationarity within the interval. If recorded evidence cannot support the short-window target, omit/narrow that target or identify constant-position simulations separately as an assumption-based stress set. Do not fill the gap and call it observed confirmation.
- **Interactions:** Both vessels need overlapping, adequately supported observation intervals. Passing/closing labels require recorded evidence for the relevant relative-motion phase, not merely nearby interpolated endpoints.
- **Repeated patterns:** Each claimed reversal/repetition and its temporal ordering must be supported by the original positions within the declared burst. A high total point count cannot compensate for a gap covering the decisive manoeuvre.

For every filter stage and final partition, report candidates, retained/excluded scenes, unique vessels/voyages and exclusion reasons by candidate behaviour and available vessel category/device class, including unknown metadata. Treat pre-filter labels as provisional when cadence is insufficient. Record boundary offsets and internal gaps, not only counts. Offline generation may use bracketing reference points; future AIS points must never enter online classifier features or filtering. No claim of unseen-vessel generalisation extends beyond the retained source-supported population automatically.

Export reference positions, event intervals, frame timestamps, bounding boxes/masks, true IDs, camera parameters and provenance alongside the imagery. Maintain physical time: creating more interpolated frames does not create new independent observations.

**Generation should be shared.** A student may lead a component operationally, but the research workload is the behaviour investigation in Section 5.

## 8. Evaluation without real satellite footage

Use two explicitly distinguished levels:

1. **Controlled track observations:** Corrupt reference positions with declared noise, omissions and fragmentation. This isolates behaviour recognition from visual extraction. It is a simulated track study.
2. **Rendered-image observations:** Run a detector/tracker on rendered frames and classify the resulting observations. This establishes performance through the simulated image pipeline. If this stage is absent, do not describe coordinate-only experiments as demonstrated image-sequence classification.

### Comparisons shared across students

| Baseline / condition | Purpose |
|---|---|
| Rules on perfect reference tracks | Label implementation and upper-information sanity check. |
| Rules on raw tracks, then development-tuned filtered-track rules | Keep reference label definitions frozen, but tune the prediction baseline's smoothing, persistence and decision thresholds on development data. The tuned version is the main rules competitor. |
| Feature-based classifier on observed tracks | Tests whether compact conventional ML is sufficient. |
| Compact temporal model on observed tracks | Tests the benefit of sequence modelling. |
| Matched parametric-noise versus rendered-error training | Same source paths, class mix, training volume, feature access and tuning budget; evaluate both on **the same held-out rendered detector/tracker outputs**. A richer, temporally correlated coordinate-noise baseline tests whether simple jitter is an unfairly weak comparator. |
| Reference tracks versus detector/tracker outputs | Separates classification limitations from visual extraction failures. |

Keep classifier input features comparable when claiming a modelling improvement. If one method receives extra image features or context, report that information difference as a separate comparison.

### What rendering must establish

Measure position-error correlation, size-dependent misses, fragmentation, merged detections and identity switches against simulation reference tracks. Compare their effect on the three behaviour tasks with parametric noise. A simple renderer may not reproduce wakes, occlusion or merge behaviour credibly; include those effects only if implemented and demonstrated.

Rendering can contribute either a useful training distribution **or** a reproducible diagnosis of structured visual-extraction failure. Improved classifier accuracy is not its only valid outcome. Conversely, testing on the same renderer family does not prove superiority for real images. If images add neither useful error structure nor a useful comparison, simplify the project and explicitly reframe its main result as a simulated track-observation study.

### Pair selection, timing and complete denominators

- Select B's candidate pairs using observed tracks, timestamps and a development-set proximity gate; never give the model only reference-selected positive encounters. Include unrelated nearby pairs and scenes with no target event. Report candidate recall separately.
- Match predicted tracks/events to reference objects using one frozen evaluation protocol. Report scores conditional on usable tracks **and** end-to-end recall including entirely missed vessels, missed pairs and lost events. Do not drop tracking failures from denominators.
- Distinguish complete in-field events from censored entrances/exits and incomplete events. Predefine any eligibility exclusions and report their counts and coverage rather than silently removing difficult cases.
- Primary online/prefix results use causal smoothing and trailing windows. No centred filtering, future interpolation across a not-yet-observed gap, or whole-clip track repair may enter an online model. Retrospective repair is a separate experiment.
- Student C's single- and multi-scale models receive identical maximum history at each decision time. A longer input alone is not evidence that the architecture is better.

### Held-out tests and leakage prevention

**Primary generalisation target:** New retained AIS vessel identities, under the declared simulated observation model. Use the following common partition and uncertainty protocol; voyage, scene and vessel are not interchangeable independent units.

1. Before creating windows/renders, define source voyage/manoeuvre IDs and candidate source-scene episodes. Retain original vessel IDs privately for grouping only. Fix one seed and assign each vessel deterministically to train/development/test, initially targeting 70/15/15 by vessel count. Do not search seeds for favourable final class counts or performance.
2. Keep a candidate scene only when **all AIS-sourced vessels rendered in it**, including distractors, belong to the same partition. Exclude cross-partition encounters/scenes rather than duplicating them or moving a vessel into a second partition. Report these exclusions, class/geometry changes and retained counts; this deliberately changes the encounter population and must be disclosed.
3. Every window, overlapping fragment, coordinate corruption and repeated render inherits its source scene's partition. Connected excerpts of the same source episode remain together. A cross-boundary source episode is excluded or trimmed at a documented non-overlapping boundary before sample creation; the same recorded observations cannot enter two partitions.
4. Within each partition, build a **dependency graph** linking retained scenes that share an AIS vessel or overlapping source episode. Its connected components are the common resampling units. Keep all voyages, windows and rendering variants in a component together. For each paired model comparison, resample the same held-out components and recompute the metric; never bootstrap frames or windows independently.
5. Report vessel, voyage, scene and connected-component counts, per-label component support and largest-component fraction. Encounter chains can create very large components. If too few components remain for credible uncertainty estimates or label support, report descriptive results and that limitation; revise the sampling scope or generalisation target during the pilot, document the change, and freeze it before final experiments. Do not substitute scene-level intervals or silently claim vessel independence.

This is one explicit proposed protocol, not a guarantee of enough partitions. It favours a clear claim and measurable exclusions over enforcing conflicting grouping rules implicitly. Reusing simulated assets across splits is a separate appearance-generalisation condition, not a reason to treat repeated renders as independent data.

- Separate recorded-voyage generalisation from renderer generalisation: report performance on unseen paths under familiar rendering and under held-out appearance/observation settings.
- Hold out vessel assets/backgrounds and selected noise, cadence or resolution settings. Random seeds alone do not establish a shifted test.
- Derive labels from reference paths, then generate imperfect observations. Do not recompute test truth from the model's own predicted tracks.
- Avoid label-correlated artefacts: a class must not have its own ship type, colour, background, camera setting or observation duration by construction.
- Tune on development data. Keep final test settings untouched and record all simulation assumptions.

### Metrics and robustness

Report per-class precision/recall, macro-F1, confusion matrices and paired uncertainty intervals using the held-out dependency components specified above. Disclose how scenes/windows are weighted in the point estimate; dense overlap must not be represented as extra independent evidence. For event tasks, add false alerts per scene-hour and onset delay under a frozen event-matching rule; report recall alongside delay so a model cannot appear faster by missing difficult events. Track extraction failures and abstention coverage are separate outcomes. Report memory and runtime on actual hardware rather than promising a GPU budget in advance.

Use a bounded experiment matrix covering sampling interval, observation duration, position noise, missed detections, identity errors, vessel pixel size and camera motion. Use one-factor comparisons and a small number of combined stress cases rather than an exhaustive parameter grid. Include difficult near-threshold cases and competing geometries, not only clean textbook trajectories.

An optional cross-renderer or independently constructed synthetic test would strengthen evidence beyond a single generator. It still would not substitute for real-satellite verification.

### Predeclared decisions and useful null results

Before final testing, each student names one primary comparison, metric and development-justified smallest useful difference. Use a paired 95% interval for the **difference** by resampling the shared held-out dependency components, if their number/support permit credible estimation; do not judge superiority by whether two separate confidence intervals overlap. Prespecify the small primary comparison set; other settings are exploratory.

- **A:** quality-input ablation and local-state performance/coverage under held-out observation errors. Recoverability is measured for tested methods against a prespecified performance target, not asserted as a universal information limit.
- **B:** pairwise-model versus tuned relative-motion baseline, including the missed-pair denominator; examine identity-error sensitivity as the planned diagnostic.
- **C:** two-scale versus equal-history single-scale model, using false alerts at a common recall target or recognition at a common decision time, chosen before testing.
- **Shared:** matched-noise versus rendered-error training and structured error diagnostics on identical rendered tests.

A result below the practical margin, an uncertain result, or a baseline win does not make the project fail. Distinguish these outcomes. A wide interval is inconclusive; to claim practical equivalence the interval must fit within prespecified equivalence bounds. No automatic claim that rules suffice follows merely from a non-significant difference. The project needs reproducible, adequately supported findings, not a guaranteed model victory.

## 9. Prior work and novelty boundaries

The original leads are retained below; three additional reviewer-supplied neighbours were checked against their primary records for this revision. This is a targeted check, not an exhaustive novelty audit. Distinguish movement classification, representation learning, ship-type recognition and operational event definitions.

| Study / link | Input or generated data | Established task and implication |
|---|---|---|
| [Chen et al. (2020)](https://doi.org/10.1016/j.oceaneng.2020.108182) | AIS trajectories | Static, normal navigation and manoeuvring classification. Individual movement classification already exists. |
| [Zhang et al. (2022)](https://doi.org/10.1016/j.oceaneng.2022.111852) | AIS trajectories | Loitering detection and trajectory-shape classification. Direct neighbour for Student C. |
| [CNN-Lite (2025)](https://www.mdpi.com/2077-1312/13/12/2327) | AIS trajectory images | Mooring, anchoring and sailing. A trajectory drawing is not a rendered satellite scene. |
| [Pitsikalis et al. (2019)](https://arxiv.org/abs/1903.03078) | AIS plus spatial context/metadata | Rule-based maritime event recognition, including rendezvous and loitering. Important label and rule baseline precedent. |
| [Cope et al. (2022)](https://doi.org/10.1371/journal.pone.0269490) | Coastal radar tracks | Focal/linear movement patterns using rules. Non-AIS visual/sensor track behaviour is not a new general concept. |
| [Grasso (2019)](https://www.eurasip.org/Proceedings/Eusipco/eusipco2019/Proceedings/papers/1570532157.pdf) | Sentinel-2 imagery; AIS labels | Snapshot speed and course classification. Satellite movement-related outputs already exist in narrower forms. |
| [Ballinger (2024 preprint)](https://arxiv.org/abs/2404.07607) | PlanetScope imagery and AIS cross-reference | Ship-to-ship configurations in snapshots. Related to interaction detection, with different temporal evidence. |
| [UnityShip (2021)](https://www.mdpi.com/2072-4292/13/24/4999) | Synthetic aerial ship still images | Synthetic overhead vessel imagery is established. Rendering ships alone is insufficient novelty. |
| [MarSyn (2022)](https://www.mdpi.com/1424-8220/22/21/8090) | Blender-generated UAV-style maritime video | Synthetic maritime sequences and automatic annotations already exist. |
| [RedNavi (2022)](https://www.mdpi.com/2071-1050/14/19/12572) | AIS-driven 3D maritime scenes | AIS-to-scene visualisation already exists. |
| [MP2Net (2024)](https://github.com/DonDominic/MP2Net) | Optical satellite video | Detection/tracking precedent and possible reusable component; tracking is distinct from behaviour classification. |
| [Mayra et al. (2025)](https://doi.org/10.1016/j.rse.2025.114791) | Sentinel-2 optical images | Small/recreational vessel detection is established. This project should not claim novelty simply from finding small boats. |
| [Al-Falouji et al. (2026)](https://www.mdpi.com/2077-1312/14/5/507) | AIS trajectory representations | Robust/uncertainty-aware representation baselines and behavioural clustering; vessel type is an encoder-selection probe. Narrows broad robustness claims, but is not the same finite-burst image-derived movement test. |
| [Guo et al. (2026)](https://doi.org/10.1016/j.oceaneng.2026.125198) | Compressed AIS trajectories | Encounter identification with information-degradation and reliability analysis. Student B must distinguish visual identity/candidate-pair failures from compression alone. |
| [Xu et al. (2024)](https://zghh.cinnet.cn/en/article/doi/10.3969/j.issn.1000-4653.2024.02.001) | AIS wandering trajectories | Douglas-Peucker extraction and four trajectory-shape classes with ResNet50. Student C must test partial visibility and equal-history temporal comparisons, rather than claim a new wandering category task. |

**Candidate contribution:** A controlled, reproducible investigation of recovering several behaviour families under a finite-burst observation contract, isolating quality inputs (A), observed-pair/identity failures (B), and partial-pattern temporal modelling at equal history (C), plus measured visual-extraction error effects shared by all three.

**Not yet demonstrated:** That these exact investigations are sufficiently distinct from published sparse/irregular-trajectory classification, compression-aware event recognition and synthetic visual behaviour studies. A focused nearest-neighbour comparison remains an early task. Removing real verification removes synthetic-to-real improvement as an initial contribution. A new behaviour list, renderer or combination of standard components does not automatically replace it; neither reviewer opinion nor the existence of workload establishes publishability or supervisor acceptance of every package.

## 10. Claims permitted by the starting scope

| Evidence obtained | Defensible statement | Stronger statement not established |
|---|---|---|
| Held-out synthetic-track results | Recognises specified movement definitions under the tested coordinate observation models. | Recognises behaviour from real satellite imagery. |
| Held-out rendered-image results | Recognises those definitions through the tested simulated image and tracking pipeline. | The renderer faithfully represents all real satellite conditions. |
| No AIS in classifier input | Predictions can run without receiving AIS in the simulated setting. | Proven generalisation to real AIS-silent vessels. |
| Recorded AIS drives the renderer | Training paths include recorded motion, subject to cleaning/interpolation assumptions. | Synthetic images are real observations or independently verified activity. |

Until physically small-vessel cases are explicitly represented and evaluated, use **vessels** rather than claiming a validated small-boat system. Pixel-small targets and physically small boats are different properties. Observed close movement or looping does not establish fishing, transfer, intention or illegality.

## 11. Feasibility and staged work

Design for occasional access to one modest GPU: bounded crops, cached detections/features, CPU rules/tree baselines and compact sequence models. A new foundation model, diffusion video generator, high-fidelity SAR simulator or large end-to-end video transformer is outside the starting scope.

| Suggested stage | Shared milestone | Individual progress |
|---|---|---|
| First 2-3 weeks | Download a bounded Brest subset and candidate event intervals; test IDs/times and cadence; settle the observation contract; prototype 2D rendering and baseline extraction. | Each student reports supported examples and independent split counts, one primary comparison and ambiguous/unsupported cases. |
| Months 1-2 | Reproducible small dataset and common observation pipeline. | Task specifications, conventional baselines and first model comparison. |
| Months 3-4 | Stable dataset version and experiment infrastructure. | Main model/representation investigations and bounded robustness studies. |
| Months 5-6 | Frozen final synthetic tests and integrated prototype. | Held-out evaluation, uncertainty estimates, failure analysis and writing. |
| Months 7-8, if available | Replication and consolidation; optional real-data pilot. | Resolve weaknesses before adding scope. |

This is a planning estimate, not a measured effort guarantee. Use one source/region, one renderer, one detector/tracker and one compact model family; C uses two temporal scales. Vary one factor at a time plus at most three planned combined stress cases initially. Cache tracks and render large runs only after measuring pilot time/storage. MP2Net is a precedent, not a required dependency; benchmark installation and inference before committing to its software stack.

The early gates are: **data** (post-cleaning class and independent-group counts, not assumptions that events are plentiful); **observations** (the retained task can be supported at the stated duration/resolution); **compute** (measured generation, extraction, training and storage fit available resources); and **research** (a specific neighbour comparison and primary experiment per student). If C lacks repeated patterns within the finite burst, narrow/revise C before full implementation; do not retain an hour-long label solely to fill a third role. Lack of real footage alone does not block the approved simulation-first scope.

**Minimum shared deliverables:** documented dataset/generator; three task specifications; reproducible baselines and models; frozen synthetic test suite; separate individual findings; integrated demonstration and an honest limitations statement.

If real verification later becomes possible, audit [SAT-MTB](https://csu.cas.cn/gb/kybm/sjlyzx/gcxx_sjj/sjj_wxxl/202211/t20221121_6551405.html) and [OOTB](https://github.com/YZCU/OOTB) for actual ship-event coverage, durations, metadata and labels. Their tracking annotations do not automatically provide the proposed behaviour labels. Keep any real development and final evaluation clips separate.

**Optional calibration before behaviour verification:** A tracker run on accessible real clips could estimate observation-error distributions without behaviour labels. Measuring localisation error, misses or ID switches still needs suitable reference tracking annotations, alignment and metadata; predictions alone do not reveal their true error. This is optional because access, reference quality and engineering cost are unproven. Any clips used to set simulator parameters become development/calibration data, not an untouched later verification set.

## 12. Questions for the reviewing agent

Please assess the revised **simulation-first** scope rather than rejecting it solely because real verification is initially unavailable. Equally, do not assume supervisor support establishes novelty or validates the simulator.

1. **Three-person research depth:** Are A, B and C independently substantial and connected? Identify overlap, dependencies and where a package is merely engineering or standard classification.
2. **Novelty under simulation-only evaluation:** What are the closest published neighbours for each package? Provide verifiable links and explain exactly what the proposed experiments add. Separate confirmed precedent from speculative gaps.
3. **Scientific validity:** Does the plan only learn its own labelling rules? Which comparisons would demonstrate useful robustness under observation errors without overstating semantic activity recognition?
4. **Input and label consistency:** Does the proposed observation contract match the retained classes, and can the inspected source cadence support it? Are calibration, causal timing, multi-label outputs and visibility assumptions sufficient?
5. **Value of rendering:** Could the central questions be answered equally well using noisy AIS coordinates? If so, recommend either a measurable visual contribution or an honest narrower framing.
6. **Data feasibility:** Can accessible AIS support all three families, especially simultaneous encounters and extended patterns, without unavailable expert annotation or primary collection?
7. **Compute and learning curve:** Which experiments should be removed or simplified for three students with introductory ML experience and intermittent GPU access?
8. **Revisions:** Recommend a minimal coherent scope, an improved contribution table, strongest necessary baselines and explicit success/failure criteria. Explain changes rather than adding complexity by default.

Do not invent access, class counts, published results, satellite fidelity or performance targets. Distinguish evidence-backed findings, design recommendations and unresolved questions. If the three contributions are insufficient, say so and identify the smallest defensible redesign.

## 13. Related workspace material

- [Research module and team criteria](../../../research-module-and-team-criteria.md): governing team/resource context; the user waived the avoid-crime preference for this project.
- [Earlier X48 literature and feasibility report](x48-satellite-vessel-behaviour-from-synthetic-sequences.md): useful background and references, with an older real-evaluation-first decision gate.
- [Four-page beginner project PDF](../../../output/pdf/satellite_vessel_behaviour_project_brief.pdf): introductory explanation and study tables; created before the revised simulation-first workload decision.
- [Review response and revision decisions](x48-review-response-and-revision-log.md): reasoning for accepting, modifying or declining the two reviews' suggestions.

**Current assessment:** Simulation-first remains the approved starting direction. This revision makes the three investigations more attributable and their evaluation more testable, but does not certify novelty or dataset adequacy. The immediate priority is a bounded Brest data/observation pilot and a precise nearest-neighbour comparison, followed by the simplest experiments capable of answering each student's question.
