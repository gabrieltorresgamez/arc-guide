---
title: Entity Life Cycle
slug: entity-life-cycle
category: domain-driven-design
kind: concept
summary: An entity life cycle is the path an entity follows over time, from the moment it gets an identity
  until it ends. Named, guarded transitions and invariants stop it from entering invalid states.
arc42:
- 5
- 8
- 12
step: s06-domain
related:
- entity
- aggregate
- state-machine-diagram
- business-object-lifecycle
- domain-model
- entity-vs-value-object
- bounded-context
- ddd-modeling-elements
checks:
- State changes are named methods that reject invalid transitions immediately.
- Invariants block changes to entities in terminal states.
- The aggregate root enforces integrity, and owned objects are reached only through it.
- Complex creation of objects or aggregates is handled by factories, not by the model itself.
sources:
- url: https://martinfowler.com/bliki/EvansClassification.html
  title: Evans Classification
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.proteanhq.com/patterns/aggregate-state-machines/
  title: Aggregate State Machines - Protean
  site: docs.proteanhq.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/DDD_Aggregate.html
  title: D D D_ Aggregate
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://herbertograca.com/2015/10/04/domain-driven-design-by-eric-evans-chap-6-the-lifecycle-of-a-domain-object/
  title: DDD.6 – The lifecycle of a domain object – @hgraca
  site: herbertograca.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Generic order life cycle: guarded transitions between states, ending in terminal states.'
review:
  status: generated
  flags: []
---

## Explanation

An entity is a domain object with an identity that persists through time and across different representations (see the article Entity). The life cycle describes what happens to that entity along the way: which states it can be in and how it moves between them.

**Transitions are named and guarded.** Each change of state should be a named method, such as "ship" or "cancel". Each method carries a guard. A guard is a check that rejects an invalid change. The method raises an error the moment code tries a forbidden move.

**Invariants protect the end of the life cycle.** An invariant is a rule that must always hold. One useful invariant blocks any change to an entity in a terminal state, meaning a final state such as a completed or cancelled order. The aggregate therefore enforces its own life cycle.

**Aggregates carry the rules.** An aggregate is a cluster of domain objects treated as one unit (see the article Aggregate). Its root entity ensures the integrity of the whole cluster. Owned objects are reached only through that root, and the root is responsible for them.

**Factories and repositories cover the ends.** The start of the life cycle is creation. A factory handles complex construction of an object or aggregate and keeps creation logic out of the model. A repository separates application and domain logic from persistence. In most cases only aggregate roots need to be searchable through it.

## Example

Consider an order in a web shop. A factory builds it from a basket and gives it an identity. The order then moves through states such as placed, paid, shipped, and cancelled.

The order has a method "ship". Its guard rejects the call if the order is not yet paid, and raises an error at once. Once the order is cancelled, a rule on the order root blocks any further change. Other code reaches the order's line items only through the order itself.

## Trade-offs

Putting guards and invariants inside the aggregate keeps the rules in one place and catches mistakes immediately.
