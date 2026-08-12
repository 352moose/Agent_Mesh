---
type: readme
class: work
state: unflagged
review_status: live
created: 2026/08/09
updated: 2026/08/12
tags:
  - readme
  - blueprints
---

# BLUEPRINTS

The build constraints for this mesh's machines — one folder per build, grouped by the seat that owns it. A blueprint is not a template and not a protocol: a template is a blank form to copy, a protocol is a procedure to run, and a blueprint is the strict folder shape one build pours into. `FOLDER_TREE/` is the stamp, `AGENT/DONE.md` is the acceptance, the module SPEC and MANIFEST are the contract, `AGENT/BUILD_PROMPTS/` run in order, and a break files to `AGENT/GOTCHAS/[ROOM]/` at the moment it happens — never tidied up at the end. The form lives at `../TEMPLATES/BLUEPRINT_template/`.

---

## Dive Card

> Guide: not a walk stop — deliver the fenced block verbatim only when the user takes the dive option at the shelf fork. This one card covers the seat folders and the builds inside them — the walk does not stop at each.

```
── Tour Stop — WORKSPACE/AGENT_WORKSPACE/BLUEPRINTS/

This shelf holds the build molds. When this mesh builds a machine —
a scheduled job, a tool, anything with moving parts — the code
doesn't get poured wherever the builder feels like. It gets poured
into one of these: a fixed folder shape that says where the working
parts go, what the finished thing has to do before it counts as
done, and the exact steps of the build, run in order.

Each folder here is one machine's mold. Every build also keeps a
running note of what broke, written at the moment it broke rather
than cleaned up afterwards — usually the half that saves the next
person a day.

There are two here, both the Overseer's: the job that keeps the
document index current, and the one that clears absorbed files off
the desks. If you ever want either rebuilt or running somewhere
else, its mold is how that happens.
```
