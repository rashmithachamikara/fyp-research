# X48: Simulation-first vessel movement behaviour recognition

**Purpose:** Self-contained handoff for another agent to review and improve the project scope, research contribution, workload distribution and evaluation.

**Updated:** 10 November 2026  
**Stage:** Proposed research design; no implementation results are claimed.  
**Supervisor direction, as reported by the team:** Start with simulation only; move to real-satellite verification later if possible.

> **Scope precedence:** This document records the latest direction. Earlier X48 notes and the four-page PDF treated real-footage evaluation as an initial go/no-go requirement. That requirement is superseded for the approved simulation-first starting scope. Real-data access is now an optional extension, while accessible simulation inputs and a defensible synthetic evaluation remain essential.

## 1. Project in plain language

AIS (Automatic Identification System) broadcasts vessel positions and movement information. The project would use recorded AIS paths to create computer-rendered optical satellite-style image sequences. Models would learn to recognise observable vessel movement from those images or from tracks extracted from them.

At prediction time, the intended input is an image sequence, with timestamps and any explicitly assumed camera calibration. The vessel's AIS messages are not supplied to the classifier. The simulator retains reference positions and labels separately for evaluation.

Three students would investigate different behaviour families using one shared simulator and experimental pipeline:

1. Short-window movement of an individual vessel.
2. Relative movement and interactions between vessels.
3. Longer-duration movement patterns of an individual vessel.

The intended application is eventually screening vessels visible in satellite imagery, including vessels without a reliable AIS match. Simulation alone cannot establish accuracy on real AIS-silent vessels, actual intent or illegal activity.

## 2. Approved direction versus design choices

| Status | Item |
|---|---|
| Confirmed by the user | The supervisor supports starting with simulation and attempting real verification later if possible. |
| Confirmed project context | Three students; one coherent research project; substantial individual contributions; existing datasets; limited/occasional GPU access; approximately 6-8 months of implementation within one year. |
| Proposed here | Shared data generation and infrastructure, with research responsibilities divided by behaviour family. |
| Still to establish | Accessible AIS source, precise class definitions, simulation fidelity, usable observation durations, model choices, experimental budget and novelty of each investigation. |
| Optional extension | Verification on real satellite footage, with separate labels and a suitable held-out test. |

The team's earlier preference to avoid crime-related topics was explicitly waived for this project. The proposed prediction targets nevertheless remain observable movement rather than illegality.

## 3. Objective and research question

**Working objective:** Develop and evaluate vessel movement behaviour classifiers using AIS-driven synthetic optical satellite image sequences under varied observation conditions.

**Working research question:** Under specified simulated observation conditions, can compact learned models recognise individual, pairwise and longer-duration vessel movement patterns more reliably than rules applied to the same imperfect observed tracks?

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

Conventional compositing, Blender or Unity can generate sequences; generative AI is unnecessary. Start with manageable crops, consistent ship appearance through each sequence, realistic time intervals, declared ground sampling distance, and bounded appearance variation. More realistic rendering is justified only by a testable question.

## 5. Proposed individual workload

The following are candidate research packages. Each needs its own hypothesis, method investigation, baseline comparisons, experiments and attributable result. Different labels alone do not establish distinct research contributions.

| Student | Behaviour family and candidate outputs | Research problem | Candidate model investigation | Individual experimental result |
|---|---|---|---|---|
| **A: Individual movement** | Transit; slowing/stopping; turning. | Short-window movement can be obscured by position noise, missed observations and uncertain velocity estimates. | Compare kinematic features and a compact temporal model; investigate whether accounting for observation quality improves robustness. | Performance versus sampling interval, noise, missing detections and window length; comparison with raw/smoothed-track rules and a feature classifier. |
| **B: Vessel interactions** | Closing/approaching; separating; co-moving; passing encounters. | Nearby vessels may pass briefly or move independently; proximity alone does not establish a sustained interaction. | Compare distance/speed rules with a compact model using relative positions and velocities over time. Pairwise models come before optional graph models. | Interaction recognition under chance proximity, different encounter geometries, track gaps and identity switches; comparison with rule and feature baselines. |
| **C: Longer movement patterns** | Localised looping; repeated back-and-forth movement; through-transit. | A short fragment of a longer pattern may look like a normal turn or straight transit. | Compare a fixed-window model with a model combining several observation-window lengths or a hierarchical temporal representation. | Pattern recognition versus observation duration, partial visibility, path scale, missing segments and movement speed; detection delay and false alerts. |

### Boundaries between the contributions

- **A** studies local motion state and state transitions, not the overall purpose or shape of an extended voyage.
- **B** studies relationships between simultaneous tracks; success cannot be assessed from a single vessel alone.
- **C** studies extended temporal structure; an isolated turn must not automatically become a looping/loitering label.
- A vessel may turn while approaching another vessel and also be part of a longer looping pattern. The three outputs therefore need not be mutually exclusive.
- Within each family, specify whether labels are mutually exclusive, hierarchical or multi-label. For example, turning and slowing can happen together; closing and co-moving may also overlap.
- No student should be assigned only rendering, annotation, backend or frontend development. Shared engineering can be allocated fairly, but does not replace individual experiments.

