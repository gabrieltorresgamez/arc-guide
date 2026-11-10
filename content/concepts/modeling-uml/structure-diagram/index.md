---
title: UML Structure Diagram
slug: structure-diagram
category: modeling-uml
kind: notation-element
summary: UML structure diagrams show the static parts of a system and how they relate, without showing
  behavior over time. Different diagram types cover different levels, such as components and hardware.
arc42:
- 5
- 7
step: s10-document
related:
- uml-diagram-taxonomy
- behavior-diagram
- uml-component-diagram
- component-port
- c4-model
- distribution-view
- uml-unified-modeling-language
checks:
- The building block view shows the static decomposition of the system, starting with a level 1 white
  box containing black boxes.
- Deeper levels zoom into selected building blocks of the level above.
- The deployment view maps software to hardware, with a UML deployment diagram and nested diagrams for
  complex infrastructure.
- Component diagrams show how the system is split into components and the dependencies between them.
sources:
- url: https://en.wikipedia.org/wiki/Unified_Modeling_Language
  title: Unified Modeling Language - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Composite_structure_diagram
  title: Composite structure diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/faq
  title: FAQ | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams
  title: Diagrams | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Level 1 and level 2 of a static decomposition, shown as components.
review:
  status: generated
  flags: []
---

## Explanation

A structure diagram answers one question: what is the system made of? It shows building blocks and their relationships. It does not show how the system acts over time. Behavior diagrams cover that. They show how objects collaborate (see UML Behavioral Diagram).

This article covers three structure diagram types.

**Composite structure diagram.** It shows the internal structure of a class and the collaborations that structure makes possible. A port is an interaction point. It connects a structured classifier (a class with internal parts) to its parts. See Port.

**Component diagram.** It shows how a software system is split into components and which dependencies exist between them. See UML Component Diagram.

**Deployment diagram.** arc42 recommends it for the deployment view, which maps software to hardware. Complex infrastructure can use nested diagrams. Infrastructure matters because software needs hardware. It can influence the system and its cross-cutting concepts. See UML Deployment Diagram.

**Link to arc42.** The arc42 building block view is a static decomposition of the system. It is mandatory. Level 1 is a white box of the whole system, with black boxes inside. Level 2 zooms into some of those blocks. Level 3 zooms further. Structure diagrams can show each level.

**Link to C4.** The C4 model is named after a set of static structure diagrams: context, containers, components and code. It was inspired by UML and the 4+1 model. Teams that use UML successfully can keep it. They may add UML state or timing diagrams to C4. See C4 Model.

## Example

A team documents an online shop. At level 1, one diagram shows the shop as a whole, with boxes inside: catalog, orders and payment. A second diagram zooms into "orders" and shows its parts and their dependencies. A third diagram shows which server runs the shop. None of these diagrams shows the order in which things happen. The team uses a behavior diagram for that.

## Trade-offs

Structure diagrams show only the static picture. Readers learn what exists and how it connects, but not what happens at runtime. Teams need behavior diagrams for that. C4 is an alternative for teams that do not use UML already.
