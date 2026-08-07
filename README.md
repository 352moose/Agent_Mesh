# AGENT MESH

A self-organizing AI workspace, all self-contained in plain markdown. Point any modern AI assistant at this folder and it builds itself into a small organized team: one role learns who you are and how you work, one keeps the workspace in order, one plans and runs your projects, one writes the code. They work with you in scoped, turn-sized steps, remember between sessions, and hand work to each other as notes in folders.

Turn-based and semi-autonomous — quality output over loops or sandboxes, with security-first build practices baked in, mined from official documentation at first spin-up. No installs — minus a few crontab scripts that manage the index and trash cadence, built by the overseer's first session on your machine under whatever permission gates you grant it.

## Quick start

| Step | Do | Gotcha |
|---|---|---|
| 1 | Get this folder onto your machine. | — |
| 2 | Point your assistant at `VAULT_SEED/START_HERE/START_HERE.md` and tell it to **execute this document**. | Say *execute* — an agent told to *read* will read, nod, and wait. The assistant needs real file access: CLI assistants have it natively; chat/desktop assistants (e.g. running inside Obsidian) reach the folder through an MCP file server — set that up first, pointed at the vault root. |
| 3 | The guide spins up and walks you through the vault, then prompts a session close — the first memory cycle, which seeds the standard. | Intake is skippable. |
| 4 | Open a new session and spin up the overseer with the trigger phrase the guide taught you. | Make sure the new session is pointed at the same folder. |
| 5 | The overseer does the heavy lifting: workspace setup and crons, under whatever permission gates you grant it. It also keeps a protocol for building new agents — ask for one, and it builds the fixtures while holding the standards across the mesh. | — |
| 6 | Once setup is done, the overseer hands you off to the director, who walks you through the build cadence. | — |

## Obsidian install

```
VAULT_SEED  →  →  →  drop into your vault's root folder — in Finder / File Explorer
```

> Drag in the **file system**, not the Obsidian window — dropping onto the Obsidian interface imports/attaches instead of placing the folder at vault root.

## What's here

| Path | What it is |
|---|---|
| `VAULT_SEED/` | The seed — front door (`START_HERE/`) plus the blank workspace (`WORKSPACE/`) |
| `APPS/seed_nav/` | Optional file-tree sidebar — only for browsing without a markdown editor |

## Nav app (optional)

The workspace is just files and folders — the intended way to live in it is any markdown editor (Obsidian is a natural fit). Seed Nav exists only for those who'd rather not adopt one: a bare-bones sidebar for clicking around the file structure. Already have an editor you like? Skip this whole section.

Double-click **`Seed Nav`** (the app, macOS) or **`Seed Nav.bat`** (Windows) here at the root — a tall sidebar window opens with the file tree; double-click any file to open it in your default editor.

First launch on macOS shows a warning — *"Apple could not verify 'Seed Nav' is free of malware"*. That's because the app is an unsigned open-source script, not registered with Apple. Click **Done** (not Move to Trash), then open **System Settings → Privacy & Security**, scroll down to the "Seed Nav" notice, and click **Open Anyway** — the next double-click opens normally, and the warning never returns. On older macOS versions, right-click → **Open** → **Open** does the same job in one step.

Or from a terminal:

```
python3 APPS/seed_nav/seed_nav.py [folder]
```

No argument opens the seed vault (`VAULT_SEED/`) — the repo's app scaffolding stays out of view; pass a folder to open anything else. Python 3 standard library only — no installs, no build step.

### Factory-fresh machine

The nav needs a Python with **Tk 8.6**. A brand-new machine doesn't have one — one installer fixes it:

- **macOS** — install Python 3 from <https://www.python.org/downloads/> (ships Tk 8.6). The launcher prefers it automatically once present. Without it, macOS falls back to its own python, which first prompts to install Apple's developer tools — and even then its Tk 8.5 draws a blank, unpopulated tree on current macOS.
- **Windows** — install Python 3 from the same page and tick **"Add python.exe to PATH"** in the installer; `Seed Nav.bat` needs `pythonw`/`python` on PATH.

### Gotchas

| Symptom | Cause | Fix |
|---|---|---|
| Window opens but the tree is blank | Running under Apple's system python (Tk 8.5) | Install python.org Python 3, relaunch |
| Double-click prompts "install developer tools" | No real Python on the machine yet | Install python.org Python 3 instead — the prompt then never appears |
| Double-clicking `Seed Nav` opens it as a folder instead of launching | Finder cached the bundle as a plain folder (can happen right after the repo lands) | Run `open "Seed Nav.app"` once from a terminal at the repo root — Finder re-registers it; double-click works from then on |

**Saving caveat:** the nav opens files in your system's default editor, and saving is that editor's job, not the nav's. TextEdit and Obsidian auto-save continuously; VS Code does not unless you enable it (`files.autoSave`). This matters here: agents read what is on **disk** — an unsaved editor buffer is invisible to the mesh until it saves. An auto-saving editor as your default `.md` handler makes this a non-issue.