### Individual deliverables

Each student owns a short task specification, one explicit hypothesis, baseline implementations, one bounded model/representation investigation, an experiment matrix, error analysis and an individual results section. The shared final report should identify these contributions through separate comparisons and ablations, without requiring three independent systems or papers.

## 6. Labels: operational definitions rather than confirmed activities

Agree on definitions before final model experiments. Do not let easy simulation examples determine overly convenient labels.

| Family | Definition elements to settle | Important ambiguity |
|---|---|---|
| Individual movement | Speed/displacement thresholds; heading-change measure; minimum duration; treatment of transitions. | Near-stationary does not prove anchoring or mooring; small direction changes can be measurement noise. |
| Interactions | Relative distance trend; heading similarity; duration; pair selection; definition of a complete passing event. | Being close is not proof of a meeting, cargo transfer or coordinated intent. |
| Longer patterns | Localisation, repeated direction changes, loop structure, spatial extent and required observation duration. | Curved routes, channel geometry and a short manoeuvre can resemble loitering. |

Threshold values are deliberately not fixed here. Select and justify them from the task definition and inspected AIS examples, then freeze them before final testing. Test sensitivity to reasonable alternative definitions.

Labels derived from rules are **weak/operational labels**. Scores against them measure recovery of those definitions under the simulated observation process. They do not independently establish semantic understanding. If rules applied to perfect reference tracks define the labels, their agreement is an oracle sanity check, not a meaningful competitor to outperform.

Use an **unknown/insufficient evidence** outcome for cases where the observation window or track quality cannot support a label. Reference labels may be known from the full simulator path even when a short visible fragment is ambiguous; analyse these cases separately instead of demanding confident predictions.

## 7. Training data and generation plan

