---
title: Use Case Goal Hierarchy with Include Relationships
slug: use-case-goal-hierarchy-with-include-relationships
category: modeling-uml
kind: notation-element
summary: An include relationship links a base use case to another use case whose behavior it always runs
  as part of its own flow. Shared steps such as Authenticate are written once and reused by many goals.
arc42:
- 3
- 6
step: s03-functional-requirements
related:
- use-case
- use-case-diagram
- use-case-goal-levels
- goal-hierarchy-to-component-mapping
- use-case-diagram-modeling-mistakes
- runtime-view
- use-case-template
- generalization-and-specialization
checks:
- Each include arrow starts at the base use case and points at the included use case.
- Included use cases describe mandatory behavior; optional behavior is modeled with extend instead.
- Behavior shared by several use cases, such as Authenticate, is factored out into one included use case.
- Runtime view scenarios are chosen for architectural relevance, not one per use case or included step.
sources:
- url: https://swi.cs.vsb.cz/RUPLarge/core.base_rup/guidances/guidelines/include-relationship_5AE2718.html
  title: 'Guideline: Include-Relationship'
  site: swi.cs.vsb.cz
  accessed: '2026-11-09'
- url: https://blog.visual-paradigm.com/include-and-extend-use-cases/
  title: “Include” and “Extend” Use Cases - Visual Paradigm Blog
  site: blog.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UseCase.html
  title: Use Case
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Two goals include the shared Authenticate use case. Arrows point from base to included.
review:
  status: generated
  flags: []
---

## Explanation

A use case describes how a user reaches a goal with a system (see the article Use Case). Big goals often need smaller steps. The include relationship shows this in a use case diagram (see Use Case Diagram).

**What include means**

A base use case includes another use case as part of its own flow. The included behavior runs in full. Then the base use case continues where it left off. The included step is always executed when the base use case reaches that point.

**Arrow direction**

The arrow starts at the base use case. The arrowhead points at the included use case. Read it as "the base needs the included one."

**Why use it: reuse**

One use is reuse. When two or more use cases share the same behavior, you move it into its own use case. Each goal that needs it includes it, so the behavior is described only once.

**Include versus extend**

Extend differs in one key way. An extending use case adds optional behavior to a base use case. An included use case is not optional.

**Use in documentation**

Use cases feed the runtime view in arc42 (see Runtime View). That view shows how building blocks carry out the important use cases. Scenarios are chosen by architectural relevance. You do not need one for every use case or every included step.

## Example

A bank's ATM supports the goal Change PIN.

- Change PIN includes Define New PIN.
- Change PIN also includes Authenticate.
- Withdraw Cash includes Authenticate too.

Authenticate is described once. Both goals reuse it. In the diagram, each arrow starts at the goal and points at the included use case.

## Trade-offs

Splitting out shared behavior avoids repeating it. Use cases are a requirements technique whose value lies in short, readable text. Heavy documentation effort before development starts is a warning sign. In the runtime view, pick scenarios by architectural relevance, not by counting included steps.
