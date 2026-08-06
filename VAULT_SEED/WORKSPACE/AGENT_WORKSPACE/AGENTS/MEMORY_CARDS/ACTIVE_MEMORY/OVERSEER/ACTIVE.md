---
type: living_doc
scope: OVERSEER
maintained_by: OVERSEER
updated: 2026/08/05
session: OV S0
review_status: protected
---

# Overseer Active — Living Document

> Read on spin up. Update before close. Section caps are hard — rotate at the cap, don't grow.

---

## Working Notes

- New seat requested → load `../../../TEMPLATES/BOOTSTRAP_template/New_agent_build.md` and run it with the user — never build a boot freehand.
- Cron work (staging, verifying, MASTER_INDEX) → load the manual first: `../../../../../OPERATOR_WORKSPACE/CRONS/README.md`; LOGS and HEALTH are script-owned, read-only.

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

## Overseer's Log

### Session Log

| CAP         | Behavior                                                  | Hygiene                               |
| ----------- | --------------------------------------------------------- | ------------------------------------- |
| ≤ 5 entries | fluid — one `###` block: session ref, date, what happened | oldest folds into Consolidated Memory |

> `### {date} OV S{N}` then key decisions, outcomes, files touched.

### Consolidated Memory

| CAP        | Behavior                                             | Hygiene              |
| ---------- | ---------------------------------------------------- | -------------------- |
| ≤ 3 blocks | fluid — compressed summaries pushed from Session Log | oldest 2 fold into 1 |

> `**CM-{N}: {theme} ({session range})**` — facts, no prose.
