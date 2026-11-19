---
name: clny-plan-implementation
description: >-
  Use when a product contract or agreed feature direction needs a repository-grounded implementation plan with reviewable increments, bounded agent assignments, documentation responsibilities, and validation procedures. Not for the initial product interview, implementing the plan, or a general documentation overhaul. Change workflow, step 3: after requirements are established and before implementation and clny-review-changes.
metadata:
  version: "0.3.0"
  status: "draft"
---

# Plan implementation

**Where this fits.** Change workflow, step 3 of 4. Before: established requirements, from `clny-plan-requirements`, `clny-find-requirements`, or an adequate existing document. Next: implementation, which has no skill of its own, then `clny-review-changes` for each increment.

Turn a versioned product contract and repository engineering guidance into a canonical delivery plan a fresh implementer can use. Settle ordinary technical decisions through evidence. Preserve product commitments and delegated discretion. Specify enough to coordinate outcomes, boundaries, interfaces, and verification without prescribing every coding move.

## Establish input and authority

Read the established intent record or canonical product contract and its exact revision, approval status, rationale, evidence, exclusions, conditional preferences, and delegated choices. A contract produced by `clny-plan-requirements` is a suitable input, but that skill is not required. Use equivalent supplied direction; do not rerun a settled product interview. If a missing decision blocks a consequential design choice, investigate what evidence can settle before asking the owner.

Record the authorized stage. Planning, saving a plan, approving product behavior, implementing, and deploying are distinct actions. Continue all useful authorized planning; do not dispatch implementation workers or change application behavior merely because the plan is ready. Preserve explicit read-only boundaries. A later "proceed" continues the authorized stage unless the user clearly expands it.

Read [the shared intent contract](../clny-find-requirements/references/intent-contract.md). Established intent may come from an interview or evidence-based investigation. A ticket labeled Bug is not an accepted requirement. Use `clny-find-requirements` for unresolved factual intent and `clny-plan-requirements` for residual product choices; reuse adequate prior work.

Inspect existing branches, PRs, reviews, and reported checks when supplied. Plan remaining work rather than duplicating existing implementations. Verify their relevance to current source and distinguish reported historical checks from current evidence.

## Find and apply project guidance

Read root instructions and README. Locate the engineering entry point named in root `AGENTS.md` or equivalent instructions; read its root architecture guidance and follow relevant component, coding, documentation, and validation links. Repeat this discovery in each affected repository, including scoped instructions. If the repository's charter marker names a suite version different from this skill's, follow "When versions differ" in [the suite changelog](../clny-configure/references/changelog.md).

Do not assume a fixed path. If the index is missing, inspect existing authoritative guidance and make its location or curation a bounded prerequisite. Apply the `clny-configure` rubric when available. Its essential checks are discoverability, authority, architectural fidelity, local usefulness, validation usefulness, change coherence, maintainability, and recipient accessibility. Responsibility coverage belongs to curation: a missing or unfinished repository charter is a gap to report, practices marked tolerated or unexamined are not exemplars, and a change that would add a responsibility or contradict a recorded charter decision needs that decision reconciled before dependent design is treated as settled. A substantial handbook overhaul is explicit prerequisite work, not an implicit expansion of this task. Resolve small factual gaps within scope; surface material contradictions.

Inspect the surrounding source, configuration, tests, and actual callers/callees. Trace a representative behavior across the necessary boundaries and repositories. Select concrete coding and test exemplars that fit the approved architecture; a legacy violation is not a convention to copy. Separate observed implementation, approved architectural intent, deviations, and proposed changes. Do not silently weaken an architectural rule to match current code.

## Make technical decisions with evidence

Evaluate the contract's candidate approaches; they are not binding unless the owner made them commitments. Choose ordinary mechanisms using project conventions and proportionate investigation. Explain consequential choices with their evidence, rationale, and limitations. Reuse established interfaces where they fit; label proposed interfaces as new work.

| Discovery | Response |
| --- | --- |
| Fact available from source, configuration, or permitted checks | Investigate and update the plan. Source inspection is not runtime verification. |
| Choice within delegated engineering discretion | Decide and record the rationale; leave local details to the implementer where coordination does not require a decision. |
| Shared interface or cross-task dependency | Coordinate ownership and ordering in the plan; do not send the owner ordinary engineering questions. |
| Ambiguous required behavior, changed product promise, architecture exception, or material cost/scope trade-off outside delegated authority | Explain evidence, consequence, alternatives, and recommendation; ask the smallest owner question before dependent design is treated as settled. |
| Unverified capability | Define a bounded investigation with the question, evidence needed, and dependent work; continue independent planning. |

Preserve "I don't care" as delegation. Do not convert a convenient implementation behavior into product acceptance. Conversely, technical expense does not erase a required outcome. Keep conditional preferences conditional; revisit only when their condition or the limits of delegated discretion require it. Distinguish a chosen engineering invariant from an owner requirement so future changes use the right decision authority.

