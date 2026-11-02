<div align="center">
<img src="assets/ascii-portrait.svg" alt="Animated terminal: Ajinkya Awari, MSc AI for Biomedicine and Healthcare at UCL. I build ML systems that tell you when they are wrong." width="100%" />
</div>

<div align="center">
<img src="assets/info-card.svg" alt="20 public repos, 7 with real results, 81 tests with CI green on the flagship benchmark, 3 negative results published on purpose" width="100%" />
</div>

<div align="center">

[**GitHub**](https://github.com/ajinkya-awari) · [**Hugging Face**](https://huggingface.co/ajinkya1807) · [**Kaggle**](https://www.kaggle.com/ajinkya1225) · [**Email**](mailto:ajinkya18072001@gmail.com)

</div>

<sub>**The seven with real results:** [AIXI-Complexity](https://github.com/ajinkya-awari/aixi-complexity-benchmark) · [FedScope](https://github.com/ajinkya-awari/fedscope) · [GraphGPS-Upgrade](https://github.com/ajinkya-awari/graphgps-upgrade) · [ESM2-Protein-Fitness](https://github.com/ajinkya-awari/esm2-protein-fitness) · [AFBind](https://github.com/ajinkya-awari/afbind) · [F2-HistoGNN](https://github.com/ajinkya-awari/f2-histognn) · [SolomonoffBench](https://github.com/ajinkya-awari/solomonoff-bench). **The three negative results** are in the ledger below, marked 🟡 and ⛔.</sub>

---

## The thesis

Most ML portfolios show what worked. Mine shows what was **measured**, including the runs that came back near chance. Every project here starts with leakage-safe splits, frozen budgets and a synthetic test layer, and only touches real data once access, licence and privacy gates are cleared. If a result is weak, the README says so in the first screen.

I'm an incoming **MSc Artificial Intelligence for Biomedicine and Healthcare** student at **UCL**, working on reliable learning systems for biomedical problems: protein ML, graph learning, federated and private learning, evaluation and interpretability.

## The journey

<div align="center">
<img src="assets/journey.svg" alt="Three scenes: the failure (frozen BatchNorm collapsed accuracy, found and published in 2023), the build (20 gated projects), the ask (real-model research)" width="100%" />
</div>

---

## Case file: the evidence ledger

Status key: ✅ verified result · 🟡 measured, weak or partial · ⛔ documented gap

| Project | What was measured | Status |
| --- | --- | :---: |
| [**AIXI-Complexity**](https://github.com/ajinkya-awari/aixi-complexity-benchmark) | 5 agent types on 20 frozen finite-state tasks. 81 tests, CI green. No difficulty proxy stays significant after Holm correction (min adjusted p = 0.144). | ✅ |
| [**FedScope**](https://github.com/ajinkya-awari/fedscope) | FedAvg, FedProx and FedNova against a centralized baseline. F1 0.78–0.80 over 3 seeds. | ✅ |
| [**GraphGPS-Upgrade**](https://github.com/ajinkya-awari/graphgps-upgrade) | Frozen 30-epoch budget on a Tesla T4. Test ROC-AUC: GPS 0.748, GIN 0.698, GCN 0.693 (3 seeds). | ✅ |
| [**ESM2-Protein-Fitness**](https://github.com/ajinkya-awari/esm2-protein-fitness) | Protein mutation fitness from ESM2 embeddings. 87/87 tests, Kaggle kernel run complete. | ✅ |
| [**PrivacyFL-DP**](https://github.com/ajinkya-awari/privacyfl-dp) | Real NIH ChestX-ray14, 5 federated clients, Opacus. 1 of 6 privacy levels run so far: measured ε = 0.096, macro-AUC 0.497, which is chance. Reported as is. | 🟡 |
| [**KnetMiner-LLM**](https://github.com/ajinkya-awari/knetminer-llm) | Evidence-grounded biomedical graph retrieval. Release engineering complete, but strict per-answer acceptance is **0/30**. [Live demo](https://ajinkya-awari.github.io/knetminer-llm/demo/). | ⛔ |

---

## All 21 projects, 00 to 20

### Reliable ML and MLOps

| # | Project | What it is | Status |
| ---: | --- | --- | --- |
| 00 | [SolomonoffBench](https://github.com/ajinkya-awari/solomonoff-bench) | Do LLMs compress like optimal predictors? Complexity-vs-compression benchmark. | ✅ Closed, with limitations |
| 01 | [T1 MLOps Stack](https://github.com/ajinkya-awari/t1-mlops-stack) | Training pipeline, experiment tracking and a deployed inference app. | 🟡 Complete with limitations |
| 02 | [T2 XAI Triple](https://github.com/ajinkya-awari/xai-medical-imaging-project-02) | Grad-CAM, SHAP and Integrated Gradients on NIH ChestX-ray14 (mean IoU 0.1289). | 🟡 Complete with limitations |
| 03 | [AgentTrace](https://github.com/ajinkya-awari/agentrace) | Evaluation harness for LLM agent tool-call traces. Live runs wait on provider quota. | ⛔ Implemented, provider-gated |
| 12 | [GraphGPS-Upgrade](https://github.com/ajinkya-awari/graphgps-upgrade) | GPS vs GCN and GIN ablation under a frozen compute budget. | ✅ Verified |

### Biomedical and protein intelligence

| # | Project | What it is | Status |
| ---: | --- | --- | --- |
| 04 | [AFBind](https://github.com/ajinkya-awari/afbind) | AlphaFold2-guided protein-ligand affinity benchmark. ECFP6 baseline Pearson r = 0.4765 on BindingDB Ki, leakage-safe split, 37 tests. | ✅ Verified |
| 06 | [KnetMiner-LLM](https://github.com/ajinkya-awari/knetminer-llm) | Evidence-grounded biomedical graph retrieval with leakage-safe HGT evaluation. | ⛔ Strict acceptance 0/30 |
| 07 | [F2-HistoGNN](https://github.com/ajinkya-awari/f2-histognn) | Nuclei-graph benchmark for LUAD/LUSC histology. 62 tests, real-data pilot (4 models × 3 seeds). | ✅ Pilot-scale |
| 15 | [ESM2-Protein-Fitness](https://github.com/ajinkya-awari/esm2-protein-fitness) | Protein fitness prediction on ESM2 embeddings. | ✅ Verified |
| 18 | [OmicsGraph](https://github.com/ajinkya-awari/omicsgraph) | Governance-first contracts for single-cell omics graph learning. | 🧪 Synthetic scope |

### Clinical systems and safety

| # | Project | What it is | Status |
| ---: | --- | --- | --- |
| 08 | [ClinicalBERT-ICD](https://github.com/ajinkya-awari/clinicalbert-icd) | Leakage-safe ICD-9 multi-label scaffold, LoRA vs full fine-tuning (171 tests). | 🧪 Synthetic, MIMIC-III access pending |
| 09 | [NHSCopilot-Eval](https://github.com/ajinkya-awari/-nhscopilot-eval) | Evaluation harness for NHS-facing AI copilot workflows (33 tests). | 🧪 Synthetic scope |
| 10 | [PubMedQA-LoRA](https://github.com/ajinkya-awari/pubmedqa-lora) | QLoRA vs zero-shot on PubMedQA evidence classification. Full runs wait on GPU quota. | ⛔ Quota-gated |
| 11 | [MedLLM-Safety](https://github.com/ajinkya-awari/medllm-safety) | Provider-free safety contracts for medical-LLM evaluation (63 tests). | 🧪 Synthetic scope |
| 13 | [ClinVision](https://github.com/ajinkya-awari/clinvision) | Auditable image-to-text prototype on licence-cleared imaging data. | 🧪 Synthetic scope |
| 14 | *CausalClinical* | Causal-inference benchmark design for MIMIC-III treatment effects. No repository yet. | 🗂 Planning, access required |
| 19 | [NICE-RAG](https://github.com/ajinkya-awari/-nice-rag) | Citation-first NICE guideline retrieval (151 tests). NICE content is gated. | 🧪 Synthetic scope |

### Privacy and federated learning

| # | Project | What it is | Status |
| ---: | --- | --- | --- |
| 05 | [FedScope](https://github.com/ajinkya-awari/fedscope) | FedAvg / FedProx / FedNova vs centralized baseline (F1 0.78–0.80, 3 seeds). | ✅ Verified |
| 17 | [PrivacyFL-DP](https://github.com/ajinkya-awari/privacyfl-dp) | Federated learning with differential privacy on NIH ChestX-ray14. | 🟡 1 of 6 privacy levels run |

### Interpretability and theory

| # | Project | What it is | Status |
| ---: | --- | --- | --- |
| 16 | [Mech-Interp](https://github.com/ajinkya-awari/mech-interp) | Deterministic toy contracts for activation capture, attribution and interventions. Real-model work is the next step. | 🧪 Toy scale |
| 20 | [AIXI-Complexity](https://github.com/ajinkya-awari/aixi-complexity-benchmark) | Agents on 20 frozen finite-state tasks with declared proxy vectors. 81 tests, CI green. | ✅ Released, with limitations |

`🧪` means the contract and test layer is verified on synthetic data only. It is not a claim about real data.

---

## What I'm looking for

A **research fellowship, paid placement or role** that funds the next step: taking interpretability and evaluation from toy models to real ones, with the same habit of reporting exactly what the numbers say. My dissertation period (March to September 2027) is open for a placement.

If you work on reliable ML for biomedicine, protein or graph learning, privacy-preserving ML, or model evaluation, the fastest way to judge me is to open one repo above and read its Limitations section. Then [email me](mailto:ajinkya18072001@gmail.com).

---

## GitHub activity

<div align="center">
<img src="assets/contrib-heatmap.svg" alt="Contribution heatmap" width="860" />
</div>

<sub>Calendar generated daily from GitHub's public contribution data. No JavaScript or tracking widgets.</sub>

---

## Published research

| Paper | Venue | DOI |
| --- | --- | --- |
| Plant Disease Detection using Machine Learning | IJARSCT, 2023 | [10.48175/IJARSCT-9297](https://doi.org/10.48175/IJARSCT-9297) |
| Transfer Learning for Plant Disease Detection | IJARSCT, 2023 | [10.48175/IJARSCT-9156](https://doi.org/10.48175/IJARSCT-9156) |

---

<details>
<summary><strong>Earlier experiments</strong> (before the numbered portfolio)</summary>

| Project | Area |
| --- | --- |
| [Transfer-Learning-Plant-Disease](https://github.com/ajinkya-awari/Transfer-Learning-Plant-Disease) | Transfer learning on PlantVillage |
| [GNN Agricultural Networks](https://github.com/ajinkya-awari/gnn-agricultural-networks) | Graph learning for disease propagation |
| [ChestXplain](https://github.com/ajinkya-awari/xai-medical-imaging) | Chest X-ray explainability |
| [Curious Adaptive Planner](https://github.com/ajinkya-awari/curious-adaptive-planner) | Curiosity-augmented planning |
| [RL Autonomous Navigation](https://github.com/ajinkya-awari/rl-autonomous-navigation) | Reinforcement learning navigation |
| [Adaptive AI Monitoring](https://github.com/ajinkya-awari/adaptive-ai-monitoring) | Reward and drift monitoring |
| [LLM Reasoning Orchestrator](https://github.com/ajinkya-awari/llm-reasoning-orchestrator) | Neuro-symbolic routing |
| [Algorithm Complexity Visualizer](https://github.com/ajinkya-awari/algorithm-complexity-visualizer) | Empirical complexity analysis |
| [NN Optimizer Study](https://github.com/ajinkya-awari/nn-optimizer-study) | Optimizer comparisons |
| [IoT Anomaly Detection](https://github.com/ajinkya-awari/iot-anomaly-detection) | Industrial anomaly detection |
| [Advanced DSA Patterns](https://github.com/ajinkya-awari/Advanced-DSA-Patterns) | Tested algorithmic patterns |
| [Market Density Cloud](https://github.com/ajinkya-awari/market-density-cloud) | PCA and clustering for market structure |

</details>

<div align="center">
<sub>Ajinkya Awari · UCL MSc Artificial Intelligence for Biomedicine and Healthcare</sub>
</div>
