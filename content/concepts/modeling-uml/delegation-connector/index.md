---
title: Delegation Connector
slug: delegation-connector
category: modeling-uml
kind: notation-element
summary: A delegation connector passes a component's external port inward to an internal part that does
  the real work. Outsiders see one contract, and the internal structure stays hidden.
arc42:
- 5
step: s10-document
related:
- component-connector-assembly-and-delegation
- component-port
- uml-component-diagram
- provided-and-required-interface
- nested-components-and-subsystems
- uml-interface
- information-hiding
- component-view-refinement-levels
checks:
- Each delegation connector joins a boundary port or interface to an internal one of the same kind.
- Connectors between sibling components are drawn as assembly connectors, and delegation is used only
  for crossing a component boundary.
- A whitebox shows the building blocks inside a blackbox and their relationships.
sources:
- url: https://developer.ibm.com/articles/the-component-diagram/
  title: The component diagram
  site: developer.ibm.com
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/B-9/
  title: 'Question B-9: What is a whitebox? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://guides.visual-paradigm.com/docs/mastering-uml-2-5-a-use-case-driven-approach-to-agile-modeling/module-3-the-skeleton-the-7-structural-uml-diagrams/component-diagrams/
  title: Component Diagrams - Visual Paradigm Guides
  site: guides.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://issues.omg.org/issues/UML25-566
  title: Unified Modeling Language 2.5 (UML) FTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: WebStore delegates its search port to an internal SearchEngine.
review:
  status: generated
  flags: []
---

## Explanation

A component can hide smaller parts inside it. Its outside face is a port, a connection point that decouples the internals from outside entities (see the article "Port"). A delegation connector links that port to a port or interface on an internal part. The internal part typically handles the processing, though the outer component may have its own logic.

An assembly connector ties one component's provided interface to another component's required interface, the familiar ball-and-socket. A delegation connector instead shows internal realization: the outer component hands work to its sub-components.

In arc42, a whitebox is a more detailed view of a blackbox. It shows several building blocks and their relationships. The building block view is a hierarchy of blackboxes and whiteboxes. Level 1 is the whitebox of the whole system.

arc42 gives no template for interface specification, because interfaces vary too much. You choose how to describe the contract that the port exposes.

## Example

A WebStore component offers a search interface on its boundary. Inside, a SearchEngine part does the searching. A delegation connector links WebStore's search port to SearchEngine's search interface. Callers talk only to WebStore. If the team later swaps SearchEngine for another part, the outside contract stays the same. Only the internal connector changes.

## Trade-offs

One benefit is clear: outsiders depend on the port, not on the internals. Without an interface template in arc42, you must decide yourself how to specify the interface.
