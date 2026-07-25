---
document: project-rules
status: draft
version: 0.1
last_updated: YYYY-MM-DD
approved_by: null
approved_on: null
---

# Project Rules

`AGENTS.md` contains NoYap's mandatory agent behaviour. This file adds rules specific to the project.

## Coding conventions

- Language and framework conventions:
- Naming:
- Formatting:
- File organization:
- Error handling:
- Logging:
- Comments and documentation:

## Reuse and simplicity

- Reuse existing components, services, utilities, types, and patterns before creating new ones.
- Use the smallest clear implementation that satisfies the requirement.
- Do not create an abstraction for a single trivial use unless it removes real complexity.
- Do not implement anticipated future requirements.
- Do not duplicate logic to avoid understanding existing code.

## Change boundaries

- Do not modify unrelated files.
- Do not combine broad cleanup with a feature or bug fix.
- Do not change public behaviour without an approved requirement.
- Treat more than five changed files for a small fix as a review trigger.
- Keep generated code and vendored files clearly separated when used.

## Testing rules

| Change type | Minimum validation |
|---|---|
| Documentation only | Link and NoYap validation |
| Local logic | Targeted unit tests |
| User workflow | Unit plus relevant integration or end-to-end evidence |
| Schema or persistence | Migration, rollback or recovery consideration, and integration test |
| Security-sensitive | Threat review and negative-path tests |
| Public interface | Contract and compatibility checks |

Project-specific commands belong in `TECH_STACK.md` and `PROJECT_STATE.md`.

## Documentation rules

- Update documentation only when the task changes documented behaviour.
- Keep one source of truth for each fact.
- Link instead of duplicating long content.
- Document public modules and non-obvious operational behaviour.
- Keep `PROJECT_STATE.md` current and `MEMORY.md` durable.

## Security rules

- Never commit secrets, credentials, production data, or private keys.
- Validate untrusted input at the appropriate boundary.
- Apply least privilege.
- Do not weaken checks, permissions, or encryption to make a test pass.
- Do not introduce telemetry or external data sharing without approval.

## Dependency rules

- Use the approved package manager and lockfile.
- Do not add a production dependency without approval.
- Do not make unrelated upgrades.
- Do not replace a stable library merely because another is preferred.

## Git and review rules

- Keep changes logically focused.
- Do not rewrite history unless explicitly requested and safe.
- Do not discard user changes.
- Do not claim a clean state without checking it.
- Summarize generated or binary changes separately.

## Project-specific prohibited actions

- [ ] Add prohibitions here

## Definition of done

A task is done only when:

- approved behaviour is implemented;
- relevant validation passes or failures are explicitly recorded;
- no protected boundary changed without approval;
- affected documentation is updated;
- project state is current;
- the next prompt is generated or a blocker prompt is active;
- the completion report is reviewable.
