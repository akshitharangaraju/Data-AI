# Healthcare Knowledge Chatbot (RAG + Vector Database)

This project implements a complete pipeline for ingesting healthcare documents, embedding them into a Pinecone vector database, and using a Retrieval-Augmented Generation (RAG) architecture to answer healthcare questions reliably using Google Gemini.

## Project Architecture

1. **`ingestion/`**: Contains the logic to load PDFs (`loader.py`), split the text into manageable chunks (`chunker.py`), and then embed those chunks using Gemini and push them to Pinecone with attached metadata (`embed_store.py`).
2. **`retrieval/`**: Uses `search.py` to embed user questions and fetch the top K most semantically similar chunks from Pinecone.
3. **`chatbot/`**: Provides the chat loop and Gemini response generation in `chatbot.py`. It feeds the retrieved chunks into Gemini to provide grounded context.
4. **`data/`**: The folder you place your PDF healthcare guidelines or documents.

## Setup Instructions

1. **Virtual Environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Environment Keys**:
   Make sure you have set `PINECONE_API_KEY`, `GEMINI_API_KEY`, and `INDEX_NAME` in the `.env` file. Do not commit your `.env` to GitHub.
4. **Vector Database**:
   Verify an index with the name provided in `INDEX_NAME` exists in Pinecone, using dimension `768` (for text-embedding-004 model) or `768` for standard genai.

## Running the Application

Execute the **`main.py`** entry point.

```bash
python main.py
```

- **Option 1**: Parses PDFs from `data/`, chunks them, generates embeddings, and uploads everything into Pinecone.
- **Option 2**: Launches the Chatbot for you to test your RAG system directly from the terminal.
