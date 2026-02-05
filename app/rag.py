import os
from config import DOCS_PATH, ENABLE_RAG, EMBEDDING_MODEL, FAISS_PATH
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

_vectorstore = None


def _ensure_faiss_dir():
    os.makedirs(FAISS_PATH, exist_ok=True)


def _get_embeddings():
    return OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url="http://localhost:11434"
    )


def _build_vectorstore():
    global _vectorstore

    if not os.path.exists(DOCS_PATH):
        return None

    docs = []

    for file in os.listdir(DOCS_PATH):
        if not file.endswith(".txt"):
            continue

        path = os.path.join(DOCS_PATH, file)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        for chunk in splitter.split_text(text):
            docs.append(
                Document(
                    page_content=chunk,
                    metadata={"source": file}
                )
            )

    if not docs:
        return None

    _ensure_faiss_dir()

    embeddings = _get_embeddings()
    _vectorstore = FAISS.from_documents(docs, embeddings)
    _vectorstore.save_local(FAISS_PATH)

    return _vectorstore


def _load_vectorstore():
    global _vectorstore

    if not os.path.exists(FAISS_PATH):
        return None

    embeddings = _get_embeddings()

    try:
        _vectorstore = FAISS.load_local(
            FAISS_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
        return _vectorstore
    except Exception:
        return None


def retrieve_context(query, top_k=3):
    if not ENABLE_RAG:
        return None

    global _vectorstore

    if _vectorstore is None:
        if _load_vectorstore() is None:
            if _build_vectorstore() is None:
                return None

    results = _vectorstore.similarity_search(query, k=top_k)
    if not results:
        return None

    return (
        "Use the following context if relevant:\n"
        + "\n---\n".join(r.page_content for r in results)
    )
