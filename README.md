# Daanik Everyday AI

**AI that understands everyday problems.**  
**Built by Daanik. Open for everyone.**

Daanik Everyday AI is a free, open collection of practical AI Skills designed to help people with ordinary tasks: planning a day, organising money, shopping wisely, communicating clearly, learning something new, managing home administration, staying safer online and making decisions with greater clarity.

We believe people should not need to become AI experts to benefit from AI. These Skills are written in plain language, explain when and how to use them, show example prompts and set clear boundaries.

> **What is a Skill?** A Skill is a reusable folder containing a `SKILL.md` instruction file and optional supporting resources. A compatible AI assistant can load the Skill when a request matches its purpose. A Skill is not, by itself, a separately hosted chatbot, autonomous agent, API, MCP server or guarantee of a particular model capability.

## Start here

1. Choose the problem you want help with from the catalogue below.
2. Open that Skill's `SKILL.md` and read its purpose, examples and limitations.
3. Install the Skill in a supported AI environment using the instructions in [Getting Started](docs/GETTING_STARTED.md).
4. Ask naturally. Use the example starter prompt or describe your situation in your own words.
5. Check important facts and keep control of consequential decisions.

## The eight everyday Skills

| Skill | What it helps with | Example request |
|---|---|---|
| [Daily Planner & Habit Builder](.agents/skills/daily-planner/SKILL.md) | Plan tasks, routines and priorities without overfilling the day. | "Help me plan today around these commitments." |
| [Everyday Money Companion](.agents/skills/money-companion/SKILL.md) | Organise a simple budget, bills, savings goals and everyday financial concepts. | "Help me understand where my monthly income goes." |
| [Smart Shopping & Consumer Advocate](.agents/skills/smart-shopping-advocate/SKILL.md) | Compare options, total ownership costs and common sales-pressure signals. | "Help me decide whether this offer is worth it." |
| [Everyday Communication Coach](.agents/skills/communication-coach/SKILL.md) | Draft clear messages, prepare for difficult conversations and set respectful boundaries. | "Help me write a firm but respectful reminder." |
| [Everyday Learning Coach](.agents/skills/learning-coach/SKILL.md) | Learn a topic in small steps using examples, practice and feedback. | "Teach me this topic and check my understanding." |
| [Home & Life Admin Organizer](.agents/skills/home-life-admin/SKILL.md) | Organise household chores, lists, errands and recurring administration. | "Help me organise this week's household tasks." |
| [Digital Safety & Scam Checker](.agents/skills/digital-safety-checker/SKILL.md) | Recognise suspicious signals and verify safely. | "Help me assess this message. I have removed my personal details." |
| [Decision Clarity Coach](.agents/skills/decision-clarity-coach/SKILL.md) | Compare options, understand trade-offs and reduce decision confusion. | "Help me compare these choices fairly." |

## Where the files live

The same core Skills are provided in common project-level locations:

- `.agents/skills/<skill-name>/` — portable Agent Skills layout; used by Codex and supported by other compatible agents.
- `.claude/skills/<skill-name>/` — Claude Code project Skills.
- `.github/skills/<skill-name>/` — GitHub Copilot project Skills.

The canonical source of each Skill is the matching folder under `.agents/skills/`. Platform copies are kept in sync when releases are prepared. OpenAI-specific UI metadata is included in `agents/openai.yaml` inside each canonical Skill folder.

## Installation

See **[docs/GETTING_STARTED.md](docs/GETTING_STARTED.md)** for step-by-step instructions and platform-specific requirements.

### Quick install: GitHub Copilot

In a repository where you want to use the Skills, copy this repository's `.github/skills/` folder into the root of that project. Copilot supports project Skills in `.github/skills`, `.claude/skills` and `.agents/skills`. Start or reload your Copilot session and ask for the task in ordinary language. See the [official Copilot Skill guide](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

### Quick install: Claude Code

Copy the desired folder(s) from `.claude/skills/` into the root of your own project under `.claude/skills/`. For personal use across projects, copy them to `~/.claude/skills/`. Start a new Claude Code session and describe the task.

### Quick install: Codex

Copy the desired folder(s) from `.agents/skills/` into the root of your project under `.agents/skills/`. For personal use, place them under `~/.agents/skills/`. Refresh or restart the session if the Skill is not detected. Codex also supports explicit Skill invocation using the Skill name in supported interfaces.

### Claude.ai and ChatGPT web upload

Claude.ai and ChatGPT Skills upload workflows use a ZIP containing a Skill folder. The repository's `scripts/package_skills.py` creates one ZIP per Skill from the canonical `.agents/skills/` folder:

