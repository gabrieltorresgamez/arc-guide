---
title: Unclear Level of Abstraction Antipattern
slug: unclear-level-of-abstraction-antipattern
category: documentation
kind: concept
summary: An architecture diagram that mixes high-level and low-level elements confuses readers. The fix
  is to keep each diagram at one abstraction level and draw separate diagrams when both views are needed.
arc42:
- 5
- 7
step: s10-document
related:
- architectural-overview-antipatterns
- architectural-overview-diagram
- c4-model
- architecture-levels
- component-view-refinement-levels
- iso-iec-ieee-42010-architecture-description-standard
- distribution-view-antipatterns
- self-invented-notation-drawback
checks:
- Every element in each diagram belongs to the same abstraction level.
- High-level and low-level views are drawn as separate diagrams, not combined in one.
- Busy diagrams are split so each one focuses on one or two concerns.
- A reader can tell the element type of every element, such as software system or container.
- Each diagram has a title, a clear diagram type and a legend.
sources:
- url: https://www.ilograph.com/blog/posts/diagram-mistakes/
  title: 7 Common Mistakes in Architecture Diagrams | Ilograph Blog
  site: ilograph.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/checklist
  title: Review checklist | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://c4model.com/abstractions
  title: Abstractions | C4 model
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

A diagram has an abstraction level: how much detail its elements show. A whole system sits at a high level. A single part sits at a low level.

The antipattern appears when one diagram mixes high-level and low-level resources. Linking low-level resources directly to a high-level one is unbalanced and not very informative.

**Remedy**

Pick one abstraction level per diagram. If you want both a high-level and a low-level view, split them into two separate diagrams. If a diagram is busy, split it so each part covers one or two concerns.

**Zoom levels in C4 and arc42**

The C4 model (see C4 Model) gives every element a clear type. A software system contains containers, which are applications and data stores.

The arc42 building block view is organized in hierarchical levels. Level 1 shows the overall system as a white box, meaning you see inside it. Level 2 zooms into some level 1 building blocks. arc42 advises always describing level 1.

**Review and related mistakes**

The C4 review checklist asks whether you understand the type of every element, which is its abstraction level. The same checklist also covers related diagram problems: a missing title, an unclear diagram type and a missing legend.

## Example

Imagine one overview picture that shows a web shop as a whole, next to a single barcode scanner and a network router. Readers cannot tell whether it shows the system, the hardware or the setup.

The fix is to draw two diagrams. The first shows the shop as one box. The second zooms into the shop and shows its applications and data stores. Within each diagram, all elements sit at the same level.
