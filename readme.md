# Chatbot with Local/Cloud LLM and RAG

This is a chatbot built with **Python**, **Streamlit**, **SQLite**, and **RAG (Retrieval-Augmented Generation)**.  
It supports both **local and cloud LLMs**, stores chat history in a **SQLite database**, and can optionally use **document context** to provide smarter answers.

---

## Features

- **Local & Cloud LLMs**: Switch between running a model locally or in the cloud.
- **Memory**: Stores conversations in a SQLite database per user.
- **RAG (Optional)**: Use documents as references for more informative responses.
- **Streamlit UI**: Interactive web interface for chatting.
- **User Management**: Each user has separate conversation history.
- **Reset Chat**: Clear the chat screen while keeping database history.

---

## Project Structure

``` plain text
.
chatbot/
├── app/
│ ├── main.py # Entry point (CLI)
│ ├── streamlit_ui.py # Streamlit UI
│ ├── llm.py # Local / Cloud LLM inference
│ ├── memory.py # SQLite memory
│ ├── rag.py # RAG logic
│ └── config.py # Config & switches
├── data/
│ ├── chat_memory.db # SQLite DB (gitignored)
│ └── documents/ # Text files for RAG
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```
## Installation (Local)

1. **Clone the repository:**
``` bash
git clone https://github.com/Glombrox/Chatbot.git
cd chatbot
```

2. **Create a python virtual environment:**
``` bash
python -m venv .venv
source venv/scripts/activate   # linux/macOS
venv/scripts/activate          # windows
```

3. **Install Dependencies:**
``` bash
pip install -r requirements.txt
```

4. **Create a `.env` file and set your API KEYS**:
``` ini
GROQ_API_KEY=your-groq-api-key
OLLAMA_API_KEY=your-ollama-api-key
```

5. **Run streamlit UI:**
``` bash
streamlit run app/streamlit_ui.py
```
The app will open in your browser at `http://localhost:8501`.

---

## Using the chatbot

- Enter a user ID to start a conversation.

- Use the sidebar to toggle:

  - Use Local LLM → run inference locally.

  - Enable RAG → allow the bot to read documents for context.

- Reset Chat clears the chat window without deleting DB history.

- Your chat history is stored per user in `data/chat_memory.db`.

---

## Adding Documents for RAG

1. Place `.txt` files in the `data/documents/` folder.
2. The chatbot will automatically split, embed, and store them for similarity search.
3. When RAG is enabled, relevant document content is added to the conversation.

---

## Important Notes

- **Local vs Cloud LLM**: You can switch models anytime via the UI. FAISS embeddings are independent of model choice.

- **FAISS Persistence**: Vector store is saved in `data/faiss_index/`.

- **Chat History**: Stored in SQLite for all users `data/chat_memory.db`.

---

## Docker Usage

1. **Build and start with docker compose**
``` bash
docker-compose up --build
```
2. **Open your browser at https://localhost:8501**
> Note:Make sure `.env` and `data/documents/` are accessible to Docker.

> FAISS indexes will be built automatically if missing.
