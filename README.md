# Local In-Process RAG & Inference Microservice

A production-grade, containerized Retrieval-Augmented Generation (RAG) backend engineered to run entirely local workloads without external API dependencies or third-party cloud wrappers. 

---

## 🏗️ Architectural Overview

[ Raw Documents (.txt/.md) ]
│
▼
[ ingest.py ] ──► Sliding Window Chunking ──► Sentence-Transformers (all-MiniLM-L6-v2)
│
▼
ChromaDB (Persistent SQLite / HNSW)
│
▼
[ Client / UI ] ──► FastAPI Gateway (/rag/query) ◄── Hugging Face (Flan-T5-Small)
(Pydantic Schema Validation)

---

## 🚀 Key Engineering Highlights
* **Zero External Cloud Dependencies:** Runs local embedding generation and sequence-to-sequence text synthesis using raw Hugging Face `transformers` and PyTorch tensors.
* **Persistent Vector Storage:** Utilizes ChromaDB with disk-backed SQLite indexes to maintain state across application reboots.
* **Asynchronous REST Gateway:** Exposes core inference pipelines through FastAPI with strict Pydantic validation and a built-in health-check route.
* **Containerized Deployment:** Fully dockerized for isolated, reproducible execution environments.

---

## 🛠 Tech Stack
* **Language & Frameworks:** Python, FastAPI, PyTorch, Hugging Face `transformers`, `sentence-transformers`
* **Vector Store:** ChromaDB
* **DevOps & Tooling:** Docker, Uvicorn, Git/GitHub, GitHub Actions (CI/CD)

---

## ⚙️ Quickstart & Local Execution

1. **Clone the Repository & Install Dependencies:**
   ```bash
  git clone https://github.com/saurabh-MLE/MLE_Sprint.git
  cd MLE_Sprint
  pip install -r requirements.txt

Ingest Local Documents:
Place your reference documents inside the data/ directory and run:

Bash
python ingest.py

Launch the FastAPI Server:

Bash
python -m uvicorn rag_app:app --reload --host 127.0.0.1 --port 8000

Access the interactive Swagger documentation at: http://127.0.0.1:8000/docs

Run via Docker:

Bash
docker build -t local-rag-app:latest .
docker run -d -p 8000:8000 --name rag_container local-rag-app:latest
