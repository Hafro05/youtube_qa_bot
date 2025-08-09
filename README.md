# 🎥 YouTube Q&A Bot (Local & Free)

A local, free question-answering bot for YouTube videos — fetches transcripts, stores embeddings, and uses a local LLM (Ollama) to answer your questions.

## 🚀 Features
- Works **offline** after first run (no API costs)
- Handles **multiple languages** (falls back if English not available)
- Uses **FAISS** for fast transcript search
- Supports **lightweight local models** (e.g., `gemma:2b`, `phi3:3.8b`)
- Modular file structure for easy extensions

---

## 📂 Project Structure
```
youtube_qa_bot/
├── main.py
├── config.py
├── requirements.txt
├── ingestion/
├── retriever/
├── qa/
├── data/
└── ui/
```

---

## ⚙️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/youtube_qa_bot.git
cd youtube_qa_bot
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Ollama

* Download from https://ollama.ai/download

* Pull a lightweight model:
```bash
ollama pull gemma:2b
```

## ▶️ Usage
```bash
python main.py
```
1. Paste a YouTube URL.

2. Wait for transcript + embedding.

3. Ask your question.

## 🛠 Configuration

Edit config.py to change:

* Embedding model

* LLM model

* Data paths

## ⚡ Speed Tips

* Use a smaller model: gemma:2b or tinyllama:1.1b

* Reduce chunk_size in chunker to embed less text

* Keep FAISS index on disk — skip re-embedding if already exists

## 📜 License

MIT License
