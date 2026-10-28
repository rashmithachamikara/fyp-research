[← Research candidates](../research-candidates.md)

# Learning elephant corridor permeability instead of assuming habitat suitability equals movement

**ID:** X18 · **Area:** Ecological ML / landscape connectivity and remote sensing · **Status:** Conditional opportunity; local outcome data not secured

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

A patch can attract elephants while also exposing them to people. Habitat suitability, structural connectivity and observed movement are distinct. Corridor maps built from expert weights or modelled suitability can therefore look plausible without predicting actual passage.

**Potential stakeholders:** Landscape ecologists and researchers comparing corridor-prioritisation methods; this project does not authorise land-use changes.

## 2. Research gap and question

**Tentative gap:** Learn and independently evaluate movement resistance using existing trajectories or effort-labelled passages, and propagate land-cover/model uncertainty into corridor ranking. Test whether rankings remain stable when alternative plausible resistance models fit the same observations.

**Documented versus inferred:** Sri Lankan GIS-MCDA and LUCIS work map suitability/conflict; LUCIS notes independent validation is absent. Elephant connectivity already has multi-scalar international studies. The uncertainty-and-passage test is an inferred opportunity, requiring an actual movement dataset rather than validation against another model's map.

**Research question:** Does a movement-trained resistance model predict held-out Sri Lankan passage better than habitat-suitability and expert-weighted resistance maps, and how stable are its corridor rankings under mapping uncertainty?

**Hypothesis and rival explanation:** Observed-movement supervision improves passage prediction and reveals corridors that expert suitability weights rank inconsistently. Rival explanation: routes reflect observation access, repeated animals, or shared predictor/label sources rather than landscape permeability.

