---

document: prompts
status: active
mode: bootstrap
last_updated: 2026-07-26
------------------------

# NoYap Project Prompts

## Instructions for the user

Copy only the prompt inside the **NEXT PROMPT** block and give it to the coding agent that has access to this repository.

After the agent finishes:

1. read its short review summary;
2. review only the decisions that require human approval;
3. confirm that validation passed;
4. return to this file;
5. copy the newly generated NEXT PROMPT.

Do not skip ahead using roadmap titles. Roadmap entries describe future work but are not executable prompts.

Do not manually edit the NEXT PROMPT unless correcting an obvious error. The coding agent should generate the next prompt from the latest approved project state.

## Current project state

The canonical current phase, current task, blockers, implementation permission, completed work, and next permitted action are stored only in:

`noyap/PROJECT_STATE.md`

To display the latest project state, run:

```bash
python scripts/noyap.py status
```

To print the current copy-paste prompt directly, run:

```bash
python scripts/noyap.py next
```

This file stores executable prompts and the prompt roadmap. It must not independently duplicate canonical project-state information.

## NEXT PROMPT

<!-- NEXT_PROMPT_START -->

```text
You are continuing a project that uses NoYap.

Before taking action, read:

1. AGENTS.md
2. PROJECT_INPUT.md
3. noyap/PROJECT_STATE.md
4. the active Phase 0 section in noyap/PHASES.md

Do not write application code.

Determine whether PROJECT_INPUT.md contains:

- a rough project idea;
- supplied requirements or an SRS;
- an existing codebase;
- supporting documents;
- or a mixture of these inputs.

Continue project discovery using only information supported by the user,
provided documents, or the existing repository.

Do not silently convert recommendations into approved requirements.

Classify important information as:

- Confirmed
- Proposed
- Open
- Out of scope

Ask one short and concrete question at a time only when the answer materially
affects requirements, scope, architecture, security, data handling, cost,
design, deployment, or project feasibility.

For low-risk and reversible details, recommend a reasonable default and keep
it marked Proposed until accepted.

Do not:

- write application code;
- select or change architecture prematurely;
- install dependencies;
- create implementation files;
- expand the project scope;
- invent unsupported user requirements;
- draft future governance documents during this task.

When project discovery is sufficiently complete:

1. update PROJECT_INPUT.md with the confirmed input, proposed decisions,
   unresolved questions, and explicitly excluded items;
2. provide a concise human-review summary containing:
   - what was confirmed;
   - what remains open;
   - what was proposed;
   - what requires approval;
3. update noyap/PROJECT_STATE.md with the completed discovery status and the
   next permitted action;
4. update last_updated fields in every governed document changed during this task;
5. generate the next executable prompt for drafting noyap/PRD.md;
6. replace only the content inside the NEXT_PROMPT_START and NEXT_PROMPT_END
   markers in PROMPTS.md;
7. run:
   python scripts/noyap.py validate
8. report the validation result;
9. stop without drafting the PRD or writing application code.
```

<!-- NEXT_PROMPT_END -->

## Planned prompt roadmap

These are high-level checkpoints. Detailed executable prompts are generated just in time from the latest validated project state.

1. Complete project discovery
2. Draft the PRD from confirmed project input
3. Review and approve the PRD
4. Draft and approve project scope
5. Draft architecture and the approved technology stack
6. Draft design rules when applicable
7. Finalize engineering and agent rules
8. Build the complete phase roadmap
9. Review and approve the project baseline
10. Generate detailed prompts for the active phase
11. Implement and validate one task or approved task batch
12. Review the completed phase
13. Progress to the next approved phase
14. Complete release preparation
15. Prepare the final project handoff and documentation

Roadmap entries must not be copied directly to an agent unless they have been converted into a complete NEXT PROMPT.

## Prompt-generation rules

Every newly generated NEXT PROMPT must:

1. identify one exact objective;
2. reference the active phase and task from `noyap/PROJECT_STATE.md`;
3. list only the files needed for that task;
4. identify the approved requirement or task being completed;
5. state what must not be changed;
6. require the smallest coherent implementation;
7. prohibit unrelated refactoring;
8. prohibit unapproved dependencies;
9. define the required validation;
10. identify which documents must be updated;
11. require the next prompt to be generated only after validation;
12. stop after the current task or approved task batch.

Future prompts must not duplicate the full PRD, architecture, scope, design, or rules. They should reference the relevant files and sections instead.

