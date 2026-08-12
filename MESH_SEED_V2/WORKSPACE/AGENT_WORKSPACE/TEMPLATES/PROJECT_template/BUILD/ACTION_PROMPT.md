---
type: project
class: work
state: unflagged
review_status: live
created: "{YYYY/MM/DD XX S_N}"
updated: "{YYYY/MM/DD XX S_N}"
tags:
  - build
  - prompt
---

## Page Rules

| Rule        | Value                                         |
| ----------- | --------------------------------------------- |
| Who writes  | DIRECTOR                                      |
| Who reads   | CLIDE                          |
| Write model | Director overwrites in place each step        |
| Size target | one focused goal                              |

---

## Frontmatter

```yaml
---
type: project
class: work
state: unflagged
review_status: live
created: "{YYYY/MM/DD XX S_N}"
updated: "{YYYY/MM/DD XX S_N}"
tags:
  - build
  - prompt
---
```

---

# {STEP_ID}: {Step Title}

## Context

{Project stack, recent changes, relevant file paths — current codebase facts. Enough for CLIde to orient without reading the whole codebase.}

---

## Security Check

{Applicable gates distilled from the Director's security checklist (`REFS/DIRECTOR/SECURITY_CHECKLIST.md`) + project-specific gotchas. Bake security into the step.}

---

## Intent

{The goal of this step. Not instructions. CLIde and the user figure out the how. Skeleton first — pipes connected, data flowing. No feature polish.}

---

## Success Criteria

- [ ] {Observable outcome 1 — app launches, test passes, data persists}
- [ ] {Observable outcome 2}

---

## When Complete

Write `BUILD/ACTION_REPORT.md` per its page rules — full overwrite, every section; score each Success Criterion in Verification, security gates included. New bugs land in `BUILD/CODEBASE/BUGS.md`, not in the report — flag the count in Director Notes.
