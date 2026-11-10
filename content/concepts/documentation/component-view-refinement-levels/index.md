---
title: Component View Refinement Levels
slug: component-view-refinement-levels
category: documentation
kind: practice
summary: A building block view is built in levels. Each level zooms into chosen blocks of the level above.
  Only important, risky, complex or volatile blocks get refined. Simple or standard parts are left out.
arc42:
- 5
step: s10-document
related:
- component-view
- nested-components-and-subsystems
- c4-model
- c4-container-diagram
- c4-level-3-component-diagram
- arc42-documentation-template
- uml-component-diagram
- package-diagram
checks:
- The building block view is a hierarchy of black boxes and white boxes, not a single diagram.
- Each deeper level zooms into selected blocks of the level above, not into every block.
- Refined blocks are the important, risky, complex or volatile ones.
- Simple or standardized parts are left out of the refinement.
sources:
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/
  title: Home | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Each level zooms into selected blocks of the level above.
review:
  status: generated
  flags: []
---

## Explanation

The arc42 building block view is not one diagram. It is a hierarchy of black boxes and white boxes. (See the Component View and Nested Components and Subsystems articles for the building blocks themselves.)

**How the levels work**

- Level 1 is the first breakdown of the system into blocks.
- Level 2 zooms into selected blocks of level 1.
- Level 3 zooms into selected blocks of level 2.
- Level 3 and further levels follow the same pattern; the template can be copied for more levels.

The word "selected" matters. You do not open every block at every level. Each deeper level covers only the blocks that need more explanation.

**How deep to go**

Relevance beats completeness. Refine a block when it is important, risky, complex or volatile. Leave out the normal, simple, boring or standardized parts.

**Comparison with C4**

The C4 model defines a set of hierarchical diagrams: system context, containers, components and code. See the C4 Model article for more.

## Example

A team documents an online shop. Level 1 shows a few main blocks, such as catalog, ordering, payment and a standard login component. Ordering is complex and changes often, so level 2 opens it and shows its inner parts. One of those parts is risky, so level 3 opens it too. Catalog, payment and the standard login stay as black boxes. The team does not draw them in more detail.
