# Nithesh's AI-Powered Portfolio with ResumeIQ    

Welcome to my AI-enhanced full-stack personal portfolio project! This interactive platform goes beyond a typical resume—it features dynamic sections, a custom Resume Q&A chatbot, and a modular backend powered by FastAPI. It showcases not only my skills and experiences, but also my ability to build intelligent GenAI-based applications.

**Live Demo**
Try it here: [https://nithesh-ai-portfolio.onrender.com](https://nithesh-ai-portfolio.onrender.com)

---

## Project Overview

This project features:
* A **Streamlit frontend** that provides a user-friendly portfolio interface.
* A **FastAPI backend** that serves structured resume data and handles Resume Q&A logic.
* A **modular codebase** that's easily extendable with Generative AI capabilities like RAG, embeddings, and LLM APIs.
* An **offline Q&A chatbot** based on rule-based logic for fast and secure resume interaction.

---

## Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| Frontend | Streamlit | UI/UX for portfolio |
| Backend | FastAPI | API layer for data and Q&A handling |
| Data Storage | JSON | Stores structured resume content |
| LLM (optional) | Phi-3 / Gemini | For smart resume Q&A (optional via API) |
| Deployment | Localhost / Cloud | Render, HuggingFace, or Streamlit Cloud |
| Python Libs | requests, json, streamlit, fastapi, uvicorn | Core dependencies |

---

## Project Structure

nithesh_ai_portfolio/   
├── run_app.bat - Script to launch both frontend and backend   
├── backend/   
│ ├── main.py - FastAPI backend server   
│ └── resume_data.json   
│
├── frontend/   
│ ├── app.py - Streamlit main app   
│ └── sections/   
│ ├── about.py   
│ ├── skills.py   
│ ├── projects.py   
│ ├── certifications.py   
│ ├── education.py   
│ ├── resume_qa.py - Q&A chatbot UI   
│ └── ml_playground.py   
└── requirements.txt - Python dependencies   


---

## How It Works – Architecture

### Frontend (Streamlit)
* Uses a sidebar for navigation across different resume sections.
* Each section (e.g., About, Skills, Projects) is modularized.
* Sends `GET` requests to `/profile` to fetch dynamic content.
* The Resume Q&A section sends `POST` requests to `/chat_resume`.

### Backend (FastAPI)
* Loads `resume_data.json` on startup.
* Exposes two endpoints:
    * `/profile` → Returns structured resume data.
    * `/chat_resume` → Receives user questions and returns intelligent answers using `generate_response()`.

### Resume Q&A Logic
Uses either:
a.  An LLM-based system (e.g., Phi-3, Gemini via API), or
b.  A rule-based static system for offline, fast, and deterministic answers.

### Request-Response Flow
`User` → `Streamlit UI` → `FastAPI API`
* `GET /profile` → Resume JSON data
* `POST /chat_resume` → User question → Resume answer

---

## Features

* **Dynamic Resume Sections** (About, Skills, Projects, etc.)
* **Custom Resume Q&A Chatbot** (LLM or Rule-based)
* **Modular Design** (easy to extend and maintain)
* **Optional ML Playground** (demo ML/AI capabilities)
* **Fully Offline Capable**
* **Ready for Deployment** on Render / Hugging Face / Streamlit Cloud

---

## Planned Enhancements

| Feature | Description |
| :--- | :--- |
| RAG Integration | Replace static Q&A with LangChain + Gemini/Ollama |
| Online Deployment | Deploy to platforms like Render or HuggingFace |
| Admin Interface | Add a UI to update resume content (edit JSON from web) |
| PDF Resume Upload | Extract structured data from PDF automatically |
| Embedding Support | Use FAISS/Chroma for semantic search |
| ML Playground | Add ML/AI demo section to showcase technical depth |

---

## License
This project is for educational and personal branding purposes.    

## Contact

Author: Nithesh Goutham M   
Location: Chennai, India   
Email: nitheshgoutham2000@gmail.com    
LinkedIn: https://www.linkedin.com/in/nithesh-goutham-m/   
Portfolio: https://nithesh-ai-portfolio.onrender.com    
