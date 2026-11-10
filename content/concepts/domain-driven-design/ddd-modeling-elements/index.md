---
title: DDD Building Blocks (Tactical Patterns)
slug: ddd-modeling-elements
category: domain-driven-design
kind: pattern
summary: 'DDD building blocks are modeling elements: entities, value objects, aggregates, domain events,
  domain services and repositories. They align code with business problems and share business vocabulary.'
arc42:
- 4
- 5
- 8
- 12
step: s06-domain
related:
- domain-driven-design
- entity
- value-object
- aggregate
- domain-event
- domain-service
- domain-layer
- ubiquitous-language
checks:
- Each entity in the domain model has a unique identity, and its validation and state transitions live
  in the entity itself.
- Value objects are immutable and are replaced by new instances when they change.
- Each aggregate names exactly one root entity and states the consistency rules it protects.
- Logic spanning several entities or aggregates sits in a stateless domain service.
- The domain layer does not depend on other layers, and persistence is delegated to infrastructure.
sources:
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice
  title: Designing a DDD-oriented microservice - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/microservices/model/tactical-domain-driven-design
  title: Use Tactical DDD to Design Microservices - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/eaaCatalog/repository.html
  title: Repository
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/ValueObject.html
  title: Value Object
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/DDD_Aggregate.html
  title: D D D_ Aggregate
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/eaaDev/DomainEvent.html
  title: Domain Event
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'Generic library example: an aggregate with a root entity, a value object, a domain service
    and a repository.'
review:
  status: generated
  flags: []
---

## Explanation

Domain-Driven Design (see Domain-Driven Design) offers building blocks for modeling business logic. The patterns themselves are not the point. The value lies in organizing code around the business problem and using the same business terms everywhere. That shared vocabulary is the ubiquitous language (see Ubiquitous Language).

**Entity.** An entity has a unique identity that persists over time. Two instances with the same identity are the same thing, even when their attributes change. Entities should also hold behavior: validation, state transitions and business rules. An entity with only data is called an anemic domain model, and you should avoid it. See Entity.

**Value object.** A value object has no identity. Objects with equal attribute values are interchangeable. Value objects are immutable. To change one, you create a new instance that replaces the old one. Immutability avoids aliasing bugs, where one object is shared and silently changed. See Value Object and Entity and Value Object.

**Aggregate.** An aggregate is a cluster of domain objects treated as one unit. It is a consistency boundary that protects transactional rules. Exactly one entity is the root, and the aggregate is looked up through it. See Aggregate.

**Domain event.** A domain event captures something significant that happened in the domain. Aggregates raise events after they change state. Events are the main way to coordinate work across aggregate boundaries. See Domain Event.

**Domain service.** A domain service is a stateless object. It holds logic that does not naturally belong to one entity or value object. It encapsulates rules that span several entities or aggregates. See Domain Service.

**Repository.** A repository sits between the domain and the data mapping layers. It offers a collection-like interface to domain objects and hides how they are stored.

**Layering.** The domain layer holds business concepts and rules. It must not depend on other layers. Storing data is delegated to the infrastructure layer. See Domain Layer Separation.

## Example

A library models a reader who borrows books. Reader is an aggregate root and an entity: the same reader stays the same reader after a change of address. Each loan sits inside the reader aggregate. A loan period (start and due date) is a value object. Extending a loan creates a new period instead of editing the old one. A lending service holds the rule for lending a book, because it involves both a reader and a book. When a loan is made, a "book lent" event is raised so other parts can react. A reader repository loads and saves readers without exposing the database.

## Trade-offs

Treat the patterns as a means, not a goal. Their value comes from alignment with the business problem and shared terms, not from using every pattern.
