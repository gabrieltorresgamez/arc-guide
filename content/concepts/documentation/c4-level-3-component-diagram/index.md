---
title: C4 Component Diagram
slug: c4-level-3-component-diagram
category: documentation
kind: notation-element
summary: A C4 component diagram opens up one container and shows the components inside it, with their
  responsibilities and technology. Teams draw it only when it adds value.
arc42:
- 5
step: s10-document
related:
- c4-model
- c4-container-diagram
- c4-level-4-code-diagram
- c4-level-1-system-context-diagram
- uml-component-diagram
- diagrams-as-code
- documentation-as-code
checks:
- Each component diagram zooms into exactly one container and shows the components inside it with their
  responsibilities and technology.
- The diagram shows the directly connected containers, people, and software systems around the components.
- Component diagrams exist only for containers where they add value.
- For long-lived documentation, the team has considered automating diagram creation.
sources:
- url: https://c4model.com/diagrams/component
  title: Component diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.c4.puml
  caption: Generic component diagram of one container with its surrounding elements.
review:
  status: generated
  flags: []
---

## Explanation

A component diagram is the third level of the C4 model (see the article C4 Model). It zooms into one container. The component diagram decomposes that container into the components that live inside it.

Each component is described with its responsibilities and technology or implementation details.

The diagram also shows its surroundings. These supporting elements are:

- the other containers of the system in scope,
- people who connect directly to the components,
- software systems that connect directly to the components.

**Create it only when it helps.** The C4 guidance says to draw component diagrams only if you feel they add value.

**Automate for long-lived documentation.** If the documentation must last, consider generating these diagrams instead of drawing them by hand.

**Link to arc42.** The arc42 building block view has a level 2. It zooms into some of the level 1 building blocks.

## Example

An online shop has a container called "Order Service". Its component diagram shows three components: one that accepts orders, one that calculates prices, and one that talks to the payment provider. Arrows connect them. Outside the box sit the "Web Shop" container, the "Order Database" container, and the external payment system. The "Customer Service" container has no component diagram, because the team saw no gain.

## Trade-offs

A component diagram gives readers detail about one container. The C4 guidance recommends drawing it only where it adds value. For documentation that must last, consider automating its creation.
