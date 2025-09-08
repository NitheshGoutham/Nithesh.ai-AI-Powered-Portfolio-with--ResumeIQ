# sections/resume_keyword_extractor.py

def extract_keywords(resume_text: str, jd_text: str):
    return {
        "top_keywords": [("Python", 3), ("SQL", 2)],
        "matched_skills": ["Python", "SQL"],
        "missing_skills": ["Machine Learning"],
        "match_percentage": 70
    }
