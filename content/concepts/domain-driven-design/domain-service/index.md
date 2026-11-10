---
title: Domain Service
slug: domain-service
category: domain-driven-design
kind: pattern
summary: A domain service is a stateless object that holds business logic which does not fit naturally
  in one entity or value object. It often covers rules that span several entities or aggregates.
arc42:
- 5
- 8
step: s06-domain
related:
- domain-driven-design
- entity
- value-object
- aggregate
- domain-layer
- ddd-modeling-elements
- domain-model
- ubiquitous-language
checks:
- Business rules that span several entities or aggregates sit in a domain service, not in an application
  service.
- Application services contain no business logic and only coordinate domain services, repositories, and
  transactions.
- Entities keep their own behavior, so the model is not anemic.
- Domain services are stateless and are not confused with microservices.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/microservices/model/tactical-domain-driven-design
  title: Use Tactical DDD to Design Microservices - Azure Architecture Center | Microsoft Learn
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
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

In domain-driven design, a "service" is a stateless object. It implements logic that does not naturally belong to an entity or a value object. The word has nothing to do with microservices.

**What a domain service does**

A domain service holds business rules that span several entities or aggregates. An aggregate is a cluster of related objects treated as one unit. In the drone-delivery example, the Scheduler is a domain service. No single drone or delivery owns the scheduling rules, so a separate service holds them.

**How it differs from other services**

Application services orchestrate a use case. They call domain services and repositories and manage transactions. They also handle concerns such as user authentication or SMS notifications. They contain no business logic themselves. The business rules stay in the domain service.

A service layer is a related idea. It defines the boundary of an application and the operations it offers. It coordinates transactions and application logic. It is kept thin: the key logic stays in the domain layer.

**Do not overuse it**

Entities should keep their own behavior. If you move business logic out of entities into service classes, you get an anemic domain model. This antipattern defeats the main benefit of DDD: keeping the business rules inside the domain model. Fowler warns that pulling all behavior into services leaves you with transaction scripts and wastes the domain model.

So a domain service is the exception. Use it only when the logic does not belong to one entity or value object.

## Example

An online shop must decide which warehouse ships an order. The rule looks at the order, stock records, and several warehouses. No single one of these objects owns the rule. The team puts it in a stateless domain service. A separate application service receives the request, calls the domain service, and manages the transaction. The business rule lives only in the domain service.

## Trade-offs

A domain service gives rules that span several objects a clear home. The cost is the risk of an anemic domain model. If teams reach for services too often, entities lose their behavior and the domain model loses its value. Keep the split clear: domain services hold business rules, application services only coordinate.
