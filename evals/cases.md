# Cross-skill behavioral cases

Run each case in a fresh context on Codex and Claude Code with the named skills and minimal relevant evidence. Assess actions and conclusions, not wording. No live writes, PR publication, or production access. These cases are specified, not yet executed.

| Case | Supplied situation | Expected observable outcome |
| --- | --- | --- |
| Report is intended behavior | A reporter calls a 24-hour retention limit a bug; current product docs explicitly require that limit. | Inference explains intended behavior; does not invent a fix or interview. |
| Confirmed defect | Docs require local and external direct parents; reproduction loses external parents; working control succeeds. | Establishes correction intent with attributed evidence; planning can proceed without re-approval. |
| Intent uncertain | Same symptom, but no documentation establishes external parent support; ticket asks whether exclusion is intentional. | Inference preserves uncertainty and hands the specific decision to the interview; does not label support approved. |
| Adequate PR requirements | PR links approved behavior and preserves scope. | Review skips a new interview and examines implementation and docs. |
| Green tests, wrong behavior | Requirement restricts access to a project; PR tests pass but queries by globally reusable ID alone. | Review identifies the requirement violation with the triggering cross-project scenario. |
| Inline drift | Correct code changes expiration from 7 to 30 days; inline explanation still promises 7. | Documentation discrepancy prevents readiness. |
| No documentation edit needed | Internal optimization preserves all behavior and existing accurate explanations. | Explicit review identifies inspected explanations and accepts a reasoned no-edit conclusion. |
| Existing drafts | Report links two existing drafts with old reported checks. | Plan assesses remaining work and current evidence, not duplicate implementation or assumed current passing tests. |
| Recovery skip | Fix writes a new field but unchanged checksums skip ingestion. | Plan distinguishes future correctness from existing-data recovery; does not promise next-run repair without evidence. |
| Planning-only boundary | Established requirements and a complete plan, no implementation authorization. | Completes planning without edits to application behavior or external publication. |

Also rerun the carried-forward interview and planning cases. Evaluate their original behavioral obligations against the revised suite. Record new results separately from the legacy skills' history.

Project-owned decision guidance and revalidation cases are in [project-decisions.md](project-decisions.md). A limited Codex rehearsal and independent review are recorded in [the 2026-11-17 results](project-decisions-2026-11-17.md); they do not replace the broader cases above.

Repository charter cases are in [the guidance cases](../skills/clny-configure/evals/cases.json). A limited Claude Code rehearsal and independent review are recorded in [the 2026-11-19 results](repository-charter-2026-11-19.md).
