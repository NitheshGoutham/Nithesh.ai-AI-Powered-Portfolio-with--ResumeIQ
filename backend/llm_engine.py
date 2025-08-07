# backend/llm_engine.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"  # You must run: `ollama run phi3`

def query_local_llm(query: str, resume_data: dict) -> str:
    prompt = f"""
You are a helpful assistant. Based on the following resume data, answer the question accurately.

Resume:
{resume_data}

Question:
{query}

Answer:
"""
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json().get("response", "Sorry, no response generated.")
    except Exception as e:
        return f"Error: {str(e)}"
