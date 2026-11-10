---
title: Diagram Metadata in PNG (drawio.png)
slug: diagram-metadata-in-png-drawio-png
category: documentation
kind: practice
summary: A .drawio.png file is a normal PNG image that also carries its own draw.io diagram source. You
  can show it in documentation and reopen it for editing. Plain XML or SVG files suit Git better.
arc42:
- 5
- 6
- 7
- 8
step: s10-document
related:
- documentation-as-code
- diagrams-as-code
- modeling-tool-vs-drawing-tool
- kroki
- guidelines-for-documentation
- self-documentation
checks:
- Diagrams meant to stay editable are saved as .drawio.png and were exported with the 'Include a copy
  of my diagram' option enabled.
- The documentation names an editor that can reopen the embedded diagrams, such as VS Code with the Draw.io
  Integration extension.
- Where readable Git diffs matter, the team uses plain .drawio files instead of .drawio.png.
- Images that pass through image hosts are checked, because resampling can strip the embedded source.
sources:
- url: https://www.drawio.com/docs/manual/export/xml-in-png/
  title: Embedded XML in PNG image files | draw.io
  site: drawio.com
  accessed: '2026-11-09'
- url: https://github.com/hediet/vscode-drawio
  title: 'GitHub - hediet/vscode-drawio: This unofficial extension integrates Draw.io (also known as diagrams.net)
    into VS Code. · GitHub'
  site: github.com
  accessed: '2026-11-09'
- url: https://www.drawio.com/docs/manual/collaboration/diagram-data-image-formats/
  title: Share diagram data in an image file | draw.io
  site: drawio.com
  accessed: '2026-11-09'
- url: https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/recipes/preferred-diagram-tooling/
  title: Preferred Diagram Tooling - Engineering Fundamentals Playbook
  site: microsoft.github.io
  accessed: '2026-11-09'
- url: https://github.com/lukecarrier/mkdocs-drawio-exporter
  title: 'GitHub - LukeCarrier/mkdocs-drawio-exporter: Exports your Draw.io diagrams at build time for
    easier embedding into your documentation · GitHub'
  site: github.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Draw.io is a diagramming tool. It can hide the diagram's XML source inside an image file. It places that XML in the `zTxt` section of the file, a text area that is not part of the picture itself.

Because the source travels with the image, the file keeps everything needed for further editing. The file displays like a normal PNG in browsers and other viewers, so it is easy to transfer and embed.

**How to create one**

When you export to PNG, keep the option *Include a copy of my diagram* enabled. Without it, you cannot reopen the file for editing in draw.io. Editable SVG exports need the same checkbox.

**How to edit one**

The Draw.io Integration extension for VS Code can edit and save `.drawio.png` and `.drawio.svg` files directly.

**Things to watch**

Some image hosts resample PNGs. That can strip the embedded data and leave a plain picture.

**Alternatives**

- Plain `.drawio` files are XML. They diff cleanly in Git.
- `.drawio.svg` files are valid SVGs. You can embed them in GitHub READMEs.

**Automation**

A MkDocs plugin exported draw.io diagrams while building documentation. This shows that export can be automated. The repository is now archived.

## Example

A team keeps its context diagram as `context.drawio.png` in the docs folder. The README shows it as a normal image. When the system changes, an engineer opens the same file in VS Code, edits the boxes, and saves. No separate export step is needed. The team made sure the *Include a copy of my diagram* option was on when they exported.

## Trade-offs

The main benefit is one file that serves as both image and source. The VS Code extension recommends plain `.drawio` files over `.drawio.png` when you want readable diffs for reviewers and AI tools. Image hosts that resample PNGs may also strip the embedded source. Choose `.drawio.png` for convenience, and plain `.drawio` when review and diffs matter most.
