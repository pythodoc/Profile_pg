"""Unit tests for the pure content helpers.

Run:  python -m pytest -q
"""

from __future__ import annotations

from datetime import date

import pytest

import content as C


class TestMonthsBetween:
    def test_same_month(self) -> None:
        assert C.months_between(date(2024, 9, 1), date(2024, 9, 28)) == 0

    def test_full_year(self) -> None:
        assert C.months_between(date(2024, 9, 1), date(2025, 9, 1)) == 12

    def test_cross_year(self) -> None:
        assert C.months_between(date(2024, 9, 1), date(2025, 2, 1)) == 5

    def test_never_negative(self) -> None:
        assert C.months_between(date(2025, 1, 1), date(2024, 1, 1)) == 0


class TestHumanTenure:
    @pytest.mark.parametrize(
        ("months", "expected"),
        [
            (0, "under a month"),
            (1, "1 mo"),
            (5, "5 mos"),
            (12, "1 yr"),
            (13, "1 yr 1 mo"),
            (29, "2 yrs 5 mos"),
            (24, "2 yrs"),
        ],
    )
    def test_labels(self, months: int, expected: str) -> None:
        assert C.human_tenure(months) == expected

    def test_negative_is_clamped(self) -> None:
        assert C.human_tenure(-6) == "under a month"


class TestDerivedExperience:
    def test_counts_from_earliest_role(self) -> None:
        earliest = C.EXPERIENCE[-1]["start"]
        assert C.experience_months(date(2025, 1, 15)) == C.months_between(
            earliest, date(2025, 1, 15)
        )

    def test_years_floor_at_one(self) -> None:
        assert C.years_experience(C.EXPERIENCE[-1]["start"]) == 1


class TestContentIntegrity:
    def test_every_project_has_required_keys(self) -> None:
        for project in C.PROJECTS:
            assert project["name"], project
            assert project["desc"], project
            assert "url" in project and "flag" in project

    def test_public_projects_have_https_links(self) -> None:
        for project in C.PROJECTS:
            if project["flag"] is None:
                assert project["url"].startswith("https://"), project

    def test_roles_are_reverse_chronological(self) -> None:
        starts = [job["start"] for job in C.EXPERIENCE]
        assert starts == sorted(starts, reverse=True)

    def test_only_one_current_role(self) -> None:
        assert sum(1 for job in C.EXPERIENCE if job["current"]) == 1

    def test_current_role_has_no_end_date(self) -> None:
        for job in C.EXPERIENCE:
            if job["current"]:
                assert job["end"] is None, job
