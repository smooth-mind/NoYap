# NoYap governance files

This folder contains the project-owned source of truth.

## Core files

- `PRD.md`: what the product must achieve.
- `SCOPE.md`: what is included, excluded, deferred, and rejected.
- `ARCHITECTURE.md`: how the system is divided and which boundaries must remain stable.
- `TECH_STACK.md`: approved technology and dependency choices.
- `DESIGN.md`: visual and interaction rules when the project has a user interface.
- `RULES.md`: project-specific development, testing, review, and documentation rules.
- `PHASES.md`: the complete high-level journey and current implementation sequence.
- `PROJECT_STATE.md`: small current-state dashboard, updated after every task.
- `MEMORY.md`: durable facts that future agents would otherwise need to rediscover.

## Supporting folders

- `decisions/`: lasting technical decisions using ADRs.
- `changes/`: proposed, approved, and completed baseline changes.
- `prompts/completed/`: archived detailed prompts.
- `templates/`: templates for controlled records.
- `optional/`: documents activated only for relevant projects.

## Status values

Use one of:

- `draft`
- `under-review`
- `approved`
- `active`
- `blocked`
- `completed`
- `superseded`
- `not-applicable`

Do not mark a document approved without a recorded human approval or an explicit project policy allowing that approval.
