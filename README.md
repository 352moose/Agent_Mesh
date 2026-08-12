# AGENT MESH

A self-organizing AI workspace, all self-contained in plain markdown. Point any modern AI assistant at this folder and it builds itself into a small organized team: one meets you at the door — learns who you are, gives you the tour, and routes every ask to the right seat from then on; one keeps the workspace in order; one plans and runs your projects; one writes the code. They work with you in scoped, turn-sized steps, remember between sessions, and hand work to each other as notes in folders.

Turn-based and semi-autonomous — quality output over loops or sandboxes, with security-first build practices baked in, mined from official documentation at first spin-up. No installs — minus a few crontab scripts that manage the index and trash cadence, built by the overseer's first session on your machine under whatever permission gates you grant it.

## Quick start

| Step | Do | Gotcha |
|---|---|---|
| 1 | Get this folder onto your machine. | — |
| 2 | Point your assistant at `MESH_SEED_V2/START_HERE.md` and tell it to **execute this document**. | Say *execute* — an agent told to *read* will read, nod, and wait. The assistant needs real file access: CLI assistants have it natively; chat/desktop assistants (e.g. running inside Obsidian) reach the folder through an MCP file server — set that up first, pointed at the vault root. |
| 3 | The guide spins up, learns who you are, and gives you the tour (below), then prompts a session close — the first memory cycle, which seeds the standard. | Intake is skippable. |
| 4 | Open a new session and spin up the overseer with the trigger phrase the guide taught you. | Make sure the new session is pointed at the same folder. |
| 5 | The overseer does the heavy lifting: workspace setup and crons, under whatever permission gates you grant it. It also keeps a protocol for building new agents — ask for one, and it builds the fixtures while holding the standards across the mesh. | — |
| 6 | Once setup is done, the overseer hands you off to the director, who walks you through the build cadence. | — |

## The tour

First spin-up is a guided walk, not a README dump. The guide takes you through the workspace one room per turn — each stop draws where you are in the tree, delivers that room's card, and asks before moving on. Shelves with seat folders fork: continue to the next room, or dive into any seat for the fuller story. By the end you know every room, every trigger phrase, and where your own desk is — and the session closes into the mesh's first memory cycle, crystallizing the walk into the guide's own map so it never needs the tour again.

## Obsidian install

```
MESH_SEED_V2  →  →  →  drop into your vault's root folder — in Finder / File Explorer
```

> Drag in the **file system**, not the Obsidian window — Obsidian's UI won't accept a nested folder dropped into it; the drop silently does nothing. A nested folder has to land at the vault root in Finder / File Explorer.

## What's here

| Path | What it is |
|---|---|
| `MESH_SEED_V2/` | The seed — the entry work order (`START_HERE.md`) at its root plus the blank workspace (`WORKSPACE/`) |
