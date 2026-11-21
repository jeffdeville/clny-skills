# Documentation contract and review rubric

This is a content and navigation contract, not a required directory layout. Its only metadata is the small charter marker described in [the repository charter](repository-charter.md). Combine roles in a small repository; split when readers need independent detail. Reuse authoritative material and omit inapplicable topics.

## Entry point

The root agent instructions name and link the engineering guidance entry point. For example:

> Engineering guidance starts at the engineering index at `docs/engineering/README.md`. Read its architecture guidance, then follow the component and cross-cutting guides relevant to your change. Maintain affected explanations and validation instructions with the change.

Adapt the path to the repository. A link to a personal filesystem skill is not a substitute for repository-owned guidance.

The index contains:

- A short purpose and scope statement.
- The charter marker and responsibilities table, or a link to the charter document that holds them.
- Root architecture guidance, inline when brief or linked when substantial.
- A component map explaining responsibilities, not just folder names.
- Links annotated with when to read them, including cross-cutting practices and validation.

Example index rows:

| Area | Read when | Authoritative guide |
| --- | --- | --- |
| Architecture | Changing ownership, persistence, or service dependencies | Existing architecture guide |
| API | Changing request validation, authorization, or response behavior | API component README |
| Worker | Changing processing, retries, or work ownership | Worker component README |
| Documentation | Changing a system explanation, diagram, or guide location | Documentation practices |
| Validation | Planning evidence for a behavior change or preparing its environment | Validation guide |

Actual links must resolve to substantive content; this example does not require five separate files.

## Root architecture guidance

This and the following sections describe what software responsibilities usually need. For other work, cover the same reader needs in that field's terms.

Explain system purpose, major owners and handoffs, allowed dependencies, and essential invariants. Use a compact diagram when it communicates relationships more clearly than prose. Preserve rationale and evidence for consequential boundaries. State approved intent separately from current behavior, known deviations, and proposed future design. Link detailed decisions rather than copying their history into the overview.

## Component guides

Explain responsibility and non-responsibility, relevant entry points and interfaces, local constraints and conventions, and consequential lifecycle or failure behavior. Link representative implementation and tests when useful. Link back to the parent map and to applicable development and validation procedures. Put deep mechanics in focused guides rather than expanding every overview. Do not create guides for directories that have no independent reader need.

## Cross-cutting practices

Make coding conventions, documentation authoring, and validation discoverable. These may live in root instructions, CONTRIBUTING, tool configuration, or existing guides. Link to one authority for each rule; distinguish required rules from examples and recommendations. Tool configuration can specify formatting, but it does not explain architectural intent.

Documentation authoring guidance should preserve: concise maps, focused owning guides, useful diagrams, authoritative links instead of copied policies, explicit current/proposed status, and updates to explanations and incoming navigation alongside relevant code changes.

## Validation guidance

For each meaningful validation route, identify:

| Field | Reader needs |
| --- | --- |
| Scope | The behavior or risk the check addresses and when it applies. |
| Prerequisites | Environment, services, access, fixtures, and setup needed. Never include secrets. |
| Procedure | Exact existing command or reproducible manual steps and working directory. |
| Expected evidence | Observable result demonstrating success; distinguish a green unit test from an integrated user outcome. |
| Limits | What the check does not establish and any known blocked prerequisites. |
| Cleanup | Required teardown or restoration if the procedure changes state. |

Use the project's targeted test policies. Separate local checks, integration checks, and deployment observations when their evidence differs. Record missing procedures as gaps rather than supplying plausible commands. A historical successful run is evidence for that run, not a permanent guarantee or an instruction to access production.

## Rubric

For the requested scope, mark each applicable dimension adequate, needs correction, or unverified. Give source locations and practical consequences for material findings. Do not use an aggregate score to hide a blocking contradiction.

| Dimension | Review question |
| --- | --- |
| Responsibility coverage | Does the charter state each responsibility as a business function, does the component map account for every part and trace it to one, with every concern recorded as adopted, declined, deferred, or open, and found practices marked endorsed, tolerated, or unexamined? |
| Discoverability | Can a fresh agent find the entry point from root instructions and choose relevant guides before knowing which files will change? |
| Authority | Is each rule's scope and force clear, with one current source and links to approved decisions where needed? |
| Architectural fidelity | Are intent, observed behavior, deviations, and proposals distinct? Are boundaries and rationale preserved? |
| Local usefulness | Can the reader identify ownership, interfaces, applicable conventions, and useful implementation examples? |
| Validation usefulness | Can the reader prepare and execute appropriate checks, recognize success, and see what remains unproven? |
| Change coherence | Do code descriptions, diagrams, procedures, and parent/child navigation tell the same current story? |
| Maintainability | Is detail located with its owner, duplication avoided, and the structure proportionate? |
| Accessibility | Do links and anchors work, and will the intended checkout or worker actually receive the documents? |

