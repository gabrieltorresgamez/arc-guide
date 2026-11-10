---
title: Domain-Driven Design of the Data Model
slug: domain-modeling-procedure
category: domain-driven-design
kind: method
summary: Domain-driven design of the data model builds data structures from business knowledge. Teams
  use business vocabulary to find entities, value objects, aggregates and bounded contexts, and they keep
  refining the result.
arc42:
- 3
- 5
- 8
- 12
step: s06-domain
related:
- ubiquitous-language
- bounded-context
- aggregate
- entity-vs-value-object
- domain-event
- domain-service
- domain-model
- evolutionary-domain-modeling
checks:
- The model uses one shared vocabulary that developers and domain experts both understand.
- Each bounded context is named and consists of one or more aggregates.
- Each aggregate has a root that enforces its consistency boundary.
- Entities have identity and life cycle, while value objects are immutable.
sources:
- url: https://martinfowler.com/bliki/UbiquitousLanguage.html
  title: Ubiquitous Language
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/DDD_Aggregate.html
  title: D D D_ Aggregate
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://ozimmer.ch/modeling/2022/11/23/ContextMapperInsights.html
  title: Domain-Driven Design in Practice — Experience with Context Mapper
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/ValueObject.html
  title: Value Object
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/activities/DPR-TacticDDD.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'A bounded context holding one aggregate: an order root, its items, and a value object.'
review:
  status: generated
  flags: []
---

## Explanation

Domain-driven design (DDD) designs software based on models of the business domain. The building blocks and the shared language are described below.

**Shared language first.** A domain model acts as a shared vocabulary between developers and domain experts. See the article Ubiquitous Language. That vocabulary should evolve as the team learns more about the domain. So the model is not finished after one pass.

**Bounded contexts.** A bounded context is a central DDD pattern. Strategic design also describes how bounded contexts relate to each other. A bounded context typically consists of one or more aggregates.

**Entities and value objects.** An entity has an identity and a life cycle. A value object has neither, and it is immutable, so it never changes once created. Whether a concept is a value object depends on context.

**Aggregates.** An aggregate is a cluster of domain objects treated as one unit. It is also the unit for loading and saving data. Its root ensures the integrity of the aggregate as a whole, and aggregates serve as units of consistency. An order with its items is a typical case.

**Events and services.** Aggregates communicate state changes through domain events. A domain service holds logic that does not fit a single entity.

## Example

A small shop team talks with its sales experts and notes the terms they use: customer, order, order item, price, "order placed". The team keeps these words in the model, so developers and experts mean the same thing.

The customer becomes an entity, because it has an identity and a life cycle. A price becomes a value object. The order and its items form one aggregate, with the order as root. When an order changes state, the aggregate announces it with an "order placed" domain event. Later the team learns more and renames or reshapes terms.
