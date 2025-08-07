import streamlit as st

def run():
    st.header("🎓 Certifications")

    certifications = [
        {
            "title": "Certified Professional in Advanced Programming – IITM Pravartak",
            "date": "January 2025",
            "link": "https://digitalskills.iitmpravartak.org.in/verify/cert/0497J024114L03b8V9"
        },
        {
            "title": "Microsoft Certified: Azure AI Engineer Associate",
            "date": "July 2025",
            "link": "https://learn.microsoft.com/en-us/users/mnitheshgoutham-3071/credentials/458491a0476eb4e7"
        },
        {
            "title": "Microsoft Certified: Azure Data Scientist Associate",
            "date": "June 2025",
            "link": "https://learn.microsoft.com/en-us/users/mnitheshgoutham-3071/credentials/6c052adf016aa768"
        },
        {
            "title": "Master Data Scientist – GUVI Geek Network (IITM)",
            "date": "October 2024",
            "link": "https://www.guvi.in/share-certificate/0497J024114L03b8V9"
        },
        {
            "title": "Microsoft Certified: Azure Administrator Associate",
            "date": "July 2023",
            "link": "https://learn.microsoft.com/en-us/users/mnitheshgoutham-3071/credentials/cb82f1f614c4b016"
        },
        {
            "title": "Microsoft Certified: Virtual Desktop Specialty",
            "date": "July 2023",
            "link": "https://learn.microsoft.com/en-us/users/mnitheshgoutham-3071/credentials/784900d13054a668"
        },
        {
            "title": "Microsoft Certified: Azure Data Fundamentals",
            "date": "December 2022",
            "link": "https://learn.microsoft.com/en-us/users/mnitheshgoutham-3071/credentials/7f4bd48d91b6a7b"
        },
        {
            "title": "Microsoft 365 Certified: Fundamentals",
            "date": "December 2022",
            "link": "https://learn.microsoft.com/en-us/users/mnitheshgoutham-3071/credentials/4a4b03cd72235b0b"
        },
        {
            "title": "Microsoft Certified: Security, Compliance, and Identity Fundamentals",
            "date": "November 2022",
            "link": "https://learn.microsoft.com/en-us/users/mnitheshgoutham-3071/credentials/c8e21911142d5b92"
        },
        {
            "title": "Microsoft Certified: Azure Fundamentals",
            "date": "November 2022",
            "link": "https://learn.microsoft.com/en-us/users/mnitheshgoutham-3071/credentials/76e4eacfaa96828b"
        }
    ]

    for cert in certifications:
        with st.expander(f"📜 {cert['title']} ({cert['date']})"):
            st.markdown(f"[🔗 View Certificate]({cert['link']})", unsafe_allow_html=True)