Prioritize incorrect authority or architecture and misleading validation claims, then gaps that prevent navigation or execution, then readability refinements. State audit coverage and unresolved evidence honestly.

## Example: code diverges from architecture

An approved guide says only the worker writes report storage. A legacy API handler writes directly, while its README incorrectly claims it never does.

Correct the API description and record the legacy deviation with a source link. Preserve the worker-only architectural rule. Do not rewrite the rule to authorize direct API writes, claim the migration is implemented, or change application code during curation. If migration is proposed later, mark its documentation as proposed until the implementation exists.

## Interview deliverables and acceptance criteria

At apparent completion, compare each applicable deliverable with the scan, the owner's answers, and the guidance a contributor will actually receive. These are content requirements; a small project can satisfy them in one document.

| Deliverable | Evidence that it meets the objective |
| --- | --- |
| Map of the repository | Every meaningful area has a purpose, supporting evidence, a responsibility or an owner's ruling, and a guide or a visible guidance gap. Check mixed-purpose and apparently dormant areas against representative evidence. |
| Responsibility charter | The owner confirmed whom each business function serves, what it does, and its ambition after seeing the scan. A plausible adjacent request can be placed inside or outside the responsibility using the recorded boundaries. |
| Account of current practice and authority | A contributor can tell what happens today, what binds, what the owner endorses or tolerates, and what remains unexamined. Trace material discrepancies, including partial migrations, to evidence and the owner's ruling or an explicit open question. |
| Standing decisions | For each responsibility, all eight charter concerns and seriously weighed candidates have dispositions or explicit inherited defaults. Check the recorded decisions against the owner's actual qualifications. Show costs and benefits of candidates and surface serious exposures at every ambition. Adoption identifies a procedure or implementation gap, refusal a reason and revisit condition, deferral a trigger. Unanswered questions stay open. |
| Discoverable change, operation, and validation guidance | Apply the [human oversight and editing questions](../../clny-find-requirements/references/intent-contract.md#guidance-for-human-oversight-and-editing) to a real responsibility. Identify where each reader starts and what answer they can find, or repair the specific gap. All expected guidance files are reachable from the contributor's root document. The applicable route identifies authority, constraints, procedures, expected evidence and limits, or records the specific missing procedure. Verify distribution to the intended checkout separately. |
| Resumable completion record | From the saved charter a new session can recover decisions, the next open concern, and any adopted work awaiting implementation. Open concerns keep a responsibility in progress. Whole-charter review date and satisfied suite version each follow their own milestone rules. In read-only work identify what lives only in chat. |

For each criterion give a concrete source or gap. Repair omissions from available evidence, ask the smallest remaining owner question where a decision is needed, and recheck affected criteria. Carry open work forward explicitly. Within an audit or narrow maintenance request, assess only the requested scope.

### Check root reachability

Build the expected set **before crawling** from the scoped component inventory and existing authorities. Reconcile it with guidance created, moved, or designated during this run, including unchanged guides that should remain accessible. Include an expected file even if it is missing. Record intentionally deferred guides as guidance gaps. Extra reachable files are fine.

Run the bundled [guidance checker](../scripts/check_guidance.py) with Python 3.9+ and Pandoc with GFM support. For example, from the configured repository, substituting the installed script location and the actual paths:

```sh
uv run --no-project /path/to/clny-configure/scripts/check_guidance.py AGENTS.md docs/engineering.md docs/recovery.md
```

Start at the document contributors actually open, including its link to the engineering index. If all guidance lives in the root document, pass it as both root and expected file. The checker follows local Markdown and HTML hyperlinks through Markdown documents, checks GFM heading fragments and explicit HTML anchors, and reports missing targets and unreachable expected files with a nonzero exit. Leading slashes are repository-relative. Existing directories and non-Markdown files end traversal. External URLs, renderer-specific includes, and fragments inside other file types are outside its coverage. When a repository uses another navigation format or a prerequisite is unavailable, verify that route separately and report the evidence or limitation.
