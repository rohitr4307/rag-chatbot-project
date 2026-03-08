An **AI-powered Retrieval-Augmented Generation (RAG) chatbot** that allows users to upload PDF documents and ask natural language questions.
The system retrieves relevant document sections using **vector similarity search (FAISS)** and generates accurate answers using a **Large Language Model (LLM)**.

Built with **LangChain, OpenAI/NVIDIA Nemotron, FAISS, and Gradio**.

---

# 🚀 Live Demo

*(Optional if deployed)*

```text
https://your-demo-link.gradio.app
```

---

# 🧠 How It Works

This project implements a **Retrieval-Augmented Generation (RAG) pipeline**.

1️. User uploads PDF documents
2️. Documents are **split into chunks**
3️. Chunks are converted into **vector embeddings**
4️. Embeddings are stored in **FAISS vector database**
5️. User question is converted into an embedding
6️. Similar document chunks are retrieved
7️. Retrieved context is sent to **LLM**
8️. LLM generates an accurate answer

---

# 🏗 Architecture

```text
          User Question
                │
                ▼
        Question Embedding
                │
                ▼
        FAISS Vector Search
                │
                ▼
      Relevant Document Chunks
                │
                ▼
        Prompt + Context
                │
                ▼
           LLM (Nemotron/OpenAI)
                │
                ▼
            Generated Answer
```

---

# ⚙️ Tech Stack

| Technology               | Purpose                    |
| ------------------------ | -------------------------- |
| Python                   | Core programming language  |
| LangChain                | RAG pipeline orchestration |
| FAISS                    | Vector similarity search   |
| OpenAI / NVIDIA Nemotron | LLM for answer generation  |
| Gradio                   | Chat UI interface          |
| PyPDF                    | PDF document loader        |
| tiktoken                 | Tokenization               |

---

# 📂 Project Structure

```text
rag-chatbot-project
│
├── app_v2_.py
│   └── Gradio UI (ChatGPT-style interface)
│
├── rag_chatbot_project.py
│   └── RAG pipeline and conversation logic
│
├── src
│   ├── loader.py
│   │   └── PDF loading and chunking
│   │
│   └── database.py
│       └── FAISS vector database creation
│
├── data
│   └── Sample PDFs
│
├── faiss_index
│   └── Saved vector embeddings
│
├── requirements.txt
└── README.md
```

---

# 💡 Key Features

✅ Upload **multiple PDF documents**
✅ Ask questions in **natural language**
✅ **Context-aware answers** using RAG
✅ **Vector similarity search** with FAISS
✅ **ChatGPT-style interface** using Gradio
✅ **Source document retrieval**
✅ Efficient document chunking

---

# 🖥 Example Usage

### Upload Documents

```text
Employment Contract.pdf
HR Policy.pdf
Company Handbook.pdf
```

### Ask Questions

```text
"What is the notice period mentioned in the contract?"
```

### AI Response

```text
The employment contract specifies a notice period of 60 days
for employee resignation.
```

---

# ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/rag-chatbot-project.git
```

Move into the project folder:

```bash
cd rag-chatbot-project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```text
OPENAI_API_KEY=your_api_key
```

Run the application:

```bash
python app.py
```

---

# 🧪 Example Interface

<img width="899" height="449" alt="Screenshot 2026-03-05 160334" src="https://github.com/user-attachments/assets/d11cb9bd-cddf-4b6c-a170-e44fcc23373d" />

Example:

```
📄 Chat with your PDFs

User:
What is the termination policy?

Bot:
The document states that termination requires a written
notice of 60 days from either party.
```

---

# 📈 Future Improvements

* Streaming responses (ChatGPT-style typing)
* Support for **DOCX / CSV / Websites**
* Persistent vector database
* Semantic caching
* Multi-user sessions
* Docker deployment
* Cloud hosting (HuggingFace / AWS)

---

# 👨‍💻 Author

**Rohit Ranjan**

AI / Data Science Professional

LinkedIn:

```
[https://www.linkedin.com/in/rohitranjan4307/]
```

GitHub:

```
[https://github.com/rohitr4307]
```

---

# ⭐ If You Like This Project

Give it a ⭐ on GitHub!

---
