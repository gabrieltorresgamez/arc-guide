---
title: Diagrams as Code
slug: diagrams-as-code
category: documentation
kind: practice
summary: Diagrams as code means writing architecture diagrams as plain text. A toolchain renders the text
  into pictures. Teams can then store, compare, and build diagrams like source code.
arc42:
- 3
- 5
- 6
- 7
step: s10-document
related:
- documentation-as-code
- modeling-tool-vs-drawing-tool
- model-vs-view
- c4-model
- kroki
- diagram-metadata-in-png-drawio-png
- architecture-view
- self-documentation
checks:
- Diagrams are stored as plain text in version control, not only as binary or hard-to-compare files.
- Views are generated from one shared model, so the diagrams stay consistent with each other.
- Generated diagrams are regenerated automatically before the documentation build.
- The document states which renderer produces the diagrams, and styles are checked against that renderer.
sources:
- url: https://c4model.com/tooling
  title: Tooling | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.asciidoctor.org/diagram-extension/latest/
  title: Overview | Asciidoctor Docs
  site: docs.asciidoctor.org
  accessed: '2026-11-09'
- url: https://docs.structurizr.com/dsl/cookbook/
  title: Cookbook | Structurizr
  site: docs.structurizr.com
  accessed: '2026-11-09'
- url: https://docs.structurizr.com/dsl/language
  title: Language reference | Structurizr
  site: docs.structurizr.com
  accessed: '2026-11-09'
- url: https://www.codecentric.de/en/knowledge-hub/blog/architecture-documentation-as-code-with-structurizr-and-asciidoctor-part-3-structurizr
  title: 'Structurizr & C4-PlantUML: Architecture as Code'
  site: codecentric.de
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: One text model produces several views, which a renderer turns into images for the documentation.
review:
  status: generated
  flags: []
---

## Explanation

Many diagramming tools save diagrams in formats that are hard to compare. That makes them tricky to use with pull requests.

**Text embedded in documents.** Asciidoctor Diagram is a set of extensions for Asciidoctor, a tool that builds AsciiDoc documents. It renders plain-text diagrams from inside those documents. To do this, it calls external renderers.

**One model, many views.** A second approach starts from a model, not from single drawings. A modelling tool builds a non-visual model of the software architecture. Pure drawing tools only produce boxes and lines. With a model, renaming elements is easy and the tool can validate what you draw. See Modeling Tool vs. Drawing Tool and Model vs. View.

Structurizr DSL follows this approach. It is a text language that creates diagrams from one consistent model. A workspace has these parts:

- A `model` block. It is required. It defines elements and relationships.
- A `views` block. It holds one or more views. Defining any view removes the default set. Inside it, a `styles` block sets how elements and relationships look.

Layout can be automatic. You add the `autoLayout` statement inside a view.

**Renderers differ.** Image views in Structurizr DSL can take PlantUML, Mermaid, or Kroki sources and render them through those services, with png or svg output. Some styles are made for the Structurizr tools. PlantUML or Mermaid exports may not support them fully. See Kroki.

**Keeping diagrams current.** One published example generates its views from a single Structurizr model as C4-PlantUML diagrams. The Asciidoctor task depends on the task that writes the diagrams, so the diagrams are written before the documentation is generated.

## Example

A team keeps one text file that describes its system: a web shop, a payment service, and the links between them. The file defines two views, an overview and a detail view. Before each documentation build, a script renders both views into images. When the team renames the payment service, it edits one line. Both views update on the next build. A reviewer sees the rename as a small text change in the pull request.

## Trade-offs

One benefit stands out. A single model makes renaming easy and lets tools validate the diagrams.

There is also a cost. Renderers do not support every style equally, so the same model can look different in the Structurizr tools, PlantUML, or Mermaid.
