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
| swept files | `TRASH/Desk_Sweep/[SEAT]/` in the file's own vault, collision-suffixed | script moves; cron sweeps of the trash tree own the rest of the lifecycle |
| run report | the shelf's log for this job — one JSON object per tick: swept, skipped, errors, totals, timestamp | script and crontab redirect write; agents and operator read, never write |