This is an AI-assisted research opportunity, not certified novelty. Sri Lankan geography alone is not an original contribution. Seasonal ranging, local passage, habitat suitability, reported conflict and migration are different targets.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Indexing habitat suitability and HEC using GIS-MCDA, 2023](https://doi.org/10.1016/j.geosus.2023.08.004) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1016%2Fj.geosus.2023.08.004) | Expert-weighted habitat and conflict suitability in a Sri Lankan landscape. | Suitability is not observed movement resistance; test independent passage evidence. | Indexed abstract plus supplied review's selected limitations; original full methods inaccessible; Abstract; review pp. 16 and 60 (X18-L1) |
| [Landscape connectivity for African elephants: multi-scalar assessment, 2024](https://doi.org/10.1111/1365-2664.14746) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1111%2F1365-2664.14746) | Large-scale elephant connectivity assessment provides a close methodological comparison. | Neither learned resistance nor multi-scale connectivity is new; Sri Lankan validation and model-error propagation need distinction. | Retrieved scholarly record and supplied review; original full methods inaccessible; HEC-D3R nearest neighbours; review p. 41 (X18-L2) |
| [Game theory-enhanced LUCIS planning in Sri Lanka, 2026](https://www.frontiersin.org/journals/sustainability/articles/10.3389/frsus.2026.1838933/full) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3389%2Ffrsus.2026.1838933) | Suitability overlap and modelled allocation scenarios; authors explicitly note missing independent predictive validation. | Test external outcomes rather than treating an improved planning index as reduced conflict. | Full text; source data, limitations and repository statement; Sections 2.1 and 4.5; Data availability (X18-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1016%2Fj.geosus.2023.08.004,10.1111%2F1365-2664.14746,10.3389%2Ffrsus.2026.1838933). The supplied 63-page review informed discovery; selected original sources were checked, not all 50 references. [Evidence ledger](../../metadata/evidence-ledger.csv) · [Search, access and review records](../../metadata/elephant-expansion-records.json).

## 4. Proposed approach

Use one landscape and a small set of candidate connections. Learn resistance from source movement data, compare least-cost/circuit baselines and analyse the stability of rankings. Human-exposure proxies are a separate trade-off, not a measured probability of safe passage.

## 5. Data and resources

| Item | Current position |
|---|---|
| Required outcome | Existing georeferenced/time-stamped Sri Lankan GPS tracks or systematic passage detections with effort, including independent validation locations. No suitable licensed movement corpus has been secured. |
| Public environmental evidence | [LUCIS supplement](https://github.com/batlahiya/Supplementary-data-and-figures-for-the-LUCIS) contains suitability/planning outputs; the [Dryad Asian habitat archive](https://datadryad.org/dataset/doi:10.6076/D1P305) lists historical model outputs. These can support reproduction/context, not independent observed routes. |
| Access/terms limit | Access to outcome observations, spatial precision and reuse terms is unresolved. A public GitHub repository without explicit underlying-data rights does not grant permission to redistribute sensitive locations. |
| Bounded core / fallback | One landscape, a few source/destination areas and compact resistance learners. Uncertainty analysis of public model outputs is a fallback exploratory study, but does not satisfy the central movement-validation claim. |
| Resources, estimated | CPU GIS/network methods, 16–32 GB RAM and 10–30 GB working storage for a capped landscape. A small tabular learner is sufficient; no large image model is necessary. Data access and ecological learning are larger risks than compute. |
| Prototype | Historical comparison of corridor rankings, uncertainty and exposure proxies; do not publish precise live elephant routes or imply a corridor is approved/safe. |

**Access is a selection dependency.** No institutional partnership, free licensed local outcome corpus or author permission is assumed. No data-access request was sent. Resource figures are estimates; no model training or timing experiment ran. The bounded supplement audit inspected an archive listing and two GeoPackage schemas, not a complete ecological dataset.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: learned resistance | Does observed-movement supervision improve permeability estimates? H: Learned resistance outperforms inverse-suitability weights. | Fit a constrained resistance/step-selection learner using source observations. | Uniform, expert and inverse-suitability resistance; remove movement supervision. | Held-out movement-use prediction at fixed corridor-area budget. |
| B: map-error propagation | How much do remote-sensing errors change corridor conclusions? H: Propagating class/feature uncertainty exposes unstable routes. | Learn/estimate an uncertainty-aware environmental representation and propagate it through a common resistance model. | Deterministic map and independent perturbation controls; remove correlated uncertainty. | Route/rank stability and held-out predictive uncertainty using baseline resistance. |
| C: robust prioritisation | Can a learned ranker retain useful connections across plausible models? H: Robust ranking generalises better than one optimal path. | Train a compact corridor ranker or compare robust optimisation against a common fixed resistance ensemble. | Single least-cost path, circuit ranking and equal-area alternatives; remove robustness term. | Independent passage capture and ranking stability at matched area/exposure-proxy budget. |

One shared problem, three independently assessable contributions. Each intervention runs against an unchanged common baseline, so another member's method need not succeed first. Shared data/code/models are allowed; papers are optional. The team design is conditional on adequate existing data, not a reason to start new fieldwork.

## 7. Evaluation

- **Primary metric:** Held-out observed passage/use captured within a fixed mapped corridor-area budget; for GPS data use held-out step-selection log-loss as a complementary endpoint. Specify the outcome only after inspecting the actual observation design.
- **Split:** Hold out complete animals and geographically separate passage sites/time blocks. Do not train and validate against the same expert corridor map or digitised model output.
- **Baselines:** Uniform distance, expert resistance, inverse habitat suitability, conventional step-selection and gradient-boosted resistance; least-cost and circuit-theory connectivity using identical endpoints.
- **Ablations:** Learned resistance, uncertainty propagation and robust ranking separately; water/crop/human-proximity inputs; match endpoints, area budget, resolution and available observations.
- **Uncertainty and errors:** Animal/site bootstrap, multiple plausible resistance mappings and explicit land-cover perturbations. Analyse seasonal differences, barrier proximity and sparse observation zones; few independent routes imply wide uncertainty.
- **Useful result without winning:** Show that many corridor maps fit observed use equally well, or that uncertainty in land-cover inputs dominates differences between algorithms.
- **Interpretation limit:** Predicted connectivity and low settlement proximity do not demonstrate safe passage, reduced conflict, feasible land acquisition or conservation benefit.

## 8. Score and next decision

**Provisional conditional score: 62.4/100.** This compares the current proposal design and access risks. It is not qualification or achieved model performance. Novelty is 3/5; dataset suitability and/or feasibility are below required thresholds. Four mandatory gates remain Unknown.

### Weighted rubric

Nine relative weights total 98; the final score is normalised to 100. Unresolved gates prevent qualification regardless of arithmetic.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: the suitability/movement distinction is important but resistance learning and validation are established research areas. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: public model maps exist; independent Sri Lankan movement outcomes are not secured. |
| Feasibility and learning curve | 14 | 2 | 5.6 | Low: data, resistance modelling and ecological interpretation create substantial dependency and learning risks. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: learned resistance, uncertainty propagation and rank learning support ML research. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: independent observations could support strong tests, but the correct endpoint and effective sample size remain unresolved. |
| Three-member structure | 12 | 4 | 9.6 | Medium: each contribution can use a common fixed resistance baseline and its own experiment. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: corridor evidence is relevant to Sri Lankan coexistence research; outcomes remain indirect. |
| Compute/storage | 5 | 4 | 4.0 | Medium: bounded GIS and tabular learning fit ordinary compute, subject to raster resolution. |
| Prototype | 3 | 4 | 2.4 | Medium: comparison map is feasible once the research data are usable. |
| **Normalised total / 100** | **98** | | **62.4** | **Not qualified; data access and gap verification required.** |

### Mandatory gates

Pass is supported at bounded design level only. The same provisional-comparison convention used in the existing table applies; unknown gates are not waived and these entries are not admitted as qualified projects.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the Sri Lankan source studies establish a concrete problem; proposed benefits remain untested. |
| 2. ML essential | Pass | Learning or adapting a predictive model is central, not an optional app feature. |
| 3. Train/adapt models | Pass | Sections 4 and 6 define trainable models/objectives; no paid inference service is required. |
| 4. Existing data accessible | Unknown | A suitable licensed Sri Lankan event-level outcome dataset has not been secured; public predictor layers do not replace outcome labels. |
| 5. No unavailable human evaluation | Pass | The bounded design uses existing observations/annotations, without new questionnaires, fieldwork or expert labelling; access is assessed separately. |
| 6. Precise research gap | Unknown | The specific methodological distinction needs checking beyond the cited local studies and broader ecological ML work. |
| 7. Beyond application assembly | Pass | Model-level investigations and ablations go beyond integrating a detector or producing a map. |
| 8. Objective evaluation | Pass | Section 7 specifies an objective conditional evaluation, baseline controls and grouped uncertainty; it is not evidence those outcomes are currently available. |
| 9. 6–8 month feasibility | Unknown | Completion in 6–8 months depends on obtaining adequate existing data early; no partnership or access guarantee exists. |
| 10. Three connected contributions | Pass | Three related contributions can each run against a common unchanged baseline; no separate papers required. |
| 11. No specialised/continuous high-end compute | Pass | The bounded design uses CPU/cached features or an occasional modest GPU; new collars, cameras, microphones and field infrastructure are not required. |
| 12. Manageable responsible use | Unknown | Outcome-data reuse terms, precision restrictions and permitted sharing remain unresolved. |
| 13. Useful negative findings | Pass | Section 7 defines useful negative results and limits when a proposed model is not better. |

**Decision:** High conceptual relevance but a weak fit until independent movement observations and reuse rights are confirmed.

**Next decision point:** Find a legally reusable independent movement/passage dataset; do not train a corridor model against suitability-map outputs and call that validation. Then discuss the evidence, ecological interpretation and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Data feasibility audit](../../metadata/source-checks/elephant-data-checks.json).
