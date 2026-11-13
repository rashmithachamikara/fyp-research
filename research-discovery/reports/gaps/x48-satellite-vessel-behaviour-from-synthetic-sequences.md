[← Research candidates](../research-candidates.md)

# Vessel Movement Behaviour Recognition Using AIS-Driven Synthetic Optical Satellite Image Sequences

**ID:** X48 · **Area:** Simulated optical satellite sequences, vessel behaviour recognition, compact temporal ML · **Status:** Ready for a bounded feasibility pilot; three-person research scope remains conditional on data and contribution depth.

**Updated:** 10 November 2026, incorporating the simulation-first decision and review revisions 1-3. Original literature checks were recorded on 4 November; later targeted checks are identified in the [review decision log](x48-review-response-and-revision-log.md). This is a research plan, not an implemented result or exhaustive novelty audit.

> **Current scope:** The supervisor supports starting with simulation only and attempting real-satellite verification later if possible. Real footage is therefore an optional extension, not an initial go/no-go requirement. The [detailed workload and protocol brief, revision 3](x48-simulation-first-workload-and-review-brief.md) supplies the full experimental specification. This report preserves the broader literature/dataset context while reflecting the same current direction.

## 1. What the project would do

AIS (Automatic Identification System) provides recorded vessel positions and movement information. The project uses those paths to generate **synthetic optical satellite-style image sequences**, then trains models to recognise observable movement from the images or tracks extracted from them. The intended classifier inputs exclude the vessel's AIS messages; the simulator keeps reference positions and labels separately for evaluation.

Three connected behaviour families divide the research: **A**, individual movement such as transit, turning and deceleration-to-stop; **B**, pairwise movement such as closing, separating, co-moving and passing; **C**, repeated movement patterns distinguishable from isolated turns within a supported observation burst. Sustained near-stationary motion and completed loops remain conditional on adequate source evidence. Zone crossing is a possible extension rather than a core research package.

The core chain is: **recorded AIS → source-supported operational labels → timestamped synthetic optical frames → detector/tracker → behaviour models → held-out synthetic evaluation**. Real-video verification may be added later. Correctly spaced frames can suffice; smooth cinematic video is unnecessary. A 2D renderer is the starting choice, and generative AI is not required. A rendered sequence is an assumed observation of the reference path, not a new real observation between AIS samples.

The target is observable movement, not actual intent, fishing gear use, cargo transfer or illegality. “Approach” is measurable relative motion; “transfer” needs independent evidence. The initial results concern simulated observations of recorded or explicitly procedural paths. Generalisation to real imagery or genuinely AIS-silent vessels remains unverified until a suitable independent evaluation is added.

## 2. Research question and contribution to establish

**Working objective:** Develop and evaluate vessel movement behaviour classifiers using AIS-driven synthetic optical satellite image sequences under varied observation conditions.

**Question:** Under a declared finite-burst simulated observation model, when do quality-aware, pairwise and multi-scale temporal models improve recovery of operational movement patterns over tuned rules and feature models given the same observations?

**Candidate contribution:** A reproducible investigation of local-state recoverability and observation-quality inputs (A), interaction recognition under pair-selection and identity errors (B), and partial-pattern recognition at equal available history (C). A shared comparison tests whether rendered-image extraction creates useful error structure beyond parametric coordinate noise.

**Novelty remains conditional.** AIS classification, sparse/compressed-track event recognition, synthetic maritime imagery and satellite snapshot activities already exist. Different behaviour lists, another renderer or generic robustness experiments alone are insufficient. Removing mandatory real verification also removes synthetic-to-real improvement as an initial contribution; a potential gap in a full real-transfer pipeline cannot be claimed as a completed simulation-only contribution. Each student needs a precise comparison with the closest studies and a specific attributable finding. A well-supported baseline win or null result may still be useful.

## 3. Prior studies: what is already done

