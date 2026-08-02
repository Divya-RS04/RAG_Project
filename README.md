# 📚 Simple RAG (Retrieval-Augmented Generation) System using LangChain, FAISS & FLAN-T5

A beginner-friendly implementation of a **Retrieval-Augmented Generation (RAG)** system using Python. This project demonstrates how to retrieve relevant information from a custom knowledge base using semantic search (FAISS + Sentence Transformers) and generate accurate answers using Google's FLAN-T5 language model.

---

## 🚀 Features

- 📄 Load knowledge from a text file
- ✂️ Split documents into semantic chunks
- 🧠 Generate embeddings using Sentence Transformers
- 🔍 Store and search embeddings with FAISS
- 🤖 Generate answers using Google FLAN-T5
- 💬 Interactive question-answering through the terminal
- ⚡ Runs completely on your local machine

---

## 🛠️ Technologies Used

- Python 3.10+
- LangChain
- LangChain Text Splitters
- Sentence Transformers
- FAISS
- Hugging Face Transformers
- Google FLAN-T5 Small

---

## 📂 Project Structure

```
RAG_Project/
│
├── app.py                 # Main RAG application
├── my_knowledge.txt       # Knowledge base
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
└── venv/                  # Virtual environment (optional)

## 📖 How It Works

### Step 1 — Load Knowledge Base

The system reads the contents of `my_knowledge.txt`.

↓

### Step 2 — Split Text

The document is split into smaller chunks using LangChain's Recursive Character Text Splitter.

↓

### Step 3 — Generate Embeddings

Each chunk is converted into vector embeddings using the Sentence Transformer model:
all-MiniLM-L6-v2

↓

### Step 4 — Store in FAISS

All embeddings are stored inside a FAISS vector database for efficient similarity search.

↓

### Step 5 — User Query

The user's question is converted into an embedding.

↓

### Step 6 — Retrieve Relevant Chunks

FAISS finds the most relevant document chunks.

↓

### Step 7 — Generate Answer

The retrieved context and user question are passed to Google's FLAN-T5 model, which generates the final answer.

## To Run : streamlit run app.py