| Source | Intended role | Check before relying on it |
|---|---|---|
| [US Marine Cadastre AIS](https://marinecadastre.gov/ais/) or another accessible historical AIS archive | Recorded single-vessel paths and simultaneous vessel groups. | Actual download access, licence, timestamps, cleaning burden and coverage of the proposed behaviours. |
| [Composite Maritime Events](https://zenodo.org/records/2557290) and its [event-recognition paper](https://arxiv.org/abs/1903.03078) | Existing event definitions and possible weakly labelled examples. | Event records are not automatically raw trajectories. Confirm underlying position access and vessel/time alignment; do not assume all proposed classes are supplied. |
| Procedurally constructed trajectories | Controlled stress cases and rare geometries. | Mark them separately from recorded AIS. Report results for each provenance; a procedural-only study would require changing the AIS-driven claim. |

For genuine interactions, preserve vessels that were recorded in the same area at the same time. Artificially pairing unrelated AIS tracks creates a simulated encounter, which must be identified as such. Interpolation fills a computational path, not verified movement through missing intervals; exclude large gaps or test interpolation uncertainty explicitly.

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
| The same rules on raw and smoothed observed tracks | Strong, fair conventional baseline under the model's actual information conditions. |
| Feature-based classifier on observed tracks | Tests whether compact conventional ML is sufficient. |
| Compact temporal model on observed tracks | Tests the benefit of sequence modelling. |
| Noisy-coordinate training versus rendered-image-derived training | Tests whether image generation and its resulting observation errors add value. |
| Reference tracks versus detector/tracker outputs | Separates classification limitations from visual extraction failures. |

Keep classifier input features comparable when claiming a modelling improvement. If one method receives extra image features or context, report that information difference as a separate comparison.

### Held-out tests and leakage prevention

- Split by source voyage/vessel and relevant time groups **before** window extraction and rendering. Assign interacting groups together.
- Keep overlapping windows, altered renders of the same path and fragments of the same source recording in one partition.
- Separate recorded-voyage generalisation from renderer generalisation: report performance on unseen paths under familiar rendering and under held-out appearance/observation settings.
- Hold out vessel assets/backgrounds and selected noise, cadence or resolution settings. Random seeds alone do not establish a shifted test.
- Derive labels from reference paths, then generate imperfect observations. Do not recompute test truth from the model's own predicted tracks.
- Avoid label-correlated artefacts: a class must not have its own ship type, colour, background, camera setting or observation duration by construction.
- Tune on development data. Keep final test settings untouched and record all simulation assumptions.

### Metrics and robustness

Report per-class precision/recall, macro-F1, confusion matrices and uncertainty intervals grouped by independent voyage/scene. For event tasks, add false alerts and detection delay with a declared time unit and event-matching rule. Measure tracking failures separately. Report memory and runtime on actual hardware rather than promising a GPU budget in advance.

Use a bounded experiment matrix covering sampling interval, observation duration, position noise, missed detections, identity errors, vessel pixel size and camera motion. Use one-factor comparisons and a small number of combined stress cases rather than an exhaustive parameter grid. Include difficult near-threshold cases and competing geometries, not only clean textbook trajectories.

An optional cross-renderer or independently constructed synthetic test would strengthen evidence beyond a single generator. It still would not substitute for real-satellite verification.

## 9. Prior work and novelty boundaries

These are leads already discussed in the project, not a fresh exhaustive literature audit for this document. A reviewing agent should verify the closest matches and distinguish movement classification from ship-type recognition.

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

**Candidate contribution:** A controlled, reproducible investigation of recovering several behaviour families under specified simulated satellite observation constraints, with fair rules/ML baselines and attributable robustness/temporal-modelling results.

**Not yet demonstrated:** That this is novel enough compared with existing noisy-trajectory classification, maritime simulation and synthetic visual behaviour research. Removing real verification also removes synthetic-to-real improvement as an initial contribution. A new behaviour list, renderer or combination of standard components does not automatically replace it.

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
| First 2-3 weeks | Access AIS; inspect examples; settle label and split formats; prototype a small generator and baseline. | Each student demonstrates at least one supported behaviour contrast and identifies ambiguous cases. |
| Months 1-2 | Reproducible small dataset and common observation pipeline. | Task specifications, conventional baselines and first model comparison. |
| Months 3-4 | Stable dataset version and experiment infrastructure. | Main model/representation investigations and bounded robustness studies. |
| Months 5-6 | Frozen final synthetic tests and integrated prototype. | Held-out evaluation, uncertainty estimates, failure analysis and writing. |
| Months 7-8, if available | Replication and consolidation; optional real-data pilot. | Resolve weaknesses before adding scope. |

This is a planning estimate, not a measured effort guarantee. The early gate now concerns AIS access, behaviour coverage, simulator/observation validity, compute and a viable research comparison. Lack of real footage alone does not block the supervisor-approved starting scope.

**Minimum shared deliverables:** documented dataset/generator; three task specifications; reproducible baselines and models; frozen synthetic test suite; separate individual findings; integrated demonstration and an honest limitations statement.

If real verification later becomes possible, audit [SAT-MTB](https://csu.cas.cn/gb/kybm/sjlyzx/gcxx_sjj/sjj_wxxl/202211/t20221121_6551405.html) and [OOTB](https://github.com/YZCU/OOTB) for actual ship-event coverage, durations, metadata and labels. Their tracking annotations do not automatically provide the proposed behaviour labels. Keep any real development and final evaluation clips separate.

## 12. Questions for the reviewing agent

Please assess the revised **simulation-first** scope rather than rejecting it solely because real verification is initially unavailable. Equally, do not assume supervisor support establishes novelty or validates the simulator.

1. **Three-person research depth:** Are A, B and C independently substantial and connected? Identify overlap, dependencies and where a package is merely engineering or standard classification.
2. **Novelty under simulation-only evaluation:** What are the closest published neighbours for each package? Provide verifiable links and explain exactly what the proposed experiments add. Separate confirmed precedent from speculative gaps.
3. **Scientific validity:** Does the plan only learn its own labelling rules? Which comparisons would demonstrate useful robustness under observation errors without overstating semantic activity recognition?
4. **Input and label consistency:** Are time scales, physical coordinates, calibration, multi-label outputs and visibility assumptions explicit enough? Are the proposed classes observable under the tested settings?
5. **Value of rendering:** Could the central questions be answered equally well using noisy AIS coordinates? If so, recommend either a measurable visual contribution or an honest narrower framing.
6. **Data feasibility:** Can accessible AIS support all three families, especially simultaneous encounters and extended patterns, without unavailable expert annotation or primary collection?
7. **Compute and learning curve:** Which experiments should be removed or simplified for three students with introductory ML experience and intermittent GPU access?
8. **Revisions:** Recommend a minimal coherent scope, an improved contribution table, strongest necessary baselines and explicit success/failure criteria. Explain changes rather than adding complexity by default.

Do not invent access, class counts, published results, satellite fidelity or performance targets. Distinguish evidence-backed findings, design recommendations and unresolved questions. If the three contributions are insufficient, say so and identify the smallest defensible redesign.

## 13. Related workspace material

- [Research module and team criteria](../../../research-module-and-team-criteria.md): governing team/resource context; the user waived the avoid-crime preference for this project.
- [Earlier X48 literature and feasibility report](x48-satellite-vessel-behaviour-from-synthetic-sequences.md): useful background and references, with an older real-evaluation-first decision gate.
- [Four-page beginner project PDF](../../../output/pdf/satellite_vessel_behaviour_project_brief.pdf): introductory explanation and study tables; created before the revised simulation-first workload decision.

**Current assessment:** There is a plausible three-student workload, but adequacy of the research contribution remains to be established. The next review should strengthen each behaviour investigation and the synthetic evaluation, not treat shared generation effort as proof of novelty.
