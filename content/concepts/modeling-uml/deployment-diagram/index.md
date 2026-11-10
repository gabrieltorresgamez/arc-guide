---
title: UML Deployment Diagram
slug: deployment-diagram
category: modeling-uml
kind: notation-element
summary: A UML deployment diagram shows where software runs. It assigns software artifacts to system elements,
  drawn as boxes called nodes.
arc42:
- 7
step: s10-document
related:
- distribution-view
- deployment-diagram-modeling-mistakes
- uml-component-diagram
- structure-diagram
- arc42-documentation-template
- uml-unified-modeling-language
checks:
- Artifacts are drawn as rectangles inside the box of the node they are allocated to.
- Complex infrastructure is documented with nested diagrams or nested nodes.
- Each environment that needs it (development, test, production) has its own deployment documentation.
sources:
- url: https://en.wikipedia.org/wiki/Deployment_diagram
  title: Deployment diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'Generic deployment diagram: artifacts inside nested nodes.'
review:
  status: generated
  flags: []
---

## Explanation

A deployment diagram describes the execution architecture of a system. It assigns software artifacts to system elements. The artifacts are the software components that run on each node.

**How it looks**

- Nodes are drawn as boxes.
- Artifacts allocated to a node appear as rectangles inside its box.
- Nodes can be nested. A subnode appears as a box inside another box.
- One node can stand for several physical nodes at once.

**Use in architecture documentation**

arc42 recommends UML deployment diagrams for the deployment view. For more complex infrastructure, it suggests nested diagrams. The article Deployment View covers that view in detail.

Systems often run in several environments. Examples are development, test, and production. Each environment may need its own deployment documentation.

## Example

An online shop runs on three boxes: a web server, an application server, and a database server. Each box holds a rectangle for the software placed on it. A fourth box group, labeled "test environment", could repeat this layout for testing. A box labeled "application server" might stand for several identical machines.
