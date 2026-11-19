# clny-skills

Portable delivery skills for Codex and Claude Code. Investigate intended behavior, interview owners when decisions remain, plan implementation, review changes, and maintain the codebase's documented story.

## Skills and routing

| Skill | Responsibility |
| --- | --- |
| `clny-infer-intent` | Investigate reports and existing evidence; distinguish defects, intended behavior, misunderstandings, and unresolved intent. |
| `clny-interview-owner` | Establish new requirements for a change or resolve remaining product decisions with the owner. |
| `clny-plan-implementation` | Convert established intent into bounded implementation, documentation, and validation work. |
| `clny-review-changes` | Review an existing change against requirements, engineering guidance, and evidence. |
| `clny-revise-guidance` | Establish the charter of what the repository is responsible for; establish missing guidance or reconcile existing repository and inline explanations. |

A request for new product behavior starts with an interview when consequential decisions remain. Established requirements can proceed directly to planning. A bug report starts with investigation and needs an interview only if product decisions remain. A PR with adequate requirements goes directly to review; unclear requirements route through investigation and, when necessary, an interview. These are responsibilities, not five mandatory invocations.

The [shared intent contract](skills/clny-infer-intent/references/intent-contract.md) preserves requirements, discretion, and evidence limits. Every change explicitly reviews affected documentation, including inline explanations. Required corrections accompany the change; a justified no-edit conclusion is valid.

Guidance starts from a [repository charter](skills/clny-revise-guidance/references/repository-charter.md): the responsibilities the repository carries and the owner's recorded decisions about each, including what was declined. The guidance skill reads the charter's state from the repository instead of being told whether a setup is new, and interviews the owner only on the difference.

Project engineering guidance owns reflection triggers and consequential project conventions. Planning exposes structural choices in a brief human proposal, with implementation detail and decision records alongside it. Implementation handoffs require independent review of each bounded increment or PR. Guidance revalidation examines relevant changes since the last supported assessment; use alone does not renew a rule. See the [decision-record contract](skills/clny-plan-implementation/references/decision-records.md) and [revalidation procedure](skills/clny-revise-guidance/references/project-decisions.md).

## Install on each computer

Keep the five skills together: their relative references form one suite. The Markdown instructions have no dependency on a specific model, proprietary tool name, or personal filesystem path. Use the local skills mechanism of Codex or Claude Code (not a Claude.ai/Cowork upload).

After the GitHub repository is populated:

```sh
git clone git@github.com:jeffdeville/clny-skills.git
cd clny-skills
```

From this checkout, link each skill into the desired personal skill directory. These commands are for macOS/Linux. They refuse to replace existing destinations; resolve a collision explicitly rather than overwriting it.

Codex:

```sh
mkdir -p "$HOME/.agents/skills"
for skill in "$PWD"/skills/clny-*; do
  target="$HOME/.agents/skills/$(basename "$skill")"
  if [ -e "$target" ] || [ -L "$target" ]; then
    printf 'Already exists; leaving unchanged: %s\n' "$target"
  else
    ln -s "$skill" "$target"
  fi
done
```

Claude Code:

```sh
mkdir -p "$HOME/.claude/skills"
for skill in "$PWD"/skills/clny-*; do
  target="$HOME/.claude/skills/$(basename "$skill")"
  if [ -e "$target" ] || [ -L "$target" ]; then
    printf 'Already exists; leaving unchanged: %s\n' "$target"
  else
    ln -s "$skill" "$target"
  fi
done
```

Alternatively copy all five directories into the relevant skills directory; copied installations must be refreshed after updates. Restart the client and verify that all five names appear. In Codex invoke `$clny-infer-intent`; in Claude Code invoke `/clny-infer-intent`. Automatic selection is also allowed.

For project-scoped use, copy all five directories into `.agents/skills/` for Codex or `.claude/skills/` for Claude Code, following your repository's policy. Avoid duplicate installations of the same names.

To update a linked installation, run `git pull --ff-only` in this checkout and start a fresh client session. Keep the checkout at the same location or recreate its links. Each computer has its own clone and installation; no private tickets, credentials, or machine settings belong in this repo.

This package supersedes the responsibilities of `delivery-product`, `delivery-plan`, and `delivery-guidance`. It does not automatically delete existing installations. After validating the new suite, remove the old copies from discovery to avoid overlapping triggers; retain history in version control rather than keeping compatibility skills.

Official installation references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Development and evaluation

Read [CONTRIBUTING.md](CONTRIBUTING.md). This is an initial draft, not a claim of behavioral reliability across clients. See [the evaluation cases](evals/cases.md); existing interview and planning cases live under their skill directories. Historical results for the prior skills are deliberately not presented as results for this suite.
