---
type: note
scope: CLIDE
maintained_by: CLIDE
created: 2026/08/05
review_status: protected
---

# REFS — CLIDE

> CLIde's reference shelf. Standing build-side references that outlive a single job — platform gotchas, toolchain notes, cross-project build references.

| Rule |
|---|
| One doc per topic; CLIde owns and maintains |
| CLIde has no seat cards — when a doc lands here, save a pointer to the relevant project memory card (`../../PROJECTS/ACTIVE/[PROJECT]/BUILD/CLIDE/ACTIVE.md`) |
| Project-specific facts stay on the project card; only cross-project references live here |
| Fixtures here are `review_status: protected` — the sweep never touches them |

---

## Dive Card

> Guide: not a walk stop — deliver the fenced block verbatim only when the user takes the dive option at the shelf fork.

```
── Tour Stop — WORKSPACE/AGENT_WORKSPACE/REFS/CLIDE/

CLIde's shelf is the build side of the same idea: references that
outlive a single job — platform gotchas, toolchain notes, anything
one build teaches that the next build will need. One thing sets it
apart. CLIde keeps no seat memory cards at all; its working memory
lives inside each project. So this is the only place its
cross-project knowledge accumulates, which makes the split matter —
facts about a single project stay on that project's card, and only
what travels between projects earns a spot here. Its first job is
already queued: when you and the Director open the starter build,
the first action prompt wakes CLIde inside that project.
```
