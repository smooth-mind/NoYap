---
document: phases
status: draft
version: 0.1
last_updated: YYYY-MM-DD
approved_by: null
approved_on: null
---

# Project Phases

Plan the full journey at a useful level, but generate detailed executable prompts close to execution.

## Progression rules

- Only one phase is active.
- Future phase entries are plans, not permission to implement.
- A phase may contain tasks or small approved task batches.
- Exit criteria must pass before progression.
- A protected-area change requires approval even when it appears in a future plan.
- When validation fails, generate a recovery prompt instead of progressing.

## Phase 0: Discovery and governance

- **Status:** Active
- **Objective:** Turn available project input into an approved, traceable baseline.
- **Included work:** input discovery, PRD, scope, architecture, stack, design when relevant, rules, roadmap, baseline review.
- **Excluded work:** application implementation.
- **Entry criteria:** repository created and project input available.
- **Tasks:**
  - [ ] Review and clarify `PROJECT_INPUT.md`
  - [ ] Draft and approve `PRD.md`
  - [ ] Draft and approve `SCOPE.md`
  - [ ] Draft and approve `ARCHITECTURE.md`
  - [ ] Draft and approve `TECH_STACK.md`
  - [ ] Draft and approve or mark `DESIGN.md` not applicable
  - [ ] Finalize `RULES.md`
  - [ ] Replace later phases with project-specific phases
  - [ ] Approve baseline and generate current-phase prompts
- **Required validation:** NoYap validation and human baseline review.
- **Exit criteria:** required baseline documents approved, open blockers resolved or explicitly accepted, implementation permission set true for Phase 1.
- **Human approval required:** Yes.

## Phase 1: Project foundation

Replace this generic phase after requirements and architecture are understood.

- **Status:** Planned
- **Objective:** Establish the smallest working project foundation required by the approved architecture.
- **Requirements covered:** To be mapped
- **Allowed change area:** To be defined
- **Tasks:** To be generated
- **Validation:** To be defined
- **Exit criteria:** To be defined
- **Human approval required:** Based on project risk

## Phase 2: Core user value

- **Status:** Planned
- **Objective:** Implement the smallest complete path that delivers the project's main approved value.
- **Requirements covered:** To be mapped
- **Tasks:** To be generated
- **Validation:** To be defined
- **Exit criteria:** To be defined

## Phase 3: Supporting workflows

- **Status:** Planned
- **Objective:** Implement approved supporting features without expanding scope.
- **Requirements covered:** To be mapped
- **Tasks:** To be generated
- **Validation:** To be defined
- **Exit criteria:** To be defined

## Phase 4: Hardening and release readiness

- **Status:** Planned
- **Objective:** Complete required security, accessibility, performance, reliability, documentation, and release checks.
- **Requirements covered:** To be mapped
- **Tasks:** To be generated
- **Validation:** To be defined
- **Exit criteria:** To be defined

## Phase 5: Release and handoff

- **Status:** Planned
- **Objective:** Release the approved product and leave a reproducible, understandable project state.
- **Tasks:** deployment, smoke checks, operating documentation, final state, handoff, known limitations.
- **Validation:** To be defined
- **Exit criteria:** release evidence and complete handoff.

## Phase template

Use `templates/PHASE.template.md` for additional or replacement phases.
