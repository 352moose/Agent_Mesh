---
type: project
class: work
state: unflagged
review_status: live
created: "{YYYY/MM/DD XX S_N}"
updated: "{YYYY/MM/DD XX S_N}"
tags:
  - build
  - report
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
  - report
---
```

---

## Page Rules

> CLIde execution report. Overwritten in full after each step. Director reads to determine pass/fail, absorb flags, and plan next step.

| Rule           | Value                                     |
| -------------- | ----------------------------------------- |
| Write model    | overwrite — entire doc replaced each step |
| Who writes     | CLIDE                                     |
| Who reads      | DIRECTOR                                  |
| Update trigger | user confirms pass/fail                   |

---

## Body

### Status

> One line — pass, fail, or partial.

```markdown
## Status: {PASS | FAIL | PARTIAL}
```

### Step Executed

> One line — step ID and title from the ACTION_PROMPT.

```markdown
## Step Executed

{STEP_ID} — {Step title from the ACTION_PROMPT.}
```

### What Was Done

> Plain-language summary of the work. What changed, what was added, how it works. Enough detail for the Director to understand the delta without reading code.

```markdown
## What Was Done

{Summary of implementation. File changes, logic added, architectural decisions executed. No code blocks — describe in prose.}
```

### Files Changed

> Table of files added, modified, or deleted. Total file count after step.

```markdown
## Files Changed

| File | Change |
|---|---|
| {path} | {Added / Modified / Deleted — brief note} |

**Total: {N} source files** ({+N added, -N deleted, N modified})
```

### Verification

> Score each Success Criterion from the ACTION_PROMPT — met / not met — and the Security Check gates that applied. The operator's own run is the gate — CLIde's checks are claims.

```markdown
## Verification

- [ ] {Success Criterion 1 — met / not met, how it was checked}
- [ ] {Security gate — held / violated}

{Other checks run — static, runtime, manual. State outcomes clearly — passed/failed/skipped.}
```

### Deviations

> Departures from the step's Intent or Security gates. The how is CLIde's to choose — free implementation choices are not deviations. If none, state "None."

```markdown
## Deviations

- {deviation — what the step bound, what was done instead, why}
```

### Director Notes

> Information the Director needs for the next step — flags, recommendations, stale docs, scope observations, count of bugs filed to `BUILD/CODEBASE/BUGS.md` this step. This is CLIde's channel to the Director.

```markdown
## Director Notes

- {note for Director}
- Bugs filed: {N or none}
```


### Refs

> Key paths and references for this step. Bugs go in `BUILD/CODEBASE/BUGS.md`, not here.

```markdown
## Refs

| Item | Path |
|---|---|
| ACTION_PROMPT | BUILD/ACTION_PROMPT.md |
| BUGS | BUILD/CODEBASE/BUGS.md |
```
