---
type: living_doc
scope: blueprint_gotchas
name: Master index refresh cron
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

- **[1]x** — Cron reading user folders fails at the macOS TCC privacy boundary regardless of code correctness → grant Full Disk Access to `/usr/sbin/cron` in System Settings before the first tick, or site the vault outside protected folders [macOS 15, Apple Silicon, 2026/08/04]
- **[1]x** — Interactive test runs write the same log as scheduled runs, so a job that has NEVER succeeded under cron shows successes in its log → verification only counts from a real scheduled tick; never accept a hand-run as proof [macOS 15, 2026/08/04]
- **[1]x** — A bare `python3` in a crontab line resolves against a PATH cron does not have → use the interpreter's absolute path [macOS 15, 2026/08/03]
- **[1]x** — Rebuilding the index without harvesting the previous description column destroys every human-written description on the first run → harvest before rebuild, key by vault-relative path [macOS 15, 2026/08/03]
- **[1]x** — A description containing a pipe character breaks the markdown table it is written into → escape on harvest, not on write [macOS 15, 2026/08/03]
- **[1]x** — Unconditional daily writes churn the file for sync and backup even when the content is identical → compare before writing, skip when unchanged [macOS 15, 2026/08/03]
- **[1]x** — This script shipped with a hardcoded absolute vault root while its sibling sweep script resolved from its own file location — only the sibling survived a vault move. Found by writing this blueprint, fixed at the source on 2026/08/09 (`str(Path(__file__).resolve().parents[2])`, same depth as the sibling) → resolve from `__file__`; treat any absolute constant in a shipped script as a defect [macOS 15, 2026/08/08]
