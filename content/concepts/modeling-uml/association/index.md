---
title: UML Association
slug: association
category: modeling-uml
kind: notation-element
summary: A UML association is a solid line between two classes. It shows that objects of one class refer
  to objects of the other. Ends can carry role names, multiplicity and navigability arrows.
arc42:
- 5
- 12
step: s10-document
related:
- class-diagram
- class-diagram-relationships
- composition-versus-aggregation
- common-class-diagram-modeling-mistakes
- entity-relationship-clarification
- structure-diagram
- uml-unified-modeling-language
- domain-model
checks:
- Each relationship between two classes is shown either as an association line or as an attribute, not
  both.
- Association ends that matter carry a multiplicity such as * or 0..1.
- Role names on association ends match the attribute names used in code.
- Where reachability matters, navigability is shown with an open arrowhead or a cross.
sources:
- url: https://en.wikipedia.org/wiki/Class_diagram
  title: Class diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=1398623&seqNum=5
  title: '16.4 Ways to Show UML Attributes: Attribute Text and Association Lines | Applying UML and Patterns:
    UML Class Diagrams | InformIT'
  site: informit.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: An association with a name, role names, multiplicities and a navigability arrow.
review:
  status: generated
  flags: []
---

## Explanation

An association is a line in a UML class diagram (see UML Class Diagram). It connects two classes. It says that at least one of the two classes refers to the other.

**Drawing it**

A binary association is a solid line between two classes. A reflexive (self) association is a binary association that connects a class to itself.

**Names and role names**

The line may carry a name. Each end may carry a role name. Officially, a role name is the association end name. It indicates the attribute name used in code.

**Multiplicity**

An end may show a multiplicity such as `*` or `0..1`. Multiplicity states how many objects take part in the association. You read it from the perspective of the other end.

**Navigability**

An open arrowhead on one end documents that the class at that end can be reached efficiently. In unidirectional navigation, a small cross on the line marks the side of the class that cannot be reached. A navigability arrow points from the source object to the target object.

**Association or attribute**

An association line and an attribute show the same relationship. They are semantically equal. The line gives more visual emphasis.

## Example

A diagram has two classes, `Customer` and `Order`. A solid line joins them. The end at `Order` is labeled `orders` with multiplicity `*`. The end at `Customer` is labeled `buyer` with multiplicity `1`. An open arrow points to `Order`. The diagram says a customer can reach its orders. In code, `Customer` would hold an attribute named `orders`. The diagram does not also list `orders` inside the `Customer` box.

## Trade-offs

An association line gives a relationship visual weight. A guideline is to use attribute text for data type objects and association lines for other classes, because the line catches the eye and emphasizes the connection between classes.
