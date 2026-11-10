---
title: Layers and Components Decomposition
slug: layers-and-components-decomposition
category: styles-patterns
kind: concept
summary: Layers and components split a system two ways. Layers stack by kind of work, and upper layers
  use lower ones. Components are vertical slices that each cover one function. Together they form a grid.
arc42:
- 5
step: s10-document
related:
- layered-architecture
- layers-pattern
- modularity
- coupling-and-cohesion
- separation-of-concerns
- bounded-context
- domain-driven-design
- deriving-system-components-from-the-domain-model
checks:
- The building block view shows the static decomposition of the system, with level 1 as a white box of
  the whole system.
- Layer dependencies run top to bottom, and the document says layers are logical, not physical tiers.
- Blocks that are not detailed are shown as black boxes with their inner workings hidden.
sources:
- url: https://martinfowler.com/bliki/PresentationDomainDataLayering.html
  title: Presentation Domain Data Layering
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Layers (rows) and components (columns) form a grid. Each component has a slice in every layer.
review:
  status: generated
  flags: []
---

## Explanation

**Layers.** A layer groups code by kind of work. One common split has three broad layers: presentation (the user interface), domain logic (the business rules), and data access. Dependencies generally run from top to bottom: presentation depends on the domain, which depends on the data source. A mapper between the domain and data layers can reverse the second dependency.

Layers are logical. They organize the code. They do not describe physical deployment tiers.

**Domain-oriented modules.** For large systems, one suggestion is to split the top level into domain-oriented modules and then layer each module internally. Separately, Domain-Driven Design divides a large system into Bounded Contexts, each with a unified model. See the articles Domain-Driven Design and Bounded Context.

**Documenting it.** The arc42 building block view shows how the system is statically broken down into building blocks. It is hierarchical. Level 1 is a white box of the whole system. Deeper levels zoom into chosen blocks. For blocks you do not open up, arc42 advises hiding their inner workings.

## Example

An online shop uses three layers: presentation, domain logic, and data access. Its components are Catalog, Orders, and Payment. The Orders component has its own screens, its own order rules, and its own data access. The Orders screens call the Orders rules. The Orders rules call the Orders data access. The building block view lists Catalog, Orders, and Payment at level 1. A deeper level can zoom into Orders.

## Trade-offs

One point is clear: layers are a logical structure only. Do not read them as a deployment plan.
