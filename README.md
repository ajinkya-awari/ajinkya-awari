<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=Ajinkya%20Awari&fontSize=56&fontColor=fff&animation=twinkling&fontAlignY=40&desc=ML%20Engineer%20%C2%B7%20Biomedical%20AI%20%C2%B7%20Reliable%20Learning%20Systems&descAlignY=60&descAlign=50&descSize=17" width="100%" />

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org) [![PyTorch](https://img.shields.io/badge/PyTorch-research-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org) [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-ajinkya1807-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/ajinkya1807) [![Kaggle](https://img.shields.io/badge/Kaggle-ajinkya1225-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://www.kaggle.com/ajinkya1225) [![GitHub followers](https://img.shields.io/github/followers/ajinkya-awari?style=flat-square&logo=github&color=181717)](https://github.com/ajinkya-awari)

</div>

<div align="center">
<img src="assets/ascii-portrait.svg" alt="Animated terminal: Ajinkya Awari, MSc AI for Biomedicine and Healthcare at UCL. I build ML systems that tell you when they are wrong." width="100%" />
</div>

<div align="center">
<img src="assets/info-card.svg" alt="20 public repos, 7 with real results, 81 tests with CI green on the flagship benchmark, 3 negative results published on purpose" width="100%" />
</div>

<sub>**The seven with real results:** [AIXI-Complexity](https://github.com/ajinkya-awari/aixi-complexity-benchmark) · [FedScope](https://github.com/ajinkya-awari/fedscope) · [GraphGPS-Upgrade](https://github.com/ajinkya-awari/graphgps-upgrade) · [ESM2-Protein-Fitness](https://github.com/ajinkya-awari/esm2-protein-fitness) · [AFBind](https://github.com/ajinkya-awari/afbind) · [F2-HistoGNN](https://github.com/ajinkya-awari/f2-histognn) · [SolomonoffBench](https://github.com/ajinkya-awari/solomonoff-bench). **The three negative results** are in the ledger below, marked 🟡 and ⛔.</sub>

<img src="assets/divider.svg" alt="" width="100%" />

I am an **ML Engineer** pursuing an **MSc in Artificial Intelligence for Biomedicine and Healthcare at University College London (UCL)**.

Most ML portfolios show what worked. Mine shows what was **measured**, including the runs that came back near chance. Each project starts with leakage-safe splits, frozen budgets and a synthetic test layer, and touches real data only once access, licence and privacy gates are cleared. If a result is weak, the README says so on the first screen.

## Research areas

| Area | What I build |
| --- | --- |
| **Reliable ML / MLOps** | Reproducible training pipelines, leakage-safe splits, experiment tracking, versioned inference |
| **Biomedical AI** | Graph neural networks for pathology, protein fitness, clinical retrieval, ICD coding |
| **Evaluation and safety** | Agent-trace evaluation, medical-LLM safety contracts, XAI benchmarks |
| **Privacy and federated learning** | Differential-privacy contracts, federated baselines, privacy-boundary testing |
| **Interpretability** | Mechanistic attribution, activation capture, structured intervention tests |

<img src="assets/divider.svg" alt="" width="100%" />

## The journey

<div align="center">
<img src="assets/journey.svg" alt="Three scenes: the failure (frozen BatchNorm collapsed accuracy, found and published in 2023), the build (20 gated projects), the ask (real-model research)" width="100%" />
</div>

<img src="assets/divider.svg" alt="" width="100%" />

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

<img src="assets/divider.svg" alt="" width="100%" />

## All 21 projects, 00 to 20

`🧪` means the contract and test layer is verified on synthetic data only. It is not a claim about real data.

### Reliable ML and MLOps

| # | Project | What it does | Evidence and limits |
| ---: | --- | --- | --- |
| 00 | [SolomonoffBench](https://github.com/ajinkya-awari/solomonoff-bench) | Tests whether LLMs compress sequences the way an ideal predictor would, using sequences of known, varying algorithmic complexity. | ✅ Benchmark slice closed; complexity-vs-compression analysis complete. Limits listed in the README. |
| 01 | [T1 MLOps Stack](https://github.com/ajinkya-awari/t1-mlops-stack) | An end-to-end ML pipeline: reproducible training, experiment tracking and a deployed inference app, covering the path from notebook to served model. | 🟡 Core pipeline complete. Deployment evidence is historical and due for re-verification. |
| 02 | [T2 XAI Triple](https://github.com/ajinkya-awari/xai-medical-imaging-project-02) | Compares Grad-CAM, SHAP and Integrated Gradients on NIH ChestX-ray14 and scores how well each explanation overlaps the annotated finding. | 🟡 Mean IoU 0.1289, so overlap is weak. Reported as measured; research use only. |
| 03 | [AgentTrace](https://github.com/ajinkya-awari/agentrace) | An evaluation harness for LLM agent tool-call traces, with probes for sycophancy and reasoning-effort effects. | ⛔ Implementation complete. Live runs are blocked by provider rate limits, so no live results are claimed. |
| 12 | [GraphGPS-Upgrade](https://github.com/ajinkya-awari/graphgps-upgrade) | Compares the GraphGPS graph transformer with GCN and GIN under one frozen 30-epoch budget on a Tesla T4, so gaps come from the model and not from extra tuning. | ✅ Test ROC-AUC: GPS 0.748, GIN 0.698, GCN 0.693 (3 seeds). Holds for this frozen recipe only. |

### Biomedical and protein intelligence

| # | Project | What it does | Evidence and limits |
| ---: | --- | --- | --- |
| 04 | [AFBind](https://github.com/ajinkya-awari/afbind) | Tests whether AlphaFold2-predicted structures help predict protein-ligand binding affinity, using BindingDB Ki values and a leakage-safe cross-target split. | ✅ ECFP6 baseline Pearson r = 0.4765; 37 tests pass. The baseline is the reference point, not an AF2 comparison claim. |
| 06 | [KnetMiner-LLM](https://github.com/ajinkya-awari/knetminer-llm) | Answers biomedical questions over a knowledge graph with strict citations and abstention, evaluated with leakage-safe heterogeneous-graph splits. | ⛔ Release complete, but strict per-answer acceptance is 0/30 with the local model. |
| 07 | [F2-HistoGNN](https://github.com/ajinkya-awari/f2-histognn) | Turns histology images into nuclei graphs and compares graph models on lung adenocarcinoma vs squamous (LUAD/LUSC) classification. | ✅ 62 tests; real-data pilot with 4 models × 3 seeds. Pilot-sized, not clinical validation. |
| 15 | [ESM2-Protein-Fitness](https://github.com/ajinkya-awari/esm2-protein-fitness) | Predicts how protein mutations change fitness, from ESM2 language-model embeddings. | ✅ 87/87 tests; Kaggle run complete. Full-assay confidence intervals are optional follow-up. |
| 18 | [OmicsGraph](https://github.com/ajinkya-awari/omicsgraph) | Pipeline contracts for single-cell omics graph learning: provenance, leakage and schema checks that must pass before real data is joined. | 🧪 Synthetic scope verified. Real data waits on source licence and annotation review. |

### Clinical systems and safety

| # | Project | What it does | Evidence and limits |
| ---: | --- | --- | --- |
| 08 | [ClinicalBERT-ICD](https://github.com/ajinkya-awari/clinicalbert-icd) | Multi-label ICD-9 coding, comparing LoRA with full fine-tuning, using patient-grouped splits and labels fitted on training data only. | 🧪 171 synthetic tests. The MIMIC-III benchmark awaits data-use approval. |
| 09 | [NHSCopilot-Eval](https://github.com/ajinkya-awari/-nhscopilot-eval) | An evaluation harness for NHS-style AI assistant workflows, with scoring contracts that run without any provider or patient data. | 🧪 33 public tests. Makes no clinical or NHS-endorsement claims. |
| 10 | [PubMedQA-LoRA](https://github.com/ajinkya-awari/pubmedqa-lora) | Classifies PubMedQA evidence labels with QLoRA fine-tuning against zero-shot, using official split provenance, constrained outputs and a gated locked test set. | ⛔ Development evidence only. Remaining folds wait on GPU quota. |
| 11 | [MedLLM-Safety](https://github.com/ajinkya-awari/medllm-safety) | Defines what a medical-LLM evaluation must check before any real model is involved, and tests those checks on synthetic cases. | 🧪 63 tests. Real-model readiness is not claimed. |
| 13 | [ClinVision](https://github.com/ajinkya-awari/clinvision) | A research-only contract layer for image-to-text workflows on licence-cleared imaging data, built to validate safety checks before a real model runs. | 🧪 Synthetic only. MIMIC-CXR is blocked, so no clinical claims. |
| 14 | *CausalClinical* | A benchmark design for estimating treatment effects from MIMIC-III with causal methods and explicit assumption review. | 🗂 Planning only. Needs MIMIC-III data-use approval; no code or repo yet. |
| 19 | [NICE-RAG](https://github.com/ajinkya-awari/-nice-rag) | A retrieval scaffold where every answer must cite its NICE guideline source. | 🧪 151 tests; 5 CC BY 4.0 PMC records verified. NICE content itself is gated. |

### Privacy and federated learning

| # | Project | What it does | Evidence and limits |
| ---: | --- | --- | --- |
| 05 | [FedScope](https://github.com/ajinkya-awari/fedscope) | Benchmarks the federated algorithms FedAvg, FedProx and FedNova against a centralized baseline on the same task. | ✅ F1 0.78–0.80 across 3 seeds. |
| 17 | [PrivacyFL-DP](https://github.com/ajinkya-awari/privacyfl-dp) | Federated learning with differential privacy (Opacus) on NIH ChestX-ray14 across 5 clients, measuring how the privacy level affects accuracy. | 🟡 1 of 6 privacy levels run: ε = 0.096, macro-AUC 0.497 (chance). The other five are pending. |

### Interpretability and theory

| # | Project | What it does | Evidence and limits |
| ---: | --- | --- | --- |
| 16 | [Mech-Interp](https://github.com/ajinkya-awari/mech-interp) | Toy-scale tooling for mechanistic interpretability: capture activations, attribute behaviour and test interventions, with explicit limits on what each result proves. | 🧪 Toy scale. Real-model research is the next step. |
| 20 | [AIXI-Complexity](https://github.com/ajinkya-awari/aixi-complexity-benchmark) | Compares five agent types (random, tabular Q, an AIXI-inspired planner, a small local LLM and an exact oracle) on 20 frozen tasks as declared difficulty proxies change. | ✅ 81 tests, CI green. No proxy stays significant after Holm correction (min adjusted p = 0.144). |

<img src="assets/divider.svg" alt="" width="100%" />

## What I'm looking for

A **research fellowship, paid placement or role** that funds the next step: taking interpretability and evaluation from toy models to real ones, with the same habit of reporting exactly what the numbers say. My dissertation period (March to September 2027) is open for a placement.

If you work on reliable ML for biomedicine, protein or graph learning, privacy-preserving ML, or model evaluation, the fastest way to judge me is to open one repo above and read its Limitations section. Then [email me](mailto:ajinkya18072001@gmail.com).

## Technologies

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

</div>

<img src="assets/divider.svg" alt="" width="100%" />

## GitHub activity

<div align="center">
<img src="assets/contrib-heatmap.svg" alt="Contribution heatmap" width="860" />
</div>

<sub>Calendar generated from GitHub's public contribution data. No JavaScript or tracking widgets.</sub>

## Published research

| Paper | Venue | DOI |
| --- | --- | --- |
| Plant Disease Detection using Machine Learning | IJARSCT, 2023 | [10.48175/IJARSCT-9297](https://doi.org/10.48175/IJARSCT-9297) |
| Transfer Learning for Plant Disease Detection | IJARSCT, 2023 | [10.48175/IJARSCT-9156](https://doi.org/10.48175/IJARSCT-9156) |

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

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%" />

<div align="center">
<sub>Ajinkya Awari · UCL MSc Artificial Intelligence for Biomedicine and Healthcare</sub>
</div>
