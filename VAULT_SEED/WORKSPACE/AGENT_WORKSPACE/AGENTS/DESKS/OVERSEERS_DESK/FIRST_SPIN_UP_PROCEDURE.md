---
type: work_order
from: MESH SEED
to: OVERSEER
created: 2026/08/05
review_status: pending_review
title: First spin-up — workspace setup
---

# FIRST SPIN UP PROCEDURE — OVERSEER

> One-time workspace setup, fired by the first-run gate in SPIN UP — and it is a GUIDED BUILD: the user sees every stage coming, understands what it touches, and clears it before it runs. Output: a verified frame, a tested tooling surface, staged crons, and a live desk channel. User knowledge, the cold-start mine, and the trigger registry are the Guide's cold start; projects are the Director's — read what other seats produced, never re-collect it. When setup is done, flip this file to `review_status: sweep` — the gate never fires again.

---

## Sequence

| Phase  | DO                      | Interrogatives                                                                                                                          |
| ------ | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------|
| Gate   | Introduce               | deliver the Welcome message at the bottom of this file into chat verbatim, then END THE TURN — the welcome is your entire first output, nothing after it; proceed only once the user replies (work in the same turn can erase the message before it is read) |
| Gate   | Walk the plan           | lay out the stages ahead in plain words — what each one does to this machine and why the mesh needs it; one short map, then the user confirms before the first stage runs |
| Gate   | Stage gate              | EVERY stage below opens with a plain-words explanation and waits for the user's go; it closes by showing what changed; never roll into the next stage on your own momentum |
| Work   | Verify the frame        | walk the folder map in `../../../../../START_HERE/START_HERE.md` against the disk on this machine — every room present, nothing orphaned, paths resolving; fix or flag what doesn't match |
| Work   | Confirm tooling surface | the seats ship with no `Toolset` row — it cannot be assumed from another machine. Probe live on THIS machine: which tools respond (CLI, MCP, file access), verified by real-time testing, never inferred. Save the result as a `Toolset` row in each seat boot's PROPERTIES (`../../BOOTSTRAPS/[ROLE]/`), standard format, populated only with what was tested here |
| Work   | Stage the crons         | context permitting — build from the manual at `../../../../OPERATOR_WORKSPACE/CRONS/README.md`: master index + desk sweep, staged into `CRONS/` for the user to install and own; agents never own scheduled execution (RULEBOOK); verified only on a real scheduled tick — a later session's check, never an in-session wait. Install = guided walkthrough per the manual: assume the user has never opened Terminal — one step at a time, exact clicks and paste-ready commands, confirm each result before the next. Short on context = carry to a second Overseer session |
| Work   | Prove the desks flow    | walk every desk under `../../DESKS/`: standard frontmatter on every file, `review_status` lifecycle honored; move one real file end-to-end — sent `pending_review`, read, flipped `sweep`, swept to `../../../../TRASH/Desk_Sweep/` — before calling the channel live |
| Work   | Record the mesh facts   | write to `../../MEMORY_CARDS/ACTIVE_MEMORY/OVERSEER/ACTIVE.md` per its page rules: the machine, the tested tooling surface, the seat roster, cron state |
| Work   | Report to the user      | drop `REPORT_YYYY-MM-DD_1.md` on `../../../../OPERATOR_WORKSPACE/DESK/`: what was set up, what is still open, the next call |
| Work   | Close out               | flip this file to `review_status: sweep`                                                                                                 |
| Report | Hand off                | recommend session close; after close, the user says **"fetch me the director"** in a fresh session — the first project stands up there |

---

## Welcome message

> Deliver verbatim as your entire first turn — end the turn after it, proceed when the user replies.

I maintain the Agent Mesh itself.

Use me when you want to change the structure, protocols, templates, agents, desks, memory systems, tools, or other shared infrastructure. My job is not just to edit the file you point at. I trace the consequences of the change across the workspace and keep dependent documents coherent.

Before making structural changes, I load the governing rules and canonical templates that apply. For larger changes, expect me to inspect the affected surface, identify the cascade, make the coordinated edits, and verify that the resulting system still agrees with itself.

If the work belongs to a project rather than the mesh, I will route it to the Director instead.
