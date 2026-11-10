---
title: Bounded Context
slug: bounded-context
category: domain-driven-design
kind: concept
summary: A bounded context is a boundary inside which one domain model applies. Large domains split into
  several contexts, each with its own model and vocabulary, so no single model has to fit everything.
arc42:
- 3
- 5
- 12
step: s06-domain
related:
- context-map
- ubiquitous-language
- domain-driven-design
- bounded-context-canvas
- microservices-architecture
- domain-model
- aggregate
- domain-event
checks:
- The document lists its bounded contexts and states which subdomain model each one holds.
- A context map shows the relationships and integration points between contexts, including external systems.
- Each bounded context owns its model and its database.
- Each context has a clear owning team, and no team owns several unrelated contexts.
- Terms that mean different things in different contexts are defined per context.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis
  title: Use Domain Analysis to Model Microservices - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/sk-sk/dotnet/architecture/microservices/architect-microservice-container-applications/data-sovereignty-per-microservice
  title: Data sovereignty per microservice - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Two bounded contexts model the same person differently and connect at an integration point.
review:
  status: generated
  flags: []
---

## Explanation

A model is a simplified picture of a business area. The larger the area, the harder it is to build one unified model for all of it. Domain-Driven Design (see the article Domain-Driven Design) responds by dividing a complex domain into several **bounded contexts** and mapping the relationships between them.

A bounded context marks the boundary where one specific domain model applies. Each context holds the model of a subdomain, which is one part of the wider business domain.

**Language depends on context.** Each bounded context can have its own ubiquitous language (see Ubiquitous Language). The same word can therefore mean different things in different contexts. "Account" is a typical example.

**One model per context.** Sharing a single model across subsystems adds complexity and slows change. It is better to build separate models of the same real-world thing, one per context. Each model keeps only the attributes that matter there.

**Ownership.** Each bounded context owns its model and its database. Team ownership should line up with the contexts. Conway's law can be used on purpose: analyze the domain to set boundaries, then assign teams to match. If one team owns several unrelated contexts, or one context needs coordination across many teams, revisit the boundaries or the team structure.

**Context maps.** A context map shows how bounded contexts relate. It highlights integration points and clarifies responsibilities. It can include external systems. Fowler considers drawing one usually worthwhile. See Context Map.

**Microservices.** A microservice is like a bounded context that is also a distributed service. The bounded context idea itself does not require distribution. A context can be a logical boundary inside a monolith, while a microservice is a separate process. See Microservices Architecture.

## Example

An online shop has a Sales context and a Shipping context. In Sales, a "customer" has a payment history and discount level. In Shipping, the same person is a "recipient" with an address and delivery window. Each context has its own model and its own database. A context map shows where the two connect.

## Trade-offs

Separate models mean the same real-world thing is described more than once. Even so, the sources favor this over one shared model, which adds complexity and slows evolution. Splitting also needs care. Boundaries and team structure must be kept in step, and a mismatch is a signal to revisit them.
