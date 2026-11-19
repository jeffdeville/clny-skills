---
name: clny-review-changes
description: Review an existing PR or proposed code change against established product requirements, repository guidance, documentation, and validation evidence. Does not implement fixes or publish review comments unless separately authorized. Change workflow, step 4: after a change exists.
metadata:
  version: "0.2.1"
  status: draft
---

# Review changes

**Where this fits.** Change workflow, step 4 of 4. Before: an implemented change or PR. If its requirements are unclear, go back to `clny-infer-intent` and resume here. Findings about guidance or the charter go to `clny-configure`.

Understand the requirement before judging whether a change satisfies it. Assess actual behavior and evidence, not only the diff's style or the author's stated solution.

## Establish scope and intent

Read the request, PR description, linked requirements, current diff/base/head, existing review context, root instructions, README, and affected guidance. Note the reviewed revisions. Use available repository tools; report missing repositories or access. Review authorization does not itself authorize code edits, external comments, approval, or merge.

Read [the shared intent contract](../clny-infer-intent/references/intent-contract.md). Check whether linked requirements establish applicable intent, decision authority, and coverage of the actual change. If adequate, proceed without another interview or separate intent document.

If intent is missing or disputed, use `clny-infer-intent` to investigate existing evidence. It frames unresolved questions; `clny-plan-requirements` handles remaining product decisions. Carry forward context and resume review after resolution. Continue independent technical checks where useful, but do not declare requirement alignment settled while consequential intent is unknown. Do not treat an author's implementation or tests as approval of new behavior.

## Review implementation against the promise

Trace representative required behavior through the affected callers, callees, persistence, and user-visible boundaries, including other repositories when necessary. Identify scope drift, missing outcomes, broken preserved behavior, and violations of project invariants. Select consequential failure, permission, lifecycle, and compatibility cases from the actual change rather than applying unrelated exhaustive checklists.

Inspect tests and perform proportionate authorized targeted checks using discovered project procedures. Separate checks read, checks run, author-reported results, and unverified runtime claims. For a defect, assess whether regression evidence exercises the original failure and preserves working controls. A green test suite does not establish all required behavior.

For stateful changes, review migration/release ordering and recovery of already-affected data. Read applicable PR templates and deployment guidance. Do not assume a future run refreshes data without checking relevant caches and skip conditions. Report environmental or pre-existing failures accurately; neither silently excuse them nor attribute them to the change without evidence.

## Challenge necessity and guidance

Read [the decision-record contract](../clny-plan-implementation/references/decision-records.md) and the initiative's plan and decision log. Discover project-owned reflection triggers through the engineering map. Review implemented changes, not standalone implementation plans; planning owns its pre-code assessment.

Verify claimed reuse investigations against source. Distinguish owner requirements from implementer mechanisms, assess simpler alternatives, and name concrete maintenance obligations across the cumulative feature or stack. Investigate triggered choices without rationale; do not invent findings merely to fill a checklist. A documented rationale is evidence to challenge, not approval.

Check whether applicable guidance is overdue or challenged and whether its reassessment used actual evidence. Use [the revalidation procedure](../clny-configure/references/project-decisions.md); in read-only review report required corrections without writing them. Guidance compliance is not sufficient when the rule itself appears inappropriate. Separate implementation defects, missing justification, and proposed guidance corrections. State limits when plan, history, or other repositories are inaccessible.

## Reconcile documentation explicitly

Review relevant inline comments/docstrings, component documentation, architectural explanations, and validation instructions against the actual diff and established intent. Name the locations reviewed. Require updates when changed behavior makes them wrong or materially incomplete. Historical ADRs alone are insufficient. Accept a concrete no-edit rationale when existing explanations remain sufficient; never require cosmetic churn.

Treat a consequential documentation discrepancy as a review finding. So is a change that gives the repository a responsibility its charter does not record, or that contradicts a recorded charter decision; report it for reconciliation through `clny-configure`. Do not declare a change ready with such discrepancies unresolved. During read-only review, describe the correction; do not edit documentation implicitly.

## Report actionable findings and readiness

Lead with concrete findings prioritized by consequence. Each finding identifies the affected location, triggering scenario, expected behavior and basis, actual consequence, and evidence. Distinguish defects from uncertainty, missing validation, and optional suggestions. Avoid invented findings and restating issues already resolved in the reviewed revision.

Report requirement alignment, implementation validation, documentation reconciliation, and material release/recovery limits. A clean review means no actionable findings within the stated scope and evidence, not proof of production behavior. A review of a new head must reconcile changed code and prior findings before reusing old conclusions. Do not publish or approve a PR unless the user authorized that external action.
