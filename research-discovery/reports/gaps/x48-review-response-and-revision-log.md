# X48 review decisions: Revisions 2 and 3

**Date:** 10 November 2026  
**Revised document:** [Simulation-first workload and review brief](x48-simulation-first-workload-and-review-brief.md)

## Scope of this revision

The user supplied `x48-review.md` and a second pasted review. Both are treated as critique to assess, not instructions to follow automatically. The supervisor's simulation-first direction is retained. The user's follow-up about the Pitsikalis/Artikis dataset also prompted a targeted check of the underlying Brest data release.

This revision updates the Markdown brief. The earlier beginner PDF is unchanged and predates these scope/evaluation refinements.

## Decisions and reasons

| Review suggestion / claim | Decision | Reason and resulting change |
|---|---|---|
| Specify an observation regime before fixing classes. | **Adopt.** | Added a finite-burst contract covering physical duration, source/rendered cadence, field of view, pixel sampling, calibration, camera motion, gaps and prediction timing. Numeric settings are provisional design defaults, not verified sensor emulation. |
| NOAA's archive is filtered to one-minute observations. | **Verify and adopt for the documented product.** | The [2025 NOAA record](https://catalog.data.gov/dataset/nationwide-automatic-identification-system-2025) explicitly states this filtering. Do not interpolate it into claimed second-level manoeuvre evidence; do not assume every other archive/year has identical processing. |
| Composite Maritime Events may lack the positions needed for rendering. | **Resolve the missing-source question; retain the practical audit.** | The [original Brest release](https://zenodo.org/records/1167595) lists an AIS archive, and the [dataset paper](https://doi.org/10.1016/j.dib.2019.104141) links the derived event ecosystem. Make Brest positions plus event intervals the preferred combination. Local parsing, cadence, IDs/times and retained class counts remain unverified. |
| Replace Student A with an observability study. | **Modify.** | Preserve individual behaviour recognition as requested by the user. Add a quality-input ablation and empirical recoverability curves. A heatmap alone is insufficient model research; finite experiments cannot establish universal physical observability limits. |
| Student B needs observed pair selection and identity-error experiments. | **Adopt.** | All models use the same candidate pairs selected from observed tracks. Report candidate recall, false pairs, merged/fragmented tracks and complete event recall, including events lost before classification. |
| C needs duration constraints and an equal-history comparison. | **Adopt.** | Core C concerns partial/repeated patterns within a 60-120 second burst, when supported, not an arbitrary long loitering label. Compare two scales with a single-scale model receiving the same maximum history. Revise C if the data do not support a distinct task. |
| Looping necessarily requires tens of minutes/hours; orbital video cannot support C. | **Reject the absolute claim; retain the concern.** | Pattern duration depends on path geometry, speed and the operational definition. A loop's idealised period is `2*pi*radius/speed`, not a fixed number of minutes. This does not prove actual vessel examples are available. Long-duration loitering remains outside the core; no time-compression shortcut is permitted. |
| Calibrate noise using a tracker on real satellite videos from month one. | **Optional enhancement.** | Useful if accessible and affordable, but real footage cannot become a new prerequisite for the approved starting scope. True error statistics require reference tracking annotations and alignment, although behaviour labels are unnecessary. Calibration footage must be separated from later final verification. |
| Rendering is justified only if it improves accuracy; otherwise drop it. | **Modify.** | Rendering may reveal correlated visual-extraction failures even without an accuracy gain. Add matched training comparisons and measured error diagnostics. Simplify/reframe if it adds neither useful error structure nor experimental value. A win on rendered tests does not prove real transfer. |
| A learned model can beat rules only by learning observation-error structure. | **Reject the exclusivity.** | Gains can also reflect learned motion priors, temporal context, class imbalance or extra information. Match inputs/history and include ablations before attributing a gain specifically to error modelling. |
| Main rules baseline should be tuned on filtered tracks. | **Adopt.** | Keep reference label definitions frozen while tuning prediction smoothing, persistence and thresholds on development data. Raw rules remain a diagnostic, not the sole main comparator. |
| Match the rendering comparison and preserve full pipeline denominators. | **Adopt.** | Match source paths, training volume, class mix and tuning effort; evaluate both training strategies on identical held-out extracted tracks. Include correlated-noise baselines. Report conditional classification and end-to-end recall, abstention coverage and censored cases. |
| Beat the baseline outside the confidence interval, or the package fails. | **Correct.** | Use paired intervals for the difference and a predeclared practical margin. Overlapping separate intervals are not the right test. A null/baseline win may be useful; an imprecise result is inconclusive. Absence of significance does not establish equivalence. |
| Use 2D compositing, compact models and a small experiment matrix. | **Adopt as the default, not a universal ban.** | One source/region, renderer, detector/tracker and small temporal-model family; two scales for C. A richer renderer needs a measured justification. Avoid graph models and broad architecture searches in the core. |
| Relevant events should be plentiful; no experts are needed anywhere. | **Do not assume.** | Counts and source density must be measured after cleaning/splitting. Operational motion labels can avoid recruiting experts, but cannot establish semantic activity truth. |
| The proposed novelty is probably enough for an FYP or a conference paper. | **Do not endorse as established.** | Workload, novelty, evaluation strength and publication suitability are different questions. Add closer literature and retain a focused comparison task rather than promise adequacy or publication. |

## Additional literature checked

These primary records support narrower precedent statements, not an exhaustive duplication verdict:

- [Al-Falouji et al. (2026)](https://www.mdpi.com/2077-1312/14/5/507): AIS representation learning, robustness/uncertainty-aware baselines and clustering. Vessel-type classification is an encoder-selection probe; do not describe it as the same fixed movement-class experiment.
- [Guo et al. (2026)](https://doi.org/10.1016/j.oceaneng.2026.125198): encounter identification from compressed AIS, with information-loss and reliability analysis. Relevant to B, but visual identity failures are a different mechanism to test.
- [Xu et al. (2024)](https://zghh.cinnet.cn/en/article/doi/10.3969/j.issn.1000-4653.2024.02.001): wandering extraction and four trajectory-shape classes. C needs a partial-observation/equal-history comparison beyond relabelling shapes.
- [Planet SkySat documentation](https://docs.planet.com/data/imagery/skysat/): 30-120 second video collections. This anchors duration only; the brief does not borrow the 50 cm orthorectified still-product sampling as a video-resolution guarantee.

The underlying [Brest AIS release](https://zenodo.org/records/1167595) is now explicitly prioritised alongside [Composite Maritime Events](https://zenodo.org/records/2557290). Published availability was checked; neither archive was downloaded or counted in this revision. Linking them is a testable data-engineering step, not an assumed completed join.

## Revision 3: Targeted follow-up review

The follow-up judged revision 2 ready for a bounded pilot and proposed three focused corrections. All three were adopted without expanding the project into another research direction:

| Point | Assessment and change |
|---|---|
| Universal dense-AIS eligibility can exclude stationary motion. | Verified the [USCG Class A reporting description](https://www.navcen.uscg.gov/ais-class-a-reports). Replaced the six-timestamps/ten-second-gap screen with task-specific support and explicit boundary coverage. Separate deceleration-to-stop from sustained near-stationary examples. Report retention by candidate behaviour/category; this is a plausible bias mechanism, not a measured Brest result. |
| C needs independent recorded examples, not many windows from a few manoeuvres. | Added a required pilot evidence pack: timestamped original-position plots, candidate labels, recorded support for repeated changes and post-split vessel/voyage/manoeuvre/component counts. Keep the existing decision to revise C only after inspecting the data. |
| Split and uncertainty units are ambiguous. | Specified a single primary unseen-vessel protocol: fixed-seed vessel assignment; exclude scenes involving vessels from different partitions; inherit partitions across windows/renders; resample connected components of retained scenes sharing vessels or source episodes. Report cross-partition exclusions and component sizes. Too few components is an estimation limit to resolve/report, not a reason to bootstrap correlated scenes independently. |

The 70/15/15 allocation is a proposed starting design, not an observed balance or promised class support. Crossing-scene exclusions can materially change the interaction population, so the pilot must report their effect before final scope is frozen. Neither the review nor this revision establishes C's dataset adequacy.

## Review assistance

The scientific-critical-thinking skill informed the appraisal of experimental units, fair comparisons, uncertainty and claim limits. Its methodological source is Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026), [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://doi.org/10.48550/arXiv.2609.00065). This is acknowledgement of review assistance, not evidence for the maritime proposal's novelty or performance.
