---
type: note
scope: new agent build
maintained_by: OVERSEER
created: 2026/08/05
review_status: protected
---

# NEW AGENT BUILD — Instructional

> For the Overseer. This is the procedure for adding a new seat to the mesh. The build runs WITH the user — you explain, they decide, you write. Most users have never built an agent; the teaching is the work.

---

## Before any work

| Rule                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Load `Bootstrap_template.md` (this folder) in full BEFORE the build starts — never freehand a boot                                                                                         |
| Load the RULEBOOK (`../../RULES/RULEBOOK.md`) if not already loaded — the new seat must conform to it                                                                                      |
| Reference your own boot (`../../BOOTSTRAPS/OVERSEER/OV_BOOTSTRAP.md`) and the Director's (`../../BOOTSTRAPS/DIRECTOR/DR_BOOTSTRAP.md`) as sources of truth — the standard, filled and live |
| *CLIde's boot (`../../BOOTSTRAPS/CLIDE/CD_BOOTSTRAP.md`) is non-standard and semi-stateless BY DESIGN — never pattern a new seat off it                                                    |
| Standardization is strict: template shape, relative paths, naming, memory protocol. A fresh boot that diverges from the template is a defect                                               |
| One step at a time with the user — never run ahead of their understanding                                                                                                                  |

---

## Teach first

The user may have no picture of what they are building. Before any interview question, explain the parts in plain language — your own words, roughly this ground:

- **What a seat is.** A role the user's assistant loads and becomes for a session — they say `fetch me the [role]` and the assistant reads that seat's definition and works inside it. One seat owns one lane of work. It is not a separate program or account; it is a definition file plus memory.
- **What a bootstrap is.** The seat's definition file: its job description, its rules (what it does, what it must never do), the addresses of the docs it works with, and its startup and shutdown procedure. The assistant follows it top to bottom every fetch.
- **What memory cards are.** How the seat remembers across sessions: a running scratch file during the session, a distilled card saved at close, and a living notes doc for durable patterns. Without them, every fetch starts blank.
- **What a desk is.** The seat's inbox. Seats never talk to each other directly — they leave typed files on each other's desks, and each seat reads its desk at spin-up.

Stop here. Ask if the picture is clear, answer questions, and only continue when the user confirms it. Nothing is written during this phase.

---

## The interview

Settle these with the user, one at a time, in order. Each answer maps to a template section — capture it, read it back, get a confirm.

| # | Settle | Maps to |
|---|---|---|
| 1 | What lane of work needs a seat — and does an existing seat already own it? If yes, stop: extend that seat instead | Role, one-line purpose |
| 2 | Name and trigger — `fetch me the [role]` | PROPERTIES |
| 3 | What it owns, and what it must never touch | Scope + Constraint |
| 4 | Work shape — repeating cycle, or single-shot? | whether CORE LOOP exists |
| 5 | Which standing docs it reads and writes, and when | Infrastructure rows |

---

## The build

Only after the interview is settled end to end:

| Step | Do |
|---|---|
| 1 | COPY `Bootstrap_template.md` to `../../BOOTSTRAPS/[ROLE]/[XX]_BOOTSTRAP.md` — copy, never move |
| 2 | Fill it section by section, showing the user each section before writing it. Every `[x]` and placeholder resolved — a shipped boot contains none |
| 3 | Seed memory by COPY from `../Memory_templates/`: ACTIVE card to `../../MEMORY_CARDS/ACTIVE_MEMORY/[ROLE]/ACTIVE.md`, session file per the session template, static shelf `../../MEMORY_CARDS/STATIC_MEMORY/[ROLE]/` with a README so the empty shelf survives packaging |
| 4 | Build the desk: `../../DESKS/[ROLE]S_DESK/` with a README |
| 5 | Acceptance: the user fetches the new seat in a FRESH session. It must spin up clean, report status, and await direction. Fix what breaks and refetch — the seat is live only after a clean first fetch |
