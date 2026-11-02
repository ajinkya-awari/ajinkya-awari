<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=Ajinkya%20Awari&fontSize=56&fontColor=fff&animation=twinkling&fontAlignY=40&desc=ML%20Engineer%20%C2%B7%20Biomedical%20AI%20%C2%B7%20Reliable%20Learning%20Systems&descAlignY=60&descAlign=50&descSize=17" width="100%" />

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-research-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-ajinkya1807-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/ajinkya1807)
[![Kaggle](https://img.shields.io/badge/Kaggle-ajinkya1225-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://www.kaggle.com/ajinkya1225)
[![GitHub followers](https://img.shields.io/github/followers/ajinkya-awari?style=flat-square&logo=github&color=181717)](https://github.com/ajinkya-awari)

</div>

I am an **ML Engineer** currently pursuing an **MSc in Artificial Intelligence for Biomedicine and Healthcare at University College London (UCL), UK**.

I build machine-learning systems that hold up past the demo: reproducible pipelines, leakage-safe evaluation, provenance-first retrieval, graph models, protein-learning experiments, privacy boundaries, and explanations that let people inspect model decisions before trusting them.

My portfolio contains **20 public repositories out of 21 numbered projects**. Every repository shows its actual status, including when the evidence is synthetic, pilot-scale, externally gated, or planning-only. I do not present synthetic contracts as clinical validation.

---

## Research Areas

| Area | What I build |
| --- | --- |
| **Reliable ML / MLOps** | Reproducible training pipelines, leakage-safe splits, experiment tracking, versioned inference |
| **Biomedical AI** | Graph neural networks for pathology, protein fitness, clinical retrieval, ICD coding |
| **Evaluation & Safety** | Agent-trace evaluation, medical-LLM safety contracts, XAI benchmarks |
| **Privacy & Federated Learning** | Differential-privacy contracts, federated baselines, privacy-boundary testing |
| **Interpretability** | Mechanistic attribution, activation capture, structured intervention tests |

---

## Selected Work

| # | Project | Domain | Status | Verified result or limitation |
| ---: | --- | --- | --- | --- |
| 05 | [FedScope](https://github.com/ajinkya-awari/fedscope) | Federated learning | Publicly verified | F1 approximately 0.78-0.80 across three seeds |
| 12 | [GraphGPS-Upgrade](https://github.com/ajinkya-awari/graphgps-upgrade) | Graph learning | Publicly verified | Full-budget graph ablation with public evidence |
| 04 | [AFBind](https://github.com/ajinkya-awari/afbind) | Structural biology | Publicly verified | BindingDB Ki baseline evidence; not an AF2 comparison claim |
| 07 | [F2-HistoGNN](https://github.com/ajinkya-awari/f2-histognn) | Computational pathology | Pilot benchmark | Four models and three seeds; not clinical validation |
| 15 | [ESM2 Protein Fitness](https://github.com/ajinkya-awari/esm2-protein-fitness) | Protein ML | Publicly verified | Public benchmark and 112 tests in the current suite |
| 06 | [KnetMiner-LLM](https://github.com/ajinkya-awari/knetminer-llm) | Biomedical graph retrieval | Public release | Strict Qwen acceptance gap documented honestly |
| 19 | [NICE-RAG](https://github.com/ajinkya-awari/-nice-rag) | Clinical retrieval | Complete with limitations | 151 tests and five open PMC records; NICE/provider gates remain |
| 20 | [AIXI-Complexity](https://github.com/ajinkya-awari/aixi-complexity-benchmark) | Agent evaluation | Public benchmark | Fixed synthetic suite; primary Qwen valid on 86/200 records |

---

## Full Portfolio - All 21 Projects

> **20 of 21 projects have public repositories.** Project 14 remains intentionally unpublished because it is planning-only and requires restricted-data authorization.

### Reliable ML & MLOps

| # | Project | Status | Link |
| ---: | --- | --- | --- |
| 00 | **SolomonoffBench** - empirical LLM sequence-compression benchmark | Complete with limitations | [Repository](https://github.com/ajinkya-awari/solomonoff-bench) |
| 01 | **T1 MLOps Stack** - training pipeline, tracking, and inference engineering | Complete with limitations | [Repository](https://github.com/ajinkya-awari/t1-mlops-stack) |
| 02 | **T2 XAI Triple** - Grad-CAM, SHAP, and Integrated Gradients | Complete with limitations | [Repository](https://github.com/ajinkya-awari/xai-medical-imaging-project-02) |
| 03 | **AgentTrace** - evaluation harness for agent tool-call traces | Implementation complete; provider gated | [Repository](https://github.com/ajinkya-awari/agentrace) |
| 12 | **GraphGPS-Upgrade** - controlled graph-model ablation | Public benchmark release | [Repository](https://github.com/ajinkya-awari/graphgps-upgrade) |
| 20 | **AIXI-Complexity** - reproducible agent-complexity benchmark | Public benchmark with limitations | [Repository](https://github.com/ajinkya-awari/aixi-complexity-benchmark) |

### Biomedical & Protein Intelligence

| # | Project | Status | Link |
| ---: | --- | --- | --- |
| 04 | **AFBind** - protein-ligand affinity benchmark | Public benchmark evidence | [Repository](https://github.com/ajinkya-awari/afbind) |
| 06 | **KnetMiner-LLM** - evidence-grounded biomedical graph retrieval | Public static release | [Repository](https://github.com/ajinkya-awari/knetminer-llm) |
| 07 | **F2-HistoGNN** - nuclei-graph pathology benchmark | Public pilot with limitations | [Repository](https://github.com/ajinkya-awari/f2-histognn) |
| 15 | **ESM2 Protein Fitness** - mutation-fitness prediction | Public benchmark release | [Repository](https://github.com/ajinkya-awari/esm2-protein-fitness) |
| 18 | **OmicsGraph** - governance-first omics graph pipeline | Public synthetic release | [Repository](https://github.com/ajinkya-awari/omicsgraph) |

### Clinical Systems & Safety

| # | Project | Status | Link |
| ---: | --- | --- | --- |
| 08 | **ClinicalBERT-ICD** - leakage-safe ICD coding scaffold | Synthetic release; MIMIC/DUA gated | [Repository](https://github.com/ajinkya-awari/clinicalbert-icd) |
| 09 | **NHSCopilot-Eval** - NHS-facing AI evaluation harness | Synthetic release with limitations | [Repository](https://github.com/ajinkya-awari/-nhscopilot-eval) |
| 10 | **PubMedQA-LoRA** - evidence-classification fine-tuning scaffold | Partial/recovery scope; further execution gated | [Repository](https://github.com/ajinkya-awari/pubmedqa-lora) |
| 11 | **MedLLM-Safety** - provider-free medical-LLM safety contracts | Synthetic safety release | [Repository](https://github.com/ajinkya-awari/medllm-safety) |
| 13 | **ClinVision** - auditable clinical-vision prototype | Synthetic release with limitations | [Repository](https://github.com/ajinkya-awari/clinvision) |
| 14 | **CausalClinical** - causal clinical benchmark design | Planning-only; no public repository | - |
| 19 | **NICE-RAG** - citation-first guideline retrieval | Complete with limitations | [Repository](https://github.com/ajinkya-awari/-nice-rag) |

### Privacy & Federated Learning

| # | Project | Status | Link |
| ---: | --- | --- | --- |
| 05 | **FedScope** - federated baselines and multi-seed evaluation | Public benchmark release | [Repository](https://github.com/ajinkya-awari/fedscope) |
| 17 | **PrivacyFL-DP** - privacy-preserving federated-learning contracts | Synthetic scope; real DP-FL execution not released | [Repository](https://github.com/ajinkya-awari/privacyfl-dp) |

### Interpretability & Theoretical Systems

| # | Project | Status | Link |
| ---: | --- | --- | --- |
| 16 | **Mech-Interp** - deterministic toy interpretability contracts | Synthetic release | [Repository](https://github.com/ajinkya-awari/mech-interp) |

---

## Limitations, stated plainly

- Several projects are synthetic or contract-level releases because restricted datasets, clinical approvals, provider credentials, or model access were not available.
- Project 08 requires MIMIC-III/DUA approval before real-data work.
- Project 14 remains planning-only and has no public repository.
- Project 17 has no released measured epsilon or real-data utility result; only the synthetic privacy/federated-learning contract layer is public.
- Project 20 uses a fixed synthetic suite. The primary Qwen arm is valid on 86/200 records covering 10/20 tasks. The constrained arm is post-hoc, secondary, and exploratory; the two arms are not directly comparable.
- Project 07 is pilot-scale and is not clinical validation.
- Public repositories do not imply regulatory approval, clinical deployment, or production readiness.

---

## Technologies

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-retrieval-8B5CF6?style=for-the-badge)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

</div>

---

## How I Work

- **Contracts before code** - define acceptance tests and failure states first.
- **Synthetic before restricted** - validate the pipeline before requesting sensitive data or provider access.
- **Explicit gates** - data, models, APIs, GPU, privacy, and publication require recorded authorization.
- **Evidence before claims** - preserve test counts, seeds, hashes, provenance, and limitations.
- **Honest status** - every repository distinguishes verified, synthetic-only, blocked, and planning-only work.
- **No hidden attribution** - public repositories contain no AI session transcripts or AI co-author trailers.

---

## Current professional focus

I am looking for ML engineering, research engineering, biomedical AI, responsible-AI, MLOps, and research-assistant opportunities in the UK and internationally.

The strongest areas for collaboration are protein intelligence, clinical AI evaluation, graph learning, privacy-preserving ML, and reproducible research infrastructure.

---

## GitHub Activity

<div align="center">
<img src="assets/contrib-heatmap.svg" alt="Contribution heatmap" width="860" />
</div>

<sub>Activity calendar generated from GitHub public contribution data. No JavaScript or tracking widgets.</sub>

---

## Contact

- **GitHub** - [github.com/ajinkya-awari](https://github.com/ajinkya-awari)
- **Hugging Face** - [huggingface.co/ajinkya1807](https://huggingface.co/ajinkya1807)
- **Kaggle** - [kaggle.com/ajinkya1225](https://www.kaggle.com/ajinkya1225)
- **Email** - ajinkya18072001@gmail.com

---

## Published Research

| Paper | Venue | DOI |
| --- | --- | --- |
| Plant Disease Detection using Machine Learning | IJARSCT, 2023 | [10.48175/IJARSCT-9297](https://doi.org/10.48175/IJARSCT-9297) |
| Transfer Learning for Plant Disease Detection | IJARSCT, 2023 | [10.48175/IJARSCT-9156](https://doi.org/10.48175/IJARSCT-9156) |

---

<details>
<summary><strong>Earlier experiments</strong></summary>

These projects predate the numbered portfolio and form part of the broader engineering record.

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

</details>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%" />

<div align="center">
<sub>Built and maintained by Ajinkya Awari · ML Engineer · UCL MSc Artificial Intelligence for Biomedicine and Healthcare</sub>
</div>
