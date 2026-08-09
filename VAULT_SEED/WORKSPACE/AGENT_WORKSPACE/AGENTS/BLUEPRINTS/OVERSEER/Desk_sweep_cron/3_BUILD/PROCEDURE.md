---
type: blueprint_procedure
name: Desk sweep cron
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

### Gate 1 — Does this machine hold one vault or several?

| Fork | Condition | Machines run | Steps |
| ---- | --------- | ------------ | ----- |
| A | One vault | 0 | below |
| B | Several vaults, one sweeper | 1 | below |

#### Fork A — one vault

| # | Did | Why |
| - | --- | --- |
| 1 | Authored, not run. Resolve the vault root from the script's own file location and sweep the desks beneath it | Untested as a standalone — the origin machine went straight to Fork B |

#### Fork B — several vaults, one sweeper

| # | Did | Why |
| - | --- | --- |
| 1 | Resolved the primary vault root from the script's own file location | The tool survives the primary vault being moved or renamed |
| 2 | Carried the secondary vault as a single absolute constant, deliberately | It is a genuinely separate tree at a fixed location, not a sibling. One sweeper covering both was an explicit ruling — two sweepers means two schedules to keep honest |
| 3 | Confirmed the schedule runner could cross into the secondary location before trusting it | On this machine the second vault sat inside a protected folder — see `GOTCHAS.md` |

### Gate 2 — What schedules jobs on this machine?

| Fork | Condition | Machines run | Steps |
| ---- | --------- | ------------ | ----- |
| A | cron | 1 | below |
| B | launchd only | 0 | below |
| C | systemd / other | 0 | below |

#### Fork A — cron

| # | Did | Why |
| - | --- | --- |
| 1 | Granted Full Disk Access to `/usr/sbin/cron` and installed a user crontab line at forty past each hour | The permission is granted to the runner, not the script. Whatever runs the job is what needs the grant |
| 2 | Used the interpreter's absolute path | Cron runs with a minimal environment and no useful PATH |

#### Fork B — launchd only

| # | Did | Why |
| - | --- | --- |
| 1 | Tried and abandoned on the origin machine. launchd did not hold the Full Disk Access grant that cron held, so the job could not reach one of the vaults | Recorded as a fork so the next machine does not repeat the attempt. If launchd is the only option, the grant must be re-established for it directly |

#### Fork C — systemd / other

| # | Did | Why |
| - | --- | --- |
| 1 | Authored, not run | Untested — record the result if you take this fork |

---

## Steps After All Gates

| # | Did | Why |
| - | --- | --- |
| 1 | Wrote one self-contained script, standard library only | No dependency install means nothing to break on a machine that has never run it |
| 2 | Read the flag out of each file's frontmatter and acted only on an exact match | A loose match is how a sweeper eats a live desk |
| 3 | Moved files, never deleted them | The trash tree stays browsable, and a wrong sweep is recoverable by hand |
| 4 | Created the per-desk destination folder when it was missing | A missing destination is a normal first-run state, not an error worth failing on |
| 5 | Left every file without the flag untouched, regardless of age | Age is not a signal. The only signal is the flag |
| 6 | Added a preview mode that reports what would move without moving it | The first run on a new machine should be observable before it is trusted |
| 7 | Emitted a machine-readable result and a dated log line every run, success or failure | The log is the only evidence a scheduled job ever ran |
| 8 | Listed the desks the script sweeps explicitly | This was the origin machine's choice and it is the weakest part of the build — a desk added later is silently never swept. See `GOTCHAS.md`; prefer scanning the desks directory |

---

## Acceptance

| CAP       | Behavior                                          | Hygiene                                              |
| --------- | ------------------------------------------------- | ---------------------------------------------------- |
| ≤ 8 lines | overwrite — what "done" looks like on any machine | rewritten only when what the blueprint builds changes |

> Observable on the receiving machine, in terms the user can check. Never "the script completed." A criterion that can only be met later is still a criterion — mark it outstanding and carry on; no session waits for it.

- Preview mode names the flagged files and moves nothing.
- A file marked finished is gone from its desk and present in the trash tree under that desk's name.
- An unflagged file on the same desk is still exactly where it was.
- A dated line appeared in the log at the scheduled time, on an hour nobody ran it by hand — OUTSTANDING until a real tick; whichever session comes next reads the log.

---

## Sync and Close

> Fires once, after the build is confirmed operational — never before it, never on handoff. The blueprint is the record; this is where the record catches up to what actually happened.

| Phase  | DO             | Interrogatives                                                                                  |
| ------ | -------------- | ------------------------------------------------------------------------------------------------ |
| Gate   | Operational    | acceptance met, or its outstanding criteria named and carried — otherwise the build is not done  |
| Work   | Sync the stack | one pass over every file in this tree: forks authored, registers written, head bumped            |
| Report | Close          | recommend session close per the seat's own procedure                                             |
