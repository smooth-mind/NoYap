---

document: prompts
status: active
mode: bootstrap
last_updated: 2026-07-27
---

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

Do not manually edit the NEXT PROMPT unless correcting an obvious error. The coding agent should generate the next prompt from the latest approved and validated project state.

## Current project state

The canonical current phase, current task, execution mode, blockers, implementation permission, completed work, and next permitted action are stored only in:

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

Identify the active execution mode from noyap/PROJECT_STATE.md and follow the
mode rules in AGENTS.md.

This prompt authorizes only project discovery. It does not authorize drafting
later governance documents or writing application code, regardless of mode.

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
- Rejected
- Observed
- Out of scope

Ask one short and concrete question at a time only when the answer materially
affects requirements, scope, architecture, security, data handling, cost,
design, deployment, compatibility, or project feasibility.

For low-risk and reversible details, recommend a reasonable default and keep
it marked Proposed until accepted.

Do not:

- write application code;
- select or change architecture prematurely;
- install dependencies;
- create implementation files;
- expand project scope;
- invent unsupported user requirements;
- draft future governance documents during this task;
- continue into PRD drafting during this run.

When project discovery is sufficiently complete:

1. update PROJECT_INPUT.md with:
   - confirmed input;
   - observed facts;
   - proposed decisions;
   - unresolved questions;
   - rejected or explicitly excluded items;
2. provide a concise human-review summary containing:
   - what was confirmed;
   - what was observed;
   - what remains open;
   - what was proposed;
   - what requires approval;
3. update noyap/PROJECT_STATE.md with:
   - the completed discovery status;
   - the next permitted action;
   - any blocker or approval requirement;
4. update last_updated in every governed document materially changed during
   this task;
5. generate the next executable prompt for drafting noyap/PRD.md;
6. make the generated prompt state the active execution mode and authorize
   only the work permitted for that mode;
7. replace only the content inside the NEXT_PROMPT_START and NEXT_PROMPT_END
   markers in PROMPTS.md;
8. run:
   python scripts/noyap.py validate
9. report the validation result;
10. stop without drafting the PRD or writing application code.
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
11. Implement and validate the task or explicitly approved batch permitted by the active mode
12. Review the completed task, batch, or phase
13. Progress to the next approved execution unit
14. Complete release preparation
15. Prepare the final project handoff and documentation

Roadmap entries must not be copied directly to an agent unless they have been converted into a complete NEXT PROMPT.

A roadmap section, phase, or group of neighbouring tasks is not automatically an approved batch.

## Prompt-generation rules

Every newly generated NEXT PROMPT must:

1. state the active execution mode from `noyap/PROJECT_STATE.md`;
2. identify one exact objective;
3. reference the active phase and task from `noyap/PROJECT_STATE.md`;
4. identify the execution unit authorized by the prompt;
5. explicitly enumerate every task when a batch is authorized;
6. list only the files and source-of-truth documents needed for the work;
7. identify the approved requirement, verified bug, or governed task being completed;
8. state what must not be changed;
9. require the smallest coherent implementation;
10. prohibit unrelated refactoring;
11. prohibit unapproved dependencies;
12. define the required task, batch, and project validation;
13. identify which documents must be updated;
14. require the next prompt to be generated only after successful validation;
15. stop after the current task or explicitly approved batch;
16. include all applicable mandatory stop conditions.

The active mode sets the maximum batching level. It does not create permission to perform work that is not explicitly listed.

Use these execution limits:

* **guided:** authorize exactly one task;
* **balanced:** authorize one task or one explicitly approved small batch of closely related tasks;
* **autonomous:** authorize one explicitly enumerated approved batch that may contain several tasks.

Future prompts must not duplicate the full PRD, architecture, scope, design, rules, or project state. They should reference only the relevant files and sections.

## Prompt progression rule

Normally, one agent run should, according to the active mode in `noyap/PROJECT_STATE.md`:

