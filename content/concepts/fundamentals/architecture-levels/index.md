---
title: Architecture Level
slug: architecture-levels
category: fundamentals
kind: concept
summary: Architecture can be described at several levels of detail. In arc42's building block view, each
  deeper level zooms into selected parts of the level above, and you only zoom where it matters.
arc42:
- 5
step: s10-document
related:
- arc42-documentation-template
- component-view-refinement-levels
- c4-model
- nested-components-and-subsystems
- software-architecture-basic-concepts
- unclear-level-of-abstraction-antipattern
- levels-of-architectural-decisions
- component-view
checks:
- Each deeper level of the building block view zooms into selected blocks of the level above.
- The hierarchy continues to further levels only where details of a block need describing.
- Blocks chosen for a lower-level description are important, risky, complex or volatile; other blocks
  are not forced to have one.
sources:
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Each level zooms into selected blocks of the level above.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

An architecture level is a degree of detail. You start with the whole system and move step by step toward its inner parts.

arc42 shows this in its building block view (see the article on the arc42 Architecture Documentation Template). A building block is a part of the system, such as a component or subsystem. The view is hierarchical:

- Level 1 shows the overall system split into its main building blocks.
- Level 2 zooms into some of the level 1 blocks and shows their insides.
- Level 3 zooms into some of the level 2 blocks, and so on.

Each level adds detail to selected blocks of the level above. The hierarchy can continue as deep as needed, so levels can be subdivided further.

You do not have to zoom into every block. arc42 advises describing only the blocks that matter. These are blocks that are important, surprising, risky, complex or volatile. Normal, simple or standardized parts can be left out.

## Example

A team documents an online shop. Level 1 shows a few large blocks: storefront, orders, payments and catalog. Payments is risky and complex, so level 2 zooms into it and shows its inner parts. One of those parts is especially tricky, so level 3 zooms into it. The catalog is simple, so it gets no lower-level description.

## Trade-offs

arc42 advises preferring relevance over completeness, so only important, risky, complex or volatile blocks are zoomed into.
