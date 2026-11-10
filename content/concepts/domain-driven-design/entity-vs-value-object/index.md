---
title: Entity and Value Object
slug: entity-vs-value-object
category: domain-driven-design
kind: pattern
summary: An entity is tracked by an identity that lasts even as its attributes change. A value object
  has no identity, is immutable, and equals another when all its values match.
arc42:
- 5
- 8
- 12
step: s06-domain
related:
- entity
- value-object
- domain-driven-design
- cargo-shipping-domain-model-example
- aggregate
- domain-model
- ddd-modeling-elements
- entity-life-cycle
checks:
- Each entity in the model has an identity that stays the same through its life.
- Value objects are immutable and are compared by their attribute values.
- Objects with a life cycle and state transitions that matter to the business are modeled as entities.
sources:
- url: https://martinfowler.com/bliki/EvansClassification.html
  title: Evans Classification
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://lostechies.com/jimmybogard/2008/05/21/entities-value-objects-aggregates-and-roots/
  title: Entities, Value Objects, Aggregates and Roots · Los Techies
  site: lostechies.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/ValueObject.html
  title: Value Object
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://dddsample.sourceforge.net/characterization.html
  title: DDD Sample Application - Characterization of building blocks.
  site: dddsample.sourceforge.net
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Domain-Driven Design (see the article Domain-Driven Design) builds a model of a business from a few basic parts. Two of them are the entity and the value object. They differ in how you decide that two objects are the same.

**Entity.** An entity has an identity that lasts through time and across different representations. Its attributes do not define it. A thread of continuity and identity does. If its attributes change, it is still the same thing.

**Value object.** A value object has no conceptual identity. It describes a characteristic of a thing. Only the combination of its attributes matters. Two value objects with equal values for all attributes count as equal. For example, two point objects that both hold the coordinates (2,3) can be treated as the same.

**Immutability.** Value objects should be immutable, meaning they never change after creation. This avoids aliasing bugs. An aliasing bug happens when two parts of a program share one object and one part changes it without the other knowing. Immutability also makes value objects easy to handle. You can create them, discard them, and pass them around freely.

**Cargo example.** The DDD Sample (see the article Cargo Shipping Domain Model) treats a cargo as an entity. A cargo has a clear identity. It also has a life cycle with state transitions that the business cares about. Its tracking id is assigned when the cargo is created and never changes.

**How to choose.** Ask whether you need to follow this thing over time as the same thing. If yes, it is likely an entity. If you only care about what it looks like, it is likely a value object.

## Example

A shop models its orders. An order is an entity. It gets an order number when it is created, and that number never changes. Its status moves from "placed" to "shipped", but it stays the same order. A price of 10.00 USD is a value object. Any two prices of 10.00 USD are interchangeable. To change a price, the shop replaces the whole value with a new one. It does not edit the old one.

## Trade-offs

Treating something as an entity means you must assign and protect its identity. Treating it as a value object means you must never change it. You replace it instead.
