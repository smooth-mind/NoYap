# Prompt: [Task ID and title]

```text
You are continuing an existing project under NoYap governance.

OBJECTIVE
Implement only [TASK ID]: [exact approved outcome].
Related requirement: [FR/NFR ID].

REQUIRED READING
1. AGENTS.md
2. noyap/PROJECT_STATE.md
3. The active phase in noyap/PHASES.md
4. [only relevant governance and module documents]
5. [relevant source files and tests]

PRECONDITIONS
- [previous task or phase condition]
- implementation_permitted is true
- no blocker affects this task

EXPECTED BEHAVIOUR
- [observable acceptance criterion]

RESTRICTIONS
- Do not change architecture, scope, approved technology, dependencies,
  database strategy, security boundaries, design system, or unrelated code.
- Reuse existing patterns.
- Use the smallest clear implementation.
- Do not implement future tasks.

EXPECTED CHANGE AREA
- [files or directories]

VALIDATION
- [targeted checks]
- [required project checks]

AFTER SUCCESS
1. Update affected documentation.
2. Update noyap/PROJECT_STATE.md.
3. Update noyap/MEMORY.md only for durable knowledge.
4. Archive this prompt when useful.
5. Generate the exact next permitted prompt in PROMPTS.md.
6. Stop without implementing the next task.

COMPLETION REPORT
Report the objective, files changed, behaviour, validation results, assumptions,
remaining issues, protected-area impact, state updates, next prompt title, and
whether human approval is required.
```
