---
title: Clean Architecture
slug: clean-architecture
category: styles-patterns
kind: style
summary: Clean Architecture arranges code in circles. Source code dependencies point only inward, toward
  the business rules. Web, database, and frameworks stay on the outside, so the rules can be tested without
  them.
arc42:
- 4
- 5
- 8
step: s07-solution-strategy
related:
- layered-architecture
- testability
- domain-driven-design
- use-case
- separation-of-concerns
- model-view-controller-pattern
- architectural-style
checks:
- The document states that source code dependencies point only inward.
- Boundaries between layers are crossed with simple data structures such as DTOs.
- Where control flow runs against the dependency direction, an output port interface in the inner circle
  resolves it.
- Business rules can be tested without the UI, database, or web server.
sources:
- url: https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
  title: Clean Coder Blog
  site: blog.cleancoder.com
  accessed: '2026-11-09'
- url: https://alistair.cockburn.us/hexagonal-architecture
  title: hexagonal-architecture
  site: alistair.cockburn.us
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Control flow runs from controller through use case to presenter. The presenter implements the
    output port, so the dependency still points inward.
review:
  status: generated
  flags: []
---

## Explanation

Clean Architecture organizes a system as circles, or layers. Business rules sit toward the center. Technical details sit on the outside.

**The Dependency Rule.** Source code dependencies may only point inward. An inner layer never refers to anything in an outer layer.

**Layers:**

- **Use cases** hold application-specific business rules. They describe what this particular application does. (See the article on Use Case.)
- **Interface adapters** hold presenters, views, and controllers. They connect the inner rules to the outside world.
- **Frameworks and drivers** form the outer layer. The web and the database are treated as details, not as the core of the system.

**Control flow versus dependency direction.** At runtime, a request begins in the controller. It moves through the use case and ends in the presenter. This path goes inward and then back outward. It seems to conflict with the Dependency Rule.

The Dependency Inversion Principle resolves this conflict at the boundaries. The use case does not call the presenter directly. It calls an output port, which is an interface defined in the inner circle. The outer layer implements that interface. The code dependency therefore still points inward.

**Crossing boundaries.** Data crosses a boundary as a simple data structure, such as a Data Transfer Object (DTO). A DTO is a plain container for values.

**Why it helps.** Business rules can be tested without the UI, the database, or a web server.

**A related idea.** Hexagonal Architecture has a similar aim. It lets users, programs, or tests drive an application. It also lets the application be developed and tested in isolation from runtime devices and databases. There, technology-specific adapters convert events that arrive at a port.

## Example

An online shop has a rule: an order needs at least one item. A use case "Place order" applies that rule. A web controller receives the request and passes a simple data object to the use case. The use case reports its result through an output port. A presenter implements that port and prepares the answer for the screen. A test can call the use case directly, with no web server and no database.
