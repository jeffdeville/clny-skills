# Consequential decisions

Use this contract in planning, implementation handoffs, and independent change review. Project engineering guidance owns concrete reflection triggers; discover its pointer through the engineering index or root instructions. Do not prescribe one technology-specific checklist for every project.

Record decisions whose rationale cannot be recovered easily from the resulting changes, especially meaningful tradeoffs, departures from established practice, uncertain assumptions, or constraints on future work. Ordinary local implementation choices need no diary entry. Missing project triggers do not exempt consequential choices from scrutiny; apply this general rule and identify the guidance gap without expanding into an unrelated overhaul.

## Minimal record

Keep a versioned decision log beside the initiative plan, accessible to a reviewer without the conversation. Each consequential entry states:

- Behavior or requirement served, distinguishing owner requirements from chosen mechanisms.
- Choice and the simpler credible alternative, including existing facilities inspected and source evidence.
- Why the choice is proportionate: concrete failure consequences, plausible frequency, detectability, recovery, and the obligations a future maintainer must understand.
- Assumptions, evidence limits, status, and conditions for reconsideration.

Scale entries to the choice. Do not invent estimates, numerical complexity scores, or universal reliability budgets. Explain cost and benefit concretely; asking whether the owner wants reliability conceals the tradeoff. An entry documents a choice, not approval or proof that it is justified. No special commit references or commit workflow are required.

## Reflection and escalation

During planning, compare the smallest complete flow with proposed additions. During implementation, consult project triggers when new evidence or a consequential departure appears. On first relevant use, check whether guidance is overdue or challenged and follow the [revalidation procedure](../../clny-configure/references/project-decisions.md) before treating it as settled justification. Investigate locally and choose simpler approaches that preserve the contract within delegated authority. Surface a concrete comparison before settling choices that materially change behavior, failure consequences, scope, or operational burden beyond that authority. Continue unaffected authorized work.

Update the human-facing proposal when structure changes; implementation detail must not quietly introduce a different design. Keep the decision log with the relevant changes. Project-specific triggers belong in project engineering guidance, not this shared contract.

## Independent review

Review implementation one PR or bounded increment at a time using clny-review-changes in a separate context. Supply contract and plan revisions, the decision log, project guidance, relevant source, and current base/head; do not rely on inherited conversation or coach the reviewer toward the author's conclusion. Review cumulative feature behavior and dependencies for stacks, not merely isolated diffs. If an independent context or skill is unavailable, label self-review and the outstanding independent review explicitly; do not claim equivalence or silently skip it.

Check necessity, reuse evidence, simpler alternatives, and the concrete maintenance obligations of the complete flow. A project trigger without a rationale warrants investigation; do not manufacture a defect from missing paperwork alone. Evidence may show a guidance rule itself needs revision or removal.
