"""Wrap an authored lesson fragment in the approved editorial HTML style."""
import argparse
import html
from html.parser import HTMLParser
from pathlib import Path
import os
import re
from urllib.parse import quote, unquote


class ReadingStructure(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.anchors = []
        self.headings = []
        self.heading = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        identity = attrs.get("id")
        if identity:
            if identity in self.ids:
                raise ValueError(f"Duplicate HTML ID: {identity}")
            self.ids.add(identity)
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.anchors.append(unquote(attrs["href"][1:]))
        if tag == "h2":
            if not identity:
                raise ValueError("Each H2 needs a unique ID for the contents list")
            self.heading = [identity, []]

    def handle_data(self, data):
        if self.heading is not None:
            self.heading[1].append(data)

    def handle_endtag(self, tag):
        if tag == "h2" and self.heading is not None:
            identity, pieces = self.heading
            label = " ".join("".join(pieces).split())
            if not label:
                raise ValueError(f"Empty H2: {identity}")
            self.headings.append((identity, label))
            self.heading = None


def build(args):
    content_path = Path(args.content).resolve()
    source = Path(args.source).resolve()
    output = Path(args.output).resolve()
    if output in (source, content_path):
        raise ValueError("Output must not overwrite source Markdown or the HTML fragment")
    if not source.is_file():
        raise ValueError(f"Source file does not exist: {source}")
    content = content_path.read_text(encoding="utf-8")
    if re.search(r"<\s*(?:html|head|body)\b", content, re.I):
        raise ValueError("Content must be an HTML fragment, not a full document")
    structure = ReadingStructure()
    structure.feed(content)
    structure.close()
    if not structure.headings:
        raise ValueError("Content needs at least one H2 heading")
    if structure.ids & {"reading", "lesson-title"}:
        raise ValueError("The shell reserves the IDs reading and lesson-title")
    approved = Path(__file__).resolve().parent.parent / "assets" / "approved-reading.html"
    reference = approved.read_text(encoding="utf-8")
    match = re.search(r"<style>(.*?)</style>", reference, re.S)
    if not match:
        raise ValueError("The approved reference is missing its inline stylesheet")
    css = match.group(1)
    escape = html.escape
    source_href = quote(os.path.relpath(source, output.parent).replace(os.sep, "/"), safe="/")
    nav = "\n".join(
        f'<a href="#{quote(identity, safe="-_:.~")}">{escape(label)}</a>'
        for identity, label in structure.headings
    )
    rendered = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(args.subtitle, quote=True)}">
<title>{escape(args.title)} · Illustrated Reading</title>
<style>{css}</style>
</head>
<body>
<a class="skip" href="#reading">Skip to reading</a>
<header class="masthead">
  <div class="publication">Learning notes <span>{escape(args.collection)}</span></div>
  <a class="source-link" href="{source_href}">Original Markdown ↗</a>
</header>
<div class="layout">
  <aside class="contents" aria-label="Contents">
    <div class="eyebrow">In this lesson</div>
    <nav>{nav}</nav>
  </aside>
  <article id="reading" aria-labelledby="lesson-title">
    <header class="hero measure">
      <div class="eyebrow">{escape(args.label)}</div>
      <h1 id="lesson-title">{escape(args.title)}</h1>
      <p class="standfirst">{escape(args.subtitle)}</p>
    </header>
{content}
    <footer class="closing measure">
      <a href="{source_href}">Read the original Markdown ↗</a>
    </footer>
  </article>
</div>
</body>
</html>
'''
    final = ReadingStructure()
    final.feed(rendered)
    final.close()
    broken = set(final.anchors) - final.ids
    if broken:
        raise ValueError(f"Broken local links: {', '.join(sorted(broken))}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    print(f"Created {output} with {len(structure.headings)} contents entries.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for flag in ("content", "source", "output", "title", "subtitle", "label"):
        parser.add_argument(f"--{flag}", required=True)
    parser.add_argument("--collection", default="Learning notes")
    build(parser.parse_args())
