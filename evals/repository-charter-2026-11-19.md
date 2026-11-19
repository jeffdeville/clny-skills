# Repository charter rehearsal results — 2026-11-19

Skill names in this record follow the 2026-11-19 renames; the runs used the earlier names clny-revise-guidance, clny-interview-owner, and clny-infer-intent.

## Scope and method

Claude Code cloud session, independent subagent contexts; the exact model identifier is deliberately not recorded in the repository. Candidate: branch claude/affectionate-rubin-51jo2l based on 307612b, with the charter changes in this PR. This is a limited synthetic rehearsal, not a real-project trial, and it was not run on Codex.

Cases are the three charter cases and the amended small-change case in [the guidance cases](../skills/clny-configure/evals/cases.json). Each rehearsal agent received the skill path, the scenario prompts, and read-only and no-network limits. Expected checks, the evals directory, the diff, and the design conversation were withheld. Scenarios shared one agent context per run; they were not separately isolated. No repository existed behind any scenario, so every response rested on the supplied description. The checks were written by the same author as the skill change and assessed by that author, which limits their independence.

A separate agent reviewed the first draft's diff against the agreed requirements and repository rules.

## Run 1: first draft (commit e6ece0c)

| Case | Observed outcome | Limit |
| --- | --- | --- |
| Several responsibilities | Inferred the empty charter without asking; proposed three responsibilities as outcomes with evidence and unseen items; recorded the shared pipeline once; raised unattended, unlimited advertising spend ahead of any ambition choice; presented practices as costed candidates labeled as general knowledge with some recommended against; preserved the no-write boundary and ended on an owner decision. | Asked for list confirmation and the first advertising question in the same turn. No sources consulted. |
| Resume and declined | Left the declined site decision alone because its revisit condition had not arrived; identified customer email as unrecorded with its exposure; asked whether the owner had decided to carry it; kept the review date unchanged. | Planned to resume the open advertising concern in the same session, which the later scope rule no longer calls for. |
| Toy proportion | One responsibility; recommended against guides, tests, and pipelines; named irreversible photo loss as the single exposure. | Drafted health and dependencies as declined before the owner answered. Unclear whether an instruction file was needed for the pointer. |

The independent diff review reported ten findings. The most serious: a repository without a marker would turn any narrow maintenance or audit request into a charter interview; the older-version row gave no way to know what had changed; resumability was under-specified; the planner's restated rubric had gone stale; marker placement conflicted when the index lives in root instructions; the exposure floor was tied to ambition but not familiarity; and the route for adopted, unbuilt practices was unnamed. All ten were addressed in the revised text, together with the ambiguities the rehearsal agent listed.

## Run 2: revised text

| Case | Observed outcome | Limit |
| --- | --- | --- |
| Small-change maintenance, index without front matter | Reported the broken link and the no-edit conclusions; reported the absent charter as a gap outside the change and did not start an interview. | Marked responsibility coverage as needing correction in an audit scoped to one change, which is arguably louder than a gap note. |
| Toy proportion, README and no agent instructions | One responsibility; exposure named and left for the owner; no instruction file proposed; pointer from the README; nothing recorded as declined. | Still proposed a separate guidance document path by default. |
| Resume and declined | Did not reopen the site decision or resume advertising; proposed customer email as a separate responsibility using the exposure and authority test; asked only whether the owner intends to carry it; routed behavior questions to the change interview. | Left unclear whether the new responsibility's concerns would be interviewed in the same session after a yes. |

Four small clarifications followed Run 2: reconciling a touched responsibility includes its concerns, a tiny repository may use one document for everything, familiarity is inferred before it is asked, and evidence-settled answers may accompany the list question. One check in the resume case was amended to match the scope rule. These last edits were not rehearsed again.

## Structural checks

Run with uv: every relative Markdown link target exists; all five skill frontmatters parse with matching names; the marker example parses as YAML; the case file parses as JSON; no prohibited character; git diff --check clean. These establish structure, not agent behavior.

## Not done

The carried-forward interview, planning, and cross-skill cases were not rerun, although clny-plan-requirements, clny-plan-implementation, and clny-review-changes each gained a routing sentence. The several-responsibilities case was not rerun against the revised text. No field research with real sources was exercised. No real repository has been chartered with this skill.
