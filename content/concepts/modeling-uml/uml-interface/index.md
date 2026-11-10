---
title: UML Interface
slug: uml-interface
category: modeling-uml
kind: notation-element
summary: A UML interface is a contract that lists operations without implementing them. Classes or components
  realize it. Clients rely on the contract, not on the implementation behind it.
arc42:
- 3
- 5
- 8
step: s10-document
related:
- provided-and-required-interface
- uml-component-diagram
- class-diagram
- information-hiding
- component-connector-assembly-and-delegation
- interface-segregation-principle
- loose-coupling
- component-view
checks:
- Each interface shown in a component diagram is drawn as a ball (provided) or socket (required), or as
  a class box with the interface stereotype.
- Black-box building blocks describe their responsibility and their interfaces, not their internals.
- No interface is shown as instantiated; each is realized by at least one class or component.
sources:
- url: https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html
  title: Interfaces (The Java™ Tutorials > Learning the Java Language > Interfaces and Inheritance)
  site: docs.oracle.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/5-6/
  title: 'Tip 5-6: Hide the inner workings of blackboxes! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/interfaces
  title: Interfaces - define behavior for multiple types - C# | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BallAndSocket.html
  title: Ball And Socket
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Component_diagram
  title: Component diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: One interface, realized by two classes and used by a client.
review:
  status: generated
  flags: []
---

## Explanation

An interface in UML (the Unified Modeling Language) is a contract. It names operations that something must offer. It does not say how they work. You cannot create an object directly from an interface. A class or component has to realize it, meaning it supplies the real behavior. In Java, a class uses the `implements` keyword. In C#, the class lists the interface after a colon in its declaration.

**Interface versus abstract class.** An abstract class can share state between related types. A C# interface cannot hold instance fields or constructors, and its members are public by default. A class can implement several interfaces but inherit from only one base class. So abstract classes suit related types that share state. Interfaces suit contracts that span unrelated hierarchies.

**Two ways to draw it.** The explicit form is a class box for the interface. The compact form is a lollipop. A ball shows an interface that something provides. UML 2 added the socket to show an interface that something requires. Microsoft popularized the ball. The article Provided and Required Interface covers this in more depth.

**Component diagrams.** In a component diagram, the provided interface appears as a ball. Ball-and-socket is an accepted way to present interfaces there. One expert notes that mating a ball with a socket was ruled an error outside composite structure connectors. UML 1 used a dependency instead.

**Why architects care.** A black box exposes only its responsibility and its input and output interfaces. Additional details about its inner workings are usually not required. The inner workings can change without clients having to adapt. This is information hiding.

## Example

A shop system defines an interface `PaymentService` with one operation, `charge`. Two classes, `CardPayment` and `InvoicePayment`, each realize it. The checkout component depends only on `PaymentService`. In the diagram, the payment components show a ball for `PaymentService`, and checkout shows a socket for it.

## Trade-offs

Interfaces cannot hold instance fields or constructors in C#. If related types need shared state, an abstract class fits better. A class can inherit only one base class, but it can implement many interfaces. Martin Fowler says he may use the dependency notation between the ball and socket in more complicated cases, and that when he does, he prefers explicit class boxes for the interfaces.
