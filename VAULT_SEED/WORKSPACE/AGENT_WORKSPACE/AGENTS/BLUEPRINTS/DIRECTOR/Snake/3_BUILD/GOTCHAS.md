---
type: living_doc
scope: blueprint_gotchas
name: Snake — tutorial project
created: 2026/08/09
updated: 2026/08/09
maintained_by: BUILDING AGENT
review_status: protected
---

# Gotchas — What Broke, and On What

> Environment failures only. Comprehension failures go to `../2_TEACH.md`. Write the entry the moment you hit it — the register fills from use, never from a step at the end.

---

## Gotchas

| CAP        | Behavior                                                     | Hygiene                                                                                  |
| ---------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| ≤ 30 lines | fluid — one line per gotcha, `[N]x` tally, newest on top     | at 3x a gotcha graduates into `PROCEDURE.md` as a gate or step, then is removed from here |

> One line: what broke, on what, and the workaround. Tally increments when another machine hits the same thing. A tally that keeps climbing is a gate the procedure is missing.

- **Empty.** This blueprint has never been built. The first thing that breaks on your machine is the first line here — write it while it is still broken, not after you have fixed it and forgotten what it looked like.
