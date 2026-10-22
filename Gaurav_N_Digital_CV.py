"""Gaurav Nazare — Digital CV (Streamlit).

Single-page professional profile. Copy and data live in content.py,
presentation in main.css, markup builders here.

    streamlit run Gaurav_N_Digital_CV.py
"""

from __future__ import annotations

import base64
import io
import textwrap
from datetime import date
from pathlib import Path
from urllib.parse import quote

import streamlit as st
from PIL import Image

import content as C

BASE_DIR = Path(__file__).parent
CSS_FILE = BASE_DIR / "main.css"

CV_CANDIDATES = [BASE_DIR / "CV.pdf", BASE_DIR / "Gaurav_Nazare_CV.pdf"]
# assets/profile.png is the curated, headroom-corrected crop — prefer it over the
# raw camera file, which is framed too tight for a circular mask.
PIC_CANDIDATES = [
    BASE_DIR / "assets" / "profile.png",
    BASE_DIR / "gaurav profile_pic1.PNG",
    BASE_DIR / "profile.png",
    BASE_DIR / "assets" / "profile.jpg",
]


# --------------------------------------------------------------------------
# assets
# --------------------------------------------------------------------------
def first_existing(paths: list[Path]) -> Path | None:
    return next((p for p in paths if p.is_file()), None)


