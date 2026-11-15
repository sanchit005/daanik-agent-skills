# Getting Started with Daanik Everyday AI Skills

This guide is for people who have never installed an Agent Skill before. You do not need to know programming to use a Skill in a supported AI interface, although copying Skills into a code project requires basic file or Git access.

## Step 1 — Choose the task

Start at the repository README and choose one Skill. Read its `SKILL.md` before installing it. Each Skill explains what it does, when to use it, a starter prompt, workflow, examples and safety boundaries.

## Step 2 — Choose where you want to use it

### Claude.ai (web or desktop)
1. Enable **Code execution and file creation** in Settings → Capabilities if it is not already enabled.
2. Open Customize → Skills.
3. Select + → Create skill → Upload a skill.
4. Upload a ZIP containing the Skill folder with `SKILL.md` at its top level.
5. Enable the Skill in your Skills list.
6. Ask Claude a natural-language request matching the Skill's purpose.

To create upload ZIPs from this repository, run:

```bash
python scripts/package_skills.py --platform claude
```

Upload one ZIP per Skill. The official Claude guide is at https://support.claude.com/en/articles/12512180-use-skills-in-claude.

### Claude Code
For one project, copy the relevant folder from `.claude/skills/` into your project's `.claude/skills/` directory.

For personal use across projects, copy the folder into `~/.claude/skills/`.

Example:

```bash
mkdir -p .claude/skills
cp -R /path/to/daanik-agent-skills/.claude/skills/daily-planner .claude/skills/
```

Start a new Claude Code session and ask for a task, for example: "Plan my day around these commitments." Use `/skills` if supported by your version to inspect discovered Skills. Claude documentation: https://docs.anthropic.com/en/docs/claude-code/skills.

### OpenAI Codex
For one project, copy a Skill folder from `.agents/skills/` into the project's `.agents/skills/` directory.

For personal use, place it under `~/.agents/skills/`.

Example:

```bash
mkdir -p .agents/skills
cp -R /path/to/daanik-agent-skills/.agents/skills/daily-planner .agents/skills/
```

Refresh or restart Codex if it does not detect the new Skill. In supported Codex interfaces, inspect the Skills list or invoke it explicitly by its Skill name. Each canonical folder includes `agents/openai.yaml` metadata for the OpenAI interface where supported.

OpenAI product availability varies. ChatGPT's Skills upload interface is currently documented for eligible Business, Enterprise, Healthcare and Edu workspaces, subject to workspace settings. Do not assume the upload interface exists on every individual ChatGPT plan. See https://help.openai.com/en/articles/20001066-skills-in-chatgpt.

### GitHub Copilot
For a repository, copy the Skill folder from `.github/skills/` into the root of your project under the same path. GitHub Copilot also supports project Skills in `.agents/skills/` and `.claude/skills/`.

For personal use, supported locations include `~/.copilot/skills/` and `~/.agents/skills/`, depending on the Copilot surface.

Start or reload your Copilot session, then describe the task in ordinary language. The agent selects Skills based on the folder's description. See https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills.

## Step 3 — Try a starter prompt

- Planner: "Help me plan today. These are my tasks and fixed commitments..."
- Money: "Help me organise a monthly budget using these rounded figures..."
- Shopping: "Help me compare these products against my needs and budget..."
- Communication: "Help me write a clear and respectful message about..."
- Learning: "Teach me this topic step by step and check my understanding..."
- Home admin: "Turn this household task into a simple checklist..."
- Digital safety: "Review this suspicious message. I have removed all personal information..."
- Decision clarity: "Help me compare these options using the priorities that matter to me..."

You do not need to use the exact prompts. Describe your own problem naturally.

## Step 4 — Review the result

A Skill guides the assistant; it does not guarantee that every answer is correct. Check calculations, live facts, important dates, official requirements and consequential recommendations. Use qualified professionals for high-stakes medical, legal, tax, investment or safety decisions.

## Common troubleshooting

**The Skill is not detected:** confirm the folder is in the correct project or personal path, that the folder contains a file named exactly `SKILL.md`, and that the YAML frontmatter has a valid `name` and `description`. Restart or reload the host app.

**The Skill is not selected automatically:** try a more direct prompt that matches the description. The Skill's description is the trigger signal.

**The upload ZIP is rejected:** make sure the ZIP contains one Skill folder at its root, and that `SKILL.md` is inside that folder rather than buried in an extra nested directory.

**I cannot see Skills in ChatGPT:** access depends on plan, workspace and product availability. Use Codex's local `.agents/skills/` path where available.

## Safety reminder
Read any third-party Skill before enabling it. Do not share account credentials or private customer data with an AI assistant. See the repository's SECURITY.md and the safety section in each Skill.
