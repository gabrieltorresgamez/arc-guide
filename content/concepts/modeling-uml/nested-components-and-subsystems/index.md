---
title: Nested Components and Subsystems
slug: nested-components-and-subsystems
category: modeling-uml
kind: notation-element
summary: A component can contain smaller parts that work together inside it. Ports on its edge pass outside
  requests to those parts. This lets you describe a system level by level, from a coarse view to detail.
arc42:
- 5
step: s10-document
related:
- uml-component-diagram
- component-port
- delegation-connector
- component-connector-assembly-and-delegation
- provided-and-required-interface
- c4-level-3-component-diagram
- component-view-refinement-levels
- structure-diagram
checks:
- The top-level building block view shows the whole system as a white box with all top-level blocks as
  black boxes.
- Selected blocks are refined in further levels, and each level is documented in its matching section
  5-n.
- Ports on a nested component's boundary are shown, and delegation to internal parts is clear.
sources:
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Composite_structure_diagram
  title: Composite structure diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-5-11/
  title: 'Question C-5-11: How does the hierarchy of building blocks relate to the arc42 sections (5.1,
    5.2 etc.)? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/abstractions/component
  title: Component | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A component with a boundary port that delegates to an inner part, which works with another
    inner part.
review:
  status: generated
  flags: []
---

## Explanation

**Structure from the inside.** In UML, a structured classifier is an element whose behavior can be described by how its internal parts interact.

**Ports.** A port is an interaction point. It connects a structured classifier with its parts and with its environment. A port can also delegate: it hands a request it received to an internal part. Outside callers deal with the port.

**Two views of the same thing.** From outside, you see a closed box. From inside, you see its parts. arc42, a documentation template, describes its building block view as a hierarchy of black boxes and white boxes:

- Level 1 is the white box description of the whole system, together with black box descriptions of all the building blocks it contains.
- Level 3 zooms into selected level-2 blocks, and so on.

arc42 also fixes where each level goes. Level n is documented in section 5-n. Level 0 is the context view. Level 1 is the top-level system view.

**Comparison with C4.** The C4 model defines a component as a group of related functionality behind a well-defined interface. Unlike a container, a C4 component is not deployed separately.

## Example

Imagine an online shop called "OrderSystem". Seen from outside, it is one box with one port that accepts orders.

Seen from inside, it holds two parts: "Cart" and "Catalogue". The port passes each incoming order request to "Cart". "Cart" works together with "Catalogue" to handle it. A reader of the top-level view needs only the box and its port. A reader who wants detail opens the box.

## Trade-offs

arc42 lets you zoom only into selected blocks, so you can stop where more detail adds little.
