# Repository charter

Read when establishing guidance for a repository, when resuming or revisiting its charter, when the charter marker's version differs from this skill's, or when a change adds, alters, or contradicts a recorded responsibility.

A repository is defined by what it is accountable for, not by a project type. One repository may be a single library. Another may hold a marketing site, a product, and the advertising that drives traffic to both. The charter records those responsibilities and the owner's standing decisions about each. It is the repository's account of its own intent; it is not a product contract for a change.

## Read the state; do not ask for it

Never require the user to say whether this is a new setup or an update. Find the charter marker and compare the recorded charter with the evidence. New and update are one procedure: interview only on the difference.

| Observed state | In map-and-establish scope, or when the owner asks |
| --- | --- |
| No marker | Treat the charter as empty and establish it. Existing guidance is evidence, not an obstacle. |
| Responsibilities pending or in progress | Resume them; do not restart completed ones. |
| Evidence shows an unrecorded or changed responsibility | Reconcile that responsibility only. |
| Complete and consistent | Proceed with the requested curation. Reopen a decision only when the owner asks or its revisit condition has arrived. |
| Marker version older than this skill's | Read [the suite changelog](changelog.md). For each entry after the marker's version, check its acceptance criteria against the repository and interview only on those that fail. Record the new version when all are met. |
| Marker version newer than this skill's | Do not downgrade or rewrite it. Report that the installed skills are older and work within what you can read. |

Scope still governs. When maintaining guidance with a change, or auditing, do not start or resume a charter interview. Report a missing, unfinished, or outdated charter as a gap, reconcile only a responsibility the change itself touches, and continue the requested work. Reconciling that one responsibility includes its concerns once the owner confirms the repository carries it. When stakes order the work, apply that order across resumed and newly found responsibilities alike.

Without write authority the charter lives in chat. Say so, and say that progress will not survive the session.

## Charter marker

The marker is a small front matter block recording only what a mechanical check could use.

```yaml
---
clny_guidance:
  version: "0.3.0"
  reviewed: 2026-11-19
  responsibilities:
    - id: marketing-site
      interview: complete
    - id: saas-product
      interview: in-progress
    - id: advertising
      interview: pending
---
```

| Field | Meaning |
| --- | --- |
| version | The suite version, from this skill's frontmatter, that the charter last satisfied. Copy the current value; the example's number is illustrative. |
| reviewed | Date the whole charter was last reconciled with evidence. Reconciling one responsibility does not advance it. |
| responsibilities | Stable identifiers with an interview state. Pending: not started. In progress: at least one concern has no recorded state or is open. Complete: all six concerns have a recorded state. A completed responsibility that evidence reopens returns to in progress. |

The marker and the responsibilities table live together on the engineering entry point. Merge the key into any front matter already there. Keep both off the root README, which is the repository's public page, and off the root agent instructions, which are read as instructions. When the index lives inside the root instructions, put the marker and table on a short charter document linked from them, and follow that link when reading the state. Where a small repository has no agent instructions, a pointer from the root README is enough; do not create an instruction file only to hold a pointer. In such a repository one short guidance document is the entry point, the charter, and the guide together.

Write the marker once the owner confirms the list, with every responsibility pending. The marker records provenance; the repository's guidance must remain understandable without this skill installed.

## Scan before interviewing

Scan the repository first; many answers are already there. Source, configuration, pipelines, schedules, credentials referenced, external services, and existing documentation usually reveal most responsibilities and much of how each is handled. Label facts that rest only on the owner's description as reports.

What the scan finds is what exists, not what is wanted. Long-lived repositories accumulate practices nobody chose. Give every found practice that bears on a concern one of three standings, and never promote it on your own:

| Standing | Meaning |
| --- | --- |
| Endorsed | In place, and the owner stands behind it. Others may follow it. |
| Tolerated | In place and known not to be well. Do not copy it as an example, and do not fix it unasked. Record what is wrong as the owner describes it. |
| Unexamined | Found by the scan; the owner has not spoken to it. The default. Not a precedent. |

Deciding how to repair a tolerated practice is not this interview's work; representing it accurately is. Record standings where the practice lives, in the guide beside the owning code, and let the charter link there. Spend the detail in those guides rather than in the charter. Classify only what bears on the six concerns or what a planner would be likely to copy; leave the rest unexamined and say that it is.

## Identify the responsibilities

Propose the list from the scan, with the evidence for each entry and what you could not see.

A responsibility is an outcome the repository is accountable for in the world, such as "serves the public marketing site" or "creates, publishes, and adjusts paid advertising". Deployment, observability, and dependency maintenance are concerns that a responsibility raises, not responsibilities. Neither is a directory. New work is a separate responsibility when its exposure or authority answers differ from those of the responsibility it sits beside; otherwise it is a change to that one.

Confirming the list is the first charter decision and its own question. Ask for each responsibility's ambition in the same step. Do not put concern-level questions to the owner before the list is answered; showing what the scan found alongside it is fine. State a serious exposure as soon as you find it rather than holding it until its turn. Order the interviews by what is at stake, with anything that spends money, acts on customers, or cannot be undone first. A large repository may nest: a responsibility's guide carries its own table in the same shape.

