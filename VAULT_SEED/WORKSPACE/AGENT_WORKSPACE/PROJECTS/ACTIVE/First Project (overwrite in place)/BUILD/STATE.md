---
type: project_state
project: {PROJECT_NAME}
maintained_by: DIRECTOR / CLIDE
updated: {YYYY/MM/DD}
review_status: protected
---

# {PROJECT_NAME} — State

> High-level state + re-entry doc — where the project stands, what's open, and what to read to resume. Specifics live in their own docs; STATE points to them, it does not duplicate.

## Reading List

| CAP       | Behavior                                        | Hygiene                     |
| --------- | ----------------------------------------------- | --------------------------- |
| ≤ 6 lines | overwrite — read order after this doc, top-down | replaced each session close |

> Ordered by priority; label each with ~context %. Read top-down, stop when the budget is spent. Paths relative to this file.

| # | Document             | Path                                  | ~Context % |
|---|----------------------|---------------------------------------|------------|
| 1 | Action Report (last) | `ACTION_REPORT.md`                    |            |
| 2 | Action Prompt        | `ACTION_PROMPT.md`                    |            |
| 3 | Standing Conventions | `STANDING_CONVENTIONS.md`             |            |
| 4 | Codebase Orientation | `CODEBASE/CODEBASE_ORIENTATION.md`    |            |
| 5 | PRD (frame)          | `../REFS/PRD.md`                      |            |

## Last Completed

| CAP       | Behavior                                   | Hygiene             |
| --------- | ------------------------------------------ | ------------------- |
| ≤ 3 lines | fluid — one line per milestone, newest top | oldest line deletes |

> One line per completion: what milestone shipped + when.

- {milestone} — {date}

## Architectural Intent

| CAP       | Behavior                                   | Hygiene                                |
| --------- | ------------------------------------------ | -------------------------------------- |
| ≤ 6 lines | overwrite — current design at a high level | complete overwrite of previous version |

{One paragraph: the project's architecture and design philosophy — the shape, not the specifics.}

## Open Items

| CAP       | Behavior                                           | Hygiene              |
| --------- | -------------------------------------------------- | -------------------- |
| ≤ 8 lines | fluid — open threads + project-direction decisions | remove when actioned |

> Project/direction-level only. Code/build-pending lives in CODEBASE_ORIENTATION's Pending.

- {open item}

## Blockers / Bugs

| CAP       | Behavior                     | Hygiene              |
| --------- | ---------------------------- | -------------------- |
| ≤ 6 lines | fluid — active blockers only | remove when resolved |

- {blocker}

## Patterns / Anti-Patterns

| CAP                 | Behavior                                | Hygiene                   |
| ------------------- | --------------------------------------- | ------------------------- |
| ≤ 7 lines each list | fluid — one line + tally, cross-session | lowest tally prunes first |

> Tally increments each re-flag. High tally = proven pattern / recurring trap; a proven pattern graduates to STANDING_CONVENTIONS.

### Patterns
- **[N]x** — {pattern}

### Anti-Patterns
- **[N]x** — {anti-pattern}
