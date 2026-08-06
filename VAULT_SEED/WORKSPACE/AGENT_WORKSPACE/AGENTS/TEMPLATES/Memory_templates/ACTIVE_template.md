---
type: living_doc
scope:              # agent role
maintained_by:      # agent role
updated:            # YYYY/MM/DD
session:            # {ROLE} S{N}
review_status: protected
---

# {Agent} Active — Living Document

> Read on spin up. Update before close. Section caps are hard — rotate at the cap, don't grow.

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
