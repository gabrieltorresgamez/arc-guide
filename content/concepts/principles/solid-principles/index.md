---
title: SOLID Principles
slug: solid-principles
order: 70
category: principles
kind: principle
summary: "SOLID is a mnemonic for five object-oriented design principles: single responsibility, open-closed, Liskov substitution, interface segregation and dependency inversion. They aim at code that is easier to understand, change and maintain."
arc42:
- 8
step: s07-solution-strategy
related:
- coupling-and-cohesion
- separation-of-concerns
- modularity
- design-for-change
- information-hiding
- architecture-principle
checks:
- Where the code base follows SOLID, the documentation names the principles it relies on.
sources:
- url: https://en.wikipedia.org/wiki/SOLID
  title: "SOLID - Wikipedia"
  site: en.wikipedia.org
  accessed: '2026-11-16'
- url: https://en.wikipedia.org/wiki/Interface_segregation_principle
  title: Interface segregation principle - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/RoleInterface.html
  title: Role Interface
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/HeaderInterface.html
  title: Header Interface
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/RequiredInterface.html
  title: Required Interface
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
  title: Open–closed principle - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/dipInTheWild.html
  title: DIP in the Wild
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/Yagni.html
  title: Yagni
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

SOLID is a mnemonic acronym for five principles that are intended to make source code more understandable, flexible and maintainable. Robert C. Martin introduced the basic principles in his 2000 paper "Design Principles and Design Patterns", which was about software rot [src:1]. Michael Feathers coined the acronym around 2004 [src:1]. The principles apply to object-oriented programming, and they are also a core philosophy for methodologies such as agile software development.

- **Single responsibility (SRP):** there should never be more than one reason for a class to change. In other words, every class should have only one responsibility. It makes classes easier to understand, modify and test.
- **Open-closed (OCP):** software entities should be open for extension but closed for modification. A building block stays open to new behavior but closed to edits of its existing code. Other parts rely on a fixed interface, and new behavior arrives through new implementations of it.
- **Liskov substitution (LSP):** functions that use references to base classes must be able to use references to derived classes without knowing it. Replacing a superclass object with a subclass object must not break the program.
- **Interface segregation (ISP):** clients should not be forced to depend on interface methods that they do not use. The Interface Segregation Principle says code should not depend on methods it does not use [src:2]. Teams split large interfaces into smaller ones, each fitted to one role.
- **Dependency inversion (DIP):** one should depend on abstractions, not on concrete implementations. It reduces dependencies between modules and lets implementations change without affecting their clients.

## Example

A shop has an `Order` class that calculates prices, saves itself to the database and prints invoices. Each of those is a separate reason to change. Following the single responsibility principle, the team gives pricing, storage and invoicing to three classes. The order service then depends on a storage interface (dependency inversion), so the database can change without touching the order logic.

## Trade-offs

The sources present the principles by their benefits: maintainability, testability, flexibility, extensibility and loose coupling.
