<div align="center">

# `ajinkya-awari@github:~$`

**ML Engineer · Reliable Learning Systems · Biomedical AI**

<a href="https://github.com/ajinkya-awari">
  <img src="assets/ascii-portrait.svg" alt="Animated terminal-style AA monogram" width="370" />
</a>

<a href="https://github.com/ajinkya-awari">
  <img src="assets/info-card.svg" alt="Terminal information card for Ajinkya Awari" width="490" />
</a>

</div>

I build and audit machine-learning systems that are useful beyond a single metric:
reproducible experiments, leakage-safe evaluation, tool-assisted reasoning, and
explanations that help people inspect model decisions before trusting them.

## `~/` about this work

My portfolio focuses on **reliable ML systems, biomedical AI, evaluation, privacy,
provenance, and reproducibility** rather than one-shot demos. Most projects below
are deliberately staged: a synthetic or local contract layer is built and tested
first, and real data, real models, or real deployment are only attempted once an
explicit access, licensing, or governance gate is cleared. The status legend below
exists so that a repository link never implies more than what is actually verified.

## `~/` status legend

| Label | Meaning |
| --- | --- |
| **Publicly verified** | Public repo, benchmark/tests run, and a result is recorded with evidence. |
| **Complete with limitations** | A defined scope is finished and public, with an explicitly documented gap (e.g. one dataset stage still blocked). |
| **Synthetic scope verified** | Local/synthetic contracts and tests are complete and public; real-data or real-model execution is not yet run. |
| **Runtime in progress / blocked** | Work is active but currently stalled on an external dependency (provider quota, data access, compute). |
| **Planning-only** | Design and scaffold only; no benchmark, dataset, or model execution has occurred. |
| **Not publicly released** | Work exists locally but has not been pushed to a public repository. |

## `~/` selected work

Strongest, most-verified projects. Full 21-project map is below.

