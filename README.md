# NoYap

**Keep coding agents useful, in scope, and easy to supervise.**

NoYap is a lightweight, agent-neutral governance and prompt system for AI-assisted software projects. It helps a person turn a rough idea, SRS, or existing codebase into a controlled project plan, then guides implementation one approved step at a time.

NoYap is designed for people who do not know how to manage coding agents as well as developers who want stronger scope, architecture, design, dependency, memory, and handoff control.

> Plan the full journey early. Generate the next executable prompt using the latest project state.

## What problem does NoYap solve?

Coding agents can be helpful, but they may also:

- assume missing requirements;
- add features that were never requested;
- change architecture or dependencies without permission;
- redesign pages while fixing a small issue;
- rewrite working code instead of making a focused change;
- forget earlier decisions when the agent or conversation changes;
- produce large, difficult-to-review changes;
- move into future phases before the current work is validated.

NoYap gives the agent a small set of project-owned source-of-truth files and a strict workflow:

```text
Understand -> Clarify -> Document -> Review -> Approve
-> Plan -> Implement -> Validate -> Record -> Generate next prompt
```

## Core principles

1. **No silent assumptions** for requirements, scope, architecture, security, data, or design.
2. **No unauthorized drift** in architecture, technology, dependencies, database, scope, or visual system.
3. **Smallest clear change** instead of unnecessary abstractions or broad refactors.
4. **One task or approved task batch at a time.**
5. **Read only relevant context** rather than loading every project document for every task.
6. **A task is not complete until validated.**
7. **Durable memory, not conversation history.**
8. **The next prompt is generated from the real current state.**

## Repository map

| File or folder | Purpose | Updated when |
|---|---|---|
| `AGENTS.md` | Main instructions and restrictions for coding agents | Rarely |
| `PROJECT_INPUT.md` | Original idea, SRS findings, existing-project facts, and open questions | During discovery |
| `PROMPTS.md` | Beginner-friendly copy-paste prompts, current next prompt, and roadmap | After each validated task |
| `noyap/PRD.md` | Approved product requirements and acceptance criteria | Requirements change |
| `noyap/SCOPE.md` | In-scope, out-of-scope, future, and rejected work | Scope change |
| `noyap/ARCHITECTURE.md` | Modules, boundaries, data flow, and invariants | Approved architecture change |
| `noyap/TECH_STACK.md` | Approved technologies, versions, and dependency policy | Approved stack change |
| `noyap/DESIGN.md` | UI theme, style, components, and experience rules | Approved design change |
| `noyap/RULES.md` | Project-specific engineering and review rules | Approved rule change |
| `noyap/PHASES.md` | Full roadmap, phase gates, and task sequence | Planning change |
| `noyap/PROJECT_STATE.md` | Current phase, task, blockers, validation, and next action | Every task |
| `noyap/MEMORY.md` | Small set of durable facts future agents need | Only when durable knowledge changes |
| `noyap/decisions/` | Architecture Decision Records | Important decision |
| `noyap/changes/` | Proposed and approved controlled changes | Baseline change |
| `docs/` | Human-facing implementation documentation | Relevant code change |
| `scripts/noyap.py` | Zero-dependency validator and prompt helper | NoYap maintenance |

Optional files are available in `noyap/optional/`. Activate only the ones the project actually needs.

## Start in three steps

### 1. Create your project from NoYap

After this repository is published, the easiest method will be GitHub's **Use this template** button.

You can also clone it:

```bash
git clone https://github.com/smooth-mind/NoYap.git my-project
cd my-project
```

To make it a new project with fresh Git history:

```bash
rm -rf .git
git init
git add .
git commit -m "Initialize project with NoYap"
```

On Windows PowerShell, remove `.git` with:

```powershell
Remove-Item -Recurse -Force .git
git init
git add .
git commit -m "Initialize project with NoYap"
```

### 2. Put your information in `PROJECT_INPUT.md`

Use whatever you already have:

- a rough idea in ordinary language;
- an SRS or requirements document;
- notes, sketches, workflows, or screenshots;
- an existing codebase;
- a mixture of these.

For files such as PDFs or DOCX documents, place them in a local `inputs/` folder or attach them to the coding-agent session. Do not copy secrets, passwords, private keys, or production credentials into project documents.

### 3. Copy one starting prompt

Choose only one route below.

<details>
<summary><strong>Starter A: I have a rough idea</strong></summary>

```text
You are starting a project that uses the NoYap governance workflow.

Read README.md, AGENTS.md, PROJECT_INPUT.md, and noyap/PROJECT_STATE.md.
Do not write application code yet.

My current source is a rough idea. Help me make it complete without silently
inventing requirements. Ask one short, concrete question at a time only when
an answer materially affects the product, scope, architecture, security,
data, cost, or design. Record each answer in PROJECT_INPUT.md and label it as
Confirmed. Keep agent recommendations labelled Proposed until I approve them.
Keep unresolved matters labelled Open.

When the idea is sufficiently clear:
1. summarize the confirmed project in simple language;
2. list important remaining open decisions;
3. update noyap/PROJECT_STATE.md;
4. place the exact next copy-paste prompt in PROMPTS.md;
5. stop without generating the PRD or writing code.
```

