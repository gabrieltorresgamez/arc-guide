---
title: Component View
slug: component-view
category: documentation
kind: artifact
summary: 'A component view shows how a system is built from parts. In arc42 it is the mandatory building
  block view: a hierarchy of black boxes and white boxes that makes source code structure understandable
  through abstraction.'
arc42:
- 5
step: s10-document
related:
- c4-level-3-component-diagram
- c4-model
- arc42-documentation-template
- component-view-refinement-levels
- uml-component-diagram
- nested-components-and-subsystems
- architecture-view
- component-view-antipattern-lifting-code-to-model-level
checks:
- The architecture document contains a building block view, since it is mandatory in arc42.
- The building block view is organized as a hierarchy of black boxes and white boxes, each with a description.
- Deeper levels zoom only into selected building blocks of the level above.
- C4 component diagrams exist only where they add value.
sources:
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/component
  title: Component diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Refinement from a black box to selected inner blocks.
review:
  status: generated
  flags: []
---

## Explanation

A component view describes the internal structure of a system. It helps readers keep an overview of the source code by making its structure understandable through abstraction.

In arc42, this view is called the building block view. It is a mandatory part of the template. See the article arc42 Architecture Documentation Template for the full chapter list.

**Black boxes and white boxes**

The view is a hierarchy of black boxes and white boxes, each with a description. A black box shows a building block from the outside. A white box opens it up and shows the blocks inside.

**Refinement level by level**

The view starts with a coarse picture. You then zoom into selected blocks, one level at a time. Level 3, for example, zooms into details of selected blocks from level 2. This continues as far as it is useful.

**In C4**

The C4 Model also has component diagrams. They are optional. You create them only when they add value. See the article C4 Component Diagram for details.

## Example

A team documents an online shop. Level 1 treats the shop as one black box. Level 2 opens it as a white box with three blocks: catalog, orders and payments. The team then zooms into "orders" only, because it is the most complex part. That gives level 3. They leave "catalog" and "payments" as black boxes.

## Trade-offs

In arc42, you should prefer relevance over completeness and zoom only into the important building blocks. In C4, component diagrams are optional: create them only when they add value.
