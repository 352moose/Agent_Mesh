---
type: readme
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - blueprint
  - data
---

What running it lands, self-stamped:

| Output | Where | Ownership |
| ------ | ----- | --------- |
| index rows | between the sentinels in the tree root's `MASTER_INDEX.md` | script owns the rows; agents own the Description cells |
| run log | the shelf's log for this job — one stamped line per run: `index refreshed (N descriptions carried)` · `no change` · `FAIL <reason>` | script and crontab redirect write; agents and operator read, never write |
