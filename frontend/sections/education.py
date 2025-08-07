import streamlit as st

def run():
    st.title("📚 Education")

    # ==== Pondicherry University – DDE ====
    st.subheader(':red[Pondicherry University – DDE, Puducherry]')
    st.markdown('**MBA in Human Resource Management**  \n📅 *2022 – 2024*  \n📊 CGPA: **8 / 10**')

    c1, c2, c3 = st.columns(3)
    with c1:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwwMfsijW45v84aLYFEu2OjWJnl7j68WkPSQ&s', use_column_width=True)
    with c2:
        st.image('https://www.pv-magazine-india.com/wp-content/uploads/sites/8/2021/09/PHOTO-2021-09-14-15-28-11-1200x675.jpg', use_column_width=True)
    with c3:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReXZfqaF2v_kwNu0Ss0DJ5pKHRgUvxQ2ayrw&s', use_column_width=True)

    st.link_button('🔗 Official Website', url='https://dde.pondiuni.edu.in/', use_container_width=True)

    with st.expander("🎓 MBA Highlights"):
        st.markdown("""
        - 🧠 Specialized in **Human Resource Management**
        - 📈 Completed courses on **Organizational Behavior**, **HR Analytics**, and **Leadership**
        - 🤝 Interned with **HR consultancy firm** for workforce planning case study
        """)

    with st.expander("🧪 MBA Academic Project"):
        st.markdown("""
        **Project Title:** A Study on Employees' Training and Development  
        🔍 Focus: Impact of L&D practices on employee performance and satisfaction  
        📂 [GitHub Repository](https://github.com/NitheshGoutham/A-STUDY-ON-EMPLOYEES-TRAINING-AND-DEVELOPMENT-)
        """)

    st.divider()

    # ==== Rajalakshmi Engineering College ====
    st.subheader(':red[Rajalakshmi Engineering College, Chennai]')
    st.markdown('**Bachelor of Engineering in ECE**  \n📅 *2018 – 2022*  \n📊 CGPA: **8.2 / 10**')

    c1, c2, c3 = st.columns(3)
    with c1:
        st.image('https://www.rajalakshmi.org/image/banner-1.jpg', use_column_width=True)
    with c2:
        st.image('https://i.ytimg.com/vi/ek6h-WNRR1Y/maxresdefault.jpg', use_column_width=True)
    with c3:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzGqaQ9cskQMFXWvsVAXUSJxTxpIpoCT-qEg&s', use_column_width=True)

    st.link_button('🔗 Official Website', url='https://www.rajalakshmi.org/', use_container_width=True)

    with st.expander("🎖️ Notable Achievements & Activities"):
        st.markdown("""
        - 🤖 Participated in Inter-College IoT Hackathon (2021)
        - 🗣️ Participated in department events under ECE Association
        - 👨‍💻 Active member of Google Developer Student Club (GDSC) and IEEE Student Chapter
        """)

    with st.expander("🧪 BE Final Year Project"):
        st.markdown("""
        **Project Title:** Sentinel-2 Data Processing for Pichavaram Mangrove Forest Using CNN  
        🌍 Focus: Satellite image classification for environmental monitoring  
        📂 [GitHub Repository](https://github.com/NitheshGoutham/Sentinel-2-Data-Processing-for-Pichavaram-Mangrove-Forest-Using-CNN)
        """)

    st.divider()

    # ==== Jeeva Velu Residential School ====
    st.subheader(':red[Jeeva Velu Residential School, Tiruvannamalai]')
    st.markdown('**Higher Secondary Certificate (HSC)**  \n📅 *2017 – 2018*  \n📊 Score: **83.67%**')

    st.markdown('**Secondary School Leaving Certificate (SSLC)**  \n📅 *2015 – 2016*  \n📊 Score: **94%**')

    c1, c2 = st.columns(2)
    with c1:
        st.image('https://content.jdmagicbox.com/comp/tiruvannamalai/v6/9999p4175.4175.121017112458.v9v6/catalogue/jeeva-velu-international-school-mathur-tiruvannamalai-cbse-schools-3evijsp.jpg', use_column_width=True)
    with c2:
        st.image('https://www.google.com/imgres?imgurl=https://jeevavelu.org/upload/life-title-bg.JPG&tbnid=r0mD6vgC3TEIkM&vet=1&imgrefurl=https://jeevavelu.org/standard-post-type.html&docid=r3t95ZpQLFlllM&w=5184&h=3456&itg=1&source=sh/x/im/m1/1&kgs=7335874cbbf6cf19&shem=isst#imgrc=NquzN2XgOWPYHM&imgdii=qP-UMnsAwmOErM', use_column_width=True)
    

    st.link_button('🔗 Official Website', url='https://jeevavelu.org/', use_container_width=True)
