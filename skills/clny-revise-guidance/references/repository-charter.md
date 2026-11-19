# Repository charter

Read when establishing guidance for a repository, when its recorded responsibilities are missing, incomplete, or contradicted by evidence, or when the owner wants to revisit a charter decision.

A repository is defined by what it is accountable for, not by a project type. One repository may be a library, a set of workflow scripts, or a marketing site, a product, and the advertising that drives traffic to both. The charter records those responsibilities and the owner's decisions about each. It is the standing account of the repository's intent; it is not a product contract for a change.

## Read the state; do not ask for it

Never require the user to say whether this is a new setup or an update. Follow the root agent instructions to the engineering entry point and read its charter marker.

| Observed state | Action |
| --- | --- |
| No entry point or no marker | Treat the charter as empty and establish it. Existing guidance is evidence, not an obstacle. |
| Marker with pending or in-progress responsibilities | Resume those interviews; do not restart completed ones. |
| Marker complete, evidence shows an unrecorded or changed responsibility | Reconcile that responsibility only. |
| Marker complete and consistent | Proceed with the requested curation. Reopen a decision only when the owner asks or its revisit condition has arrived. |
| Marker names an older contract version | Compare against the current contract and examine what changed; do not rerun the whole charter. |

All five are one procedure: compare the recorded charter with the evidence and interview only on the difference. The user still chooses scope and authority, such as audit only or revisiting one decision. In audit-only mode, report the proposed charter without writing it.

## Charter marker

Place a small front matter block on the engineering entry point. It records only what a mechanical check could use.

```yaml
---
clny_guidance:
  contract: "0.3.0"
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
| contract | The `clny-revise-guidance` version whose contract the charter was last examined against. |
| reviewed | Date the charter as a whole was last reconciled with evidence, not merely read. |
| responsibilities | Stable identifiers, each with an interview state of pending, in-progress, or complete. |

Do not put this block on the root README or the root agent instructions: the first is a public page that many hosts render literally, and the second is read as instructions. If the repository keeps its index inside the root instructions, put the marker on a short charter document linked from them. Everything else in the charter is ordinary Markdown in the body. The marker records provenance; the repository's guidance must remain understandable without this skill installed.

## Identify the responsibilities

Inspect before asking. Source, configuration, pipelines, schedules, credentials referenced, external services, and existing documentation usually reveal most responsibilities. Propose the list with the evidence for each entry and what you could not see.

A responsibility is an outcome the repository is accountable for in the world, such as "serves the public marketing site" or "creates, publishes, and adjusts paid advertising". Deployment, observability, and dependency maintenance are not responsibilities; they are concerns that each responsibility raises. A directory is not a responsibility either.

Confirm the list with the owner before going deep; it is the first charter decision. Order the interviews by what is at stake, with anything that spends money, acts on customers, or cannot be undone first. A large repository may nest: a responsibility's guide carries its own table in the same shape.

## Calibrate each responsibility with the owner

Before examining a responsibility's concerns, establish two things. Ask once per responsibility, not once per repository, since the answers often differ.

**Familiarity.** Where the owner holds settled, expert opinions, record them and ask little. Where the owner says they do not know the field, the interview is also how they learn what they might be missing; survey more widely and explain more.

**Ambition.** Offer a plain choice and record it:

| Level | Meaning |
| --- | --- |
| Starter | The least that makes the responsibility safe to operate and easy to improve later. |
| Proportionate | The practices that prevent most of the likely trouble for modest cost. The default when the owner has no preference. |
| Thorough | What a careful practitioner would expect where failure is expensive. |

Ambition changes how much you recommend, never whether a serious exposure is raised. At every level, name anything that can spend money, leak secrets or personal data, mislead customers, or cause loss that cannot be reversed. The owner may still decline it; record that decision like any other.

An owner without expertise tends to accept every recommendation, which produces guidance nobody maintains. Give each candidate its ongoing cost alongside its benefit, recommend against practices that exceed the chosen ambition, and say when the honest recommendation is to do nothing yet.

## Examine the concerns

For each responsibility, answer these questions from evidence first and bring the remainder to the owner. They are deliberately not specific to software.

| Concern | Question |
| --- | --- |
| Change | How does this get changed, by whom, and what review does a change receive? |
| Delivery | How does a change reach the place where it takes effect, and what triggers that? |
| Health | How would anyone know it is working, or that it has stopped? |
| Dependencies | What does it rely on that changes underneath it, and how is that tracked? |
| Exposure | What can it spend, damage, disclose, or commit the owner to? |
| Authority | Who decides, who may act without asking, and what requires approval? |

For a product these become release, deployment, observability, and dependency updates. For advertising they become campaign edits, publication, spend and performance monitoring, platform policy, budget limits, and approval of creative. Translate the questions into the field's own terms rather than forcing software vocabulary onto it.

Answer a concern once where responsibilities share it. Record a repository-wide default, such as one delivery pipeline, and let each responsibility inherit it or state its difference. Do not ask the same question three times.

## Research the field for candidates

When the owner lacks settled practice for a responsibility, find out what practitioners in that field treat as essential, common, and optional at the chosen ambition. Prefer authoritative and version-appropriate sources and link them. Where a fresh, delegated researcher is available and permitted, give it the responsibility, the evidence, and the ambition rather than your conclusions. Adopting the vocabulary of an expert is not a substitute for sources; label what rests on general knowledge alone.

Research produces candidates for the owner. It never produces guidance directly. Present a short ranked set per concern with a recommendation that is visibly yours. A wide survey is useful as interview material and harmful as a list of rules written into the repository.

## Record decisions, including refusals

Every candidate that was seriously considered ends in a recorded state:

| State | Meaning |
| --- | --- |
| Adopted | The owner chose it. Link the guide or procedure that carries it, or mark it not yet implemented. |
| Declined | The owner chose not to have it. Record why and what would change the answer. |
| Deferred | Wanted later. Record the condition or date for returning to it. |
| Open | Not yet decided. Dependent guidance stays provisional. |

A declined concern is a decision, not a gap. Recording it stops every later session from asking again and lets a future reader see that it was considered. Use the freshness fields in [project decisions and revalidation](project-decisions.md) for decisions that may stop holding. Never record owner approval that was not given.

Keep the record in the entry point's body as a table, with detail in the linked guides:

| Responsibility | Ambition | Read when | Guide | Concerns |
| --- | --- | --- | --- | --- |
| Marketing site | Starter | Changing public pages or their hosting | Site guide | Health declined: static pages, revisit if a form is added |
| Advertising | Thorough | Changing campaigns, budgets, or creative | Advertising guide | Exposure adopted: daily spend limit; authority adopted: owner approves new creative |

This example is a shape, not required columns. Omit what does not apply and never create an empty guide to fill a cell.

## Conduct and boundaries

Follow the interviewing conduct in [the owner interview skill](../../clny-interview-owner/SKILL.md): investigate facts before asking about them, prefer one consequential question at a time, reuse earlier answers, keep recommendations visibly yours, and end each turn in an explicit stopping state. Apply those rules to the charter instead of a product contract; do not restate them here.

A charter interview can be long. Update the marker and table as each responsibility completes so the work can stop and resume without loss. After a resumed session, re-read the charter rather than reconstructing it from memory.

The charter decides what the repository intends. It does not make changes. When the owner adopts something that does not yet exist, record it as adopted and not yet implemented, then hand the work to the change-scoped skills. Do not build it during curation, and do not describe it as present.
