from pathlib import Path
import streamlit as st
from PIL import Image
import time
from datetime import date

if "last_rerun" not in st.session_state:
    st.session_state.last_rerun = time.time()

if time.time() - st.session_state.last_rerun > 60:
    st.session_state.last_rerun = time.time()
    st.experimental_rerun()


def _months_between(start: date, end: date) -> int:
    return (end.year - start.year) * 12 + (end.month - start.month)


def format_tenure(start: date, end: date) -> str:
    """Return tenure string like '1 year 5 months'."""
    months = max(0, _months_between(start, end))
    years, rem = divmod(months, 12)
    parts = []
    if years:
        parts.append(f"{years} year" + ("s" if years != 1 else ""))
    if rem:
        parts.append(f"{rem} month" + ("s" if rem != 1 else ""))
    if not parts:
        return "0 months"
    return " ".join(parts)


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "main.css"

resume_file = current_dir / "CV.pdf"

profile_pic = current_dir / "gaurav profile_pic1.PNG"


# --- GENERAL SETTINGS ---
JR_ROLE_START = date(2024, 9, 1)
INTERN_ROLE_START = date(2024, 7, 1)
INTERN_ROLE_END = date(2024, 9, 1)
PAGE_TITLE = "Digital CV | Gaurav Nazare"
PAGE_ICON = ":briefcase:"
NAME = "Gaurav Nazare"
DESCRIPTION = """
Software Engineer focused on building reliable trading systems and high-quality data services.
"""
EMAIL = "gauravnazare214@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/gaurav-nazare-bkt9741/",
    "GitHub": "https://github.com/pythodoc",
}
PROJECTS = {
    "GreekSoft API Python Library Package": "https://pypi.org/project/greeksoft/",
    "Database Keyword Search Application": "Deployed within organization",
    "Email Ticket Tracking System": "Deployed within organization",
    "Temple Website - Custom Website hosted on Streamlit": "https://omshivgorakshayogiasthana.streamlit.app/",
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
    st.caption("Profile photo")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="Gaurav_N CV.pdf",
        mime="application/octet-stream",
    )
    st.write(EMAIL)
    st.write("Mumbai, MH")


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
icon_map = {
    "LinkedIn": """<svg viewBox='0 0 24 24' width='18' height='18' fill='currentColor' aria-hidden='true'>
<path d='M4.98 3.5C4.98 4.88 3.86 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM0.5 8h4V24h-4V8zm7.5 0h3.8v2.2h.06c.53-1 1.83-2.2 3.77-2.2 4.03 0 4.77 2.65 4.77 6.1V24h-4v-7.6c0-1.81-.03-4.14-2.52-4.14-2.52 0-2.9 1.97-2.9 4.01V24h-4V8z'/>
</svg>""",
    "GitHub": """<svg viewBox='0 0 24 24' width='18' height='18' fill='currentColor' aria-hidden='true'>
<path d='M12 0C5.37 0 0 5.37 0 12c0 5.3 3.44 9.8 8.21 11.39.6.11.82-.26.82-.58 0-.29-.01-1.05-.02-2.06-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.09-.74.08-.73.08-.73 1.2.08 1.84 1.23 1.84 1.23 1.07 1.84 2.8 1.31 3.49 1 .11-.78.42-1.31.76-1.61-2.66-.3-5.46-1.33-5.46-5.93 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.17 0 0 1.01-.32 3.3 1.23.96-.27 1.99-.4 3.01-.4 1.02 0 2.05.14 3.01.4 2.29-1.55 3.3-1.23 3.3-1.23.66 1.65.24 2.87.12 3.17.77.84 1.24 1.91 1.24 3.22 0 4.61-2.8 5.62-5.47 5.92.43.37.81 1.1.81 2.22 0 1.6-.01 2.89-.01 3.28 0 .32.22.69.82.58C20.56 21.8 24 17.3 24 12c0-6.63-5.37-12-12-12z'/>
</svg>""",
}

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    icon = icon_map.get(platform, "")
    cols[index].markdown(
        f"<a href='{link}' target='_blank' style='display:inline-flex; align-items:center; gap:8px;'>"
        f"{icon}<span>{platform}</span></a>",
        unsafe_allow_html=True,
    )


