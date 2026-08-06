---
type: bug_map
project: {PROJECT_NAME}
maintained_by: DIRECTOR
updated: {YYYY/MM/DD}
review_status: protected
---

# {PROJECT_NAME} — Bug Map

> Parking lot for observed defects in shipped behavior. One line per bug, framed as it was seen — no diagnosis, no fix specs, no session context. Rotate fixed or dead bugs. New capabilities go in FEATURE_MAP; working-as-built adjustments go in TWEAK_MAP, not here.

## Bugs

| CAP        | Behavior                                        | Hygiene                                                 |
| ---------- | ----------------------------------------------- | ------------------------------------------------------- |
| ≤ 30 lines | fluid — one line per bug, `[N]x` tally + origin | remove on dispatch/fix/kill; at cap, lowest tally drops |

> One line = the defect in plain words — what broke and where it was seen. Tally increments each time it recurs; recurrence earns dispatch, not roadmap order.

- **[N]x** — {bug, one plain sentence} [{origin session}, {date}]
