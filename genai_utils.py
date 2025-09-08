import os
import google.generativeai as genai
import streamlit as st

# Load Gemini API key and model from Streamlit secrets or environment variables
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
GEMINI_MODEL = st.secrets.get("GEMINI_MODEL", os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))  # default model

# Configure Gemini
if not GEMINI_API_KEY:
    st.error("Gemini API key not found. Please set it in Render environment variables or .streamlit/secrets.toml")
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
