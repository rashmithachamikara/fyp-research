## Page 1
Research Proposal: Small Road-Damage
Detection That Transfers to Unseen Countries
 Oct 29, 2026  ·  @Amri
Summary
We will test, on countries a road-damage detector has never seen, three targeted
changes: a short-side-normalised assignment rule, a small-object-anchored consistency
loss, and a source-trained model that predicts where the detector has missed small or
thin damage. Robustness to noisy boxes is an extension, run only if extra GPU time is
confirmed. Each change has one pre-declared main comparison.
Domain generalisation for road-damage detection on unseen countries is already
published (MAMDG, Chen et al., 2026, which aligns features across source countries), so
the four-country protocol is our testbed, not our contribution. The contribution is three
controlled studies that act on other parts of the detector, with questions, controls and
analysis fixed before the held-out countries are opened.
Item Detail
Working title Short-side-normalised assignment, small-damage
consistency and missed-damage prediction for
road-damage detection on unseen countries
Team Three members, UoM Faculty of IT, Level 4 final-
year research
Main research question With no data from the target country, do these
changes improve detection and small-or-thin
damage recall on that country, and can a source-
trained model predict where small or thin damage
was missed there, compared with matched
controls?
Dataset RDD2022 (public, CC BY-SA 4.0): 25,846 labelled
training images from Japan, India, United States
and Czech Republic
Core design YOLO11; leave one country out; an inner validation
country inside every fold for all development; held-
out countries opened once, at the end
Research Proposal: Cross-Country Road Damage Detection
Page 1 of 28

## Page 2
This is version 8, revised after external examiner-style reviews; from version 5 on, a
suggestion was adopted only after we checked it ourselves (October 2026). Version 7
replaced Member C's calibration study with missed-damage prediction; version 8 fully
specifies that study, corrects the Ultralytics version history and re-counts compute.
Novelty claims are bounded to the papers we examined.
Problem and motivation
A detector trained in one country cannot be trusted in another, and challenge reports and
PROBE suggest small, thin damage is especially hard; whether it fails first on our folds is
something we measure, not assume.
What fails today
Country shift. Road surfaces, lane markings, lighting, camera height and phone models
differ between countries. A detector trained on Japanese roads sees a different world
in India or the Czech Republic.
Small damage is lost. Hairline longitudinal and transverse cracks occupy only a few
pixels. Detectors tuned for aggregate accuracy trade them away first.
Annotation style may differ (a hypothesis, not established for RDD2022). Different
annotation teams may draw boxes around the same crack differently, but camera
viewpoint and genuinely different damage produce the same observation, so a
descriptive audit of box shapes cannot establish it. The main study does not depend on
it; simulated box variation is an optional extension.
Silent failure. On a new country the detector still outputs confident boxes. Nothing
tells an operator which detections to trust.
Why it matters
Municipalities and road agencies increasingly use low-cost phone or dashboard cameras
for road surveys, and RDD2022 itself was created to support this kind of crowd-sensed
monitoring. Sri Lanka, for example, has no large public labelled road-damage dataset that
Item Detail
Compute Default scope 72–84 final trainings plus 20–30
development runs; the noise extension adds 48.
GPU time measured in a week-6 pilot; the
extension only with documented extra GPU
capacity
Deliverables Three evaluated member studies, a reproducible
benchmark, a small web demo
Research Proposal: Cross-Country Road Damage Detection
Page 2 of 28

## Page 3
we could find, so a detector used there would most likely be trained on other countries'
data. A method that transfers without target labels, and that flags its own uncertainty, is
the realistic path for them.
Stakeholders: road maintenance agencies and local authorities, pavement-inspection
teams, and developers of road-survey apps.
What this project will not claim: reduced maintenance cost, improved road safety or
readiness for deployment. A benchmark result cannot show those (section 11).
Literature and research gap
Source-only cross-country road-damage detection is published, and each of our three
techniques has close neighbours; the gap is that none of the papers we examined tests
these specific changes, with these controls, on an unseen road-damage country.
Closest work by part
Part Closest work What it already does What we must show
beyond it
Protocol Chen et al., MAMDG,
Image and Vision
Computing 2026
Domain generalisation
for road-damage
detection: trains on
several RDD2022 source
countries with no target
data, using multiple
domain discriminators
and a triplet loss on a
CSPDarknet53 detector,
and claims to be the first
such work. Abstract,
introduction and section
snippets read;
experiments not yet
read; its GitHub
repository contains no
code (checked October
2026)
Nothing for the setting,
which we use as a
testbed and credit to
MAMDG; our three
changes act elsewhere
in the detector
(matching, small-object
consistency, miss
prediction)
Research Proposal: Cross-Country Road Damage Detection
Page 3 of 28

## Page 4
Part Closest work What it already does What we must show
beyond it
Protocol MSDA-RDD, IEEE TCSVT
2026
YOLO11 adaptation with
feature alignment and
teacher–student pseudo-
labels; an external review
reports an accessible
IEEE abstract with these
details, but we have not
been able to open it, so
they remain unverified
Nothing; it is
adaptation, not our
setting
A SimD, IROS 2024; NWD,
2021; scale-adaptive IoU,
EUSIPCO 2025; CoSWA-
YOLOv12, 2026 preprint
Size-dependent
similarity and
Wasserstein assignment
for tiny objects, in single
domains
That our short-side-
relative rule beats
equally tuned plain
NWD on unseen
countries, with the
change in assignment
and target weights
measured by box
geometry
A SSD-Det, ICCV 2023;
Noise-Aware Evaluation,
WACV 2025
Training with inaccurate
boxes; evaluation
sensitivity to annotation
noise
We evaluate on
unchanged labels and
report evaluation
sensitivity separately
B Danish et al., CVPR 2024;
Guo et al., Sensors 2025
Source-only cross-view
agreement (Danish);
scale consistency with
target data (Guo)
That anchoring
consistency on small
and thin ground-truth
boxes beats generic
consistency with
identical views and
budget, and beats a
random subset of the
same size
B CrackTinyNet, IET ITS
2024; PROBE, WACV
2026
NWD for tiny road
cracks; small cracks
named as a failure under
adaptation
Recall by box geometry
on unseen countries
Research Proposal: Cross-Country Road Damage Detection
Page 4 of 28

## Page 5
Also relevant: Dynamic Adaptive Label Assignment for Tiny Object Detection, CAAI TIT
2026 (online 2025) combines similarity-distance matching, ratio-based positive selection
and dynamic loss weighting, so adaptive tiny-object assignment is established territory
for Member A. YOLO-Crack, Sensors 2026 is a YOLO11n crack detector evaluated on
Crack500; an external review reports a cross-dataset generalisation section in its full text,
which we could not open (abstract and Sections 1–2 only), so treat it as possible transfer
evidence to check. Two further items were suggested by an external review but could not
be found or opened by our searches, so they are not relied on: VALA (Neurocomputing
2026) and DIFEDA (IEEE TCSVT, cross-scene road-damage domain adaptation; only its
title was found on IEEE Xplore). A repository on class-wise ensemble fusion and
confidence recalibration for RDD2022 claims CVIP 2026 acceptance; unverified, but a
lead for Member C.
The bounded gap
1 . A: size-dependent assignment similarity is established territory; among the papers
examined, none tests short-side-relative NWD against equally tuned plain NWD on
unseen road-damage countries, with the effect on assignment counts and target
weights measured by box geometry.
2. B: consistency under domain shift is established; none of the transfer papers
examined tests whether which objects receive consistency matters, comparing small-
object-anchored, generic and count-matched random consistency on unseen road-
damage countries.
Part Closest work What it already does What we must show
beyond it
C KGFP, CVPR Workshops
2026; Yatbaz et al., 2024;
Rahman et al., IROS 2019;
Rahman et al., 2020
Predict when a detector
missed objects from its
internal features (people,
traffic signs, driving
scenes), including spatial
vs pooled features and
cross-dataset tests
Road damage; an
unseen country under
leave-one-country-out;
a dense small-or-thin
miss target; whether
detector features add
anything beyond a
learned model of the
weak detections
C Küppers et al., 2020;
Kuzucu et al., ECCV
2024; Park et al., 2024–
2026
Detector calibration
using box geometry;
evaluation pitfalls; per-
image reliability from
confidence scores
Calibration is kept only
as a supporting check;
no road-damage
detection paper we
found measures it
Research Proposal: Cross-Country Road Damage Detection
Page 5 of 28

