---
name: clny-revise-guidance
description: Use when establishing, auditing, or maintaining a repository's guidance hierarchy, including the charter of what the repository is responsible for, its entry point, architecture rules, component guides, and validation instructions, or reconciling that guidance with a proposed or completed change. Interviews the owner about the repository's standing responsibilities. Not for interviews about a specific change, implementation task decomposition, or changing application behavior.
metadata:
  version: "0.3.0"
  status: "draft"
---

# Revise guidance

Make repository guidance discoverable, coherent, and trustworthy for a fresh planner or implementer. Produce a maintained map of authoritative explanations, not a duplicate manual or a README in every directory.

## Start from the repository's responsibilities

Guidance follows from what the repository is accountable for. Look for the charter marker on the engineering entry point to learn the charter's state; do not ask the user whether the setup is new. When establishing guidance, when the owner asks to resume or revisit the charter, or when a change adds, alters, or contradicts a recorded responsibility, read [the repository charter](references/repository-charter.md) and establish or reconcile the affected responsibilities with the owner, one at a time, calibrated to the owner's familiarity and ambition. A recorded and consistent charter needs no interview.

A missing or unfinished charter does not widen a narrower request. When maintaining guidance with a change, or auditing, report the charter's state as a gap and continue the requested work.

The architecture, component, and validation topics below are what software responsibilities usually need. Apply the charter's concerns to other kinds of work in that work's own terms; do not force software headings onto them or skip a responsibility because it is not code.

## Choose the scope

- **Map and establish:** inventory existing guidance and representative implementation paths; connect useful material and fill consequential gaps.
- **Maintain with a change:** trace a proposed or completed change to the explanations, constraints, procedures, and navigation it affects. Keep unrelated documentation out of scope.
- **Audit only:** report findings and concrete corrections without writing files.

Honor the requested mode and repository boundaries. A charter decision to adopt a practice does not implement it; building it is a new change request for `clny-interview-owner` or `clny-plan-implementation`. Documentation work does not authorize code changes, architecture policy changes, runtime operations, commits, or publication. Reversible documentation edits within the requested scope do not require repeated approval.

Read root instructions and README first. Locate the existing engineering entry point and scoped instructions. Read [the documentation contract and rubric](references/contract-and-rubric.md). Use concise overviews, ownership maps, focused component explanations, and link/diagram checks. Repositories must not depend on a personal skill installation to understand their own rules.

## Establish a discoverable map

Use the engineering entry point identified in root `AGENTS.md` or the repository's equivalent agent instructions. Preserve an existing authoritative location. If none exists, choose a tracked location consistent with repository conventions; `docs/engineering/README.md` is a default, not a mandatory path. Link it from root instructions and the root README when appropriate and authorized. Check ignore rules and reader accessibility before claiming the guidance is distributed.

Keep the index mainly a table of contents with purpose, component responsibilities, and when each link applies. Charter decisions appear there as one-line summaries linking to their guides. Include or link root architecture guidance. Link substantive component guides near their owning code and cross-cutting practices where they are already maintained. Include a return route from focused guides. Do not duplicate policies, replace the root setup guide with an index, or introduce empty pages just to satisfy a schema.

Follow enough source, configuration, tests, and existing decisions to understand the relevant ownership and behavior. For a broad map, sample meaningful paths and state coverage limits; do not imply every component was audited. Link evidence that helps readers verify consequential claims.

## Preserve authority while reconciling facts

Separate current implementation, approved architectural intent, known deviations, and proposed changes. Existing code establishes what happens, not automatically what should happen. A design proposal or historical plan is not approved guidance merely because it is detailed.

Correct inaccurate descriptions using evidence. When implementation violates an approved rule, document the observed deviation and link its evidence without weakening the rule or silently blessing an exception. If authoritative sources conflict, investigate their scope, dates, and decision provenance. Ask for a decision only when the conflict remains material; complete unaffected curation first. Do not invent owners or approval history.

Keep required constraints, recommendations, conditional preferences, and delegated choices distinguishable. Preserve rationale that helps a future engineer apply a rule. Avoid turning a convenient local pattern into a universal architectural mandate.

## Establish and reassess project decisions

Read [project decisions and revalidation](references/project-decisions.md) when establishing reflection triggers or assessing overdue, challenged, or change-sensitive project guidance. Keep concrete triggers project-owned and discoverable through the engineering map. Distinguish observed patterns from justified conventions. Assess relevant changes since last validation; following a rule does not renew its evidence. Preserve mandatory constraints while unresolved and propose corrections within authority.

## Maintain explanations with the change

Apply [the shared documentation obligation](../clny-infer-intent/references/intent-contract.md). Explicitly inspect inline comments and docstrings as well as guides. A change cannot be considered ready with inaccurate or materially incomplete affected explanations. ADRs supplement the maintained current account; they do not replace it.


For each affected behavior or boundary, identify the authoritative guide and the incoming links that help readers find it. Update component responsibilities, interfaces, invariants, error/recovery behavior, development procedures, and validation guidance where the change makes them inaccurate. Revisit the parent map when ownership or flow changes. A change that adds a responsibility or contradicts a recorded charter decision is a guidance finding: reconcile that responsibility with the owner rather than documenting it as settled. A folder edit does not by itself require a documentation edit; explain no-impact conclusions briefly.

For proposed changes, label documentation proposals and planned behavior. For completed changes, describe what the source establishes and distinguish deployment or runtime claims that remain unverified. Preserve historical decisions as history while updating the current authoritative account and repairing navigation.

Document missing validation as a specific gap: which behavior cannot yet be demonstrated, what prerequisite or procedure is missing, and where that procedure belongs. Discover commands from project guidance and configuration rather than inventing them. Running a documented check requires the same environment and authority as running it directly; prefer safe targeted checks and respect repository restrictions.

## Verify and hand off

Review the scoped result against the rubric. Check relative paths, heading anchors, incoming links after moves, and consistency of diagrams with the described flow. Render changed diagrams when tooling is available; state when rendering remains unverified. Distinguish commands inspected from commands run and record actual results.

For significant structural work, use a fresh-reader navigation rehearsal when available and permitted: provide the entry point and a realistic change, then ask which guidance applies and how to validate it. Otherwise label the exercise a self-review.

Return the canonical entry point, the charter state with any responsibilities not yet complete and concerns still open, what was established or changed, material discrepancies, validation performed, and remaining gaps. For an audit, return a prioritized set of corrections with locations. For implementation planning, provide applicable source links and documentation/validation obligations; the planner owns delivery increments and assignments. Routine implementers can apply the same maintenance rubric without a separate curation pass.
