# AI Document Assistant

This is a small FastAPI project that uses RAG architecture to ask questions over uploaded documents.

I built this project to practice Python, FastAPI, vector DB, document processing and LLM integration.

## What It Does

- Upload txt or pdf document
- Extract text from the document
- Split text into chunks
- Store chunks in Chroma vector DB
- Ask questions about uploaded document
- Retrieve related chunks
- Send question + context to LLM
- Return answer with sources

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Chroma DB
- pypdf
- OpenAI compatible API / GitHub Models
- GitHub Codespaces

## RAG Flow

```text
Upload document
↓
Extract text
↓
Chunk text
↓
Store chunks in vector DB
↓
Ask question
↓
Find related chunks
↓
Send context to LLM
↓
Return answer with sources
```

## Project Structure

```text
app/
  main.py
  api/v1/
    health.py
    documents.py
    questions.py
  services/
    text_extractor.py
    chunking_service.py
    vector_store_service.py
    llm_service.py

sample_documents/
requirements.txt
README.md
```

## Health

```http
GET /api/v1/health
```

## Upload Document

```http
POST /api/v1/documents
```

Body type:

```text
form-data
key: file
```

## Get Uploaded Documents

```http
GET /api/v1/documents
```

## Ask Question

```http
GET /api/v1/questions?question=What skills does John Doe have&max_results=3
```

## Install Packages

```bash
pip install -r requirements.txt
```

## Set Token

```bash
export GITHUB_TOKEN="your-token"
```

## Run API

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```



