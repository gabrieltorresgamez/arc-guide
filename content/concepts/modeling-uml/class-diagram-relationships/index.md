---
title: UML Class Diagram Relationship
slug: class-diagram-relationships
category: modeling-uml
kind: notation-element
summary: 'UML class diagrams use different relationship types to link classes. Pick the type that matches
  the real link: associations resemble fields, composition means single ownership, and aggregation adds
  no meaning beyond association.'
arc42:
- 5
- 8
step: s10-document
related:
- class-diagram
- association
- composition-versus-aggregation
- provided-and-required-interface
- uml-interface
- common-class-diagram-modeling-mistakes
- generalization-and-specialization
- instance-specification
checks:
- Associations are used for field-like structural links between classes.
- Composition (black diamond) is used only where a part belongs to a single owner.
- Any aggregation (white diamond) in the diagram comes with an explanation of what it means.
- Required interfaces are shown with a notation that UML allows for that diagram type.
sources:
- url: https://martinfowler.com/bliki/AggregationAndComposition.html
  title: Aggregation And Composition
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/DependencyAndAssociation.html
  title: Dependency And Association
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BallAndSocket.html
  title: Ball And Socket
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Composition (black diamond) for an owned part, and a plain association for a field-like link.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A UML class diagram shows classes and the links between them. UML offers several relationship types. Each says something different, so the choice should match the real link between the classes. See UML Class Diagram for the basics.

**Association.** An association is the general structural link. It usually stands for something like a field in a class. If an Order holds its items in a field, an association fits.

**Dependency and required interfaces.** Classes do not only implement interfaces. They can also require them. UML has a compact socket notation for a required interface. That ball-and-socket notation is limited to connectors in Composite Structure Diagrams. In UML 1, the link between required and provided interfaces was shown with a dependency. See Provided and Required Interface and UML Interface.

**Composition.** Composition is drawn with a black diamond. It carries real meaning. A part object can belong to only one composition at a time. Ordinary multiplicity markers cannot easily express this single-owner rule, so the diamond does that job.

**Aggregation.** Aggregation is drawn with a white diamond. It adds nothing beyond a plain association. Jim Rumbaugh called it a "modeling placebo". It has no standard meaning, so add an explanation if you use it. See Aggregation vs. Composition.

**Choosing.** Ask what the link really is.
- A field-like link: use an association.
- One owner for a part: use composition.
- A class that needs an interface: think of a required interface.
- A white diamond: use it only with a note that says what you mean.

## Example

A shop model has an Order, its OrderLines, and a PriceCalculator.

- Order keeps its OrderLines in a field. Each line belongs to exactly one order. A black diamond on the Order side shows this single owner.
- Order also holds a Customer in a field. A plain association shows that link.
- Order needs a pricing interface that PriceCalculator provides. Order requires that interface.

The diagram uses no white diamond. A reader never has to guess what it means.

## Trade-offs

Composition adds meaning, but it also adds a rule readers must know: one owner only. Plain associations are simpler, but they say less. Aggregation looks richer but carries no standard meaning, so it needs extra explanation. The socket notation for required interfaces is compact, but it works only in Composite Structure Diagrams.
