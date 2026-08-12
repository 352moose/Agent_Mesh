---
type: Infra
class: work
state: unflagged
review_status: live
created: 2026/08/05
updated: 2026/08/11 OV S99
tags:
  - memory
  - active
---

# Director Active — Living Document

> Read on spin up. Update before close. Section caps are hard — rotate at the cap, don't grow.

> **doc size = 25 KB → DISTILL triggered** — run `AGENTS/PROTOCOLS/DIRECTOR/DR_DISTILL.md`; section caps govern below the threshold.

---

## Working Notes

- New seat requested → Overseer's lane: `AGENTS/PROTOCOLS/OVERSEER/BUILD/NEW_AGENT.md` — loaded and run with the user, never freehand.
- New project intake → copy rule in `PROJECTS/ACTIVE/README.md` — copy `PROJECT_template`, never move.

### Patterns

| CAP        | Behavior                            | Hygiene                     | Tally                    |
| ---------- | ----------------------------------- | --------------------------- | ------------------------ |
| ≤ 10 lines | fluid — one line per pattern, dated | lowest tally / oldest drops | each repeat gets a tally |

> Live observations, not implemented systems.

- {pattern} [{date}]

### Anti-Patterns

| CAP        | Behavior                          | Hygiene                     | Tally                    |
| ---------- | --------------------------------- | --------------------------- | ------------------------ |
| ≤ 10 lines | fluid — one line per anti-pattern | lowest tally / oldest drops | each repeat gets a tally |

- {anti-pattern} [{source}]

---

## Director's Log

### Session Log

| CAP         | Behavior                                                  | Hygiene                               |
| ----------- | --------------------------------------------------------- | ------------------------------------- |
| ≤ 5 entries | fluid — one `###` block: session ref, date, what happened | oldest folds into Consolidated Memory |

> `### {date} DR S{N}` then key decisions, outcomes, files touched.

### Consolidated Memory

| CAP        | Behavior                                             | Hygiene              |
| ---------- | ---------------------------------------------------- | -------------------- |
| ≤ 3 blocks | fluid — compressed summaries pushed from Session Log | oldest 2 fold into 1 |

> `**CM-{N}: {theme} ({session range})**` — facts, no prose.
