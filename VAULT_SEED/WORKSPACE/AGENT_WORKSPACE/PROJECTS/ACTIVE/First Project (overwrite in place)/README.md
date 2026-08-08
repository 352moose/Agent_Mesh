---
type: note
scope: PROJECTS/ACTIVE/First Project
maintained_by: OVERSEER
created: 2026/08/07
review_status: protected
---

# First Project (overwrite in place)

> The project template, pre-placed. The Director renames and fills this folder in place when the first build starts — every later project copies the same shape from `../../../AGENTS/TEMPLATES/PROJECT_template/`.

---

## Tour Card

> Guide: deliver the fenced block verbatim at this tour stop — the turn after the PROJECTS layer card. Shallow on purpose: the cycle is the point, the other docs are side notes.

```
── Tour Stop — WORKSPACE/AGENT_WORKSPACE/PROJECTS/ACTIVE/First Project (overwrite in place)/

Step inside a project folder — this one is already yours. It's the
template, pre-placed: when your first build starts, the Director
renames it and fills it in, right here. Two rooms inside. REFS/
holds the PRD — the "what are we building, and why." BUILD/ is
where the work happens, and its heartbeat is two files passing back
and forth: the Director writes ACTION_PROMPT.md — one clear build
step, no more — CLIde picks it up, does the work against your
actual code, and writes what really happened into ACTION_REPORT.md.
The Director reads that and writes the next step. That's the whole
engine: one step, checked, then the next. Everything else in BUILD/
supports that loop. STATE.md is the "you are here" map any session
can pick up from. FEATURE_MAP, TWEAK_MAP, and BUG_MAP are parking
lots — one line each for ideas, adjustments, and bugs, so nothing
gets lost and nothing derails the current step. STANDING_CONVENTIONS
is the project's house rules, CODEBASE/ is the guidebook to your
real code, and CLIDE/ is where CLIde keeps its notes for this build.
No need to open any of them now — each one explains itself when the
time comes.
```
