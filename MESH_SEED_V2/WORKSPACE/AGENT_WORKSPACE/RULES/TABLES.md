---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/08/11 OV S96
updated: 2026/08/11 OV S97
tags:
  - tables
  - infra
---

# Table Formats

> The house table classes — one skeleton each, devoid of prose. A new table matches a class below or argues for a new class here; the why of any row lives in a blockquote above the table, never in a cell.

---

## Rules

| Rule |
|---|
| One line per row — a cell that wraps into a paragraph is a doc trying to be a table |
| Separator row carries the same column count as the header — checkers count it too |
| No emptied rows — a deleted row goes, its pipes don't stay |
| Commands, paths, keys in backticks |
| Why lives in the blockquote above the table, never in a cell |

---

## Control table

> Governs a fluid section — cap, write behavior, prune rule. Always three columns.

| CAP | Behavior | Hygiene |
| --- | -------- | ------- |
| {≤ N lines} | {write model} | {prune rule} |

---

## Rules table

> Bare rules, one column. Add a `Value` / `Detail` column only when every row has one.

| Rule |
| ---- |
| {rule} |

---

## Constraint table

> Boot AGENT RULES. Every row starts with a verb.

| Do not | Do |
| ------ | -- |
| {prohibited act} | {replacement act} |

---

## Directive table

> Boot AGENT RULES — keyed by work mode. Single-mode agents use one row. Base shape — add a column (`When`, `Write`) only when every mode fills it.

| Mode | Execute |
| ---- | ------- |
| {mode} | {output + where it lands} |

---

## Infrastructure table

> Boot AGENT RULES — one row per standing doc. Non-spin-up docs marked ON DEMAND.

| Doc | WHEN | WHAT | WHY | HOW |
| --- | ---- | ---- | --- | --- |
| {doc} | {trigger/cadence} | {what it is} | {its purpose in the role} | {how the agent engages} |

---

## Paths table

> Boot VAULT PATHS. Relative to `AGENT_WORKSPACE/` unless marked absolute.

| Item | Path |
| ---- | ---- |
| {item} | `{path}` |

---

## Loop table

> SPIN UP / CORE LOOP / SESSION CLOSE. Phase values defined in `CONVENTIONS.md` §Loop Phases — use the words, don't redefine them. Third column holds ONE payload per row: a path, a command, a condition, or a verbatim report line — never mixed prose.

| Phase | DO | Interrogatives |
| ----- | -- | -------------- |
| {phase} | {two-word act} | {one payload: `path` · `command` · condition · *"report line"*} |

---

## Tally board

> Tally-kept lists — conventions, patterns. Tally increments on contact, lowest tally prunes first.

| Tally | {Subject} | Why |
| ----- | --------- | --- |
| [N]x | {one-line entry} | {why it binds} |
