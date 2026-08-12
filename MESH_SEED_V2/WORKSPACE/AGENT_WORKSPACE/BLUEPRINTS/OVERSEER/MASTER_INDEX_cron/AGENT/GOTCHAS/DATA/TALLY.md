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
| 1   | rewriting an identical body every tick churns multi-device sync and buries real changes | write-if-changed, with the refresh stamp excluded from the comparison — else the stamp itself forces a daily write |
| 1   | a refresh clobbers descriptions agents wrote into the index by hand | the script never authors a description: harvest first, re-attach by path, carry a moved file by unique basename, leave ambiguity blank |
