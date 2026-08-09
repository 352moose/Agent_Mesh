---
type: living_doc
scope: blueprint_machines
name: Desk sweep cron
created: 2026/08/08
updated: 2026/08/08
maintained_by: BUILDING AGENT
review_status: protected
---

# Machines — Where This Has Been Built

> The evidence behind the gates. Read this when no gate matches your environment: the nearest listed machine is the best thing to translate from.

---

## Builds

| CAP        | Behavior                                     | Hygiene                                                          |
| ---------- | -------------------------------------------- | ---------------------------------------------------------------- |
| ≤ 25 lines | fluid — one row per build, newest on top     | at cap, collapse rows sharing an OS and outcome into one with a count |

> Every build is recorded, clean ones included — a fork with no successful machines behind it reads as untested, and that is information.

| Machine | Tooling | Fork taken | Outcome | Added |
| ------- | ------- | ---------- | ------- | ----- |
| macOS 15 (Darwin 25.5), Apple Silicon | `/usr/bin/python3` 3.9 system interpreter; user crontab; two Obsidian vaults, one inside a TCC-protected folder | 1B, 2A | clean with workarounds — launchd abandoned, TCC grant required, sweeps two vaults hourly | the whole gotcha register; Gate 1 (multi-vault); Gate 2B (launchd fails the grant); the enumeration warning |

> Gates 1A, 2B and 2C are authored and unproven — no single-vault, launchd-only, or systemd build has been run.
