from memory import init_db, ensure_user, save_message, load_history
from llm import chat
from rag import retrieve_context

USER_ID = "demo-user"

def main():
    init_db()
    ensure_user(USER_ID)

    print("Chatbot ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("User : ")
        if user_input.lower() in ("exit", "quit"):
            break

        save_message(USER_ID, "user", user_input)

        history = load_history(USER_ID)

        context = retrieve_context(user_input)
        if context:
            history.insert(0, {"role": "system", "content": context})

        answer = chat(history)

        save_message(USER_ID, "assistant", answer)
        print("Assistant :", answer)

if __name__ == "__main__":
    main()
