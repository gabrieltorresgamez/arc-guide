---
title: Connect or Disconnect
slug: connect-or-disconnect
category: principles
kind: principle
summary: Connecting components creates dependencies between them. Disconnecting them avoids that but can
  hide dependencies. Good design keeps few, narrow, explicit dependencies, and the right amount depends
  on how much control you have.
arc42:
- 4
- 5
- 8
- 9
step: s08-integration-data
related:
- coupling-and-cohesion
- loose-coupling
- reduce-coupling
- broker-pattern
- messaging
- modifiability
- software-connector
- architectural-trade-off-thinking
checks:
- Dependencies between building blocks are explicit and kept narrow, not hidden.
- Shared data formats and message-order assumptions are documented as dependencies, even where the systems
  look decoupled.
- Where an intermediary (broker, bus, mediator) is used, its added latency and its role as a possible
  bottleneck are assessed.
- The chosen level of coupling is justified by the control the team has over the connected systems.
sources:
- url: https://www.enterpriseintegrationpatterns.com/ramblings/coupling_facets.html
  title: The Many Facets of Coupling - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/approaches/reduce-coupling
  title: Reduce Coupling | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://connascence.io/
  title: connascence.io
  site: connascence.io
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Whenever two parts of a system might interact, you choose between connecting and disconnecting them.

Coupling describes whether a change in one connected system affects another. If a change in System A affects System B, they are coupled. If each can change on its own, they vary independently.

**Coupling is not on or off.** It comes in degrees. It also has many dimensions: technology, location, data format, message order and time. Two systems can be loose in one dimension and tight in another.

**The right amount depends on control.** How much coupling is appropriate depends on how much control you have over the systems at each end.

**Loose coupling has benefits.** Parts can change independently, and operations are more resilient. But it is not free.

**Disconnecting does not remove every dependency.** Hidden (implicit) coupling can remain. Two systems may look separate but still share a data format. A change to that format then affects both.

**Aim for fewer dependencies, not zero.** A system with no dependencies does nothing. The goal is fewer, narrower and explicit dependencies. Narrow, explicit interfaces make a split into modules real instead of nominal. They also keep change local.

**Types of coupling have names.** Connascence is a catalog of coupling types. It splits them into static and dynamic forms, such as Timing and Execution. It also says that coupled elements are better placed close together in the code than far apart.

See also Coupling and Cohesion, Loose Coupling and Reduce Coupling.

## Example

A web shop has an ordering part and a shipping part. In one design, ordering calls shipping directly. If shipping changes its input format, ordering breaks. That is a connection with an explicit dependency.

In another design, ordering drops a message into a broker (an intermediary that passes messages along), and shipping picks it up later. The two no longer call each other. But both still read the same message format. If that format changes, both break. The dependency moved. It did not vanish.

## Trade-offs

Decoupling through an intermediary such as a broker, message bus or mediator has costs.

The intermediary can become a new coupling point. Every path crosses it, so it can turn into a bottleneck.

Loose coupling brings independent change and resilience, but it has a price. Judge each connection by how much control you have over both ends and which dimensions of coupling matter there.
