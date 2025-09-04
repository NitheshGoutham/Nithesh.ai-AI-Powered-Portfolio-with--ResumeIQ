# Nithesh's AI-Powered Portfolio

Welcome to my AI-enhanced Streamlit-based personal portfolio!
This platform goes beyond a typical resume: it features dynamic sections, a static Resume Q&A chatbot powered by structured JSON data and Gemini API integration. It’s lightweight, accurate (no hallucinations), and demonstrates my Generative AI, Python, and data engineering skills.

**Live Demo**
Try it here: [https://nithesh-ai-portfolio.onrender.com](https://nithesh-ai-portfolio.onrender.com)

---

## Project Overview

This project features:
* A single **Streamlit app**(no backend servers) for easy deployment.
* A **Resume Q&A chatbot** powered by Gemini API or static JSON-based rule-based answers.
* **Modular sections** (About, Skills, Projects, Certifications, Education).
* **Lightweight, portable architecture** that’s easy to extend.

---

## Tech Stack

| Layer        | Technology                                 | Purpose                      |
| :----------- | :----------------------------------------- | :--------------------------- |
| Frontend     | Streamlit                                  | Portfolio UI/UX              |
| AI           | Gemini API                                 | Resume Q\&A and AI responses |
| Data Storage | JSON                                       | Structured resume content    |
| Deployment   | Streamlit Cloud / Render                   | Easy hosting                 |
| Python Libs  | `streamlit`, `google-generativeai`, `json` | Core dependencies            |

---

## Project Structure

nithesh_ai_portfolio/
├── app.py                     # Streamlit main app
├── resume_data.json           # Structured resume data
├── sections/                  # Modular portfolio sections
│   ├── about.py
│   ├── skills.py
│   ├── projects.py
│   ├── certifications.py
│   ├── education.py
│   ├── resume_qa.py           # Q&A chatbot section
│   └── ml_playground.py
├── genai_utils.py             # Gemini API integration
└── requirements.txt           # Python dependencies


---

## How It Works – Architecture

* **Streamlit Frontend Only** – All logic is in a single Streamlit app.

* **Static Resume Q&A** – Reads structured JSON resume data for consistent answers.

* **Gemini API Option** – Dynamically answers user questions with Google Gemini models.

* **No Backend or Ollama** – Simple and cloud-friendly setup.


### Request-Response Flow
`User` → `Streamlit UI` →  `Gemini API / JSON resume` → `Answer`

---

## Features

* Interactive **portfolio UI** with sidebar navigation.
* **Resume Q&A chatbot** (static JSON or Gemini AI).
* **Dynamic filtering and tags** for projects and skills.
* **Lightweight architectur**e – no separate backend or DB.
* **Easily deployable** on Streamlit Cloud, Render, or locally.


---

## Planned Enhancements

| Feature           | Description                                 |
| :---------------- | :------------------------------------------ |
| RAG Integration   | Replace static Q\&A with LangChain + Gemini |
| PDF Parsing       | Auto-extract structured data from resumes   |
| Admin Panel       | Update JSON content from a web interface    |
| Embedding Support | FAISS/Chroma for semantic search            |
| ML Playground     | More AI/ML demos                            |


---

## License
This project is for educational and personal branding purposes.

## Contact
Author: Nithesh Goutham M
Location: Chennai, India
Email: nitheshgoutham@email.com
LinkedIn: https://linkedin.com/in/nitheshgoutham
Portfolio: https://nithesh-ai-portfolio.onrender.com