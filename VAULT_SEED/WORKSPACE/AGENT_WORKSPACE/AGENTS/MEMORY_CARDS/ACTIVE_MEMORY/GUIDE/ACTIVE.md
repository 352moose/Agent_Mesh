---
type: living_doc
scope: GUIDE
maintained_by: GUIDE
updated: 2026/08/05
session: GD S0
review_status: protected
---

# Guide Active — Living Document

> Read on spin up. Update before close. Section caps are hard — rotate at the cap, don't grow.

---

## Workspace Index

| CAP       | Behavior                                                                   | Hygiene                                          |
| --------- | -------------------------------------------------------------------------- | ------------------------------------------------ |
| ≤ 20 rows | one row per room — address + one line, formed at first close from the tour | consult silently at spin up; edit as rooms change |

| Address                                                    | One line                                                              |
| ---------------------------------------------------------- | --------------------------------------------------------------------- |
| `AGENT_WORKSPACE/AGENTS/MEMORY_CARDS/ACTIVE_MEMORY/GUIDE/ACTIVE.md` | this card — the silent map; read first at spin up, grown at every close |

---

## Working Notes

- New seat requested → Overseer's lane: `../../../TEMPLATES/BOOTSTRAP_template/New_agent_build.md` — loaded and run with the user, never freehand.

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

## Guide's Log

### Session Log

| CAP         | Behavior                                                  | Hygiene                               |
| ----------- | --------------------------------------------------------- | ------------------------------------- |
| ≤ 5 entries | fluid — one `###` block: session ref, date, what happened | oldest folds into Consolidated Memory |

> `### {date} GD S{N}` then key decisions, outcomes, files touched.

### Consolidated Memory

| CAP        | Behavior                                             | Hygiene              |
| ---------- | ---------------------------------------------------- | -------------------- |
| ≤ 3 blocks | fluid — compressed summaries pushed from Session Log | oldest 2 fold into 1 |

> `**CM-{N}: {theme} ({session range})**` — facts, no prose.