| Study | Actual result/task | Relation to this proposal |
|---|---|---|
| [Li et al., SAT-MTB, *IEEE TGRS* (2023)](https://csu.cas.cn/gb/kybm/sjlyzx/gcxx_sjj/sjj_wxxl/202211/t20221121_6551405.html) | Public satellite-video benchmark: 249 videos, more than 50,000 frames, aircraft/ship/vehicle/train categories, framewise boxes/masks for detection, tracking and segmentation. | Real video **exists**, including ships. The stated annotations are not turning, loitering or approach labels; ship-only sequence count, length and event coverage need auditing. |
| [SVSDet, *IEEE JSTARS* (2024)](https://doi.org/10.1109/JSTARS.2024.3359252) | Fine-grained **ship type** recognition in satellite video, evaluated on SAT-MTB and ShipRSImageNet. | Proves a video-based vessel category task, not motion behaviour. A yacht/speedboat label is not an approach/turn label. |
| [MP2Net, *IEEE TGRS* (2024), official code](https://github.com/DonDominic/MP2Net) | Detects and tracks moving objects in satellite video, including ship experiments on SAT-MTB. | Reusable tracking precedent and possible baseline. Tracking identity across frames is a necessary input to movement classification, not the final behaviour output. |
| [Chen et al., OOTB, *ISPRS JPRS* (2024)](https://github.com/YZCU/OOTB) | 110 satellite-video tracking sequences / 29,890 frames including ships, manually annotated oriented boxes and tracking attributes. | Another real ship-video source. Tracking challenge labels are **not** verified maritime activities. |
| [Pitsikalis et al., composite maritime event recognition, DEBS (2019)](https://arxiv.org/abs/1903.03078) · [dataset](https://zenodo.org/records/2557290) | Produces many rule-recognised events on AIS signals (for example, loitering and proximity-related events). | Can supply weak event definitions/labels for trajectories; cannot serve as independent truth that a synthetic-image model recognizes real-world activities. |
| [He et al., UnityShip, *Remote Sensing* (2021)](https://www.mdpi.com/2072-4292/13/24/4999) | Large synthetic overhead ship-image dataset for ship recognition. | Establishes synthetic overhead vessel imagery. Does not test temporal movement events learned from AIS-driven sequences. |
| [Ribeiro et al., MarSyn, *Sensors* (2022)](https://www.mdpi.com/1424-8220/22/21/8090) | Blender-generated maritime surveillance video for instance segmentation, evaluated alongside aerial footage. | Establishes that synthetic **maritime video** can be useful, but the viewpoint is UAV and the target is segmentation, not orbital movement classification. |
| [Liu & Wakabayashi, RedNavi, *Sustainability* (2022)](https://www.mdpi.com/2071-1050/14/19/12572) | Builds 3D sea scenes using incoming AIS for navigation/visualisation. | Demonstrates AIS→scene rendering, but not training or real-satellite-video behaviour recognition. |
| [SatSAM2 / MVOT, preprint (2025–26)](https://arxiv.org/abs/2511.18264) | Creates 1,500+ synthetic satellite-video sequences and studies object tracking. | Synthetic satellite-like video is established outside this exact maritime behaviour question. Public availability and suitability of the announced dataset should be checked before dependence. |
| [Ballinger, ship-to-ship activity from PlanetScope imagery (2024)](https://arxiv.org/abs/2404.07607) | Uses optical satellite **snapshots** and AIS cross-reference to detect ship-to-ship configurations. | Strong adjacent event-recognition precedent. It studies spatial arrangements in images, not a temporal motion classifier from continuous ship video; event labels also have AIS-derived limits. |
| [Grasso et al., Sentinel-2/AIS ship classification (2019)](https://www.eurasip.org/Proceedings/Eusipco/eusipco2019/Proceedings/papers/1570532157.pdf) | AIS-associated Sentinel-2 crops support image classification including a speed-related target. | A single-image motion-state precedent. This narrows any claim that “satellite imagery has never classified behaviour,” but does not solve time-sequence turn/approach/loitering. |
| [Snapir et al., fisheries classification from Sentinel-1 SAR detections, *Remote Sensing* (2019)](https://www.mdpi.com/2072-4292/11/3/353) | Trains a random forest on AIS-derived position, estimated vessel length, distance to shore and time to identify **fishing-vessel type**, then applies it to SAR detections. Reports 58% precision for the fishing class on AIS evaluation and compares satellite count trends with AIS-derived maps. | A real AIS→satellite-detector transfer precedent, but **not image-sequence behaviour recognition** and not evidence that an individual detected vessel is actively fishing. |
| [Fridman et al., *Satellite Detection of Moving Vessels in Marine Environments*, AAAI (2019)](https://ojs.aaai.org/index.php/AAAI/article/view/4998) | Predicts vessel movement from AIS to choose future satellite observation windows. | Satellite/AIS movement prediction exists. Its predictive input is AIS, and the question is where/when to observe, not image-only recognition of an observed vessel's movement class. |
| [SatRMOT project and dataset](https://satrmot.github.io/) | Reannotates satellite-video tracking datasets with natural-language references involving motion direction/status, position and context; reports 523 videos and a ship-category expression subset. | A closer **motion-description** precedent than tracking alone. Its expressions are for referring to tracked objects, not the proposed operational maritime event classes. Audit ship expressions and source-video overlap before claiming a distinct benchmark. |
| [Chen et al., AIS movement classification, *Ocean Engineering* (2020)](https://doi.org/10.1016/j.oceaneng.2020.108182) | CNN classification of static, normal navigation and manoeuvring from AIS trajectories. | Direct neighbour for A; individual movement classification itself is established. |
| [Zhang et al., loitering detection and classification, *Ocean Engineering* (2022)](https://doi.org/10.1016/j.oceaneng.2022.111852) | Loitering detection and four trajectory-shape classes from AIS. | Direct neighbour for C; the proposed difference must concern supported partial observations and equal-history comparisons. |
| [CNN-Lite, *JMSE* (2025)](https://www.mdpi.com/2077-1312/13/12/2327) | Mooring, anchoring and sailing classification using AIS trajectory images. | A drawing of a trajectory differs from a rendered satellite scene, but the behaviour-learning task is an established precedent. |
| [Al-Falouji et al., robust trajectory representations, *JMSE* (2026)](https://www.mdpi.com/2077-1312/14/5/507) | Robust/uncertainty-aware representation baselines and behavioural clustering; vessel type is an encoder-selection probe. | Narrows broad robustness claims without establishing duplication of the finite-burst image-derived task. |
| [Guo et al., encounters from compressed trajectories, *Ocean Engineering* (2026)](https://doi.org/10.1016/j.oceaneng.2026.125198) | Encounter identification with information-degradation and reliability analysis. | B must distinguish visual tracking/identity and candidate-pair failures from compression alone. |
| [Xu et al., wandering trajectory extraction/classification (2024)](https://zghh.cinnet.cn/en/article/doi/10.3969/j.issn.1000-4653.2024.02.001) | Douglas-Peucker extraction and four wandering shapes classified using ResNet50. | C needs a partial-visibility/model comparison beyond relabelling trajectory shapes. |
| [Mayra et al., recreational vessel detection, *Remote Sensing of Environment* (2025)](https://doi.org/10.1016/j.rse.2025.114791) | Sentinel-2 small/recreational vessel detection; 8,768 annotations; reported test F1 0.863. | Small-boat detection in free optical imagery is established. Boxes can include wakes; the result is not a universal vessel-size guarantee. |

Recent AIS-labelled [Sentinel-2 ship-type classification](https://www.sciencedirect.com/science/article/pii/S0029801826025382) reinforces that using AIS to label optical images is established. The initial claim should concern measured recovery of behaviour under declared simulated observations. Real-image transfer requires separate evidence if pursued later. The sources are a starting set, not proof that no exact predecessor exists.

## 4. Candidate datasets: core simulation inputs and optional real verification

| Dataset | What it contains / best role | Missing piece or caveat |
|---|---|---|
| **Preferred: [original Brest AIS release, Ray et al.](https://zenodo.org/records/1167595)** | Recorded paths and simultaneous groups from the same six-month setting as the composite-event study. The release lists a separate 201.4 MB AIS archive; inspect `nari_dynamic.csv`. | Published availability is confirmed; local download/parsing, source cadence, cleaning, component licences and retained class counts remain pilot tasks. Original positions are preferable to compressed synopses for checking short-burst motion. |
| **Paired candidate: [Composite Maritime Events](https://zenodo.org/records/2557290)** | About 4 million rule-recognised events over six months near Brest; event definitions/intervals may locate useful segments in the original position data. | Validate vessel IDs, times/time zones, preprocessing and interval boundaries before joining. Labels are operational rules, not complete independent truth. Long-event labels do not automatically describe a short rendered fragment, and not all proposed classes are supplied. |
| [US Marine Cadastre AIS](https://marinecadastre.gov/ais/) | Optional larger-track background source. | The [2025 product documentation](https://catalog.data.gov/dataset/nationwide-automatic-identification-system-2025) states one-minute filtering. Denser rendering cannot establish second-level manoeuvres between those points. Audit other years separately. |
| [Danish Maritime Authority historical AIS](https://www.dma.dk/safety-at-sea/navigational-information/ais-data) | Fallback if usable Brest subsets are inadequate. | Actual download, terms, per-vessel cadence and simultaneous-event support remain to be tested; archive existence does not guarantee dense examples. |
| Procedurally generated trajectories | Controlled stress cases or rare geometries. | Label their provenance and report separately from recorded AIS. Procedural-only results require narrowing the AIS-driven claim. |
| [SAT-MTB official page](https://csu.cas.cn/gb/kybm/sjlyzx/gcxx_sjj/sjj_wxxl/202211/t20221121_6551405.html) · [download listed by its authors](https://zenodo.org/records/15253996) | Primary candidate **real optical satellite video**. Overall 249 videos and >50,000 frames; framewise object annotations include ships. | Download record could not be opened by this check, although the official page lists it. Inspect actual archive, licensing, ship-sequence durations, multiple-ship encounters, time metadata and annotation quality. No stated movement-event labels. |
| [OOTB repository](https://github.com/YZCU/OOTB) | Alternative real satellite-video ship tracking source (110 total sequences, 29,890 total frames). | Not all sequences are ships. Oriented boxes/tracking attributes are not behaviour labels. Download links and usable ship count must be checked. |
| [SatSOT official page](https://www.csu.cas.cn/gb/kybm/sjlyzx/gcxx_sjj/sjj_wxxl/202106/t20210607_6080256.html) | Additional real single-object satellite-video tracking examples, including some ships. | Small ship subset; no verified event labels. |
| [VISO dataset/code](https://github.com/QingyongHu/VISO) | Satellite-video tracking benchmark with moving objects; possible extra visual domain test. | Verify actual ship representation and access before using; it is not an activity-labelled corpus. |
| [AIR-MOT, TGraM repository](https://github.com/HeQibin/TGraM) | Satellite multi-object tracking videos; repository lists 70 released videos and an [updated 100-video link](https://github.com/HeQibin/TGraM/issues/9). | Its classes and ship-specific event coverage must be inspected; tracking labels do not automatically become movement-event labels. |
| [SatRMOT](https://satrmot.github.io/) | Reannotations of SatVideoDT, SAT-MTB-MOT, AIR-MOT and VISO with language descriptions of tracked objects; ship expressions may help locate candidate motion examples. | Not independent source footage if combined with its component datasets; expression count is not a count of unique ship events or validated loitering/encounters. |
| [MMDEC, Zenodo](https://zenodo.org/records/17491518) | Co-located AIS and Sentinel-1 **SAR acquisitions** in the English Channel region over three months; useful for a separate snapshot/matching analysis. | Not optical video and not a dense ship-by-ship motion-event benchmark. Do not describe repeated satellite acquisitions as continuous frames. |
| [FUSAR-Ship, Fudan University](https://emwlab.fudan.edu.cn/resources/list.htm) | Over 5,000 Gaofen-3 SAR ship chips associated with AIS; useful for a separate SAR snapshot/ship-recognition branch. | Static SAR chips, not optical video or temporally labelled behaviour. The AIS association does not make it a movement-sequence benchmark. |
| [Sentinel-2 multispectral vessel boxes matched to AIS](https://zenodo.org/records/15571607) | AIS-linked optical snapshot crops for appearance/resolution/domain checks. | Single images; no continuous motion labels. |
| [Ship-S2-AIS, Zenodo](https://zenodo.org/records/7229756) | Roughly 13,000 Sentinel-2 tiles from 29 products, AIS auto-labelled and manually checked, useful as adjacent detector/type data. | **Files are restricted** despite the public record; unsuitable as an assumed core dataset. Snapshots, not video. |
| [Global Fishing Watch Sentinel-2 vessel detections](https://zenodo.org/records/20762421) | Real detection catalogue and metadata for broad optical context. | Detections at satellite acquisition times, not continuous identity-labelled ship videos or gold movement events. |

The [Brest dataset paper](https://doi.org/10.1016/j.dib.2019.104141) links the original position data and the derived event ecosystem. The remaining concern is suitability and alignment, not whether an underlying AIS archive exists. For interaction examples, preserve simultaneous recorded groups; artificial combinations of unrelated tracks are simulated encounters, not recorded interactions.

**Real-footage datasets above are optional.** No checked source yet secures real ship video, matching AIS and independently verified labels for all proposed behaviours together. SAT-MTB/OOTB might support a narrower image-track-based reference, but only for visibly represented events and adequate durations. This limitation does not block the approved simulation-first start.

**AIS labels have a specific strength and limit.** The [Composite Maritime Events paper](https://cer.iit.demokritos.gr/publications/papers/2019/pitsikalis-CERMM.pdf) was peer reviewed and checked selected first-month recognized events with expert feedback. For example, its expert-feedback table reported 52 true positives and 2 false positives for `rendezVous`. The authors could not calculate recall without complete ground truth; loitering was not among the expert-checked classes. Its event rules can train a synthetic-image model or provide a **rule-agreement test**, but they cannot independently verify what real satellite footage shows. Apply equivalent rules to AIS paired with a real image only when an actual time/location match exists; do not join unrelated Brest events to SAT-MTB clips.

## 5. Simulation-first study design

1. **Inspect a bounded Brest subset first.** Check positions, timestamps and event alignment; count candidate behaviours and independent vessels/voyages before large-scale generation. Do not assume event coverage from the size of the archive.
2. **Define supported movement labels.** Specify speed/displacement changes, relative motion and repeated-pattern evidence. Freeze reference definitions before final experiments. Scores against rule-derived labels measure recovery of operational definitions, not confirmed intent or activity.
3. **Partition before sampling and rendering.** Use the vessel-disjoint protocol in Section 7. Keep all windows and altered renders attached to their source group; preserve genuine simultaneous groups for interactions.
4. **Generate a simple observation pipeline.** Start with 2D top-down ship sprites on sea backgrounds, consistent appearance through each clip, declared camera geometry, blur/downsampling and bounded image variation. Use a small pretrained detector and lightweight tracker rather than training detection from scratch. Export reference boxes/masks, true IDs and timestamps separately from model inputs.
5. **Compare observation levels.** Use perfect reference tracks for sanity checks, corrupted-coordinate observations for controlled experiments, and detector/tracker outputs from rendered images for the simulated image-pipeline test. If image extraction is absent, report a simulated track study rather than demonstrated image-sequence classification.
6. **Investigate the three behaviour packages.** Use a compact GRU or 1D-CNN family, shared baselines and task-specific comparisons; limit C initially to two temporal scales. Teams can begin on the coordinate interface while rendering is developed, avoiding a shared infrastructure bottleneck.
7. **Test held-out simulation settings and reliability.** Measure error, coverage and tracking failures under changed observation conditions. Real verification/adaptation may be added later using separate development and final test footage.

### 5.1 Declared observation contract

These are proposed experimental defaults to test in the pilot, not validated parameters or a claim of exact sensor replication. [Planet documents SkySat videos of 30-120 seconds](https://docs.planet.com/data/imagery/skysat/); this anchors burst duration only, not the renderer's pixel scale or optical realism.

| Item | Core setting and limitation |
|---|---|
| Physical duration | Begin with 60-second scenes; extend to at most 120 seconds if source examples and compute support it. Evaluate shorter prefixes. Never speed up a long AIS voyage to fit. |
| Source cadence/support | Inspect received AIS gaps. Use task-specific support with recorded points bracketing scene boundaries and limits on boundary offsets/internal gaps. Counts alone are insufficient. Interpolated motion is explicitly assumed. |
| Frame interval | Initially one rendered frame per second; compare 2- and 5-second intervals on matched scenes. Denser frames add no new recorded AIS evidence. |
| Pixel sampling/field | Start at 2 m/pixel over a fixed 1,024 m square field, giving 512 x 512 pixels. Test 1/2/4 m per pixel only with the same physical field and declared raster sizes/resizing. Blur and contrast also affect effective resolution. |
| Camera/calibration | Fixed registered view and declared pixel-to-metre mapping first; registration perturbations are stress tests. A vessel-centred camera must supply/estimate its motion explicitly. Hidden reference camera motion is not an ordinary model input. |
| Visibility | Specify task-dependent maximum visible gap/minimum evidence. A vessel leaving the field is censored; do not silently move the camera or remove the loss from coverage reporting. |
| Decision timing | Primary predictions use currently available trailing windows. Online delay measurements require causal filtering and no future-assisted interpolation/track repair; retrospective whole-clip results are separate. |

The core does not assume hours of uninterrupted orbital video. Longer continuous simulations are hypothetical sensor/track stress experiments, not established applicability to a current video product. A completed loop is retained only if supported in the declared burst; long-duration loitering is not inferred from an uninformative short fragment.

### 5.2 Source eligibility, stationary motion and ambiguity

The [US Coast Guard Class A documentation](https://www.navcen.uscg.gov/ais-class-a-reports) describes reports every 2-10 seconds underway and every three minutes at anchor. These are not guaranteed received intervals in Brest or a rule for all AIS device classes. A universal six-points/ten-second-gap filter could disproportionately remove stationary examples; measure this rather than assume it happens.

- **A:** For turning/deceleration, require original recorded displacements before and after the change and adequate boundary/gap support. Treat sustained near-stationary motion separately from deceleration-to-stop. Sparse agreeing endpoints do not confirm continuous stationarity; omit/narrow that target or label a constant-position stress simulation as assumption-based.
- **B:** Both vessels need overlapping supported intervals, with recorded evidence for the relevant relative-motion phase. Close interpolated endpoints alone are insufficient.
- **C:** Each claimed reversal/repetition must be supported by successive recorded displacements in the burst. A large point count cannot compensate for a gap over the decisive manoeuvre. Plot timestamps, positions, candidate labels and ambiguous examples during the pilot.

Freeze task-specific limits after development inspection. Report candidate/retained/excluded counts and reasons by candidate behaviour and available vessel category/device class, including unknown metadata, plus unique vessels, voyages and final independent groups. Pre-filter labels may be provisional where evidence is weak. Offline reference generation may use bracketing points; future AIS must not enter online classifier features.

Keep **abstention** separate from movement labels. Identify incomplete/ambiguous reference windows and report error versus answered fraction (coverage), including per-class coverage. Rejecting a hard case is not automatically a correct extra class. Full-path labels must not silently turn short-window recognition into hidden-activity prediction.

**Compute boundary:** One AIS source/region, one 2D renderer, one shared detector/tracker, cached outputs and compact temporal models. No graph model, diffusion generator, high-fidelity SAR simulator or broad architecture search in the core. A richer renderer requires a measured justification; injected noise/identity errors must not be described as naturally produced by image extraction. SAR remains a separate modality with different imaging physics.

## 6. Sentinel-2 snapshots versus satellite video

The supplied **“Reading ship behaviour from free satellite photos”** PDF proposes a **different, narrower study**. Its input is one Sentinel-1 SAR or Sentinel-2 optical image crop, not a sequence; its proposed outputs are parked/slow/underway, single/alongside/nearby, and confidence or “I don't know.” It would match ships in free coastal satellite images to AIS at acquisition time, derive weak motion/proximity labels, train a small image model and test on unseen regions. Its illustrative pilot asks whether enough images align with AIS within roughly 15 minutes, whether clear encounter examples exist and whether two large nearby ships remain visually separable. Those are **proposal assumptions to test**, not established dataset facts or validated thresholds.

That alternative snapshot plan suggested three different member studies: (1) motion-state recognition against wake/physics-based speed estimates; (2) alongside/nearby recognition and its resolution-dependent size limit; and (3) AIS label-error, region transfer and confidence. These are not the current workload in Section 8. The current sequence project adds temporal motion and tracking in simulation, with real transfer optional later. If a behaviour is unobservable at the declared duration, synthetic video does not remove that limitation.

Sentinel-2 snapshots can support vessel detection, rough type, wake/speed cues and spatial arrangements in certain conditions. They generally cannot reconstruct an individual ship's short turn, approach or loitering history from revisit-spaced acquisitions. A single image may weakly suggest motion; it does not show a trajectory through time. At 10 m pixels a 100 m ship occupies only about ten pixels along its length; very small boats may occupy one or two pixels. Sentinel-2 optical images are cloud-limited; Sentinel-1 SAR works in cloud/night but is a different visual domain. The [Sentinel-2 band-offset speed study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6651096/) and [single-image AIS-linked classification](https://www.eurasip.org/Proceedings/Eusipco/eusipco2019/Proceedings/papers/1570532157.pdf) are important precedents for the narrower motion-state claim. [Ballinger's PlanetScope encounter study](https://arxiv.org/abs/2404.07607) is a close precedent for the alongside claim, although it used commercial imagery.

The snapshot proposal's phrase “parked (anchored or moored)” is too strong if based only on speed or a single image: slow motion, drifting, docking and anchoring can look similar. Its suggested close-and-slow AIS encounter rule is also a **derived event definition**, not a confirmed meeting or transfer. The Brest composite-event labels were expert-checked only for selected recognized examples, not fully independently verified for all activities. Train/test region separation, AIS/image timing-error audit, cloud filtering and vessel-size breakdown would be essential. A freely downloadable, adequately large **alongside** image test set has not yet been secured.

The current proposal needs source-supported AIS paths and an explicit simulated sampling regime. Real sequences become necessary only for a later real-verification claim. A few correctly spaced frames may support a turn/approach, while a longer event needs a longer observation. Neither synthetic continuous video nor a large video model repairs missing information in Sentinel-2 revisit-spaced snapshots. The [Copernicus mission documentation](https://sentiwiki.copernicus.eu/web/s2-mission) describes the nominal multi-day revisit regime.

## 7. Evaluation and claim boundaries

### 7.1 Fair comparisons and complete denominators

| Comparison | Specification |
|---|---|
| Oracle rules | Rules on perfect reference tracks check label implementation; they are not a meaningful competitor to outperform when those rules define truth. |
| Main rules baseline | Tune prediction smoothing, persistence and thresholds on development data while reference label definitions stay frozen. Keep raw-track rules as a diagnostic. |
| Learned baselines | Feature classifier and compact temporal model given comparable observations, maximum history and quality/context information. Give A's quality variables to the feature baseline too. |
| Rendering value | Match source paths, class mix, training volume, feature access and tuning budget for parametric-noise versus rendered-error training. Test both on the same held-out rendered detector/tracker outputs. Include temporally correlated noise so simple jitter is not the only comparator. |
| C's temporal scales | Compare two-scale and single-scale models at identical maximum history/decision time with comparable capacity; more input alone does not establish an architectural gain. |

Measure error correlation, size-dependent misses, fragmentation, merged detections and identity switches against simulation references. Rendering may provide useful structured failure diagnostics without increasing accuracy. If it adds neither useful error structure nor a useful comparison, simplify and explicitly reframe the result as a simulated track-observation study. A win on one renderer does not establish real-image transfer.

Select B's pairs from observed tracks with a development-set gate, including unrelated nearby pairs and scenes without target events. All methods use the same candidates. Report candidate recall, conditional classification and **end-to-end recall including entirely missed vessels, pairs and events**. Freeze reference matching/event eligibility; report censored and incomplete cases rather than dropping them silently.

### 7.2 One partition and uncertainty protocol

**Primary target:** Generalisation to new retained AIS vessel identities under the declared simulated observation model. Use the same protocol for all packages:

1. Define source scene/voyage/manoeuvre IDs before windows/renders. Assign vessels deterministically with one fixed seed to train/development/test, initially targeting 70/15/15 by vessel count; do not search seeds for favourable final counts/performance.
2. Keep a scene only if all AIS-sourced vessels rendered in it, including distractors, belong to the same partition. Exclude cross-partition scenes/encounters; report their number and effect on the class/geometry distribution. Do not duplicate a vessel across partitions to preserve a pair.
3. All windows, corruptions and repeated renders inherit their source partition. Connected excerpts stay together; exclude or explicitly trim crossing source episodes before sampling so recorded observations cannot enter two partitions.
4. Within a partition, link retained scenes sharing an AIS vessel or overlapping source episode. These dependency-graph **connected components** are the resampling units. In paired comparisons, resample the same components, keeping every contained voyage/window/render together; do not bootstrap frames/scenes as if independent.
5. Report vessel/voyage/scene/component counts, per-label component support and largest-component fraction. Encounter chains may leave few components. If credible uncertainty or class support is impossible, report the limitation and revise sampling/generalisation scope during the pilot before final experiments; do not silently switch to narrower scene-level intervals.

Hold out backgrounds/assets and selected observation settings separately when testing renderer generalisation. Avoid label-correlated ship appearance, background or duration. Freeze final tests and maintain one source manifest. These rules do not themselves prove enough groups exist.

### 7.3 Metrics, decisions and valid claims

- Report macro-F1, per-class precision/recall and confusion matrices. Declare point-estimate weighting so dense overlap does not masquerade as independent evidence. For events, report false alerts per scene-hour, onset delay and recall together; include tracking failures and per-class abstention coverage.
- Choose one primary comparison/metric per student and a development-justified smallest useful difference. Use paired 95% intervals for the difference from the dependency-component resampling protocol when support permits. Separate confidence-interval overlap is not a superiority test; few components may make estimation inconclusive.
- Use one-factor comparisons and initially at most three planned combined stress conditions for cadence, duration, pixel scale, missed observations, identity errors and registration. Other comparisons are exploratory.
- A baseline win or supported null result is valid research. A wide interval is inconclusive, and non-significance alone does not establish equivalence or prove rules suffice. Practical equivalence requires prespecified bounds and adequate precision.
- Synthetic results establish recovery of the specified operational labels under tested assumptions. They do not establish real-satellite performance, actual activity/intent, accuracy for every AIS-silent vessel or illegal-vessel detection. AIS-free classifier input demonstrates an information boundary, not population generalisation. Physically small boats and pixel-small targets need separate definition/evaluation.

Optional real calibration requires reference tracking annotations to estimate true errors; predictions alone are insufficient. Behaviour labels are unnecessary for this limited calibration task. Keep calibration/development clips separate from any later final verification, and account for reused source videos across benchmarks.

## 8. Three connected research contributions

| Member | Behaviour family and question | Primary comparison and attributable result |
|---|---|---|
| **A: Individual movement and recoverability** | Transit, turning and deceleration-to-stop; sustained near-stationary motion only if supported. When does estimated observation quality help recognition? | Same compact model with/without observable quality inputs, plus quality-informed feature and tuned-rule baselines. Report performance/coverage against cadence, pixel scale, noise and history, with retention by behaviour/category. Recoverability is method-dependent, not a universal physical limit. |
| **B: Interactions and identity errors** | Closing/separating, co-moving and passing when the event is visible. Can relative temporal modelling distinguish interaction from chance proximity under identity/fragmentation errors? | Relative-motion rules, feature classifier and compact pairwise model on identical observed candidates. Report candidate recall, end-to-end event recall, false alerts and identity-error sensitivity. |
| **C: Partial pattern recognition** | Repeated direction changes/back-and-forth versus isolated turn/transit; completed loops only within supported bursts. Does combining temporal scales improve recognition at equal available history? | Two-scale versus equal-history single-scale model and applicable shape baseline. Report accuracy/coverage versus visible prefix, false repeated-pattern alerts and optional delay at comparable recall. |

**Shared engineering:** AIS preparation, generator, source labels, detector/tracker, splits/manifests, evaluation utilities, caching and interface. Dividing only generation/training/frontend would not establish three research contributions. Each student owns a task specification, hypothesis, primary comparison, bounded experiments and failure analysis. Different behaviour labels alone are insufficient novelty.

The outputs can coexist: turning while approaching is possible. Specify hierarchical/multi-label decisions within each family. A studies local state/quality; B studies relationships between tracks; C studies repeated structure requiring more history than an isolated turn. Do not assign C an unavailable hours-long feed to create workload.

**C's feasibility gate:** Show timestamped source-position plots, candidate labels and recorded support for each repetition/reversal. Count distinct vessels, voyages, source manoeuvres and final dependency components by label and partition. Many overlapping windows/renders from a few manoeuvres do not establish independent support. Narrow/revise C only after inspecting these examples if its primary comparison cannot be supported; do not invent a replacement package in advance.

## 9. Feasibility and go/no-go gates

**Decision: ready for a bounded feasibility pilot under the supervisor-approved simulation-first scope.** The three-person contribution remains conditional on data support, especially C, and on precise differentiation from prior work. Real footage is not required for the initial pilot. Its absence limits claims rather than automatically cancelling the agreed starting direction.

The project is planned around three students, approximately 6-8 implementation months and intermittent access to one modest GPU. Prototype rendering, extraction, training and storage must be measured rather than promised. A working interface demonstrates the research but is not a substitute for an individual contribution. The user waived the module's earlier avoid-crime preference for this project; no semantic illegality target is introduced.

### First 2-3 weeks: concrete pilot evidence

1. **Data:** Download a bounded original Brest subset, inspect positions/cadence and candidate event intervals, test ID/time alignment, and record terms. Show post-filter and post-split counts, task-specific eligibility, boundary coverage and the effect of cross-partition exclusions.
2. **Observations:** Show recorded-point evidence for retained labels, ambiguous fragments and C's repeated patterns under the declared burst. Do not replace missing evidence with interpolation or time compression.
3. **Compute:** Demonstrate a small 2D generation/extraction run, cache compact tracks and measure runtime/storage/model memory. MP2Net is a precedent, not a compulsory software dependency; installation cost is a pilot consideration.
4. **Research:** Each student identifies the nearest studies, one hypothesis, a primary fair comparison and a practical-effect criterion. Shared work must not be counted as three separate methodological contributions.

### Bounded continuation plan

| Stage | Shared milestone | Individual evidence |
|---|---|---|
| Months 1-2 | Versioned small dataset, generator, observation interface and baselines. | Supported task specification, split counts and initial comparison per student. |
| Months 3-4 | Stable extraction/evaluation and bounded observation-stress matrix. | Main quality-input, pairwise and temporal-scale investigations. |
| Months 5-6 | Frozen synthetic tests and integrated demonstration. | Paired results, coverage, failure analysis and writing. |
| Months 7-8, if available | Replication/consolidation; optional real-data calibration or verification pilot. | Resolve weaknesses before adding scope. |

**Minimum deliverables:** Documented simulator/data manifest; three attributable task/model investigations; reproducible baselines; held-out synthetic tests with dependence-aware evaluation; integrated demonstration and explicit limitations. Simulation-only findings are a legitimate starting deliverable, not a validated general-purpose system for every real satellite-detected ship.

## 10. Current protocol and review history

- [Detailed simulation-first workload and review brief, revision 3](x48-simulation-first-workload-and-review-brief.md): full task boundaries, observation assumptions, source support, partition/resampling algorithm and pilot requirements.
- [Review response and revision log](x48-review-response-and-revision-log.md): accepted, modified and declined suggestions, targeted source checks and methodological assistance acknowledgement.
- [Research module and team criteria](../../../research-module-and-team-criteria.md): individual contribution, data and resource requirements.
- [Earlier four-page beginner PDF](../../../output/pdf/satellite_vessel_behaviour_project_brief.pdf): literature/introduction reference; predates the simulation-first workload revisions and is not the current protocol.

This report and the detailed revision-3 brief now share the simulation-first direction. Future scope changes should update both; earlier real-verification-first conclusions in historical material do not override the supervisor's later decision.
