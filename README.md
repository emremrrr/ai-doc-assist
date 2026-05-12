# aidocassist

# AI Document Assistant

This is a small FastAPI project that uses RAG architecture to ask questions over uploaded documents.

I built this project to practice Python, FastAPI, vector DB, document processing and LLM integration.

## What it does

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


## Project Structure

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
API Endpoints
Health

## Upload document

POST /api/v1/documents

Body type:

form-data
key: file

Get uploaded documents

GET /api/v1/documents
 
Ask question

GET /api/v1/questions?question=....&max_results=3

Install packages:

pip install -r requirements.txt

Set token:

export GITHUB_TOKEN="your-token"

Run API:

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000