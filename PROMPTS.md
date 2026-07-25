---
document: prompts
status: active
mode: bootstrap
last_updated: YYYY-MM-DD
---

# NoYap Project Prompts

## Instructions for the user

Copy only the prompt inside the **NEXT PROMPT** block. Give it to the coding agent that has access to this repository.

After the agent finishes:

1. read its short review summary;
2. approve only decisions that require approval;
3. confirm that validation passed;
4. return here and copy the newly generated next prompt.

Do not skip ahead using roadmap titles. Roadmap entries are not executable prompts.

## Current progress

- Current phase: Phase 0
- Current task: Project discovery
- Last completed task: None
- Next prompt status: Ready
- Human approval required before execution: No

## NEXT PROMPT

<!-- NEXT_PROMPT_START -->
```text
You are continuing a project that uses NoYap.

Read AGENTS.md, PROJECT_INPUT.md, noyap/PROJECT_STATE.md, and the Phase 0 section
of noyap/PHASES.md. Do not write application code.

Determine whether PROJECT_INPUT.md contains a rough idea, supplied documents,
an existing codebase, or a mixture. Continue project discovery using only
supported facts. Ask one short, concrete question at a time when an answer
materially affects requirements, scope, architecture, security, data, cost,
or design. Keep recommendations Proposed until approved and keep unresolved
matters Open.

When discovery is sufficiently complete:
1. update PROJECT_INPUT.md;
2. provide a concise human-review summary;
3. update noyap/PROJECT_STATE.md;
4. generate the next prompt for drafting noyap/PRD.md;
5. replace this NEXT PROMPT block with that prompt;
6. stop without drafting the PRD or writing code.
```
<!-- NEXT_PROMPT_END -->

## Planned prompt roadmap

These are high-level checkpoints. Detailed executable prompts are generated just in time.

1. Complete project discovery
2. Draft PRD from confirmed input
3. Review and approve PRD
4. Draft and approve scope
5. Draft architecture and tech stack
6. Draft design rules when applicable
7. Finalize engineering rules
8. Build the full phase roadmap
9. Review and approve the project baseline
10. Generate detailed prompts for the current phase
11. Implement and validate one task or approved batch
12. Review the phase and progress to the next approved phase
13. Complete release, handoff, and final documentation

## Recovery prompt: resume safely

```text
Resume this NoYap project safely.

Read AGENTS.md, noyap/PROJECT_STATE.md, the active section of noyap/PHASES.md,
noyap/MEMORY.md, and the NEXT PROMPT block in PROMPTS.md. Inspect git status and
relevant recent changes. Do not modify code until you can state the current
phase, current task, last validated result, blockers, protected boundaries,
and exact next permitted action. Resolve contradictions in project state
before implementation. Then execute only the current NEXT PROMPT.
```

## Recovery prompt: fix a bug with minimal change

```text
Handle this bug under NoYap governance.

First read AGENTS.md and noyap/PROJECT_STATE.md. Locate the relevant approved
requirement, existing behaviour, code, tests, and documentation. Reproduce or
establish evidence for the bug before editing. Propose the smallest coherent
fix and identify the expected files to change. Do not change architecture,
dependencies, scope, design system, unrelated code, or future features.

Implement only the fix, run targeted validation, update affected documentation
and project state, and generate the next prompt. If the fix requires a
protected-area change, stop and prepare a change request instead.
```

## Recovery prompt: propose a new or changed feature

```text
Evaluate this requested feature under NoYap governance without implementing it.

Read AGENTS.md, noyap/PROJECT_STATE.md, noyap/PRD.md, noyap/SCOPE.md,
noyap/ARCHITECTURE.md, noyap/TECH_STACK.md, and relevant design and phase
sections. Determine whether the request is already approved, in scope but not
planned, or outside the baseline. Explain the smallest safe option and the
impact on requirements, architecture, data, security, dependencies, design,
testing, phases, and documentation. Create a proposed change record when a
baseline change is required. Do not write implementation code.
```

## Completed prompt archive

Move long completed prompts to `noyap/prompts/completed/`. Keep only a short index here.

| Prompt | Result | Archive | Date |
|---|---|---|---|
| | | | |
