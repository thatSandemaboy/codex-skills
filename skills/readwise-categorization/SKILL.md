---
name: readwise-categorization
description: Use when categorizing saved Readwise Reader articles/posts, assigning exactly two tags per saved document using the Domain + Lens clustering rule, and optionally writing verified tags back through the Readwise CLI.
---

# Readwise Categorization

Use this skill when the user wants to categorize, cluster, tag, retag, or reorganize saved Readwise Reader documents.

Do not use highlight-only exports as the source of truth. Categorize saved Reader documents from `reader-list-documents`, using full document content when available.

## Core Rule

Assign exactly 2 tags per saved document:

```text
Domain + Lens
```

- `Domain`: the broad world or shelf the document belongs to.
- `Lens`: the core mechanism, message, reusable idea, or narrower concept inside the document.
- Sentence test: "This is about [Domain], through the lens of [Lens]."

Prefer clustering value over exhaustive description. Do not add extra tags just because they are accurate.

## Source Of Truth

Primary source:

- `html_content` from `readwise reader-list-documents`

Supporting signals:

- `summary`
- `title`
- `author`
- `site_name`
- `source_url`
- existing document tags

If `html_content` is missing or too sparse, mark the row `needs_full_text` or `low_confidence` instead of guessing.

## Readwise Commands

Fetch saved articles:

```bash
readwise reader-list-documents --category article --limit 25 --response-fields title,author,category,site_name,word_count,summary,source_url,tags,html_content --json
```

Fetch compact metadata:

```bash
readwise reader-list-documents --category article --limit 25 --response-fields title,author,category,site_name,word_count,summary,source_url,tags --json
```

Fetch one document:

```bash
readwise reader-list-documents --id <document-id> --response-fields title,author,category,site_name,word_count,summary,source_url,tags,html_content --json
```

Add tags:

```bash
readwise reader-add-tags-to-document --document-id <document-id> --tag-names domain,lens
```

Remove tags:

```bash
readwise reader-remove-tags-from-document --document-id <document-id> --tag-names old-tag,extra-tag
```

Verify tags:

```bash
readwise reader-list-documents --id <document-id> --response-fields title,category,tags --json
```

## Workflow

1. Pull a saved Reader document batch, usually `category=article` unless the user asks for posts/tweets too.
2. Read the full `html_content` for each document. Use summary only as support.
3. Propose exactly two tags: `domain_tag` and `lens_tag`.
4. Save a review CSV before writeback.
5. Ask for approval before changing Readwise unless the user has already clearly approved writeback.
6. Apply tags with `reader-add-tags-to-document`.
7. Remove extra old/pilot tags when the user wants a strict two-tag system.
8. Verify each document with compact metadata.
9. Save/update a writeback log.

## CSV Schema

Use this schema for review artifacts:

```csv
document_id,title,author,category,word_count,source_url,current_tags,content_basis,domain_tag,lens_tag,confidence,writeback_ready,reasoning
```

Rules:

- `domain_tag` and `lens_tag` must each contain exactly one tag.
- `content_basis` should say whether full Reader `html_content` was available.
- `reasoning` should include the sentence test.
- `writeback_ready` should be `yes` only when both tags are high enough confidence.

## Tag Selection

Good domain tags are broad and stable:

- `ai`
- `startups`
- `finance`
- `education`
- `research`
- `policy`
- `mental-health`
- `personal-growth`
- `writing`
- `career`
- `design`

Good lens tags capture the useful idea:

- `growth`
- `distribution`
- `knowledge-graphs`
- `workflow-redesign`
- `financial-statements`
- `geopolitics`
- `self-hypnosis`
- `mindfulness`
- `learning-systems`
- `decision-making`

Examples:

- `startups` + `growth`
- `finance` + `hedge-funds`
- `ai` + `workflow-redesign`
- `research` + `legal-data`
- `personal-growth` + `self-hypnosis`

## Guardrails

- Do not categorize from title alone.
- Do not use highlights as the main source for article categorization.
- Do not write back before a review artifact exists.
- Preserve existing user tags unless the user asks for strict replacement or cleanup.
- When enforcing two tags, remove extras only after deciding which two tags survive.
- Always verify after writeback.

