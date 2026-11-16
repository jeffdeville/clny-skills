# Product contract and handoff formats

Use these shapes proportionally. A small change may fit in a paragraph. Keep one canonical document unless separate evidence material improves actual use. Omit empty categories; the deliverable is an agreement, not an interview transcript or implementation backlog.

## Durable product contract

Use [the shared intent contract](../../clny-infer-intent/references/intent-contract.md) as the canonical requirements for content, decision meaning, documentation obligations, persistence, and recipient access. An interview produces an instance with explicit decision and approval status. Include usefulness measures separately from delivery acceptance when relevant.

## Compact evolving view

During the interview, show intent, required behavior, preferences/delegation, significant evidence, remaining owner decisions, and exclusions as they become relevant. Add acceptance scenarios as commitments settle. Update material changes rather than reprinting the whole document.

## Example: convenience is not a requirement

Owner: "If an asset is deleted or renamed, I don't care what happens to its annotation. Keeping the rows sounded easier because we wouldn't need cleanup."

Record: "Annotation behavior after deletion or rename is delegated to engineering. Retaining rows was accepted as a possible simplification; automatic restoration is not required. Choose an approach consistent with the other requirements. Revisit only if investigation exposes material consequences outside that delegation."

Do not make disappearance, retention, or restoration mandatory acceptance scenarios from this answer. If an earlier draft calls restoration required, reconcile it explicitly with this clarification rather than silently preserving the stronger statement. Conversely, if the owner explicitly requires restoration, preserve it as a requirement even when expensive; evidence of cost can motivate a new decision, not erase the existing one.

## Example: conditional preference

Owner: "Keep this internal until we've learned from usage, unless that adds a lot of work."

Existing separate public/internal schemas and an exclusion test support honoring that preference. Cite them and retain the cost condition. Do not reopen the audience question unnecessarily, treat the preference as unconditional, or claim runtime exposure has been tested.

## Handoff to technical planning

Name the accessible contract path and exact revision, require reading it, and state approval and next-stage authority. Explain remaining investigations and the decisions delegated to the recipient. Link discovered project instructions and development, documentation, and validation guidance; make missing guidance visible without fabricating it.

The next stage determines implementation architecture, dependencies, reviewable increments, coding exemplars, documentation responsibilities, concrete validation procedures, and worker assignments. Product acceptance scenarios define what must hold; technical validation procedures define how to demonstrate it. Do not require a completed implementation design for product planning to finish.

Product planning is complete when no unresolved owner decision prevents technical planning. If feasibility uncertainty could overturn the core promise, hand off a bounded investigation with the question to resolve and the consequence of its answer. A complete contract can await approval; approval of the contract does not itself authorize implementation.

## Fresh-reader rehearsal

Give a fresh reader the candidate contract and relevant raw evidence without the interview transcript or expected answer. Ask:

- What outcomes must hold, and what is excluded?
- What may engineering choose or change, and what remains conditional?
- What evidence is established versus unverified?
- What discovery would require owner clarification?
- Can technical planning proceed, or is bounded feasibility investigation needed first?

Repair omissions using existing answers and evidence. Return only residual consequential choices to the owner. A rehearsal supports handoff clarity, not implementation correctness. If a fresh reader is unavailable, label the exercise a self-review.
