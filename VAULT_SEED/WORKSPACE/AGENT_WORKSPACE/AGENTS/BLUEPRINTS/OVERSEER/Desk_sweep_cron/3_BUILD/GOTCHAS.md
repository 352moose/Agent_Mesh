---
type: living_doc
scope: blueprint_gotchas
name: Desk sweep cron
created: 2026/08/08
updated: 2026/08/08
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

- **[1]x** — Desks are listed explicitly in the script, so a desk added after the build is silently never swept and nothing reports it → scan the desks directory instead of enumerating it; a folder that names its own contents needs no maintenance [macOS 15, 2026/08/08]
- **[1]x** — launchd did not hold the Full Disk Access grant that cron held, so the job silently could not reach the second vault → moved the job to cron; grant belongs to whatever runs the job, not to the script [macOS 15, 2026/08/05]
- **[1]x** — Cron reading user folders fails at the macOS TCC privacy boundary regardless of code correctness → grant Full Disk Access to `/usr/sbin/cron` before the first tick, or site the vault outside protected folders [macOS 15, 2026/08/04]
- **[1]x** — Interactive test runs write the same log as scheduled runs, so a job that has never succeeded under the scheduler shows successes → verification only counts from a real scheduled tick [macOS 15, 2026/08/04]
- **[1]x** — A bare `python3` in a crontab line resolves against a PATH cron does not have → use the interpreter's absolute path [macOS 15, 2026/08/05]
