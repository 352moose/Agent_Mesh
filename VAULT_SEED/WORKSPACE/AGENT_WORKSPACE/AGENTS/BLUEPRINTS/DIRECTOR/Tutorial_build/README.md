---
type: note
scope: BLUEPRINTS/DIRECTOR/Tutorial_build
maintained_by: DIRECTOR
created: 2026/08/09
review_status: protected
---

# Tutorial build — blueprint

Case study for the tutorial run offered at the Director's first spin-up. The deliverable is a demonstrated Director→CLIde cycle; the game is the vehicle it runs on. Read `0_ORIENTATION` through `3_BUILD` in order. Unbuilt as of writing — both evidence registers are empty on purpose.

---

## Dive Card

> Guide: not a walk stop — deliver the fenced block verbatim only when the user takes the dive option at the shelf fork. This one card covers the numbered files inside — the fork does not go deeper here.

```
── Tour Stop — AGENTS/BLUEPRINTS/DIRECTOR/Tutorial_build/

This blueprint demonstrates how work actually gets built here, and
it is the one the Director offers a user who arrives with nothing
queued. Three rounds, each one a single instruction out and a
written report back, and the user checking the report against what
they actually got. That exchange is the deliverable.

A game of Snake is what the rounds happen to produce. It is real
and it runs on the machine, but it is the vehicle, not the point —
chosen because a game is the one thing nobody needs a report to
evaluate. A round that produces a broken game and an honest report
has done its job. A round that produces a working game and a report
nobody read has not.

It is also the only blueprint in here that runs backwards. Every
other one was written after the build, from a machine where the
thing already works. This one was written first, so the record of
what broke and the list of machines it has run on are both empty.
The user who plays the first round is the one who fills them in —
which means a person learning the workflow also produces the mesh's
first case study, on a build where nothing is lost if it goes wrong.
```
