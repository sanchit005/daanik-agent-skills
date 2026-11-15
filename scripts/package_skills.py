#!/usr/bin/env python3
"""Build one ZIP per Skill for Claude.ai, ChatGPT Skills upload, or Copilot sharing.

Copyright (c) 2026 Daanik Eduventures Private Limited.
Licensed under the MIT License.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / ".agents" / "skills"
COPILOT = ROOT / ".github" / "skills"
PLATFORMS = ("claude", "openai", "copilot")


def collect_skill_files(skill_dir: Path, platform: str) -> list[Path]:
    files = [p for p in skill_dir.rglob("*") if p.is_file()]
    if platform == "claude":
        files = [p for p in files if p.relative_to(skill_dir).as_posix() != "agents/openai.yaml"]
    return sorted(files)


def build(platform: str, output_root: Path) -> int:
    source_root = COPILOT if platform == "copilot" else CANONICAL
    if not source_root.is_dir():
        raise SystemExit(f"Missing source directory: {source_root}")

    platform_dir = output_root / platform
    platform_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for skill_dir in sorted(p for p in source_root.iterdir() if p.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            print(f"SKIP {skill_dir.name}: missing SKILL.md")
            continue

        archive_path = platform_dir / f"{skill_dir.name}.zip"
        files = collect_skill_files(skill_dir, platform)
        with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
            for file_path in files:
                # The Skill directory is the ZIP root, as required by upload flows.
                arcname = Path(skill_dir.name) / file_path.relative_to(skill_dir)
                archive.write(file_path, arcname.as_posix())

        print(f"CREATED {archive_path.relative_to(ROOT)} ({len(files)} files)")
        count += 1

    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Package Daanik Agent Skills for supported hosts.")
    parser.add_argument(
        "--platform",
        choices=[*PLATFORMS, "all"],
        default="all",
        help="Host bundle to create (default: all).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "dist",
        help="Output directory (default: repository-root/dist).",
    )
    args = parser.parse_args()

    platforms = PLATFORMS if args.platform == "all" else (args.platform,)
    total = 0
    for platform in platforms:
        total += build(platform, args.output.resolve())
    print(f"Done. Created {total} Skill ZIP(s).")


if __name__ == "__main__":
    main()
