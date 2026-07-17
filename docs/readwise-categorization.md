# Readwise Categorization Guide

This skill turns saved Readwise Reader documents into a strict two-tag library.

## Clustering Rule

Every document gets exactly two tags:

```text
Domain + Lens
```

- `Domain`: the broad shelf the document belongs to.
- `Lens`: the reusable idea, mechanism, or message inside the document.

Sentence test:

```text
This is about [Domain], through the lens of [Lens].
```

## Workflow

1. Pull Reader documents with `reader-list-documents`.
2. Read full `html_content` when available.
3. Propose one `domain_tag` and one `lens_tag`.
4. Save a review CSV.
5. Apply tags only after approval or an explicit writeback request.
6. Verify the document tags after writeback.
7. Save a writeback log.

## Example Tags

| Domain | Lens |
| --- | --- |
| `ai` | `workflow-redesign` |
| `startups` | `growth` |
| `finance` | `hedge-funds` |
| `research` | `legal-data` |
| `personal-growth` | `self-hypnosis` |

## Guardrails

- Do not categorize from title alone.
- Do not use highlights as the main source for article categorization.
- Do not add more than two tags.
- Preserve existing user tags unless the task asks for strict cleanup.

