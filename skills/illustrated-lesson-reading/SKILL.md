---
name: illustrated-lesson-reading
description: Turn lesson Markdown or reading notes into a polished, continuous HTML reading page using the user's approved white-background, black-text editorial style, with diagrams where they improve comprehension. Use when formatting other lessons like the approved illustrated reading. Not an activity-first lab or course dashboard.
---

# Illustrated lesson reading

Create a beautiful reading of the source notes. Preserve the learning content; make its relationships easier to see. Reading is the primary experience; activities and visuals support it rather than replace it.

## Read and reuse

1. Read the requested source notes completely. Resolve which lesson or lessons the user placed in scope; do not automatically convert the whole course.
2. Read `references/design.md`. Inspect `assets/approved-reading.html` for its exact CSS, page structure, and diagram vocabulary. Its recipe-scaling content is a public-safe example, not content to copy into other lessons. `references/approved-source.md` contains the corresponding Markdown for fidelity comparisons; `assets/example-body.html` is the authored fragment used to reproduce the sample. The sample retains the approved stylesheet without publishing private lesson notes.
3. Keep the source's definitions, explanations, examples, equations, caveats, and reflection questions. Preserve their logical order. Improve presentation without silently shortening the lesson or drafting assignment submissions. Label any substantive clarification rather than silently changing a contested teaching claim.

## Reading is the primary experience

- The entire lesson is readable by scrolling. No next-chapter gate, mandatory interaction, quiz progression, or exercise replacing an explanation.
- Use a modest title and introduction, quiet desktop contents list, continuous prose, and optional reflection questions at the end when present in the source.
- White page and surfaces (`#ffffff`), black ordinary text (`#000000`), including captions and navigation. Hierarchy comes from spacing, size, and restrained weight—not gray text.
- Georgia prose, 18px / 1.75 line height, 660px reading measure; 17px on phones. Regular serif headings, compact system sans-serif labels. The look combines newspaper reading typography with Linear/Attio restraint; do not claim proprietary New York Times fonts.
- Keep colored links and meaningful teal/blue highlights. Avoid decorative shadows, tinted cards, thick dividers, repeated numbered labels, oversized headings, and large corner radii.
- Preserve the approved CSS rather than redesigning from memory. Apply a new user preference when explicitly requested.

## Add visuals selectively

Ask what relationship a visual makes easier to understand at this exact point in the reading. Suitable choices include a flow for training, a component diagram for model parameters, a labeled plot for regression, or a table for precise comparisons.

- Put each diagram adjacent to the explanation it supports, with a short caption and any simplifying assumption.
- Use the smallest useful visual. No fixed diagram quota: include only visuals that clarify the particular source.
- Diagrams sit on the white page. Thin outlines may identify components; semantic color can distinguish roles. Reuse the reference's `.lane`, `.node`, `.model-flow`, `.flow-loop`, and `.phase-comparison` patterns where appropriate.
- Add 3D or interactivity only when it materially improves understanding beyond a static view. Keep the prose complete and provide a readable default/fallback. Do not turn the output into a lab.
- Label axes, units, inputs, outputs, and arrows accurately. Numerical illustrations must agree with the source and calculations. Avoid implying causation, certainty, or universal rules that the source does not establish.

## Build

Create a standalone HTML file near the source, normally `Lesson N - Illustrated Reading.html`. Preserve the Markdown and unrelated earlier variants. Update an existing illustrated reading when requested.

Author a semantic HTML fragment containing the lesson's sections. Use `<section class="section">`, a unique ID on each `<h2>`, `.measure.prose` for the text column, and captioned `<figure>` elements outside that narrow column when useful. Escape source text and code properly.

Use `scripts/build_reading.py` to wrap the fragment in the exact approved styling. It derives the contents list from H2 headings and computes the relative source link:

```sh
python3 scripts/build_reading.py \
  --content /absolute/path/lesson-body.html \
  --source /absolute/path/lesson.md \
  --output /absolute/path/lesson-illustrated.html \
  --title "Lesson title" \
  --subtitle "The lesson's central question" \
  --label "Lesson 02 · Linear regression" \
  --collection "Week 1 · Foundations"
```

Use an available Python runtime; no extra packages are required. The helper supports static diagrams via the approved CSS and inline SVG. If a lesson needs genuinely useful custom visuals, extend narrowly while retaining this reading structure and design.

## Verify and hand off

- Compare the rendered reading content with the source: no omitted concepts, examples, equations, or reflection prompts.
- Check headings, internal links, accessible diagram descriptions, mobile reflow, black text on white, and mathematical consistency. The builder checks duplicate IDs and broken local anchors; it cannot judge content fidelity or visual quality.
- If browser inspection is available and permitted, check representative desktop and narrow layouts. If local browser access is blocked, do not bypass it or claim visual verification; perform the remaining structural checks.
- Link the completed local HTML and open it in the app's file preview if useful. Existing tabs may need refreshing.
- This skill does not imply hosting, repository creation, publishing, or course-wide conversion. Do those only when the user's request includes them.
