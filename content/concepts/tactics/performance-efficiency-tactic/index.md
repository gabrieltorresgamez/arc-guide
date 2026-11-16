---
title: Performance Efficiency Tactic
slug: performance-efficiency-tactic
order: 10
category: tactics
kind: tactic
summary: 'Performance efficiency tactics are design decisions that help a system answer requests fast enough. They
  work in two ways: limiting the demand placed on the system, or managing the available resources better.'
arc42:
- 4
- 8
- 9
- 10
step: s07-solution-strategy
related:
- architectural-tactic
- performance-efficiency
- choosing-and-applying-tactics
- tactic-trade-off-balancing
- flexibility
- reliability-tactic
checks:
- Performance decisions are identified as either controlling resource demand or managing resources.
- Where events differ in importance, the document describes how they are prioritized.
- Queue sizes and execution time per event are bounded, or the document explains why not.
- Use of caching or data replication is stated where copies of data are kept.
- Contended resources have a stated scheduling approach.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=3
  title: 3.3 Design Concepts to Support Performance | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://investigadores.anid.cl/en/public_search/work?id=725771
  title: PDI - Resultado de Búsqueda
  site: investigadores.anid.cl
  accessed: '2026-11-08'
- url: https://quality.arc42.org/approaches/caching
  title: "Caching | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/content-delivery-network
  title: "Content Delivery Network (CDN) | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/database-sharding
  title: "Database Sharding | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/computational-overhead-reduction
  title: "Computational Overhead Reduction | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/rate-limiting
  title: "Rate Limiting | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/backpressure-propagation
  title: "Backpressure Propagation | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams:
- file: diagram-1.mmd
  caption: The two categories of performance tactics and example tactics in each.
review:
  status: generated
  flags: []
---

## Explanation

A performance tactic is a design decision that helps a system meet its timing goals. It is one kind of Architectural Tactic. That article explains the general idea.

Performance tactics fall into two major categories:

- **Control resource demand.** Reduce the work the system has to do.
- **Manage resources.** Add resources or use them in ways that improve performance.

**Control resource demand**

These tactics limit how much load arrives or how much work each arrival causes:

- Manage work requests. This is one way to limit demand.
- Prioritize events. If events are not equally important, set up a priority scheme.
- Bound execution time. Set a limit on how much time the system spends responding to one event.

**Manage resources**

These tactics add resources or make better use of them:

- Introduce concurrency. Processing requests in parallel reduces blocked time.
- Maintain multiple copies of data. Two common ways are replication and caching.
- Bound queue sizes. This caps the number of queued arrivals. That in turn caps the resources used to process them.
- Schedule resources. When several requests contend for the same resource, the resource should be scheduled.

Tactics help an architect reason about a quality attribute such as performance. The article Choosing and Applying Tactics covers that step.

**Further approaches in the arc42 quality model.** The arc42 quality model has more approach pages on related ideas: [Caching](https://quality.arc42.org/approaches/caching), [Content Delivery Network (CDN)](https://quality.arc42.org/approaches/content-delivery-network), [Database Sharding](https://quality.arc42.org/approaches/database-sharding), [Computational Overhead Reduction](https://quality.arc42.org/approaches/computational-overhead-reduction), [Rate Limiting](https://quality.arc42.org/approaches/rate-limiting), [Backpressure Propagation](https://quality.arc42.org/approaches/backpressure-propagation).

## Example

An online ticket shop expects a rush when a popular event goes on sale. The team keeps copies of the event listings in a cache, so most visitors do not hit the database. They process several purchase requests in parallel. They cap the waiting line so it cannot grow without limit. They also set a time limit per request, so one slow request cannot hold up the rest.

## Trade-offs

One broader finding applies: tactics in general have been extended to many quality attributes since 2003. A mapping study found little rigor in how they are defined and little industrial evidence for their use. Treat tactic lists as guidance, and check that a chosen tactic really helps in your case.
