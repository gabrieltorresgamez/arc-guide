---
title: Use Case Diagram
slug: use-case-diagram
category: modeling-uml
kind: notation-element
summary: A use case diagram gives an overview of what a system offers. It shows the actors who use it
  and which functions are in scope, without describing how the system works inside.
arc42:
- 3
- 1
step: s03-functional-requirements
related:
- use-case
- use-case-diagram-modeling-mistakes
- behavior-diagram
- generalization-and-specialization
- use-case-template
- arc42-context-and-scope
- user-story-vs-use-case
- association
checks:
- The diagram draws a system boundary, so it is clear which functionality is in scope and which is not.
- Every actor is a person, organization or external system that interacts with the system.
- Extend relationships are used with care, and their meaning is made clear to readers.
sources:
- url: https://agilemodeling.com/artifacts/useCaseDiagram.htm
  title: 'UML Use Case Diagrams: An Agile Introduction'
  site: agilemodeling.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Use_case
  title: Use case - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Use_case_diagram
  title: Use case diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'Library example: actors, system boundary, include and extend.'
review:
  status: generated
  flags: []
---

## Explanation

A use case diagram gives an overview of the usage requirements for a system. It is a higher-level view of the system.

**Main elements**

- **Actors** are people, organizations or external systems. Each plays a role when interacting with the system.
- **Use cases** describe system behavior. A use case is a structured description of how the system responds to requests from external actors. See the article Use Case.
- **System boundary** is a box around the use cases. Functionality inside the box is in scope. Anything outside is not.

**Relationships between use cases**

- **Include** works like a procedure call.
- **Extend** works like a hardware interrupt. You do not know when, or whether, the extending use case will run.
- **Inheritance** is applied as on UML class diagrams, to model specialization. It applies to use cases and to actors.

## Example

A library system has two actors: "Member" and "Catalog System" (an external system). Inside the system box sit the use cases "Borrow Book" and "Search Catalog". "Borrow Book" includes "Check Member Status". "Pay Late Fee" extends "Return Book", because it only happens if the book is late. The diagram shows none of the screens, data or code behind these use cases.

## Trade-offs

The diagram gives a higher-level view, while a use case itself can go into much more detail. Some relationships, such as extend, are ambiguous in interpretation and can be difficult for stakeholders to understand.
