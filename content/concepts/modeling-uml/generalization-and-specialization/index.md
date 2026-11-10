---
title: UML Generalization and Specialization
slug: generalization-and-specialization
category: modeling-uml
kind: notation-element
summary: Generalization links a specific class to a more general one. The specific class inherits the
  general class's characteristics and can add its own. Every instance of the specific class is also an
  instance of the general class.
arc42:
- 5
- 8
- 12
step: s10-document
related:
- class-diagram
- class-diagram-relationships
- association
- composition-versus-aggregation
- use-case-diagram
- common-class-diagram-modeling-mistakes
- uml-interface
- open-closed-principle
checks:
- Generalization arrows use a hollow triangle and point to the more general class.
- Every subclass can stand in for its superclass, because each of its instances is also an instance of
  the superclass.
- Abstract classes are used only for shared characteristics and have no direct instances.
- Generalization sets state whether they are complete and whether they are disjoint.
sources:
- url: https://the-requirements-engineer.com/modeling/uml-generalization-and-specialization/
  title: Understanding UML Generalization and Specialization | The Requirements Engineer
  site: the-requirements-engineer.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Class_diagram
  title: Class diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Liskov_substitution_principle
  title: Liskov substitution principle - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://issues.omg.org/issues/UML25-339
  title: Unified Modeling Language 2.5 (UML) FTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/OpenInheritance.html
  title: Open Inheritance
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Two specific payment classes generalize to one abstract Payment class.
review:
  status: generated
  flags: []
---

## Explanation

Generalization is a relationship between a general class (the superclass) and a more specific class (the subclass). Specialization is the same relationship seen from the other direction: you start from the general class and add more specific ones. See UML Class Diagram for the diagram type.

**Notation.** A hollow triangular arrowhead marks the relationship. It points toward the more general class.

**Inheritance.** A specialized class inherits the characteristics of its general class. It may also add characteristics of its own.

**Abstract classes.** An abstract class defines common characteristics but has no direct instances of its own.

**Substitutability.** Every instance of a subclass is also an instance of its superclass. The Liskov formulation says that when S is a subtype of T, a program can use objects of type S wherever it uses objects of type T, and its desirable properties stay the same.

**Generalization sets.** A set groups the specializations of one general class. Two properties describe a set:
- *Complete*: the set covers all permitted specializations. In the UML 2.5 specification, the notation uses the word "complete" and the metamodel uses "covering"; these are defined as synonyms.
- *Disjoint*: one instance can belong to only one specialization in the set.

**Where it appears.** One source states that generalization can be shown only on class diagrams and use case diagrams.

## Example

A shop models a general class "Payment". Two specific classes, "CardPayment" and "BankTransfer", each point to it with a hollow triangle. Both inherit what all payments share, such as an amount. Each adds its own details. "Payment" is abstract, so the shop never creates a plain payment. A card payment can be used wherever a payment is expected. If the set holds only these two classes and no payment is both, it is complete and disjoint.

## Trade-offs

Superclass behavior can easily be broken through inheritance, and one should be wary of upgrades, since a subclass can rely on hidden implementation details.
