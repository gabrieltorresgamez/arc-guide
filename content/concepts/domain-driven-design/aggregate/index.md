---
title: Aggregate
slug: aggregate
category: domain-driven-design
kind: pattern
summary: An aggregate is a group of related domain objects treated as one unit. One object, the root,
  is the only entry point from outside, and it keeps the whole group consistent.
arc42:
- 5
- 8
step: s06-domain
related:
- domain-driven-design
- ddd-modeling-elements
- entity
- value-object
- entity-vs-value-object
- domain-model
- bounded-context
- cargo-shipping-domain-model-example
checks:
- Each aggregate names one root object.
- References from outside an aggregate point only to its root.
- Changes to an aggregate go through methods on the root.
- Aggregate boundaries follow the transactions that must be consistent together.
- Other aggregates are referenced by identity (foreign key), not by direct navigation.
sources:
- url: https://martinfowler.com/bliki/DDD_Aggregate.html
  title: D D D_ Aggregate
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-domain-model
  title: Designing a microservice domain model - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Domain-driven_design
  title: Domain-driven design - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'An order aggregate: outside code reaches only the root.'
review:
  status: generated
  flags: []
---

## Explanation

An aggregate is a cluster of domain objects that the system treats as a single unit. (See Domain-Driven Design and Entity and Value Object for these terms.)

**The root.** One object in the cluster acts as the aggregate root. Code outside the aggregate may hold references only to this root. It may not point at any other object inside.

**Why the root matters.** The root is the single entry point for updates. It offers methods that change the aggregate. Because every change passes through it, the root can check the rules that must hold and keep the whole aggregate consistent. If code changed a child object directly, it would bypass those checks.

**Finding the boundary.** Think about transactions. A transaction is a set of changes that must succeed or fail together. Objects that must stay consistent together in one transaction form an aggregate. You usually define an aggregate from the transactions you need.

**Links between aggregates.** Avoid direct navigation from one aggregate to another. Store only the identity of the other aggregate, such as a foreign key (a stored ID that points to another record).

## Example

An online shop has orders. Each order contains order items. Placing an order and changing its items must succeed together, so the order and its items form one aggregate. The order is the root.

Other code asks the order to add or remove an item. It never edits an item directly. The order checks its rules first. A shipment record elsewhere stores only the order's ID, not a link to the order object.

## Trade-offs

Routing every change through the root gives one guarded place for rules. The cost is that callers cannot edit inner objects directly. Referencing other aggregates only by identity keeps boundaries clear. The cost is that you cannot navigate straight from one aggregate to another.
