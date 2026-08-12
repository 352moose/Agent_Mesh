---
type: Infra
class: work
state: unflagged
review_status: live
created: 2026/08/05
updated: 2026/08/11 OV S101
tags:
  - memory
  - active
---

# Guide Active — Living Document

> Read on spin up. Update before close. Section caps are hard — rotate at the cap, don't grow.

> **doc size = 25 KB → DISTILL triggered** — run `AGENTS/PROTOCOLS/GUIDE/GD_DISTILL.md`; section caps govern below the threshold.

---

## Working Notes

- New seat requested → Overseer's lane: `AGENTS/PROTOCOLS/OVERSEER/BUILD/NEW_AGENT.md` — loaded and run with the user, never freehand.

### Captured Facts

| CAP        | Behavior                                               | Hygiene                                                                          | Tally                                                                              |
| ---------- | ------------------------------------------------------ | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| ≤ 20 lines | fluid — one line per fact: `[N]x — {fact} [{session}]` | lowest tally / oldest drops; low tally = verify on disk before answering from it | contact confirms = +1; contact contradicts = rewrite the line, tally back to [1]x |

> Crystals, not canon — a fact is only as fresh as its last confirmation; the disk outranks every line here. Seeded at [1]x by the first walk.

- {fact} [{session}]

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