## Page 6
3. C: predicting detector misses is established (KGFP 2026; Yatbaz et al. 2024; Rahman et
al. 2019–2021), but none of the papers examined does it for road damage, under leave-
one-country-out shift, or with a dense small-or-thin miss target. Comparing against the
detector's own rejected or low-confidence detections is not new (Rahman et al., 2019,
already do so), so our distinction is the grid target, the damage geometry and the
country-transfer test.
No verified paper duplicates the three studies, but each must stand on its own
comparison. MAMDG's abstract, introduction and section snippets were read in October
2026: it shares our setting, not our methods. Read its experiments section and MSDA-
RDD in full before submission and record which sections were read.
Research questions and hypotheses
Each member has one question, one method and one principal contrast, all fixed before
any held-out country is opened; everything else they report is labelled secondary or
exploratory.
Main question. With no data from the target country, do a short-side-relative assignment
rule and small-object-anchored consistency each improve a road-damage detector on
that country, and can a source-trained model predict where the detector misses small or
thin damage there, compared with matched controls?
Member Question Principal
contrast
Hypothesis Primary
outcome
A: thin-box
assignment
Does short-side-
relative
similarity in the
assigner change
assignment and
supervision
weights for thin
boxes, and does
that improve
held-out
detection under
country shift?
(Extension: does
it also help when
training boxes
are noisy?)
A's rule vs plain
NWD with
identical
candidate
eligibility and
equal source-
only tuning of κ
and C, on
original labels
(extension: the
same contrast
on noisy boxes
from a
perturbation
family not used
for tuning)
H1: A's rule gives
higher held-out
mAP50:95 than
plain NWD,
overall and for
small-or-thin
boxes
Held-out
mAP50:95 on
unchanged
labels,
country-macro
Research Proposal: Cross-Country Road Damage Detection
Page 6 of 28

## Page 7
Clean-label check for A. In the noise extension, let Δ  = A's clean-label mAP50:95 minus the
baseline's. Clean performance counts as preserved only if the lower end of the 95%
interval for Δ  stays above −1.0 point (margin fixed now, before any target evaluation). An
interval crossing −1.0 is reported as inconclusive; one entirely below it is reported as a
cost.
A negative result counts as a useful answer only because the contrast, controls and
outcome were fixed in advance; it is not a contribution by itself.
Member Question Principal
contrast
Hypothesis Primary
outcome
B: small and
thin damage
Does anchoring
consistency on
small and thin
ground-truth
boxes add value
over generic
consistency?
Anchored
consistency vs
generic
consistency,
with identical
views,
supervision and
training budget
(secondary:
anchored vs a
random subset
of the same
number of
boxes, one
seed)
H2: anchoring
gives higher
held-out recall
for small-or-thin
boxes at the
source-chosen
threshold, with
false positives
per image no
more than 10%
above generic
consistency's
Held-out recall
for boxes that
are small or
thin (one
population,
each box
counted once)
at each
detector's
source-chosen
threshold
C: missed-
damage
prediction
On a country the
detector has
never seen, can a
model trained on
source countries
predict where it
missed small or
thin damage,
better than the
detector's own
below-threshold
detections
already show?
Head on
detector
features plus
the weak-
detection map
vs a matched
learned head on
the weak-
detection map
alone (same
labels, grid,
training and
selection rules);
the raw weak
map is an extra
baseline
H3: adding
detector
features gives
higher held-out
cell-level AUPRC
for missed small-
or-thin damage
than the learned
weak-map-only
head
Held-out cell-
level AUPRC,
country-macro,
with the share
of positive
cells stated
Research Proposal: Cross-Country Road Damage Detection
Page 7 of 28

## Page 8
Dataset
The project uses the public RDD2022 dataset (CC BY-SA 4.0); the four core countries give
25,846 labelled training images, and some damage types are rare enough to limit what can
be claimed per class.
Labelled images and damage instances (public training release)
Counts from the RDD2022 data paper, figures 4 and 5. The official test images (about
6,500 for these countries) have no public labels and are not used. India D10 (68) and
United States D40 (135) are too sparse for per-class conclusions on those countries;
results for them are reported but labelled as low-support.
Classes: D00, D10, D20 and D40, following the official challenge mapping.
Labels: Pascal VOC XML boxes, converted to YOLO format by script.
Negatives: images in the labelled release whose annotation file contains no boxes are
kept as genuine negatives. An image with no annotation file is never assumed to be
clean road.
Not used in the core: Norway (very large images, different labelling tool) and the two
China subsets; possible extensions.
Where and how to get it
1 . Official source: sekilab/RoadDamageDetector on GitHub, one ZIP per country; the four
core countries are about 2.2 GB.
2. Mirror: Dataset Ninja, with a 296 MB sample.
3. Paper: RDD2022 data article. Cite the journal version, Geoscience Data Journal 2024.
4. Storage: keep original ZIPs unchanged, write converted copies separately, and record
checksums.
Country Labelled images D00 longitudinal D10 transverse D20 alligator D40 pothole
Japan 10,506 4,049 3,979 6,199 2,243
India 7,706 1,555 68 2,021 3,187
United States 4,805 6,750 3,295 834 135
Czech Republic 2,829 988 399 161 197
Total 25,846
Research Proposal: Cross-Country Road Damage Detection
Page 8 of 28

## Page 9
Data preparation (fixed before any experiment)
Duplicate groups and capture sequences are different things. Duplicate groups
(near-identical frames) come from exact hashes and perceptual similarity with
thresholds set once. Capture sequences come from file-name sequence information
where it exists. Both are kept whole inside one split; counts of each are published.
Where sequences cannot be recovered, remaining dependence is stated.
Box geometry (primary definition): common pixel thresholds at a 640 px reference,
the same for every fold: small = area under 32 × 32 px; thin = short side under 16 px;
aspect ratio reported as a separate descriptor. Source-quantile bins are a secondary
analysis. A box keeps its bin in every experiment, including 960 px runs. These describe
boxes, not physical crack width or severity.
Size-specific evaluation: predictions are matched against all ground truth first; boxes
outside a bin are then ignored rather than deleted, so a correct detection of a large
crack is not counted as a false positive in the small-box results.
Data roles inside every fold
Each fold runs in two phases. In development, one source country is set aside as the inner
validation country and the detector trains on the other two. In the final (confirmatory)
phase, settings are frozen and the detector is retrained on all three source countries; only
then is the held-out country opened. All splits keep whole duplicate groups together.
Phase Role Data Used for
Development Training About 80% of the two
training-source
countries
Debugging and trying
settings (mostly one seed)
Development Selection About 20% of the
same
Checkpoints and
hyperparameters
Development Inner validation
country
The third source
country
Go/no-go decisions,
operating thresholds,
checking that methods work
Final Detector
training
About 70% of all three
source countries
The confirmatory runs in the
grid
Final Detector
selection
About 10% of each
source country
Checkpoints only, with the
frozen rules
Research Proposal: Cross-Country Road Damage Detection
Page 9 of 28

## Page 10
C's labels come from the frozen detector's predictions on these two splits, which the
detector never trained on. How many missed small or thin boxes exist is counted per fold
from those predictions, not taken from dataset totals.
If compute is short
Follow the cut order and the reduced scope under Resources and compute. Do not cap
countries at a fixed image count, which would erase rare classes, and never drop a held-
out country.
Methodology
All development happens on source data and an inner validation country; the held-out
countries are opened once, after code, settings and analysis are frozen.
Sequence that prevents leakage
1 . Weeks 1–3: write the protocol (folds, fixed inner validation country per fold, data roles,
principal contrasts, controls, metrics, the decision table below, the cut ladder and the
cap on development trials) and commit it with a date.
2. Weeks 4–22: develop and debug using the development phase only. Go/no-go
decisions, operating-threshold rules, A's κ  and B's loss weight are chosen here,
separately within each fold.
3. Rolling final training: as each configuration is frozen (its code tag and settings file
committed), its final-phase runs start on all three source countries. Their held-out
predictions are written to disk unscored and unopened: no overlays, inspection or
debugging on them before the freeze. Source-country predictions remain available for
that work.
4. Global freeze, week 22: all configurations frozen.
Phase Role Data Used for
Final Miss-predictor
selection (C)
About 10% of each
source country
Choosing C's head settings
and early stopping; the
supporting calibration's
settings
Final Miss-predictor
training (C)
About 10% of each
source country
Training C's head and fitting
the supporting score
calibration
Final Held-out
country
The fold's target
country
Opened once, for the final
evaluation
Research Proposal: Cross-Country Road Damage Detection
Page 10 of 28

