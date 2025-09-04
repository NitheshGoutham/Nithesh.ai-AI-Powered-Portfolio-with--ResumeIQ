# frontend/sections/about.py

import streamlit as st
from datetime import datetime
import pytz
from streamlit_lottie import st_lottie
import requests

# Load Lottie animation
def load_lottie_url(url: str):
    res = requests.get(url)
    if res.status_code != 200:
        return None
    return res.json()

# Dynamic greeting
def get_greeting():
    india_time = datetime.now(pytz.timezone('Asia/Kolkata'))
    hour = india_time.hour
    if hour < 12:
        return "🌅 Good Morning"
    elif 12 <= hour < 17:
        return "🌞 Good Afternoon"
    else:
        return "🌙 Good Evening"

# Main display function
def run():
    # Load animation only when run
    lottie_hello = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_t24tpvcu.json")
    
    st_lottie(lottie_hello, height=150)
    st.header(f"{get_greeting()}, I'm Nithesh Goutham! ")

    st.markdown("""
Welcome to my AI-powered portfolio!  
I'm a **AI Engineer** from Chennai 🇮🇳, passionate about building intelligent, full-stack solutions using **Python, FastAPI, LangChain, and Streamlit**.

---

### 🔍 Who am I?
- 🎓 B.E. in ECE, MBA in HRM  
- 💼 3+ years across IT Service, Chatbot Analyst and GenAI  
- 💡 Currently working on **NTT DATA**  
- 🧠 Experience with **LangChain, RAG, MCP, Google ADK, Gemini API**  
- 🧰 Skilled in SQL, Power BI, Streamlit, LLMs, CNN, OpenCV  
""")

    

    st.markdown("### 📬 Get in Touch")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <a href="mailto:nitheshgoutham2000@gmail.com" target="_blank" style="text-decoration: none;">
            <div style="margin-bottom: 20px; border-radius: 10px; padding: 20px; 
                        text-align: center; background-color: black; color: white; 
                        font-weight: bold; font-size: 16px;">
                📧 Email Me
            </div>
        </a>
        """, unsafe_allow_html=True)

        st.markdown("""
        <a href="https://github.com/NitheshGoutham" target="_blank" style="text-decoration: none;">
            <div style="margin-bottom: 20px; border-radius: 10px; padding: 20px;
                        text-align: center; background-color: black; color: white;
                        font-weight: bold; font-size: 16px;">
                💻 GitHub
            </div>
        </a>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <a href="https://www.linkedin.com/in/nithesh-goutham-m/" target="_blank" style="text-decoration: none;">
            <div style="margin-bottom: 20px; border-radius: 10px; padding: 20px;
                        text-align: center; background-color: black; color: white;
                        font-weight: bold; font-size: 16px;">
                💼 LinkedIn
            </div>
        </a>
        """, unsafe_allow_html=True)

        st.markdown("""
        <a href="https://drive.google.com/file/d/1jDx8sMrrpHRr8VdJ_sdimy9A0QTf1UKo/view?usp=sharing" target="_blank" style="text-decoration: none;">
            <div style="margin-bottom: 20px; border-radius: 10px; padding: 20px;
                        text-align: center; background-color: black; color: white;
                        font-weight: bold; font-size: 16px;">
                📄 View Resume
            </div>
        </a>
        """, unsafe_allow_html=True)
