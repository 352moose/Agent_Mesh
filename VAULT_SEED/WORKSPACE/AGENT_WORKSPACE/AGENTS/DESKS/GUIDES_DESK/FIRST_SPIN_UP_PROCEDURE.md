---
type: work_order
from: MESH SEED
to: GUIDE
created: 2026/08/05
review_status: pending_review
title: First spin-up — user intake
---

# FIRST SPIN UP PROCEDURE — GUIDE

> One-time intake, fired by the first-run gate in SPIN UP. Output: registered triggers, a filled USER_PROFILE, and a user who knows how the mesh works. When the profile is live, flip this file to `review_status: sweep` — the gate never fires again.

---

## Sequence

| Phase  | DO                      | Interrogatives                                                                                                                                                                                                                                                                                                            |
| ------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Work   | Trigger registry        | confirm the fetch-line → bootstrap map from START_HERE (`../../../../../START_HERE/START_HERE.md`) is saved to persistent memory, paths resolved to this machine — save it now if the entry protocol was skipped                                                                                                          |
| Work   | Unknown mechanism?      | not sure how THIS platform persists instructions across sessions = web-search your own platform's official documentation (memory feature, custom instructions, agent configuration files) — never improvise or assume it saved                                                                                            |
| Gate   | Confirm persistence     | read the saved registry back to the user verbatim; state WHERE it was saved (which mechanism) and confirm it survives a fresh session. No native save mechanism = show the user the `START_HERE/` folder (`../../../../../START_HERE/`) instead — every fetch line is a file named exactly what they say; the tutorial still runs          |
| Work   | Trigger tutorial        | teach the user the triggers: each fetch line, what seat it summons, what a fetch does (load + run spin-up, never summarize); then run one live test — the test phrase is **"fetch me the guide"**, and only that: the user summons the seat already in the chair, proving the trigger fires without pulling the session to another seat mid-intake |
| Work   | Mine saved memory       | before asking anything — if this assistant holds saved memory about the user, mine it; intake questions cover only what memory cannot answer                                                                                                                                                                              |
| Work   | No memory to mine?      | this assistant holds no saved memory = hand the user the Memory Export Block below to paste into whichever assistant DOES hold it; they save the reply to this desk as `USER_MEMORY_EXPORT.md`; mine it in memory's place, fold durable facts into USER_PROFILE, then flag the export `sweep` like any absorbed desk file |
| Work   | Intake conversation     | ask the user, one question at a time, following the USER_PROFILE skeleton: who they are and their context; how they like to work (pace, depth, autonomy vs check-ins); preferences and pet peeves; domains and interests; current goals                                                                                   |
| Work   | Fill the profile        | fill the skeleton at `../../../REFS/GUIDE/USER_PROFILE.md` — page rules live on that file; their words over inference; stamp `updated`                                                                                                                                                                                    |
| Gate   | User review             | walk the user through the profile section by section; adjust; user approves                                                                                                                                                                                                                                               |
| Work   | Tour — the important bits | seats and their fetch lines, the desks, how work flows, where the user's own desk is — from MESH_GUIDE (`../../../REFS/GUIDE/MESH_GUIDE.md`). Lead with what the user needs on day one                                                                                                                                  |
| Work   | Tour — layer by layer   | then walk the tree top-down: orient each layer from the START_HERE folder map, and at every folder that carries a README, read it as that stop's tour card — desks, REFS shelves, project tiers, memory, the operator's rooms, the trash                                                                                  |
| Gate   | Tour check              | user confirms they know the fetch lines and where their own desk is                                                                                                                                                                                                                                                       |
| Work   | Close out               | flip this file to `review_status: sweep`                                                                                                                                                                                                                                                                                  |
| Report | Confirm                 | *Triggers registered. User profile live at REFS. First spin-up complete.*                                                                                                                                                                                                                                                 |
| Report | Hand off                | recommend session close; after close, the user says **"fetch me the overseer"** in a fresh session — workspace setup is that seat's first spin-up                                                                                                                                                                         |

---

## Memory Export Block

> Hand this to the user only when this assistant has no saved memory to mine.

```
You have saved memory about me from our past conversations. Compile it into one portable markdown document.

Include everything you know about me from saved memory, custom instructions, and our conversation history: who I am, what I do, active projects and their status, how I like to work and communicate, tools and platforms I use, constraints and preferences, ongoing goals, and recurring people or organizations in my work.

Rules:
- Output ONE markdown document and nothing else — no preamble, no commentary.
- Use these sections, skipping any that are empty: Identity & Role, Work & Active Projects, Working Style & Preferences, Tools & Stack, Constraints, Goals, People & Organizations, Other.
- One bullet per fact, stated plainly. Mark anything uncertain with (unverified).
- Memory and history only — do not invent or embellish.
- Begin with the line: # User Memory Export — [today's date]
```
