# Document-Grounded AI Assistant

## Project Overview

This project is a full-stack AI-powered document assistant that allows users to upload documents (PDF/TXT) and interact with them through a chat interface.

The system uses Retrieval-Augmented Generation (RAG) combined with an agent-based workflow to ensure answers are grounded in uploaded documents, with proper citations and tool usage.

The goal is to demonstrate a production-like understanding of:

* RAG pipelines
* Agentic workflows
* Full-stack architecture
* Clean API design
* Source-grounded AI responses

---

## Core Idea

Users can:

1. Upload documents
2. Ask questions about their content
3. Receive accurate, grounded answers with citations
4. Use additional tools (summarization, calculation)

The assistant will NOT hallucinate and will explicitly say when information is not found in documents.

---

## System Architecture

### High-Level Flow

```
User (Next.js Frontend)
        │
        ▼
FastAPI Backend
        │
        ▼
LangGraph Agent
        │
 ┌──────┼──────────────┐
 ▼      ▼              ▼
RAG   Summarizer   Calculator
 │
 ▼
ChromaDB (Vector Store)
 │
 ▼
Embeddings (MiniLM)
```

---

## Backend Architecture

### FastAPI Responsibilities

* Handle document uploads
* Manage chat requests
* Interface with LangGraph agent
* Return structured responses with citations

### Main Modules

#### 1. API Layer

* `/upload` → Upload documents
* `/chat` → Ask questions
* `/documents` → List documents

---

#### 2. Ingestion Pipeline

When a document is uploaded:

```
PDF → Text Extraction → Chunking → Embeddings → Vector Storage
```

Chunking strategy:

* Recursive character splitting
* Chunk size: ~1000 tokens
* Overlap: ~200 tokens

---

#### 3. Vector Store (ChromaDB)

Stores:

* Document chunks
* Metadata (document name, page number, chunk ID)

Used for semantic retrieval during question answering.

---

#### 4. Embeddings Model

* sentence-transformers/all-MiniLM-L6-v2
* Free and lightweight
* Used for both documents and queries

---

## Agent Architecture (LangGraph)

The system uses a routing-based agent:

### Workflow

```
User Query
    │
    ▼
Router Node (LLM decides action)
    │
 ┌──┼───────────────┐
 ▼  ▼               ▼
RAG Summarize   Calculator
    │
    ▼
Final Answer Generator
```

---

### Agent Tools

#### 1. Retrieval Tool

Used when answering questions based on documents.

Example:

* "What is the refund policy?"
* "What does the contract say about termination?"

---

#### 2. Summarization Tool

Used when user requests summaries of full documents.

Example:

* "Summarize this PDF"
* "Give me a short overview of the handbook"

---

#### 3. Calculator Tool

Used for numerical reasoning.

Example:

* "What is 15% of 5000?"
* "Compute total budget allocation"

---

## Frontend Architecture (Next.js)

### Pages

#### 1. Upload Page

* Drag & drop documents
* View uploaded files

#### 2. Chat Page

* Chat interface (like ChatGPT)
* Displays responses
* Shows loading states

#### 3. Sources Panel

* Shows retrieved chunks
* Displays document name + page number
* Allows inspection of source text

---

## Key Features

### 1. Document Grounded QA

All answers are strictly based on retrieved context.

If no relevant information is found:

> "I couldn't find this information in the uploaded documents."

---

### 2. Citations

Every answer includes:

* Document name
* Chunk reference
* Optional page number

---

### 3. Agentic Decision Making

The system does not rely on a single LLM call.
It dynamically decides whether to:

* Retrieve information
* Summarize a document
* Perform calculations

---

### 4. Clean API Design

FastAPI endpoints are designed to be:

* Simple
* Predictable
* Easy to integrate with frontend

---

## Tech Stack

### Frontend

* Next.js
* TypeScript
* TailwindCSS

### Backend

* FastAPI
* LangGraph

### AI / ML

* OpenAI GPT-4o-mini or GPT-4.1-mini (or local Ollama model)
* sentence-transformers MiniLM
* ChromaDB

---

## What Makes This Project Strong

This project demonstrates:

* Real RAG implementation (not just tutorial level)
* Agent-based AI system (LangGraph)
* Proper system design and separation of concerns
* Production-style API architecture
* Source-grounded AI responses with citations
* Full-stack integration

---

## Possible Improvements (If Time Allows)

* Streaming responses (token-by-token)
* Authentication system
* Better reranking of retrieved chunks
* Hybrid search (keyword + semantic)
* Docker setup for one-command startup

---

## Summary

This project is designed to simulate a real-world AI assistant that can be deployed in production environments. It focuses on correctness, traceability, and system design rather than feature overload.
