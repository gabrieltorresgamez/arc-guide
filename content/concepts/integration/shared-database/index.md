---
title: Shared Database
slug: shared-database
category: integration
kind: pattern
summary: A shared database lets several applications exchange data by storing it in one common database.
  Information is shared quickly and consistently. The price is deep coupling to one schema, which is hard
  to design and risky to change.
arc42:
- 3
- 5
- 8
- 9
- 11
step: s08-integration-data
related:
- integration-pattern
- file-transfer
- remote-procedure-call
- messaging
- microservices-architecture
- coupling-and-cohesion
- canonical-data-model
checks:
- The document names which applications share the database and states that all of them are coupled to
  its schema.
- Ownership and agreement of the shared schema across teams or departments is addressed.
- The risk of changing applications that use the shared database is acknowledged.
- The choice of a shared database over file transfer, remote invocation, messaging or database-per-service
  is justified.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/SharedDataBaseIntegration.html
  title: Shared Database - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/IntegrationDatabase.html
  title: Integration Database
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Several applications store and read data in one common database.
review:
  status: generated
  flags: []
---

## Explanation

A shared database is an integration style. Applications built separately, even in different languages and on different platforms, store their data in one common database. Each application reads what the others wrote. This shares information rapidly and consistently.

It is one of four integration styles: file transfer, shared database, remote invocation and messaging. See the article Integration Styles for the overview. Each style addresses the same integration problem, and what differentiates them is different forces seeking a more sophisticated solution. Here the applications share data in a common database. Messaging goes further. It exchanges data and also invokes behavior through a common messaging system.

**The schema is the hard part.** The schema is the structure of the shared data. One schema must meet the needs of many applications. Designing it is a very difficult exercise. There are also political difficulties. Conflicts between departments make agreeing on a shared schema worse.

**Coupling.** Martin Fowler warns that the database becomes a point of coupling between all applications that access it. The coupling is deep. It makes changing those applications riskier. See Coupling and Cohesion for background.

**Microservices.** Microservices take the opposite view. Each service manages its own database. Enterprises, by contrast, often prefer a single database across applications. See Microservices Architecture.

## Example

A company has an order application, a billing application and a reporting tool. All three keep customer data in one common database. When a clerk updates an address in the order application, billing and reporting read the same data. If the team wants to restructure the customer data, it must involve all three applications.

## Trade-offs

**Benefits**
- Applications on different languages and platforms can share information rapidly and consistently.

**Costs**
- Designing one schema for many applications is very hard.
- Agreeing on it can be political, especially when departments conflict.
- All applications are deeply coupled through the database, so changing them is riskier.
