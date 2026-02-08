import os
from dotenv import load_dotenv

load_dotenv()


USE_LOCAL = os.getenv("USE_LOCAL", "true").lower() == "true"


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
LOCAL_MODEL = os.getenv("LOCAL_MODEL", "llama3.1:latest")


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
CLOUD_MODEL = os.getenv("CLOUD_MODEL", "llama-3.1-8b-instant")

EMBEDDING_MODEL = "nomic-embed-text"

ENABLE_RAG = os.getenv("ENABLE_RAG", "true").lower() == "true"
FAISS_PATH = "data/faiss_index"


DB_PATH = "data/chat_memory.db"
DOCS_PATH = "data/documents"
