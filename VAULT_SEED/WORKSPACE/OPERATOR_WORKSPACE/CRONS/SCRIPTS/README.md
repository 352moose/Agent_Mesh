---
type: note
created: 2026/08/05
review_status: protected
title: Cron scripts
---

# Scripts

> The `.py` jobs live here — one self-contained script per cron, standard library only. Build them from the shelf manual: `../README.md`. The user's crontab points at these files; agents stage them, the user installs.

---

## Tour Card

> Guide: deliver the fenced block verbatim at this tour stop.

```
This shelf holds the jobs themselves — one self-contained Python script
per cron, built by the Overseer from the manual one level up. It starts
empty and fills during workspace setup. Once installed, your crontab
points straight at these files: they are what actually runs on the
clock. You won't edit them day to day — agents stage them here, you own
the schedule — but this is where to look when you want to see exactly
what a scheduled job does.
```
