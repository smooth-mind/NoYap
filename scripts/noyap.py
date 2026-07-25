#!/usr/bin/env python3
"""Small, dependency-free helpers for a NoYap repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "AGENTS.md",
    "PROJECT_INPUT.md",
    "PROMPTS.md",
    "noyap/PRD.md",
    "noyap/SCOPE.md",
    "noyap/ARCHITECTURE.md",
    "noyap/TECH_STACK.md",
    "noyap/DESIGN.md",
    "noyap/RULES.md",
    "noyap/PHASES.md",
    "noyap/PROJECT_STATE.md",
    "noyap/MEMORY.md",
)

GOVERNANCE_FILES = (
    "noyap/PRD.md",
    "noyap/SCOPE.md",
    "noyap/ARCHITECTURE.md",
    "noyap/TECH_STACK.md",
    "noyap/DESIGN.md",
    "noyap/RULES.md",
    "noyap/PHASES.md",
    "noyap/PROJECT_STATE.md",
    "noyap/MEMORY.md",
)

BASELINE_FILES = (
    "noyap/PRD.md",
    "noyap/SCOPE.md",
    "noyap/ARCHITECTURE.md",
    "noyap/TECH_STACK.md",
    "noyap/RULES.md",
    "noyap/PHASES.md",
)

VALID_STATUSES = {
    "draft",
    "under-review",
    "approved",
    "active",
    "blocked",
    "completed",
    "superseded",
    "not-applicable",
}

FRONT_MATTER_PATTERN = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
NEXT_PROMPT_PATTERN = re.compile(
    r"<!-- NEXT_PROMPT_START -->\s*(.*?)\s*<!-- NEXT_PROMPT_END -->",
    re.DOTALL,
)


def read_text(relative_path: str) -> str:
    path = ROOT / relative_path
    return path.read_text(encoding="utf-8")


def parse_front_matter(text: str) -> dict[str, str]:
    match = FRONT_MATTER_PATTERN.search(text)
    if not match:
        return {}

    result: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def validation_errors() -> list[str]:
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            errors.append(f"Missing required file: {relative_path}")
            continue
        if not path.read_text(encoding="utf-8").strip():
            errors.append(f"Required file is empty: {relative_path}")

    governance_metadata: dict[str, dict[str, str]] = {}
    for relative_path in GOVERNANCE_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            continue
        metadata = parse_front_matter(path.read_text(encoding="utf-8"))
        governance_metadata[relative_path] = metadata
        if not metadata:
            errors.append(f"Missing YAML front matter: {relative_path}")
            continue
        status = metadata.get("status")
        if not status:
            errors.append(f"Missing status in front matter: {relative_path}")
        elif status not in VALID_STATUSES:
            errors.append(f"Invalid status '{status}' in {relative_path}")

    state_path = ROOT / "noyap/PROJECT_STATE.md"
    if state_path.is_file():
        metadata = governance_metadata.get("noyap/PROJECT_STATE.md", {})
        for field in (
            "status",
            "mode",
            "baseline_status",
            "implementation_permitted",
            "current_phase",
            "current_task",
        ):
            if not metadata.get(field):
                errors.append(f"PROJECT_STATE.md is missing front-matter field: {field}")

        if metadata.get("mode") not in {"guided", "balanced", "autonomous"}:
            errors.append(
                "PROJECT_STATE.md mode must be guided, balanced, or autonomous"
            )
        if metadata.get("implementation_permitted") not in {"true", "false"}:
            errors.append(
                "PROJECT_STATE.md implementation_permitted must be true or false"
            )

        baseline_status = metadata.get("baseline_status")
        implementation_permitted = metadata.get("implementation_permitted")
        current_phase = metadata.get("current_phase", "")

        if implementation_permitted == "true" and baseline_status != "approved":
            errors.append(
                "Implementation cannot be permitted until baseline_status is approved"
            )
        if current_phase != "phase-0" and baseline_status != "approved":
            errors.append(
                "A project cannot leave phase-0 until the baseline is approved"
            )

        if baseline_status == "approved":
            for relative_path in BASELINE_FILES:
                document_status = governance_metadata.get(relative_path, {}).get("status")
                if document_status != "approved":
                    errors.append(
                        f"Approved baseline requires {relative_path} status approved"
                    )

            design_status = governance_metadata.get("noyap/DESIGN.md", {}).get("status")
            if design_status not in {"approved", "not-applicable"}:
                errors.append(
                    "Approved baseline requires DESIGN.md to be approved or not-applicable"
                )

            for relative_path in (*BASELINE_FILES, "noyap/DESIGN.md"):
                document = governance_metadata.get(relative_path, {})
                if document.get("status") == "approved":
                    if document.get("approved_by") in {None, "", "null"}:
                        errors.append(f"Approved document lacks approved_by: {relative_path}")
                    if document.get("approved_on") in {None, "", "null"}:
                        errors.append(f"Approved document lacks approved_on: {relative_path}")

    prompts_path = ROOT / "PROMPTS.md"
    if prompts_path.is_file():
        prompts = prompts_path.read_text(encoding="utf-8")
        matches = NEXT_PROMPT_PATTERN.findall(prompts)
        if len(matches) != 1:
            errors.append(
                "PROMPTS.md must contain exactly one NEXT_PROMPT_START/END block"
            )
        elif not matches[0].strip():
            errors.append("The NEXT PROMPT block is empty")

    memory_path = ROOT / "noyap/MEMORY.md"
    if memory_path.is_file():
        memory_lines = memory_path.read_text(encoding="utf-8").splitlines()
        metadata = parse_front_matter("\n".join(memory_lines))
        try:
            soft_limit = int(metadata.get("soft_line_limit", "250"))
        except ValueError:
            errors.append("MEMORY.md soft_line_limit must be an integer")
        else:
            if len(memory_lines) > soft_limit:
                errors.append(
                    f"MEMORY.md has {len(memory_lines)} lines, above soft limit {soft_limit}"
                )

    return errors


def command_validate(_: argparse.Namespace) -> int:
    errors = validation_errors()
    if errors:
        print("NoYap validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("NoYap validation passed.")
    return 0


def command_status(_: argparse.Namespace) -> int:
    path = ROOT / "noyap/PROJECT_STATE.md"
    if not path.is_file():
        print("PROJECT_STATE.md is missing.", file=sys.stderr)
        return 1

    metadata = parse_front_matter(path.read_text(encoding="utf-8"))
    fields = (
        ("NoYap version", "noyap_version"),
        ("Mode", "mode"),
        ("Baseline", "baseline_status"),
        ("Implementation permitted", "implementation_permitted"),
        ("Current phase", "current_phase"),
        ("Current task", "current_task"),
        ("Last updated", "last_updated"),
    )
    for label, key in fields:
        print(f"{label}: {metadata.get(key, '<missing>')}")
    return 0


def extract_next_prompt() -> str:
    prompts = read_text("PROMPTS.md")
    match = NEXT_PROMPT_PATTERN.search(prompts)
    if not match:
        raise ValueError("NEXT PROMPT markers were not found")
    value = match.group(1).strip()
    if value.startswith("```text") and value.endswith("```"):
        value = value[len("```text") : -len("```")].strip()
    return value


def command_next(_: argparse.Namespace) -> int:
    try:
        print(extract_next_prompt())
    except (OSError, ValueError) as exc:
        print(f"Unable to read next prompt: {exc}", file=sys.stderr)
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="noyap",
        description="Validate and inspect a NoYap project.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser(
        "validate", help="Validate required NoYap files and state"
    )
    validate_parser.set_defaults(handler=command_validate)

    status_parser = subparsers.add_parser(
        "status", help="Print concise project state metadata"
    )
    status_parser.set_defaults(handler=command_status)

    next_parser = subparsers.add_parser(
        "next", help="Print the current copy-paste prompt"
    )
    next_parser.set_defaults(handler=command_next)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
