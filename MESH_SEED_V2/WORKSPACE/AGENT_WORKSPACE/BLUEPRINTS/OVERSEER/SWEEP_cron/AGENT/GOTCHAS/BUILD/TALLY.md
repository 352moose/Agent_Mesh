---
type: project
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - gotchas
  - build
---

# GOTCHAS — `BUILD/`

> Repeat break = +1 tally, no new row.

| x   | Gotcha | Fix |
| --- | ------ | --- |
| 1   | a hand-run writes the same report as the scheduler and has masked a totally dead cron | verify with `--dry-run` and pure-function calls; liveness = a REAL scheduled tick advancing the log, nothing else counts |
| 1   | the install file drifts from the live crontab and a later install silently reverts a job | regenerate the install file FROM `crontab -l` after every change — the live crontab is the source, the file is its record |
