---
type: blueprint_procedure
name: Master index refresh cron
created: 2026/08/08
updated: 2026/08/08
review_status: protected
---

# Procedure — Gates, Forks, and Why

> Written as record, not as command. Every step says what was done and why it was done that way, so an agent on a different machine can translate instead of obey. A step that says only "run X" carries nothing to translate and is a defect.

---

## How to Read a Step

| Element          | Meaning                                                                      |
| ---------------- | ---------------------------------------------------------------------------- |
| Gate             | a question about THIS machine — answer it before continuing                  |
| Fork             | the branch taken for one answer; each fork carries its own steps             |
| Step             | what was done, and the reason it was done that way                           |
| No matching fork | reason it out, build it, then author the gate here        |

> Evidence for any fork is the machine list in `MACHINES.md`. A fork with no machines behind it was authored, not proven — treat it as a starting point, not a guarantee.

---

## Gates

### Gate 1 — Where does the vault live relative to this script?

| Fork | Condition | Machines run | Steps |
| ---- | --------- | ------------ | ----- |
| A | Script sits inside the vault at a fixed depth | 1 | below |
| B | Script sits outside the vault | 0 | below |

#### Fork A — script inside the vault

| # | Did | Why |
| - | --- | --- |
| 1 | Resolved the vault root from the script's own location, walking up a fixed number of parent directories | The tool then survives the whole vault being moved or renamed. The origin machine learned this the hard way — see `GOTCHAS.md`: this script shipped with a hardcoded root while its sibling resolved from `__file__`, and writing this blueprint is what surfaced the split |

#### Fork B — script outside the vault

| # | Did | Why |
| - | --- | --- |
| 1 | Authored, not run. A single absolute constant at the top of the file, nothing else hardcoded | Untested on any machine — if you take this fork, record it |

### Gate 2 — Is this macOS?

| Fork | Condition | Machines run | Steps |
| ---- | --------- | ------------ | ----- |
| A | macOS | 1 | below |
| B | Linux / other unix | 0 | below |

#### Fork A — macOS

| # | Did | Why |
| - | --- | --- |
| 1 | Granted Full Disk Access to `/usr/sbin/cron` in System Settings before the first tick | Cron hits the TCC privacy boundary reading user folders and fails on permissions no matter how correct the code is. This is the single most expensive gotcha in this blueprint — read its entry before skipping the step |
| 2 | Used `/usr/bin/python3`, the system interpreter, by absolute path in the crontab line | Cron runs with a minimal environment. A bare `python3` resolves against a PATH that cron does not have |

#### Fork B — Linux / other unix

| # | Did | Why |
| - | --- | --- |
| 1 | Authored, not run. No TCC layer exists, so the permission step drops; the interpreter still needs an absolute path | Untested — record the result if you take this fork |

---

## Steps After All Gates

| # | Did | Why |
| - | --- | --- |
| 1 | Wrote one self-contained script, standard library only | No dependency install means nothing to break on a machine that has never run it |
| 2 | Bounded every write to the text between two marker comments in the index file | Everything above the markers is human-curated. The script owning only what it generated is what makes an unattended daily write safe |
| 3 | Made it fail closed — markers missing or index missing exits non-zero and writes nothing | A half-written index is worse than a stale one |
| 4 | Harvested the existing description column before rebuilding, keyed by vault-relative path, and re-attached it to the new rows | The rows belong to the script; the descriptions belong to agents and the user. Rebuilding without harvesting silently destroys human work every night |
| 5 | Carried descriptions across file moves by matching on unique basename when the path no longer resolves | A moved file keeping its description is the difference between an index that survives a reorganisation and one that empties itself |
| 6 | Escaped pipe characters in harvested descriptions before writing them into table cells | An unescaped pipe silently breaks the markdown table it lands in |
| 7 | Compared the newly built body against the existing one and skipped the write when identical | An unconditional daily write churns the file for sync and backup tools even when nothing changed. This is where the machine's save and sync behaviour enters the design |
| 8 | Excluded trash, logs, and memory-card directories from the scan | Indexing the trash makes the index a record of what was deleted |
| 9 | Wrote a dated line to the log on every run, success or failure | The log is the only evidence a scheduled job ever ran. a real tick advancing this log is the acceptance test below |

---

## Acceptance

| CAP       | Behavior                                          | Hygiene                                              |
| --------- | ------------------------------------------------- | ---------------------------------------------------- |
| ≤ 8 lines | overwrite — what "done" looks like on any machine | rewritten only when what the blueprint builds changes |

> Observable on the receiving machine, in terms the user can check. Never "the script completed." A criterion that can only be met later is still a criterion — mark it outstanding and carry on; no session waits for it.

- The index file's auto block lists the vault's current files, and the text above the markers is untouched.
- Descriptions written before the run are still present after it.
- Running it twice with no file changes leaves the file's modified time unchanged the second time.
- A dated line appeared in the log at the scheduled time, on a day nobody ran it by hand — OUTSTANDING until a real tick; whichever session comes next reads the log.

---

## Sync and Close

> Fires once, after the build is confirmed operational — never before it, never on handoff. The blueprint is the record; this is where the record catches up to what actually happened.

| Phase  | DO             | Interrogatives                                                                                  |
| ------ | -------------- | ------------------------------------------------------------------------------------------------ |
| Gate   | Operational    | acceptance met, or its outstanding criteria named and carried — otherwise the build is not done  |
| Work   | Sync the stack | one pass over every file in this tree: forks authored, registers written, head bumped            |
| Report | Close          | recommend session close per the seat's own procedure                                             |