## Page 11
5. Weeks 23–27: finish remaining final runs, train C's miss predictors and fit the
supporting calibration, then score each held-out country once.
Fixed inner validation country per fold: Japan held out → United States; India held out →
Czech Republic; United States held out → Japan; Czech Republic held out → India. Each
country serves once as inner validation, and no setting is averaged across folds.
A country can be a source in one fold and the target in another; that is normal, and source-
only does not mean the team has never seen that country's images. What is not allowed is
using a held-out country's results to change a method later evaluated on it. Because one
country's development results could still shape a design that is later held out on it, every
decision is recorded in one of two classes:
Development tuning is screened before it is confirmed, so it fits the 20–30-run allowance.
Each tuned setting (A's κ , plain NWD's constant, B's anchored and generic λ ) is screened
at three values on one fold with a short schedule (12 runs). Only the best two values per
method are then confirmed on all four folds (8 runs), about 20 runs in total, with the same
budget for every method.
Shared baseline
Detector: YOLO11s from COCO weights, 640 px, Ultralytics 8.4.192 pinned (one
detector size only; YOLO11n is a fallback if the pilot requires it). Its standard loss
already includes DFL and the task-aligned assigner (TAL), so neither is a contribution.
Source-only rivals: country-balanced sampling, and a strong photometric and
geometric augmentation baseline. MAMDG's repository contains no code (checked
October 2026), so its published numbers are cited only where its setting matches ours,
and it is rerun only if code is released.
Decision Class When and on what
Architecture (YOLO11s, 640 px),
losses, assigner code, B's views and
mask, C's features and model family,
metrics, threshold rule
Fixed
globally
Before week 4, from the literature
and the protocol; not changed after
any fold result
Changes found necessary during
development (bugs, failed training)
Fixed
globally
Logged with date and the evidence
used; applied to all folds and all
methods
κ , the NWD constant, λ , epochs, miss-
predictor settings, operating
threshold
Fitted per
fold
On that fold's source splits and
inner validation country only
Research Proposal: Cross-Country Road Damage Detection
Page 11 of 28

## Page 12
Faster R-CNN: removed from the core; an optional exploratory check only if GPU time
remains, with its method and folds fixed in advance.
Member A: short-side-relative assignment and weighting
Boxes are treated as Gaussians, as in NWD. For a prediction p and a ground-truth box g
with centre (x, y), width w and height h, measured at the 640 px reference:
What the rule actually does. It measures error relative to the box's short side. For the
same pixel offset, a thin box gets a lower similarity than a wide one (with κ  = 1 and W₂ = 2
px, short sides of 2 and 20 px give about 0.37 and 0.90). So it is stricter on thin boxes in
pixel terms, not more lenient. Whether that helps transfer is the empirical question.
Before training, plot S against W₂ for typical short sides under both rules and record how
they differ.
Where it enters YOLO11: in TAL, the overlap term (normally CIoU) is replaced by S. That
value feeds both the alignment metric used for assignment and the normalisation of
target scores, so the change alters both which predictions become positives and how
strongly each is supervised. It is therefore described as an assignment-and-weighting
change, not a pure assignment change. The mechanism analysis, planned in advance
for A and plain NWD alike, logs by geometry bin: positives per ground-truth box, the
share of boxes with zero positives, and total target-score mass. An assignment-only
variant (S chooses positives, CIoU sets weights) would separate the two effects; it is
an optional one-seed run, not part of the default scope.
Candidate eligibility is identical for A and plain NWD. Pin the Ultralytics release tag
v8.4.192 (commit 922563e). We read the tagged source with git: from 8.4.0 to 8.4.127,
TAL's candidate step widens a ground-truth side below the smallest stride (8 px) to 16
px; from 8.4.128, including 8.4.192, it widens any side below 16 px to 16 px, which covers
every thin box by our definition. Archive the installed source with the code, and in the
pilot check candidate counts for boxes with 6, 12 and 20 px sides. Both rules use this
built-in widening unchanged, so the principal contrast tests only the normalisation.
One development-only run with the widening switched off shows how much candidate
supply matters.
Quantity Definition
Distance W₂(p, g) = length of the vector (x_p − x_g, y_p −
y_g, (w_p − w_g)/2, (h_p − h_g)/2)
Plain NWD (comparator) S = exp(−W₂ / C), one constant C for every box
A's rule S = exp(−W₂ / ( κ  × s_g)), where s_g = min(w_g, h_g)
is the ground-truth box's short side
Research Proposal: Cross-Country Road Damage Detection
Page 12 of 28

## Page 13
κ and plain NWD's constant C are each tuned per fold on that fold's inner validation
country, from the same number of candidate values, so tuning effort is equal. C's
candidates centre on the source data's average box size, as the NWD paper sets C
from its dataset's average object size.
Noise: (extension only) static corruption, generated once per dataset with its own
random seed, shared by every method, separate from the training seed. Methods
never see the clean boxes or the offsets. Boxes are clipped to the image; a box that
becomes invalid keeps its original coordinates and is logged. With one fixed corruption,
the three training seeds measure training variation, not variation across noise
realisations; this is stated as a limitation.
Design family (used to tune κ ): shifts and side expansion or contraction scaled to each
box's short side. Held-out family (the principal test, never used for tuning): fixed-pixel
displacement plus expansion along the long axis only.
Severity: in the extension, one medium severity is confirmatory; low and high are
exploratory, one seed.
Controls: baseline and matched jitter augmentation, trained on the same corrupted
boxes.
Evaluation: always on the held-out country's unchanged labels.
Member B: small-object-anchored consistency
Supervised training policy: the student is trained with the normal detection loss on
the full 640 px image, exactly like the baseline, and is the model used at inference (640
px). In addition, the student makes a forward pass on a half-size copy, used only for the
consistency loss. A separate exponential-moving-average (EMA) teacher, with no
gradients, sees the full-size image.
Which predictions are compared: for each eligible ground-truth box, the top 3
predictions by TAL alignment score in each view (the student on the half-size copy, the
teacher on the full-size image). If fewer than 3 exist, all available are used; if a view has
none, the box is skipped and counted.
Loss: per-class Bernoulli KL divergence between the score-weighted mean class
scores (YOLO's class scores are independent sigmoids, not one probability
distribution), plus L1 between score-weighted mean boxes in normalised coordinates.
The loss is averaged over included boxes in the batch, so its size per box is comparable
whether few or many boxes are included. Added to the detection loss with weight λ ,
chosen per fold on the inner validation country.
Mask: a box whose short side is below 4 px in the half-size copy (below 8 px at full size)
is excluded, so B does not directly supervise the very thinnest cracks. Their share of
the small-or-thin population, and the baseline's recall on them, are reported per
country, and B's results are interpreted with that in mind.
Research Proposal: Cross-Country Road Damage Detection
Page 13 of 28

