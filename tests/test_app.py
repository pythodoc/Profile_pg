"""Smoke tests for the rendered page, using Streamlit's own AppTest harness.

These run the real script without a browser, so a broken f-string, a renamed
asset or a malformed builder fails CI instead of the live site.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parents[1] / "Gaurav_N_Digital_CV.py")


@pytest.fixture(scope="module")
def rendered() -> AppTest:
    at = AppTest.from_file(APP, default_timeout=60).run()
    return at


def test_renders_without_exception(rendered: AppTest) -> None:
    assert not rendered.exception, rendered.exception


def test_no_error_elements(rendered: AppTest) -> None:
    assert not rendered.error, [e.value for e in rendered.error]


def test_all_sections_present(rendered: AppTest) -> None:
    html = "\n".join(m.value for m in rendered.markdown)
    for heading in (
        "What I focus on",
        "Experience",
        "Selected projects",
        "Toolkit",
        "Key achievements",
    ):
        assert heading in html, f"missing section: {heading}"


def test_current_projects_are_listed(rendered: AppTest) -> None:
    html = "\n".join(m.value for m in rendered.markdown)
    assert "Aegis" in html
    assert "700+ devices" in html
    assert "Retail trading platform" in html
    assert "GreekSoft" in html


def test_experience_includes_support_track(rendered: AppTest) -> None:
    html = "\n".join(m.value for m in rendered.markdown)
    assert "Desktop Support Engineer" in html
    assert "Ashtech" in html


def test_hero_and_contact_render(rendered: AppTest) -> None:
    html = "\n".join(m.value for m in rendered.markdown)
    assert "Gaurav Nazare" in html
    assert "gn-hero" in html
    assert "gn-contact" in html
    # AppTest does not surface download_button/link_button as `button`,
    # so the CTA row is verified by the browser check in CI, not here.


def test_css_is_injected(rendered: AppTest) -> None:
    assert any("<style>" in m.value for m in rendered.markdown)
