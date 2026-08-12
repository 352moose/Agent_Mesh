---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/08/10 OV S92
updated: 2026/08/11 OV S97
tags:
  - properties
  - infra
---

# Properties

---

## RULES

| Rule                                                                                 |
| ------------------------------------------------------------------------------------ |
| Seven fields, this order, on every doc in the vault                                  |
| Every field is written out                                                           |
| No doc adds an eighth field                                                          |
| No value contains `---`, no key appears twice — either breaks a cron parser silently |

---

## YAML

```yaml
type:
class:
state:
review_status:
created:
updated:
tags:
```

---

## TYPE

| Value        | Reason                                                       |
| ------------ | ------------------------------------------------------------ |
| `report`     | any report                                                   |
| `work_order` | mail — job for another agent                                 |
| `note`       | mail — informational, notice on desk                         |
| `readme`     | shelved — folder orientation                                 |
| `project`    | any doc in a project folder                                  |
| `queue`      | any doc that backlogs work                                   |
| `Infra`      | the RULES/ shelf, bootstraps and the like                    |
| `Index`      | any card indexing things (supersedes cron type below)        |
| `cron`       | any card related to automation crons                         |

---

## CLASS

| Value      | Mutability                      |
| ---------- | ------------------------------- |
| **canon**  | via patch cycle only            |
| **work**   | mutable by default              |
| **record** | finished on write, never edited |

---

## STATE

| Value       | Reason                                                                                         | Set / Cleared                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `unflagged` | assessed, nothing wrong — the default, written out                                             | —                                                                              |
| `stale`     | priors unverified, in need of update at time of friction or work — verify before leaning on it | set by whoever notices drift; cleared by whoever verifies, in the same pass    |
| `stasis`    | authority suspended — lose whatever authority they held while in stasis; do not route          | set on freeze; cleared at thaw, authority re-earned, fix on thaw               |
| `flagged`   | noticed something out of place, needs investigation                                            | don't surface, flip state value to flagged and file a note to appropriate agent |

---

## REVIEW STATUS

| Value             | Reason                                            |
| ----------------- | ------------------------------------------------- |
| `protected`       | fixture docs; trips the edit protocols            |
| `priority_notice` | user directed only                                |
| `pending_review`  | receiver has not absorbed this yet — every work order ships this, silent included, until watcher crons run |
| `watcher_pending` | awaiting watcher pickup (roadmapped cron, unimplemented) |
| `watcher_claimed` | watcher absorbed (roadmapped cron, unimplemented) |
| `sweep`           | awaiting cron sweep                               |
| `trashed`         | landed in /TRASH                                  |
| `archived`        | anything archived (research, refs)                |
| `live`            | working docs with no review cycle                 |


---

## CREATED + UPDATED

| Value     | Meaning       | Set By                       |
| --------- | ------------- | ---------------------------- |
| `created` | creation date | `YYYY/MM/DD AGENT_TAG S_N` |
| `updated` | last update   | `YYYY/MM/DD AGENT_TAG S_N` |

Example: `2026/08/10 OV S92`.

---

## TAGS

> Tags group docs, editor graph views, and agent grep

grep a staged tag before committing to an adjacent tag when a live version already exists.

Cap: 5 tags per doc, one word each. Example: `bugs`.