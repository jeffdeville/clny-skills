# Project decision rehearsal results — 2026-11-17

Skill names in this record follow the 2026-11-19 renames; the runs used the earlier names clny-revise-guidance and clny-interview-owner.

## Scope and method

Codex desktop, independent agent contexts; exact model identifier was not exposed in the evaluation output. Candidate revision: branch codex/project-decision-guidance based on 865fe9974cceccc3ab3f7df4eb38996611d717b4, with the changes in this PR. This is a limited synthetic rehearsal, not a production-project trial or cross-client certification.

One fresh agent received the three scenarios in [project-decisions.md](project-decisions.md), the candidate skill paths, and read-only/no-network limits. Expected outcomes and the implementation conversation were withheld. The three scenarios shared that evaluator context; they were not three separately isolated runs. A second independent agent reviewed the skill diff using clny-review-changes and the agreed requirements. No application changes, live services, external publication, or runtime behavior were part of either exercise.

## Observed behavior

| Scenario | Actual outcome | Limit |
| --- | --- | --- |
| Changed upstream capability | Identified the overdue recommendation and September dependency upgrade; rejected repeated compliance as validation; proposed correcting the capability explanation while leaving local replacement unresolved. Preserved the original validation date for the unsupported adapter choice. | Relied on supplied release evidence; no real source/history or accessibility checks. |
| Small frontend change | Proposed controlled sorting with local ownership; exposed the global store/wrapper as unjustified additions; described maintenance obligations and required source investigation, decision records, documentation, and independent review. | Explicitly labeled the proposal non-execution-ready without concrete repository paths and checks. |
| Infrastructure precedent | Distinguished unsupported convention from confirmed operational defect; compared reuse against duplication and state/address churn; requested evidence without requiring unrelated refactoring. | No actual Terraform diff or plan; did not claim runtime correctness. |

The independent diff review found a routing gap: a rule could become overdue after planning, but implementation was not explicitly named in freshness discovery. The fix added implementation to the reassessment procedure, linked that procedure from the decision-record contract, and carried the obligation into the implementation handoff. The reviewer rechecked the fix and reported no remaining actionable findings within scope.

## Structural checks and remaining trial

All five skills passed the skill-creator frontmatter validator. Relative Markdown file targets and prohibited-character checks passed; git diff --check passed. These checks do not establish behavioral reliability. No new diagrams were introduced.

The broader existing behavioral suite and Claude Code were not rerun. Reloading the approved skills and testing them on the original project remains a separate, explicitly deferred trial.
