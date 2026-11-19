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

## Changes after owner review, not rehearsed

Following review of the PR, the charter dropped inference of the owner's familiarity, asks ambition explicitly with revised level definitions, requires a scan before the interview, and gives found practices a standing of endorsed, tolerated, or unexamined. The suite gained one version, a changelog with acceptance criteria, and version-mismatch notification in every skill. Two cases were added for the brownfield and mismatch situations. None of this has been rehearsed. The six concerns are held as a working hypothesis pending an experiment on real repositories, and the PR is held until that is done.

## Trial on four private repositories, 2026-11-19

Method: for each repository, three agents in separate contexts. One used the skill to scan and draft a charter up to the owner's questions. One wrote a free-form standing briefing without seeing the skill. One planned real requested changes from the charter draft and logged each standing fact it needed and where it came from. The owner was absent from all passes. Project details are deliberately not recorded here.

Of 169 standing facts the planners needed, 40 percent were supplied by the charter draft, 31 percent would have arrived once queued owner questions were answered, 15 percent fell under a concern but were neither recorded nor asked, and 14 percent fell under none of the six concerns.

Generalized findings:

- Responsibilities were over-split. Agents proposed 19 across four repositories where a business-objective reading gives about 6, because the definition split by risk surface. Much apparent filler in the concern grid followed from this.
- Change and Authority gave the same answer in every repository. Exposure carried most distinct content.
- Recurring facts with no concern: scope and non-goals, promises to those relying on the work, durable state and its recovery, outside obligations, which of several contradictory documents is current, and terms used for more than one thing.
- The scan was the larger failure. In the two large repositories it read about three and one percent of files, mostly root documents, and the charter omitted whole directories that the planned changes concerned. The experiment prompt and the skill both told the agent to sample.
- Marking everything unexamined by default hid which written rules bind.

Limits: one run per cell; planners classified their own facts; shallow clones; nothing was executed; the owner set the business-objective definition and confirmed the count for two repositories, the other two counts are the author's estimate, and the individual findings are unchecked.

Changes made in response, none yet rehearsed or retested: responsibilities defined as business objectives; a scan step with a coverage rule and a component map; written rules binding by default and observed practices unexamined by default; concerns revised to Promises, Change, Delivery, Health, State, Dependencies, and Exposure; ambition asked after the scan summary; existing documents linked or moved, never copied.

## Structural checks

The earlier report incorrectly said all five skill frontmatters parsed. Independent review of 0ada19b reproduced four YAML errors in unquoted descriptions. Other author-reported structural checks at that revision were: every relative Markdown link target exists; the marker example parses as YAML; the case file parses as JSON; no prohibited character; git diff --check clean. These establish structure, not agent behavior.

## Not done

The carried-forward interview, planning, and cross-skill cases were not rerun, although clny-plan-requirements, clny-plan-implementation, and clny-review-changes each gained a routing sentence. The several-responsibilities case was not rerun against the revised text. No field research with real sources was exercised. No real repository has been chartered with this skill.

## Review repairs and focused rehearsal

Ruby Psych parsed the five repaired skill frontmatters. Each name matched its directory, each description was a string, and each version was 0.3.0. The charter example also parsed. An independent reviewer traced the milestone and version rules across the skill entry points, charter, and changelog and found the four review issues addressed.

A fresh GPT-6-based Codex desktop agent read the configure skill and its references in a read-only checkout. The exact model variant was unavailable. The skill, charter, and changelog under test had Git blob IDs 6082172, 989588b, and 84a5bbe. The agent received the following synthetic scenarios together, without evaluation checks, history, or diff. It described the intended actions without editing files.

| Prompt | Observed response |
| --- | --- |
| We just confirmed one publication responsibility. What marker is saved? On resume, five concerns are adopted and the sixth is open. What is saved now? | Saved the responsibility as pending with neither milestone field. On resume it recorded the decisions, marked the responsibility in-progress and identified the open concern for the next session. |
| A separate repository records 0.4.0 and your installation is 0.3.0. Update our charter and correct an unrelated guide typo. | Preserved the charter, identified the missing release information, suggested updating the installed suite and continued the independent typo correction. |

The rehearsal used no real repository or client skill-discovery test. The real-repository interview experiment remains open.
