import streamlit as st
from memory import init_db, ensure_user, save_message, load_history
from llm import chat as llm_chat, USE_LOCAL
from rag import retrieve_context, ENABLE_RAG


init_db()

st.set_page_config(page_title="Chatbot Demo", layout="centered")


if "user_id" not in st.session_state:
    st.session_state.user_id = "demo-user"

USER_ID = st.session_state.user_id
ensure_user(USER_ID)


st.sidebar.title("Settings")

use_local = st.sidebar.checkbox("Use Local LLM", value=USE_LOCAL)
enable_rag = st.sidebar.checkbox("Enable RAG", value=ENABLE_RAG)


if "history" not in st.session_state:
    st.session_state.history = []

st.title("Chatbot Demo")

for msg in st.session_state.history:
    role = "You" if msg["role"] == "user" else "Assistant"
    st.markdown(f"**{role}:** {msg['content']}")

user_input = st.text_input("Type your message here:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Send") and user_input.strip():

        save_message(USER_ID, "user", user_input)
        st.session_state.history.append(
            {"role": "user", "content": user_input}
        )

        history = st.session_state.history.copy()

        if enable_rag:
            context = retrieve_context(user_input)
            if context:
                history.insert(
                    0,
                    {"role": "system", "content": context}
                )

        response = llm_chat(history, use_local=use_local)

        save_message(USER_ID, "assistant", response)
        st.session_state.history.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()

with col2:
    if st.button("Reset Chat (screen only)"):
        st.session_state.history = []
        st.rerun()
