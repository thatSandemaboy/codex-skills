# Illustrated lesson design

Reference implementation: `../assets/approved-reading.html` within this skill.

The lesson is a continuous reading of its source Markdown. Keep the explanations, examples, and reflection questions. Add a visual only when it makes a relationship easier to understand at that point in the text. Activities must not replace the reading.

## Visual language

- Pure white page and diagram surfaces: `#ffffff`.
- All ordinary text, including secondary text, captions, navigation, and quotations: pure black `#000000`. Establish hierarchy with size, weight, and spacing rather than gray text.
- Hairline dividers: `#e8eaec`.
- Reserve color for meaningful highlights, links, and diagram accents: muted teal `#386968` and blue `#536b8a`. Keep the background pure white.
- Editorial serif prose with quiet, compact sans-serif navigation and labels; inspired by newspaper typography and Linear/Attio's restraint.
- Use Georgia with Times New Roman and serif fallbacks. This is an available editorial typeface, not a claim to use the New York Times' proprietary fonts.

## Typography and spacing

- Body: 18px equivalent (`1.125rem`), regular weight, 1.75 line height; 17px on narrow screens.
- Reading measure: 660px maximum. Diagrams may extend to the article width.
- Main title: responsive 35–50px, regular serif, 1.13 line height.
- Section heading: about 26px, regular serif. No repeated numbered eyebrow above it.
- Subheading: 15px medium sans serif. Navigation: 13px. Diagram labels: 13–14px; captions: 13px.
- Use relative font sizes so browser text enlargement remains usable.
- Paragraph gap: 17px. Section transition: approximately 39px total; no mandatory divider.
- Reserve emphasis for definitions and essential distinctions.

## Containers and diagrams

- No decorative shadows, tinted cards, large corner radii, or background panels.
- Diagrams sit on the white page. Preserve thin outlines only where they identify a component, boundary, or flow.
- Diagram nodes may use a 4px radius and a restrained colored border for a meaningful distinction.
- Notes and quotations use a single hairline at the left.
- Captions explain the visual and any simplifying assumption. They are adjacent to the diagram.
- Avoid 3D unless depth carries information that a simpler diagram cannot convey as clearly.

## Reading behavior

- Everything is readable in order without clicking through chapters.
- The desktop contents list is small, sticky, and optional; hide it on narrow screens.
- Reflow diagrams vertically on phones. Keep all labels readable and preserve the relationships.
- Preserve keyboard access, semantic headings, figure captions, reduced-motion behavior, and print styles.
- Prefer a standalone HTML file with no external font or script dependency.
- Keep future lessons on this reading-first pattern unless the user asks to change it.
