---
title: DDD Building Blocks (Tactical Patterns)
slug: ddd-building-blocks-tactical-patterns
order: 60
category: domain-driven-design
kind: pattern
summary: 'DDD building blocks are modeling elements: entities, value objects, aggregates, domain events,
  domain services and repositories. They align code with business problems and share business vocabulary.'
long_ok: true
arc42:
- 4
- 5
- 8
- 12
step: s06-domain
related:
- domain-driven-design
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
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-domain-model
  title: Designing a microservice domain model - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Domain-driven_design
  title: Domain-driven design - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/EvansClassification.html
  title: Evans Classification
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
- url: https://en.wikipedia.org/wiki/Value_object
  title: Value object - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation
  title: 'Domain events: Design and implementation - .NET | Microsoft Learn'
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/AnemicDomainModel.html
  title: Anemic Domain Model
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/eaaCatalog/serviceLayer.html
  title: Service Layer
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/PresentationDomainDataLayering.html
  title: Presentation Domain Data Layering
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://herbertograca.com/2015/09/18/domain-driven-design-by-eric-evans-chap-4-isolationg-the-domain/
  title: DDD.4 – Isolating the domain – @hgraca
  site: herbertograca.com
  accessed: '2026-11-09'
- url: https://uniknow.github.io/AgileDev/site/0.1.10-SNAPSHOT/ddd/layered_architecture.html
  title: AgileDev - Layered Architecture
  site: uniknow.github.io
  accessed: '2026-11-09'
- url: https://docs.proteanhq.com/patterns/aggregate-state-machines/
  title: Aggregate State Machines - Protean
  site: docs.proteanhq.com
  accessed: '2026-11-09'
- url: https://herbertograca.com/2015/10/04/domain-driven-design-by-eric-evans-chap-6-the-lifecycle-of-a-domain-object/
  title: DDD.6 – The lifecycle of a domain object – @hgraca
  site: herbertograca.com
  accessed: '2026-11-09'
- url: https://dddsample.sourceforge.net/characterization.html
  title: DDD Sample Application - Characterization of building blocks.
  site: dddsample.sourceforge.net
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/archive/msdn-magazine/2013/october/data-points-coding-for-domain-driven-design-tips-for-data-focused-devs-part-3
  title: 'Data Points - Coding for Domain-Driven Design: Tips for Data-Focused Devs, Part 3 | Microsoft
    Learn'
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://www.informit.com:443/articles/article.aspx?p=1398623&seqNum=16
  title: '16.15 Qualified Association | Applying UML and Patterns: UML Class Diagrams | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://modeling-languages.com/navigability-associations-conceptual-modeling/
  title: Navigability of associations is NOT a conceptual modeling concern
  site: modeling-languages.com
  accessed: '2026-11-09'
- url: http://uniknow.github.io/AgileDev/site/0.1.8-SNAPSHOT/parent/ddd/core/modules.html
  title: Domain Driven Design - Modules
  site: uniknow.github.io
  accessed: '2026-11-09'
- url: https://herbertograca.com/2015/09/29/domain-driven-design-by-eric-evans-chap-5-a-model-expressed-in-software/
  title: DDD.5 – A model expressed in software – @hgraca
  site: herbertograca.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
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

**Entity.** An entity has a unique identity that persists over time. Two instances with the same identity are the same thing, even when their attributes change. Entities should also hold behavior: validation, state transitions and business rules. A model whose entities hold only data is called an anemic domain model. Microsoft's guidance calls it an anti-pattern for complex domains, though it can be fine for simple CRUD services.

**Value object.** A value object has no identity. Objects with equal attribute values are interchangeable. Value objects are immutable. To change one, you create a new instance that replaces the old one. Immutability avoids aliasing bugs, where one object is shared and silently changed.

**Aggregate.** An aggregate is a cluster of domain objects treated as one unit. It is a consistency boundary that protects transactional rules. Exactly one entity is the root, and the aggregate is looked up through it.

**Domain event.** A domain event captures something significant that happened in the domain. Aggregates raise events after they change state. Events are the main way to coordinate work across aggregate boundaries.

**Domain service.** A domain service is a stateless object. It holds logic that does not naturally belong to one entity or value object. It encapsulates rules that span several entities or aggregates.

**Repository.** A repository sits between the domain and the data mapping layers. It offers a collection-like interface to domain objects and hides how they are stored.

**Layering.** The domain layer holds business concepts and rules. It must not depend on other layers. Storing data is delegated to the infrastructure layer.

**More about the building blocks.**

- **Aggregate:** An aggregate is a group of related domain objects treated as one unit. One object, the root, is the only entry point from outside, and it keeps the whole group consistent.
- **Entity:** An entity is a domain object defined by its identity, not its attributes. Its attributes can change and it stays the same thing. Two objects with equal attributes can still be different entities.
- **Value Object:** A value object is a small domain object with no identity of its own. Two value objects with the same attribute values are equal. Treat them as immutable: to change one, create a new one.
- **Domain Event:** A domain event records something that happened in the business and that other parts of the domain need to know about. It is named in the past tense, never changes, and can trigger reactions in other aggregates or bounded contexts.
- **Domain Service:** A domain service is a stateless object that holds business logic which does not fit naturally in one entity or value object. It often covers rules that span several entities or aggregates.
- **Domain Layer Separation:** Domain layer separation keeps business logic in its own layer, apart from the user interface, the application layer, and technical infrastructure. Several front ends can then reuse the same logic.
- **Entity Life Cycle:** One framework's guidance models the life cycle of an aggregate as a state machine: a closed set of states, changed only through guarded transition methods.
- **Entity and Value Object:** An entity is tracked by an identity that lasts even as its attributes change. A value object has no identity, is immutable, and equals another when all its values match.
- **Constraining Associations:** Constraining associations means limiting how objects in a domain model can reach each other. You impose a direction or add a qualifier, so each remaining link needs less implementation.
- **Module:** A module groups related domain concepts so people can understand one group at a time. Choose modules by meaning, not by technical category, and give them names the whole team uses.

## Example

A library models a reader who borrows books. Reader is an aggregate root and an entity: the same reader stays the same reader after a change of address. Each loan sits inside the reader aggregate. A loan period (start and due date) is a value object. Extending a loan creates a new period instead of editing the old one. A lending service holds the rule for lending a book, because it involves both a reader and a book. When a loan is made, a "book lent" event is raised so other parts can react. A reader repository loads and saves readers without exposing the database.

## Trade-offs

Treat the patterns as a means, not a goal. Their value comes from alignment with the business problem and shared terms, not from using every pattern.
