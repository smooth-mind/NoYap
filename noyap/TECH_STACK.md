---
document: tech-stack
status: draft
version: 0.1
last_updated: YYYY-MM-DD
approved_by: null
approved_on: null
---

# Technology Stack

Choose the smallest stack that satisfies the approved requirements and the team's ability to maintain it.

## Approved technologies

| Layer | Technology | Version policy | Why chosen | Approval status |
|---|---|---|---|---|
| Runtime | | | | Proposed |
| Frontend | | | | Proposed |
| Backend | | | | Proposed |
| Database | | | | Proposed |
| Testing | | | | Proposed |
| Deployment | | | | Proposed |

## Required commands

| Purpose | Command | Notes |
|---|---|---|
| Install | | |
| Develop | | |
| Test | | |
| Lint | | |
| Type check | | |
| Build | | |

## Approved production dependencies

| Dependency | Version policy | Purpose | Why local code is insufficient | Approved by | Date |
|---|---|---|---|---|---|
| | | | | | |

## Development-only dependencies

| Dependency | Purpose | Version policy |
|---|---|---|
| | | |

## Rejected alternatives

| Alternative | Reason rejected | Reconsider when |
|---|---|---|
| | | |

## Dependency rule

A normal task may use existing approved dependencies. It may not add or replace a production dependency without an approved change record.

Before proposing a dependency:

1. show the requirement it satisfies;
2. confirm existing code or dependencies cannot satisfy it clearly;
3. consider maintenance, security, license, size, compatibility, and lock-in;
4. identify the smallest acceptable option;
5. request approval.

## Upgrade rule

Do not perform unrelated upgrades during a feature or bug-fix task. Security and compatibility upgrades should be isolated, tested, and documented.
