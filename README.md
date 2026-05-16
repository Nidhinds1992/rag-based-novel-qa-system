# Enterprise RAG Chatbot using LangChain + Ollama + FastAPI + Streamlit

## Features
- Local LLM using Ollama Llama3
- FAISS Vector Database
- HuggingFace Embeddings
- FastAPI Backend
- Streamlit Frontend
- End-to-End RAG Pipeline

## Tech Stack
- Python
- LangChain
- Ollama
- FAISS
- FastAPI
- Streamlit

## Run Backend

```bash
uvicorn backend_noval:app --reload
```

## Run Frontend

```bash
streamlit run frontend_noval.py
```

## Model Used
- llama3:8b

## Embedding Model
- all-MiniLM-L6-v2