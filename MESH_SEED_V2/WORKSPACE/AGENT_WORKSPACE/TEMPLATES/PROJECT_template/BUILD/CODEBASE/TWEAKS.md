---
type: project
class: work
state: unflagged
review_status: live
created: "{YYYY/MM/DD XX S_N}"
updated: "{YYYY/MM/DD XX S_N}"
tags:
  - build
  - tweaks
---

# {PROJECT_NAME} — Tweak Map

> Parking lot for small adjustments to shipped features. One line per tweak, framed as it was spoken — no specs, no session context. New capabilities go in FEATURES.md, not here.

## Tweaks

| CAP        | Behavior                                          | Hygiene                                             |
| ---------- | ------------------------------------------------- | --------------------------------------------------- |
| ≤ 30 lines | fluid — one line per tweak, `[N]x` tally + origin | remove on dispatch/kill; at cap, lowest tally drops |

> One line = the tweak in plain words — what changes and why. Tally increments each time it resurfaces; friction earns dispatch, not roadmap order.

- **[N]x** — {tweak, one plain sentence} [{origin session}, {date}]
