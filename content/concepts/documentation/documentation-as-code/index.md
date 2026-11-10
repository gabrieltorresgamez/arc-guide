---
title: Documentation as Code
slug: documentation-as-code
category: documentation
kind: practice
summary: 'Documentation as code means writing documentation with the same tools and workflows as software:
  plain-text markup, Git, code review, and automated builds. Docs become versioned, reviewable, and publishable
  by tools.'
arc42:
- 1
- 8
- 12
step: s10-document
related:
- diagrams-as-code
- arc42-documentation-template
- guidelines-for-documentation
- kroki
- c4-model
- motivation-for-architecture-documentation
checks:
- Documentation sources are plain-text markup (for example AsciiDoc or Markdown) kept in a version control
  system such as Git.
- Changes to the documentation are proposed and reviewed through pull requests.
- Documents such as HTML or PDF are built automatically from the text sources by a toolchain.
- Diagrams are generated from text and included in the documentation instead of being copied.
sources:
- url: https://www.writethedocs.org/guide/docs-as-code/
  title: Docs as code — Write the Docs
  site: writethedocs.org
  accessed: '2026-11-09'
- url: https://doctoolchain.org/docToolchain/v2.0.x/010_manual/single-page.html
  title: docToolchain Manual
  site: doctoolchain.org
  accessed: '2026-11-09'
- url: https://docs.asciidoctor.org/asciidoctor/latest/
  title: Asciidoctor Documentation | Asciidoctor Docs
  site: docs.asciidoctor.org
  accessed: '2026-11-09'
- url: https://examples.arc42.org/systems/doctoolchain-v4/
  title: docToolchain v4 · arc42 Examples
  site: examples.arc42.org
  accessed: '2026-11-09'
- url: https://doctoolchain.org/docToolchain/v2.0.x/
  title: docToolchain
  site: doctoolchain.org
  accessed: '2026-11-09'
- url: https://arc42.org/documentation/
  title: arc42 Documentation - arc42
  site: arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Docs-as-code flow from plain-text source to published document
review:
  status: generated
  flags: []
---

## Explanation

Documentation as code (also called docs as code) is a philosophy. You write documentation with the same tools you use to write code. That means plain-text markup such as AsciiDoc, a version control system such as Git, code review, and automated tests.

**Version control.** Git tracks every change to the text. One toolchain manual notes that this gives you a document management system without extra tooling.

**Same workflow as development.** Others can fork the docs and send pull requests with their changes. A pull request is a proposed change that teammates review before it is accepted. Because docs follow the developer workflow, a team can block a feature from merging when it lacks documentation.

**From text to document in three steps.** You write the source. A converter such as Asciidoctor parses AsciiDoc into a document model. It then converts that model into formats such as HTML5, DocBook 5, PDF and EPUB 3. The asciidoctor-pdf plugin produces the PDF output.

**Diagrams from text.** docToolchain uses the asciidoctor-diagram plugin to create PlantUML diagrams from text. See the article Diagrams as Code.

**Toolchains.** docToolchain is a docs-as-code toolchain. It publishes AsciiDoc to HTML, PDF, microsites and Confluence. It uses jBake as its static site generator. It also supports teams who want docs as code but still use a wiki.

**Fit with arc42.** arc42 works well with this approach. Its AsciiDoc or Markdown templates live in Git. Pull requests review them. docToolchain or any static-site generator builds them. See the article arc42 Architecture Documentation Template.

## Example

A team keeps its architecture documentation as AsciiDoc files in a Git repository. A developer changes a service and edits the matching text in the same branch. A teammate reviews both changes in one pull request. After the merge, an automated build converts the text to HTML and PDF.

## Trade-offs

One point is visible. For teams that want docs as code but also use a wiki, docToolchain can publish to Confluence.
