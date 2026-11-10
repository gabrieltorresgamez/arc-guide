---
title: Domain Layer Separation
slug: domain-layer
category: domain-driven-design
kind: pattern
summary: Domain layer separation keeps business logic in its own layer, apart from the user interface,
  the application layer, and technical infrastructure. Several front ends can then reuse the same logic.
arc42:
- 5
- 8
step: s06-domain
related:
- layered-architecture
- domain-driven-design
- bounded-context
- domain-model
- separation-of-concerns
- layers-pattern
- clean-architecture
- model-view-controller-pattern
checks:
- The domain layer is described as isolated from the other layers.
- The application layer is thin and the key logic sits in the domain layer.
- Each layer depends only on the layer below it.
- Layers are described as logical layers, not as physical tiers.
sources:
- url: https://martinfowler.com/bliki/PresentationDomainDataLayering.html
  title: Presentation Domain Data Layering
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://herbertograca.com/2015/09/18/domain-driven-design-by-eric-evans-chap-4-isolationg-the-domain/
  title: DDD.4 – Isolating the domain – @hgraca
  site: herbertograca.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/AnemicDomainModel.html
  title: Anemic Domain Model
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://uniknow.github.io/AgileDev/site/0.1.10-SNAPSHOT/ddd/layered_architecture.html
  title: AgileDev - Layered Architecture
  site: uniknow.github.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Logical layers: the application layer stays thin and the domain layer holds the key logic.'
review:
  status: generated
  flags: []
---

## Explanation

Domain layer separation puts business logic into a layer of its own. The domain layer is the heart of a bounded context (see Bounded Context). It should be well isolated from the other layers. This isolation is central to Domain-Driven Design (see Domain-Driven Design).

**The layers around it**

- The presentation layer shows information to users and takes their input.
- The application layer, also called the service layer, stays thin. The key logic lies in the domain layer, not here.
- The infrastructure layer acts as a supporting library for the other layers.

**Logical, not physical**

These layers are logical layers, not physical tiers. You can split the code into layers without putting each layer on its own server.

**Direction of dependency**

Each layer should depend only on the layer below it.

**Why it pays off**

Separating presentation from domain logic lets you build several presentations on top of the same domain logic. You do not have to copy that logic into each one.

For the general idea of layers, see Layered Architecture.

## Example

An insurance company has a web portal and a mobile app. Both need the same rule for calculating a premium. The team keeps that rule in the domain layer. Both front ends reach it through a thin application layer. When the rule changes, the team edits one place. Neither front end holds its own copy.

## Trade-offs

One caution: the application layer must stay thin. If key logic moves into it, the domain layer stops being the home of the business rules. Also remember that layers are logical. Drawing layers on a diagram does not by itself decide how the system is deployed.
