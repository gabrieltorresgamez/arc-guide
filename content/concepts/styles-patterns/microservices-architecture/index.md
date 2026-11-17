---
title: Microservices Architecture
slug: microservices-architecture
category: styles-patterns
kind: style
summary: Microservices split a system into small services, each built around one business capability and
  deployable on its own. The style gains team autonomy and flexibility, but it adds network, data, and
  operations costs.
arc42:
- 4
- 5
- 8
- 9
- 11
step: s07-solution-strategy
related:
- bounded-context
- domain-driven-design
- coupling-and-cohesion
- service-oriented-architecture
- synchronous-vs-asynchronous-communication
- shared-database
- business-capability
- architecture-style
checks:
- The document says why microservices were chosen over a modular monolith.
- Each service implements a single business capability within a bounded context.
- Each service owns its data and schema, with no shared database.
- The document explains how data stays consistent across services without ACID transactions.
- Long call chains and chatty APIs between services are avoided or justified.
- Orchestration, CI/CD, centralized logging, and distributed tracing are in place or planned.
sources:
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/MicroservicePremium.html
  title: Microservice Premium
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/MonolithFirst.html
  title: Monolith First
  site: martinfowler.com
  accessed: '2026-11-17'
- url: https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity
  title: 'Deconstructing the Monolith: Designing Software that Maximizes Developer Productivity'
  site: shopify.engineering
  accessed: '2026-11-17'
- url: https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer
  title: 'Modular Monolith: A Primer'
  site: kamilgrzybek.com
  accessed: '2026-11-17'
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices
  title: Microservices Architecture Style - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/approaches/microservice-architecture
  title: "Microservice Architecture | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/self-contained-systems
  title: "Self-Contained Systems | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams:
- file: diagram-1.mmd
  caption: Services organized by business capability, each owning its data, communicating through lightweight
    interfaces.
review:
  status: generated
  flags: []
---

## Explanation

A microservices architecture builds a system from many small services. Each service can be deployed on its own. Fowler and Lewis give this independent deployability as one main reason to use services instead of libraries as components.

**Split by business capability.** Many systems divide into technical layers. Microservices divide by business capability instead. Each service implements one capability within a bounded context. A bounded context is a boundary around one part of a complex domain. Domain-driven design uses it to split that domain. See the articles Bounded Context and Domain-Driven Design.

**Size and granularity.** Size is often described by team size: a single small team can maintain each service. Avoid services that are too fine-grained. Keep functions that change together in the same service. Chatty communication between services signals tight coupling and low cohesion. See Coupling and Cohesion.

**Own data.** Each service owns its data and schema. Services share no database. This cuts dependencies between services and lets them evolve independently.

**Communication.** Services usually talk through HTTP request-response with resource APIs, or through lightweight messaging. Long call chains (A calls B, which calls C) add latency and network load. APIs should not be chatty, and asynchronous communication helps where possible.

**Operations.** Success needs a mature DevOps culture. A management or orchestration component, typically a platform such as Kubernetes, is a common part of the architecture, and CI/CD pipelines are a recommended practice for automating testing and deployment. Observability needs centralized logging and distributed tracing. Teams may pick different languages and frameworks. Too many make the system hard to maintain, so some governance is advisable.

**Origin.** The term was first discussed at an architects' workshop near Venice in 2011 [src:1].

**In the arc42 quality model.** It has approach pages on [Microservice Architecture](https://quality.arc42.org/approaches/microservice-architecture) and [Self-Contained Systems](https://quality.arc42.org/approaches/self-contained-systems).

## Example

An online shop has separate services for catalog, orders, and payments. Each has its own small team and its own database. The orders service never reads the payments database. It asks the payments service through an API or a message. The team can release a payments change without touching the other two services.

## Trade-offs

Microservices add a cost premium. Fowler advises that most systems should be built as a single monolithic application, with attention to good modularity inside it [src:2]. Microservices fit only when the system's complexity and size justify them.

**The usual alternative: a modular monolith.** As in any monolith, all parts of the system form one deployment unit. The code, however, is split into modules whose boundaries are defined and respected. One practitioner defines each module as a business module that provides a complete set of features. Shopify chose this path for its large codebase. Among its reasons: microservices would have added a test and deployment pipeline and infrastructure overhead for each service. Fowler calls a monolith designed with care for modularity, at its API boundaries and in how data is stored, the logical way to make a later move to microservices relatively simple [src:3]. He also warns that many attempts to break up a monolith end in a mess.

Costs of microservices:

- **Data consistency:** A change that spans several services is unlikely to be an ACID transaction. Teams use BASE and eventual consistency instead, which makes data consistency a challenge.
- **Latency:** Calls over the network add delay, especially in long chains.
- **Debugging:** Correlated logging across services can be hard.
- **Operations:** The system needs DevOps maturity, orchestration, and automation.
- **Technology sprawl:** Free technology choice creates a maintenance burden.
