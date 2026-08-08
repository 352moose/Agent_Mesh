---
type: note
scope: move cascade
maintained_by: OVERSEER
created: 2026/08/08
review_status: protected
---

# MOVE CASCADE

> Fires when anything keeps its name but changes its address — a file or folder relocating in the tree. Every written path to the old address is now a lie; the cascade is finding and repointing them all. Never move first and sweep later.

---

## The walk

| Step | Do |
|---|---|
| 1 | Freeze — nothing moved yet. State `old path → new path` in one line, confirm with the user |
| 2 | Destination check: parent exists, name conforms to conventions, and NOTHING already sits at the target. A file already there gets a provenance check — never assume it is scratch |
| 3 | Sweep the whole tree for the old path AND the bare filename — contents and filenames, no result cap. Wikilinks, PATHS tables, README maps, scripts, cron lines: path consumers in automation break silently |
| 4 | Build the census: every hit by filename, classified live / fossil / coincidence. Fossils keep the old path — expected, not drift |
| 5 | Move — `git mv` inside a repo, copy-then-verify otherwise. The move itself is one step of seven, not the job |
| 6 | Fan out per `Cascade_fan_out.md` — slice the census across instances primed with `old path → new path` and one correction class: repoint the address, touch nothing else |
| 7 | Verify: old-path sweep returns fossils only; every repointed link resolves; any script or cron consuming the path gets a live read check |

---

## Hard rules

| Rule |
|---|
| An address copied into N boots belongs in ONE contract file the boots point at — flag it; the next move becomes a one-file edit |
| The user actively reshaping the tree = re-check disk state immediately before every batch; their moves outrun yours |
| Nothing is deleted on this walk — the old location empties by the move; anything else found there routes through the sweep, provenance-checked first |
