import os
import google.generativeai as genai
import streamlit as st

# Safe helper to get secrets or environment variables
def get_secret(key: str, default: str = None):
    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key, default)

# Load Gemini API key and model
GEMINI_API_KEY = get_secret("GEMINI_API_KEY")
GEMINI_MODEL = get_secret("GEMINI_MODEL", "gemini-1.5-flash")  # default model

# Configure Gemini
if not GEMINI_API_KEY:
    st.error("❌ Gemini API key not found. Set it in Render's Environment Variables or in .streamlit/secrets.toml")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# Initialize model
model = genai.GenerativeModel(GEMINI_MODEL)

def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return its response."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
