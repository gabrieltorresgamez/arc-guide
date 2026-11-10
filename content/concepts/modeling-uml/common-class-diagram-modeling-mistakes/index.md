---
title: Common Class Diagram Modeling Mistakes
slug: common-class-diagram-modeling-mistakes
category: modeling-uml
kind: concept
summary: 'Class diagrams often repeat the same errors: impossible multiplicities, shared parts in a composition,
  missing multiplicity, and wrong arrows. Knowing them helps you review diagrams, even though tools catch
  some automatically.'
arc42:
- 5
- 8
step: s10-document
related:
- class-diagram
- class-diagram-relationships
- composition-versus-aggregation
- association
- generalization-and-specialization
- uml-modeling-anti-patterns
- uml-modeling-best-practice
- component-diagram-modeling-mistakes
checks:
- No multiplicity has a lower bound greater than its upper bound.
- Every association line states its multiplicity.
- No part in a composition (filled diamond) belongs to more than one whole.
- Dependency, realization and generalization arrows match their intended meaning.
- Generalization is used only for is-a relationships, not for whole-part ones.
sources:
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/7.3.32.html
  title: ''
  site: site.uottawa.ca
  accessed: '2026-11-09'
- url: https://cruise.umple.org/umple/Multiplicity.html
  title: 'Umple User Manual: Multiplicity'
  site: cruise.umple.org
  accessed: '2026-11-09'
- url: https://tobiasduerschmid.github.io/SEBook/uml_class_diagram.html
  title: UML Class Diagrams | SE Book
  site: tobiasduerschmid.github.io
  accessed: '2026-11-09'
- url: https://www.visual-paradigm.com/guide/the-comprehensive-guide-to-uml-2-5-for-modern-software-teams/
  title: The Comprehensive Guide to UML 2.5 for Modern Software Teams
  site: visual-paradigm.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'Invalid composition: one part has two wholes.'
review:
  status: generated
  flags: []
---

## Explanation

A class diagram (see UML Class Diagram) shows classes and the links between them. A few mistakes appear again and again. A reviewer can check for them one by one.

**Invalid multiplicity.** Multiplicity says how many objects take part in a link. It has a lower bound (the minimum) and an upper bound (the maximum). The upper bound must be at least as large as the lower bound. A range such as "5 to 2" is invalid.

**Missing multiplicity.** Some diagrams leave multiplicity off association lines. Developers then have to guess the rules of the system.

**Composition errors.** Composition means exclusive ownership. A part cannot belong to several wholes. Deleting the whole deletes its parts. A part shared by two wholes breaks this rule.

**Aggregation.** Aggregation or plain association fits shared or independent relationships, where composition does not apply. See Aggregation vs. Composition.

**Inheritance mixed up with whole-part.** Designers often confuse "is-a" (inheritance) with "has-a" (whole-part). Generalization then appears where composition or association was meant. See UML Generalization and Specialization.

**Wrong arrows.** Realization is drawn with a dashed line and a hollow triangle pointing to the interface. Drawing a solid line there is a pitfall.

**Tool support.** Modeling tools can catch some errors. The Umple compiler, for example, reports a multiplicity error and highlights the offending line.

## Example

A shop diagram links Order to Customer with the multiplicity "3..1". A reviewer flags it, because the upper bound is below the lower bound. The same diagram draws a composition from both Order and Shipment to Address. The reviewer flags this too: a composed part cannot have two wholes. The team changes both links to plain associations and adds a multiplicity to each.

## Trade-offs

Tools find mechanical errors such as an invalid multiplicity.
