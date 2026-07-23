# 🩺 MedRAG AI Development Methodology

## Method and Procedure

This document describes the step-by-step methodology followed to develop **MedRAG AI**, an intelligent Retrieval-Augmented Generation (RAG) system for answering questions from Medical AI research papers.

---

# Development Workflow

The project was developed incrementally using thirteen phases.

```
Phase 1
↓

Phase 2
↓

Phase 3

...

↓

Phase 13
```

Each phase builds upon the previous one, resulting in a complete RAG application.

---

# Phase 1 — Project Setup

## Goal

Create the project structure and configure the Python development environment.

## Objectives

- Initialize the project repository
- Create a virtual environment
- Install required libraries
- Organize folders
- Configure environment variables

## Outputs

- Python project
- requirements.txt
- .env
- Initial folder structure

---

# Phase 2 — PDF Processing

## Goal

Extract text from Medical AI research papers.

## Procedure

1. Load PDF documents.
2. Read each page using PyMuPDF.
3. Extract textual content.
4. Store extracted text.

## Output

Clean document text ready for preprocessing.

---

# Phase 3 — Document Chunking

## Goal

Split long research papers into manageable chunks.

## Procedure

1. Read extracted text.
2. Divide into overlapping chunks.
3. Preserve contextual continuity.
4. Assign chunk identifiers.

## Output

Document chunks with metadata.

Example

```
Chunk 0
Chunk 1
Chunk 2
...
```

---

# Phase 4 — Embeddings

## Goal

Convert document chunks into vector representations.

## Procedure

1. Load Sentence Transformer.
2. Encode each chunk.
3. Generate dense embeddings.
4. Store vectors.

## Model

Sentence Transformers

Example

```
Text

↓

Embedding Model

↓

768-dimensional Vector
```

---

# Phase 5 — ChromaDB

## Goal

Store embeddings inside a vector database.

## Procedure

1. Initialize ChromaDB.
2. Create collection.
3. Insert vectors.
4. Save metadata.

Metadata includes

- filename
- chunk_id
- document text

---

# Phase 6 — Semantic Retrieval

## Goal

Retrieve the most relevant document chunks.

## Procedure

1. Encode user query.
2. Compare query embedding against ChromaDB.
3. Rank nearest vectors.
4. Return Top-K chunks.

Output

```
Question

↓

Embedding

↓

ChromaDB Search

↓

Top 5 Documents
```

---

# Phase 7 — Prompt Engineering

## Goal

Construct prompts for the LLM using retrieved documents.

## Procedure

1. Receive user question.
2. Insert retrieved passages.
3. Add system instructions.
4. Build the final prompt.

Template

```
Context

Question

Instructions

Answer
```

---

# Phase 8 — Google Gemini Integration

## Goal

Generate grounded responses using Google Gemini.

## Procedure

1. Send prompt to Gemini.
2. Generate response.
3. Return answer.
4. Preserve retrieved citations.

Model

```
gemini-2.5-flash
```

---

# Phase 9 — FastAPI Backend

## Goal

Expose the RAG system through REST APIs.

## Endpoints

### GET /

Health message

### GET /health

API status

### POST /ask

Accepts

```json
{
  "question":"..."
}
```

Returns

```json
{
  "answer":"...",
  "sources":[]
}
```

---

# Phase 10 — Streamlit Interface

## Goal

Develop an interactive web application.

## Features

- Question input
- AI answer display
- Retrieved documents
- Similarity score
- Download answer
- API status
- Sidebar information

Workflow

```
User

↓

Streamlit

↓

FastAPI

↓

Gemini

↓

Answer
```

---

# Phase 11 — Evaluation Pipeline

## Goal

Evaluate the performance of the RAG system.

## Metrics

- Response Time
- Number of Retrieved Documents
- Average Retrieval Distance
- Answer Length

Output

```
results.csv
```

---

# Phase 12 — Documentation

## Goal

Document every component of the project.

Deliverables

- README
- Development Guide
- Architecture
- Installation Guide
- API Documentation
- Evaluation Guide

---

# Phase 13 — Deployment

## Goal

Deploy MedRAG AI for public use.

Planned Platforms

- Docker
- Hugging Face Spaces
- Streamlit Community Cloud
- Render
- Railway

Future Improvements

- Authentication
- Conversation Memory
- Hybrid Retrieval
- Re-ranking
- Medical Image Support

---

# Complete System Workflow

```
Medical Research Papers
          │
          ▼
PDF Processing
          │
          ▼
Document Chunking
          │
          ▼
Sentence Embeddings
          │
          ▼
ChromaDB
          │
          ▼
User Question
          │
          ▼
Semantic Retrieval
          │
          ▼
Prompt Construction
          │
          ▼
Google Gemini
          │
          ▼
Generated Answer
          │
          ▼
FastAPI
          │
          ▼
Streamlit Interface
          │
          ▼
User
```

---

# Summary

The MedRAG AI project was developed through a structured thirteen-phase methodology that progressively built a complete Retrieval-Augmented Generation (RAG) system. Starting from project setup and document processing, the workflow advanced through semantic retrieval, prompt engineering, LLM integration, API development, user interface implementation, evaluation, and documentation. The final phase focuses on deployment, enabling the application to become a production-ready medical research assistant.
