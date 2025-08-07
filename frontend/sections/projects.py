import streamlit as st

# Define your projects
projects = [
    {
    "title": "🤖 Nithesh's AI-Powered Portfolio with ResumeIQ",
    "tech": ["Streamlit", "FastAPI", "LangChain", "Ollama", "Gemini", "JSON", "LLMs"],
    "desc": "Developed a full-stack interactive portfolio powered by Generative AI, featuring project filtering, static Q&A from resume, and local/remote LLM support using Gemini or Ollama.",
    "features": [
        "Frontend built with Streamlit featuring sidebar navigation and interactive sections",
        "Backend FastAPI app serving resume data and custom rule-based QA logic",
        "LLM support via Gemini API or local Ollama models (Mistral, LLaMA)",
        "Static question answering based on structured resume data (no hallucination)",
        "Project filtering, tags, and tech-stack categorization with screenshots"
    ],
    "impact": "Showcases personal GenAI development skills and serves as a centralized portfolio for recruiters and clients.",
    "github": "https://github.com/NitheshGoutham/Nithesh.ai-AI-Powered-Portfolio-with--ResumeIQ/tree/main",
    "tags": ["GenAI", "Portfolio", "Full Stack", "Web", "Resume Q&A", "LLM"]
},

    {
    "title": "✈️ Airline Customer Segmentation – K-Means Clustering",
    "tech": ["Python", "Pandas", "scikit-learn", "Seaborn", "Matplotlib"],
    "desc": "Identified distinct airline customer segments using LRFMC analysis and K-Means clustering to drive loyalty program enhancements and churn prevention strategies.",
    "features": [
        "Handled missing values, outliers, and transformed data for clustering",
        "Engineered LRFMC features for customer behavior modeling",
        "Applied Elbow Method to determine optimal number of clusters",
        "Cluster visualization using PCA",
        "Business insights and marketing recommendations for each cluster"
    ],
    "impact": "Helps airlines classify customers into actionable segments, optimize marketing campaigns, and improve retention strategies.",
    "github": "https://github.com/NitheshGoutham/Airline-Customer-Segmentation",
    "tags": ["Clustering", "K-Means", "Customer Segmentation", "Airline", "EDA"]
},

    
    {
    "title": "🌱 Sentinel-2 Data Processing for Pichavaram Mangrove Forest",
    "tech": ["Python", "TensorFlow", "CNN", "Remote Sensing", "Matplotlib", "Seaborn", "rasterio"],
    "desc": "Deep learning-based image classification model using Sentinel-2 satellite data to monitor environmental changes in the Pichavaram Mangrove Forest.",
    "features": [
        "Acquires satellite imagery using Sentinel-2 open datasets",
        "Preprocessing pipeline for resizing, noise reduction, and georeferencing",
        "Convolutional Neural Network (CNN) trained to classify land cover types",
        "Output includes classified maps of mangroves, water bodies, and vegetation",
        "Visual insights generated using Matplotlib and Seaborn"
    ],
    "impact": "Enables environmental monitoring and change detection for ecologically sensitive regions using AI-powered satellite image analysis.",
    "github": "https://github.com/NitheshGoutham/Sentinel-2-Data-Processing-for-Pichavaram-Mangrove-Forest-Using-CNN",
    "tags": ["Deep Learning", "Remote Sensing", "Image Processing", "Environmental"]
}
,
    {
    "title": "🏘️ Singapore Resale Flat Prices Prediction",
    "tech": ["Python", "Pandas", "NumPy", "Scikit-Learn", "Streamlit", "Render", "Pickle"],
    "desc": "A machine learning web app that predicts Singapore HDB resale flat prices based on user inputs, with real-time prediction and deployment via Streamlit.",
    "features": [
        "Historical HDB resale data cleaning and preprocessing",
        "Feature engineering, outlier handling, skew correction",
        "Regression model evaluation and selection via cross-validation",
        "Streamlit app to input flat features and get predictions",
        "Deployment on Render with smooth user experience"
    ],
    "impact": "Empowered users to make informed housing decisions by visualizing and predicting HDB resale flat prices in real-time using ML techniques.",
    "link": "https://singapore-resale-flat-prices-predicting-600l.onrender.com",

    "github": "https://github.com/NitheshGoutham/Singapore-Resale-Flat-Prices-Predicting",  
    "tags": ["ML", "Real Estate", "Web", "BI"]
},
{
    "title": "⚙️ Industrial Copper Price & Status Prediction",
    "tech": ["Python", "Scikit-learn", "Streamlit", "EDA", "ML"],
    "desc": "Built an ML-powered tool to predict copper's selling price and status using regression and classification models. The app uses user inputs to dynamically provide results via a Streamlit interface.",
    "features": [
        "Data preprocessing: null handling, outlier treatment, skew correction",
        "Feature engineering and multicollinearity check",
        "Random Forest Regressor for price prediction",
        "Extra Trees Classifier for status prediction",
        "Model pickling and deployment with Streamlit interface"
    ],
    "impact": "Supports the manufacturing industry in forecasting copper pricing and stock status, combining ML with a user-friendly front-end.",
    "github": "https://github.com/NitheshGoutham/Industrial-Copper-Modeling",
    "tags": ["Manufacturing", "ML", "Regression", "Classification"]
}

,
{
    "title": "🏘️ Airbnb Data Analytics Platform",
    "tech": ["Python", "MySQL", "Streamlit", "Plotly", "Power BI"],
    "desc": "Developed an interactive Streamlit app and Power BI dashboard to explore Airbnb 2019 listings. Data was extracted, transformed, and visualized using geo-charts and SQL-backed insights.",
    "features": [
        "Processed JSON Airbnb dataset into structured DataFrames",
        "Stored and queried data using MySQL with SQLAlchemy",
        "Streamlit UI with multi-tab dashboard (Home, Discover, Insight)",
        "Dynamic geo-visualizations using Plotly",
        "Power BI dashboard showing pricing trends, property types, locations"
    ],
    "impact": "Empowers tourism and property managers to derive actionable insights from Airbnb listings using both web and BI tools.",
    "github": "https://github.com/NitheshGoutham/Airbnb-Analysis-Using-PowerBi",
    "tags": ["Tourism", "BI", "SQL", "Visualization", "Dashboard"]
},

    {
    "title": "📊 PhonePe Pulse Data Visualization",
    "tech": ["Python", "MySQL", "Streamlit", "Plotly", "SQLAlchemy", "Pandas", "Git"],
    "desc": "A user-friendly analytics dashboard for exploring the PhonePe Pulse dataset with geo-visualizations and interactive insights.",
    "features": [
        "GitHub cloning of PhonePe Pulse public dataset",
        "Raw JSON transformed into structured Pandas DataFrames",
        "Stored and queried using MySQL with SQLAlchemy engine",
        "Geospatial plots of transaction/user data using Plotly",
        "Streamlit dashboard with filters for state, year, and quarter"
    ],
    "impact": "Provides an accessible way to analyze India’s digital payment trends using open data and interactive charts. Suitable for fintech market analysis and educational purposes.",
    "github": "https://github.com/NitheshGoutham/Phonepe-Pulse-Data",  # Replace with your actual repo
    "tags": ["Fintech", "BI", "ETL", "Visualization"]
    },

    {
    "title": "📺 YouTube Data Harvesting & Warehousing",
    "tech": ["Python", "Streamlit", "MySQL", "YouTube API", "Pandas"],
    "desc": "A Streamlit-based tool that harvests YouTube channel data using the YouTube API, stores it in a MySQL warehouse, and allows SQL-based querying and visualization.",
    "features": [
        "Retrieve channel, video, playlist, and comment data using YouTube Data API",
        "Store collected data in structured MySQL tables (local DB)",
        "Query the database using SQL through the app and visualize results",
        "Interactive Streamlit UI with side menu options",
        "Answer 10 pre-defined analysis questions from YouTube data"
    ],
    "impact": "Simplifies YouTube data exploration using SQL and Streamlit for analysts or creators, demonstrating full-stack data engineering and API integration skills.",
    "github": "https://github.com/NitheshGoutham/youtube-data-harvesting-warehousing-using-streamlit",
    "tags": ["Social Media", "Data Engineering", "Web", "SQL"]
},
{
    "title": "🧱 Flask + Streamlit CRUD Application",
    "tech": ["Python", "Flask", "MySQL", "Streamlit", "SQLAlchemy", "Pandas"],
    "desc": "A full-stack CRUD web application using Flask for backend and Streamlit for frontend to manage structured records stored in a MySQL database.",
    "features": [
        "Flask backend API with endpoints for Create, Read, Update, Delete",
        "MySQL used as the primary data storage with optimized queries",
        "Streamlit-based UI for user-friendly data entry and manipulation",
        "SQLAlchemy ORM to interface between Flask and MySQL",
        "Dynamic forms, tables, and feedback alerts for user actions"
    ],
    "impact": "Provides a scalable data management interface for small to mid-sized apps, bridging frontend and backend seamlessly with Python-based tools.",
    "github": "https://github.com/NitheshGoutham/Flask-and-Streamlit-CRUD-Application-",
    "tags": ["Web", "Data Management", "CRUD", "Full Stack"]
},
{
        "title": "🧾 Digital CV using Streamlit",
        "tech": ["Streamlit", "Python", "pandas", "NumPy", "Render"],
        "desc": "An interactive, hosted digital resume to showcase skills and experience.",
        "features": [
            "Sidebar navigation for resume sections",
            "PDF export functionality for offline sharing",
            "Hosted on Render for real-time access"
        ],
        "impact": "Increased portfolio visibility and demonstrated Python + Web dev skills to recruiters.",
        "link": "https://digital-cv-using-streamlit.onrender.com/",
        "github": "https://github.com/NitheshGoutham/Digital-CV-Using-Streamlit",
        "tags": ["Web"]
    },
{
    "title": "👨‍🏫 Employee Training & Development – Saehan Stamping Ltd",
    "tech": ["Statistical Analysis", "Chi-Square Test", "Correlation", "SPSS", "Excel"],
    "desc": "A research-driven project evaluating training programs at Saehan Stamping Ltd, with recommendations to enhance employee performance and engagement.",
    "features": [
        "Primary data collection through employee surveys",
        "Hypothesis testing using Chi-Square and Correlation methods",
        "Detailed findings on training effectiveness and productivity gains",
        "Recommendations to improve technical and safety training infrastructure",
        "Scope defined for extending research to similar industrial contexts"
    ],
    "impact": "Provides actionable insights for HR teams and management to enhance workforce capabilities and align training strategies with organizational growth.",
    "github": "https://github.com/NitheshGoutham/A-STUDY-ON-EMPLOYEES-TRAINING-AND-DEVELOPMENT-",
    "tags": ["HR Analytics", "Research", "Training Effectiveness", "Organizational Development"]
},
{
    "title": "🧠 Face Recognition Attendance System with Voice Output",
    "tech": ["Python", "OpenCV", "Pyttsx3", "Tkinter", "Numpy", "xlwt"],
    "desc": "Developed a biometric face recognition system with voice feedback and automated attendance marking via email reporting.",
    "features": [
        "Face data collection, training, and recognition via OpenCV",
        "Voice-based ID announcement using pyttsx3",
        "Attendance logging in Excel sheets with timestamps",
        "Email automation of attendance reports to stakeholders",
        "Modular structure for Create, Train, Recognize, Mail workflows"
    ],
    "impact": "Streamlines attendance tracking in educational and professional environments with real-time voice feedback and reporting.",
    "github": "https://github.com/NitheshGoutham/Face-recogition-attendance-system-",
    "tags": ["Computer Vision", "Automation", "Voice AI", "Face Recognition"]
}




]


def run():
    st.header("🧪 Projects")

    # Tag filtering
    selected_tags = st.multiselect("Filter by tag:", options=sorted({tag for p in projects for tag in p["tags"]}))

    for project in projects:
        if selected_tags and not any(tag in project["tags"] for tag in selected_tags):
            continue

        with st.expander(f"{project['title']}", expanded=False):
            st.markdown(f"**Tech Stack:** {', '.join(project['tech'])}")
            st.markdown(f"**Description:** {project['desc']}")

            if "features" in project:
                st.markdown("**Key Features:**")
                for f in project["features"]:
                    st.markdown(f"- {f}")

            if "impact" in project:
                st.markdown(f"**Impact:** {project['impact']}")

            if project.get('github'):
                st.markdown(
        f"""
        <a href="{project['github']}" target="_blank">
            <div style="border: 1px solid #ccc; padding: 8px 12px; border-radius: 8px;
                        background-color: black; display: inline-block; font-weight: bold;
                        text-decoration: none; color: white;">
                📂 View GitHub Repo
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
