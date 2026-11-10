---
title: Entity
slug: entity
category: domain-driven-design
kind: concept
summary: An entity is a domain object defined by its identity, not its attributes. Its attributes can
  change and it stays the same thing. Two objects with equal attributes can still be different entities.
arc42:
- 5
- 8
- 12
step: s06-domain
related:
- entity-vs-value-object
- value-object
- entity-life-cycle
- aggregate
- bounded-context
- domain-model
- ddd-modeling-elements
- business-object-lifecycle
checks:
- Each entity has a defined identity, and the document states what counts as the same entity.
- Entity equality is based on identity only, not on attributes.
- Entities contain behavior that enforces their own invariants, not only data.
- Where an entity appears in several bounded contexts, each context holds only the attributes it needs.
- The document explains why a concept such as an address is an entity or a value object in this context.
sources:
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-domain-model
  title: Designing a microservice domain model - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/EvansClassification.html
  title: Evans Classification
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/ValueObject.html
  title: Value Object
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://lostechies.com/jimmybogard/2008/05/21/entities-value-objects-aggregates-and-roots/
  title: Entities, Value Objects, Aggregates and Roots · Los Techies
  site: lostechies.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Artifact-centric_business_process_model
  title: Artifact-centric business process model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An entity is a thing in the business domain that you track over time. A person or an order is a typical example. What makes it an entity is its identity, its continuity, and its persistence over time. Attributes such as name or address describe it but do not define it.

**Identity, not attributes.** Two people can share the same first and last name and still be two different entities. The reverse also holds. If two instances have different attribute values but share one identity value, and they are the same thing, the class is an entity. The model must say what "same identity" means.

**Identity across representations.** An entity keeps its identity through time and across different representations. Different systems care about different attributes of a person, yet it is always the same person. The same identity can also appear in several bounded contexts or microservices (see Bounded Context). Each context keeps only the attributes and behavior it needs. This keeps entities lean.

**Equality in code is not identity.** Value objects override equality, so equal values count as equal. Entities usually do not. An entity's equality should look only at its identity. A unique order number is one example. A generated surrogate key such as a GUID is another option.

**Behavior, not just data.** An entity should enforce its own rules. Its methods should hold the invariants (rules that must always hold) instead of having those rules spread across the application layer.

**Entity or value object?** A value object has no conceptual identity. You care what it is, not who it is. The same concept can be either one, depending on the business need. See Entity and Value Object.

**Life cycle.** In artifact-centric modeling, key business entities (called artifacts) are data objects whose manipulations define the process. They have prominent life cycles. See Entity Life Cycle.

## Example

A power utility stores customers and their service addresses. Two customers are both named "A. Smith". They are two entities with two customer numbers. If one of them moves and changes name and address, the customer number still points to the same entity. For billing, the utility must link bills directly to the address, so there the address also gets its own identity. A shipping context may know the same customer by the same number but keep only a delivery address.

## Trade-offs

Whether an address is an entity depends on the context.
