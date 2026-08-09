---
type: note
scope: DESKS
maintained_by: OVERSEER
created: 2026/08/09
review_status: protected
---

# DESKS

One inbox per seat — the channel work travels on when it is not being said in chat. A typed file lands on a desk, the owning seat reads it at its next spin-up, acts, and flags it `review_status: sweep`; the sweep cron moves flagged files to `TRASH/Desk_Sweep/`. No agent deletes anything.

Frontmatter rules for desk deliveries live in the RULEBOOK. Each seat folder here carries a Dive Card describing what that particular desk receives.

---

## Tour Card

> Guide: deliver the fenced block verbatim at this tour stop. This one card covers all three desks and the sweep folder they clear into — the walk does not stop at each.

```
── Tour Stop — WORKSPACE/AGENT_WORKSPACE/AGENTS/DESKS/

These are the desks — one inbox per seat, and the way work reaches a
seat when you are not in the room to say it. They all run the same
way: a typed file lands on a desk, the seat reads it at its next
spin-up, acts on it, and flags it as absorbed. Nothing gets deleted
here by an agent; a scheduled job moves the flagged files to the
trash later, which means a mistake is always recoverable.

There are three. The Director's desk takes project work. The Guide's
belongs to the seat you are talking to right now, and it is the one
desk you might ever put something on yourself. The Overseer's takes
notices about the workspace itself rather than about any one project.

You mostly won't file anything here — what you'll see is a seat
clearing its desk at the start of a session, which is why a seat
sometimes opens by telling you what was waiting for it.
```