</details>

<details>
<summary><strong>Starter B: I have an SRS or related documents</strong></summary>

```text
You are starting a project that uses the NoYap governance workflow.

Read README.md, AGENTS.md, PROJECT_INPUT.md, noyap/PROJECT_STATE.md, and every
source document I explicitly provide. Do not write application code yet.

Extract only information supported by the supplied documents. Preserve source
traceability. Mark contradictions, missing decisions, and unclear terms. Do
not convert your recommendations into requirements. Ask one short, concrete
question at a time only when the answer materially affects the project.

Update PROJECT_INPUT.md using these labels:
- Confirmed: directly stated by me or the source documents;
- Proposed: your recommendation, not yet approved;
- Open: still undecided;
- Rejected: explicitly excluded.

When extraction and clarification are complete:
1. provide a short human-review summary;
2. update noyap/PROJECT_STATE.md;
3. place the exact next copy-paste prompt in PROMPTS.md;
4. stop without generating the PRD or writing code.
```

</details>

<details>
<summary><strong>Starter C: I have an existing codebase</strong></summary>

```text
You are onboarding an existing codebase into the NoYap governance workflow.

Read README.md, AGENTS.md, PROJECT_INPUT.md, and noyap/PROJECT_STATE.md. Inspect
the repository in read-only discovery mode. Do not change source code,
dependencies, configuration, schemas, architecture, formatting, or design.

Document what actually exists: project purpose, stack, versions, commands,
folder structure, modules, data flow, external services, database use, tests,
security boundaries, coding patterns, and visual patterns. Distinguish facts
observed in code from your recommendations. Record uncertainties instead of
assuming.

Update PROJECT_INPUT.md, give me a concise discovery summary, update
noyap/PROJECT_STATE.md, generate the exact next prompt in PROMPTS.md, and stop.
```

</details>

## What happens next?

NoYap guides the agent through the governance files one by one:

```text
Project input
-> PRD
-> Scope
-> Architecture and tech stack
-> Design, when applicable
-> Rules
-> Phases
-> Baseline review and approval
-> Detailed current-phase prompts
-> Implementation
```

The complete phase roadmap is planned after the baseline documents are approved. However, detailed code prompts are generated progressively. This prevents future prompts from becoming stale.

## How to use `PROMPTS.md`

For a beginner, the normal workflow is:

1. Open `PROMPTS.md`.
2. Copy only the section marked **NEXT PROMPT**.
3. Paste it into the coding agent working in the repository.
4. Let the agent complete only that task or approved task batch.
5. Review the short completion report.
6. Confirm any required approval.
7. Open `PROMPTS.md` again and copy the newly generated next prompt.

The agent must not implement the next task during the same run unless the active phase explicitly allows a safe task batch.

## Guided, balanced, and autonomous modes

Set the mode in `noyap/PROJECT_STATE.md`.

| Mode | Behaviour | Best for |
|---|---|---|
| `guided` | One task per prompt, frequent simple reviews | Non-technical users and new projects |
| `balanced` | Small related tasks may be grouped, important gates remain | Default for most projects |
| `autonomous` | Several approved tasks may run, but phase and risk gates still stop execution | Experienced users and stable projects |

No mode may bypass approval for scope, architecture, security, sensitive data, database technology, major dependency, or design-system changes.

## Low overhead by design

NoYap avoids bureaucracy through these rules:

- only the core files are required;
- optional documents are activated only when relevant;
- the agent reads documents based on the task type;
- small reversible implementation details do not require approval;
- only important baseline changes use formal change requests;
- `MEMORY.md` stores durable facts, not a diary;
- completed prompts are archived outside the main `PROMPTS.md`;
- small fixes should produce small diffs.

## Validate the NoYap state

NoYap includes a Python script that uses only the standard library:

```bash
python scripts/noyap.py validate
python scripts/noyap.py status
python scripts/noyap.py next
```

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

## Controlled changes

After the project baseline is approved, a normal feature or bug-fix prompt must not directly change:

- approved scope;
- architecture and module boundaries;
- production technology choices;
- database technology or schema strategy;
- security boundaries;
- design system and visual identity;
- major public interfaces;
- phase goals.

Use `noyap/templates/CHANGE_REQUEST.template.md` for a controlled change. Use an ADR when a technical decision has lasting consequences.

## Agent compatibility

`AGENTS.md` is the main agent-neutral instruction file. Short adapter files route Claude Code and GitHub Copilot to the same source of truth, so project rules are not duplicated.

Agent products evolve. Keep adapters short and verify tool-specific discovery behaviour before claiming full compatibility with a new tool.

## Project status

This archive is **NoYap v0.1.1**, an initial working template and validator. The next sensible milestone is to test it on one small website and one existing codebase, then measure:

- unrequested changes;
- files and lines changed per task;
- architecture or dependency drift;
- human corrections required;
- prompt and context size;
- successful agent handoffs.

## License

MIT. See `LICENSE`.
