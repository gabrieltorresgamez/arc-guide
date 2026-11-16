---
title: UML Class Diagram
slug: uml-class-diagram
order: 10
category: modeling-uml
kind: notation-element
summary: A UML class diagram shows classes and how they relate. Use it as a selective sketch of the interesting
  classes, not as a full specification of every class.
arc42:
- 5
step: s10-document
related:
- uml-component-diagram
- uml-structure-diagram
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
- url: https://en.wikipedia.org/wiki/Class_diagram
  title: Class diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=1398623&seqNum=5
  title: '16.4 Ways to Show UML Attributes: Attribute Text and Association Lines | Applying UML and Patterns:
    UML Class Diagrams | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/AggregationAndComposition.html
  title: Aggregation And Composition
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=1398623&seqNum=14
  title: '16.13 Composition Over Aggregation | Applying UML and Patterns: UML Class Diagrams | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2013/dd479569(v=vs.120)
  title: AggregationKind Enumeration (Microsoft.VisualStudio.Uml.Classes) | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://the-requirements-engineer.com/modeling/uml-generalization-and-specialization/
  title: Understanding UML Generalization and Specialization | The Requirements Engineer
  site: the-requirements-engineer.com
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
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/7.3.22.html
  title: "7.3.22 InstanceSpecification"
  site: site.uottawa.ca
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Object_diagram
  title: Object diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/7.3.32.html
  title: "7.3.32 MultiplicityElement"
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
  caption: 'A selective sketch: three classes, with associations that read like fields.'
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A class diagram shows classes and the links between them. See UML Class Diagram for the full set of relationship types.

**Associations.** An association is a line between two classes. It usually stands for something like a field in a class. The link is always there, so you can always ask an order for its customer.

**Dependencies.** A dependency means that a change to one element (the supplier) may force a change in another (the client). Associations and generalizations already imply a dependency. So there is no need to draw an extra dependency line next to them.

**Interfaces.** UML 2 added the socket notation to show interfaces a class requires. It grew out of the lollipop notation, which shows interfaces a class provides. The UML committee ruled that the combined ball-and-socket notation may only be used for connectors in Composite Structure Diagrams. The author still likes the mated ball and socket as a way to show how interfaces and implementations connect. See UML Component Diagram for more.

**Stay selective.** Use UML as sketches. Show only the classes that are interesting and worth discussing before you read the code. The goal is communication, not a complete specification. Fowler's sound-bite is that comprehensiveness is the enemy of comprehensibility.

**More about class diagram elements.**

- **UML Association:** A UML association is a solid line between two classes. It shows that objects of one class refer to objects of the other. Ends can carry role names, multiplicity and navigability arrows.
- **Aggregation vs. Composition:** Aggregation and composition are UML ways to show that something is made of parts. Composition is strict: a part belongs to one whole. Aggregation is loose and adds little beyond a plain association.
- **UML Generalization and Specialization:** Generalization links a specific class to a more general one. The specific class inherits the general class's characteristics and can add its own. Every instance of the specific class is also an instance of the general class.
- **UML Class Diagram Relationship:** UML class diagrams use different relationship types to link classes. Pick the type that matches the real link: associations resemble fields, composition means single ownership, and aggregation adds no meaning beyond association.
- **Instance Specification:** An instance specification is a UML model element that stands for one instance in a modeled system. It gives a concrete example, with attribute values, of something a class describes in general.
- **Common Class Diagram Modeling Mistakes:** Class diagrams often repeat the same errors: impossible multiplicities, shared parts in a composition, missing multiplicity, and wrong arrows. Knowing them helps you review diagrams, even though tools catch some automatically.

## Example

A team sketches an online shop. The diagram shows three classes: Order, Customer and Product. An association from Order to Customer reflects that an order holds a reference to its customer. Helper classes stay out of the picture. The team uses the sketch to agree on the core ideas before looking at code.

## Trade-offs

Sketching is done quickly and informally, and it helps communication. It leaves classes out, so it is not a complete specification. Drawing every class would be more complete, but it would hurt comprehensibility.
