---
type: Infra
class: work
state: unflagged
review_status: live
created: "{YYYY/MM/DD XX S_N}"
updated: "{YYYY/MM/DD XX S_N}"
tags:
  - memory
  - active
  - template
---

# {Agent} Active — Living Document

> Read on spin up. Update before close. Section caps are hard — rotate at the cap, don't grow.

> **doc size = 25 KB → DISTILL triggered** — run the seat's DISTILL protocol (`AGENTS/PROTOCOLS/[ROLE]/`); section caps govern below the threshold.

---

## Working Notes

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

## {Agent}'s Log

### Session Log

| CAP         | Behavior                                                   | Hygiene                               |
| ----------- | ---------------------------------------------------------- | ------------------------------------- |
| ≤ 5 entries | fluid — one `###` block: session ref, date, what happened  | oldest folds into Consolidated Memory |

> `### {date} {ROLE} S{N}` then key decisions, outcomes, files touched.

### Consolidated Memory

| CAP        | Behavior                                             | Hygiene              |
| ---------- | ---------------------------------------------------- | -------------------- |
| ≤ 3 blocks | fluid — compressed summaries pushed from Session Log | oldest 2 fold into 1 |

> `**CM-{N}: {theme} ({session range})**` — facts, no prose.
