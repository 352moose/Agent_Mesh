---
type: note
created: 2026/08/05
review_status: protected
title: Cron shelf — build instructions
---

# Cron Shelf — Build Instructions

> Scheduled jobs live here. Agents stage scripts onto this shelf; the user installs and owns the crontab — agents never own scheduled execution. Layout: `SCRIPTS/` (the jobs), `LOGS/` (run stamps and errors), `HEALTH/` (optional status boards).

> Any modern LLM can build these scripts from this page — instruction is deliberately light. Every path below is relative to this file.

## The Crons

| Job | Schedule | Reads | Writes |
|---|---|---|---|
| Master index refresh | daily | the `../../` tree (excluding memory cards, desks, trash) | `../../MASTER_INDEX.md` — rows between the `AUTO:INDEX` sentinels only |
| Desk sweep | hourly | every desk: `../../AGENT_WORKSPACE/AGENTS/DESKS/*/` and `../DESK/` | moves files marked `review_status: sweep` to `../../TRASH/Desk_Sweep/[SEAT]/` |

## Build Rules

- One self-contained script per job in `SCRIPTS/`, standard library only, no third-party dependencies.
- Every run writes a dated stamp to `LOGS/` — success or failure. Fail loudly to the log, never silently.
- Master index: rows are script-owned; the Description column is agent-editable and MUST be preserved across refreshes, including file moves. Blank descriptions stay blank until an agent fills them. Touch nothing outside the sentinels.
- Desk sweep: move, never delete. Create the per-seat subfolder in `Desk_Sweep/` if missing. Files without the `sweep` flag are never touched.

## Install — guided walkthrough

The crontab is user-owned, but the user may never have opened Terminal. The agent leads, ONE step at a time: give the exact click or paste-ready command, say what the user should see, and wait for their confirmation before the next step. Never bundle steps. No placeholders ever reach the user — the agent resolves every absolute path before speaking.

1. **Agent prepares.** Resolve both script paths on this machine and write the two finished crontab lines — schedule times adjusted with the user first:

   ```
   10 15 * * * /usr/bin/python3 [absolute path]/SCRIPTS/master_index.py
   40 * * * *  /usr/bin/python3 [absolute path]/SCRIPTS/desk_sweep.py
   ```

2. **macOS only — Full Disk Access first.** Cron fails at the TCC privacy boundary without it (see Verify below). Walk the user click by click, describing each screen before they click: System Settings → Privacy & Security → Full Disk Access → the **+** button (unlock with password if asked) → in the file-picker press **Cmd+Shift+G** → type `/usr/sbin/cron` → Enter → **Open** → confirm the `cron` row appears with its toggle ON.

3. **Open Terminal.** Tell the user how: press **Cmd+Space**, type `Terminal`, press Enter.

4. **Install the lines** with an append-safe paste — never send the user into `crontab -e` (it opens an editor a novice cannot exit). Hand them ONE paste block, payload only, with the real lines substituted:

   ```
   (crontab -l 2>/dev/null; echo 'LINE_1'; echo 'LINE_2') | crontab -
   ```

5. **Confirm the install.** The user pastes `crontab -l`; the agent reads the echoed output back and confirms both lines are present.

6. **Close out — verification belongs to a later session.** Never wait for a tick in-session: note "first tick pending" and end the install here. The next session reads `HEALTH/` — a stamp advanced by a real tick = live. Per Verify below.

## Verify

A job is live only when a REAL scheduled tick advances its `LOGS/` stamp. Interactive test runs mask cron failures — never count them as verification. Verification is asynchronous by design: no session ever waits for a tick. Install, record "first tick pending", and move on — whichever session comes next checks the stamp.

**macOS:** cron reading user folders (Documents, Desktop, iCloud paths) hits the TCC privacy boundary and fails with permission errors regardless of code correctness. Grant Full Disk Access to `cron` in System Settings before the first tick, or place the mesh outside protected folders.
