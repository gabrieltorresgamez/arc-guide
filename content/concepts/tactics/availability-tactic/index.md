---
title: Availability Tactic
slug: availability-tactic
category: tactics
kind: tactic
summary: 'Availability tactics are design measures that keep faults from turning into failures. They fall
  into three groups: detecting faults, recovering from faults, and preventing faults.'
arc42:
- 4
- 8
- 10
step: s07-solution-strategy
related:
- availability-tactics-fault-detection
- availability-tactics-fault-recovery
- availability-tactics-fault-prevention
- heartbeat
- voting
- retry
- graceful-degradation
- circuit-breaker
checks:
- The document names which availability tactics it uses and groups them as detecting, recovering from
  or preventing faults.
- Calls between services use timeouts, so clients do not block forever.
- Where a remote call may fail, a fallback such as cached data or a default value is defined.
- Calls to unreliable dependencies are protected by a circuit breaker that fails fast after a failure
  threshold.
- The document states which critical functions stay running when components fail, and which are dropped.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/library/realizing-and-refining-architectural-tactics-availability/
  title: 'Realizing and Refining Architectural Tactics: Availability | CMU Software Engineering Institute'
  site: sei.cmu.edu
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/partial-failure-strategies
  title: Strategies for handling partial failure - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/CircuitBreaker.html
  title: Circuit Breaker
  site: martinfowler.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: The three categories of availability tactics, with examples.
review:
  status: generated
  flags: []
---

## Explanation

A **fault** is a potential cause of a failure. A **failure** happens when the system no longer delivers service that matches its specification (the description of what it must do). Availability tactics work on faults, so that faults do not become failures.

The catalog has three categories:

- **Detect faults.** Find out that something is wrong.
- **Recover from faults.** Get back to correct service.
- **Prevent faults.** Act before a fault can cause harm.

**Detection examples**

- *Heartbeat*: a monitor and a watched process exchange messages at regular intervals. See the article Heartbeat.
- *Voting*: replicated components do the same work, and the system checks that their results agree. Triple modular redundancy is one case. See the article Voting.

**Recovery examples**

- *Rollback*: go back to a state known to be good.
- *Retry*: repeat an operation. This can succeed when the failure is transient, meaning it passes on its own. See the article Retry.
- *Graceful degradation*: keep the most critical functions running during component failures by dropping less critical ones. See the article Graceful Degradation.

**Prevention example**

- *Removal from service*: take a component out of service for a while to reduce the chance of failures.

**Microservice tactics.** Microsoft's guidance for microservices lists these measures against partial failure:

- asynchronous messaging
- retries with backoff
- timeouts
- circuit breakers
- fallbacks
- bulkhead limits

A *timeout* keeps a client from blocking forever and tying up resources. A *fallback* lets the client return something else, such as cached data or a default value, when a request fails. A *circuit breaker* wraps a protected call and watches it for failures. After a threshold, it trips, and later calls fail fast without invoking the protected call. See the article Circuit Breaker.

The catalog has been used in academia and industry for several years. That use motivated a refinement of it.

## Example

An online shop shows product recommendations from a separate service. A heartbeat tells the shop that the recommendation service has stopped. A timeout stops product pages from hanging while they wait. A circuit breaker then trips, and the shop returns a default list of popular items as a fallback. The checkout, the most critical function, keeps working. Rollback and retry would apply to other parts of the shop, for example when an order update fails halfway.

## Trade-offs

The catalog is a set of options grouped by purpose. Each tactic addresses one part of the problem: detecting, recovering or preventing.
