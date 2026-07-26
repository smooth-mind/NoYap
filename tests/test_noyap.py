from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_ROOT / "scripts" / "noyap.py"

SPEC = importlib.util.spec_from_file_location("noyap_script", MODULE_PATH)
assert SPEC and SPEC.loader

NOYAP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(NOYAP)


@contextmanager
def temporary_repo() -> Iterator[Path]:
    """Copy the repository so negative-path tests never alter real files."""
    original_root = NOYAP.ROOT

    with tempfile.TemporaryDirectory() as temporary_directory:
        copied_root = Path(temporary_directory) / "repo"
        shutil.copytree(PROJECT_ROOT, copied_root)

        NOYAP.ROOT = copied_root

        try:
            yield copied_root
        finally:
            NOYAP.ROOT = original_root


def replace_once(path: Path, old: str, new: str) -> None:
    """Replace one exact fixture fragment or fail with a useful message."""
    text = path.read_text(encoding="utf-8")

    if old not in text:
        raise AssertionError(
            f"Test fixture text not found in {path}: {old!r}"
        )

    path.write_text(
        text.replace(old, new, 1),
        encoding="utf-8",
    )


class NoYapTests(unittest.TestCase):
    def test_required_template_is_valid(self) -> None:
        self.assertEqual(NOYAP.validation_errors(), [])

    def test_next_prompt_is_available(self) -> None:
        prompt = NOYAP.extract_next_prompt()

        self.assertIn("NoYap", prompt)
        self.assertIn("PROJECT_INPUT.md", prompt)

    def test_project_state_front_matter(self) -> None:
        text = NOYAP.read_text("noyap/PROJECT_STATE.md")
        metadata = NOYAP.parse_front_matter(text)

        self.assertEqual(metadata["mode"], "guided")
        self.assertEqual(metadata["baseline_status"], "draft")
        self.assertEqual(
            metadata["implementation_permitted"],
            "false",
        )

    def test_prompts_front_matter_is_valid(self) -> None:
        text = NOYAP.read_text("PROMPTS.md")
        metadata = NOYAP.parse_front_matter(text)

        self.assertEqual(metadata["document"], "prompts")
        self.assertEqual(metadata["status"], "active")
        self.assertTrue(
            NOYAP.is_valid_iso_date(metadata["last_updated"])
        )

    def test_iso_date_validation(self) -> None:
        valid = (
            "2026-07-26",
            "2024-02-29",
        )

        invalid = (
            None,
            "",
            "YYYY-MM-DD",
            "2026-2-03",
            "2026-02-30",
        )

        for value in valid:
            with self.subTest(value=value):
                self.assertTrue(
                    NOYAP.is_valid_iso_date(value)
                )

        for value in invalid:
            with self.subTest(value=value):
                self.assertFalse(
                    NOYAP.is_valid_iso_date(value)
                )

    def test_invalid_baseline_status_fails(self) -> None:
        with temporary_repo() as root:
            replace_once(
                root / "noyap/PROJECT_STATE.md",
                "baseline_status: draft",
                "baseline_status: aproved",
            )

            errors = NOYAP.validation_errors()

            self.assertTrue(
                any(
                    "baseline_status must be" in error
                    for error in errors
                ),
                errors,
            )

    def test_nonexistent_current_phase_fails(self) -> None:
        with temporary_repo() as root:
            replace_once(
                root / "noyap/PROJECT_STATE.md",
                "current_phase: phase-0",
                "current_phase: phase-999",
            )

            errors = NOYAP.validation_errors()

            self.assertTrue(
                any(
                    "does not exist in PHASES.md" in error
                    for error in errors
                ),
                errors,
            )

    def test_nonactive_current_phase_fails(self) -> None:
        with temporary_repo() as root:
            replace_once(
                root / "noyap/PROJECT_STATE.md",
                "baseline_status: draft",
                "baseline_status: approved",
            )
            replace_once(
                root / "noyap/PROJECT_STATE.md",
                "current_phase: phase-0",
                "current_phase: phase-1",
            )

            errors = NOYAP.validation_errors()

            self.assertTrue(
                any(
                    "is not Active in PHASES.md" in error
                    for error in errors
                ),
                errors,
            )

    def test_multiple_active_phases_fail(self) -> None:
        with temporary_repo() as root:
            replace_once(
                root / "noyap/PHASES.md",
                (
                    "## Phase 1: Project foundation\n\n"
                    "Replace this generic phase after requirements and "
                    "architecture are understood.\n\n"
                    "- **Status:** Planned"
                ),
                (
                    "## Phase 1: Project foundation\n\n"
                    "Replace this generic phase after requirements and "
                    "architecture are understood.\n\n"
                    "- **Status:** Active"
                ),
            )

            errors = NOYAP.validation_errors()

            self.assertIn(
                "PHASES.md must contain exactly one Active phase",
                errors,
            )

    def test_duplicate_phase_identifier_is_reported(self) -> None:
        phases_text = """\
## Phase 0: Discovery

- **Status:** Active

## Phase 0: Duplicate

- **Status:** Planned
"""

        _, errors = NOYAP.parse_phases(phases_text)

        self.assertTrue(
            any(
                "Duplicate phase identifier" in error
                for error in errors
            ),
            errors,
        )

    def test_missing_required_change_directory_fails(self) -> None:
        with temporary_repo() as root:
            shutil.rmtree(
                root / "noyap/changes/proposed"
            )

            errors = NOYAP.validation_errors()

            self.assertIn(
                "Missing required directory: "
                "noyap/changes/proposed",
                errors,
            )

    def test_malformed_prompts_front_matter_fails(self) -> None:
        with temporary_repo() as root:
            prompts_path = root / "PROMPTS.md"

            # Break the closing front-matter fence without depending
            # on the value of last_updated.
            replace_once(
                prompts_path,
                "\n---\n\n# NoYap Project Prompts",
                "\n------------------------\n\n"
                "# NoYap Project Prompts",
            )

            errors = NOYAP.validation_errors()

            self.assertTrue(
                any(
                    "PROMPTS.md" in error
                    and "front matter" in error.lower()
                    for error in errors
                ),
                errors,
            )

    def test_duplicated_prompt_project_state_fails(self) -> None:
        with temporary_repo() as root:
            prompts_path = root / "PROMPTS.md"
            text = prompts_path.read_text(
                encoding="utf-8"
            )

            marker = "## Current project state\n"
            replacement = (
                marker
                + "\n- Current phase: Phase 0\n"
            )

            if marker not in text:
                self.fail(
                    "PROMPTS.md current-state heading not found"
                )

            prompts_path.write_text(
                text.replace(
                    marker,
                    replacement,
                    1,
                ),
                encoding="utf-8",
            )

            errors = NOYAP.validation_errors()

            self.assertTrue(
                any(
                    "current phase" in error.lower()
                    for error in errors
                ),
                errors,
            )


if __name__ == "__main__":
    unittest.main()
    