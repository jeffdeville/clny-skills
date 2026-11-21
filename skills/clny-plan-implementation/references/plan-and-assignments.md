# Implementation plan and assignment contract

Use descriptive behavior titles. These are content requirements, not a fixed number of documents, phases, or fields for every small change. Prefer one canonical plan with embedded assignments; split only when it improves actual use.

## Human proposal and agent detail

Deliver two views of the same plan revision. The detailed plan equips an agent to execute and verify each increment. Lead with a compressed human brief that stands on its own, usually about one screen. Show the user outcome, how the proposed change works, what it reuses or adds, the consequential choice and why it matters, and what is ready or still needs a decision. Link to the detailed increments and decisions. Preserve qualifications when compressing.

Include an actual visual in every human brief. Choose the simplest form that answers the reader's question. For a button rename, `[ Run ] → [ Preview ]` with a caption explaining what clicking still does can be the whole illustration. For a change in who approves publication, draw the proposed path and label where approval happens. For a sequence with overlapping retries or a concept the reader needs to explore, deliver an animation or a self-contained HTML walkthrough when motion or interaction clarifies it. An analogy can introduce an unfamiliar mechanism; connect it to the actual components. Give the visual a short textual takeaway.

Inspect the visual in its intended medium, exercise any interaction it relies on, and confirm it agrees with the agent plan about ordering, ownership, and uncertainty. When rendering is unavailable, provide a readable inline equivalent and state the verification limit. Put the brief and any richer media where the intended reviewer can open them, including when the authorized delivery is chat only.

A useful layout is plans/<initiative>/README.md, implementation.md, and decisions.md. Adapt to existing conventions and combine for small work. Preserve one canonical source for each fact rather than duplicate accounts. Use [the decision-record contract](decision-records.md).

Before marking a slice ready, explain its concrete behavior, path through existing interfaces, consequential state changes and failure/recovery behavior, proposed mechanisms versus simpler alternatives, and completion evidence. Missing knowledge calls for bounded investigation; too many coupled outcomes call for narrowing or sequencing. Do not prescribe every helper or invent certainty to make a plan appear complete.


## Canonical implementation plan

| Part | Required account |
| --- | --- |
| Authority | Plan location and revision; intent record or product contract path and exact revision; approval provenance; permitted actions; readiness and gates. |
| Outcome and boundaries | Behavior served and exclusions, linked to the intent record or product contract rather than redundantly rewriting it. Preserve conditional preferences and delegated choices. |
| Project grounding | Engineering entry points; applicable architecture, coding, documentation, and validation guidance; representative source/test paths; missing or conflicting guidance. |
| Design and evidence | Selected mechanisms, boundaries, interfaces and ownership, rationale, significant alternatives, observed facts, and unverified assumptions. Separate engineering decisions from product requirements. |
| Delivery increments | Observable outcomes, dependencies, sequencing, responsibilities, and what each increment proves. Include an early integrated behavior when practical. |
| Validation | Acceptance-to-evidence mapping; existing procedures, new checks to author, prerequisites, expected results, and evidence limits. |
| Documentation | Owning guides and upstream navigation affected by each increment; proposed versus current state; prerequisites for missing guidance. |
| Coordination | Shared interfaces, cross-repository dependencies, revision reconciliation, and applicable release/migration/rollback constraints. |
| Decisions and gaps | Owner questions, bounded investigations, access gates, dependent work, and unaffected work that can proceed. |

A plan may be ready for review while execution is unauthorized. A bounded investigation may be ready while dependent implementation remains unready. State these separately.

## Bounded assignment

An implementer receives:

- Accessible intent record or product contract and implementation plan paths and exact revisions, instructions to read them, approval status, and permitted actions.
- Descriptive outcome and required behavior served; relevant exclusions.
- Local responsibility and interfaces with other owners, including shared files or resources requiring coordination.
- Dependencies and conditions that must hold before starting or claiming completion.
- Applicable project guidance and concrete nearby code/test exemplars, with scope and known exceptions.
- Decisions already settled, engineering choices delegated to the implementer, and discoveries requiring coordination or owner clarification.
- Documentation destinations and the expected impact, including diagrams, links, and validation procedures where relevant.
- Completion evidence: checks to run or author, prerequisites, expected observations, and unresolved runtime limits.
- A progress checkpoint describing the observable outcome, evidence, documentation status, and remaining work.

A task is bounded by outcome and responsibility, not necessarily one folder. Do not create independent assignments for coupled edits that need one coherent change. Parallel execution is optional, not implied by multiple briefs.

## Acceptance-to-evidence mapping

For each meaningful required outcome, name the increment and how it will be demonstrated. For example, a private comment feature could map:

| Required outcome | Planned evidence |
| --- | --- |
| Authorized reader creates and reads a comment | Integrated create/process/readback procedure with real authorization context, using the project's documented environment. |
| Other projects cannot create or read it | Negative authorization tests across both write and read paths. |

Do not invent concrete commands or a working transport from this example. Discover them, or assign their creation with prerequisites and expected evidence. Tests needed for a selected implementation mechanism, such as duplicate-delivery safety, are engineering validation obligations; they do not retroactively become owner-specified product requirements.

If lifecycle behavior was delegated, record the chosen behavior and rationale as an engineering decision. Do not write restoration into product acceptance simply because retaining rows was initially suggested as easier.

## Documentation impact and guidance gaps

Identify authoritative locations, not a generic "update docs" task. If the API/worker boundary changes, consider both component descriptions and the parent architecture flow. If tests need a new local service, include setup and teardown in the validation guide. Leave already accurate explanations unchanged with a short rationale.

Use the curation rubric to distinguish a small factual correction from a policy conflict or broad hierarchy gap. A missing root index may warrant a bounded discovery/navigation prerequisite. An incomplete handbook does not justify withholding all planning when current guidance and source settle the affected work.

## Fresh-reader rehearsal and completion

Ask the reader what they would implement, leave out, validate, document, decide independently, and pause over. Check that they can locate the named sources and understand shared dependencies without inherited chat. Repair evidence-resolvable gaps; return only residual consequential decisions to the owner.

Before declaring the requested planning stage complete, verify that:

- The human brief and its visual are delivered and accessible. A reader can identify the outcome, consequential change, and any decision needed without reading the assignments. Compare both views to the same plan revision.
- Each increment names the human-facing explanation and the editor guidance to inspect, the specific update or reason each can remain as written, and how final review will verify both against what ships.
- Every required outcome has planned evidence; no incidental preference has become an unconditional promise.
- Dependencies and decision gates are explicit, with no assignment pretending an unknown capability exists.
- The first meaningful integrated outcome is visible, or the reason it must wait is explained.
- Documentation work accompanies affected increments and validation is grounded in project procedures.
- Contract and plan revisions, approval status, accessible handoff locations, and execution authority are clear.

Report planned checks as planned. A rehearsal of a plan does not verify implementation, deployment, or production behavior.

Every assignment includes review of affected inline comments/docstrings and owning guides. Documentation inconsistencies block readiness; adequate unchanged documentation receives a concrete no-edit rationale. For defects, include baseline regression evidence and how already-affected users or data recover, when relevant.
