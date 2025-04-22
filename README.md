
# PDF-RAG with DeepSeek LLM

A lightweight PDF Question Answering app built using DeepSeek LLM and LangChain with Streamlit frontend.

## 🔍 Overview

This project allows users to upload a PDF document and ask natural language questions about its content. The app processes the PDF, splits the content into chunks, embeds them into a vector database using FAISS and DeepSeek embeddings, and retrieves the most relevant chunks to generate answers using DeepSeek LLM.

## 🚀 Features

- Upload any PDF
- Chunk and embed content using LangChain
- Semantic search using FAISS
- LLM-based question answering using DeepSeek
- Streamlit-based intuitive UI

## 📂 Project Structure

```
RAG_WITH_DEEPSEEK/
│
├── deepseek/
│   ├── vector_databases.py      # Loads, chunks, embeds PDF content
│   ├── Rag_pipeline.py          # Retrieval + QA logic
│   ├── frontend.py              # Streamlit app
│   └── requirements.txt
│
├── pdfs/                        # PDF upload folder
├── vectorstore/                 # FAISS vector database folder
├── data.pdf                     # Sample PDF
├── .env                         # Environment variables
└── README.md
```

## ⚙️ How It Works

1. Upload a PDF using the Streamlit UI.
2. PDF is parsed using `PDFPlumberLoader`.
3. Content is chunked via `RecursiveCharacterTextSplitter`.
4. Chunks are embedded using `DeepSeek` embeddings via `OllamaEmbeddings`.
5. Chunks are stored in a FAISS vector store.
6. On a user query, relevant chunks are retrieved and passed to DeepSeek LLM for answering.

## 🧰 Installation

```bash
git clone https://github.com/your-username/pdf-rag-deepseek.git
cd pdf-rag-deepseek
python -m venv deepseek
source deepseek/bin/activate  # or .\deepseek\Scripts\activate on Windows
pip install -r requirements.txt
```

## 🏃 Usage

```bash
streamlit run frontend.py
```

## 📝 Requirements

Check `requirements.txt` for full list.

## 🏷️ Tags

`RAG`, `LangChain`, `DeepSeek`, `Streamlit`, `Vector Database`, `LLM`, `PDF`, `FAISS`

## 📄 License

MIT License
