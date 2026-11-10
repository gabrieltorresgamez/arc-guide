---
title: Common Use Case Diagram Errors
slug: use-case-diagram-modeling-mistakes
category: modeling-uml
kind: concept
summary: 'Use case diagrams often go wrong in repeatable ways: actors inside the boundary, actors named
  after job titles, technical parts shown as actors, and include or extend used without purpose. Fixing
  these makes the diagram clear.'
arc42:
- 3
step: s03-functional-requirements
related:
- use-case-diagram
- use-case
- uml-modeling-anti-patterns
- common-class-diagram-modeling-mistakes
- generalization-and-specialization
- use-case-template
- uml-modeling-best-practice
- use-case-completeness-check
checks:
- All actors are drawn outside the system boundary box.
- Actor names describe roles, not job titles.
- No database, API, or server appears as an actor or use case.
- Every extend relation has a defined, testable condition and a named extension point on the base use
  case.
- Include arrows point from base to included use case; extend arrows point from extension to base.
sources:
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
  caption: 'A corrected diagram: the actor sits outside the boundary, include points to the included case,
    extend points to the base case with a condition.'
review:
  status: generated
  flags: []
---

## Explanation

A use case diagram shows who uses a system and what they can do with it. (See the articles Use Case Diagram and Use Case for the basics.) A few mistakes appear again and again.

**Actors inside the boundary.** The boundary box marks the system. Actors are external to the system, so always draw them outside the box, never inside it.

**Actors named after job titles.** An actor is a role played by a user or an external system. It is not a job title. Titles and actor names are different things, and mixing them up is listed as a top mistake in use case modeling.

**Technical parts as actors or use cases.** Do not add a database, an API, or a server as an actor or a use case. These are technical components.

**Misusing include and extend.** Using these relationships without understanding their purpose gives a confusing model. The rules are short:
- Include is for behavior that always runs. Do not put optional steps in an include.
- Extend is conditional. The extension happens only when a guard condition holds.
- The condition must be unambiguous and testable. Visual Paradigm pages differ on where to show it: one says to keep conditions in text specifications, another says to add a note near the extend arrow or use a guard.
- The base use case must define named extension points, the places where an extension may attach. An open OMG issue asks whether a condition note may refer to an extension point the use case does not define. The issue notes that extension points appear in the properties of a use case.

**Wrong arrow direction.** An include arrow points from the base use case to the included one. An extend arrow points from the extension to the base use case.

**Generalization.** Generalization shows inheritance. For example, a specialized actor such as Admin User inherits the use cases of a general actor such as Standard User.

## Example

An online shop diagram has a box labeled "Shop". Inside the box sits "Sales Manager", drawn next to "Database". Two fixes are needed. Move the actor outside the box and name the role, for example "Customer". Remove "Database", because it is a technical component. Then "Place Order" always needs "Check Stock", so that is an include arrow from "Place Order" to "Check Stock". "Apply Voucher" happens only if the customer enters a code. That is an extend arrow from "Apply Voucher" to "Place Order". It carries the condition "voucher code entered". "Place Order" defines a named extension point for it.

## Trade-offs

One practical point: the sources disagree on whether extend conditions go in text specifications or in a note or guard near the arrow.
