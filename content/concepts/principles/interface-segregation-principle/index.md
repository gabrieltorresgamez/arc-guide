---
title: Interface Segregation Principle
slug: interface-segregation-principle
category: principles
kind: principle
summary: The Interface Segregation Principle says code should not depend on methods it does not use. Teams
  split large interfaces into smaller ones, each fitted to one role.
arc42:
- 5
- 8
step: s10-document
related:
- loose-coupling
- coupling-and-cohesion
- information-hiding
- uml-interface
- provided-and-required-interface
- reduce-coupling
- split-module
- patterns-for-api-design
checks:
- Interfaces are defined around the needs of specific consumers, not copied from all public methods of
  a class.
- No component is forced to depend on methods it does not use.
- No single large class or interface serves many different clients with many different methods.
sources:
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
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An interface is a list of methods that one piece of code offers to another. The Interface Segregation Principle (ISP) has one rule: code must not be made to depend on methods that it never uses. When an interface is large, the fix is to split it into smaller, role-specific interfaces.

**Where the idea came from.** Robert C. Martin formulated ISP while consulting for Xerox. Xerox had built a new printer system that could do many tasks, such as stapling and faxing. A single Job class grew into a "fat" class. It held many methods, each meant for a different client. Every client was therefore tied to methods it never used.

**What a role interface is.** A role interface is defined by one specific interaction between a supplier (the code that offers methods) and its consumers (the code that calls them). Often a class does not use all the methods of the class it collaborates with. A role interface shows which methods a consumer actually needs.

**The opposite: the header interface.** A header interface copies all public methods of a class into one interface. This is the reverse of a role interface.

**Who should shape the interface.** Required interfaces are specified, and often defined, by the client. Thinking about what clients require often gives more useful interfaces, and that view leads toward role interfaces.

## Example

A reporting tool and a billing tool both call one `CustomerService` interface. It offers `getName`, `getAddress`, `changeAddress`, `closeAccount` and `exportAll`. The reporting tool needs only `getName` and `getAddress`. A team applies ISP and defines a small read-only interface with those two methods. Billing gets its own interface with the methods it needs. Each client now sees only what it uses.

## Trade-offs

Role interfaces have costs. They take more design effort, and they create a sense of dependence on the consumers, because the interface is shaped around them. Martin Fowler much prefers them and suggests pushing toward them as much as you can.
