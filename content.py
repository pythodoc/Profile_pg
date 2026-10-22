"""Profile content and pure helpers.

Kept free of Streamlit imports so it can be unit-tested and reused.
All copy lives here — update this file to change the CV, not the entry point.
"""

from __future__ import annotations

from datetime import date

# ---------------------------------------------------------------- identity
PAGE_TITLE = "Gaurav Nazare — Software Engineer"
PAGE_ICON = "◈"

NAME = "Gaurav Nazare"
ROLE = "Software Engineer · Platforms & Trading Systems"
LEAD = (
    "I build <strong>internal platforms and trading systems</strong> people use every day — an IT "
    "operations console serving 700+ devices, a retail trading front end on the firm's trading API, "
    "and the market-data clients underneath. I started on desktop support, so I build for the "
    "workflows I used to run by hand."
)
EMAIL = "gauravnazare214@gmail.com"
LOCATION = "Mumbai, India"
AVAILABILITY = "Open to opportunities"

SOCIALS = {
    "LinkedIn": "https://www.linkedin.com/in/gaurav-nazare-bkt9741/",
    "GitHub": "https://github.com/pythodoc",
}

# ---------------------------------------------------------------- experience
# `start` / `end` are the single source of truth: tenure badges and the
# "years of experience" stat are derived, so they can never go stale.
EXPERIENCE = [
    {
        "role": "Software Engineer",
        "company": "Silverstream Equities",
        "location": "Mumbai",
        "start": date(2024, 9, 1),
        "end": None,
        "current": True,
        "bullets": [
            "<strong>Sole developer of Aegis</strong>, an internal IT operations platform now in UAT: "
            "asset and licence tracking, VM host/guest inventory, one-click Ansible patch and software "
            "deployment to Linux and Windows, plus SSH and remote VNC from one console.",
            "<strong>Sole developer of a retail trading platform</strong> built on the firm's trading "
            "REST API — dealer-ID integration, full order-scenario coverage, Next.js front end over a "
            "Python/PostgreSQL backend.",
            "Ship custom trading logic on Pandas and NumPy — signal generation, market analysis and "
            "strategy backtesting over historical market data.",
            "Build Streamlit and Gradio dashboards that surface live market trends, trading signals "
            "and simulated trades, and maintain <strong>GreekSoft</strong>, a published Python client "
            "for broker REST and WebSocket APIs.",
        ],
        "tags": ["Python", "FastAPI", "Next.js", "PostgreSQL", "Ansible", "Docker", "Pandas", "Streamlit"],
    },
    {
        "role": "Intern — Python Developer",
        "company": "Silverstream Equities",
        "location": "Mumbai",
        "start": date(2024, 7, 1),
        "end": date(2024, 9, 1),
        "current": False,
        "bullets": [
            "Built backtesting models on historical market data to evaluate trading strategy performance.",
            "Wrapped those models in Streamlit apps for visual analysis and simulated decision-making.",
            "Developed a working foundation in market structure, order flow and trading logic.",
        ],
        "tags": ["Python", "Pandas", "Streamlit", "Backtesting"],
    },
    {
        "role": "Desktop Support Engineer",
        "company": "Ashtech · Chenoa · Microland",
        "location": "Mumbai",
        "start": date(2020, 7, 1),
        "end": date(2024, 7, 1),
        "current": False,
        "track": "support",
        "bullets": [
            "Provided end-user and systems support across desktop environments, diagnosing hardware, "
            "OS and network faults for four years in direct employment.",
            "Worked inside the manual workflows — asset tracking, patching, remote sessions, licence "
            "records — that Aegis now replaces. The requirements came from doing this work, not "
            "researching it.",
        ],
        "tags": ["Windows", "Hardware", "Networking", "End-user support"],
    },
]

# ---------------------------------------------------------------- focus
FOCUS = [
    {
        "icon": "chart",
        "title": "Trading systems",
        "text": "Signal generation, backtesting and order flows on top of broker APIs, tested end to end.",
    },
    {
        "icon": "api",
        "title": "Internal platforms",
        "text": "Full-stack tools that replace manual IT work — inventory, deployment, remote access.",
    },
    {
        "icon": "board",
        "title": "APIs & data services",
        "text": "REST and WebSocket clients, ETL pipelines and schemas built for reliability at speed.",
    },
]

