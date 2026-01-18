Medical Retrieval-Augmented Generation (RAG) System

This project is an industry-ready Medical Question Answering system built using Retrieval-Augmented Generation (RAG).
It allows users to ask natural language questions over medical research PDFs and generates grounded, source-attributed answers using a local LLM (Ollama).

🚀 Key Features

📄 Medical PDF ingestion

✂️ Text cleaning & chunking

🧠 Semantic embeddings (Sentence Transformers)

📦 FAISS vector database for fast retrieval

🔍 Context-aware semantic search

🤖 Local LLM inference using Ollama (privacy-preserving)

🚫 Hallucination control (answers only from documents)

📚 Page-level source attribution

🖥️ Streamlit UI for live demo

🧠 System Architecture (High Level)
User Question
     ↓
Streamlit UI
     ↓
RAG Pipeline
     ↓
Semantic Retriever (FAISS)
     ↓
Relevant Text Chunks
     ↓
Prompt Construction
     ↓
Local LLM (Ollama)
     ↓
Grounded Answer + Sources

🏗️ Detailed Architecture Diagram
┌──────────────────┐
│   Medical PDFs   │
└────────┬─────────┘
         ↓
┌────────────────────────┐
│ PDF Loader (PyMuPDF)   │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ Text Cleaner           │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ Chunker (Overlap)      │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ Embeddings Generator   │
│ (SentenceTransformers) │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ FAISS Vector Store     │
│ (Text + Metadata)     │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ Semantic Retriever     │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ Prompt Builder         │
│ (Context + Guardrails) │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ Ollama LLM (Local)     │
│ gemma3:4b              │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ Answer + Source Pages  │
└────────────────────────┘

📁 Project Structure
rag-medical-qa/
│
├── data/
│   └── pdfs/                    # Medical PDFs
│
├── data_ingestion/
│   └── pdf_loader.py            # Extract text from PDFs
│
├── processing/
│   ├── text_cleaner.py          # Clean raw text
│   └── chunker.py               # Chunk text with overlap
│
├── vector_store/
│   ├── embedder.py              # Generate embeddings
│   └── faiss_store.py           # FAISS index handling
│
├── retriever/
│   └── semantic_retriever.py    # Semantic search
│
├── llm/
│   └── ollama_client.py         # Local LLM interface
│
├── rag/
│   └── rag_pipeline.py          # End-to-end RAG logic
│
├── app/
│   └── app.py                   # Streamlit UI
│
├── tests/
│   ├── test_embeddings.py       # Build FAISS index
│   └── test_rag_llm.py           # Full RAG test
│
└── README.md

🧩 Module-by-Module Explanation
1️⃣ PDF Loader (pdf_loader.py)

Uses PyMuPDF

Extracts text page-by-page

Preserves document name & page number

Why?
Page-level granularity is required for traceable answers.

2️⃣ Text Cleaner (text_cleaner.py)

Removes extra whitespace

Normalizes formatting

Keeps medical terminology intact

Why?
Cleaner text improves embedding quality.

3️⃣ Chunker (chunker.py)

Splits text into overlapping chunks

Prevents context loss across boundaries

Why?
LLMs perform better on short, coherent chunks.

4️⃣ Embedder (embedder.py)

Uses Sentence-Transformers (MiniLM)

Converts text into dense vectors

Why?
Enables semantic search, not keyword search.

5️⃣ FAISS Vector Store (faiss_store.py)

Stores embeddings + metadata + actual text

Enables fast similarity search

Why FAISS?

Scales well

Industry standard

CPU-efficient

6️⃣ Semantic Retriever (semantic_retriever.py)

Converts query → embedding

Retrieves top-K relevant chunks

Why?
Ensures only relevant medical context is passed to the LLM.

7️⃣ RAG Pipeline (rag_pipeline.py)

Orchestrates retrieval + generation

Builds hallucination-safe prompts

Returns answer + sources

Key Design Choice:
LLM sees only retrieved content, nothing else.

8️⃣ Ollama Client (ollama_client.py)

Runs local LLM via CLI

UTF-8 safe for Windows

No API keys required

Why Ollama?

Offline

Privacy-preserving

Cost-free

Ideal for medical data

9️⃣ Streamlit UI (app.py)

Interactive web interface

Displays answer + sources

Optional context inspection

Why Streamlit?

Fast prototyping

Perfect for interviews & demos

🔐 Hallucination Control Strategy

LLM instructed to:

“Answer ONLY using the provided context”

If information is missing → explicit fallback

No external knowledge injection

🧪 How to Run
1️⃣ Build embeddings
python -m tests.test_embeddings

2️⃣ Run full RAG test
python -m tests.test_rag_llm

3️⃣ Launch UI
streamlit run app/app.py
------>Local URL: http://localhost:8501------->
