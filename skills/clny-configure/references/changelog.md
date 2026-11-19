# Suite changelog

The five clny skills share one version, carried in every skill's frontmatter. A configured repository records the version it last satisfied in its charter marker. This file ships with the installed skills so that a repository's version can be compared with the installed one.

## When versions differ

Any skill that reads a charter marker and finds a version different from its own tells the user, summarizes the entries between the two versions, and offers `clny-configure` to bring the repository up to date. It then continues the requested work, unless an entry between the two versions is marked blocking. When the marker is newer than the installed skills, say that the installation is older and do not rewrite the marker.

`clny-configure` brings a repository up to date by checking each intervening entry's acceptance criteria against the repository, interviewing the owner only on criteria that fail, and recording the new version when all are met.

## Writing an entry

Every release adds one entry, newest first: the version and date, what changed, whether it is blocking, and acceptance criteria. Criteria are statements about a configured repository that an agent can check and, where they fail, turn into interview questions. A release that asks nothing of configured repositories says so.

## 0.3.0 — 2026-11-19

Blocking: no.

Changed:

- Guidance starts from a repository charter: responsibilities, an ambition level for each, six concerns, and recorded decisions.
- Practices found in a repository carry a standing of endorsed, tolerated, or unexamined.
- The suite has one version and this changelog.
- Three skills were renamed: `clny-revise-guidance` to `clny-configure`, `clny-interview-owner` to `clny-plan-requirements`, and `clny-infer-intent` to `clny-find-requirements`.
- Every skill states its workflow and position.

A configured repository satisfies this version when:

- Its engineering entry point, or the charter document linked from root instructions, carries a charter marker with a version, a review date, and each responsibility's interview state.
- Every responsibility the evidence shows is listed, and the owner has confirmed the list.
- Each responsibility has an ambition level the owner chose.
- Each of the six concerns has a recorded state for each responsibility, directly or by inheriting a recorded repository default.
- Practices that bear on a concern are marked endorsed, tolerated, or unexamined in the guide beside the code they belong to.
- Repository guidance refers to the skills by their current names.

## Earlier versions

Repositories guided before 0.3.0 have no marker. Treat them as unconfigured; their existing guidance is evidence for the first charter.