# ---------------------------------------------------------------- projects
# flag: None = public, "Internal" = shipped inside an organisation (no link).
# metric: the one number a reader should remember, rendered under the summary.
PROJECTS = [
    {
        "name": "Aegis",
        "desc": "IT operations console replacing several paid tools: asset and licence tracking, VM "
                "inventory, network-device records, one-click Ansible patch and software deployment to "
                "Linux and Windows, SSH and remote VNC. Sole developer, from requirements through "
                "support — in UAT, go-live pending load test.",
        "metric": "700+ devices · ~500 users · 100k+ records",
        "stack": "FastAPI · Next.js · TimescaleDB",
        "url": None,
        "flag": "Internal",
    },
    {
        "name": "Retail trading platform",
        "desc": "Trading front end for retail clients on the firm's trading REST API — dealer-ID "
                "integration, complete order-scenario coverage, tested end to end against the live API. "
                "Sole developer; in UAT ahead of go-live.",
        "metric": "8–10 traders now · 75 planned at rollout",
        "stack": "Next.js · Python · PostgreSQL",
        "url": None,
        "flag": "Internal",
    },
    {
        "name": "GreekSoft API",
        "desc": "Published Python client wrapping broker REST and WebSocket endpoints — auth, live "
                "market data and order execution. Installable straight from PyPI.",
        "metric": "Published package",
        "stack": "Python · REST · WebSocket",
        "url": "https://pypi.org/project/greeksoft/",
        "flag": None,
    },
    {
        "name": "Paramount Holidayz",
        "desc": "Django website that markets holiday packages and turns enquiries into bookings for a "
                "travel business.",
        "metric": "Live in production",
        "stack": "Django · Python · HTML",
        "url": "https://paramountholidayz.com/",
        "flag": None,
    },
    {
        "name": "Temple Website",
        "desc": "Custom Streamlit site for a temple trust — content pages, events and a responsive "
                "layout for phone-first visitors.",
        "metric": "Public, phone-first",
        "stack": "Streamlit · Python",
        "url": "https://omshivgorakshayogiasthana.streamlit.app/",
        "flag": None,
    },
    {
        "name": "Database Keyword Search",
        "desc": "Internal tool for fast keyword discovery across structured datasets and schemas.",
        "metric": "Used by internal teams",
        "stack": "Python · SQL",
        "url": None,
        "flag": "Internal",
    },
    {
        "name": "Email Ticket Tracking",
        "desc": "Workflow automation that captures, triages and tracks support tickets raised over email.",
        "metric": "Replaced a manual queue",
        "stack": "Python · SQL · Automation",
        "url": None,
        "flag": "Internal",
    },
]

# ---------------------------------------------------------------- skills
SKILLS = {
    "Languages": ["Python", "SQL", "Bash"],
    "Backend & APIs": ["FastAPI", "Django", "Django REST Framework", "REST", "WebSockets"],
    "Data & infra": ["PostgreSQL", "TimescaleDB", "MySQL", "MongoDB", "Pandas", "NumPy", "Docker", "Ansible"],
    "Frontend & tooling": ["Next.js", "Streamlit", "Gradio", "Plotly", "GitLab CI", "Git", "Linux"],
}

# ---------------------------------------------------------------- wins
WINS = [
    "Built Aegis end to end — now the IT team's single console for 700+ devices, replacing several "
    "paid tools.",
    "Took a retail trading platform from CEO brief to UAT as sole developer, with dealer-ID "
    "integration and every order scenario tested.",
    "Published GreekSoft on PyPI so broker connectivity is a reusable client, not one-off scripts.",
]


# ---------------------------------------------------------------- helpers
def months_between(start: date, end: date) -> int:
    """Whole months from start to end, floored at zero."""
    return max(0, (end.year - start.year) * 12 + (end.month - start.month))


def human_tenure(months: int) -> str:
    """Compact tenure label, e.g. 29 -> '2 yrs 5 mos'."""
    years, rem = divmod(max(0, months), 12)
    parts = []
    if years:
        parts.append(f"{years} yr" if years == 1 else f"{years} yrs")
    if rem:
        parts.append(f"{rem} mo" if rem == 1 else f"{rem} mos")
    return " ".join(parts) or "under a month"


def experience_months(today: date | None = None) -> int:
    """Total professional tenure, counting from the earliest role."""
    today = today or date.today()
    return months_between(EXPERIENCE[-1]["start"], today)


def years_experience(today: date | None = None) -> int:
    """Completed years of experience, never below 1 for display purposes."""
    return max(1, experience_months(today) // 12)


def engineering_months(today: date | None = None) -> int:
    """Tenure in engineering roles specifically (excludes the support track)."""
    today = today or date.today()
    starts = [job["start"] for job in EXPERIENCE if job.get("track", "engineering") == "engineering"]
    return months_between(min(starts), today)
