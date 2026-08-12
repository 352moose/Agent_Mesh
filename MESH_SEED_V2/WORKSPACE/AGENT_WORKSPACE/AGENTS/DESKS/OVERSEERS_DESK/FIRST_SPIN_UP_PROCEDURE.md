---
type: work_order
class: work
state: unflagged
review_status: pending_review
created: 2026/08/05
updated: 2026/08/12
tags:
  - spinup
  - overseer
---

# FIRST SPIN UP PROCEDURE — OVERSEER

> One-time workspace setup, fired by the first-run gate in SPIN UP. It runs as a tour of this seat's own rooms, and the work happens at the room it belongs to rather than as a list of stages afterwards — the crons get built standing in the crons room, the desk channel gets proved standing at the desk. Output: a verified frame, a tested tooling surface, staged crons, and a live desk channel. User knowledge, the cold-start mine, and the trigger registry are the Guide's cold start; projects are the Director's — read what other seats produced, never re-collect it. When setup is done, flip this file to `review_status: sweep` — the gate never fires again.

---

## Sequence

| Phase  | DO                      | Interrogatives                                                                                                                          |
| ------ | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------|
| Gate   | Introduce               | deliver the Welcome message at the bottom of this file into chat verbatim, then END THE TURN — the welcome is your entire first output, nothing after it; proceed only once the user replies (work in the same turn can erase the message before it is read) |
| Work   | Probe the toolset       | FIRES AUTOMATICALLY on the reply — no gate, no ask. It reads and reports, changes nothing on the machine, and every stop after it depends on knowing what actually responds here. Probe live: which tools answer (CLI, MCP, file access), verified by real-time testing, never inferred or carried from another machine. Write the result as a `Toolset` row in each seat boot's PROPERTIES (`../../BOOTSTRAPS/[ROLE]/`), standard format, populated only with what was tested here. Report the surface in one short table before the tour opens |
| Work   | Walk the seat's rooms   | the tour at the foot of this file — one room per turn, its card delivered verbatim. Three of the five carry work; that work is offered as a fork AT ITS OWN STOP, never queued for later |
| Gate   | Work fork               | a stop that carries work closes with a fork instead of a plain continue: continue to the next room, or do the work here. The work is explained in plain words BEFORE it runs and shows what changed after — that gate stays, it has just moved to where the work is. Declining is deferral, never refusal: name it in the closing report and move on |
| Work   | Record the mesh facts   | write to `../../../MEMORY_CARDS/ACTIVE_MEMORY/OVERSEER/ACTIVE.md` per its page rules: the machine, the tested tooling surface, the seat roster, cron state, and any work fork the user declined |
| Work   | Report to the user      | drop `REPORT_YYYY-MM-DD_1.md` on `../../../../OPERATOR_WORKSPACE/DESK/`: what was set up, what was deferred and where it lives, the next call |
| Work   | Close out               | flip this file to `review_status: sweep`                                                                                                 |
| Report | Hand off                | recommend session close; after close, the user says **"fetch me the director"** in a fresh session — the first project stands up there |

---

## Welcome message

> Deliver verbatim as your entire first turn — end the turn after it, proceed when the user replies.

I maintain the Agent Mesh itself — the workspace, not the work done inside it.

Use me when you want to change the structure, protocols, templates, seats, desks, memory, or tools. My job is not just to edit the file you point at. Changing one shared file pulls on every document that depended on the old shape, so I trace that spread, make the edits together, and check that the workspace still agrees with itself afterward. Work that belongs to a project goes to the Director instead.

None of that applies yet, because this workspace has not been set up. That is what this session is for.

We walk it together — five rooms, one at a time. Three of them have setup work waiting: checking the folder map against what is actually on disk, proving the desk channel by sending one real file through it end to end, and building the two scheduled jobs that keep this place tidy. That work happens in the room it belongs to rather than piling up as a list at the end. I explain each piece in plain words before it runs and show you what changed after, and you can wave any of it off — we note it and move on.

When you reply, the first thing I do is test which tools actually answer on this machine and show you the result. That one reads only; nothing on your computer changes.

Ready when you are.

---

## The seat's rooms

> Five stops, one room per turn. Three of them carry work, and that work runs at its own stop — not queued into a list of stages the user has to hold in their head while the tour finishes.

**These rooms already have cards.** Every one below is a dive on the Guide's main walk, and this tour delivers the same card rather than a second copy written for this seat. A user who already took that dive says so and waves the stop through in one turn; the work fork still fires.

| # | Room | Card | Work at this stop |
| - | ---- | ---- | ----------------- |
| 1 | `RULES/` — the four rule docs: RULEBOOK, CONVENTIONS, PROPERTIES, TABLES | `../../../RULES/README.md` | **Verify the frame** |
| 2 | `PROTOCOLS/OVERSEER/` | `../../PROTOCOLS/OVERSEER/README.md` | — |
| 3 | `SUB_AGENTS/OVERSEER/` | `../../SUB_AGENTS/OVERSEER/README.md` | — |
| 4 | this desk | `README.md` beside this file | **Prove the desk flow** |
| 5 | the crons room, and the two blueprints behind it | `../../../../OPERATOR_WORKSPACE/CRONS/README.md` · `../../../BLUEPRINTS/OVERSEER/*/AGENT/DONE.md` | **Stage the crons, then the guided install** |

| Rule |
| ---- |
| One room per turn — present it, deliver the card verbatim, then ask |
| A stop with no work closes with a plain continue |
| A stop with work closes with a fork: continue, or do the work here |
| The tour does not pause for work already declined — a deferral is recorded once, not re-offered at every stop |
| The tour ends at the crons room; the closing steps follow, never folded into the last card |

---

## The work at each stop

### Stop 1 — Verify the frame

Walk the folder map in `../../PROTOCOLS/GUIDE/TOUR_STOPS.md` against the disk on this machine — every room present, nothing orphaned, paths resolving. Fix or flag what does not match. This runs first because every later stop assumes the tree it describes is actually there.

### Stop 4 — Prove the desk flow

Walk every desk under `../../DESKS/`: standard frontmatter on every file, `review_status` lifecycle honored. Then move one real file end to end — sent `pending_review`, read, flipped `sweep`, swept to `../../../TRASH/Desk_Sweep/`. The channel is not live until a file has made that trip; a desk that has never passed a file is a claim, not a channel.

### Stop 5 — Stage the crons, then the guided install

Build from the two blueprints at `../../../BLUEPRINTS/OVERSEER/` — `MASTER_INDEX_cron` and `SWEEP_cron`. Each is the build constraint for its job: `AGENT/DONE.md` is the acceptance, the module SPEC and MANIFEST are the contract, the `BUILD_PROMPTS/` steps run in order, and a break files to the blueprint's `GOTCHAS/[ROOM]/` at the moment it happens. Stage both scripts into `CRONS/` per the manual at `../../../../OPERATOR_WORKSPACE/CRONS/README.md`, for the user to install and own. Agents never own scheduled execution (RULEBOOK).

Install is a guided walkthrough per the manual: assume the user has never opened Terminal — one step at a time, exact clicks and paste-ready commands, confirm each result before the next.

| Rule |
| ---- |
| Verified only on a real scheduled tick — a later session's check, never an in-session wait |
| A hand-run writes the same log a scheduled run does, so a job that has never once fired on schedule can show a log full of successes. Never accept a hand-run as proof |
| Short on context here = stage what you can, record the rest, and carry it to a second Overseer session |
