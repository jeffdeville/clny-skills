---
name: clny-infer-intent
description: Investigate reports, repository documentation, historical decisions, or unclear PR requirements to infer existing product intent and identify whether a change is warranted. Does not conduct the owner interview, plan implementation, or review code quality. Change workflow, step 1 when intent must be recovered from evidence; followed by clny-plan-requirements if owner decisions remain, otherwise by planning or review.
metadata:
  version: "0.1.1"
  status: draft
---

# Infer intent

**Where this fits.** Change workflow, step 1 of 4, used only when existing intent has to be recovered from evidence. Next: `clny-plan-requirements` when owner decisions remain; `clny-plan-implementation` for an established correction; `clny-review-changes` for a PR whose requirements turn out adequate.

Recover the applicable product requirements from evidence. External reports are speculative claims, not accepted correction requirements. A reproducible symptom establishes what happens, not what should happen. Do not infer approval from a ticket, PR, proposed fix, or passing test.

## Start with existing evidence

Read the request and linked material, root project instructions and README, then the relevant component guidance, inline explanations, and decisions. Use available connected tools for supplied reports and discussions. Record inaccessible evidence; do not silently substitute guesses. Honor the current scope and permission boundaries.

If an existing requirement document adequately establishes intent, authority, and coverage of the requested change, reuse it. Do not repeat an interview or require a new document merely to use this skill.

For a reported problem, establish observed versus expected behavior and relevant context. Reuse credible reproduction evidence with attribution; reproduce safely when authorized and useful, or state that reproduction remains reported. Compare a working control where available. Investigate only enough source, configuration, tests, and history to explain the discrepancy and establish the affected boundaries. Avoid turning this investigation into implementation design.

Treat the codebase's documentation as the maintained account of intent. Read inline comments and docstrings as well as guides. When concrete contradictions arise, check scope and relevant decision history. Current implementation and tests explain behavior but do not automatically approve it. Do not invent an elaborate authority hierarchy or audit unrelated documentation.

## Resolve the report

Distinguish observed facts, attributed reports, supported inferences, established requirements, and proposed solutions. Keep requirement authority separate from confidence in a diagnosis. Use the [shared intent contract](references/intent-contract.md).

A useful conclusion may be:

- Confirmed defect against established behavior.
- Intended behavior or a known limitation.
- Usage/configuration misunderstanding.
- Documentation defect.
- A request for new behavior presented as a bug.
- Insufficient evidence to decide.

Select the conclusion supported by evidence; do not force a fix or a closed disposition. Explain what each conclusion means for the user's requested work. Establishing a misunderstanding or limitation can complete the task without an implementation plan.

## Hand off residual decisions

This skill does not conduct a product interview. Resolve factual questions through available evidence. When a consequential choice about required behavior remains, carry the findings and smallest unresolved owner question to `clny-plan-requirements`. That transition may happen in the same conversation within the user's scope; it does not require a new manual invocation. If that skill is unavailable, provide the bounded question and evidence without pretending the intent is settled.

For a PR, adequate existing intent lets `clny-review-changes` continue immediately. For an established correction, `clny-plan-implementation` can plan within authorization. Do not turn completion of inference into permission to edit, publish, or deploy.

Deliver a proportionate intent record or reference to the adequate existing document, sources, conclusion, evidence limits, and unresolved decisions. A source-supported existing requirement does not need fresh owner approval. An inference alone must not become an approved product change. Keep unrelated authorized work moving.
