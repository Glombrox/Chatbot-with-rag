# Mark app as a package and expose key modules/functions for easier imports

from .memory import init_db, ensure_user, save_message, load_history

from .llm import chat, local_chat, cloud_chat

from .rag import retrieve_context

from .config import USE_LOCAL, ENABLE_RAG, LOCAL_MODEL, CLOUD_MODEL, OLLAMA_URL, DOCS_PATH, DB_PATH
