from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "noyap.py"
SPEC = importlib.util.spec_from_file_location("noyap_script", MODULE_PATH)
assert SPEC and SPEC.loader
NOYAP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(NOYAP)


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
        self.assertEqual(metadata["implementation_permitted"], "false")


if __name__ == "__main__":
    unittest.main()