## Page 14
Anchored vs generic: identical in everything above, including the mask; the only
difference is that anchored applies to small-or-thin boxes and generic to every box.
Because this changes both which boxes and how many, a secondary one-seed arm
applies the same loss to a random subset of boxes of the same size as the anchored set
in each batch. Anchored vs generic shows whether B helps; anchored vs random shows
whether choosing by geometry is the reason.
Further controls (extension only): size-aware loss weighting alone; a 960 px baseline
at matched training exposure, with accuracy plotted against measured GPU time.
Operating threshold rule: for each final detector, the threshold with the highest recall
on its final selection split among those reaching at least 0.7 precision; ties go to the
higher threshold. If 0.7 is unreachable, the best-F1 threshold is used and reported. The
rule is frozen; the number is computed per detector.
Member C: predicting missed small or thin damage
Why: a crack the detector misses produces no box, so nothing in its output says it is
there. C trains a separate model that flags where such misses are likely. It does not
recover the missed cracks.
What counts as a miss: a small-or-thin ground-truth box left unmatched by the same
matcher that sets the operating threshold: same class, greedy by score, one-to-one,
IoU at least 0.5, using detections at or above the frozen threshold. IoU 0.3 and centre-
inside matching are reported only as sensitivity analyses, labelled as misses under
those looser rules.
Target: a 40 × 40 grid per 640 px image (stride 16). A cell is positive if it contains the
centre of at least one missed box. The target is miss location, not crack extent; how
often two or more missed centres share a cell is reported.
Weak-detection map: one extra pass of the frozen detector with a fixed 0.05
confidence floor, after NMS (boxes suppressed by NMS are not kept). Each detection
scoring between 0.05 and the threshold writes its score into the cell holding its centre,
keeping the maximum when several fall in one cell. If a fold's threshold is 0.05 or lower,
its weak map is empty and this is reported.
Model: the detector stays frozen in evaluation mode with no gradients. P3 (80 × 80) is
average-pooled to 40 × 40 and concatenated with P4 (40 × 40) and, where used, the
weak map. Then a 1 × 1 convolution to 32 channels, two 3 × 3 convolutions with ReLU,
and a 1 × 1 convolution to one logit per cell with a sigmoid (about 50,000 parameters).
Pooled features are cached in fp16 for the two training splits.
Training: binary cross-entropy with a positive-class weight set from the fitting split's
positive-cell share, AdamW with weight decay, no augmentation, and the checkpoint
with the best cell-level AUPRC on the calibration-selection split.
Research Proposal: Cross-Country Road Damage Detection
Page 14 of 28

## Page 15
Principal contrast: features plus weak map vs a matched learned head on the weak
map alone, with identical labels, grid, training and selection. This asks whether the
detector's internal features add information beyond its own low-confidence outputs.
The raw weak map (no learning) and a features-only head are further cell-level
baselines. Image-level baselines (confidence statistics, pooled features, logistic
regression) are scored only on the image-level task.
Detectors: the baseline detector in every fold and seed is primary. Heads for A and B
on one seed are secondary, reported as how predictable each detector's own misses
are, not as one monitor transferring between detectors. Alongside AUPRC, report
positive-cell share and AUPRC divided by that share.
Leakage control: the threshold is frozen before any head work; heads train on the
calibration-fitting split, are selected on the calibration-selection split, are developed
on the inner country and are scored once on the held-out country. The bootstrap
resamples whole images.
Go/no-go gate (week 8): on one baseline fold, measure positive cells and images with
at least one miss (these are different quantities). If the grid target is unusable, switch
to a neural image-level miss predictor (same features, pooled, predicting whether an
image has a miss, evaluated on all images including those with none). The version 6
calibration study is used only as a last resort.
Supporting calibration (not the research question): per-class temperature or Platt
scaling with pooled countries, reporting held-out Brier score and ECE for baseline, A
and B. The demo uses it.
Shared evaluation code (bootstrap, decision table) is common team infrastructure and
is not counted toward any member's research workload. A interprets its own
assignment logs.
Bringing it together
The integration study uses original (clean) labels throughout: baseline, A, B and AB all
trained on clean labels, with C's miss predictor and the supporting calibration fitted to
each. A's noisy-label results are a separate study and are never mixed into this
comparison. AB is an extension: it is dropped before any principal contrast if GPU time
runs short.
The diagram below shows the shared pipeline and where each member's change enters.
Research Proposal: Cross-Country Road Damage Detection
Page 15 of 28

## Page 16
A, B and C each start from the same baseline, so each member's effect is measured on its
own before the combined model is trained.
Evaluation plan
Three principal contrasts are tested on the held-out countries, one per member; all other
results are secondary or exploratory, and none is a cross-country significance claim.
shared pipeline · 3 member interventions
Member Principal contrast Primary outcome Secondary outcomes
A A's rule vs plain NWD,
identical candidate
eligibility and equal
tuning, original labels
(extension: medium
severity of the held-out
noise family)
Held-out mAP50:95 on
unchanged labels
Small-or-thin boxes;
similarity curves;
widening-off development
run; in the extension,
noisy-label results and
clean-label Δ  judged
against −1.0
Research Proposal: Cross-Country Road Damage Detection
Page 16 of 28

## Page 17
Operating threshold (B, C's labels, and the demo): the frozen rule picks, for each final
detector, the threshold with the highest recall on its final selection split among those with
at least 0.7 precision (ties to the higher threshold; best-F1 fallback if 0.7 is unreachable).
Held-out precision is then whatever it turns out to be, and is reported. H2 counts as
supported only if anchored consistency raises held-out small-or-thin recall and its false
positives per image are no more than 10% above generic consistency's; otherwise the
recall–false-positive trade-off is reported without declaring support.
Size-specific scoring: predictions are matched against all ground truth first; ground-truth
boxes outside the bin, and predictions matched to them, are ignored, not counted as
errors.
Macro averages: a class or geometry bin with no ground truth in a held-out country is left
out of that country's average and listed. Low-support groups (fewer than 30 ground-truth
boxes) are flagged.
Uncertainty:
For each country, method differences use a paired bootstrap that resamples whole
images for both methods, keeping duplicate groups together (RDD2022 has no reliable
capture-sequence IDs). Member C's grid cells are never resampled individually.
Seeds: within each bootstrap resample, the method difference is computed separately
for each seed and then averaged over seeds; predictions are never pooled across
seeds, which would evaluate an ensemble. Seed-to-seed spread is reported separately.
Member Principal contrast Primary outcome Secondary outcomes
B Anchored vs generic
consistency, identical
views and budget
Held-out recall for
small-or-thin boxes
(one population) at
each detector's source-
chosen threshold,
always shown with
held-out precision and
false positives
Recall at a fixed precision
read from the held-out
precision–recall curve
(retrospective); mask
exclusion rates; 960 px
comparison against GPU
time
C Features plus weak map
vs learned weak-map-
only head, baseline
detector
Held-out cell-level
AUPRC for missed
small-or-thin damage,
with positive-cell share
AUROC; recall at a fixed
false-alarm rate;
Spearman correlation for
missed counts; Brier score
of the head; same analysis
for A and B (one seed);
supporting calibration
Brier and ECE
Research Proposal: Cross-Country Road Damage Detection
Page 17 of 28

## Page 18
Three seeds estimate training variation only roughly, and one-seed controls support
exploratory conclusions only; for A's extension, seeds share one fixed corruption, so
they do not measure variation across noise realisations.
Results are given per country, as a country-macro mean, and for the worst country.
With four countries, even a clean sweep gives only p = 0.125 on a sign test, so four-
country averages are not presented as predictions for other countries.
Limits stated up front. Four countries do not represent all countries. Any box noise is
simulated. Box geometry is not crack size or severity. C's predictions flag where small
damage was probably missed; they do not find the missed cracks, and they depend on
RDD2022's labels being complete. Benchmark results do not show savings or safety
benefits.
Prototype
A small web app shows the research in action; it is a demonstration, not the contribution.
Upload a road photo from the RDD2022 held-out test images or other public images;
the app returns boxes for cracks and potholes.
Scores and miss warnings shown honestly: each box shows a calibrated score, and a
heat-map overlay from Member C marks where small or thin damage was probably
missed. Both are labelled as estimates measured on benchmark data, not guarantees.
Boxes below the source-chosen operating threshold are greyed out rather than
hidden.
Compare models side by side: baseline versus improved detector on the same image.
Stack: Python FastAPI service running the exported model (ONNX on CPU) and a
simple React or Next.js page. No GPU is needed at demo time.
No new photos are collected for the demo, in line with the module's no-data-collection
rule.
Resources and compute
The reduced scope is the realistic default with 15–25 GPU-hours a week; the noise
extension needs documented extra GPU capacity, and the week-6 pilot decides between
them.
Default scope (final phase, four folds)
A becomes a different question: does short-side-normalised assignment help on original
labels? The noise study is dropped.
Research Proposal: Cross-Country Road Damage Detection
Page 18 of 28

