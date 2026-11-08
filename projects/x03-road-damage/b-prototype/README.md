# B prototype: source-only small/thin consistency

Three fresh YOLO11s/COCO arms, 50 epochs each, seed42: supervised baseline, generic consistency, small/thin consistency. Ultralytics8.4.192, commit922563e. No A intervention/C head, no target pseudo-labels, no Japan access. Exact existing preparation manifest and COCO SHA256s are pinned in experiment.json.

The student is supervised only at640; its320 view receives Bernoulli teacher-to-student KL plus normalized-xyxy L1. The teacher is the existing stock FP32 EMA, eval/no-grad, updated by the normal optimizer-step hook. Full/half views derive from the same augmented tensor. Both consistency arms always execute the extra views, including empty batches. Matching uses stock detached TAL, final positive assignment, top3 by raw alignment with stable anchor-index ties, detached normalized alignment weights. Loss math/matching is FP32. Lambda ramps0->1 over the first5epochs. Stock three-component loss receives the auxiliary scalar exactly once before the trainer sums it.

Training geometry uses augmented normalized widths/heights at640; evaluation uses canonical original-image640 geometry. Small area<1024 or short side<16; visibility requires short side>=8. Potholes dominate the source subgroup; physical crack width is not measured by box width. Generic and focused differ only in selected GT subset; count-matched random/high-resolution controls and additional seeds/folds are deferred, so geometry-specific causation remains unresolved.

## Execution

`python build.py` embeds helper sources into private Kaggle notebooks. Stages: smoke -> baseline/generic/small-thin -> select -> evaluate. Inputs reuse x03-road-prepare and the initial COCO asset from x03-road-train, never its trained detector weights. All three checkpoints/thresholds are frozen by select before evaluate opens source-audit/US predictions. Source-selection rule is the existing precision>=.70 maximum-recall rule, best-F1 fallback. Every model is also scored at the fresh baseline threshold.

Smoke: shared enriched256 training images,64 selection images,2epochs per arm, intentional epoch0 interruption, optimizer/EMA/ramp recovery, inference export parity. Smoke keeps mosaic enabled to stress memory; full runs retain stock final-ten-epoch closure. Common batch16, then8 only if needed for all arms. Stock silent batch shrink is disabled; any unexpected per-arm change fails the run.

The budget gate uses warmed synchronized batch medians from the resumed epoch (first2 excluded), the measured old1.528h baseline,20% contingency, measured smoke hours and1h reserved for selection/evaluation. Stop before full training if estimate>12T4 hours. No silent shorter runs/model changes. Queue time is additional. Paid scaling must remain disabled.

Native resume checkpoints retain optimizer/EMA state on Kaggle and require b_core.py. Exported ARM-best.pt uses a stock DetectionModel, with unchanged EMA weights and verified prediction parity; evaluation does not need training hooks. Unpacked inputs are cleaned in finally; original preparation remains upstream. Predictions/logs compress for transfer. Local virtual environment and artifacts are ignored by Git. All substantive actions are logged in ../log.md; commits are local/project-scoped only.

The local controller holds an OS byte lock under artifacts/executor.lock for its lifetime. A second controller fails before any submission; the OS releases the lock after process exit. Reattach to existing work with --monitor. Windows sandbox process visibility differs by permission context, so a failed non-escalated PID lookup must not be treated as proof that an executor has exited. Source selection was accidentally submitted twice before this lock was added; both frozen configurations matched exactly, and the redundant stage is included in the resource accounting. Detector training ran once per arm.

## Local checks

Use .venv/Scripts/python.exe -m unittest discover -s . -p test_b_core.py. Local CPU environment reuses PyTorch2.12 and matching TorchVision0.27; actual Kaggle CUDA compatibility is tested again in smoke. Tests cover sigmoid KL, normalized boxes, top3 ties/empty matches, visibility/size boundaries, detached teacher/nonzero student gradients through TAL+DFL decode, auxiliary scaling and stock loss/gradient parity. This validates execution, not research efficacy.