| Project | What it does | Domain | Status | Metric |
| --- | --- | --- | --- | --- |
| [SolomonoffBench](https://github.com/ajinkya-awari/solomonoff-bench) | Empirical benchmark comparing how LLMs compress formally generated sequences of varying algorithmic complexity | LLM evaluation · information theory | Complete with limitations | Technical benchmark slice closed |
| [AFBind](https://github.com/ajinkya-awari/afbind) | Benchmarking library for AlphaFold2 structure substitution in protein–ligand affinity prediction | Structural biology | Publicly verified | 37/37 synthetic tests pass on Kaggle |
| [FedScope](https://github.com/ajinkya-awari/fedscope) | Federated-learning benchmark comparing FedAvg, FedProx, FedNova, and server-momentum against a centralized baseline | Federated learning | Publicly verified | Centralized 3-seed gate passed (F1 0.78–0.80) |
| [KnetMiner-LLM](https://github.com/ajinkya-awari/knetminer-llm) | Evidence-grounded biomedical graph retrieval with leakage-safe HGT evaluation, strict citations, and abstention | Biomedical retrieval | Publicly verified | Release-engineering scope complete; strict per-answer acceptance remains 0/30 (documented limitation) |
| [F2-HistoGNN](https://github.com/ajinkya-awari/f2-histognn) | Reproducible nuclei-graph benchmark scaffold for exploratory LUAD/LUSC histology classification | Computational pathology | Publicly verified | 62 synthetic tests pass; Kaggle real-data pilot run complete (4 models × 3 seeds) |
| [GraphGPS-Upgrade](https://github.com/ajinkya-awari/graphgps-upgrade) | GPS vs. GCN/GIN ablation under a frozen 30-epoch budget, Tesla T4 execution | Graph learning | Publicly verified | Test ROC-AUC: GPS 0.748, GIN 0.698, GCN 0.693 (3 seeds) |
| [ESM2-Protein-Fitness](https://github.com/ajinkya-awari/esm2-protein-fitness) | Protein mutation fitness-prediction benchmark built on ESM2 embeddings | Protein ML | Publicly verified | 87/87 tests pass; Kaggle kernel run complete |
| [PrivacyFL-DP](https://github.com/ajinkya-awari/privacyfl-dp) | Local synthetic contract layer for a differentially-private federated-learning research workflow | Privacy · federated learning | Synthetic scope verified | 23/23 tests pass at pinned commit `f7d7d7b` |
| [NICE-RAG](https://github.com/ajinkya-awari/-nice-rag) | Citation-first retrieval scaffold for NICE clinical guidelines with bounded synthetic validation | Clinical NLP · retrieval | Complete with limitations | 139/139 local tests pass; open-evidence acquisition partial |

## `~/` full portfolio map

All 21 canonical projects, grouped by area. "Not publicly released" and
"planning-only" rows show no link — none exists yet, and none is guessed.

<details>
<summary><strong>Reliable ML and MLOps</strong></summary>

| # | Project | Status |
| ---: | --- | --- |
| 00 | [Solomonoff-LLM](https://github.com/ajinkya-awari/solomonoff-bench) — sequence-compression benchmark for LLMs | Complete with limitations |
| 01 | [T1 MLOps Stack](https://github.com/ajinkya-awari/t1-mlops-stack) — training pipeline, experiment tracking, and a deployed inference app | Complete with limitations |
| 02 | [T2 XAI Triple](https://github.com/ajinkya-awari/xai-medical-imaging-project-02) — Grad-CAM, SHAP, and Integrated Gradients benchmarked against NIH ChestX-ray14 radiologist bounding boxes (mean IoU 0.1289, Grad-CAM) | Complete with limitations |
| 03 | [AgentTrace](https://github.com/ajinkya-awari/agentrace) — evaluation harness for LLM agent tool-call traces, probing sycophancy and reasoning-effort behavior | Runtime in progress / blocked (provider quota) |
| 12 | [GraphGPS-Upgrade](https://github.com/ajinkya-awari/graphgps-upgrade) — GPS vs. GCN/GIN ablation on a frozen benchmark protocol | Publicly verified |

</details>

<details>
<summary><strong>Biomedical and protein intelligence</strong></summary>

| # | Project | Status |
| ---: | --- | --- |
| 04 | [AlphaFold-Guided Binding](https://github.com/ajinkya-awari/afbind) — AF2 structure substitution for protein–ligand affinity prediction | Publicly verified |
| 06 | [KnetMiner-LLM](https://github.com/ajinkya-awari/knetminer-llm) — evidence-grounded biomedical graph retrieval | Publicly verified |
| 07 | [F2-HistoGNN](https://github.com/ajinkya-awari/f2-histognn) — nuclei-graph histology classification benchmark | Publicly verified |
| 15 | [ESM2-Protein-Fitness](https://github.com/ajinkya-awari/esm2-protein-fitness) — protein mutation fitness prediction | Publicly verified |
| 18 | [OmicsGraph](https://github.com/ajinkya-awari/omicsgraph) — governance-first contracts (provenance, leakage, schema) for a future single-cell omics graph pipeline | Synthetic scope verified |

</details>

<details>
<summary><strong>Evaluation, safety, and clinical systems</strong></summary>

| # | Project | Status |
| ---: | --- | --- |
| 08 | [ClinicalBERT-ICD](https://github.com/ajinkya-awari/clinicalbert-icd) — leakage-safe ICD-9 multi-label classification scaffold, LoRA vs. full fine-tuning (171 synthetic tests) | Synthetic scope verified (MIMIC-III access blocked by DUA) |
| 09 | [NHSCopilot-Eval](https://github.com/ajinkya-awari/-nhscopilot-eval) — evaluation harness for an NHS-facing AI copilot workflow (33 public-export tests pass) | Complete with limitations (synthetic scope only; no NHS/clinical claims) |
| 10 | PubMedQA-LoRA — QLoRA fine-tuning vs. zero-shot baselines on PubMedQA evidence classification | Not publicly released |
| 11 | [MedLLM-Safety](https://github.com/ajinkya-awari/medllm-safety) — provider-free synthetic safety contracts for medical-LLM evaluation (63 public-export tests pass) | Synthetic scope verified |
| 13 | ClinVision — auditable image-to-text prototype on licence-cleared paired image/report data | Not publicly released |
| 14 | CausalClinical — causal-inference benchmark design for MIMIC-III treatment-effect estimation | Planning-only (blocked on DUA/governance) |
| 19 | [NICE-RAG](https://github.com/ajinkya-awari/-nice-rag) — citation-first NICE guideline retrieval scaffold | Complete with limitations |

</details>

<details>
<summary><strong>Privacy and federated learning</strong></summary>

| # | Project | Status |
| ---: | --- | --- |
| 05 | [FedScope](https://github.com/ajinkya-awari/fedscope) — federated-learning method comparison against a centralized baseline | Publicly verified |
| 17 | [PrivacyFL-DP](https://github.com/ajinkya-awari/privacyfl-dp) — differentially-private federated-learning contract layer | Synthetic scope verified |

</details>

<details>
<summary><strong>Reasoning, interpretability, and theoretical systems</strong></summary>

| # | Project | Status |
| ---: | --- | --- |
| 16 | [Mech-Interp](https://github.com/ajinkya-awari/mech-interp) — deterministic toy contracts for activation capture, attribution, and interventions (16/16 tests pass) | Synthetic scope verified |
| 20 | AIXI-Complexity — planned benchmark comparing AIXI-style agents to LLM agents across environments of known Kolmogorov complexity | Planning-only |

</details>

## `~/` research interests

Reliable ML · reinforcement learning evaluation and monitoring ·
neuro-symbolic reasoning · explainable and privacy-preserving biomedical AI ·
information-theoretic evaluation · reproducible research software

## `~/` current focus

Closing the synthetic-to-real gap on the projects above in priority order,
each gated on its own explicit dataset/access/licence approval rather than on
convenience — and publishing status honestly at every step, including when
the honest status is "blocked" or "planning-only."

## `~/` find me

- [GitHub](https://github.com/ajinkya-awari)
- [Hugging Face](https://huggingface.co/ajinkya1807)
- [Research flagship: SolomonoffBench](https://github.com/ajinkya-awari/solomonoff-bench)

## `~/` GitHub activity

<div align="center">

<img src="assets/contrib-heatmap.svg" alt="Contribution calendar for the public GitHub profile" width="860" />

</div>

The heatmap is generated from GitHub's public contribution calendar. It is a
small activity view, not a measure of research quality, and may remain at its
last valid version when GitHub's public page is unavailable.

<sub>Profile visuals are local SVGs with no JavaScript, tracking pixels, visitor counters, or external statistics widgets.</sub>

<details>
<summary><strong>Earlier work and additional experiments</strong></summary>

These predate the current 00–20 portfolio numbering and are not part of it.
Kept here as a record of earlier, smaller projects — mostly coursework-scale
algorithm, RL, and CV experiments rather than the staged research workflow above.

| Project | What it explores |
| --- | --- |
| [Advanced DSA Patterns](https://github.com/ajinkya-awari/Advanced-DSA-Patterns) | Production-grade implementations of 60+ algorithmic patterns with automated tests. |
| [RL autonomous navigation](https://github.com/ajinkya-awari/rl-autonomous-navigation) | A controlled comparison of tabular Q-learning, DDQN, and PPO on stochastic FrozenLake navigation. |
| [Adaptive AI monitoring](https://github.com/ajinkya-awari/adaptive-ai-monitoring) | Lightweight monitors for reward hacking, entropy spikes, and behavioral drift during RL training. |
| [LLM reasoning orchestrator](https://github.com/ajinkya-awari/llm-reasoning-orchestrator) | A neuro-symbolic pipeline that routes exact computation to SymPy instead of relying on model arithmetic. |
| [ChestXplain](https://github.com/ajinkya-awari/xai-medical-imaging) | DenseNet121 chest-X-ray classification paired with Grad-CAM visual explanations. |
| [Market Density Cloud](https://github.com/ajinkya-awari/market-density-cloud) | PCA and clustering views of mixed stock, crypto, and forex data in an interactive dashboard. |
| [Curious Adaptive Planner](https://github.com/ajinkya-awari/curious-adaptive-planner) | Curiosity-augmented value iteration with adaptive policy arbitration for bounded-optimality experiments. |
| [Transfer Learning Plant Disease](https://github.com/ajinkya-awari/Transfer-Learning-Plant-Disease) | VGG16, ResNet50, and EfficientNetB0 transfer-learning comparisons for PlantVillage disease detection. |
| [GNN agricultural networks](https://github.com/ajinkya-awari/gnn-agricultural-networks) | GCN, GraphSAGE, and GAT experiments for agricultural disease propagation with PyTorch Geometric. |
| [NN optimizer study](https://github.com/ajinkya-awari/nn-optimizer-study) | Empirical comparison of SGD, Adam, RMSprop, Adagrad, and L-BFGS on CIFAR-10 convergence. |
| [Algorithm Complexity Visualizer](https://github.com/ajinkya-awari/algorithm-complexity-visualizer) | Operation-counting and log-log regression experiments that validate Big-O bounds interactively. |
| [IoT Anomaly Detection](https://github.com/ajinkya-awari/iot-anomaly-detection) | LSTM and Transformer autoencoders compared with Isolation Forest for industrial IoT fault detection. |

</details>

---

<sub>Built and maintained by Ajinkya Awari.</sub>
