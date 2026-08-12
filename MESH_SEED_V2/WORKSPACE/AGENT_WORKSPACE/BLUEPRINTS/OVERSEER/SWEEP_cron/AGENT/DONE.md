---
type: project
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - blueprint
  - done
---

# DONE — SWEEP cron

> What does done look like?

| Field       | Entry |
| ----------- | ----- |
| output      | Every `.md` file on any agent desk whose frontmatter reads `review_status: sweep` is moved, within the hour, to `TRASH/Desk_Sweep/[SEAT]/` in its own vault; each tick appends one JSON run report — swept, skipped, errors, totals, timestamp — to the shelf log |
| Interface   | The frontmatter field IS the whole control surface: an agent stamps `review_status: sweep` and stops — no manual moves, no notifications; a `--dry-run` flag reports without moving |
| constraints | Standard library only, one self-contained script. Home-vault desks DERIVED from the desk-room shape at run time, never enumerated. Foreign-vault desks listed, never derived — zero foreign entries is a valid list. Fixture files (`_NAME_` shape) never swept. A destination collision never overwrites. One bad file lands in the errors bucket and never halts the pass. Installation establishes scope: the shelf declares its relationship to the tree it sweeps, the root derives from the installed script's location per that relationship and is landmark-checked against the desk room. Agents never own scheduled execution. The job is live only when a REAL scheduled tick advances its log |
