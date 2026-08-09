---
type: note
scope: BLUEPRINTS/OVERSEER/Desk_sweep_cron
maintained_by: OVERSEER
created: 2026/08/09
review_status: protected
---

# Desk sweep cron — blueprint

Case study for the scheduled job that clears absorbed files off the desks. Read `0_ORIENTATION` through `3_BUILD` in order.

---

## Dive Card

> Guide: not a walk stop — deliver the fenced block verbatim only when the user takes the dive option at the shelf fork.

```
── Tour Stop — AGENTS/BLUEPRINTS/OVERSEER/Desk_sweep_cron/

This blueprint is the job that clears absorbed files off the desks.
When a seat finishes with a delivery it flags the file rather than
removing it, and this job moves the flagged ones to the trash on a
schedule — which is how the mesh keeps the rule that no agent ever
deletes anything.

It also carries a defect the build wrote down instead of quietly
fixing: the script names the desks it sweeps in a list, so a desk
added later is never swept and nothing reports the omission. It is
recorded here on purpose, because the blueprint's job is to hand over
what is true rather than what is tidy, and because the fix — read the
folder instead of listing its contents — is the same lesson this
workspace keeps relearning.
```
