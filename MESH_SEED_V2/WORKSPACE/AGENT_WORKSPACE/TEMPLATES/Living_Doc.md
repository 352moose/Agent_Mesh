---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/03/27
updated: 2026/08/10 OV S93
tags:
  - template
  - living
---

# Living Doc Template

> Reusable scaffold for any permanent, overwrite-in-place vault document. Copy this template, fill in the placeholders, delete sections that don't apply.

> **doc size = 25 KB → DISTILL triggered** — run the seat's DISTILL protocol (`AGENTS/PROTOCOLS/[ROLE]/`); section caps govern below the threshold.

---

## How to Use

1. Copy this file to the target location
2. Rename to the doc's permanent fixture name (no date suffix)
3. Replace all `{placeholders}` with real values
4. Delete any body sections that don't apply — not every living doc needs all of them
5. Keep the frontmatter block and Doc Structure section — these are mandatory
6. **Open every section you keep with a control table** — see Section Structure.

---

## Frontmatter

```yaml
---
type: "{TYPE — Infra on memory/infra shelves, project in project folders}"
class: work
state: unflagged
review_status: live
created: "{YYYY/MM/DD XX S_N}"
updated: "{YYYY/MM/DD XX S_N}"
tags:
---
```

---

## Doc Structure

> Every living doc has a purpose statement, clearly separated sections, and a control table on every section.

### Section Types

| Type      | Behavior                                                                               | Use When                               |
| --------- | -------------------------------------------------------------------------------------- | -------------------------------------- |
| overwrite | Entire section replaced each update                                                    | Current state only — no history needed |
| fluid     | New entries appended, completed entries removed, recency biased, triaged by importance | Continuous work, single maintainer     |
| fenced    | Each maintainer owns and overwrites their own section                                  | Multiple maintainers, same doc         |

---

### Section Structure

Open every section with a control table, then a one-line blockquote defining what a single line is, then the content.

| Column   | Detail                                                                                              |
| -------- | --------------------------------------------------------------------------------------------------- |
| AGENT    | who writes this section — **include only for `fenced` (multi-maintainer) sections**; omit otherwise |
| CAP      | the hard ceiling in lines — `≤ N lines`                                                              |
| Behavior | which Section Type, plus a phrase on how the section is written                                      |
| Hygiene  | the rotation protocol when the section hits its cap (consolidate / evict oldest / drop completed / clear when addressed) |

> **Standard columns are CAP · Behavior · Hygiene** (add AGENT for fenced). A section may append a **custom column** when standard hygiene isn't enough — Custom protocols are per-doc, not part of the standard.

Single-maintainer control table:

| CAP      | Behavior               | Hygiene                     |
| -------- | ---------------------- | --------------------------- |
| ≤ N lines | {type} — {how written} | {rotation protocol at cap}  |

Fenced (multi-maintainer) — prepend the AGENT column:

| AGENT  | CAP      | Behavior                       | Hygiene              |
| ------ | -------- | ------------------------------ | -------------------- |
| {role} | ≤ N lines | fenced — each owns their block | {rotation protocol}  |

---

## Example Sections

> Common living-doc archetypes, each shown in canonical form. Copy the ones you need; delete the rest.

### Patterns / Anti-Patterns

| CAP            | Behavior                                          | Hygiene                 |
| -------------- | ------------------------------------------------- | ----------------------- |
| ≤ 7 lines total | fluid — one line per pattern, `[N]x` tally + date | lowest tally drops first |

> Live observations, not implemented systems.

- **[N]x** — {pattern description} [{date}]

### Log

| CAP      | Behavior                                                        | Hygiene                        |
| -------- | -------------------------------------------------------------- | ------------------------------ |
| ≤ 7 lines | fluid — one `###` block per entry: session ref, source, date  | oldest 5 fold into Summarization Log |

> `### {Session ref} — {date}` then what happened: key decisions, outcomes, files touched.

### Summarization Log

| CAP      | Behavior                                                       | Hygiene              |
| -------- | ------------------------------------------------------------- | -------------------- |
| ≤ 5 lines | fluid — compressed summaries pushed from Log rotation; facts, no prose | oldest 3 fold into 1 |

> `### SL-{N} — {date range}` then the compressed summary of the consolidated entries.

### Annotations

| AGENT               | CAP      | Behavior                          | Hygiene                              |
| ------------------- | -------- | --------------------------------- | ------------------------------------ |
| other agents / user | ≤ 5 lines | fenced — appended by the writer  | cleared by the maintainer once absorbed |

- {note from another agent or the user} [{source}, {date}]