## Page 19
Extension: noise study (only with confirmed extra GPU capacity)
Added on top of the default scope.
Experiment Seeds Trainings Cost per run
Baseline, clean labels 3 12 Ordinary
A's rule, clean labels 3 12 Ordinary
Plain NWD, clean labels (A's
principal comparator)
3 12 Ordinary
B anchored consistency 3 12 Two-view
B generic consistency 3 12 Two-view
AB combined (extension, first
to drop)
3 12 Two-view
One-seed controls: B random
subset of equal size (two-view),
country-balanced, strong
augmentation
1 12 Ordinary (random subset: two-
view)
Total 84 (72
without AB)
About 104 (86 without AB)
ordinary-run equivalents
Experiment Seeds Trainings Cost per run
A's rule, held-out noise family,
medium severity
3 12 Ordinary
Plain NWD, held-out noise family,
medium severity
3 12 Ordinary
Baseline on noisy boxes; matched
jitter
1 8 Ordinary
Design-family noise for A and plain
NWD
1 8 Ordinary
960 px baseline; B size-aware
weighting only
1 8 960 px about 2.25 × ordinary;
weighting ordinary
Extension total 48 About 53 ordinary-run
equivalents
Research Proposal: Cross-Country Road Damage Detection
Page 19 of 28

## Page 20
Default plus extension: 132 final trainings (about 157 ordinary-run equivalents), plus 20–30
development runs, so about 152–162 trainings; 168–178 with the 16 optional severity runs.
Estimate and schedule (assumptions until measured)
At roughly 10,700–16,100 training images per fold (70% of each fold's source pool) and 50
epochs, an ordinary YOLO11s run is assumed to take 3–9 GPU-hours, and a two-view run
about 1.5 times that. Both are guesses until the pilot; the two-view multiplier depends on
the training policy defined in the Methodology. Epochs are set from convergence on the
selection split.
Member C's compute is counted by fits. About 44 head fits before tuning: features plus
weak map, weak map only, features only (12 each across 4 folds and 3 seeds), plus about 8
on A and B. Pooled P3 and P4 features (40 × 40, fp16, about 1.2 MB per image) are cached
for the two training splits only, about 5 GB per detector and fold and about 60 GB in total.
Feature extraction takes under 0.1 GPU-hours per detector and fold, and heads train in
seconds per epoch, so C needs roughly 3–6 GPU-hours including tuning. These are
estimates until the pilot; computing features on the fly instead would cost an estimated
35–50 GPU-hours.
At 15–25 GPU-hours a week, weeks 7–27 supply roughly 300–525 hours. That covers only
the optimistic end of the default scope without AB: at 5 hours per ordinary run it already
needs about 560 hours with the allowance, before development. The noise extension
needs substantially more GPU time. Because the final phase alone cannot absorb this,
final runs start as each configuration is frozen (Methodology), not in one six-week block.
The plan relies on measured runtimes and hours actually committed, not on occasional
access.
Week-6 pilot and decision
On development data only, time one ordinary run and one two-view B run for YOLO11s,
and YOLO11n as the fallback (do not assume YOLO11n halves the time); time a 960 px run
only if the extension is in play. The pilot must also show finite losses, correct A and B
matching on a few hand-checked images, the Ultralytics candidate check, and resuming
from a checkpoint.
Scope Final training (GPU-hours) With 30% allowance
Default, without AB about 260–770 about 340–1,010
Default, with AB about 310–940 about 410–1,220
Default plus noise extension about 470–1,410 about 610–1,840
Research Proposal: Cross-Country Road Damage Detection
Page 20 of 28

## Page 21
Choose the scope from the measured numbers and the GPU hours actually
committed. For example, with 500 committed GPU-hours and 100 kept for
development, the default scope without AB fits only if an ordinary run takes about 3.5
hours or less (400 ÷ (86 × 1.3) ≈ 3.58).
Cut ladder, applied in this order when the pilot falls short: (1) drop the noise
extension and AB; (2) defer C's A and B secondary heads; (3) switch to YOLO11n for
every method; (4) reduce development screening to the minimum per fold and
method; (5) drop the country-balanced rival, but keep the strong-augmentation
reference and B's random-subset arm; (6) report resolution and augmentation
questions as exploratory only.
Never cut: a held-out country, the three seeds for principal contrasts, plain NWD for A,
or generic consistency for B.
Timeline and milestones
The plan fits about 34 weeks, with three gates before the expensive work starts. Official
module dates are not known yet; weeks count from the approved start.
Resource Need Where from
GPU Measured in week 6; at least 15–25
reliable hours a week
University GPU; Kaggle's free weekly
GPU quota; any extra capacity
confirmed in writing
Storage 10–25 GB Team's 1 TB storage
Software Python, PyTorch, Ultralytics (pinned
version and commit), scikit-learn
Free, open-source
Paid
services
None —
Research Proposal: Cross-Country Road Damage Detection
Page 21 of 28

## Page 22
If the week-6 pilot shows the grid will not fit the available GPU time, the cuts listed under
Resources and compute are applied before the member studies start, so no more than six
weeks of shared work is at risk.
Risks, ethics and fallbacks
The two biggest risks are novelty against MAMDG and GPU time; both are checked in the
first six weeks, before the member studies begin.
eight-month plan · 6 phases, 3 gates
Research Proposal: Cross-Country Road Damage Detection
Page 22 of 28

## Page 23
Risk Likelihood Early warning Fallback
MAMDG (read in part:
same setting, different
methods) or MSDA-
RDD reports one
member's analysis
Medium Full reading in weeks 1–
3
Narrow that member to
the part not reported,
and use the paper as a
baseline or reference
GPU time does not fit
the grid
High Pilot timing in week 6 Reduced scope by
default unless extra
GPU capacity is
confirmed; rolling final
runs
Leakage through
research decisions
Medium Any development step
that looks at a held-out
country
Inner validation country
for all development;
held-out countries
opened once after the
freeze
A's simulated noise
does not reflect real
annotation differences
High (by
design)
— Claim robustness to
simulated variation
only, never a share of
the real country gap
B's consistency
teaches both views to
miss cracks
Medium Small-box recall falls in
the consistency-only
ablation
EMA teacher, visibility
mask, and mask-
exclusion rates
reported; report the
failure if it persists
C's miss target too
common or too rare to
be informative
Medium Share of positive cells
and images measured
on one fold by week 8
Switch to a neural
image-level miss
predictor; the version 6
calibration study only
as a last resort
Methods give no
improvement
Medium Ablations by week 20 Report the pre-
registered answer;
compare against higher
resolution and baseline
variants
Research Proposal: Cross-Country Road Damage Detection
Page 23 of 28

## Page 24
Ethics and responsible use
No personal data is collected. RDD2022 images may show people, vehicles or number
plates; the demo shows only damage boxes, and images are not republished beyond
the licence.
CC BY-SA 4.0 requires attribution and share-alike for any released derived data.
Scores and miss warnings in the demo are described as estimates on benchmark data,
not guarantees. No claim that the system makes roads safer or replaces engineers.
Check against the module criteria
Nine gates pass at design level; four stay conditional until the closest papers are read, the
pilot is timed and the methods are implemented as specified.
Risk Likelihood Early warning Fallback
Only one member has
deep-learning
experience
High Weeks 1–6 Shared baseline built
together; each member
reproduces it before
starting their method
Gate Status Why
1. Real problem Pass Cross-country failure documented by the
dataset's authors and challenge reports
2. ML essential Pass Assignment, consistency training and
learned miss prediction are the research
3. Train or adapt models Pass All methods are trained or fitted; no paid API
4. Accessible dataset Pass RDD2022, CC BY-SA 4.0
5. No human studies Pass Existing labels only; no new photos
6. Precise gap Conditional Each contrast is bounded to the papers
examined; MAMDG shares the setting but
not the methods; its experiments and
MSDA-RDD still to be read
7. Beyond app assembly Pass Three trained or fitted interventions with
matched controls
8. Objective evaluation Pass Inner validation for development, held-out
countries opened once, fixed metrics
Research Proposal: Cross-Country Road Damage Detection
Page 24 of 28

## Page 25
Next steps (first three weeks)
References
Checked 29 October 2026. "Abstract only" means the full text has not yet been read by
the team; read these in full before relying on their details.
Dataset and challenges
Arya, D. et al. (2024). RDD2022: A multi-national image dataset for automatic road
damage detection. Geoscience Data Journal. Preprint: arXiv 2209.08538
sekilab/RoadDamageDetector, download links
Arya, D. et al. (2022). Crowdsensing-based Road Damage Detection Challenge
(CRDDC'2022)
Arya, D., Maeda, H. and Sekimoto, Y. (2025). Insights from the Road Damage Detection
Challenge series. Nature Machine Intelligence (abstract only)
Gate Status Why
9. 6–8 month feasibility Conditional Depends on the week-6 pilot; a reduced
scope is defined
10. Three connected
contributions
Pass One problem, three principal contrasts
11. No special hardware Conditional One modest GPU, but weekly hours may not
cover the full scope
12. Responsible use Pass Public data, no personal data, no safety
claims
13. Useful if no win Conditional Holds only if the controls run as specified,
so a negative result is interpretable
Write and commit the protocol: folds, data roles, principal contrasts, controls, metrics,
the 1.0-point clean-label margin
Read MAMDG's experiments section and MSDA-RDD in full; record which sections
were read; ask MAMDG's authors for code, since the repository has none
Inspect the pinned Ultralytics TAL code to confirm where A's rule and candidate
widening go
Download the four countries, convert labels, build duplicate groups and capture
sequences, count boxes per geometry bin
Take this proposal to the supervisor and agree the full or reduced scope after the
week-6 pilot
Research Proposal: Cross-Country Road Damage Detection
Page 25 of 28

## Page 26
Cross-country road damage
Chen et al. (2026). Multi-Adversarial Metric-Constrained Domain Generalization for
road damage detection. Image and Vision Computing (abstract, introduction and
section snippets read; repository contains no code)
MSDA-RDD: Multi-Source Domain Adaptation for Cross-Scene Road Damage
Detection. IEEE TCSVT, 2026 (we could not open the IEEE page; an external review
reports an accessible abstract; read it before citing)
Babawarun, Pandelani and Ngwangwa (2025). Investigation of the transferability of
measured data for application of YOLOv8s in the identification of road defects: an SA–
Indian case study. Sustainability
You and Jiang (2026). Self-supervised learning for road distress image recognition.
Traitement du Signal (page summary only)
Trinh, Anwar and Mercelis (2024). Multiple data sources and domain generalization
learning method for road surface defect classification. IEEE ITSC
Lin, C. et al. (2022/2023). DA-RDD: Toward domain adaptive road damage detection
across different countries. IEEE T-ITS
Xiao et al. (2026). Self-supervised visual prompting for cross-domain road damage
detection (PROBE). WACV
Trinh, L., Anwar, A. and Mercelis, S. (2024). Multiple data sources and domain
generalization learning method for road surface defect classification. IEEE ITSC
Arya, D. et al. (2020). Transfer learning-based road damage detection for multiple
countries
Assignment, small objects and noisy boxes (Member A and B)
Wang, J. et al. (2021). Normalized Wasserstein Distance for tiny object detection
Shi et al. (2024). Similarity distance-based label assignment for tiny object detection
(SimD). IROS
Le Jeune, P. and Mokraoui, A. (2025). Extension of intersection over union to improve
small object detection in few-shot regime. EUSIPCO (abstract only)
Issah and Mukamakuza (2026). CoSWA-YOLOv12: scale-invariant tiny object detection
and segmentation of malaria parasites. Preprint (abstract only)
Li et al. (2024). CrackTinyNet. IET Intelligent Transport Systems
Wu et al. (2023). Spatial self-distillation for object detection with inaccurate bounding
boxes. ICCV
Zhou et al. (2024). Distribution-aware calibration for object detection with noisy
bounding boxes. BMVC (abstract only)
Murrugarra-Llerena, J. and Jung, C. (2025). Noise-aware evaluation of object detectors.
WACV (abstract only)
Research Proposal: Cross-Country Road Damage Detection
Page 26 of 28

## Page 27
Danish et al. (2024), CVPR. Improving single domain-generalized object detection: a
focus on diversification and alignment (abstract only)
Guo et al. (2025). Scale-consistent and temporally ensembled UDA for object
detection. Sensors
Miss prediction and calibration (Member C)
Küppers, F. et al. (2020). Multivariate confidence calibration for object detection. CVPR
Workshops
Munir, M. A. et al. (2022). Towards improving calibration in object detection under
domain shift. NeurIPS
Kuzucu, S. et al. (2024). On calibration of object detectors: pitfalls, evaluation and
baselines. ECCV
Huseljic et al. (2024/2025). Systematic evaluation of uncertainty calibration in
pretrained object detectors. IJCV (abstract only)
Que et al. (2026). InsCal: calibrated multi-source fully test-time prompt tuning for
object detection. CVPR (abstract only)
Park, Sobolewski and Azizan (2024–2026). Uncertainty quantification in detection
transformers: object-level calibration and image-level reliability. Preprint (abstract
only)
Zimmermann, Holzbach and Lerch (2026). Knowledge-guided failure prediction:
detecting when object detectors miss safety-critical objects. CVPR Workshops
(SAIAD)
Yatbaz et al. (2024). Run-time introspection of 2D object detection in automated
driving systems using learning representations. IEEE Transactions on Intelligent
Vehicles 9(6), 2024
Rahman, Sünderhauf and Dayoub (2019). Did you miss the sign? A false negative alarm
system for traffic sign detectors. IROS
Rahman, Sünderhauf and Dayoub (2020). Online monitoring of object detection
performance during deployment. Preprint
Schubert, Kahl and Rottmann (2020). MetaDetect: uncertainty quantification and
prediction quality estimates for object detection. Preprint (venue not confirmed)
Keser and Knoll (2026). LFA: layer feature attention for run-time introspection of 2D
object detectors in automated driving. Preprint (abstract only)
Added in version 4
VALA: virtual anchor-guided label assignment for tiny object detection.
Neurocomputing, 2026 (not found by our searches; verify before citing)
YOLO-Crack: geometry-guided real-time crack detection framework toward edge
deployment. Sensors, 2026 (abstract only)
Research Proposal: Cross-Country Road Damage Detection
Page 27 of 28

## Page 28
Road damage detection using class-wise ensemble fusion and confidence
recalibration. Author repository; claimed CVIP 2026 acceptance unverified
Added in version 5
Shi, Fang and Xu (2026). Dynamic adaptive label assignment for tiny object detection in
remote sensing images. CAAI Transactions on Intelligence Technology 11(2), 428–446;
online November 2025 (abstract only)
Ultralytics 8.4.192 task-aligned assigner source, read 29 October 2026: sides below 8
px widened to 16 px in 8.4.0–8.4.127; sides below 16 px widened to 16 px from 8.4.128;
tag v8.4.192 is commit 922563e (tags read with git)
Sagawa, Koh, Hashimoto and Liang (2020). Distributionally robust neural networks for
group shifts. ICLR 2020 (venue from the authors' materials; abstract not re-read)
Tools: Ultralytics YOLO11, Ultralytics task-aligned assigner, Ultralytics loss implementation
Research Proposal: Cross-Country Road Damage Detection
Page 28 of 28

## Page 29
Literature review
This tab holds one current evidence table and a note on how each source was checked.
Earlier working notes from the search and verification rounds were removed in version 4;
they remain in the doc's version history.
Current evidence (version 4)
No verified paper duplicates the three principal contrasts; each technique has close
neighbours, so each member's claim rests on its own matched comparison. "Access" says
how much the team has read.
Paper What it does Relevance Access
Chen et al., MAMDG,
Image and Vision
Computing 2026
Domain
generalisation for
road-damage
detection with no
target data: multiple
domain
discriminators plus a
triplet loss,
CSPDarknet53
detector; RDD2022,
Cityscapes, Sim10k
Same setting as
ours, different
methods (feature
alignment); our A,
B and C act on
matching,
consistency and
miss prediction
Abstract,
introduction and
section snippets
read; experiments
not read; GitHub
repository has no
code
MSDA-RDD, IEEE
TCSVT 2026
YOLO11 with feature
alignment and
teacher–student
pseudo-labels
Adaptation setting
suggested by an
external review;
partitions
unverified
Not found by our
searches; verify on
IEEE Xplore before
citing
DA-RDD, IEEE T-ITS
2022/2023
Unsupervised
adaptation; Japan to
India mAP50 0.199 to
0.596 (RDD2020)
Shows the country
gap; uses target
images
Full text
PROBE, WACV 2026 Visual prompting
with unlabelled
target images; very
small cracks a stated
failure
Motivates B Full text
Literature review
Page 1 of 5

## Page 30
Paper What it does Relevance Access
Trinh et al., ITSC 2024 Leave-one-country-
out on RDD2022 for
crop classification;
drops boxes under
400 px²
Protocol
precedent; not
detection
Full text
Arya et al., 2020 Japan-only models:
class-wise F1 0.01–
0.05 on India
Shows the country
gap
Full text
RDD2022 data paper;
CRDDC'2022
Dataset counts;
challenge results by
country
Data and
motivation
Full text
NWD, 2021; SimD, IROS
2024; VALA,
Neurocomputing 2026
(not found by our
searches); CoSWA-
YOLOv12, 2026
preprint; scale-
adaptive IoU, EUSIPCO
2025
Size-aware similarity
and tiny-object
assignment, single
domain
A's mechanism is in
established
territory; A's claim
is the matched
transfer test
Abstract only
CrackTinyNet, IET ITS
2024
NWD for tiny road
cracks; mostly in-
domain with some
external tests
A and B neighbour Abstract only
SSD-Det, ICCV 2023;
DISCO, BMVC 2024;
Noise-Aware
Evaluation, WACV
2025
Training and
evaluation with
inaccurate boxes
A's noise study;
test labels kept
unchanged
Abstract only
Danish et al., CVPR
2024; Guo et al.,
Sensors 2025
Source-only cross-
view agreement
(Danish); scale
consistency with
target data (Guo)
B's consistency
principle is
established; B's
claim is anchored
vs generic
Danish abstract
only; Guo partly
read (results tables
not seen)
Literature review
Page 2 of 5

## Page 31
Paper What it does Relevance Access
YOLO-Crack, Sensors
2026
Real-time YOLO11n
crack detection
evaluated on
Crack500; an
external review
reports a cross-
dataset
generalisation
section (3.6) in the
full text, which we
could not open
Loose neighbour
for B (small
cracks), not a
transfer baseline
Abstract and
Sections 1–2 only
Küppers et al., 2020;
Munir et al., NeurIPS
2022; Kuzucu et al.,
ECCV 2024
Geometry-aware
calibration;
calibration under
shift; evaluation
pitfalls
Background for C's
supporting
calibration check
only (version 7)
Full text
Huseljic et al., IJCV
2024; InsCal, CVPR
2026; Park et al., 2024–
2026
Calibration under
distribution change;
multi-source
calibrated detection
with test-time
adaptation; object-
level calibration
counting missed
objects
C neighbours; ours
is frozen and
source-only
Abstract only
Literature review
Page 3 of 5

## Page 32
Still to do before submission: read MAMDG's experiments section and MSDA-RDD in full
and record which sections were read.
How claims were checked
The plan was revised seven times after critiques from another AI model acting as an
examiner. From version 5 on, a suggestion was only adopted after we checked it ourselves
with independent searches.
Confirmed by us: RDD2022 country counts and licence; the four-country sign-test
bound (p = 0.125); InsCal's CVPR listing; Danish et al. as CVPR 2024; the NWD constant
being dataset-dependent; DALA (CAAI TIT, online 2025); MAMDG's abstract and
introduction (source-only domain generalisation on RDD2022; its repository holds no
code); KGFP and the other failure-prediction papers cited for Member C.
Found by us, then corrected after review: Ultralytics widens small ground-truth box
sides when picking assignment candidates. External reviews twice flagged our version
history; reading every tagged release with git, 8.4.0–8.4.127 widen sides under 8 px to
Paper What it does Relevance Access
KGFP, CVPR
Workshops 2026;
Yatbaz et al., 2024;
Rahman et al., IROS
2019; Rahman et al.,
2020
Predict detector
misses from internal
features: per image
(people, KGFP), per
region (traffic signs),
per frame (driving);
spatial vs pooled
compared; cross-
dataset tests
C's method is
established,
including
comparing against
rejected
detections
(Rahman 2019) and
combining feature
levels (LFA, 2026
preprint); C's claim
is road damage, an
unseen country, a
dense small-or-
thin miss target,
and whether
features add to a
learned weak-map
model
KGFP, Yatbaz (IEEE
T-IV 2024) and
Rahman 2019 full
text; Rahman 2020
and LFA abstract
only
road-calib repository;
class-wise ensemble
and recalibration
repository
RDD2022 calibration,
single country or
unverified setting
C leads; not peer-
reviewed
README only
Literature review
Page 4 of 5

## Page 33
16 px, and 8.4.128 onwards (including the pinned 8.4.192, commit 922563e) widen sides
under 16 px to 16 px. Member A must pin that tag and report this.
Not confirmed: MAMDG's experiments and results; MSDA-RDD; VALA; DIFEDA
beyond its title; YOLO-Crack's cross-dataset section (the publisher page loads only to
Section 2 for us); the share of missed small or thin boxes that Member C's target will
have, which is estimated, not measured, until the week-8 gate. None of these is relied
on for a claim until read.
Literature review
Page 5 of 5

## Page 34
Step-by-step method
In short: build and tune everything without ever looking at the test country, freeze it, then
test once. Each member tries one change and compares it with one fair rival.
Words used here
Detector: a model that draws boxes around cracks and potholes.
Source countries: the three countries a fold learns from.
Held-out country: the fourth country, kept sealed until the very end.
Inner validation country: one of the three source countries, used as a stand-in test
country while you develop and tune. It is how you check ideas without touching the
real test country.
Small / thin box: a box under 32 × 32 pixels / a box whose shorter side is under 16 pixels,
measured at 640-pixel image size. These describe boxes, not the real crack.
Principal contrast: the one comparison each member's main claim rests on.
Calibrated: of all boxes the model scores 0.8, about 80% really are damage.
Missed damage: a crack the detector failed to box at its chosen threshold. Member C
predicts where these are likely.
Stage 1: Write the rules and prepare (weeks 1–3, whole team)
1 . Write the protocol and commit it to Git with a date. It lists the four folds, the data
roles, each member's principal contrast, controls and main measure, a decision table
(which choices are fixed for every fold and which are tuned inside each fold), the cut
ladder and a cap on tuning trials per fold and method.
2. Read MAMDG's experiments section and MSDA-RDD in full from the library.
MAMDG's abstract and introduction are already read: it shares our setting (no target
photos) but uses feature alignment, and its GitHub repository has no code. Note which
sections you read and what each already reports, and email MAMDG's authors asking
for code.
3. Download and convert Japan, India, United States and Czech Republic from the
RDD2022 GitHub page. Keep photos whose label file has no boxes as "no damage"
examples.
4. Group photos. Group near-identical photos (hashes and image similarity) and,
separately, photos from the same drive (sequence numbers in file names). Keep each
group on one side of every split.
Step-by-step method
Page 1 of 6

## Page 35
5. Split each fold into roles. Development: train on two source countries, tune on part of
them, check on the inner validation country (fixed per fold: Japan out → US; India out →
Czech Republic; US out → Japan; Czech Republic out → India). Final: train on all three
source countries, with small slices set aside for choosing checkpoints and for Member
C's miss predictor and the supporting calibration.
6. Count boxes per size group in the source data so everyone knows how many small and
thin boxes exist.
7. Look at YOLO11's assigner code (TAL) in the pinned Ultralytics release, tag v8.4.192
(commit 922563e), so Member A knows where the change goes. From 8.4.128 on (so
including 8.4.192) it widens box sides under 16 px to 16 px when picking candidates;
8.4.0–8.4.127 only widened sides under 8 px. Archive the installed code, keep this
setting identical for every method, and report it.
Stage 2: Shared baseline and pilot (weeks 4–6, whole team)
1 . Train the baseline on development data only: YOLO11s, COCO weights, 640 px.
2. Train two simple rivals: country-balanced sampling and stronger augmentation.
3. Time two runs: an ordinary run and a two-view run (Member B), plus a 960 px run only
if the extension is in play. Also check, on a few images, how many candidates TAL gives
boxes with 6, 12 and 20 px sides.
4. Decide the scope with the supervisor. The default scope (about 72–84 final runs, with
Member A's noise study left as an extension) is the plan, and it fits 500 GPU-hours only
if an ordinary run takes about 3.5 hours or less. The full scope with the noise study
(about 132 runs) only if extra GPU time is confirmed in writing. If the pilot falls short,
apply the cut ladder in order. Time YOLO11n too rather than assuming it is faster by a
set amount.
Nothing in this stage looks at a held-out country.
Stage 3: Each member develops their method (weeks 7–22,
development data only)
Member A: tolerate wobbly boxes
1 . Extension only (if GPU time allows): make noisy boxes. Two kinds, once, with a fixed
random seed: a design kind that moves and resizes boxes in proportion to their short
side, and a test kind with fixed-pixel moves plus stretching along the long side. Every
method would train on exactly the same noisy boxes. The default scope uses the
original labels only.
Step-by-step method
Page 2 of 6

## Page 36
2. Implement the rule. In YOLO11's assigner, replace the overlap score with NWD
measured relative to each box's short side. This is stricter on thin boxes in pixels, so
first plot how it compares with plain NWD. Plain NWD gets exactly the same rule for
which anchor points may be matched, so only the normalisation differs. Because this
score also sets the target weights, it changes both which predictions are positives and
how strongly they are trained: log positives per box, boxes with no positives, and total
target weight, by box size, for both rules.
3. Tune the tolerance ( κ ) and plain NWD's constant the same way: screen three values
of each on one fold with a short schedule, then confirm the best two on all four folds,
judged on each fold's inner validation country only. B tunes its loss weight the same
way, so development stays at about 20 runs.
4. Principal contrast: your rule versus plain NWD, both trained on the original RDD2022
labels, judged by held-out mAP50:95, overall and for small-or-thin boxes.
5. Also check: the baseline assigner as a control. The 1.0-point clean-label margin and the
noise robustness test belong to the extension.
Member B: catch small and thin damage
1 . Build the two-view training. The student trains normally on the full 640 px image,
exactly like the baseline, and also looks at a half-size copy. A separate slow-moving
(EMA) teacher sees the full-size image. The student at 640 px is the model you test.
2. Match predictions. For each small-or-thin labelled box, take the top three predictions
(by the assigner's score) in each view and average them; if a view has none, skip that
box and count it.
3. Add the agreement loss for those boxes only: a per-class yes/no (Bernoulli) KL on the
class scores plus an L1 difference between boxes, averaged over the boxes included.
Skip boxes too tiny to see in the half-size copy (under 8 px at full size), count them, and
report the baseline's recall on them: B does not train these directly.
4. Choose the loss weight on the inner validation country.
5. Principal contrast: the same agreement loss applied to all boxes (generic) versus only
small and thin ones (anchored), with identical views and training time.
6. Also check (one seed): the same loss on a random set of boxes of the same size as the
anchored set, to test whether choosing by geometry is what matters. Size weighting
alone and a 960 px model are extension-only.
7. Pick the operating threshold with the frozen rule: the highest recall on the source
selection split with at least 0.7 precision (ties go to the higher threshold), recomputed
for each final model. Always report held-out precision and false positives next to recall.
Count the anchored method as a success only if its false positives per image are no
more than 10% above the generic version's.
Step-by-step method
Page 3 of 6

## Page 37
Member C: predict where small damage was missed
1 . Make the labels. Run the frozen baseline detector on the two calibration slices (it
never trained on them) at its frozen threshold. Lay a 40 × 40 grid over each 640 px
image. Mark a cell when it holds the centre of a small or thin labelled crack that no
detection matched, using the normal one-to-one matching (same class, IoU of at least
0.5). Also count how often two missed cracks share a cell. Looser matching (IoU 0.3,
centre inside) is only a side check.
2. Check the labels first (week 8 gate). On one fold, count how many cells and images
are marked. If almost none or almost all are, switch to counting missed cracks per
image, or fall back to the version 6 calibration study.
3. Build the inputs. Take the detector's P3 and P4 feature maps and add one extra map
showing its own weak detections (scores between 0.05 and the threshold). Cache
them shrunk to 40 × 40 in fp16 for the two slices only (about 60 GB across all detectors
and folds).
4. Train a small head. Keep the detector frozen in evaluation mode. Shrink P3 to 40 × 40,
stack it with P4 and the weak map, then use a 1 × 1 convolution to 32 channels, two 3 × 3
convolutions and a 1 × 1 output with a sigmoid. Train with weighted binary cross-
entropy (positives are rare), AdamW and weight decay, no augmentation, and keep the
checkpoint with the best AUPRC on the second slice. Cache the shrunk features for
the two slices (about 60 GB in total) so training takes minutes.
5. Main comparison: your head on features plus the weak map vs the same head trained
on the weak map alone. That shows whether the detector's internal features add
anything beyond its own weak guesses. Also report the raw weak map and a features-
only head on the grid. Score image-level baselines (confidence statistics, pooled
features, logistic regression) only on the image-level task. Weak detections come from
one 0.05-floor pass after NMS, written as the maximum score at each box centre's cell.
6. Main measure: cell-level AUPRC on the held-out country, always with the share of
marked cells. Also report AUROC, recall at a fixed false-alarm rate, and correlation with
the number of missed cracks.
7. Run it on the baseline detector for every fold and seed, and on A and B for one seed, to
see whether misses get harder to predict as the detector improves.
8. Keep a small calibration check: simple temperature or Platt scaling of the detector's
scores, reporting Brier score on the held-out country. The demo uses it.
9. If the grid target fails the week-8 check, switch to a neural model that predicts
whether an image has any missed small or thin crack (tested on all images, including
those with none). Go back to the version 6 calibration study only as a last resort.
Shared evaluation code is team infrastructure, not part of C's research workload.
Step-by-step method
Page 4 of 6

## Page 38
Stage 4: Freeze, run the final grid, open the sealed countries (weeks
23–27)
1 . Freeze: freeze each configuration (code tag and settings file in Git) as soon as it is
ready and start its final runs then, from about week 10; everything is frozen by week
22.
2. Retrain every model in the final grid on all three source countries, three seeds for the
principal contrasts. Save held-out predictions without scoring or looking at them until
week 23.
3. Train a fresh miss predictor and calibration for every model, fold and seed that needs
one.
4. Open each held-out country once and compute the results.
5. Report per country, the four-country average and the worst country, with paired
bootstrap ranges that resample whole images (never Member C's grid cells): in each
resample, compute the difference for each seed, then average over seeds (never pool
predictions across seeds). One-seed controls are exploratory. No cross-country p-
values.
Stage 5: Build the demo (weeks 28–30)
1 . Export the final model to ONNX.
2. FastAPI service returning boxes, calibrated scores and Member C's missed-damage
heat map.
3. A simple web page using public RDD2022 test images; no new photos are collected.
Stage 6: Write up (weeks 31–34)
1 . One chapter per member: question, method, principal contrast, controls, result.
2. Shared chapters: data, protocol, baseline, final results, limits.
3. Limits stated plainly: four countries; any box noise is simulated; box size is not crack
size; benchmark results are not road-safety evidence.
If things go wrong
Not enough GPU time: YOLO11n, drop exploratory runs, then the reduced scope. Never
drop a held-out country.
A method does not beat its rival: report it; the comparison was fixed in advance, so the
question is still answered.
A 2026 paper already covers a study: narrow that member to what it does not report.
Step-by-step method
Page 5 of 6

## Page 39
You accidentally looked at a held-out country early: write it down, and label anything
decided afterwards as exploratory.
Step-by-step method
Page 6 of 6