# Documentation contract and review rubric

This is a content and navigation contract, not a required directory layout or metadata schema. Combine roles in a small repository; split when readers need independent detail. Reuse authoritative material and omit inapplicable topics.

## Entry point

The root agent instructions name and link the engineering guidance entry point. For example:

> Engineering guidance starts at the engineering index at `docs/engineering/README.md`. Read its architecture guidance, then follow the component and cross-cutting guides relevant to your change. Maintain affected explanations and validation instructions with the change.

Adapt the path to the repository. A link to a personal filesystem skill is not a substitute for repository-owned guidance.

The index contains:

- A short purpose and scope statement.
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
