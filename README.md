# AGENT MESH

A self-populating agent workspace — a blank mesh that any modern LLM assistant can stand up from a cold start: seats, desks, memory, projects, and scheduled upkeep, all taught by the structure itself.

## Quick start

1. Get this folder onto your machine.
2. Point your assistant at `VAULT_SEED/START_HERE/START_HERE.md` and tell it to **execute this document** (say *execute* — an agent told to *read* will read, nod, and wait).
3. Say the trigger phrases it teaches you. The mesh does the rest.

## What's here

| Path | What it is |
|---|---|
| `VAULT_SEED/` | The seed — front door (`START_HERE/`) plus the blank workspace (`WORKSPACE/`) |
| `APPS/seed_nav/` | File-tree sidebar window — browse the vault, double-click to open any file natively |

## Nav app

Double-click **`Seed Nav`** (the app, macOS) or **`Seed Nav.bat`** (Windows) here at the root — a tall sidebar window opens with the file tree; double-click any file to open it in your default editor. First launch on macOS may need right-click → Open if Gatekeeper objects.

Or from a terminal:

```
python3 APPS/seed_nav/seed_nav.py [folder]
```

No argument opens this repo's root. Python 3 standard library only — no installs, no build step.

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
