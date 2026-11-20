# Initial evaluation record

Skill names in this record follow the 2026-11-19 renames; the runs used the earlier names clny-revise-guidance, clny-interview-owner, and clny-infer-intent.

Date: 2026-11-15. Suite: initial draft before first commit.

Structural checks passed for all five skill frontmatters, local Markdown link targets, JSON case files, absence of personal filesystem paths, and prohibited-character checks. Validation used the local skill-creator validator; that tool is not a runtime dependency of this package.

An independent Codex subagent performed a read-only synthetic evaluation of three scenarios using the skill instructions and supplied facts. No live client integration, application execution, external actions, or full evaluation suite was run. The inherited model identifier was not exposed in its report.

- A reported 24-hour retention limit matching current requirements was classified as intended behavior, without a manufactured fix or interview.
- A PR with adequate project-isolation requirements but an unscoped lookup was routed directly to review. The reviewer identified the behavioral defect and misleading inline explanation despite passing reported tests.
- An owner's indifference to deletion retention was preserved as delegated discretion, without turning implementation convenience into mandatory acceptance.

The evaluator found two wording risks: the README overgeneralized all new requests as requiring an interview, and a handoff reference described every interview result as agreed. Both were corrected to preserve direct planning from adequate requirements and distinguish proposal completeness from approval. This is a synthetic comprehension check, not evidence of reliable behavior in real projects; the delegation case closely resembles an existing reference example.

Still to run: the complete behavioral cases, fresh-session discovery and invocation on both Codex and Claude Code, and real-project trials. No results from the former delivery skills have been claimed as results for this suite.

## Configure closeout and reachability, 2026-11-20

Against the 0.4.0 working tree, the six synthetic CLI cases in [the checker tests](../skills/clny-configure/evals/test_check_guidance.py) passed using Python 3.13 and Pandoc 3.10. They exercise transitive links, a removed incoming link to an unchanged guide, missing files and anchors, HTML navigation, and symlink identity and containment. Running the checker with the Configure skill entry point reached all four expected reference documents and the checker script. The skill-creator validator accepted the Configure metadata.

These checks cover the link checker and skill structure. A real owner interview followed by observation of a contributor using the resulting guidance remains untested.
