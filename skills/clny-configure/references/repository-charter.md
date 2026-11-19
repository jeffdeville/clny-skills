# Repository charter

Read when establishing guidance for a repository, when resuming or revisiting its charter, when the charter marker's version differs from this skill's, or when a change adds, alters, or contradicts a recorded responsibility.

A repository is defined by the business functions it carries, not by a project type or its modules. One repository may exist only so that people can book time with its owner. Another may hold a product, the marketing site that sells it, and the advertising that brings people to that site. The charter records those responsibilities and the owner's standing decisions about each. It is the repository's account of its own intent; it is not a product contract for a change.

## Read the state; do not ask for it

Never require the user to say whether this is a new setup or an update. Find the charter marker and compare the recorded charter with the evidence. New and update are one procedure: interview only on the difference.

| Observed state | In map-and-establish scope, or when the owner asks |
| --- | --- |
| No marker | Treat the charter as empty and establish it. Existing guidance is evidence, not an obstacle. |
| Marker present without a version | First configuration is underway. Resume from the saved decisions and check the installed release criteria before recording a version. |
| Responsibilities pending or in progress | Resume them; do not restart completed ones. |
| Evidence shows an unrecorded or changed responsibility | Reconcile that responsibility only. |
| Complete and consistent | Proceed with the requested curation. Reopen a decision only when the owner asks or its revisit condition has arrived. |
| Marker version older than this skill's | Read [the suite changelog](changelog.md). For each entry after the marker's version, check its acceptance criteria against the repository and interview only on those that fail. Record the new version when all are met. |
| Marker version newer than this skill's | Do not downgrade or rewrite it. Report that the installed skills are older and work within what you can read. |

Check for a newer marker before applying any other row or editing charter data. Follow [the suite changelog](changelog.md) for that case.

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
    - id: product
      interview: complete
    - id: marketing
      interview: in-progress
    - id: advertising
      interview: pending
