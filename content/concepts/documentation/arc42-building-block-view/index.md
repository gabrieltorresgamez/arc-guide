---
title: arc42 Building Block View
slug: arc42-building-block-view
order: 60
category: documentation
kind: artifact
summary: Chapter 5 of arc42 shows the static structure of the system as building blocks and their dependencies. arc42 calls it mandatory and compares it to the floor plan of a house.
arc42:
- 5
step: s10-document
related:
- component-view
- architecture-levels
- arc42-documentation-template
- arc42-context-and-scope
- arc42-solution-strategy
- runtime-view
checks:
- The documentation contains a building block view with a level 1 white box of the whole system.
- Each building block shown has a black box description, as a table or as a list.
- Deeper levels exist only for selected building blocks.
- Dependencies between building blocks are shown.
sources:
- url: https://docs.arc42.org/section-5/
  title: "5 - Building block view | arc42 Documentation"
  site: docs.arc42.org
  accessed: '2026-11-16'
- url: https://docs.arc42.org/tips/5-2/
  title: "Tip 5-2: Organize the building block view hierarchically! | arc42 Documentation"
  site: docs.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The building block view shows the static decomposition of a system into building blocks and their dependencies. A building block can be a module, component, subsystem, class, interface, package, library, layer or a similar part. arc42 calls this view mandatory for every architecture documentation. In analogy to a house, it is the floor plan.

**Why it exists.** It keeps the source code understandable through abstraction. Teams can talk with stakeholders at an abstract level without exposing implementation details.

**How it is built.** The view is a hierarchy of black boxes and white boxes with their descriptions.

- **Level 1** is the white box description of the whole system, together with black box descriptions of all building blocks inside it.
- **Level 2** zooms into some building blocks of level 1. It holds their white box descriptions and black box descriptions of their inner building blocks.
- **Level 3** zooms into selected building blocks of level 2, and so on.

**Section 5.1, the whole system.** Its white box template has an overview diagram, a motivation for the decomposition, and black box descriptions of the contained building blocks. For the black boxes arc42 offers two choices: one table for a short and pragmatic overview, or a list of black box descriptions. The section can also list important interfaces that no black box description explains.

See the articles Component View and Architecture Level for how views and levels relate to this chapter.

## Example

A small web shop shows the shop system at level 1 as a white box with three black boxes: web interface, order service and payment adapter. A table lists each building block with its responsibility and its interfaces. Only the order service gets a level 2, because it is the block the team needs to explain.

## Trade-offs

arc42 asks for relevance over completeness. Detail goes only to building blocks that are important, risky or complex.
