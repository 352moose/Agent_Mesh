---
type: project
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - blueprint
  - modules
---

# SWEEP — manifest

> Feeds and stack-checkable claims. The stack's check IS the manifest form.

| Feed | Check |
| ---- | ----- |
| Python 3 standard library only — no third-party import | `python3 -m py_compile` under the SCHEDULER'S interpreter, then grep imports against the stdlib |
| Write access across the desk room and trash of every listed vault | `--dry-run` replay — full report, zero moves |
| Frontmatter of every desk file | status read is tolerant: no frontmatter is a skip reason, never a crash |
| The crontab (operator-owned) | `crontab -l` shows the line; liveness = a REAL scheduled tick advances the log |
| Foreign-vault access rights held by the SCHEDULER, not the agent | a scheduled tick reaches the foreign desks; an agent shell may not — that asymmetry is expected and never "fixed" by moving execution to the agent |
