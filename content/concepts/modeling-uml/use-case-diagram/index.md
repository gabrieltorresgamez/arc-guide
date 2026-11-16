---
title: Use Case Diagram
slug: use-case-diagram
order: 10
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
- behavior-diagram
- class-diagram
- arc42-context-and-scope
- user-story-vs-use-case
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
- url: https://www.visual-paradigm.com/guide/beginners-tutorial-uml-use-case-diagram-modeling/
  title: 'Beginner''s Tutorial: UML Use-Case Diagram Modeling'
  site: visual-paradigm.com
  accessed: '2026-11-09'
- url: https://skills.visual-paradigm.com/docs/uml-basics-diagrams-for-beginners/exploring-use-case-diagrams-for-requirements/uml-use-case-diagram-beginners/
  title: 'UML Use Case Diagram: A Beginner’s Guide'
  site: skills.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://www.modernanalyst.com/Community/CommunityBlog/tabid/182/ID/3436/Top-10-mistakes-in-Use-Case-Modelling.aspx
  title: Top 10 mistakes in Use Case Modelling
  site: modernanalyst.com
  accessed: '2026-11-09'
- url: https://guides.visual-paradigm.com/ultimate-guide-use-case-diagrams-2026/
  title: Ultimate Guide to Use Case Diagrams in 2026 | Visual Paradigm
  site: guides.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://www.sparxsystems.us/enterprise-architect/include-vs-extend-use-case-diagrams-ea-uml/
  title: 'Include vs Extend: Use Case Diagrams | Enterprise Architect'
  site: sparxsystems.us
  accessed: '2026-11-09'
- url: https://skills.visual-paradigm.com/docs/uml-basics-diagrams-for-beginners/exploring-use-case-diagrams-for-requirements/uml-extend-include-use-case-reuse/
  title: 'UML Extend Include: Master Use Case Reuse'
  site: skills.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://issues.omg.org/issues/UMLR-288
  title: UML 2.6 RTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
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

**More about use case diagrams.**

- **Use Case Goal Hierarchy with Include Relationships:** An include relationship links a base use case to another use case whose behavior it always runs as part of its own flow. Shared steps such as Authenticate are written once and reused by many goals.

## Example

A library system has two actors: "Member" and "Catalog System" (an external system). Inside the system box sit the use cases "Borrow Book" and "Search Catalog". "Borrow Book" includes "Check Member Status". "Pay Late Fee" extends "Return Book", because it only happens if the book is late.

## Trade-offs

The diagram gives a higher-level view, while a use case itself can go into much more detail. Some relationships, such as extend, are ambiguous in interpretation and can be difficult for stakeholders to understand.
