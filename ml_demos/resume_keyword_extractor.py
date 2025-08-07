import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def extract_keywords(resume_text, jd_text=None):
    resume_doc = nlp(resume_text.lower())
    resume_tokens = [token.text for token in resume_doc if token.pos_ in {"NOUN", "PROPN"} and not token.is_stop]

    keyword_counts = Counter(resume_tokens)
    top_keywords = keyword_counts.most_common(15)

    # Extract skills from resume
    resume_skills = set(resume_tokens)

    if jd_text:
        jd_doc = nlp(jd_text.lower())
        jd_tokens = [token.text for token in jd_doc if token.pos_ in {"NOUN", "PROPN"} and not token.is_stop]
        jd_skills = set(jd_tokens)

        matched_skills = list(resume_skills & jd_skills)
        missing_skills = list(jd_skills - resume_skills)

        total_skills = len(jd_skills)
        match_percentage = round((len(matched_skills) / total_skills) * 100, 2) if total_skills else 0.0

        return {
            "top_keywords": top_keywords,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "match_percentage": match_percentage
        }
    else:
        return {
            "top_keywords": top_keywords,
            "matched_skills": [],
            "missing_skills": [],
            "match_percentage": 0.0
        }
