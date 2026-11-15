#!/usr/bin/env python3
"""Lightweight structural validation for Daanik Agent Skills.

Copyright (c) 2026 Daanik Eduventures Private Limited.
Licensed under the MIT License.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".agents" / "skills"
REQUIRED_SECTIONS = (
    "What this skill does",
    "When to use it",
    "How the person can start",
    "Step-by-step workflow",
    "Examples",
    "Privacy, safety and limits",
    "Before responding, check",
)
EXPECTED_SKILLS = {
    "daily-planner",
    "money-companion",
    "smart-shopping-advocate",
    "communication-coach",
    "learning-coach",
    "home-life-admin",
    "digital-safety-checker",
    "decision-clarity-coach",
}
COPYRIGHT = "Copyright (c) 2026 Daanik Eduventures Private Limited."


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return [f"{path}: missing YAML frontmatter opening delimiter"]

    parts = text.split("---", 2)
    if len(parts) < 3:
        return [f"{path}: malformed YAML frontmatter"]

    frontmatter = parts[1]
    name_match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", frontmatter)
    desc_match = re.search(r"(?m)^description:\s*(.+)\s*$", frontmatter)
    if not name_match:
        errors.append(f"{path}: missing or invalid name field")
    elif name_match.group(1) != path.parent.name:
        errors.append(f"{path}: name does not match skill folder")

    if not desc_match:
        errors.append(f"{path}: missing description field")
    elif len(desc_match.group(1).strip()) > 1024:
        errors.append(f"{path}: description exceeds 1024 characters")

    if COPYRIGHT not in text:
        errors.append(f"{path}: missing Daanik copyright attribution")

    for section in REQUIRED_SECTIONS:
        if section.lower() not in text.lower():
            errors.append(f"{path}: missing required guidance section: {section}")

    if "password" not in text.lower() and "privacy" not in text.lower():
        errors.append(f"{path}: missing privacy guidance")
    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"ERROR: missing {SKILLS_DIR}")
        return 1

    folders = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
    errors: list[str] = []

    missing = EXPECTED_SKILLS - folders
    extra = folders - EXPECTED_SKILLS
    if missing:
        errors.append(f"Missing expected Skills: {', '.join(sorted(missing))}")
    if extra:
        print(f"INFO: Additional Skill folders: {', '.join(sorted(extra))}")

    for folder in sorted(folders):
        skill_path = SKILLS_DIR / folder / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"{folder}: missing SKILL.md")
            continue
        errors.extend(validate_skill(skill_path))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed for {len(folders)} Skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
