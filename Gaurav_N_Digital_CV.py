from pathlib import Path

import streamlit as st
from PIL import Image
import time as tmod

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
#current_dir=r"https://github.com/pythodoc/Profile_pg/blob/main/"
# css_file = current_dir / "styles" / "main.css"
css_file=current_dir+r"\styles\main.css"
# resume_file = current_dir / "assets" / "CV.pdf"
resume_file=current_dir+r"\assets\CV.pdf"
# profile_pic = current_dir / "assets" / "profile-pic.png"
profile_pic=current_dir+r"\assets\gaurav profile_pic1.PNG"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Gaurav Nazare"
PAGE_ICON = ":wave:"
NAME = "Gaurav Nazare"
DESCRIPTION = """
Junior Python Developer, assisting enterprises by supporting the organization's mission to build robust, 
efficient trading infrastructure and deliver high-quality data services to stakeholders.
"""
EMAIL = "gauravnazare214@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/gaurav-nazare-bkt9741/",
    "GitHub": "https://github.com/pythodoc",
}
PROJECTS = {
    "🏆 GreekSoft API Python Library Package": "https://pypi.org/project/greeksoft/",
    "🏆 Database Keyword Search Application" : "Deployed Within Organization",
    "🏆 Email Ticket Tracking System": "Deployed Within Organization",
    "🏆 Temple Website - Custome Website hosted on Streamlit": "https://omshivgorakshayogiasthana.streamlit.app/"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name="Gaurav_N CV.pdf",
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming:: Python (Adv.Pandas),Rest_API, SQL
- 📊 Data Visulization: Streamlit(Complex WebApps), MS Excel,Plotly,Gradio
- 📚 Extra: Custom Trading Business Logic, As per Client Needs
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Jr. Python Developer | Silverstream Equitas Pvt Ltd**")
st.write("09/2024 - Present")
st.write(
    """
- ► Implemented Custom Trading Logic using Python libraries such as Pandas
    and NumPy for data analysis, signal generation, and backtesting strategies on
    historical market data. Developed interactive dashboards and interfaces using
    Streamlit and Gradio to visualize market trends, display trading signals, and
    allow users to simulate trades in real-time. Focused on creating modular, efficient,
    and user-friendly tools to support both research and live decision-making
    
- ► Developing and Maintaining GreekSoft API Python Package - A Python
    package offering a RESTful interface for real-time market data operations,
    including user authentication, live data processing, and order execution. Built
    using the REST Framework and WebSocket Connections, the package is engineered for high
    performance, scalability, and clean integration. I am actively involved in the
    ongoing development, enhancement, and refactoring of the package,
    including the transition to GreekSoft CTCL Application, to ensure compatibility with evolving
    trading infrastructure and to support seamless integration into financial platforms.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Intern Python Developer | Silverstream Equitas Pvt Ltd**")
st.write("06/2024 - 09/2024")
st.write(
    """
- ► Gained hands-on experience in Advanced Python, focusing on real-world financial applications and automation.
- ► Learned the fundamentals of how financial markets operate, including market structure, order flow, and trading logic.
- ► Built custom backtesting models on historical market data to test the performance of trading strategies.
- ► Integrated these models into interactive Streamlit web applications, enabling visual analysis and simulated decision-making.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    # st.write(f"[{project}]({link})")
    if link.startswith("http"):
        st.write(f"[{project}]({link})")
    else:
        st.write(f"{project} — {link}")
tmod.sleep(60)
st.rerun()
