# Project decisions and revalidation

Read when establishing project reflection guidance or reassessing a consequential project decision. General engineering quality advice belongs in skills or existing quality standards, not in this decision register.

## Establish project-owned guidance

Locate a maintained engineering document for project-specific reflection triggers and consequential conventions. Preserve its existing path; docs/engineering/decision-making.md is an optional default. Link it from the engineering index or root instructions so planning, implementation, and review can discover it. Keep the project understandable without a personal skill installation.

Identify relevant technologies and dependency versions from configuration and representative source. Inspect existing facilities and version-appropriate official documentation where library behavior matters. Link authoritative sources rather than copying manuals. Scope research to the affected decisions; do not inventory every transitive dependency or impose generic best-practice catalogs.

Distinguish required constraints, deliberately chosen conventions, and merely observed patterns. Repeated legacy code is evidence of practice, not proof of suitability. Evaluate a pattern before promoting it into guidance; label proposed conventions and never invent approval. Prefer supported framework facilities unless a concrete mismatch justifies an alternative.

Define project-specific reflection triggers from consequential tradeoffs and likely blind spots in that project's work. Explain when they apply and why; examples illustrate rather than exhaust the triggers. Use the [decision-record contract](../../clny-plan-implementation/references/decision-records.md) for the general shape of initiative records. Do not export one project's mechanisms as universal triggers.

## Selective freshness metadata

For consequential, change-sensitive project guidance, record:

| Field | Meaning |
| --- | --- |
| Rationale | Benefit or constraint that justifies the decision. |
| Evidence | Sources or observations supporting it. |
| Last validated | Date its justification was actually assessed, not merely consulted. |
| Revisit by / when | Review date or relevant event, selected for why the decision might cease to hold. |

Keep scope and force clear: mandatory constraint, convention, or proposal. Do not give every rule an arbitrary identical lifespan. Expiry creates a reassessment obligation on next relevant use, not an automatic suspension of a constraint. Repeated use does not refresh validity; no background scheduler or continuous confidence score is required.

## Reassess on relevant use

Planning, implementation, and review must identify applicable overdue or challenged guidance. Reassess before using it as settled justification:

1. Recover the original rationale, evidence, scope, and conditions. If missing, reconstruct a justification from current evidence or flag it unresolved; do not claim historical validation.
2. Use the last validated date as an investigation window. Inspect relevant project history for changes to affected code, dependency versions, requirements, interfaces, and operating assumptions. Follow the subject, not every intervening commit. State unavailable history or evidence.
3. Check today's justification and proportionality, including supported alternatives. Relevant upstream changes can matter even with no local commits. Many unrelated commits do not invalidate a decision. Source inspection alone does not establish runtime conditions.
4. Record retain, revise, retire, or unresolved, with a brief account of evidence actually checked and useful links. Refresh the validation date only for a supported conclusion; an attempted check or "still valid" assertion is insufficient. Set the next review condition where appropriate.

Mandatory constraints remain binding while unresolved. Curation does not grant authority to repeal them; propose changes requiring owner authority and pause only dependent choices. In audit-only mode report the assessment and proposed record update without editing files.

## Learn without accumulating rules

When a review finds a missed decision, distinguish a missed existing trigger from missing or mistaken guidance. Propose a targeted addition, narrowing, or removal with evidence. Do not automatically legislate every incident. Change shared skills only for lessons that generalize across projects. Compliance with guidance does not establish that the guidance is appropriate.
