---
type: blueprint_audit
name: Desk sweep cron
created: 2026/08/08
review_status: protected
---

# Audit — Before Anything Executes

> The receiving mesh audits the blueprint before it builds. Trust is local: this tree is plain markdown, every claim in it is readable, and nothing arrives compiled. No binary is trusted and no third-party build is run.

---

## Checks

| Check | Result on the origin machine |
| ---------------- | ------------------------------------------------------------------------------ |
| Readable in full | Pass — the script is authored locally from `3_BUILD/PROCEDURE.md`, nothing is fetched |
| Scope | Pass — reads desk folders, writes only into the trash tree. Never writes to a desk |
| Privilege | Pass — no elevation. macOS needs Full Disk Access on `cron`, a user-granted permission |
| Remote code | Pass — standard library only, no third-party dependencies, no network calls |
| Secrets | Pass — reads frontmatter only, holds nothing, transmits nothing |
| Self-consistency | Pass — the Acceptance section of `3_BUILD/PROCEDURE.md` is a flagged file arriving in the trash tree, which is what the procedure produces |
| Environment | Answer per machine — see the gates in `3_BUILD/PROCEDURE.md` |

---

## Outcome

| Phase  | DO              | Interrogatives                                                                             |
| ------ | --------------- | ------------------------------------------------------------------------------------------ |
| Gate   | Pass            | every check clear — continue to `2_TEACH.md`                                                |
| Gate   | New environment | Environment alone failed — that is a fork to author, not a stop. Continue and record it     |
| Gate   | Fail            | any other check failed — report which, and STOP. Never build partially                      |
| Report | Always          | state the result to the user before continuing, pass or fail                                |

> This job MOVES files with no human in the loop. Audit the destination and the flag test yourself before accepting it — a sweeper with a wrong flag test empties live desks.
