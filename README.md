# 🩺 MedRAG AI: An Intelligent Research Assistant for Medical AI Papers

> **Final Project for DataTalksClub LLM Zoomcamp 2026**

MedRAG AI is an end-to-end **Retrieval-Augmented Generation (RAG)** application that enables researchers, students, and healthcare professionals to interact with a curated collection of Medical AI research papers using natural language.

Instead of manually searching through hundreds of pages of scientific literature, users can ask questions and receive AI-generated answers grounded in relevant research papers retrieved from a semantic vector database.

---

# 📖 Overview

MedRAG AI combines modern Large Language Models (LLMs) with semantic retrieval techniques to produce reliable, evidence-based answers from scientific publications.

The system uses:

- 📚 ChromaDB for semantic document retrieval
- 🤖 Google Gemini 2.5 Flash for answer generation
- 🔍 Sentence Transformers for embeddings
- ⚡ FastAPI for the backend REST API
- 🎨 Streamlit for the interactive web interface

The project demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline from document ingestion to answer generation with source citation.

---

# ✨ Features

- 📄 PDF document ingestion
- 📑 Automatic text extraction
- ✂️ Intelligent document chunking
- 🧠 Sentence Transformer embeddings
- 📚 ChromaDB vector database
- 🔍 Semantic similarity search
- 🤖 Google Gemini integration
- 📄 Source citation with retrieved document chunks
- ⚡ FastAPI REST API
- 🎨 Streamlit web application
- 📊 Evaluation pipeline
- 📥 Download generated answers
- 🐳 Docker support (in progress)

---

# 🏗️ System Architecture

```text
                User
                  │
                  ▼
         Streamlit Web UI
                  │
                  ▼
            FastAPI Backend
                  │
                  ▼
          Semantic Retriever
                  │
                  ▼
             ChromaDB
                  │
                  ▼
       Relevant Document Chunks
                  │
                  ▼
           Prompt Construction
                  │
                  ▼
      Google Gemini 2.5 Flash
                  │
                  ▼
      AI-generated Answer + Sources
```

---

# 📂 Project Structure

```text
LLM-Zoomcamp2026-Final-Project/

├── app/
│   ├── main.py
│   ├── service.py
│   ├── schemas.py
│   └── config.py
│
├── rag/
│   ├── embedding.py
│   ├── retriever.py
│   ├── prompt.py
│   ├── llm.py
│   └── vector_store.py
│
├── ui/
│   └── app.py
│
├── evaluation/
│
├── scripts/
│
├── chroma_db/
│
├── data/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.12 |
| LLM | Google Gemini 2.5 Flash |
| Backend | FastAPI |
| Frontend | Streamlit |
| Embeddings | Sentence Transformers |
| Vector Database | ChromaDB |
| PDF Processing | PyMuPDF |
| Machine Learning | PyTorch |
| Data Processing | Pandas, NumPy |
| API Validation | Pydantic |
| Containerization | Docker |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/LLM-Zoomcamp2026-Final-Project.git

cd LLM-Zoomcamp2026-Final-Project
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

MODEL_NAME=gemini-2.5-flash

CHROMA_PATH=chroma_db

API_URL=http://127.0.0.1:8000/ask
```

---

# ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

Start Streamlit:

```bash
streamlit run ui/app.py
```

Open:

```
http://localhost:8501
```

---

# 📊 Evaluation

Run the evaluation pipeline:

```bash
python -m evaluation.evaluate
```

The evaluation generates:

```
evaluation/results.csv
```

including:

- Response time
- Retrieved documents
- Average retrieval distance
- Answer length

---

# 📡 API Endpoint

### POST `/ask`

Request

```json
{
  "question": "What is deep learning in chest X-ray analysis?"
}
```

Response

```json
{
  "question": "...",
  "answer": "...",
  "sources": [
    {
      "filename": "...",
      "chunk_id": 1,
      "distance": 0.54,
      "text": "..."
    }
  ]
}
```

---

# 🚧 Current Project Status

| Phase | Status |
|---------|--------|
| ✅ Phase 1 – Project Setup | Completed |
| ✅ Phase 2 – PDF Processing | Completed |
| ✅ Phase 3 – Chunking | Completed |
| ✅ Phase 4 – Embeddings | Completed |
| ✅ Phase 5 – ChromaDB | Completed |
| ✅ Phase 6 – Semantic Retrieval | Completed |
| ✅ Phase 7 – Prompt Engineering | Completed |
| ✅ Phase 8 – Google Gemini Integration | Completed |
| ✅ Phase 9 – FastAPI Backend | Completed |
| ✅ Phase 10 – Streamlit Interface | Completed |
| ✅ Phase 11 – Evaluation Pipeline | Completed |
| 🚧 Phase 12 – Documentation | In Progress |
| ⏳ Phase 13 – Deployment | Planned |

---

# 🔮 Future Improvements

- Hybrid Retrieval (BM25 + Semantic Search)
- Cross-encoder document reranking
- Multi-turn conversational memory
- Medical image support
- User authentication
- Cloud deployment
- Feedback collection
- Retrieval metrics dashboard

---
## 📚 Documentation

Additional project documentation is available in the `docs/` folder:

| Document | Description |
|----------|-------------|
| `docs/METHOD_AND_PROCEDURE.md` | Development methodology and step-by-step procedures |
| `docs/API.md` | FastAPI endpoints and request/response examples |
| `docs/INSTALLATION.md` | Installation and setup instructions |
| `docs/ARCHITECTURE.md` | System architecture and workflow diagrams |
| `docs/EVALUATION.md` | Evaluation methodology and performance metrics |
---

# 👩‍💻 Author

**Jocelyn Dumlao**

Independent Data Scientist| Machine Learning Engineer

Medical AI • Machine Learning • NLP • LLM • Retrieval-Augmented Generation

---

# 📄 License

This project is released under the **MIT License**.