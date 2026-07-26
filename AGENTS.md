# NoYap Agent Instructions

This repository uses NoYap. These instructions apply to every coding agent and every task unless a stricter safety, legal, privacy, or platform rule applies.

## Mission

Complete the user’s approved objective with the smallest clear and maintainable change while preserving project scope, architecture, technology, security, design, existing behaviour, and readability.

NoYap controls the agent, not the user. It should reduce unnecessary work, assumptions, token use, and human review without creating avoidable process overhead.

## Required startup sequence

For every task:

1. Read this file.
2. Read `noyap/PROJECT_STATE.md`.
3. Identify the active phase, active task, execution mode, blockers, implementation permission, and next permitted action.
4. Read the active phase in `noyap/PHASES.md`.
5. Read only the additional source-of-truth files relevant to the task.
6. Inspect relevant existing code before proposing or making changes.
7. Confirm that the requested work is permitted before editing.
8. Determine the task or approved batch size allowed by the active execution mode.

If `noyap/PROJECT_STATE.md` is missing, contradictory, invalid, or says implementation is not permitted, stop implementation and repair or clarify governance first.

## Context routing

Always read:

* `AGENTS.md`
* `noyap/PROJECT_STATE.md`
* the active phase in `noyap/PHASES.md`

Read when relevant:

| Task                      | Additional required context                                                          |
| ------------------------- | ------------------------------------------------------------------------------------ |
| Discovery or requirements | `PROJECT_INPUT.md`, `noyap/PRD.md`, `noyap/SCOPE.md`                                 |
| Feature planning          | Relevant PRD requirement, scope, architecture, tech stack, design, and rules         |
| UI work                   | `noyap/DESIGN.md`, relevant UI documentation, and existing components                |
| Database work             | Architecture, tech stack, activated database document, migrations, and relevant ADRs |
| Security or identity work | Architecture, security model, threat decisions, and relevant ADRs                    |
| Bug fix                   | Relevant requirement, current state, affected module documentation, code, and tests  |
| Dependency change         | `noyap/TECH_STACK.md` and an approved change request                                 |
| Architecture change       | `noyap/ARCHITECTURE.md` and an accepted ADR or approved change request               |
| Handoff or resume         | State, memory, active prompt, current phase, and relevant recent decision records    |

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

`noyap/PROJECT_STATE.md` is the only source of truth for:

* current phase;
* current task;
* execution mode;
* blockers;
* implementation permission;
* last completed task;
* next permitted action.

`PROMPTS.md` stores the executable NEXT PROMPT and prompt roadmap. It must not independently duplicate canonical project-state information.

## Evidence labels and assumptions

Keep project statements classified as:

* **Confirmed:** explicitly provided by the user or an authoritative project source
* **Proposed:** recommended by an agent but not approved
* **Open:** undecided or unclear
* **Rejected:** explicitly excluded
* **Observed:** directly verified in an existing codebase

Never convert Proposed or Open items into Confirmed requirements without approval.

You may choose a low-risk, reversible implementation detail when it follows existing patterns. Record material choices in the completion report.

Stop for decisions that affect:

* scope;
* architecture;
* security;
* sensitive data;
* cost;
* compatibility;
* external services;
* persistent schemas;
* public APIs;
* design identity.

## Protected areas

A normal implementation task must not change the following without an approved change record:

* product goals, requirements, or scope;
* architecture, module boundaries, or dependency direction;
* approved runtime, framework, database, hosting, or major libraries;
* production dependencies;
* authentication, authorization, trust, privacy, or security boundaries;
* sensitive-data collection, storage, transmission, or retention;
* public APIs or persistent schemas in a breaking way;
* visual theme, design system, navigation model, or interaction conventions;
* phase objectives or completion gates.

An agent may identify and propose an improvement. It must not apply it silently.

Execution mode never grants permission to cross a protected boundary.

## Minimal-change protocol

Before editing:

1. Identify the exact objective and its governing requirement or verified bug evidence.
2. Inspect the smallest relevant set of files.
3. Search for existing code, components, utilities, types, patterns, and tests that can be reused.
4. Determine the smallest coherent change.
5. Identify the expected files to modify.
6. Check whether the change crosses a protected boundary.
7. Confirm that the task or batch is explicitly authorized by the current prompt and active mode.

During editing:

* modify only code required for the approved task or batch;
* preserve existing naming, formatting, architecture, style, theme, and conventions;
* reuse existing abstractions before creating new ones;
* do not perform unrelated cleanup;
* do not rewrite a complete file for a local change;
* do not install a package when a clear local solution already exists;
* do not create speculative extension points or future features;
* do not add placeholder subsystems that were not requested;
* do not suppress errors merely to make checks pass;
* do not continue into an unlisted task.

A small bug fix that unexpectedly touches more than five files or requires a broad rewrite is a review trigger. Pause and explain why the wider change is necessary unless the current task already approved that breadth.

The five-file threshold is a warning signal, not a hard prohibition. A coherent fix may legitimately require more files when tests, types, migrations, and documentation are included.

## Code quality

Prefer code that is:

* clear before clever;
* explicit where behaviour or risk matters;
* consistent with the repository;
* testable;
* readable by another human developer;
* no more abstract than the current use case requires.

Comments should explain decisions, constraints, or non-obvious behaviour. Do not narrate obvious syntax.

## Phase discipline

Work only in the active phase and on tasks explicitly permitted by the active phase and NEXT PROMPT.

Complete only the execution unit permitted by the active mode.

Do not:

