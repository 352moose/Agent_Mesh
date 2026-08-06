---
type: action_prompt
project: {PROJECT_NAME}
step: {STEP_ID}
updated: {YYYY/MM/DD}
status: ready
maintained_by: DIRECTOR
review_status: protected
---

## Page Rules

| Rule        | Value                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------- |
| Who writes  | DIRECTOR                                                                                        |
| Who reads   | CLIDE — fetched in a terminal, executes this doc as the job                                     |
| Write model | Director overwrites in place each step                                                          |
| Status      | `ready` → `complete` when the operator confirms the step passed                                 |
| Size target | Single step. If the prompt covers more than one focused goal, the step is too big — split it.   |

---

# {STEP_ID}: {Step Title}

## Context

{Project stack, recent changes, relevant file paths from CODEBASE_ORIENTATION. Enough for CLIde to orient without reading the whole codebase.}

---

## Security Check

{Applicable gates distilled from the Director's SECURITY_CHECKLIST (REFS) + project-specific gotchas. Bake security into the step — never paste the whole checklist.}

---

## Architecture

{Standing rules from STANDING_CONVENTIONS.md that apply to THIS step. Constraints to respect — data flow, layer boundaries, platform conventions.}

---

## Intent

{The goal of this step. Not instructions — CLIde and the user figure out the how. Skeleton first: pipes connected, data flowing. No feature polish.}

---

## Success Criteria

- [ ] {Observable outcome 1 — app launches, test passes, data persists}
- [ ] {Observable outcome 2}

---

## When Complete

Summarize what was built, what files were changed, any bugs hit, and decisions made. APPEND the changed facts to `CODEBASE/CODEBASE_ORIENTATION.md` (beside this prompt) per its page rules — honor its caps, no full rewrite.
