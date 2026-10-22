"""Smoke tests for the rendered page, using Streamlit's own AppTest harness.

These run the real script without a browser, so a broken f-string, a renamed
asset or a malformed builder fails CI instead of the live site.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
APP = str(ROOT / "Gaurav_N_Digital_CV.py")


@pytest.fixture(scope="module")
def entry() -> ModuleType:
    """Import the entry point by path, so the filename can change per repo."""
    spec = importlib.util.spec_from_file_location("entry", APP)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def rendered() -> AppTest:
    at = AppTest.from_file(APP, default_timeout=60).run()
    return at


def _modern(width: str = "stretch") -> None:  # pretends to be st.link_button (1.49+)
    return None


def _legacy(use_container_width: bool = True) -> None:  # 1.48-era signature
    return None


def test_stretch_kwargs_uses_width_when_supported(entry: ModuleType) -> None:
    assert entry.stretch_kwargs(_modern) == {"width": "stretch"}


def test_stretch_kwargs_falls_back_to_use_container_width(entry: ModuleType) -> None:
    assert entry.stretch_kwargs(_legacy) == {"use_container_width": True}


def test_stretch_kwargs_survives_uninspectable_target(entry: ModuleType) -> None:
    assert entry.stretch_kwargs(object()) == {"use_container_width": True}


def test_no_image_library_at_runtime() -> None:
    """Regression guard: Pillow 12 conflicts with Streamlit's pillow<12 pin."""
    source = Path(APP).read_text(encoding="utf-8")
    assert "from PIL" not in source
    assert "import PIL" not in source


def test_requirements_have_no_pillow() -> None:
    """Only real requirement lines count — the explanatory comment says 'pillow'."""
    text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    specs = [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    assert not any("pillow" in spec.lower() for spec in specs), specs


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
