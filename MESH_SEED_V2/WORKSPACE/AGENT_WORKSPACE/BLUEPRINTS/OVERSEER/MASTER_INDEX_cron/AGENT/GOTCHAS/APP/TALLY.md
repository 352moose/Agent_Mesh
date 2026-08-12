---
type: project
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - gotchas
  - app
---

# GOTCHAS — `APP/`

> Repeat break = +1 tally, no new row.

| x   | Gotcha | Fix |
| --- | ------ | --- |
| 1   | nothing marked the scheduled folder as scheduled, and a cleanup sweep took a live cron | co-locate every unattended job on ONE shelf whose name declares it scheduled; the shelf is the marker |
