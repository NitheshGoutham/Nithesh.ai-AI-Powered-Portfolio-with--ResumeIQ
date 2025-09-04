import streamlit as st
import json
from genai_utils import ask_gemini

def run():
    st.header("Resume Q&A with Gemini")

    # Load resume data
    with open("resume_data.json", "r") as f:
        resume_data = json.load(f)

    user_question = st.text_input("Ask me about my resume:")

    if st.button("Ask Gemini"):
        if user_question.strip() == "":
            st.warning("Please enter a question.")
        else:
            context = json.dumps(resume_data, indent=2)
            prompt = f"Here is my resume data: {context}\n\nQuestion: {user_question}\nAnswer:"
            answer = ask_gemini(prompt)
            st.success(answer)
