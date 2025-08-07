# frontend/sections/resume_qa.py

import streamlit as st
import requests

def run():
    st.header("🤖 Resume Q&A (Powered by Local LLM)")

    st.markdown("Ask questions about your resume using the local AI engine.")
    
    # Suggested questions
    examples = [
    "What is my current role?",
    "What are my key skills?",
    "Where did I work before NTT DATA?",
    "Tell me about my projects.",
    "List my certifications.",
    "Summarize my experience.",
    "What tools do I know for GenAI?",
    "What is my educational background?",
    "What was my role at Atos?",
    "What certifications do I hold from Microsoft?",
    "Name a project where I used Power BI.",
    "Describe my role in the NTT Smart AgentOps project.",
    "What is the tech stack of my portfolio?",
    "What are the key features of Nithesh.ai?",
    "Mention a project that uses CNN.",
    "Which project involved HR or employee training?",
    "What ML techniques have I used in my projects?",
    "Which LLMs does my portfolio support?",
    "What is MCP in my experience at NTT?",
    "List the technologies used in the Airbnb Analytics Project."
]


    # Selected question
    selected_example = st.selectbox("💡 Example Questions", [""] + examples)
    if selected_example:
        st.session_state["resume_query"] = selected_example

    # Input box with default value from dropdown
    user_question = st.text_input("Type your question here 👇",
                                  value=st.session_state.get("resume_query", ""),
                                  key="question_input")

    if st.button("🔍 Get Answer") and user_question:
        response = requests.post("http://localhost:8000/resume-qa", json={"query": user_question})
        if response.status_code == 200:
            st.success(response.json()["answer"])
        else:
            st.error("Error getting answer from backend.")
