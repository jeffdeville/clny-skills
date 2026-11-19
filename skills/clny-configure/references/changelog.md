# Suite changelog

The five clny skills share one version, carried in every skill's frontmatter. A configured repository records the version it last satisfied in its charter marker. This file ships with the installed skills so that a repository's version can be compared with the installed one.

## When versions differ

Compare the recorded version with the installed suite before applying migration instructions.

- **Repository version is newer.** Report both versions. The older installation lacks the intervening release criteria and blocking decisions. Preserve the charter and suggest updating the installed suite. Continue work independent of those unknown requirements.
- **Repository version is older.** Summarize the intervening entries and offer `clny-configure` to bring the repository up to date. Continue the request unless an intervening entry is blocking.
- **Marker present without a version.** First configuration is unfinished. Within configuration scope, resume from the saved decisions and assess the release criteria.

`clny-configure` brings a repository up to date by checking each intervening entry's acceptance criteria against the repository, interviewing the owner only on criteria that fail, and recording the new version when all are met.

## Writing an entry

Every release adds one entry, newest first: the version and date, what changed, whether it is blocking, and acceptance criteria. Criteria are statements about a configured repository that an agent can check and, where they fail, turn into interview questions. A release that asks nothing of configured repositories says so.

## 0.3.0 — 2026-11-19

Blocking: no.

Changed:

- Guidance starts from a repository charter: responsibilities stated as business functions, an ambition level for each, a set of concerns, and recorded decisions.
- A scan produces a skeleton tracing every meaningful path to a responsibility.
- Written rules are treated as binding; observed practices carry a standing of endorsed, tolerated, or unexamined.
- The suite has one version and this changelog.
- Three skills were renamed: `clny-revise-guidance` to `clny-configure`, `clny-interview-owner` to `clny-plan-requirements`, and `clny-infer-intent` to `clny-find-requirements`.
- Every skill states its workflow and position.

A configured repository satisfies this version when:

- Its engineering entry point, or the charter document linked from root instructions, carries a charter marker with a whole-charter review date and each responsibility's interview state. Record the satisfied version after verifying these criteria.
- Every responsibility is stated as a business function, and the owner has confirmed the list.
- The component map accounts for every part of the repository, traces it to a responsibility or records the owner's ruling, and says whether a guide exists for it.
- Each responsibility has an ambition level the owner chose.
- Each concern in the charter reference has a recorded state for each responsibility, directly or by inheriting a recorded repository default.
- Practices that bear on a concern are marked endorsed, tolerated, or unexamined in the guide beside the code they belong to.
- Repository guidance refers to the skills by their current names.

## Earlier versions

Repositories guided before 0.3.0 have no marker. Treat them as unconfigured; their existing guidance is evidence for the first charter.
