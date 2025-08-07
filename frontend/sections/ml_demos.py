import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from ml_demos.resume_keyword_extractor import extract_keywords


import streamlit as st 

def run():
    st.header("ResumeIQ: Your Smart JD Matcher")

    user_resume = st.text_area("📄 Paste your Resume text below", height=250)
    jd_text = st.text_area("🧾 Paste Job Description (JD) text below", height=250)

    if st.button("🧠 Analyze Match") and user_resume and jd_text:
        result = extract_keywords(user_resume, jd_text)

        st.subheader("🔑 Top Resume Keywords")
        for word, count in result["top_keywords"]:
            st.write(f"- {word} ({count} times)")

        st.subheader("✅ Matched Skills with JD")
        if result["matched_skills"]:
            st.success(", ".join(result["matched_skills"]))
        else:
            st.warning("No skills matched with JD.")

        st.subheader("❌ Missing Skills (from JD)")
        if result["missing_skills"]:
            st.error(", ".join(result["missing_skills"]))
        else:
            st.success("Your resume covers all JD keywords!")

        st.subheader("📊 Overall Match Score")
        st.progress(result["match_percentage"] / 100)
        st.info(f"Match Score: **{result['match_percentage']}%** with the provided JD.")