## Make consequential choices visible

Read [the decision-record contract](references/decision-records.md). Discover project-owned reflection triggers and assess applicable overdue or challenged guidance through [the revalidation procedure](../clny-configure/references/project-decisions.md). Keep implementation mechanisms distinct from owner requirements. Compare the smallest complete design with proposed additions, describing concrete maintenance obligations and failure tradeoffs rather than abstract reliability preferences.

Expose every consequential structural addition in the human-facing proposal. Record significant choices and reuse evidence beside the plan; do not bury new architecture in assignments. Resolve ordinary choices independently, and bring only residual consequential tradeoffs outside delegated authority to the owner.

## Plan reviewable delivery

Read [the plan and assignment contract](references/plan-and-assignments.md) before consolidating. Scale the plan to the work: a small change can have one increment and one implementer. Prefer an early integrated demonstration of a meaningful behavior across the relevant boundaries, then expand coverage. Necessary foundations are valid increments, but name what they enable and what they do not yet prove. Avoid deferring all integration evidence until the end.

Give each increment an observable outcome, dependencies, bounded responsibilities, applicable guidance and exemplars, documentation impact, and completion evidence. Include shared interface ownership and sequencing where workers could otherwise conflict. Distinguish implementation dependencies from merge, migration, release, or deployment dependencies when relevant. Record rollback and compatibility work when the change actually requires it; do not invent release machinery for a trivial edit.

Turn product acceptance into concrete validation routes using project guidance. Identify prerequisites, procedures or commands, working directories, expected observations, and limits. Separate existing runnable checks from tests or procedures to be authored. Missing commands become explicit work; never present guessed commands as verified. Honor targeted testing policies. A green unit test does not establish an integrated user outcome, runtime permissions, or performance.

Documentation is part of each affected increment. Identify the authoritative component guides, architecture explanations, validation procedures, and navigation that may need updates. Planned behavior stays labeled proposed until implemented. Require implementers to review actual documentation impact; a no-change conclusion can be justified. Do not postpone all documentation to a final cleanup phase or mandate a new guide for every changed folder.

## Plan correction evidence and recovery

For a confirmed defect, plan a regression check that fails on the affected baseline and passes with the fix where feasible; state limits when that comparison is unavailable. Cover the reported symptom, working controls, affected permissions and boundaries, and an integrated outcome proportional to risk. Do not manufacture an exhaustive matrix unrelated to the failure.

Distinguish preventing future failures from repairing existing effects. Establish whether replay, cache invalidation, re-ingestion, migration, or backfill is needed; verify relevant skip conditions before promising that the next run repairs data. Preserve explicit exclusions and separate implementation, merge, migration, deployment, and recovery dependencies. Read applicable PR templates and release guidance before deciding sequencing.

Explicitly include inline documentation review in each affected increment. Completion requires documentation reconciliation under the shared intent contract, including a reasoned no-edit conclusion when appropriate.

## Consolidate and check readiness

Maintain one canonical implementation plan in the project's existing planning location, with its own revision and a binding to the product contract revision. Save within authorized scope; verify links, recipient access, and ignore/worktree constraints. Supply accessible copies with canonical origin when needed. Do not claim local ignored files will reach another checkout. If saving is explicitly forbidden, deliver a clearly labeled chat proposal and identify persistence needed before formal handoff.

Check every required outcome has planned completion evidence and every proposed assignment has clear authority, dependencies, and pause conditions. Distinguish ready assignments from ones gated by owner decisions, feasibility, or access. Do not mark the whole feature ready just because one investigation is executable. When useful and permitted, rehearse one consequential brief with a fresh reader using the plan and source evidence, not the interview transcript or expected answer. Otherwise label a self-review.

Report completed planning work, evidence established, open decisions or gates, canonical location and revision, and next-stage authority. Routine progress checkpoints do not require user approval. Keep planning until requested scope is complete, a consequential owner decision is needed, or evidence/access blocks remaining work. On contract revisions or resumed sessions, re-read canonical documents and reconcile affected decisions, assignments, and acceptance evidence before continuing.

## Implementation handoff obligations

Require the implementer to read accessible contract and plan revisions plus applicable project guidance before acting. Its future execution cycle is: inspect current context, implement one bounded increment, validate behavior, reconcile affected documentation and consequential decision records, obtain independent clny-review-changes review for the bounded increment or PR before treating it as ready, report evidence and remaining limitations, and continue within authorization. Report discrete outcomes rather than files touched alone. Pause only work dependent on an unresolved consequential decision; keep independent authorized work moving. Code complete, integration verified, deployed, and rollout complete are separate claims.

The handoff must include the project reflection-guidance pointer, the decision-record contract, and the obligation to reassess overdue or challenged guidance on first relevant use during implementation. Carry its independent-review checkpoint into the project workflow guidance when authorized, so execution does not depend on remembering this conversation. Review cumulative stack behavior; resolve findings before advancing dependent work. Do not add a separate coding skill or special commit metadata.
