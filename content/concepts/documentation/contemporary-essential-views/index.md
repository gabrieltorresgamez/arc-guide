---
title: Essential Architecture Views (Context, Component, Runtime, Distribution)
slug: contemporary-essential-views
category: documentation
kind: concept
summary: 'Essential architecture views show a system from four angles: its context, its building blocks,
  its runtime behavior, and its distribution onto hardware. Each view answers a different question for
  stakeholders.'
arc42:
- 3
- 5
- 6
- 7
step: s10-document
related:
- context-view
- component-view
- runtime-view
- distribution-view
- c4-model
- architectural-overview-diagram
- 4-1-view-model
- arc42-documentation-template
checks:
- The context view shows the system as a black box with its communication partners and external interfaces.
- The building block view is present and shows a hierarchy of black boxes and white boxes.
- The runtime view covers a representative selection of architecturally relevant scenarios.
- The deployment view uses a UML deployment diagram, or another node-and-channel diagram for hardware
  stakeholders.
- Any UML versions of C4 diagrams carry descriptive text.
sources:
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/
  title: Home | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/notation
  title: Notation | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

This article covers four views: context, component (building block), runtime, and distribution (deployment). Each maps onto an arc42 section.

**Context view.** It delimits the system from its communication partners. It also specifies the external interfaces. This is arc42 section 3, "Context and Scope". It can separate business context from technical context (see *Business and Technical Context*). In the business context, all stakeholders should understand which data the system exchanges with its environment, and diagrams show the system as a black box.

**Component view.** It shows the static decomposition of the system into building blocks. The result is a hierarchy of black boxes and white boxes. arc42 compares it to a house floor plan. Blocks can be modules, components, subsystems, classes, interfaces or packages, plus their dependencies. This is arc42 section 5, and it is mandatory.

**Runtime view.** It shows how instances of building blocks do their job and communicate while the system runs. arc42 asks for a representative selection of architecturally relevant scenarios, not every possible flow. This is arc42 section 6.

**Distribution view.** It describes the technical infrastructure used to run the system and maps the software building blocks to that infrastructure. arc42 recommends UML deployment diagrams for it, nested when the infrastructure is complex. Other node-and-channel diagrams are acceptable for hardware stakeholders. This is arc42 section 7.

**Relation to C4.** C4 uses a hierarchy of diagrams: system context, containers, components, and code. It does not depend on one notation. Its core diagrams can be drawn in UML with packages, components and stereotypes. UML diagrams tend to lack descriptive text, so add it.

## Example

A team builds an online booking tool. The context view shows the tool as one box, with customers and a payment provider around it, and labels the data exchanged. The component view splits the tool into blocks such as booking, accounts and notifications. The runtime view walks through one scenario: a customer books and pays. The distribution view shows which servers host each block.

## Trade-offs

UML diagrams can be drawn for C4, but they tend to lack descriptive text. The runtime view shows only a representative selection of scenarios, so some flows are left undocumented.
