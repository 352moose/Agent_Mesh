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

# MASTER_INDEX — manifest

> Feeds and stack-checkable claims. The stack's check IS the manifest form.

| Feed | Check |
| ---- | ----- |
| Python 3 standard library only — no third-party import | `python3 -m py_compile` under the SCHEDULER'S interpreter, then grep imports against the stdlib |
| Read access from the shelf up to the tree root | read-only parse replay against the real index — call the pure functions, never `main()` |
| The previous index body | harvest replay reports N descriptions without writing |
| The crontab (operator-owned) | `crontab -l` shows the line; liveness = a REAL scheduled tick advances the log |
