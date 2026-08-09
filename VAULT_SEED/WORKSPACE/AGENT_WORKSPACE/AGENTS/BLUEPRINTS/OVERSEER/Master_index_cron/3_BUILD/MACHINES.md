---
type: living_doc
scope: blueprint_machines
name: Master index refresh cron
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
| macOS 15 (Darwin 25.5), Apple Silicon | `/usr/bin/python3` 3.9 system interpreter; user crontab; Obsidian on the vault, multi-device sync | 1A, 2A | clean with workarounds — TCC grant required before the first tick succeeded | the whole gotcha register; Gate 2 (macOS/TCC); the write-if-changed step |

> Gates 1B and 2B are authored and unproven — no Linux or outside-the-vault build has been run.
