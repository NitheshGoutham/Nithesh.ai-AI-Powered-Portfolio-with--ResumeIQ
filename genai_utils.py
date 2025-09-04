import os
import google.generativeai as genai
import streamlit as st

# Load key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Gemini model initialization
model = genai.GenerativeModel(st.secrets["GEMINI_MODEL"])

def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return its response."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
