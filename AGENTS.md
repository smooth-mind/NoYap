# NoYap Agent Instructions

This repository uses NoYap. These instructions apply to every coding agent and every task unless a stricter safety or platform rule applies.

## Mission

Complete the user's approved objective with the smallest clear, maintainable change while preserving scope, architecture, technology, security, design, existing behaviour, and project readability.

## Required startup sequence

For every task:

1. Read this file.
2. Read `noyap/PROJECT_STATE.md`.
3. Identify the active phase, active task, mode, blockers, and next permitted action.
4. Read the current phase in `noyap/PHASES.md`.
5. Read only the additional source-of-truth files relevant to the task.
6. Inspect relevant existing code before proposing or making changes.
7. Confirm that the requested work is permitted before editing.

If `noyap/PROJECT_STATE.md` is missing, contradictory, or says implementation is not permitted, stop implementation and repair or clarify governance first.

## Context routing

Always read:

- `AGENTS.md`
- `noyap/PROJECT_STATE.md`
- the active phase in `noyap/PHASES.md`

Read when relevant:

| Task | Additional required context |
|---|---|
| Discovery or requirements | `PROJECT_INPUT.md`, `noyap/PRD.md`, `noyap/SCOPE.md` |
| Feature planning | PRD requirement, scope, architecture, tech stack, relevant design and rules |
| UI work | `noyap/DESIGN.md`, relevant UI documentation and existing components |
| Database work | architecture, tech stack, activated database document, migrations, relevant ADRs |
| Security or identity work | architecture, security model, threat decisions, relevant ADRs |
| Bug fix | relevant requirement, current state, affected module docs, relevant code and tests |
| Dependency change | `noyap/TECH_STACK.md` and an approved change request |
| Architecture change | `noyap/ARCHITECTURE.md` and an accepted ADR or approved change request |
| Handoff or resume | state, memory, active prompt, current phase, relevant recent decision records |

Do not read every file by default. Do not scan the whole repository when targeted inspection is sufficient.

## Source-of-truth priority

When instructions conflict, use this order:

1. Safety, legal, privacy, and platform constraints
2. This `AGENTS.md`
3. Approved NoYap governance documents
4. Accepted ADRs and approved change requests
5. Active phase and task
6. Current user request
7. Agent recommendations

A later user request may intentionally propose a change, but it does not silently modify an approved baseline. Explain the conflict and use the controlled-change process.

## Evidence labels and assumptions

Keep project statements classified as:

- **Confirmed:** explicitly provided by the user or an authoritative project source
- **Proposed:** recommended by an agent but not approved
- **Open:** undecided or unclear
- **Rejected:** explicitly excluded
- **Observed:** directly verified in an existing codebase

Never convert Proposed or Open items into Confirmed requirements without approval.

You may choose a low-risk, reversible implementation detail when it follows existing patterns. Record material choices in the completion report. Stop for decisions that affect scope, architecture, security, data, cost, compatibility, external services, or design identity.

## Protected areas

A normal implementation task must not change the following without an approved change record:

- product goals, requirements, or scope;
- architecture, module boundaries, or dependency direction;
- approved runtime, framework, database, hosting, or major libraries;
- production dependencies;
- authentication, authorization, trust, privacy, or security boundaries;
- sensitive-data collection, storage, transmission, or retention;
- public APIs or persistent schemas in a breaking way;
- visual theme, design system, navigation model, or interaction conventions;
- phase objectives or completion gates.

An agent may identify and propose an improvement. It must not apply it silently.

## Minimal-change protocol

Before editing:

1. State the exact objective internally and identify the governing requirement or bug evidence.
2. Inspect the smallest relevant set of files.
3. Search for existing code, components, utilities, types, patterns, and tests that can be reused.
4. Determine the smallest coherent change.
5. Identify expected files to modify.
6. Check whether the change crosses a protected boundary.

During editing:

- modify only code required for the task;
- preserve existing naming, formatting, architecture, style, theme, and conventions;
- reuse existing abstractions before creating new ones;
- do not perform unrelated cleanup;
- do not rewrite a complete file for a local change;
- do not install a package when a clear local solution already exists;
- do not create speculative extension points or future features;
- do not add placeholder subsystems that were not requested;
- do not suppress errors merely to make checks pass.

A small bug fix that unexpectedly touches more than five files or requires a broad rewrite is a review trigger. Pause and explain why the wider change is necessary unless the current task already approved that breadth.

## Code quality

Prefer code that is:

- clear before clever;
- explicit where behaviour or risk matters;
- consistent with the repository;
- testable;
- readable by another human developer;
- no more abstract than the current use case requires.

Comments should explain decisions, constraints, or non-obvious behaviour. Do not narrate obvious syntax.

## Phase discipline

Work only in the active phase and task.

Normally complete:

1. one task; or
2. one explicitly approved small task batch.

Do not implement future roadmap items because they appear easy or related. Do not begin the next phase until current exit criteria pass and `PROJECT_STATE.md` permits progression.

## Validation

A task is not complete because code was written.

Run the narrowest relevant checks first, then the project-required checks listed in state, rules, phase, or documentation. Never claim a command passed if it was not run successfully.

When validation fails:

- record the exact failure;
- determine whether it was caused by the task;
- fix only task-related failures when permitted;
- do not start the next feature;
- generate a recovery prompt when unresolved work remains.

## Documentation and memory

After a successful task:

- update `noyap/PROJECT_STATE.md`;
- update only documentation affected by the change;
- update `noyap/MEMORY.md` only for durable information that a future agent would otherwise need to rediscover;
- record lasting technical decisions in an ADR;
- keep transient details out of memory;
- preserve completed prompt history.

Do not duplicate the same fact across several files. Link to the source of truth.

## Prompt progression

After implementation and validation:

1. determine the next permitted task from `noyap/PHASES.md`;
2. generate a precise project-specific prompt using the latest state;
3. replace only the `NEXT PROMPT` block in `PROMPTS.md`;
4. update the upcoming roadmap if necessary;
5. archive the completed prompt when useful;
6. stop without implementing the next task.

When a task is blocked or validation fails, the next prompt must be a recovery or decision prompt, not the next feature prompt.

## Human review

Return a concise completion report with:

- objective;
- files changed;
- behaviour implemented;
- tests and checks run with results;
- assumptions or low-risk decisions;
- unresolved issues or blockers;
- protected-area impact;
- documentation and state updates;
- next prompt title;
- whether human approval is required.

For non-technical users, explain impact in simple language before technical detail.

## Mandatory stop conditions

Stop and request a decision or approved change when:

- requirements materially conflict;
- the request is outside approved scope;
- a protected area must change;
- sensitive data or security boundaries are unclear;
- a required source document is missing or unreadable;
- the project state contains an unresolved blocker;
- implementation permission is false;
- required validation cannot be completed;
- the next action cannot be determined without guessing.