@st.cache_data(show_spinner=False, max_entries=4)
def avatar_data_uri(path_str: str, size: int = 360) -> str:
    """Inline the portrait as a compact JPEG data URI (one HTML block, no layout gap)."""
    img = Image.open(path_str).convert("RGB")
    side = min(img.size)
    left = (img.width - side) // 2
    # bias the crop upward so the face sits on the optical centre
    top = max(0, (img.height - side) // 2 - int(side * 0.06))
    img = img.crop((left, top, left + side, min(top + side, img.height)))
    img = img.resize((size, size), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=86, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def initials_avatar(name: str) -> str:
    """Fallback avatar so a missing photo degrades gracefully instead of breaking."""
    initials = "".join(part[0] for part in name.split()[:2]).upper()
    svg = textwrap.dedent(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360">
        <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#1f8f6b"/><stop offset="1" stop-color="#2f5bd0"/>
        </linearGradient></defs>
        <rect width="360" height="360" fill="url(#g)"/>
        <text x="50%" y="50%" dy=".35em" text-anchor="middle" font-family="Inter,Arial"
        font-size="140" font-weight="700" fill="#ffffff">{initials}</text></svg>"""
    ).replace("\n", "").replace("  ", "")
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


# --------------------------------------------------------------------------
# icons
# --------------------------------------------------------------------------
_ICON_ATTRS = 'width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    "chart": f'<svg viewBox="0 0 24 24" {_ICON_ATTRS}><path d="M3 20h18"/><path d="M6 16V9"/>'
             '<path d="M11 16V5"/><path d="M16 16v-4"/></svg>',
    "api": f'<svg viewBox="0 0 24 24" {_ICON_ATTRS}><path d="M8 7a4 4 0 0 1 8 0"/>'
           '<rect x="3" y="7" width="18" height="13" rx="3"/><path d="M12 12v3"/></svg>',
    "board": f'<svg viewBox="0 0 24 24" {_ICON_ATTRS}><rect x="3" y="4" width="18" height="16" rx="2"/>'
             '<path d="M3 10h18"/><path d="M9 10v10"/></svg>',
}

_SMALL = 'width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
ICON_MAIL = f'<svg viewBox="0 0 24 24" {_SMALL}><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
ICON_LINK = f'<svg viewBox="0 0 24 24" {_SMALL}><path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>'
ICON_GH = ('<svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M12 0C5.37 0 0 '
           '5.37 0 12c0 5.3 3.44 9.8 8.21 11.39.6.11.82-.26.82-.58 0-.29-.01-1.05-.02-2.06-3.34.73-4.04'
           '-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.09-.74.08-.73.08-.73 1.2.08 1.84 1.23 1.84 '
           '1.23 1.07 1.84 2.8 1.31 3.49 1 .11-.78.42-1.31.76-1.61-2.66-.3-5.46-1.33-5.46-5.93 0-1.31'
           '.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.17 0 0 1.01-.32 3.3 1.23.96-.27 1.99-.4 3.01-.4 '
           '1.02 0 2.05.14 3.01.4 2.29-1.55 3.3-1.23 3.3-1.23.66 1.65.24 2.87.12 3.17.77.84 1.24 1.91 '
           '1.24 3.22 0 4.61-2.8 5.62-5.47 5.92.43.37.81 1.1.81 2.22 0 1.6-.01 2.89-.01 3.28 0 .32.22'
           '.69.82.58C20.56 21.8 24 17.3 24 12c0-6.63-5.37-12-12-12z"/></svg>')
ICON_LI = ('<svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M4.98 3.5C4.98 4.88 '
           '3.86 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.5 8h4v16h-4V8zm7.5 0h3.8v2.2h.06'
           'c.53-1 1.83-2.2 3.77-2.2 4.03 0 4.77 2.65 4.77 6.1V24h-4v-7.6c0-1.81-.03-4.14-2.52-4.14-2.52 '
           '0-2.9 1.97-2.9 4.01V24h-4V8z"/></svg>')


# --------------------------------------------------------------------------
# markup builders
# --------------------------------------------------------------------------
def section(title: str, body: str, note: str = "") -> str:
    note_html = f'<span class="gn-section-note">{note}</span>' if note else ""
    return (
        f'<section class="gn-section"><div class="gn-section-head">'
        f'<h2 class="gn-section-title">{title}</h2>{note_html}</div>{body}</section>'
    )


def hero(avatar_uri: str) -> str:
    chips = "".join(
        [
            f'<span class="gn-chip gn-chip-live"><span class="gn-dot"></span>{C.AVAILABILITY}</span>',
            f'<span class="gn-chip">{C.LOCATION}</span>',
            f'<span class="gn-chip"><b>{C.human_tenure(C.engineering_months())}</b> in engineering</span>',
            f'<span class="gn-chip">{C.EMAIL}</span>',
        ]
    )
    return (
        '<header class="gn-hero"><div class="gn-hero-grid">'
        '<div class="gn-avatar-wrap"><div class="gn-avatar-halo"></div>'
        f'<img class="gn-avatar" src="{avatar_uri}" alt="Portrait of {C.NAME}"></div>'
        "<div>"
        f'<span class="gn-eyebrow">{C.ROLE}</span>'
        f'<h1 class="gn-name">{C.NAME}</h1>'
        f'<p class="gn-lead">{C.LEAD}</p>'
        f'<div class="gn-chips">{chips}</div>'
        "</div></div></header>"
    )


def stats() -> str:
    items = [
        (f"{C.years_experience()}+", "Years in tech"),
        (str(len(C.PROJECTS)), "Projects shipped"),
        ("700+", "Devices managed"),
        ("1", "PyPI package"),
    ]
    body = "".join(
        f'<div class="gn-stat"><div class="gn-stat-value">{v}</div>'
        f'<div class="gn-stat-label">{k}</div></div>'
        for v, k in items
    )
    return f'<div class="gn-stats">{body}</div>'


def focus() -> str:
    cards = "".join(
        f'<div class="gn-focus-card"><div class="gn-focus-icon">{ICONS.get(c["icon"], "")}</div>'
        f'<div class="gn-focus-title">{c["title"]}</div>'
        f'<p class="gn-focus-text">{c["text"]}</p></div>'
        for c in C.FOCUS
    )
    return f'<div class="gn-focus">{cards}</div>'


def experience(today: date) -> str:
    items = []
    for job in C.EXPERIENCE:
        end = job["end"] or today
        tenure = C.human_tenure(C.months_between(job["start"], end))
        if job["current"]:
            dates = f'{job["start"]:%b %Y} — Present · {tenure}'
            badge = '<span class="gn-badge is-live">Current</span>'
        else:
            dates = f'{job["start"]:%b %Y} — {job["end"]:%b %Y} · {tenure}'
            badge = ""

        bullets = "".join(f"<li>{b}</li>" for b in job["bullets"])
        tags = "".join(f'<span class="gn-tag">{t}</span>' for t in job["tags"])
        items.append(
            f'<article class="gn-job{" is-current" if job["current"] else ""}">'
            f'<div class="gn-job-top"><h3 class="gn-role">{job["role"]} '
            f'<span>· {job["company"]}</span></h3><div class="gn-badges">{badge}</div></div>'
            f'<p class="gn-dates">{dates}</p>'
            f'<ul class="gn-bullets">{bullets}</ul>'
            f'<div class="gn-tags">{tags}</div></article>'
        )
    return f'<div class="gn-timeline">{"".join(items)}</div>'


def projects() -> str:
    cards = []
    for p in C.PROJECTS:
        flag = f'<span class="gn-project-flag">{p["flag"]}</span>' if p.get("flag") else ""
        if p.get("url"):
            link = f'<a class="gn-project-link" href="{p["url"]}" target="_blank" rel="noopener">Visit ↗</a>'
        else:
            link = '<span class="gn-project-stack">Shipped internally</span>'
        metric = f'<div class="gn-project-metric">{p["metric"]}</div>' if p.get("metric") else ""
        cards.append(
            '<article class="gn-project">'
            f'<div class="gn-project-head"><h3 class="gn-project-title">{p["name"]}</h3>{flag}</div>'
            f'<p class="gn-project-desc">{p["desc"]}</p>'
            f"{metric}"
            f'<div class="gn-project-foot">{link}'
            f'<span class="gn-project-stack">{p["stack"]}</span></div></article>'
        )
    return f'<div class="gn-projects">{"".join(cards)}</div>'


def skills() -> str:
    groups = "".join(
        f'<div class="gn-skill-group"><h4>{group}</h4><div class="gn-pills">'
        + "".join(f'<span class="gn-pill">{s}</span>' for s in items)
        + "</div></div>"
        for group, items in C.SKILLS.items()
    )
    return f'<div class="gn-skills">{groups}</div>'


def wins() -> str:
    cards = "".join(
        f'<div class="gn-win"><div class="gn-win-mark">0{i + 1}</div>'
        f'<p class="gn-win-text">{w}</p></div>'
        for i, w in enumerate(C.WINS)
    )
    return f'<div class="gn-wins">{cards}</div>'


def contact() -> str:
    mail_subject = quote("Let's talk — software engineering role")
    return (
        '<section class="gn-contact">'
        "<h3>Let’s build something reliable.</h3>"
        "<p>Open to software engineering roles across trading systems, data platforms and backend "
        "engineering — Mumbai or remote.</p>"
        '<div class="gn-contact-links">'
        f'<a href="mailto:{C.EMAIL}?subject={mail_subject}">{ICON_MAIL}{C.EMAIL}</a>'
        f'<a href="{C.SOCIALS["LinkedIn"]}" target="_blank" rel="noopener">{ICON_LI}LinkedIn</a>'
        f'<a href="{C.SOCIALS["GitHub"]}" target="_blank" rel="noopener">{ICON_GH}GitHub</a>'
        "</div></section>"
    )


# --------------------------------------------------------------------------
# page
# --------------------------------------------------------------------------
def main() -> None:
    st.set_page_config(
        page_title=C.PAGE_TITLE,
        page_icon=C.PAGE_ICON,
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    if CSS_FILE.is_file():
        st.markdown(f"<style>{CSS_FILE.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

    today = date.today()

    pic = first_existing(PIC_CANDIDATES)
    avatar_uri = avatar_data_uri(str(pic)) if pic else initials_avatar(C.NAME)

    st.markdown(hero(avatar_uri), unsafe_allow_html=True)

    # Action row — native controls so the CV download works and analytics count.
    cv = first_existing(CV_CANDIDATES)
    with st.container(key="actions"):
        col_cv, col_mail, col_li, col_gh = st.columns(
            [1, 1, 1, 1], gap="small", vertical_alignment="center"
        )
        with col_cv:
            if cv:
                st.download_button(
                    ":material/download:  Download CV",
                    data=cv.read_bytes(),
                    file_name="Gaurav_Nazare_CV.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
            else:
                st.link_button(":material/mail:  Request CV",
                               f"mailto:{C.EMAIL}?subject=CV%20request", use_container_width=True)
        with col_mail:
            st.link_button("Email", f"mailto:{C.EMAIL}", use_container_width=True)
        with col_li:
            st.link_button("LinkedIn", C.SOCIALS["LinkedIn"], use_container_width=True)
        with col_gh:
            st.link_button("GitHub", C.SOCIALS["GitHub"], use_container_width=True)

    st.markdown(stats(), unsafe_allow_html=True)
    st.markdown(section("What I focus on", focus()), unsafe_allow_html=True)
    st.markdown(section("Experience", experience(today), "tenure updates automatically"),
                unsafe_allow_html=True)
    st.markdown(section("Selected projects", projects(), f"{len(C.PROJECTS)} shipped"),
                unsafe_allow_html=True)
    st.markdown(section("Toolkit", skills()), unsafe_allow_html=True)
    st.markdown(section("Key achievements", wins()), unsafe_allow_html=True)
    st.markdown(contact(), unsafe_allow_html=True)
    st.markdown(f'<p class="gn-footer">© {today.year} {C.NAME} · Built with Streamlit</p>',
                unsafe_allow_html=True)


if __name__ == "__main__":
    main()