```bash
python scripts/package_skills.py --platform claude
python scripts/package_skills.py --platform openai
```

Then upload the selected ZIP using the host's Skills interface. Availability varies by account, plan, workspace settings and product surface. For current platform instructions, consult [Claude Skills help](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

## Human-centred design

Every Skill uses the same product principles:

1. **Empathy:** Understand the real task before prescribing a solution.
2. **Simplicity:** Explain the subject in language a non-specialist can use.
3. **Behavioural awareness:** Recognise cognitive load, habits, consumer bias, social pressure and psychological reactance.
4. **Ethical influence:** Support informed choice; never covertly manipulate a person.
5. **Action orientation:** Make the next useful action concrete and proportionate.

The Skills may use behavioural-science ideas such as COM-B, EAST, implementation intentions, cognitive-load reduction, retrieval practice and decision-bias checks as design aids. They do not claim to diagnose people or reliably read hidden intentions.

### Reverse psychology and NLP

We use knowledge of psychological reactance and common persuasion tactics primarily to help users recognise pressure and retain meaningful choice. We do **not** instruct AI assistants to deceive, provoke, shame, manufacture scarcity, exploit personal vulnerabilities or use reverse psychology to force compliance.

NLP-inspired practices are limited to transparent communication techniques such as paraphrasing, reflecting a person's stated language and reframing. The repository does not claim NLP can read minds, detect lies or control a person's subconscious.

Read [Behavioural Design & Ethics](docs/BEHAVIOURAL_DESIGN_AND_ETHICS.md).

## Quality checks and evaluation

The repository includes 32 human-readable test scenarios (four per Skill), a five-dimension scoring rubric and a structural validation script.

```bash
python scripts/validate_skills.py
python scripts/package_skills.py --platform all
```

The GitHub Actions workflow validates the Skill structure and builds platform ZIP bundles on pushes and pull requests. Model-quality evaluation still requires testing on the target AI host; a passing structural check is not proof that every model will always behave correctly.

See [Evaluation Guide](evaluations/README.md), [Test Cases](evaluations/TEST_CASES.md), [Release Process](docs/RELEASE_PROCESS.md), [Copyright and Brand Notes](docs/COPYRIGHT_AND_BRAND.md) and [Changelog](CHANGELOG.md).

## Safety and important limits

- The Money Companion provides general education and budgeting organisation—not personalised investment, securities, tax, insurance, lending or legal advice.
- The Digital Safety Checker identifies warning signs; it cannot authenticate every sender, link, caller or offer.
- Never share passwords, PINs, OTPs, CVV, recovery codes or full payment credentials with an AI assistant.
- The Skills do not independently book, buy, pay, message, submit forms or change accounts. External actions require separately authorised tools and confirmation.
- Verify current, legal, medical, financial, safety and official-process information with reliable sources or qualified professionals.
- Do not include private customer data, confidential client documents, secrets or API keys in examples or public issues.

## SWOT, PESTLE and Porter's Five Forces

The project includes a qualitative market and product assessment for each of the eight Skills:

- [Full strategy analysis](docs/STRATEGIC_ANALYSIS.md)
- [Evaluation prompts and quality rubric](evaluations/README.md)
- [Getting Started](docs/GETTING_STARTED.md)

The strategy report is a set of launch hypotheses, not audited market research. Validate with user interviews, observed tests and current competitor research before making investment or pricing decisions.

## Licence and reuse

The Skills in this repository are released under the **MIT License**. You may use, copy, modify, merge, publish, distribute, sublicense and sell copies, subject to retaining the required copyright and licence notices. Read the complete [LICENSE](LICENSE).

**Copyright (c) 2026 Daanik Eduventures Private Limited.**

The MIT License does not grant permission to use Daanik's name, logo or other trademarks to imply endorsement or official affiliation. See [TRADEMARKS.md](TRADEMARKS.md).

The project is open source. That means people and businesses may commercially reuse and modify the licensed Skills; Daanik does not claim exclusivity over third-party modified versions.

## Contributing

Ideas, corrections, translations, accessibility improvements and evaluation cases are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Do not submit private user information or copyrighted materials you do not have permission to share.

## Maintained by

**Daanik Eduventures Private Limited**  
Daanik — Commitment to Share  
Website: https://www.daanik.com

For security concerns, see [SECURITY.md](SECURITY.md). For project conduct, see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

*Daanik Everyday AI is an independent open-source project. Claude, ChatGPT, OpenAI, GitHub and Copilot are third-party product names and trademarks of their respective owners. This project is not affiliated with or endorsed by those providers.*