## Prompt progression rule

Normally, one agent run should:

1. read the required context;
2. complete one task or approved task batch;
3. run the required validation;
4. update affected documentation;
5. update `noyap/PROJECT_STATE.md`;
6. generate the next executable prompt;
7. stop.

The agent must not automatically continue into the next task unless the current prompt explicitly authorizes an approved task batch.

The agent must stop when:

* validation fails;
* project state is inconsistent;
* required information is missing;
* the request changes approved scope;
* architecture must change;
* a production dependency must be added;
* database structure must change outside the approved task;
* security or privacy boundaries must change;
* the design system must change;
* human approval is required.

When validation fails, the next prompt must address the failure instead of progressing to another feature or phase.

## Recovery prompt: resume safely

```text
Resume this NoYap project safely.

Before modifying anything, read:

1. AGENTS.md
2. noyap/PROJECT_STATE.md
3. the active section of noyap/PHASES.md
4. noyap/MEMORY.md
5. the NEXT PROMPT block in PROMPTS.md

Inspect git status and only the recent changes relevant to the current task.

State:

- the current phase;
- the current task;
- the last completed task;
- the latest validation result;
- current blockers;
- protected project boundaries;
- the exact next permitted action.

Treat noyap/PROJECT_STATE.md as the canonical source of project status.

If PROMPTS.md, PHASES.md, project documentation, or the repository state
conflicts with PROJECT_STATE.md, do not implement code. Resolve or report the
contradiction first.

After project state is confirmed, execute only the current NEXT PROMPT.

Do not begin future tasks, perform unrelated refactoring, change architecture,
or add dependencies.
```

## Recovery prompt: fix a bug with minimal change

```text
Handle this bug under NoYap governance.

First read:

1. AGENTS.md
2. noyap/PROJECT_STATE.md
3. the active section of noyap/PHASES.md
4. the approved requirement related to the reported behaviour
5. the relevant implementation, tests, and documentation

Before editing:

- reproduce the bug or establish clear evidence for it;
- identify the likely root cause;
- identify the smallest coherent fix;
- list the files expected to change;
- search for existing logic that can be reused.

Do not:

- change architecture;
- add or replace dependencies;
- expand project scope;
- redesign the interface;
- modify unrelated files;
- rewrite working modules;
- add future features;
- create unnecessary abstractions.

Implement only the smallest safe fix.

Run targeted tests and the required project validation.

After the fix:

1. update only the documentation affected by the bug;
2. update noyap/PROJECT_STATE.md;
3. add information to noyap/MEMORY.md only when it will remain useful later;
4. update last_updated fields in governed documents changed during the task;
5. generate the next permitted prompt;
6. run:
   python scripts/noyap.py validate
7. report the files changed, validation performed, results, remaining issues,
   and whether human review is required;
8. stop.

If the fix requires a protected-area change, do not implement it. Prepare a
proposed change record instead.
```

## Recovery prompt: propose a new or changed feature

```text
Evaluate this requested feature under NoYap governance without implementing it.

Read:

1. AGENTS.md
2. noyap/PROJECT_STATE.md
3. noyap/PRD.md
4. noyap/SCOPE.md
5. noyap/ARCHITECTURE.md
6. noyap/TECH_STACK.md
7. the relevant sections of noyap/DESIGN.md
8. the relevant phase in noyap/PHASES.md

Determine whether the request is:

- already approved and planned;
- approved but not yet assigned to a phase;
- within the project domain but outside the current baseline;
- explicitly out of scope;
- or incompatible with an approved project boundary.

Explain:

- the smallest safe version of the request;
- requirements impact;
- scope impact;
- architecture impact;
- data and database impact;
- security and privacy impact;
- dependency impact;
- design impact;
- testing impact;
- phase and schedule impact;
- documentation impact.

Do not write implementation code.

When the request changes the approved baseline, create a proposed change record
under `noyap/changes/proposed/`.

Keep the request Proposed until it is approved.

Update noyap/PROJECT_STATE.md only when the project is now waiting for a
decision or approval.

Run:

python scripts/noyap.py validate

Report the validation result and stop.
```

## Completed prompt archive

Move long completed prompts to:

`noyap/prompts/completed/`

Keep only a short index here.

| Prompt | Result | Archive | Date |
| ------ | ------ | ------- | ---- |
|        |        |         |      |
