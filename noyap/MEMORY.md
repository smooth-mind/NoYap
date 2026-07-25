---
document: memory
status: active
version: 0.1
last_updated: YYYY-MM-DD
soft_line_limit: 250
---

# Project Memory

Memory contains durable knowledge that a future agent or developer would otherwise need to rediscover. It is not a transcript, daily log, task list, or duplicate of the PRD.

## Memory rules

Add an entry only when all are true:

1. it is likely to matter in a future session;
2. it is not already easy to find in a source-of-truth document;
3. forgetting it could cause rework, inconsistency, or risk;
4. the entry can be stated briefly and precisely.

Prefer links to ADRs, documentation, or source files. Remove or supersede stale entries. Keep this file below the soft line limit when practical.

## Project identity

- Project name: To be confirmed
- Primary purpose: To be confirmed

## Durable user or product constraints

- None recorded.

## Durable technical knowledge

- No application stack has been approved.

## Commands and environment facts

- Run NoYap validation with `python scripts/noyap.py validate`.

## Repeated pitfalls to avoid

- Do not begin implementation during Phase 0.
- Do not treat agent proposals as approved requirements.

## Known external limitations

- None recorded.

## Superseded memory

Move obsolete entries here briefly or link to the decision that superseded them. Remove them when history is preserved elsewhere.
