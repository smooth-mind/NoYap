---
document: scope
status: draft
version: 0.1
last_updated: YYYY-MM-DD
approved_by: null
approved_on: null
---

# Project Scope

This file prevents feature drift. A useful feature is not automatically an approved feature.

## In scope for the approved release

| Scope ID | Included outcome | Related requirements | Notes |
|---|---|---|---|
| IN-001 | | | |

## Explicitly out of scope

| Scope ID | Excluded item | Reason | Reconsideration condition |
|---|---|---|---|
| OUT-001 | | | |

## Possible future work

Future items are not implementation permission.

| Future ID | Idea | Earliest possible phase or release | Dependency | Status |
|---|---|---|---|---|
| FUT-001 | | | | Unapproved |

## Rejected ideas

| Rejected ID | Item | Reason | Decision source | Date |
|---|---|---|---|---|
| REJ-001 | | | | |

## Scope boundaries

Record limits such as supported users, platforms, countries, languages, devices, volumes, integrations, or workflows.

## Scope-change rule

After approval:

1. Do not implement an out-of-scope request directly.
2. Check whether the request already maps to an approved requirement.
3. If not, create a proposal from `templates/CHANGE_REQUEST.template.md`.
4. Explain the smallest safe option and impact.
5. Obtain required approval.
6. Update affected source-of-truth documents.
7. Regenerate only affected future plans and prompts.
8. Preserve completed prompt and decision history.

## Approval checklist

- [ ] Every approved PRD requirement is represented
- [ ] Major non-goals are explicit
- [ ] Future ideas cannot be mistaken for current permission
- [ ] Boundaries are understandable to a non-technical reviewer
- [ ] User approved the scope baseline