---
```

| Field | Meaning |
| --- | --- |
| version | The suite version, from this skill's frontmatter, that the charter last satisfied. Omit until the first release criteria are satisfied. Retain the last satisfied version during a later migration. |
| reviewed | Date the whole charter was last reconciled with evidence. Omit until the first whole-charter reconciliation. Retain the previous date during partial work. |
| responsibilities | Stable identifiers with an interview state. Use pending until the interview starts. Once started, use in-progress while any concern lacks a state or is open. Use complete only when every concern is adopted, declined, or deferred, directly or through a recorded default. A completed responsibility that evidence reopens returns to in progress. |

The marker and the responsibilities table live together on the engineering entry point. Merge the key into any front matter already there. Keep both off the root README, which is the repository's public page, and off the root agent instructions, which are read as instructions. When the index lives inside the root instructions, put the marker and table on a short charter document linked from them, and follow that link when reading the state. Where a small repository has no agent instructions, a pointer from the root README is enough; do not create an instruction file only to hold a pointer. In such a repository one short guidance document is the entry point, the charter, and the guide together.

Once the owner confirms the list, write the clny_guidance mapping with the responsibilities list and every interview pending. Omit both milestone fields. Set reviewed when reconciliation of the whole charter against evidence finishes. Set version when the repository meets the applicable release criteria. Save interview progress even when neither milestone advances. The marker records provenance; the repository's guidance must remain understandable without this skill installed.

## Scan before interviewing

The scan is its own step with its own product: a skeleton that says what each part of the repository is for. Do it before the interview and write it down as you go, so that it survives a long session.

**Coverage means accounting, not reading.** Every top-level area, and every part beneath it that has its own purpose, is listed and traced to the responsibility it serves, or raised with the owner because it serves none. Nothing is silently left out. Generated, vendored, and lock files are named and skipped.

**Use the cheapest reliable evidence.** Agent instructions, READMEs, manifests, build and pipeline definitions, directory and file names, and a symbol index or language server where one is available will usually say what a part is for without opening its files. Shortcuts and heuristics are expected. Reading every file is not the goal and is not asked.

**Check that the shortcut holds.** Documents are claims. Before relying on one, test it cheaply: do the paths, commands, and components it names exist, and does it predate large changes to what it describes? Where a document passes, trust it for that area. Where it fails, or where an area has no description at all, look inside that area only as far as needed to say what it is for. Record for each area what the account rests on: a current document, names and manifests, or the source itself.

**Depth.** Work breadth-first from the root, and let what the root shows decide how to divide the rest. Go deeper only where a directory mixes purposes or its description failed the check. Where fresh delegated contexts are available and permitted, give each a subtree and merge their accounts; otherwise work through the subtrees in turn.

**Product.** The skeleton is the component map the entry point already requires, or a document linked from it in a large repository: each part, what it is for, the responsibility it serves, and the guide that explains it, or that no guide exists yet. It is the route from any file to the guidance that governs it.

This scan does not write the detailed guidance for each part. That deeper pass is separate: the owner may ask for it for an area, and otherwise it happens when a change first touches a part whose guide is missing or stale, as prerequisite work for that change. The map is what makes the gap visible at that moment.

The scan separates two kinds of evidence, and they have different defaults.

*Stated rules* are what the owner has written down as intent. A sentence is a stated rule only when all three hold: the owner or someone acting for them wrote it, it is phrased as an instruction or a decision, and it sits in a file meant to instruct, such as agent instructions, a decision record, or a policy. Treat stated rules as binding and confirm them with the owner in one batch, grouped by topic rather than listed sentence by sentence.

Everything else written in the repository is a description. A README line saying what a script does is a claim to check against the code, not a rule. Text a tool generated is not the owner's intent. A promise made to the public, such as a privacy policy, is a finding for the Promises concern. Two stated rules that contradict each other are a gap to bring to the owner; neither binds until the owner says which holds.

*Observed practices* are what the code and configuration actually do. They show what exists, not what is wanted; long-lived repositories accumulate practices nobody chose. Give each one that bears on a concern a standing, and never promote it on your own:

| Standing | Meaning |
| --- | --- |
| Endorsed | In place, and the owner stands behind it. Others may follow it. |
| Tolerated | In place and known not to be well. Do not copy it as an example, and do not fix it unasked. Record what is wrong as the owner describes it. |
| Unexamined | Found by the scan; the owner has not spoken to it. The default. Not a precedent. |

The interview's main work is the gap between what is and what is wanted. Bring the owner every place where a stated rule contradicts the code, where documents contradict each other, where a path appears dormant, and where one term is used for several things. Record which account is current, and what the owner's terms mean, at the entry point.

Record the current state truthfully, including a migration that is half done and an old path that is still live. The charter does not track the plan for finishing it; the owner reconfigures when the state changes. Deciding how to repair a tolerated practice is not this interview's work; representing it accurately is.

Record standings where the practice lives: in the guide beside the owning code when one exists, and otherwise in that part's row of the component map, moving to the guide when one is written. Let the charter link there. Classify what bears on a concern or what a planner would be likely to copy; leave the rest unexamined and say that it is.

**Existing documents.** The skills can only use what is where they look. When an existing document already answers a concern in a readable form at a stable location, link it. When it does not, restructure it into the guidance by moving it and leaving a pointer behind. Never keep a second copy; two authorities drift apart.

## Identify the responsibilities

Propose the list from the scan, with the evidence for each entry and what you could not see.

A responsibility is a business function the repository carries, stated as who it is for and what it does for them. The test is the department: imagine the owner's work as a company of about fifty people, and ask whether two things would sit in different departments. Product, marketing, sales, and advertising are different responsibilities even when one exists to feed another. If the department picture does not fit, ask whether the owner would name it as a separate role.

Work that any one department would do for itself belongs to that responsibility. Deploying a product, backing it up, and monitoring it are parts of the product. A module, a directory, or a risk surface is not a responsibility. Most repositories carry one to four.

Confirming the list is the first charter decision and its own question. Show the scan's summary with it, and ask for each responsibility's ambition in the same step, so the owner chooses a level knowing what was found. Do not put concern-level questions to the owner before the list is answered. State a serious exposure as soon as you find it rather than holding it until its turn. Order the interviews by what is at stake, with anything that spends money, acts on customers, or cannot be undone first.

When a change has already landed work the charter does not cover, ask whether it belongs to a recorded responsibility or is a new one the owner intends the repository to carry. How it should behave is a question for the change-scoped skills.

## Ambition

The owner chooses one level per responsibility, after seeing the scan's summary.

| Level | Meaning |
| --- | --- |
| Starter | The minimum viable set: enough to operate safely and improve later. |
| Proportionate | The 80/20 set: the few practices that prevent most of the likely trouble. |
| Thorough | More practices are adopted, either because the work deserves expert-level attention or because it must pass substantial validation before it is approved for release. |

Ambition is the only calibration. Conduct the same interview whoever the owner is; do not shorten it or widen it by guessing at their expertise. Ambition changes how many practices you recommend, never whether a serious exposure is raised. Always name anything that can spend money, leak secrets or personal data, mislead customers, or cause loss that cannot be reversed. The owner may still decline to act on it; record that like any other decision.

Give every candidate its ongoing cost alongside its benefit, recommend against practices that exceed the chosen ambition, and say when the honest recommendation is to do nothing yet.

## Examine the concerns

For each responsibility, go through every concern. Bring the scan's answer to each as a finding for the owner to confirm, correct, or give a standing, and ask where the scan found nothing. They are deliberately not specific to software.

| Concern | Question |
| --- | --- |
| Promises | What have the people who rely on this been told, and what will it deliberately not do? |
| Change | How does this get changed, who decides, what review does a change receive, and what may agents or automation do without asking? |
| Verification | How is a change known to be correct before it takes effect, and what can only be checked by hand? |
| Delivery | How does a change reach the place where it takes effect, and what triggers that? |
| Health | How would anyone know it is working, or that it has stopped? |
| State | What does it hold that must survive, and how is that backed up, restored, retained, and deleted? |
| Dependencies | What does it rely on that changes underneath it, what do those parties require of it, and how is that tracked? |
| Exposure | What can it spend, and what harm could it do that cannot be undone? |

Promises covers scope, invariants, compatibility, service level, and commitments made in public. A complete list of non-goals would be endless, so record only the tempting ones: those the owner has already written down, and those a reasonable contributor or agent would otherwise drift into. Ask what the owner would reject if it were proposed, offer a few candidates from adjacent features, and keep a handful with reasons. Dependencies includes outside obligations such as licences, platform terms, and regulation. Exposure is deliberately narrow: what the responsibility holds belongs under State, what others require of it under Dependencies, and what it has told people under Promises. Do not repeat those answers under Exposure.

Translate each question into the field's own terms. For a hosted product they become compatibility and service level, review and release, tests and manual checks, deployment, monitoring, backups, upstream updates, and spending or irreversible loss. For advertising they become claims made to audiences, campaign edits and approval, publication, performance monitoring, audience data, platform policy, and budget limits.

One responsibility often has several parts under one concern. Give one answer that names them; a product's exposure may cover the access it holds, its backups, and what its public pages promise. Parts are not further responsibilities. Where responsibilities share an answer, such as one delivery pipeline, record it once and let the other refer to it.

These concerns were revised after two trials on four repositories with the owner absent. The interview itself has not been tested.

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
| Product: customers run their reports | Thorough | Changing the application, its data, or its hosting | Product guide | State open: no restore has been tested. Delivery tolerated: see guide. |
| Marketing: visitors learn what it does and sign up | Starter | Changing public pages or the sign-up form | Site guide | Health declined: static pages, revisit if the form changes. |
| Advertising: the right people reach the site | Proportionate | Changing campaigns, budgets, or creative | Advertising guide | Exposure adopted: daily spend limit. Change open. |

This is a shape, not required columns. The decisions cell is a one-line summary: always show open concerns, declined concerns, tolerated practices, and exposures; the rest may live in the guide or the repository default. A revisit condition in the cell is sufficient for most decisions. Use the full freshness fields in [project decisions and revalidation](project-decisions.md) only for consequential, change-sensitive ones. That register holds technical conventions and reflection triggers; the charter holds decisions about responsibilities. Link between them rather than recording a decision twice. Never create an empty guide to fill a cell.

Update the table and interview state after each concern, including an open one, so a long interview can stop and resume without loss.

## Conduct and boundaries

Conduct the interview as described under "Investigate consequential uncertainty", "Revise and continue", and "Make every yield explicit" in [the requirements planning skill](../../clny-plan-requirements/SKILL.md), reading "charter" where they say plan or contract. Its product-contract and handoff material does not apply.

The charter decides what the repository intends; it does not make changes. When the owner adopts something that does not yet exist, record it as adopted and not yet implemented. Building it is a new change request: `clny-plan-requirements` when product decisions remain, otherwise `clny-plan-implementation` with the charter entry as its evidence of intent. Do not build it during curation or describe it as present.
