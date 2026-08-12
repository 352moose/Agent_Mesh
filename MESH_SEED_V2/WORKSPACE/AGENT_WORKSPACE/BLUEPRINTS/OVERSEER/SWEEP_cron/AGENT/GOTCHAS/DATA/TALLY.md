---
type: project
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - gotchas
  - data
---

# GOTCHAS — `DATA/`

> Repeat break = +1 tally, no new row.

| x   | Gotcha | Fix |
| --- | ------ | --- |
| 1   | desk filenames collide by design and a bare move silently overwrote an earlier sweep | never overwrite a destination — suffix and retry until the name is free |
| 1   | one unreadable file halted the whole pass and every desk after it stayed dirty | per-file guard: the bad file lands in the errors bucket with its exception text, the pass continues |
