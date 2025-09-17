# 📄 HR Assistance System - FastAPI Version

This is a FastAPI-based backend application that provides an HR assistance system using LangChain, document embeddings, and a large language model (LLM). It accepts natural language queries and returns relevant answers based on your PDF or JSON document data.

---

## Features

- Loads and processes PDF or JSON documents as knowledge base.
- Splits documents into chunks for better retrieval.
- Creates an embedding-based vector store for efficient search.
- Uses a pre-trained LLM for generating answers.
- Provides a REST API endpoint to ask HR-related questions.

---

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

1. Clone the repository or copy the code.

2. Install dependencies:

```bash
pip install fastapi uvicorn
# Also install your existing requirements for langchain, embeddings, etc.


Make sure your document loading and LLM setup files (rag_loader.py, text_splitter.py, embedding_vectorstore.py, llm_setup.py, qa_system.py) are in place.

Running the Application

Run the FastAPI app using Uvicorn:  uvicorn main:app --reload

Example using curl: curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the leave policy?"}'