* infer additional tasks from nearby roadmap items;
* combine tasks merely because they appear related;
* implement future roadmap items because they appear easy;
* continue into an unlisted task;
* begin the next phase before current exit criteria pass;
* cross a phase boundary unless `PROJECT_STATE.md` explicitly permits progression.

A task batch must be explicitly listed in the active phase or the current NEXT PROMPT. Adjacent tasks are not automatically a batch.

## Mode-based execution

`mode` in `noyap/PROJECT_STATE.md` controls the maximum amount of already approved work that may be completed in one agent run.

Mode changes batching frequency only. It never changes:

* protected areas;
* approval requirements;
* mandatory stop conditions;
* validation requirements;
* phase boundaries;
* scope;
* architecture;
* security restrictions;
* dependency restrictions.

### Guided mode

Complete exactly one approved task.

Then:

1. run required validation;
2. update affected documentation and state;
3. generate the next prompt;
4. stop and report.

Use guided mode when close human review is preferred or the project is still uncertain.

### Balanced mode

Complete either:

1. one approved task; or
2. one explicitly approved small batch of closely related tasks.

A balanced batch should normally:

* share one objective;
* affect the same feature or module;
* require the same context;
* be easy to validate together;
* remain easy for a human to review.

Then:

1. validate the task or complete batch;
2. update affected documentation and state;
3. generate the next prompt;
4. stop and report.

Balanced mode is the recommended default for most projects.

### Autonomous mode

Complete all tasks explicitly listed in the current approved batch without requiring a user round trip between those tasks.

Every task in the batch must be named or clearly enumerated in:

* the active phase; or
* the current NEXT PROMPT.

Do not infer an autonomous batch from an entire phase, roadmap section, or neighbouring tasks.

For each task in the batch:

1. complete only the listed work;
2. run the narrow validation needed before depending on that result;
3. stop immediately if the task fails or reveals a blocker.

After the complete batch:

1. run all required batch and project validation;
2. update affected documentation;
3. update `noyap/PROJECT_STATE.md`;
4. generate the next prompt;
5. stop and report.

### Mode safety rule

Mode never creates permission to perform additional work.

In every mode, stop immediately when:

* a mandatory stop condition occurs;
* validation fails and cannot be resolved within the approved task;
* a protected boundary would be crossed;
* a blocker appears;
* required information is missing;
* a task outside the approved execution unit becomes necessary;
* the current phase exit boundary is reached.

## Validation

A task is not complete merely because code was written.

Run the narrowest relevant checks first, then the project-required checks listed in state, rules, the active phase, or project documentation.

Never claim a command passed if it was not run successfully.

For a batch:

* validate each task sufficiently before starting work that depends on it;
* run complete batch validation before marking the batch complete;
* do not hide one failed task behind successful results from other tasks.

When validation fails:

* record the exact failure;
* determine whether it was caused by the current task;
* fix only task-related failures when permitted;
* stop the remaining batch when continuing could compound the failure;
* do not start the next feature;
* generate a recovery prompt when unresolved work remains.

## Documentation and memory

After a successful task or approved batch:

* update `noyap/PROJECT_STATE.md`;
* update only documentation affected by the work;
* update `noyap/MEMORY.md` only for durable information that a future agent would otherwise need to rediscover;
* record lasting technical decisions in an ADR;
* keep transient details out of memory;
* preserve completed prompt history;
* update `last_updated` in governed documents that were materially changed.

Do not duplicate the same fact across several files. Link to the canonical source of truth.

For a batch, record which tasks were completed and which, if any, remain incomplete.

## Prompt progression

After implementation and successful validation:

1. determine the next permitted task from `noyap/PHASES.md`;
2. consider the active mode when selecting the next execution unit;
3. generate a precise, project-specific prompt using the latest validated state;
4. explicitly list every task when the next prompt authorizes a batch;
5. replace only the NEXT PROMPT block in `PROMPTS.md`;
6. update the upcoming roadmap only when necessary;
7. archive the completed prompt when useful;
8. stop without implementing the next prompt.

Every generated NEXT PROMPT must state:

* the active mode;
* the exact objective;
* the task or explicitly enumerated batch;
* the relevant files to read;
* protected boundaries;
* required validation;
* required state and documentation updates;
* mandatory stop conditions.

When a task is blocked or validation fails, the next prompt must be a recovery or decision prompt, not the next feature prompt.

Autonomous mode does not permit automatic phase progression. The agent must stop at the end of the approved batch or active phase boundary.

## Human review

Return a concise completion report containing:

* objective;
* active mode;
* task or batch completed;
* files changed;
* behaviour implemented;
* tests and checks run with results;
* assumptions or low-risk decisions;
* unresolved issues or blockers;
* protected-area impact;
* documentation and state updates;
* next prompt title;
* whether human approval is required.

For non-technical users, explain the practical impact in simple language before technical details.

In autonomous mode, summarize the batch as a whole and clearly identify the result of each included task.

## Mandatory stop conditions

Stop and request a decision, clarification, or approved change when:

* requirements materially conflict;
* the request is outside approved scope;
* a protected area must change;
* sensitive data or security boundaries are unclear;
* a required source document is missing or unreadable;
* the project state contains an unresolved blocker;
* implementation permission is false;
* required validation cannot be completed;
* the current task or batch is not explicitly authorized;
* continuing would require an unlisted task;
* the active mode and current prompt conflict;
* the next action cannot be determined without guessing;
* the current phase boundary has been reached.

When stopping, explain:

1. what caused the stop;
2. what work, if any, was completed safely;
3. what decision or approval is required;
4. what the next safe prompt should do.