When a change has already landed work the charter does not cover, ask only whether the owner intends the repository to carry that responsibility. How it should behave is a question for the change-scoped skills.

## Ambition

The owner chooses one level per responsibility, since the answers often differ across one repository.

| Level | Meaning |
| --- | --- |
| Starter | The minimum viable set: enough to operate safely and improve later. |
| Proportionate | The 80/20 set: the few practices that prevent most of the likely trouble. |
| Thorough | More practices are adopted, either because the work deserves expert-level attention or because it must pass substantial validation before it is approved for release. |

Ambition is the only calibration. Conduct the same interview whoever the owner is; do not shorten it or widen it by guessing at their expertise. Ambition changes how many practices you recommend, never whether a serious exposure is raised. Always name anything that can spend money, leak secrets or personal data, mislead customers, or cause loss that cannot be reversed. The owner may still decline to act on it; record that like any other decision.

Give every candidate its ongoing cost alongside its benefit, recommend against practices that exceed the chosen ambition, and say when the honest recommendation is to do nothing yet.

## Examine the concerns

For each responsibility, go through all six concerns. Bring the scan's answer to each as a finding for the owner to confirm, correct, or give a standing, and ask where the scan found nothing. They are deliberately not specific to software.

| Concern | Question |
| --- | --- |
| Change | How does this get changed, by whom, and what review does a change receive? |
| Delivery | How does a change reach the place where it takes effect, and what triggers that? |
| Health | How would anyone know it is working, or that it has stopped? |
| Dependencies | What does it rely on that changes underneath it, and how is that tracked? |
| Exposure | What can it spend, damage, disclose, or commit the owner to? |
| Authority | Who decides, who may act without asking, and what requires approval? |

For a product these become release, deployment, observability, and dependency updates. For advertising they become campaign edits, publication, spend and performance monitoring, platform policy, budget limits, and approval of creative. Translate the questions into the field's own terms.

Answer a concern once where responsibilities share it. Record a repository-wide default, such as one delivery pipeline, and let each responsibility inherit it or state its difference.

These six questions are a working hypothesis. Whether each earns its place and whether together they are sufficient for planning has not yet been established on real repositories.

## Research the field for candidates

Where a concern has no settled answer, find out what practitioners in that field treat as essential, common, and optional at the chosen ambition. Prefer authoritative, version-appropriate sources and link them. Where a fresh, delegated researcher is available and permitted, give it the responsibility, the evidence, and the ambition rather than your conclusions. Adopting an expert's vocabulary is not a substitute for sources.

Research produces candidates for the owner, never guidance directly. Present a short ranked set per concern with a recommendation that is visibly yours. Candidates resting on general knowledge alone are acceptable interview material when labeled as such; verify them against sources before writing an adopted one into guidance.

## Record decisions, including refusals

Each concern ends in a recorded state, and so does any candidate practice the owner seriously weighed under it.

| State | Meaning |
| --- | --- |
| Adopted | The owner chose it. Link the guide or procedure that carries it, or mark it not yet implemented. |
| Declined | The owner chose not to have it. Record why and what would change the answer. |
| Deferred | Wanted later. Record the condition or date for returning to it. |
| Open | Not yet decided. Dependent guidance stays provisional. |

States record what the owner decided; standings record how the owner regards what already exists. A concern handled by an endorsed practice is adopted. A concern handled only by a tolerated practice is open or deferred until the owner decides what should replace it.

A declined concern is a decision, not a gap. Recording it stops later sessions from asking again. A recommendation the owner has not answered is open with the recommendation noted, never declined. Never record approval that was not given.

Summarize in the table beside the marker and keep detail in the linked guides:

| Responsibility | Ambition | Read when | Guide | Decisions |
| --- | --- | --- | --- | --- |
| Marketing site | Starter | Changing public pages or their hosting | Site guide | Health declined: static pages, revisit if a form is added |
| Advertising | Thorough | Changing campaigns, budgets, or creative | Advertising guide | Exposure adopted: daily spend limit. Authority open. Delivery tolerated: see guide. |

This is a shape, not required columns. The decisions cell is a one-line summary: always show open concerns, declined concerns, tolerated practices, and exposures; the rest may live in the guide or the repository default. A revisit condition in the cell is sufficient for most decisions. Use the full freshness fields in [project decisions and revalidation](project-decisions.md) only for consequential, change-sensitive ones. That register holds technical conventions and reflection triggers; the charter holds decisions about responsibilities. Link between them rather than recording a decision twice. Never create an empty guide to fill a cell.

Update the table after each decided concern so a long interview can stop and resume without loss.

## Conduct and boundaries

Conduct the interview as described under "Investigate consequential uncertainty", "Revise and continue", and "Make every yield explicit" in [the requirements planning skill](../../clny-plan-requirements/SKILL.md), reading "charter" where they say plan or contract. Its product-contract and handoff material does not apply.

The charter decides what the repository intends; it does not make changes. When the owner adopts something that does not yet exist, record it as adopted and not yet implemented. Building it is a new change request: `clny-plan-requirements` when product decisions remain, otherwise `clny-plan-implementation` with the charter entry as its evidence of intent. Do not build it during curation or describe it as present.
