---
title: UML Class Diagram
slug: class-diagram
category: modeling-uml
kind: notation-element
summary: A UML class diagram shows classes and how they relate. Use it as a selective sketch of the interesting
  classes, not as a full specification of every class.
arc42:
- 5
step: s10-document
related:
- class-diagram-relationships
- association
- composition-versus-aggregation
- generalization-and-specialization
- provided-and-required-interface
- uml-interface
- common-class-diagram-modeling-mistakes
- structure-diagram
checks:
- The class diagram shows only the interesting classes, not every class in the system.
- Dependency lines are not drawn in addition to associations or generalizations between the same classes.
- The ball-and-socket notation is not used to link interfaces in class diagrams.
sources:
- url: https://martinfowler.com/bliki/UmlAsSketch.html
  title: Uml As Sketch
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
  caption: 'A selective sketch: three classes, with associations that read like fields.'
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A class diagram shows classes and the links between them. See UML Class Diagram Relationship for the full set of relationship types.

**Associations.** An association is a line between two classes. It usually stands for something like a field in a class. The link is always there, so you can always ask an order for its customer.

**Dependencies.** A dependency means that a change to one element (the supplier) may force a change in another (the client). Associations and generalizations already imply a dependency. So there is no need to draw an extra dependency line next to them.

**Interfaces.** UML 2 added the socket notation to show interfaces a class requires. It grew out of the lollipop notation, which shows interfaces a class provides. The UML committee ruled that the combined ball-and-socket notation may only be used for connectors in Composite Structure Diagrams. The author still likes the mated ball and socket as a way to show how interfaces and implementations connect. See Provided and Required Interface for more.

**Stay selective.** Use UML as sketches. Show only the classes that are interesting and worth discussing before you read the code. The goal is communication, not a complete specification. Fowler's sound-bite is that comprehensiveness is the enemy of comprehensibility.

## Example

A team sketches an online shop. The diagram shows three classes: Order, Customer and Product. An association from Order to Customer reflects that an order holds a reference to its customer. Helper classes stay out of the picture. The team uses the sketch to agree on the core ideas before looking at code.

## Trade-offs

Sketching is done quickly and informally, and it helps communication. It leaves classes out, so it is not a complete specification. Drawing every class would be more complete, but it would hurt comprehensibility.