# --- EXPERIENCE & QUALIFICATIONS ---
# Dynamic tenure since current role start
tenure_now = format_tenure(JR_ROLE_START, date.today())
intern_tenure = format_tenure(INTERN_ROLE_START, INTERN_ROLE_END)
# Total experience including internship
total_tenure = format_tenure(INTERN_ROLE_START, date.today())

st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    f"""
- {total_tenure} of overall experience (including internship) delivering data-driven solutions
- Python engineering across ETL, APIs, and analytics workflows for reliable, fast systems
- Data engineering focus on performance, automation, and scalable pipelines
- Data analysis with statistical rigor to convert data into actionable insights
"""
)


# --- CORE COMPETENCIES ---
st.write('\n')
st.subheader("Core Competencies")
st.write(
    """
- Trading systems development and automation
- REST API design, integration, and maintenance
- Data processing pipelines and analytics
- Dashboarding and stakeholder reporting
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
skills = [
    "Python", "Pandas", "NumPy", "REST APIs", "Django REST Framework",
    "Streamlit", "Gradio", "Plotly", "SQL", "PostgreSQL", "MongoDB", "MySQL"
]
cols = st.columns(4)
for i, skill in enumerate(skills):
    cols[i % 4].markdown(
        f"<span style='display:inline-block; padding:6px 10px; margin:4px 0; "
        f"border:1px solid rgba(255,255,255,0.15); border-radius:999px; '>{skill}</span>",
        unsafe_allow_html=True,
    )


# --- KEY ACHIEVEMENTS ---
st.write('\n')
st.subheader("Key Achievements")
st.write(
    """
- Delivered reusable trading tools that improved strategy testing turnaround
- Built real-time dashboards for signal tracking and decision support
- Contributed to API refactoring for cleaner integrations and stability
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("**Software Engineer | Silverstream Equities Pvt Ltd**")
st.write("09/2024 - Present")
st.write(
    """
- Implemented custom trading logic using Pandas and NumPy for analysis, signal generation,
  and strategy backtesting on historical market data.
- Built interactive dashboards with Streamlit and Gradio to visualize market trends,
  display trading signals, and simulate trades in real time.
- Developing and maintaining the GreekSoft API Python package, providing RESTful and
  WebSocket-based interfaces for authentication, live data processing, and order execution.
- Contributing to ongoing refactoring and the transition to GreekSoft CTCL to ensure
  compatibility with evolving trading infrastructure.
"""
)

# --- JOB 2
st.write('\n')
st.write("**Intern Python Developer | Silverstream Equities Pvt Ltd**")
st.write(f"07/2024 - 09/2024 ({intern_tenure})")
st.write(
    """
- Built backtesting models on historical market data to evaluate trading strategy performance.
- Integrated models into Streamlit applications for visual analysis and simulated decision-making.
- Developed foundations in financial market structure, order flow, and trading logic.
"""
)


# --- SELECTED PROJECTS ---
st.write('\n')
st.subheader("Selected Projects")
st.write("---")

project_cards = [
    ("GreekSoft API Python Package", "REST + WebSocket client for live market data, auth, and order execution.", "https://pypi.org/project/greeksoft/"),
    ("Database Keyword Search", "Internal tool for fast discovery across structured datasets.", None),
    ("Email Ticket Tracking", "Workflow automation for issue capture, triage, and tracking.", None),
    ("Temple Website", "Custom Streamlit site with content management and responsive UI.", "https://omshivgorakshayogiasthana.streamlit.app/")
]
for name, desc, link in project_cards:
    st.markdown(f"**{name}**")
    st.write(desc)
    if link:
        st.markdown(f"[{link}]({link})")
    st.write("")


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
