---
title: Architectural Overview Antipattern
slug: architectural-overview-antipatterns
category: documentation
kind: concept
summary: An overview diagram fails when readers cannot tell what it shows. Common causes are unclear scope,
  cryptic labels, and unexplained notation. Fix it with a title, a legend, plain names, and several simpler
  diagrams.
arc42:
- 5
- 3
step: s10-document
related:
- architectural-overview-diagram
- c4-model
- self-invented-notation-drawback
- ubiquitous-language
- arc42-glossary
- context-view-antipatterns
- unclear-level-of-abstraction-antipattern
- uml-modeling-anti-patterns
checks:
- Every overview diagram has a title that states its type and scope.
- Every diagram has a legend explaining the notation, including line styles.
- Acronyms and abbreviations are understandable to all intended readers.
- Every line is labeled, and the label fits the direction and intent of the relationship.
- Detail is added step by step across levels instead of packed into one diagram.
sources:
- url: https://c4model.com/diagrams/notation
  title: Notation | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/checklist
  title: Review checklist | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An architectural overview diagram (see Architectural Overview Diagram) shows the main parts of a system as boxes and lines. Several habits make these diagrams hard to read.

**Unclear scope and boundaries.** Readers cannot tell what the diagram covers. The C4 Model asks for a title on every diagram. The title states the diagram type and its scope.

**Cryptic names.** Labels such as "NLB" or "App-Srv" only work for insiders. C4 says acronyms and abbreviations should be understandable to all audiences.

**Unexplained notation.** C4 does not prescribe a notation. So a diagram that uses its own shapes or line styles must explain them. C4 asks for a key (legend) on every diagram. Its checklist also asks whether readers understand every line style, such as solid or dashed.

**Unlabeled lines.** C4 asks that every line carries a label. The label should match the direction and intent of the relationship. A bare arrow leaves readers guessing.

**Too much at once.** arc42 handles this in its building block view with hierarchical levels. Level 1 shows the big blocks. Level 2 zooms into some of them, and deeper levels follow. Each step adds detail. arc42 also notes that abstraction lets you talk to stakeholders without exposing implementation detail. Choose the level that fits the audience.

## Example

A team draws one picture of its online shop. It has dozens of boxes, arrows crossing everywhere, and labels like "NLB" and "Data Srv." Nothing says where the shop ends, and the line styles are never explained.

The team redraws it. A first diagram has a title naming its type and scope, and shows only a few large blocks with plain names. A second diagram zooms into one block. Every line has a label, and a legend explains each line style.

## Trade-offs

Abstraction hides implementation detail, so readers who need that detail must look at a deeper level.
