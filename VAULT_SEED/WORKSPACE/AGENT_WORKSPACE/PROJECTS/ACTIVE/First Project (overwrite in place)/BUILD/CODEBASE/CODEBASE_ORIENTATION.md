---
type: living_doc
scope: {PROJECT_NAME} codebase
maintained_by: CLIDE
updated: {YYYY/MM/DD}
session: {ROLE_SN}
review_status: protected
---

# Codebase — {PROJECT_NAME}

> **Purpose.** What CLIde reads to place the next step without re-reading the whole codebase — only what is worth carrying between steps, ranked by importance. CLIde reads the code itself for detail; anything that rotates off is re-derivable from it.

---

## Architecture

| CAP         | Behavior           | Hygiene                                                                                     | Anti-Bloat Protocol                                                                                                                                                |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ≤ 100 lines | New lines appended | delete stale refs; consolidate where possible; trim with recency-bias; triage by importance | a part that grows too large can be split into an adjacent file; the new file must keep this doc's header-table skeleton. Leave a pointer here in its place. |

> One line per structural fact — how a part is shaped, how parts wire, a load-bearing seam.

- {structural fact / wiring / seam} [{step}]

---

## Pending

| CAP        | Behavior                                  | Hygiene                                  |
| ---------- | ----------------------------------------- | ---------------------------------------- |
| ≤ 10 lines | New lines appended; triaged by importance | completed steps dropped after completion |

> One line per queued change. Reference the active step.

- {what is queued next} [{step}]
