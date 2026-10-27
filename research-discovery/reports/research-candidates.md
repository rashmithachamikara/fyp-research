# Research candidates

Evidence reviewed: **27–28 October 2026**. The original three candidates retain their earlier evidence; X01–X10 were added on 28 October. Based on the [team and module criteria](../../research-module-and-team-criteria.md).

[Explore research areas](areas.md).

Thirteen candidates are evaluated below, including ten additional candidate gaps. Select a topic for its standard gap brief, evidence, team contributions, evaluation and full score breakdown.

**Scoring updated:** 28 October 2026. The remaining relative weights total 98; all scores are normalised to 100.

**Project structure:** one shared problem with three substantial, independently assessable research contributions. Writing papers and publication are optional.

| Research topic | Core gap to investigate | Research area | Compute | Score / 100 | Decision |
|---|---|---|---|---:|---|
| [X10: Intermittent-demand intervals that distinguish missing readings from zero sales](gaps/x10-intermittent-demand.md) | Intervals that separate missing sales from observed zeros in intermittent series | Time-series demand forecasting | CPU-first; original data actually parsed | **80.2 provisional** | Novelty 3/5; avoid a preprocessing-only contribution |
| [X04: Preserving search relevance when compact rerankers are quantised](gaps/x04-quantised-reranking.md) | Train rerankers to preserve relevance under actual quantisation and domain transfer | Information retrieval and NLP | CPU INT8; occasional fine-tuning GPU | **79.2 provisional** | Novelty 3/5; first test whether INT8 causes material harm |
| [X09: Activity transitions under unfamiliar sensor sampling patterns](gaps/x09-activity-sampling.md) | Source-trained sampling policies that preserve brief activity transitions | Sensor-based activity recognition | CPU-first compact temporal model | **77.8 provisional** | Novelty 3/5; compare PRISM and older sampling methods |
| [Reliable confidence in compact audio classifiers](gaps/au2-r-audio-confidence.md) | Confidence reliability across unseen microphones after model compression | Acoustic scene classification | CPU development; optional modest GPU | **77.3** | Refine novelty: **3/5**, below the required 4/5 |
| [X03: Small road-damage detection across countries and annotation variation](gaps/x03-road-damage.md) | Annotation-tolerant small-damage learning with source-only country transfer | Computer vision — road-damage detection | Small country archives; modest GPU | **76.7 provisional** | Novelty 3/5; inspect recent generalisation methods |
| [X05: Rare-emotion uncertainty from limited and disagreeing text annotations](gaps/x05-text-disagreement.md) | Finite-vote uncertainty for rare co-occurring labels across communities | NLP — emotion recognition | Frozen text features; CPU heads | **75.9 provisional** | Novelty 3/5; reconstruct raw votes and grouped splits |
| [X07: Audio emotion confidence with modality-matched annotations](gaps/x07-audio-emotion-annotations.md) | Audio-only confidence trained against the appropriate annotation view | Speech emotion recognition | Frozen audio features; CPU heads | **74.9 provisional** | Novelty 3/5; verify modality-specific targets and media |
| [X08: Choosing anomaly detectors when sensor availability changes](gaps/x08-sensor-detector-selection.md) | Detector selection under changed channel availability and fixed alarm calibration | Multivariate time-series anomaly detection | CPU-first small detector pool | **74.7 provisional** | Novelty 3/5; one testbed limits data suitability to 3/5 |
| [X01: Small document regions under combined scan and layout shifts](gaps/x01-document-layout.md) | Compound scan corruption hides small regions in unfamiliar document genres | Document AI — layout detection | Occasional modest GPU; capped pages | **72.9 provisional** | Novelty 3/5; refine against current layout methods |
| [Load forecast uncertainty during meter outages](gaps/ts2-r-load-forecasting.md) | Outages interrupt both forecast inputs and calibration feedback | Time-series energy forecasting | CPU-first | **72.7 provisional** | Novelty **2/5**; gates 6 and 7 unresolved; medium-low confidence |
| [X06: Recovering short, low-consensus sound events from soft labels](gaps/x06-soft-sound-events.md) | Short low-consensus event suppression with soft targets and temporal pooling | Sound event detection | Compact CRNN or frozen audio features | **71.8 provisional** | Novelty 3/5; resolve label quality and method distinction |
| [Learning when to adapt an industrial defect detector](gaps/cv1-r-defect-adaptation.md) | Adaptation from unverified images can absorb defects into normal references | Computer vision — industrial inspection | Cached features; optional modest GPU | **67.3 provisional** | Data, novelty, workload and contribution boundaries unresolved; low confidence |
| [X02: Land-cover confidence when optical quality and sensor availability change](gaps/x02-satellite-fusion.md) | Confidence under combined sensor absence, optical degradation and geographic shift | Satellite image understanding | Modest GPU; subset route unresolved | **66.5 provisional** | Novelty 2/5; five gates unresolved; redesign/defer |

**None currently meets every qualification threshold.** At the team's request, candidates with unresolved gates now have provisional comparison scores using the revised nine-category rubric. Unknown gates still prevent qualification. Scores assess current proposal designs, not achieved model performance, and decimal places reflect arithmetic rather than certainty. Each gap brief contains the full ratings, evidence and confidence. All ten new scores are provisional; a total above 75 does not override the category minima or gates.

For the next bounded checks, X10 (intermittent demand), X04 (quantised reranking) and X09 (activity transitions) have relatively manageable data and execution paths. X03 is the stronger additional vision lead if computer vision remains the preference. This is a priority for investigation, not a final topic selection: the new candidates all fall below the required novelty rating.

## Before committing

- Resolve the topic-specific questions in section 8 of its gap brief, then review the choice with a supervisor.
- Confirm official dates and rubric, required demonstration, modelling permissions and actual compute access.
- Keep one shared problem with three independently assessable research contributions.

The additional pass used 22 scholarly searches (423 result occurrences), 20 duplication queries and original-source checks. Many search hits were irrelevant; source coverage and reading limits are recorded in [expansion metadata](../metadata/expansion-records.json). These counts do not establish novelty.

Supporting search records, screened-out formulations and checks are retained in [metadata](../metadata/); source claims are traced in the [evidence ledger](../metadata/evidence-ledger.csv).

Assessment workflow support: Scientific Brainstorming and Scientific Critical Thinking from Kassis, T., Agarwal, V., He, Y., Patel, D., and Brueckner, A. M. (2026), [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://doi.org/10.48550/arXiv.2609.00065). The project's own rubric determines the scores.
