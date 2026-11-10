---
title: Component Design Principles
slug: component-design-principles
category: principles
kind: principle
summary: Component design principles guide how to build parts of a system so they stay loosely coupled
  and easy to change. They hide internals, depend on stable interfaces, and keep wiring separate from
  use.
arc42:
- 4
- 5
- 8
- 9
step: s07-solution-strategy
related:
- information-hiding
- design-for-change
- loose-coupling
- coupling-and-cohesion
- reduce-coupling
- modifiability-tactics
- interface-segregation-principle
- open-closed-principle
checks:
- Modules are defined around design decisions that are difficult or likely to change, and each module
  hides such a decision.
- Dependencies point toward abstractions, not concrete implementations.
- Components expose state only through well-defined functions, and their public contracts are stable.
- Service configuration is kept separate from service use.
- Any intermediary (broker, mediator, bus) is justified against the extra hop it adds.
sources:
- url: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles
  title: Architectural principles - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/injection.html
  title: Inversion of Control Containers and the Dependency Injection pattern
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://blog.acolyer.org/2016/09/05/on-the-criteria-to-be-used-in-decomposing-systems-into-modules/
  title: On the criteria to be used in decomposing systems into modules – the morning paper
  site: blog.acolyer.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/InversionOfControl.html
  title: Inversion Of Control
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/dipInTheWild.html
  title: DIP in the Wild
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/approaches/reduce-coupling
  title: Reduce Coupling | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A component depends on an interface. A separate assembler wires in the implementation.
review:
  status: generated
  flags: []
---

## Explanation

Component design principles are guidelines for building a system from discrete parts. The parts are loosely coupled. They talk through explicit interfaces or messages, not through shared internals. See Loose Coupling and Coupling and Cohesion.

**Design for change and information hiding.** Start from a list of design decisions that are difficult or likely to change. Do not start from a flowchart of processing steps. Then give each module one such decision to hide from the others. This is information hiding (see Information Hiding and Design for Change).

**Interface abstraction.** Dependencies should point toward abstractions, not toward concrete implementations. This is dependency inversion. It keeps an application loosely coupled and testable. It also makes dependency injection possible.

**Encapsulation.** A component exposes behavior through well-defined functions and keeps its state private. Its internals can then change without breaking its collaborators. This holds as long as the public contract stays stable.

**Narrow, explicit interfaces.** These make a split into modules real instead of nominal. Reducing coupling means the remaining dependencies are fewer, narrower and explicit. Change then stays local (see Reduce Coupling).

**Use an intermediary.** A broker, message bus or mediator sits between components, so they do not call each other directly.

**Dependency injection and inversion of control.** Three ideas are easy to confuse:
- Dependency injection (DI) is about wiring. A separate assembler object fills in a component's dependencies.
- Inversion of control (IoC) is about direction. A framework calls your code, not the reverse. It is also called the Hollywood Principle.
- The Dependency Inversion Principle is about the shape of the abstraction you depend on.

The key point behind DI and its alternative, Service Locator, is to keep the configuration of services separate from their use. With a Service Locator, every user depends on the locator.

## Example

A shop's order component needs to send payment requests. It depends on a small "payment" interface, not on one payment provider's code. At startup, a separate assembler hands the order component the provider that is in use. The provider's data format stays hidden inside the provider module. When the shop switches provider, only the provider module and the assembler change. The order component stays as it is.

## Trade-offs

Abstractions have costs. They should match the domain, and factoring out things nobody needs breaks the YAGNI rule ("you aren't gonna need it"). Intermediaries add indirection and can become a bottleneck. Apply these principles where change is likely, not everywhere.
