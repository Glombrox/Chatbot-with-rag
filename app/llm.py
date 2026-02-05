import requests
from groq import Groq
from config import *

client = Groq(api_key=GROQ_API_KEY)

def local_chat(messages):
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": LOCAL_MODEL,
            "messages": messages,
            "stream": False
        }
    )
    response.raise_for_status()
    data = response.json()
    return data["message"]["content"]

def cloud_chat(messages):
    response = client.chat.completions.create(
        model=CLOUD_MODEL,
        messages=messages
    )
    return response.choices[0].message.content

def chat(messages, use_local: bool = USE_LOCAL):
    if use_local:
        return local_chat(messages)
    else:
        return cloud_chat(messages)
