# Source

Based on the beginner explanation in this chat and the proposed framework discussed in Small_Boat_Behaviour_Review_v3.pdf.

The proposal asks: Can we teach a computer about boat movements using AIS records, then have it recognise those movements from radar observations?

Use real AIS trajectories and rules to define movement labels. Compare clean-AIS training, synthetic degradation of AIS coordinates and timestamps, and domain adaptation using real unlabelled radar tracks. Test on held-out real radar tracks, using paired AIS observations as the reference for evaluation only. Compare against direct movement rules. Study confidence and abstention. The output is behaviour and confidence, not illegality. Evaluation covers AIS-equipped vessels with AIS withheld during inference.

