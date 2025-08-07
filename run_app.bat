@echo off
start cmd /k "cd backend && uvicorn main:app --reload"
start cmd /k "cd frontend && streamlit run app.py"

