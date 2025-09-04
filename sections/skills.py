import streamlit as st

def badgeify(skill_list):
    return " ".join([
        f"<span style='background-color:black; color:white; padding:6px 12px; margin:4px; border-radius:10px; display:inline-block; font-size:14px;'>{skill}</span>"
        for skill in skill_list
    ])

# Updated Skills dictionary with emojis for each skill
skills = {
    "Languages & Libraries": [
        "🐍 Python", "🧮 SQL", "🧷 Pandas", "➗ NumPy", "🔍 Regex", "⚛️ JavaScript"
    ],
    "GenAI & LLMs": [
        "🔗 LangChain", "📚 RAG", "🧠 Agentic AI", "🤖 LLM Integration", "🧠 Prompt Engineering", 
        "📌 OpenAI Embeddings", "🧾 MCP", "⚙️ LLMOps"
    ],
    "Frameworks & APIs": [
        "🚀 FastAPI", "📈 Streamlit", "🎛️ Gradio", "🔥 Flask", "🧱 Django", "⚛️ React.js"
    ],
    "Vector Databases": [
        "🗄️ ChromaDB", "📦 FAISS"
    ],
    "Business Intelligence": [
        "📊 Power BI", "📉 Tableau", "📋 Excel", "🔁 Pivot Tables"
    ],
    "MLOps & Observability": [
        "🛠️ Git", "🔍 PromptOps", "🕵️ AgentOps", "📊 RAGOps", "📡 Observability & Tracing", 
        "📄 JSON", "📬 Postman", "🖥️ VS Code"
    ],
    "Cloud & Platforms": [
        "☁️ Azure OpenAI", "🪄 Gemini", "🧪 Ollama", "📓 Google Colab", "🌐 Render", "🤗 Hugging Face", "🔮 Google AI SDK"
    ],
    "Deep Learning": [
        "🧠 TensorFlow", "🧬 Keras", "🖼️ CNN", "🗣️ NLP"
    ],
    "Others": [
        "🧾 ServiceNow", "📊 Chatbot Analytics", "🤖 Automation", "📑 Knowledge Base Optimization"
    ]
}

# Category icons
CATEGORY_ICONS = {
    "Languages & Libraries": "💻",
    "GenAI & LLMs": "🧠",
    "Frameworks & APIs": "🧩",
    "Vector Databases": "🗄️",
    "Business Intelligence": "📊",
    "MLOps & Observability": "🔧",
    "Cloud & Platforms": "☁️",
    "Deep Learning": "🤖",
    "Others": "🛠️"
}

def run():
    st.header("🧰 Skills & Tools")

    for category, items in skills.items():
        icon = CATEGORY_ICONS.get(category, "📁")
        with st.expander(f"{icon} {category}", expanded=False):
            st.markdown(badgeify(items), unsafe_allow_html=True)
