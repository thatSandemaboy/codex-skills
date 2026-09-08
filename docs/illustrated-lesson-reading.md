# Illustrated Lesson Reading

## Install and use

From the repository root:

```sh
./scripts/install-skill.sh illustrated-lesson-reading
```

The installer replaces an existing installed folder with the same name. Back up local customizations first. Installing is unnecessary if you already have the skill and do not want to replace that copy.

Ask Codex:

> Use $illustrated-lesson-reading to turn this Markdown lesson into a continuous illustrated HTML reading. Keep the source content intact.

Provide the source file or notes. Output is a standalone HTML reading; the source Markdown is preserved. Publishing is a separate, explicitly requested action.

## What the package contains

- `SKILL.md`: reading-first workflow and fidelity requirements.
- `references/design.md`: typography, color, spacing, and diagram rules.
- `assets/approved-reading.html`: public-safe recipe sample using the approved stylesheet.
- `references/approved-source.md`: matching sample Markdown.
- `assets/example-body.html`: semantic HTML fragment for reproducing the sample.
- `scripts/build_reading.py`: Python standard-library wrapper, contents builder, and anchor checks.
- `agents/openai.yaml`: skill display metadata.

The public sample is newly authored generic content, not a copy of private lesson notes. The original approved CSS is retained.

## Reproduce the sample

From the repository root, with Python 3 available:

```sh
python3 skills/illustrated-lesson-reading/scripts/build_reading.py \
  --content skills/illustrated-lesson-reading/assets/example-body.html \
  --source skills/illustrated-lesson-reading/references/approved-source.md \
  --output skills/illustrated-lesson-reading/assets/approved-reading.html \
  --title "Scaling a recipe" \
  --subtitle "How can a recipe serve a different number of people while keeping its proportions?" \
  --label "Sample · Proportions" \
  --collection "Illustrated reading"
```

The builder wraps an authored HTML fragment; it does not automatically translate Markdown or decide which diagrams teach well. It checks duplicate IDs and local anchors. Content fidelity, math, accessibility, and visual layout still need review.

Keep the whole skill folder together: the builder reads its stylesheet from the bundled HTML asset. No external fonts, scripts, or Python packages are needed.
