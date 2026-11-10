---
title: Differences between Class, Component and Package Diagrams
slug: class-component-and-package-diagram-differences
category: modeling-uml
kind: concept
summary: Component and package diagrams both show building blocks and can express hierarchies, because
  components and packages can be nested. Each one connects or groups blocks in a different way. Both fit
  the arc42 building block view.
arc42:
- 5
step: s10-document
related:
- class-diagram
- uml-component-diagram
- package-diagram
- provided-and-required-interface
- package-relationships-import-access-merge-use
- nested-components-and-subsystems
- structure-diagram
- matching-diagram-type-to-system-aspect
checks:
- Every piece of source code has a place in the building block view.
- 'The building block view is hierarchical: level 1 is the whitebox of the overall system, and lower levels
  zoom into selected blocks.'
- Where a hierarchy is drawn with components or packages, the diagram nests them.
- A required interface on a component diagram is drawn as a socket on the component that needs it.
sources:
- url: https://faq.arc42.org/questions/D-4/
  title: 'Question D-4: How can I use UML to communicate a hierarchy of building blocks? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/5-18/
  title: 'Tip 5-18: Ensure every piece of source code can be located in the building block view! | arc42
    Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Package_diagram
  title: Package diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Component_diagram
  title: Component diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

UML (the Unified Modeling Language) offers several diagrams for software structure. Component and package diagrams can both communicate hierarchies of building blocks.

**Component diagram.** It shows how components are wired together into larger components or whole systems. A required interface appears as a half-circle, called a socket, on the component that needs it. The article Provided and Required Interface explains the notation.

**Package diagram.** It groups elements into packages. A package import is a directed relationship. The importing namespace adds the names of the package's members to its own namespace. The article Package Relationships (Import, Access, Merge, Use) covers this.

**Class diagram.** See the article UML Class Diagram.

**Hierarchy.** UML components and packages can both be nested. So, according to the arc42 FAQ, component diagrams and package diagrams can both show hierarchies.

**Fit with the arc42 building block view.** This view is hierarchical. Level 1 is the whitebox of the overall system. Level 2 and below zoom into selected blocks. The view can hold many kinds of elements, from packages and classes to components and subsystems. Every piece of source code should have a place in it.

## Example

A web shop's level 1 view shows three nested components: Catalog, Orders and Payment. Orders needs a payment service, so it carries a socket for that interface. Level 2 zooms into Orders. There, a package diagram groups the order code into packages. One package imports another, so it adds the other package's member names to its own namespace.

## Trade-offs

Component diagrams and package diagrams can both communicate hierarchies. Pick one that fits the blocks you show and keep it consistent across levels.
