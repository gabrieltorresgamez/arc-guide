---
title: UML Modeling Best Practice
slug: uml-modeling-best-practice
category: modeling-uml
kind: practice
summary: 'Good UML practice means agreeing on shared modeling standards, modeling together, and sharing
  models openly. Match the precision to how you use UML: quick sketches need less than blueprints.'
arc42:
- 5
- 8
step: s10-document
related:
- modeling-method
- rules-of-thumb-for-modeling
- uml-modeling-anti-patterns
- uml-unified-modeling-language
- barriers-to-uml-adoption
- why-use-uml-in-architecture-documentation
checks:
- The document states which modeling standards the team follows.
- The diagrams follow the team's style guidelines consistently.
- The document makes clear whether diagrams are sketches or more precise specifications.
- Models are made visible to the team, for example on a modeling wall.
sources:
- url: https://agilemodeling.com/practices.htm
  title: The Practices of Agile Modeling (AM)
  site: agilemodeling.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UmlMode.html
  title: Uml Mode
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UmlAsSketch.html
  title: Uml As Sketch
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://agilemodeling.com/style.htm
  title: 'Modeling Style Guidelines: Strategies for Better Diagrams'
  site: agilemodeling.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

UML is a notation for drawing software models.

**Know how you use UML.** Fowler names three modes: sketch, blueprint, and programming language. Sketches stress selective communication. They show what matters and skip a full specification. UML 2 added precision aimed at the blueprint and programming-language modes. That extra precision can burden people who only sketch. Decide which mode your team is in, so nobody demands more detail than needed.

**Agree on standards.** Agile Modeling has a practice called Apply Modeling Standards. The team agrees on a common set of modeling standards and then follows them. The Agile Modeling site's separate style guidelines aim to improve the quality and readability of diagrams, so they are easier to understand and work with. For related guidance, see Modeling Method and Rules of Thumb for Modeling.

**Model as a group.** When modeling to understand something, to communicate ideas, or to build a common vision, the work is a group activity. It benefits from the input of several people working together.

**Share the results.** Models can be displayed publicly, for example on a modeling wall. Open display supports open and honest communication with the team and stakeholders.

## Example

A team building an online shop writes down one set of modeling standards. Two developers sketch the checkout flow together, showing only the steps that matter. They pin the sketch to the team's modeling wall. Later diagrams follow the same standards, so everyone reads them the same way.

## Trade-offs

Shared standards make diagrams easier to work with, but the team must agree on them and keep following them. Extra precision in UML 2 suits blueprint and programming-language use. It can burden people who only sketch.
