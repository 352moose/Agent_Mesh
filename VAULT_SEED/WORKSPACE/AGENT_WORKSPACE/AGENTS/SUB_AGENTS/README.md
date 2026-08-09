---
type: note
scope: SUB_AGENTS
maintained_by: OVERSEER
created: 2026/08/08
review_status: protected
---

# SUB_AGENTS

One folder per parent seat, holding the sub-agents that seat can spawn. **The folder is the binding** — a file in `OVERSEER/` is the Overseer's sub-agent, and nothing else has to declare it. Drop a new one in a parent's folder and that parent can spawn it; there is no registry to update.

A sub-agent is not a seat. A seat is fetched by you, remembers across sessions, and owns a lane. A sub-agent is spawned by its parent, does one bounded job, reports back, and ends — no memory, no desk, no fetch line. It exists so a parent can do the same mechanical act across many files without spending its own attention, or its own context, on each one.

List a parent's folder to see what it can spawn — filenames state the purpose. New ones are built from `../TEMPLATES/SUBAGENT_template/`.

---

## Dive Card

> Guide: not a walk stop — deliver the fenced block verbatim only when the user takes the dive option at the shelf fork. This one card covers the seat folders — the walk does not stop at each.

```
── Tour Stop — WORKSPACE/AGENT_WORKSPACE/AGENTS/SUB_AGENTS/

This shelf holds the helpers a seat can call up, one folder per seat.
The folder is the entire arrangement: a file sitting in the Overseer's
folder is an Overseer helper, and nothing anywhere else needs to be
told about it. Add one, and that seat can use it immediately.

A helper is not a seat. You never summon one yourself, it keeps no
memory, it has no desk, and it finishes the moment its job is done.
It exists so that a seat facing the same small task across thirty
files can hand each one to a fresh helper, instead of working down
the list itself and giving the thirtieth file less care than the
first.

There is one so far, on the Overseer's shelf: a relay, used when the
same correction has to land identically across a batch of files. Each
one comes back with a report of exactly what it changed, and the seat
that sent it reads every one before anything stands.
```