1. read the required context;
2. confirm the task or batch explicitly authorized by the current NEXT PROMPT;
3. complete only the execution unit permitted by the active mode;
4. run narrow validation before depending on intermediate task results;
5. run the required final validation for the completed task or batch;
6. update affected documentation;
7. update `noyap/PROJECT_STATE.md`;
8. generate the next executable prompt;
9. stop.

### Guided mode

The agent must complete exactly one approved task, validate it, update state, generate the next prompt, and stop.

### Balanced mode

The agent may complete:

* one approved task; or
* one explicitly approved small batch of closely related tasks.

The tasks must share a clear objective, affected area, and validation path.

### Autonomous mode

The agent may complete all tasks explicitly enumerated in the current approved batch without stopping for a user round trip between those tasks.

The agent must not:

* interpret an entire phase as one batch;
* add adjacent or related tasks that were not listed;
* create its own batch;
* cross the active phase boundary;
* continue after a validation failure or mandatory stop condition.

For an autonomous batch, validate each task sufficiently before starting later work that depends on it. Run complete batch validation before marking the batch complete.

## Mode safety rule

Execution mode changes reporting and batching frequency only.

It never changes:

* approved scope;
* protected areas;
* architecture restrictions;
* dependency restrictions;
* security or privacy requirements;
* validation requirements;
* approval gates;
* phase boundaries;
* mandatory stop conditions.

The agent must stop immediately when:

* validation fails and cannot be resolved within the authorized work;
* project state is inconsistent;
* required information is missing;
* the request changes approved scope;
* architecture must change;
* a production dependency must be added;
* database structure must change outside the approved work;
* security or privacy boundaries must change;
* the design system must change;
* a protected area would be crossed;
* human approval is required;
* an unlisted task becomes necessary;
* the current phase boundary is reached.

When validation fails, the next prompt must address the failure instead of progressing to another task, feature, batch, or phase.

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
- the active execution mode;
- the task or batch authorized by the current prompt;
- the last completed task or batch;
- the latest validation result;
- current blockers;
- protected project boundaries;
- the exact next permitted action.

Treat noyap/PROJECT_STATE.md as the canonical source of project status.

If PROMPTS.md, PHASES.md, project documentation, or repository state conflicts
with PROJECT_STATE.md, do not implement code. Resolve or report the
contradiction first.

After project state is confirmed, execute only the current NEXT PROMPT and only
the task granularity permitted by the active mode.

Do not:

- create or expand a batch;
- begin unlisted work;
- begin future tasks;
- cross a phase boundary;
- perform unrelated refactoring;
- change architecture;
- add dependencies.

Stop immediately on any mandatory stop condition.
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

Identify the active execution mode.

This prompt authorizes only the reported bug fix unless it explicitly lists
multiple verified bugs as one approved batch.

Before editing:

- reproduce the bug or establish clear evidence for it;
- identify the likely root cause;
- identify the smallest coherent fix;
- list the files expected to change;
- search for existing logic that can be reused;
- confirm that the fix does not cross a protected boundary.

Do not:

- change architecture;
- add or replace dependencies;
- expand project scope;
- redesign the interface;
- modify unrelated files;
- rewrite working modules;
- add future features;
- create unnecessary abstractions;
- include another bug merely because it appears nearby.

Implement only the smallest safe fix or explicitly listed bug-fix batch.

Run targeted tests and the required project validation.

For a batch, validate each fix sufficiently before continuing to work that
depends on it.

After the fix or approved batch:

1. update only the documentation affected by the work;
2. update noyap/PROJECT_STATE.md;
3. add information to noyap/MEMORY.md only when it will remain useful later;
4. update last_updated in governed documents materially changed during the work;
5. generate the next permitted prompt according to the active mode;
6. run:
   python scripts/noyap.py validate
7. report:
   - active mode;
   - bug or batch completed;
   - files changed;
   - validation performed;
   - validation results;
   - remaining issues;
   - whether human review is required;
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

Identify the active execution mode, but do not use mode as permission to
implement the feature. This is an evaluation task only.

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

Generate the next decision or planning prompt, not an implementation prompt,
when approval remains unresolved.

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
