# Evaluate a three-student undergraduate FYP proposal: a model capable of multi-ve

**Question:** Evaluate a three-student undergraduate FYP proposal: a model capable of multi-vessel behaviour understanding from simultaneous AIS histories, with a reusable pretrained vessel or time-series encoder. Seek nearest primary work on multi-ship encounters (crossing/head-on/overtaking), behaviour recognition vs forecast vs intent, interaction-aware graph/Transformer models, dyads vs three or more ships, available public AIS datasets and labels with code/weights when supported. Consider whether one feasible gap is predicting which pair in a three-plus-ship scene will pass closest over the next 10 minutes, or encounter type and per-vessel maneuver, conditional on equal own-ship/pairwise baselines, disturbed neighbours and region shift. Identify nearest conflicting/duplicating work, discriminating tests, data/compute feasibility for 6–8 months and three connected student contributions. No from-scratch FM, private data or expert labelling. Report concrete, cited studies and avoid overclaiming intent, safety or novelty. Scope as of Nov 6 2026.

# Multi-Vessel **AIS Behavior Understanding** Proposal Evaluation

Multi-vessel behavior modeling from automatic identification system (AIS) data requires evaluating three distinct facets: existing multi-ship interaction paradigms, the formulation of feasible benchmark gaps under rigorous baseline conditions, and the execution division across an undergraduate timeline [[1.1]](https://consensus.app/papers/multiship-encounter-situation-graph-structure-learning-gao-liang/3d9e0ac4a05052a59673659a888b29e1/) [[2.1]](https://consensus.app/papers/a-deep-generative-model-for-multiship-trajectory-zhu-han/3c40629fc1745776a90e5dadc42ccfdc/) [[3.1]](https://consensus.app/papers/vessel-trajectory-prediction-based-on-ais-data-dualpath-huang-liu/ca964af9659959e28779d12060032387/).

| Feature | Primary Finding / Feasibility Benchmark |
| :--- | :--- |
| **Nearest Interaction Architectures** | Spatio-temporal graph convolutional networks (ST-GCN) [[1.2]](https://consensus.app/papers/multiship-encounter-situation-graph-structure-learning-gao-liang/3d9e0ac4a05052a59673659a888b29e1/) [[4.1]](https://consensus.app/papers/vessel-trajectory-prediction-based-on-spatiotemporal-wang-li/49a1a4db5a1a55269456272981af1ee2/) and dual-path/cross-modal Transformers [[5.1]](https://consensus.app/papers/cmivtp-crossmodal-interactionbased-vessel-trajectory-lu-yang/6727e679e65a526ea89079189a515cb5/) [[3.2]](https://consensus.app/papers/vessel-trajectory-prediction-based-on-ais-data-dualpath-huang-liu/ca964af9659959e28779d12060032387/). |
| **Typical Target Horizon** | 10 to 30 minutes for tactical collision risk and closest encounters [[6.1]](https://consensus.app/papers/an-aisbased-deep-learning-framework-for-regional-ship-murray-perera/b3ad816f638352258e69b9ab23b7a98b/) [[7.1]](https://consensus.app/papers/a-dual-linear-autoencoder-approach-for-vessel-trajectory-murray-perera/5272d664ffcb5db08d4ff95de47e5d49/). |
| **Scene Composition Scope** | Predominantly pairwise dyads [[1.3]](https://consensus.app/papers/multiship-encounter-situation-graph-structure-learning-gao-liang/3d9e0ac4a05052a59673659a888b29e1/) [[8.1]](https://consensus.app/papers/interactionaware-shortterm-marine-vessel-trajectory-han-zhu/70067f781e1c543b9007bca36cd5044e/); 3+ vessels handled via heuristics or hypergraphs [[1.4]](https://consensus.app/papers/multiship-encounter-situation-graph-structure-learning-gao-liang/3d9e0ac4a05052a59673659a888b29e1/) [[9.1]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/). |
| **Open Datasets with Code** | Danish Maritime Authority (DMA) [[10.1]](https://consensus.app/papers/aisllm-a-unified-framework-for-maritime-trajectory-park-jung/da5273f48edd5cf29d90cf1d7b59cec5/) [[11.1]](https://consensus.app/papers/deep-learning-methods-for-vessel-trajectory-prediction-capobianco-millefiori/015da91658725f988489125b0eb92fa1/), DI-MTP Zhoushan/Hainan [[9.2]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/) [[9.3]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/), CmIVTP [[5.2]](https://consensus.app/papers/cmivtp-crossmodal-interactionbased-vessel-trajectory-lu-yang/6727e679e65a526ea89079189a515cb5/) [[5.3]](https://consensus.app/papers/cmivtp-crossmodal-interactionbased-vessel-trajectory-lu-yang/6727e679e65a526ea89079189a515cb5/). |
| **Compute / Foundation Model Viability** | Pretrained frozen time-series encoders or CNN-Transformer blocks avoid training from scratch [[10.2]](https://consensus.app/papers/aisllm-a-unified-framework-for-maritime-trajectory-park-jung/da5273f48edd5cf29d90cf1d7b59cec5/) [[12.1]](https://consensus.app/papers/tptrans-vessel-trajectory-prediction-model-based-on-wang-xiong/8f9c13031f8e588e834a8ddaca6571b2/). |

**Figure 1:** Core structural parameters and architectural baselines for maritime interaction analysis

## Landscape of Encounter Modeling and Representations

A central challenge in maritime surveillance is distinguishing **pure trajectory forecasting** from semantic encounter categorization and navigation intent [[13.1]](https://consensus.app/papers/an-ais-datadriven-hybrid-approach-to-ship-trajectory-zhu-han/83ef2c2199c6540da281610fe6f54a3a/) [[9.4]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/) [[11.2]](https://consensus.app/papers/deep-learning-methods-for-vessel-trajectory-prediction-capobianco-millefiori/015da91658725f988489125b0eb92fa1/). Early deep learning approaches addressed regional vessel trajectories using recurrent encoder-decoder structures or autoencoders without dynamic multi-vessel interaction modules [[14.1]](https://consensus.app/papers/hybrid-deep-learning-models-for-ship-trajectory-liu-qi/e822b5d13d1d513f9594138afa188f93/) [[6.2]](https://consensus.app/papers/an-aisbased-deep-learning-framework-for-regional-ship-murray-perera/b3ad816f638352258e69b9ab23b7a98b/) [[7.2]](https://consensus.app/papers/a-dual-linear-autoencoder-approach-for-vessel-trajectory-murray-perera/5272d664ffcb5db08d4ff95de47e5d49/) [[11.3]](https://consensus.app/papers/deep-learning-methods-for-vessel-trajectory-prediction-capobianco-millefiori/015da91658725f988489125b0eb92fa1/). Modern frameworks explicitly represent multi-ship scenes as topological structures using graph neural networks or self-attention blocks [[1.4]](https://consensus.app/papers/multiship-encounter-situation-graph-structure-learning-gao-liang/3d9e0ac4a05052a59673659a888b29e1/) [[4.2]](https://consensus.app/papers/vessel-trajectory-prediction-based-on-spatiotemporal-wang-li/49a1a4db5a1a55269456272981af1ee2/) [[15.1]](https://consensus.app/papers/aisfuser-encoding-maritime-graphical-representations-zhang-yuan/826df251621f55ab885a829ea9ccef53/):

*   **Graph Convolutional Formulations:** Gao et al. developed ST-ENAGCN using node and edge attention to convert simultaneous AIS histories into encounter graphs [[1.2]](https://consensus.app/papers/multiship-encounter-situation-graph-structure-learning-gao-liang/3d9e0ac4a05052a59673659a888b29e1/), building on earlier topological network formulations [[16.1]](https://consensus.app/papers/multiship-encounter-situation-identification-and-zhu-gao/526964a56b6656e58234f52d7d3e97ab/) [[16]](https://consensus.app/papers/multiship-encounter-situation-identification-and-zhu-gao/526964a56b6656e58234f52d7d3e97ab/).
*   **Dual-Path and Multimodal Transformers:** DualSTMA decouples dynamic kinematics from static ship attributes via gated spatial interactions [[3.3]](https://consensus.app/papers/vessel-trajectory-prediction-based-on-ais-data-dualpath-huang-liu/ca964af9659959e28779d12060032387/), while CmIVTP and Env-GATrans employ cross-modal attention to combine AIS tracks with visual grids or star graphs [[5.4]](https://consensus.app/papers/cmivtp-crossmodal-interactionbased-vessel-trajectory-lu-yang/6727e679e65a526ea89079189a515cb5/) [[17.1]](https://consensus.app/papers/multisource-fusion-for-environment-and-interactionaware-wang-xiao/1c584df2402a528c8932da23d2e3ce56/).
*   **Generative Multimodal Forecasters:** Conditional variational autoencoders (CVAEs) map multi-vessel encounter dynamics into multi-modal distributions over future positions [[2.2]](https://consensus.app/papers/a-deep-generative-model-for-multiship-trajectory-zhu-han/3c40629fc1745776a90e5dadc42ccfdc/) [[8.2]](https://consensus.app/papers/interactionaware-shortterm-marine-vessel-trajectory-han-zhu/70067f781e1c543b9007bca36cd5044e/) [[9.5]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/).

**Figure 17.** Multi-ship encounter relationship graph based on the coordinates of vessels. Figure 17. Multi-ship encounter relationship graph based on the coordinates of vessels. [[16]](https://consensus.app/papers/multiship-encounter-situation-identification-and-zhu-gao/526964a56b6656e58234f52d7d3e97ab/)

*How to read: The diagram illustrates a multi-vessel interaction graph where spatial node coordinates and connecting edges depict instantaneous encounter relationships.*

Most historical datasets, such as the expert-annotated Oslofjord set, explicitly restrict analysis to two-ship interactions [[8.1]](https://consensus.app/papers/interactionaware-shortterm-marine-vessel-trajectory-han-zhu/70067f781e1c543b9007bca36cd5044e/) [[8.3]](https://consensus.app/papers/interactionaware-shortterm-marine-vessel-trajectory-han-zhu/70067f781e1c543b9007bca36cd5044e/). However, real-world waterways frequently involve three or more vessels converging simultaneously [[1.1]](https://consensus.app/papers/multiship-encounter-situation-graph-structure-learning-gao-liang/3d9e0ac4a05052a59673659a888b29e1/) [[9.1]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/).

## Benchmark Gap and Discriminating Evaluation Tests

Directly predicting the **closest point of approach** (CPA) or identifying the most critical pair within three-plus-ship scenes over a 10-minute horizon forms a concrete, uncrowded research gap [[16.2]](https://consensus.app/papers/multiship-encounter-situation-identification-and-zhu-gao/526964a56b6656e58234f52d7d3e97ab/) [[6.3]](https://consensus.app/papers/an-aisbased-deep-learning-framework-for-regional-ship-murray-perera/b3ad816f638352258e69b9ab23b7a98b/) [[7.1]](https://consensus.app/papers/a-dual-linear-autoencoder-approach-for-vessel-trajectory-murray-perera/5272d664ffcb5db08d4ff95de47e5d49/). Trajectory prediction methods often evaluate isolated displacement metrics (ADE/FDE) [[4.3]](https://consensus.app/papers/vessel-trajectory-prediction-based-on-spatiotemporal-wang-li/49a1a4db5a1a55269456272981af1ee2/) [[9.2]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/) [[17.2]](https://consensus.app/papers/multisource-fusion-for-environment-and-interactionaware-wang-xiao/1c584df2402a528c8932da23d2e3ce56/), masking whether the model genuinely understands inter-vessel avoidance or simply tracks regular traffic flows [[9.6]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/) [[6.4]](https://consensus.app/papers/an-aisbased-deep-learning-framework-for-regional-ship-murray-perera/b3ad816f638352258e69b9ab23b7a98b/). 

To prevent pseudo-interaction artifacts where models memorize regional channels, the FYP benchmark must mandate explicit controls [[6.5]](https://consensus.app/papers/an-aisbased-deep-learning-framework-for-regional-ship-murray-perera/b3ad816f638352258e69b9ab23b7a98b/) [[12.2]](https://consensus.app/papers/tptrans-vessel-trajectory-prediction-model-based-on-wang-xiong/8f9c13031f8e588e834a8ddaca6571b2/):

*   **Isolated Own-Ship Baselines:** Compare multi-agent models against independent single-vessel predictors such as S-TGP [[14.1]](https://consensus.app/papers/hybrid-deep-learning-models-for-ship-trajectory-liu-qi/e822b5d13d1d513f9594138afa188f93/), standard LSTMs [[18.1]](https://consensus.app/papers/vessel-navigation-behavior-analysis-and-ma-zuo/ff4477cdd23d5f769e01a459187b148c/), or univariate Transformers [[19.1]](https://consensus.app/papers/probabilistic-ship-trajectory-forecasting-using-schöller/2cd234ee75aa59de914a0ea3c1449b38/) [[12.3]](https://consensus.app/papers/tptrans-vessel-trajectory-prediction-model-based-on-wang-xiong/8f9c13031f8e588e834a8ddaca6571b2/).
*   **Pairwise Dyad Accumulators:** Baseline the system against models that sum independent pairwise encounter classifications without higher-order topology [[16.3]](https://consensus.app/papers/multiship-encounter-situation-identification-and-zhu-gao/526964a56b6656e58234f52d7d3e97ab/) [[16.4]](https://consensus.app/papers/multiship-encounter-situation-identification-and-zhu-gao/526964a56b6656e58234f52d7d3e97ab/).
*   **Disturbed Neighbor Invariance:** Test performance when irrelevant background vessels or non-interacting vessels are randomly dropped or injected into the encounter scene [[3.3]](https://consensus.app/papers/vessel-trajectory-prediction-based-on-ais-data-dualpath-huang-liu/ca964af9659959e28779d12060032387/) [[17.1]](https://consensus.app/papers/multisource-fusion-for-environment-and-interactionaware-wang-xiao/1c584df2402a528c8932da23d2e3ce56/).
*   **Geographic Region Shift:** Train on one public jurisdiction (e.g., DMA Danish waters) and evaluate zero-shot transfer on another (e.g., Zhoushan or Piraeus) to confirm transferability without local route memorization [[5.5]](https://consensus.app/papers/cmivtp-crossmodal-interactionbased-vessel-trajectory-lu-yang/6727e679e65a526ea89079189a515cb5/) [[10.1]](https://consensus.app/papers/aisllm-a-unified-framework-for-maritime-trajectory-park-jung/da5273f48edd5cf29d90cf1d7b59cec5/).

## Implementation Feasibility and Student Work Allocation

Developing a foundation model from scratch or performing proprietary human labeling is unfeasible for a 6–8 month undergraduate project [[8.3]](https://consensus.app/papers/interactionaware-shortterm-marine-vessel-trajectory-han-zhu/70067f781e1c543b9007bca36cd5044e/) [[11.4]](https://consensus.app/papers/deep-learning-methods-for-vessel-trajectory-prediction-capobianco-millefiori/015da91658725f988489125b0eb92fa1/). Instead, teams can leverage existing open datasets with public codebases, such as DI-MTP's repository for multi-vessel trajectories [[9.2]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/) [[9.3]](https://consensus.app/papers/unified-multimodal-vessel-trajectory-prediction-with-zhang-li/b5ebe828bb34575096f29f55538830ad/), CmIVTP's release [[5.3]](https://consensus.app/papers/cmivtp-crossmodal-interactionbased-vessel-trajectory-lu-yang/6727e679e65a526ea89079189a515cb5/), or public AIS feeds from the Danish Maritime Authority (DMA) [[10.1]](https://consensus.app/papers/aisllm-a-unified-framework-for-maritime-trajectory-park-jung/da5273f48edd5cf29d90cf1d7b59cec5/) [[11.1]](https://consensus.app/papers/deep-learning-methods-for-vessel-trajectory-prediction-capobianco-millefiori/015da91658725f988489125b0eb92fa1/). Reusable time-series backbones or temporal convolution layers can be adapted directly to encode sequential dynamics efficiently [[10.3]](https://consensus.app/papers/aisllm-a-unified-framework-for-maritime-trajectory-park-jung/da5273f48edd5cf29d90cf1d7b59cec5/) [[20.1]](https://consensus.app/papers/trajectory-prediction-of-seagoing-ships-in-dynamic-liu-gong/98a691597b755bbbabfe0c33980be35f/) [[12.1]](https://consensus.app/papers/tptrans-vessel-trajectory-prediction-model-based-on-wang-xiong/8f9c13031f8e588e834a8ddaca6571b2/).

| Student | Core Functional Role | Technical Deliverables & Experimental Scope |
| :--- | :--- | :--- |
| **Student 1** | **Data Engineering & Extraction** | Curates multi-vessel encounter scenarios from DMA or open AIS sets [[8.4]](https://consensus.app/papers/interactionaware-shortterm-marine-vessel-trajectory-han-zhu/70067f781e1c543b9007bca36cd5044e/) [[11.1]](https://consensus.app/papers/deep-learning-methods-for-vessel-trajectory-prediction-capobianco-millefiori/015da91658725f988489125b0eb92fa1/) using geometric COLREGS encounter filters [[1.3]](https://consensus.app/papers/multiship-encounter-situation-graph-structure-learning-gao-liang/3d9e0ac4a05052a59673659a888b29e1/) [[13.2]](https://consensus.app/papers/an-ais-datadriven-hybrid-approach-to-ship-trajectory-zhu-han/83ef2c2199c6540da281610fe6f54a3a/). |
| **Student 2** | **Encoder & Graph Architecture** | Implements temporal embeddings via CNN-Transformers [[20.2]](https://consensus.app/papers/trajectory-prediction-of-seagoing-ships-in-dynamic-liu-gong/98a691597b755bbbabfe0c33980be35f/) [[12.1]](https://consensus.app/papers/tptrans-vessel-trajectory-prediction-model-based-on-wang-xiong/8f9c13031f8e588e834a8ddaca6571b2/) and constructs dynamic attention graphs over active ships [[1.2]](https://consensus.app/papers/multiship-encounter-situation-graph-structure-learning-gao-liang/3d9e0ac4a05052a59673659a888b29e1/) [[4.2]](https://consensus.app/papers/vessel-trajectory-prediction-based-on-spatiotemporal-wang-li/49a1a4db5a1a55269456272981af1ee2/). |
| **Student 3** | **Benchmarking & Robustness** | Evaluates 10-minute closest-pair prediction and maneuver classification under region shifts and neighbor perturbations [[14.2]](https://consensus.app/papers/hybrid-deep-learning-models-for-ship-trajectory-liu-qi/e822b5d13d1d513f9594138afa188f93/) [[10.1]](https://consensus.app/papers/aisllm-a-unified-framework-for-maritime-trajectory-park-jung/da5273f48edd5cf29d90cf1d7b59cec5/) [[6.1]](https://consensus.app/papers/an-aisbased-deep-learning-framework-for-regional-ship-murray-perera/b3ad816f638352258e69b9ab23b7a98b/). |

**Figure 2:** Three-student division of responsibilities across data extraction, architecture design, and robustness benchmarking

This division ensures that each student maintains clear ownership of an interdependent module while strictly staying within public data bounds and sustainable GPU compute constraints [[14.3]](https://consensus.app/papers/hybrid-deep-learning-models-for-ship-trajectory-liu-qi/e822b5d13d1d513f9594138afa188f93/) [[10.4]](https://consensus.app/papers/aisllm-a-unified-framework-for-maritime-trajectory-park-jung/da5273f48edd5cf29d90cf1d7b59cec5/).
 
_These search results were found and analyzed using Consensus, an AI-powered search engine for research. Try it at https://consensus.app. © 2026 Consensus NLP, Inc. Personal, non-commercial use only; redistribution requires copyright holders’ consent._
 
## References
 
`1.` Gao M, Liang M, Zhang A, Hu Y, Zhu J. Multi-ship encounter situation graph structure learning for ship collision avoidance based on AIS big data with spatio-temporal edge and node attention graph convolutional networks. *Ocean Engineering.* 2024. doi:10.1016/j.oceaneng.2024.117605
 
> [1.1] With the increasing number of ships on the sea, the frequency multi-ship encounters situation was becoming more common than two-ship encounter. (Abstract)
 
> [1.2] (4) Finally, a spatial-temporal edge and node attention graph convolutional network (ST-ENAGCN) was proposed with the graph convolutional unit and long short-term memory (LSTM) unit. (Abstract)
 
> [1.3] (1) The ship encounter 8-azimuths map was utilized to identify the two-ship encounter situation (25 types) from the AIS data. (Abstract)
 
> [1.4] (3) To handle the intricate relationship information between the multiple ships which were transformed into a graph structure using graph theory. (Abstract)
 
`2.` Zhu M, Han P, Tian W, Skulstad R, Zhang H, Li G. A Deep Generative Model for Multi-Ship Trajectory Forecasting with Interaction Modelling. *Journal of Offshore Mechanics and Arctic Engineering.* 2024. doi:10.1115/1.4065866
 
> [2.1] Multi-agent modeling is a challenging issue in intelligent systems, which is further compounded by heavy and complex traffic in maritime contexts. (Abstract)
 
> [2.2] Towards this end, we propose a conditional variational autoencoder approach to ship trajectory prediction in a dynamic and multi-modal encounter situation. (Abstract)
 
`3.` Huang F, Liu Z, Li X, Mou F, Li P, Fan Z. Vessel Trajectory Prediction Based on AIS Data: Dual-Path Spatial–Temporal Attention Network with Multi-Attribute Information. *Journal of Marine Science and Engineering.* 2024. doi:10.3390/jmse12112031
 
> [3.1] To address these issues, this paper proposes a dual spacial-temporal attention network with multi-attribute information (DualSTMA). (Abstract)
 
> [3.2] The main contributions of this paper are as follows: - Wedesign a dual-path spacial-temporal attention encoder that models both individual vessel behavior and inter-vessel interactions. (Introduction)
 
> [3.3] Moreover, we divide vessel attributes into dynamic and static categories, with dynamic attributes fused during feature preprocessing, and with static attributes being controlled through a gating mechanism during spatial interactions to regulate the importance of neighboring vessel features. (Abstract)
 
`4.` Wang S, Li Y, Xing H, Zhang Z. Vessel trajectory prediction based on spatio-temporal graph convolutional network for complex and crowded sea areas. *Ocean Engineering.* 2024. doi:10.1016/j.oceaneng.2024.117232
 
> [4.1] The spatial social interaction features are extracted by ST-GCN, and the temporal correlation are extracted by RT-CNN, to obtain the high-level spatio-temporal features of vessel trajectories. (Abstract)
 
> [4.2] The LSTM is used to extract the motion features of vessels, the spatio-temporal graph is constructed based on deep attention mechanism. (Abstract)
 
> [4.3] On the basis of a large number of experiments, the prediction performance of the DAA-SGCN compared to the optimal baseline model is improved by about 74% and 69% in ADE and FDE metrics. (Abstract)
 
`5.` Lu Y, Yang D, Li X, Bao M, Zhao C. CmIVTP: Cross-Modal Interaction-Based Vessel Trajectory Prediction for Maritime Intelligence. *IEEE Transactions on Intelligent Transportation Systems.* 2026;27:13445-13460. doi:10.1109/tits.2026.3703388
 
> [5.1] It leverages cross-modal attention mechanisms to simultaneously capture intra-modal semantics and inter-modal interactions, ensuring dynamically consistent and environmentally feasible predictions. (Abstract)
 
> [5.2] Additionally, we introduce the maritime multimodal dataset plus (named Maritime-MmD+), a large-scale dataset that synchronizes AIS data and CCTV video data, providing robust support for multimodal trajectory prediction research. (Abstract)
 
> [5.3] The code resources for this work can be available at https://github.com/LouisYxLu/CmIVTP (Abstract)
 
> [5.4] Distinct from existing unimodal paradigms, our framework overcomes these limitations by integrating multimodal information from AIS data and CCTV video, enabling environmentally consistent and uncertainty-aware modeling of vessel behaviors. (Methods)
 
> [5.5] To address this, we will explore transfer learning by pre-training on abundant AIS data to capture universal motion priors, followed by fine-tuning with limited multimodal data. (Discussion)
 
`6.` Murray B, Perera LP. An AIS-based deep learning framework for regional ship behavior prediction. *Reliab. Eng. Syst. Saf..* 2021;215:107819. doi:10.1016/j.ress.2021.107819
 
> [6.1] As such, this study investigates predicting the future 30 min trajectory of a selected vessel. (Introduction)
 
> [6.2] Utilizing historical AIS data, the framework is successful in clustering historical ship behavior using a variational recurrent autoencoder. (Conclusion)
 
> [6.3] To facilitate this, global scale trajectory predictions, i.e. order 5-30 min, should be conducted. (Conclusion)
 
> [6.4] It is, therefore, assumed that future ship behavior can be predicted based on the historical behavior of other vessels in a given geographical region. (Introduction)
 
> [6.5] To facilitate this, the data for a specific geographical region are used to generate a prediction model for ship behavior within this region. (Introduction)
 
`7.` Murray B, Perera LP. A dual linear autoencoder approach for vessel trajectory prediction using historical AIS data. *Ocean Engineering.* 2020. doi:10.1016/j.oceaneng.2020.107478
 
> [7.1] On the global scale however, long term trajectory predictions, on the scale of 5-30 min, are conducted. (Introduction)
 
> [7.2] Using unsupervised learning to facilitate trajectory clustering and classification, the method utilizes a cluster of historical AIS trajectories to predict the trajectory of a selected vessel. (Abstract)
 
`8.` Han P, Zhu M, Zhang H. Interaction-Aware Short-Term Marine Vessel Trajectory Prediction With Deep Generative Models. *IEEE Transactions on Industrial Informatics.* 2024;20:3188-3196. doi:10.1109/tii.2023.3302304
 
> [8.1] Experiments are performed in two-vessel encounter scenarios from real-world automatic identification system data. (Abstract)
 
> [8.2] In this article, we propose a deep generative model based on the conditional variational autoencoder framework to learn marine vessel movement and predict future trajectories. (Abstract)
 
> [8.3] Although more ships can be involved in an encounter and relatively large datasets can be easily collected since the AIS data are publicly available, we only focus on this small dataset with two-ship interactions because it is labeled and reviewed by experts. (Methods)
 
> [8.4] The goal is to make future trajectory predictions for ferries only since the dataset only contains ferries from Horten to Moss and merchant ships from bottom to top (see Fig. 3). (Methods)
 
`9.` Zhang R, Li C, Liu K, Wang C, Zheng B, Jiang H. Unified Multimodal Vessel Trajectory Prediction With Explainable Navigation Intention. *IEEE Transactions on Intelligent Transportation Systems.* 2025;27:258-269. doi:10.1109/tits.2025.3635392
 
> [9.1] (b) shows predictions for two-vessel and three-vessel encounter scenarios, respectively, showing optimal predictions in each case. (Results)
 
> [9.2] - 3) Extensive evaluation on real AIS datasets demonstrating significant improvements over state-of-the-art methods: 18.28% in ADE and 8.51% in FDE within the Zhoushan dataset and 27.48% in ADE and 27.40% in FDE within the Hainan dataset. (Introduction)
 
> [9.3] The code of DI-MTP is available at: https://github.com/EurusC/DI-MTP. (Introduction)
 
> [9.4] - 2) We propose an explainable framework leveraging attention-based intention trees to provide modal probabilities for multiple predictions, enabling explainability through distinct sustained intention prototypes. (Introduction)
 
> [9.5] Our method constructs sustained intention trees from historical trajectories and models dynamic transient intentions using a Conditional Variational Autoencoder (CVAE), while using a non-local attention mechanism to maintain global scenario consistency. (Abstract)
 
> [9.6] (a) Deterministic prediction generates a single fixed trajectory, emphasizing route selection while disregarding vessel encounters. (Introduction)
 
`10.` Park H, Jung J, Seo M, et al. AIS-LLM: A Unified Framework for Maritime Trajectory Prediction, Anomaly Detection, and Collision Risk Assessment With Explainable Forecasting. *IEEE Access.* 2025;14:106874-106891. doi:10.1109/access.2026.3705215
 
> [10.1] Extensive experiments on the Piraeus and DMA datasets demonstrate that AIS-LLM consistently outperforms state-of-the-art baselines across all tasks, achieving improvements of approximately 10.4% (Piraeus) and 5.8% (DMA) in trajectory prediction (ADE), 10.4% in anomaly detection (F1-score), and 10.0% in collision risk assessment (MAE) compared to the best-performing single-task models. (Abstract)
 
> [10.2] Shared spatio-temporal representations are learned through a Multi-Scale Temporal Attention mechanism with scales of [1, 4, 16, 32], combined with a Cross-Modal Alignment module. (Methods)
 
> [10.3] An Inverted Embedding approach is used to learn independent temporal patterns for each AIS variable (latitude, longitude, speed over ground, and course over ground), which are shared across all tasks to improve learning efficiency and parameter utilization. (Methods)
 
> [10.4] Parameters of the large language model (LLM) remain frozen using pretrained weights. (Methods)
 
`11.` Capobianco S, Millefiori LM, Forti N, Braca P, Willett P. Deep Learning Methods for Vessel Trajectory Prediction Based on Recurrent Neural Networks. *IEEE Transactions on Aerospace and Electronic Systems.* 2021;57:4329-4346. doi:10.1109/taes.2021.3096873
 
> [11.1] Experimental results on vessel trajectories from an AIS dataset made freely available by the Danish Maritime Authority (DMA) show the effectiveness of deep learning methods for trajectory prediction based on sequence-to-sequence neural networks, which achieve better performance than baseline approaches based on linear regression or on the multilayer perceptron architecture. (Abstract)
 
> [11.2] Moreover, we investigate here the use of several intermediate aggregation layers (including, but not limited to, the attention mechanism) and the exploitation of high-level intention information (i.e., ship destination). (Introduction)
 
> [11.3] Inspired by the recent success of deep-learning approaches for sequence-to-sequence applications, the proposed method is based on the LSTM encoder-decoder architecture, which has emerged as an effective and scalable model for sequence-tosequence learning. (Introduction)
 
> [11.4] This is not only because of AIS technological limitations, such as the highly irregular time sampling, poor data quality and integrity, but also because the variety of behaviors exhibited by ships (depending on, e.g., their size, navigational status, traffic regulations, etc.). (Introduction)
 
`12.` Wang W, Xiong W, Ouyang X, Chen L. TPTrans: Vessel Trajectory Prediction Model Based on Transformer Using AIS Data. *ISPRS Int. J. Geo Inf..* 2024;13:400. doi:10.3390/ijgi13110400
 
> [12.1] Secondly, we combine convolutional layers with the transformer structure, using convolutional neural networks to extract local spatiotemporal features in sequences. (Abstract)
 
> [12.2] The application of deep learning methods in vessel trajectory prediction is becoming more and more widespread; however, due to the complexity of the marine environment, including the influence of geographical environmental factors, weather factors, and real-time traffic conditions, predicting trajectories in less constrained maritime areas is more challenging than in path network conditions. (Abstract)
 
> [12.3] This study introduces an innovative model based on the transformer structure to predict the trajectory of a vessel. (Abstract)
 
`13.` Zhu M, Han P, Wang C, Skulstad R, Zhang H, Li G. An AIS Data-Driven Hybrid Approach to Ship Trajectory Prediction. *IEEE Transactions on Systems, Man, and Cybernetics: Systems.* 2025;55:96-109. doi:10.1109/tsmc.2024.3458469
 
> [13.1] In response, this article introduces a novel approach, driven by automatic identification system (AIS) data, to enhance the efficacy of ship encounter trajectory prediction. (Abstract)
 
> [13.2] It revolves around encounter classification, wherein the invaluable insights of seamanship play a pivotal role in identifying and categorizing legitimate encounters into three distinct types. (Abstract)
 
`14.` Liu Z, Qi W, Zhou S, et al. Hybrid deep learning models for ship trajectory prediction in complex scenarios based on AIS data. *Applied Ocean Research.* 2024. doi:10.1016/j.apor.2024.104231
 
> [14.1] (1) the S-TGP model, combining Time Convolutional Network (TCN) and Gated Recurrent Unit (GRU) for single-ship trajectory with high accuracy and high generalization. (Abstract)
 
> [14.2] Validated on AIS data from three regions, our models demonstrate superior performance and robustness compared to existing methods. (Abstract)
 
> [14.3] Our contributions include: (1) enhancing the accuracy of single-ship trajectory prediction with the S-TGP model; (2) improving collaborative prediction capabilities for multiple ships with the MVS-TGP model; and (3) providing real-time prediction and monitoring capabilities for maritime surveillance. (Abstract)
 
`15.` Zhang Z, Yuan W, Fan Z, Song X, Shibasaki R. AISFuser: Encoding Maritime Graphical Representations With Temporal Attribute Modeling for Vessel Trajectory Prediction. *IEEE Transactions on Knowledge and Data Engineering.* 2025;37:1571-1584. doi:10.1109/tkde.2025.3531770
 
> [15.1] Specifically, our AISFuser is constructed by combining an attention-based graph block with a transformer network to encode information across space and time, respectively. (Abstract)
 
`16.` Zhu J, Gao M, Zhang A, Hu Y, Zeng X. Multi-Ship Encounter Situation Identification and Analysis Based on AIS Data and Graph Complex Network Theory. *Journal of Marine Science and Engineering.* 2022. doi:10.3390/jmse10101536
 
> [16.1] Pairwise encounters identification results and ship motion index were combined into a ship encounter graph network which can use the complex network theory to describe the encounter spatial-temporal process. (Abstract)
 
> [16.2] Quaternary dynamic ship domain, fuzzy logic and the weighted PageRank algorithm were used to rank the whole network risk, which is critical to 'key ship collision avoidance.' (Abstract)
 
> [16.3] Based on the recognition results of pairwise encounter identification results, a discrete multi-ship encounter network is constructed. (Abstract)
 
> [16.4] However, this approach is mainly based on pairwise encounter situations and does not consider the effect of the ship avoidance action on nearby ships. (Methods)
 
`17.` Wang Y, Xiao X. Multi-source fusion for environment- and interaction-aware ship trajectory prediction. *Ships and Offshore Structures.* 2026. doi:10.1080/17445302.2026.2741334
 
> [17.1] We propose Env-GATrans, which fuses target-vessel motion, a local navigation grid, and an ego-centered star interaction graph. (Abstract)
 
> [17.2] Across short-, medium-, and long-horizon tasks, Env-GATrans outperforms LSTM, Transformer, SNIINet, and an RNN Fusion + Surface Current baseline, reducing ADE and FDE by 7.80%–26.86%. (Abstract)
 
`18.`  H, Zuo Y, Li T. Vessel Navigation Behavior Analysis and Multiple‐Trajectory Prediction Model Based on AIS Data. *Journal of Advanced Transportation.* 2022;2022. doi:10.1155/2022/6622862
 
> [18.1] Second, we design an integrated model for simultaneous prediction of multiple trajectories using the proposed features and employ the long short‐term memory (LSTM)‐based neural network and recurrent neural network (RNN) to pursue this time series task. (Abstract)
 
`19.` Schöller FET. Probabilistic Ship Trajectory Forecasting using Transformer Models on AIS Data. 2026. doi:10.48550/arxiv.2610.13557
 
> [19.1] This paper investigates Transformer and Performer models for trajectory prediction of surface vessels in confined waters. (Abstract)
 
`20.` Liu J, Gong P, Chen C, Han B, Wu Z. Trajectory prediction of seagoing ships in dynamic traffic scenes via a gated spatio-temporal graph aggregation network. *Ocean Engineering.* 2023. doi:10.1016/j.oceaneng.2023.115886
 
> [20.1] Ultimately, the spatial and temporal features obtained from the SSGE and STGE modules, respectively, are aggregated through a temporal convolutional network (TCN) to perform downstream trajectory prediction tasks. (Abstract)
 
> [20.2] Firstly, a ship spatial gating encoder (SSGE) combines graph convolutional networks (GCN) and transformers to simulate dynamic and static spatial interactions , thereby improving prediction performance. (Abstract)
