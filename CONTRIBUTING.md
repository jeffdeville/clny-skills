# Contributing

Keep skills portable between Codex and Claude Code. Use standard SKILL.md frontmatter with name and description, relative links, and generic capabilities rather than hardcoded tool names or personal paths. Keep the five-skill suite installable together. The shared intent contract lives under clny-infer-intent; reference it rather than duplicating its rules.

Keep inference, owner decisions, planning, review, and documentation curation separate. Test changes against realistic prompts and assess outcomes rather than exact phrases. Include intended behavior reports, ambiguous intent, adequate existing PR requirements, conditional preferences, delegated choices, documentation drift, and access limits. Do not include private company/customer examples in the distributable fixtures.

Review Markdown links and frontmatter before sharing. Run existing behavioral cases in fresh contexts with only the supplied evidence; use isolated fixtures and prohibit external writes. Record client/model, skill revision, prompt, evidence available, observed outcome, and limitations. A self-review is not an independent behavioral evaluation. Structural validation is not proof of agent performance.

Documentation must describe actual behavior and distinguish planned checks from completed checks. Keep package instructions and routing aligned when responsibilities change. Do not introduce an implementation skill or automatic PR publication implicitly.
