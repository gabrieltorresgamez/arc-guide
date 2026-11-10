---
title: Connectors and Distribution
slug: connectors-and-distribution
category: fundamentals
kind: concept
summary: 'A monolith can only be copied and run as several identical instances. Splitting a system into
  separate processes adds a new risk: a call to another process may be slow or fail while the rest keeps
  running.'
arc42:
- 5
- 7
- 8
- 11
step: s08-integration-data
related:
- software-connector
- distribution-view
- remote-procedure-call
- synchronous-vs-asynchronous-communication
- load-balancer
- fault-tolerance
- microservices-architecture
- circuit-breaker
checks:
- Synchronous remote calls have timeouts, so a slow service cannot block all threads of its caller.
- The document states how partial failure of a service or server is handled.
- Communication between internal services is asynchronous where possible, or the document explains why
  not.
- The availability of many chained dependencies is considered together, not one by one.
sources:
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/handle-partial-failure
  title: Handling partial failure - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/distributed-objects-microservices.html
  title: Microservices and the First Law of Distributed Objects
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How a slow remote call without a timeout can turn a partial failure into a global outage.
review:
  status: generated
  flags: []
---

## Explanation

A monolith is built and deployed as a single unit. You can run many instances of it behind a load balancer (see Load Balancer). That is horizontal scaling by replication.

Distribution is the other route. You split the system into separate processes, such as clients and services, that talk over a network. Each call now crosses a process boundary.

That boundary has a cost. Fowler's First Law of Distributed Object Design says not to distribute your objects. It targets the idea of distributed objects, which can be used in-process or remotely alike. The reason is that a remote call differs from an in-process call, and an object boundary cannot hide the difference.

Partial failure is an ever-present risk in distributed systems. A single service, container, virtual machine, or server can crash or become unreachable. A service may also answer late because it is overloaded or the network has problems.

A slow remote call can block the thread that made it. If a synchronous call has no timeout, blocked threads pile up. Eventually the application runs out of threads. A local problem then becomes a global outage.

Intermittent failure is guaranteed in a distributed, cloud-based system, even when every dependency has excellent availability. Without fault tolerance, small downtimes can be amplified. For example, without fault tolerance, 50 dependencies at 99.99% availability would result in several hours of downtime each month.

Fault tolerance therefore has to be designed in. One recommended step is asynchronous communication between internal services. It is meant to minimize this problem (see Synchronous vs. Asynchronous Communication).

## Example

An online shop runs as one program. When traffic grows, the team starts three identical copies behind a load balancer. Later the team splits out a payment service, and the shop now calls it over the network. One day payment slows down. Checkout requests wait for it and their threads stay blocked. Without timeouts, enough blocked threads can leave the whole shop unresponsive, not just checkout.

## Trade-offs

Scaling a monolith means scaling the entire application as one block. Splitting into separate processes gives more freedom, but every remote call can be slow, can fail, or can block callers. Long chains of synchronous calls can amplify these failures. Asynchronous communication is recommended to minimize the problem, but Fowler notes that asynchrony is itself a complexity booster.
