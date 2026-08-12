---
type: Infra
class: work
state: unflagged
review_status: protected
created: 2026/08/05
updated: 2026/08/11 OV S101
tags:
  - security
  - director
---

# SECURITY CHECKLIST

> Built from the security questionnaire + official-source research pass, offered at Director's first spin-up. Skeleton until then, and a skeleton is a working state — see the just-in-time rule below. Every ACTION_PROMPT distills from this file — it is the source the Security Check section draws on.

## Page Rules

| Rule                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------- |
| One section per surface; one line per gate; each gate cites its official source                                            |
| Every ACTION_PROMPT distills ONLY the gates that apply to that step — never paste the whole checklist                      |
| **Just in time when the questionnaire was declined** — a build step that touches a surface with no section here runs that surface's research pass BEFORE the prompt is written, then the step proceeds. One surface, at the moment it is first touched; never a catch-up sweep of the others |
| New surface or stack adopted = questionnaire delta + fresh research pass; write an adjacent doc, save pointer to ACTIVE.md |
| Official sources only — vendor security guides, OWASP, framework security pages; no blogs, no forums                       |

## Surfaces

> One `##` section per confirmed surface, shaped like the block below. Delete this placeholder when the first real section lands.

## [SURFACE — e.g. Web / Native app / CLI / API / Cloud]

| Gate | Source |
|---|---|

```
(empty — the first spin-up questionnaire + research pass seeds this file)
```
