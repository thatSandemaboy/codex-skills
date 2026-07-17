# Readwise Categorization

Categorize saved Readwise Reader documents with exactly two tags:

```text
Domain + Lens
```

Example: `ai` + `workflow-redesign`.

The skill is designed for saved Reader articles and posts, not highlight-only exports. It reads full document content when available, proposes a review CSV, and can write verified tags back through the Readwise CLI.

## Install

From the repo root:

```bash
./scripts/install-skill.sh readwise-categorization
```

Or copy this folder into:

```text
~/.codex/skills/readwise-categorization
```

## Codex Trigger

Ask Codex to use `readwise-categorization` when you want to tag, cluster, retag, or reorganize saved Readwise Reader documents.

## Source Of Truth

The Codex-facing instructions live in [SKILL.md](SKILL.md).

