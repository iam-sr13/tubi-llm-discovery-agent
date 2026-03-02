# 🎬 Conversational Streaming Discovery Agent

A fully local, LLM-powered conversational content discovery system designed to simulate real-world streaming platform search and recommendation workflows.

This project demonstrates end-to-end GenAI system design including:

- Natural language intent extraction
- Semantic retrieval using embeddings
- Vector search with FAISS
- Re-ranking
- Lightweight agentic constraint relaxation
- Explanation generation
- Offline evaluation metrics
- API deployment with FastAPI

All components run locally using open-source tools.

---

# 📌 Problem Statement

Streaming users often express preferences in natural language:

> “Recommend dark psychological thrillers like Gone Girl but not too violent.”

Traditional keyword-based search struggles to interpret tone, constraints, and semantic similarity.

This project implements a conversational discovery agent that:

1. Converts natural language queries into structured preferences
2. Retrieves semantically similar content
3. Applies metadata constraints
4. Re-ranks results
5. Generates personalized explanations

The goal is to demonstrate modern GenAI architecture relevant to streaming platforms.

---

# 🏗 System Architecture

User Query  
→ Intent Extraction (LLM via Ollama)  
→ Embedding Generation  
→ FAISS Vector Retrieval  
→ Constraint Filtering  
→ Re-ranking  
→ Explanation Generation  
→ JSON API Response  

---

# 🧠 Core Components

## 1️⃣ Intent Extraction

Uses a local LLM (Mistral via Ollama) to convert user queries into structured JSON preferences:

Example output:

```json
{
  "genres": ["Thriller"],
  "tone": "dark",
  "max_violence": "medium"
}
````

---

## 2️⃣ Semantic Retrieval

* SentenceTransformers (`all-MiniLM-L6-v2`)
* FAISS vector index (CPU)
* Description-based embedding search

---

## 3️⃣ Re-Ranking

Results are re-ranked using:

* Popularity score
* Metadata match

This layer simulates business logic prioritization.

---

## 4️⃣ Agentic Constraint Relaxation

If strict constraints return no results, the system relaxes them automatically (e.g., increasing allowed violence level).

This demonstrates basic agent-like decision-making.

---

## 5️⃣ Explanation Generation

The LLM generates natural language explanations describing why recommendations match the user’s preferences.

---

## 6️⃣ Evaluation

Includes offline metric:

* `precision@k`

Example usage:

```python
from src.evaluation.metrics import precision_at_k
```

This demonstrates analytical rigor and evaluation awareness.

---

# 🛠 Tech Stack

* Python 3.10+
* Ollama (Mistral model)
* SentenceTransformers
* FAISS (CPU)
* FastAPI
* Pydantic
* Pytest

All components are free and run locally.

---

# 💻 Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/iam-sr13/tubi-llm-discovery-agent.git
cd tubi-llm-discovery-agent
```

---

## 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Ollama

Mac:

```bash
brew install ollama
```

Start server:

```bash
ollama serve
```

Pull model:

```bash
ollama pull mistral
```

---

## 5️⃣ Run API Server

```bash
uvicorn src.main:app --reload
```

---

## 6️⃣ Test Endpoint

Open in browser:

```
http://127.0.0.1:8000/recommend?query=dark thriller like gone girl
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# 📂 Project Structure

```
tubi-llm-discovery-agent/
│
├── data/
│   └── movies_sample.csv
│
├── src/
│   ├── main.py
│   ├── llm/
│   │   ├── intent_parser.py
│   │   ├── response_generator.py
│   │
│   ├── retrieval/
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │
│   ├── ranking/
│   │   ├── reranker.py
│   │
│   ├── agent/
│   │   ├── constraint_agent.py
│   │
│   ├── evaluation/
│   │   ├── metrics.py
│
├── tests/
├── requirements.txt
└── README.md
```

---

# ⚙️ Design Decisions

### Why Local LLM?

Ensures privacy, reproducibility, and zero API cost.

### Why FAISS?

Industry-standard vector search solution, efficient and scalable.

### Why Modular Architecture?

Separates:

* Retrieval
* Ranking
* LLM logic
* Evaluation

Improves maintainability and testability.

### Why Include Evaluation?

GenAI systems require measurable quality, not just qualitative demos.

---

# 📊 Example Response Format

```json
{
  "recommendations": [...],
  "explanation": "These films match your preference for dark psychological thrillers..."
}
```

---

# 🚀 Future Improvements

* Hybrid retrieval (semantic + metadata filtering)
* Fine-tuned reranker
* User personalization memory
* Caching embeddings
* Docker containerization
* Online A/B testing simulation

---

# 🎯 What This Demonstrates

* LLM integration
* Embedding-based retrieval
* Vector database usage
* Basic agentic reasoning
* API deployment
* Offline evaluation
* Clean modular architecture

This repository represents a production-style prototype of conversational content discovery for streaming platforms.

---

# 👤 Author

Dr. Shriraj Sawant
AI Researcher & Engineer

````

---
