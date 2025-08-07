import streamlit as st

# Simple tool badge styling
def tool_badges(tools):
    return " ".join([
        f"<span style='background-color:#0072C6; color:white; padding:4px 8px; margin:2px; border-radius:6px; display:inline-block;'>{tool}</span>"
        for tool in tools
    ])

# Job card inside an expander
def job_card(company,title, duration, location, responsibilities, tools, emoji="💼"):
    with st.expander(f"{emoji}  **{company} – {title}**  | 📍 {location} | 📅 {duration}"):
        st.markdown(responsibilities)
        if tools:
            st.markdown(f"**🛠 Tools/Technologies:**", unsafe_allow_html=True)
            st.markdown(tool_badges(tools), unsafe_allow_html=True)
        st.markdown("---")

def run():
    st.header("💼 Professional Experience")

    # 1. NTT DATA
    job_card(
        company="NTT DATA Inc",
        title="Technical Graduate Trainee – Generative AI",
        
        duration="April 2025 – Present",
        location="Pune,India",
        responsibilities="""
- 🤖 Gained hands-on experience in designing and managing **Agentic AI solutions** using cutting-edge LLM frameworks.
- 📈 Integrated **iAgentOps** for LLM observability and agent performance tracking.
- 🧠 Worked with **Monitor Context Protocol (MCP)** to monitor multi-agent task flows.
- 📝 Maintained prompt versioning in PromptOps with metrics-based tuning.
- 🧾 Engineered prompts for schema extraction and automation.
- 🤝 Collaborated with teams to deploy LLM-powered tools with a focus on latency, cost, and compliance.
""",
        tools=["LangChain", "PromptOps", "iAgentOps", "FastAPI", "Azure OpenAI", 
               "Gemini", "RAG", "MCP", "Git", "Streamlit", "Python", "JSON", "LLMOps"],
        emoji="🧠"
    )

    # 2. Ramco Systems
    job_card(
        title="Software Engineer – Data Validation (HR/Payroll Systems)",
        company="Ramco Systems",
        duration="Dec 2024 – Feb 2025",
        location="Chennai, India",
        responsibilities="""
- 🧾 Extracted and validated payroll data from complex HRIS tables.
- 📈 Built validation scripts to detect data inconsistencies.
- 📊 Created Excel dashboards for validation summaries.
- 🧰 Automated audit trail generation with Pandas.
- 🔍 Reduced manual rework by 30% via root cause analysis.
""",
        tools=["Python", "Pandas", "MySQL", "Excel", "Regex", "Audit Frameworks", "JSON"],
        emoji="📊"
    )

    # 3. Atos Global IT
    job_card(
        title="Systems Engineer – AI Chatbot Analyst (ELIZA AI)",
        company="Atos Global IT Solutions",
        duration="June 2022 – September 2024",
        location="Chennai, India",
        responsibilities="""
- 🤖 Tuned ELIZA AI chatbot for L1 ticket handling.
- 📁 Built classification logic for NLU error handling.
- 🧪 Led regression testing across multiple releases.
- 📈 Built Power BI dashboards for usage trends.
- 🔧 Managed JSON configs for chatbot workflows.
""",
        tools=["Power BI", "ServiceNow", "Excel", "Python", "Chatbot Training", "NLU", "Intent Mapping", "JSON", "Regex"],
        emoji="🤖"
    )

    # 🔧 Summary
    st.markdown("### 🛠️ Tools & Technologies")
    st.markdown("""
`Python` &nbsp; `SQL` &nbsp; `LangChain` &nbsp; `Gemini Pro` &nbsp; `Azure OpenAI` &nbsp; `FastAPI` &nbsp; `Streamlit` &nbsp; 
`Pandas` &nbsp; `NumPy` &nbsp; `Excel` &nbsp; `Power BI` &nbsp; `Git` &nbsp; `MySQL` &nbsp; `PostgreSQL` &nbsp; 
`ServiceNow` &nbsp; `Regex` &nbsp; `JSON` &nbsp; `LCEL` &nbsp; `CNN` &nbsp; `TensorFlow` &nbsp; `Keras` &nbsp; `Pinecone` &nbsp; 
`Gradio` &nbsp; `Audit Automation` &nbsp; `Chatbot Analytics`
""")
