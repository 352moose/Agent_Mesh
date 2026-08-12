---
type: project
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - gotchas
  - packages
---

# GOTCHAS — `PACKAGES/`

> Repeat break = +1 tally, no new row.

| x   | Gotcha | Fix |
| --- | ------ | --- |
| 1   | root derived by counting parents from the script — a shelf move to a different depth silently targets the wrong tree; the source's own docstring already cited a stale home | derive per the shelf's declared relationship AND landmark-check the result: no index file at the resolved root means fail-closed, no write |
| 1   | a pipe character in a description breaks its table row and every row after it | sanitize on harvest — replace the pipe, collapse whitespace, before the cell is ever written |
