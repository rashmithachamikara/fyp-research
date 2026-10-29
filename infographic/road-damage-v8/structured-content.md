# Road damage, beyond borders

Can a model trained elsewhere detect small or thin road damage?

## The challenge
New country: different roads, cameras and lighting.

## The experiment
Train on 3 countries -> Freeze settings -> Test on the 4th.
Japan / India / United States / Czech Republic.
Repeat four times. No target-country data for training or tuning.
Public dataset: RDD2022. Shared detector: YOLO11.

## A: Match thin boxes differently
Change how training predictions are matched and weighted, using error relative to the box's short side.
Train: modified YOLO.
Compare: plain NWD.
Measure: detection accuracy (mAP).

## B: Learn across image scales
Show the same image at two scales. Encourage agreement on visible small or thin damage.
Train: YOLO with a consistency loss.
Compare: consistency on all eligible boxes.
Measure: recall plus false positives.

## C: Warn about likely misses
Freeze YOLO. Train a small CNN using internal features and weak detections to predict a 40 x 40 warning grid.
Train: separate CNN head.
Compare: learned weak-map-only head.
Measure: miss-location AUPRC.
Warnings do not recover missed cracks.

## What makes the test fair?
3 seeds / matched controls / ablations / untouched test countries.
All three train neural models. Each has its own research question.
Proposed studies: improvements are not yet demonstrated.
