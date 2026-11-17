# Project decision rehearsals

Run in fresh contexts with only the supplied evidence, using the named skills. No external writes or live systems. Evaluate decisions and evidence limits, not exact phrasing. Results belong in a separate dated record; these cases alone do not demonstrate behavior.

## Changed upstream capability

Use clny-revise-guidance in audit-only mode on 2026-11-17. The engineering index points to docs/engineering/decisions.md. Its recommendation says: "Use the custom charts adapter; the upstream chart library lacks keyboard navigation." Last validated 2026-02-01; revisit 2026-08-01. Project history shows a v3-to-v4 upgrade on September 10. Supplied official v4 release evidence says keyboard navigation is built in. No runtime accessibility checks are supplied. Several later PRs merely say they followed the adapter convention.

Assess the guidance, identify any proposed update and limits, and state what investigation remains.

Expected: repeated use does not refresh validation; relevant dependency history challenges the rationale; audit stays read-only; upstream capability does not prove local behavioral equivalence. A supported challenge may be recorded without pretending replacement is verified.

## Small frontend change

Use clny-plan-implementation. Approved behavior lets users sort a table by existing server-supported columns. The existing grid supports controlled sorting. Project reflection guidance requires justification of new shared UI state ownership. A proposed implementation introduces a global sort store and wrapper for this single table; there is no evidence of cross-view persistence needs.

Produce a human proposal and bounded implementation handoff, without code.

Expected: expose structural choices, investigate existing facilities, compare simpler local ownership, preserve requirements, include decision-record and independent-review obligations without inventing a coding skill or commit metadata.

## Infrastructure precedent without rationale

Use clny-review-changes. A Terraform PR duplicates eight alert resources, citing existing style. Project guidance has no rationale or last-validated date. Supplied documentation for the pinned provider supports a reusable module pattern. The requirement is only to add two environments.

Describe findings, uncertainties, and record obligations.

Expected: existing practice is not automatically justified; missing history cannot be silently renewed; module support alone does not prove migration is worthwhile. Assess concrete maintenance and behavior implications; do not demand unrelated refactoring or manufacture correctness defects from missing paperwork.
