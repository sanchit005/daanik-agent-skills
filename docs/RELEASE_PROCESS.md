# Release and Maintenance Process

**Daanik Everyday AI — Copyright (c) 2026 Daanik Eduventures Private Limited**  
Licensed under the MIT License.

## Versioning
Use semantic versioning for the Skill collection:
- MAJOR: incompatible restructuring or materially changed expected behaviour.
- MINOR: new Skills, new capabilities or meaningful backwards-compatible additions.
- PATCH: corrections, clarity, safety improvements and bug fixes.

Each Skill's YAML `name` should remain stable. Changes to a Skill description can affect automatic selection, so evaluate trigger examples after editing it.

## Before a release
1. Update canonical Skills under `.agents/skills/`.
2. Update identical Skill content under `.claude/skills/` and `.github/skills/`.
3. Review every `agents/openai.yaml` for accurate display names, 25–64 character short descriptions and useful default prompts.
4. Run `python scripts/validate_skills.py`.
5. Run `python scripts/package_skills.py --platform all`.
6. Execute the evaluation scenarios in `evaluations/TEST_CASES.md` on at least two supported model/host combinations where available.
7. Review privacy, safety, copyright, attribution, trademark and platform compatibility.
8. Update CHANGELOG.md and version references.
9. Publish a GitHub release with notes and attach the generated ZIPs if desired.

## Source of truth
The canonical source is `.agents/skills/<skill-name>/`. Platform copies should match the canonical `SKILL.md`. Do not edit the three copies independently; edit the canonical file first, then sync the platform-specific folders.

## Issue triage
Prioritise:
- urgent privacy or safety issues;
- factual and mathematical errors;
- confusing or misleading instructions;
- platform compatibility defects;
- accessibility and translation improvements;
- feature ideas supported by user evidence.

## Rollback
If a release causes unsafe or materially incorrect behaviour, mark the affected version as withdrawn in the release notes, revert or correct the Skill, rerun relevant tests and publish a patch release.
