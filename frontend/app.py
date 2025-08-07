import streamlit as st

from sections import about, skills, experience, education, projects, certifications, resume_qa, ml_demos

st.set_page_config(page_title="Nithesh AI Portfolio", layout="wide")
st.title(" Nithesh.AI")

# Sidebar navigation
section = st.sidebar.selectbox("Navigate", (
    "About Me", "Professional Experience", "Skills", "Education",
    "Projects", "Certifications", "Resume Q&A", "ML Playground"
)).strip()


if section == "About Me":
    about.run()
elif section == "Professional Experience":
    experience.run() 
elif section == "Skills":
    skills.run()
elif section == "Education":
    education.run() 
elif section == "Projects":
    projects.run()
elif section == "Certifications":
    certifications.run()
elif section == "Resume Q&A":
    resume_qa.run()
elif section == "ML Playground":
    ml_demos.run()