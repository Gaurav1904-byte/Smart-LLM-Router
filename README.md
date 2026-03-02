pip install llama-cpp-python --prefer-binary --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu


🧠 Smart LLM Router
Adaptive Multi-Model Cost-Aware Routing System (CPU-Optimized)
🚀 Overview

This project implements a CPU-optimized adaptive multi-model LLM routing system that dynamically selects between a lightweight model and a larger reasoning model based on query complexity.

Instead of always using a large model (high latency, high cost), the system:

Predicts query complexity using an ML classifier

Routes to a small or large model accordingly

Uses deterministic tools (calculator) when possible

Applies cascading fallback for quality control

Logs inference data for performance evaluation

Exposes a production-style REST API using FastAPI

🎯 Problem Statement

Large Language Models (LLMs) have a tradeoff:

Model Size	Latency	Cost	Reasoning Quality
Small	Low	Low	Basic
Large	High	High	Strong

Using a large model for every query is inefficient.

This project solves:

How can we dynamically route queries to the optimal model to balance latency and quality?

🏗 System Architecture
Client
   ↓
FastAPI API
   ↓
Router Engine
   ├── Math Tool Extraction (deterministic)
   ├── Complexity Classifier (TF-IDF + Logistic Regression)
   ├── Routing Policy (threshold-based)
   ├── Fallback Escalation
   ↓
Model Layer
   ├── TinyLlama (1.1B, Q4_K_M)
   └── Mistral 7B Instruct (Q4_K_M)
   ↓
Logging Layer
   ├── Console logs
   ├── File logs
   └── SQLite database
🧠 Key Features
✅ 1. Multi-Model Routing

Tiny model for simple queries

Large model for complex reasoning

✅ 2. ML-Based Complexity Estimation

TF-IDF vectorization

Logistic regression classifier

Outputs probability score

✅ 3. Deterministic Tool Integration

Extracts arithmetic expressions

Uses Python evaluator

Bypasses LLM for correct math

✅ 4. Cascading Fallback

If small model response quality is weak

Automatically escalates to large model

✅ 5. Logging & Observability

Latency tracking

Model usage tracking

SQLite storage

File-based logs

✅ 6. REST API Deployment

FastAPI service

Swagger documentation

JSON-based input/output

⚙️ Installation Guide
1️⃣ Create Conda Environment
conda create -n llmrouter python=3.10 -y
conda activate llmrouter
2️⃣ Install Dependencies
pip install --upgrade pip
pip install llama-cpp-python --prefer-binary --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
pip install fastapi uvicorn scikit-learn pandas numpy sqlalchemy matplotlib
3️⃣ Download Models

Download:

TinyLlama 1.1B Chat GGUF (Q4_K_M)

Mistral 7B Instruct GGUF (Q4_K_M)

Place them inside:

models/
    tiny.gguf
    mistral.gguf
▶️ Running the Project
Run Interactive CLI
python run.py
Run FastAPI Server
uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs

Use /ask endpoint.

📊 Example API Request
{
  "query": "Explain neural networks"
}

Response:

{
  "query": "...",
  "complexity_score": 0.62,
  "model_used": "large",
  "response": "...",
  "latency": 12.4
}
🔬 Routing Logic
Step 1 — Math Extraction

If query contains arithmetic expression:
→ Use calculator tool.

Step 2 — Complexity Estimation
P(complex∣query)
P(complex∣query)

Computed using logistic regression.

Step 3 — Threshold Routing

If:

complexity < threshold

→ Use small model

Else:
→ Use large model

Step 4 — Fallback Escalation

If small model output is low quality:
→ Escalate to large model

📈 Performance Optimization Strategy

Latency depends on:

Model size

Quantization level

Context length

Max token generation

The system reduces unnecessary large model usage by:

Threshold tuning

Tool overrides

Cascading inference

🧪 Evaluation Strategy

The system can be evaluated by comparing:

Always Small Model

Always Large Model

Smart Routing

Metrics:

Average latency

Escalation rate

Model usage distribution

Response length

Cost proxy (token generation)

🛠 Technologies Used

Python 3.10

llama-cpp-python

FastAPI

Scikit-learn

SQLite

SQLAlchemy

🧠 Engineering Concepts Demonstrated

Cost-sensitive model routing

Cascading inference

Tool augmentation

CPU-based quantized deployment

ML-based policy decision

Observability and logging

REST API design