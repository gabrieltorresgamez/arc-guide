---
title: Common Component Diagram Mistake
slug: component-diagram-modeling-mistakes
category: modeling-uml
kind: concept
summary: Two common component diagram mistakes are leaving artifacts unlinked to the components they embody,
  and letting components depend on each other in a cycle. Both are avoidable with manifestation links
  and acyclic dependencies.
arc42:
- 5
step: s10-document
related:
- uml-component-diagram
- component-connector-assembly-and-delegation
- delegation-connector
- provided-and-required-interface
- coupling-and-cohesion
- modularity
- uml-modeling-anti-patterns
- deployment-diagram
checks:
- Every artifact on a component diagram is linked by a manifestation relationship to the model element,
  such as a component, that it embodies.
- The dependency graph between components has no cycles.
- Where a cycle existed, it was broken, for example by moving shared dependencies into a new package.
sources:
- url: https://issues.omg.org/issues/UML25-197
  title: Unified Modeling Language 2.5 (UML) FTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Acyclic_dependencies_principle
  title: Acyclic dependencies principle - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Cycle removed through a shared package, and an artifact linked to its component by a manifestation.
review:
  status: generated
  flags: []
---

## Explanation

**Artifacts with no link to a component**

An artifact can embody, or *manifest*, model elements. The artifact owns the manifestation relationships. Each one represents the artifact's use of some packageable element.

One artifact may manifest several elements.

**Circular dependencies between components**

A cycle occurs when component A depends on B, and B depends, directly or through others, back on A.

The acyclic dependencies principle, defined by Robert C. Martin, says the dependency graph of packages or components should have no cycles. In other words, it forms a directed acyclic graph: arrows run one way and never loop back.

It is in general always possible to break a cycle. One way is to create a new package and move the shared dependencies into it.

## Example

A shop diagram shows an "Orders" component and a "Customers" component. Orders needs customer data. Customers needs order history. The two arrows form a loop.

The fix: move the shared parts, such as the customer and order record definitions, into a new "Shared Records" package. Both components now point to that package. No arrow points back.

On the same diagram, a file named `shop.jar` appears with no line to anything.

## Trade-offs

Breaking a cycle by moving shared parts into a new package is one way to remove it. The source pages do not go further than that, so check each case on its own.
