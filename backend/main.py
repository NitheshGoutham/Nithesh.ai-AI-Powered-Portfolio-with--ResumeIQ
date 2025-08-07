# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from llm_engine import query_local_llm
import json

app = FastAPI()

# Allow CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load resume data
with open("resume_data.json", "r") as f:
    resume_data = json.load(f)

@app.get("/profile")
def get_profile():
    return resume_data

@app.post("/resume-qa")
def resume_qa(question: dict):
    query = question.get("query", "")
    response = query_local_llm(query, resume_data)
    return {"answer": response}
