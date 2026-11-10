---
title: Fault Tolerance
slug: fault-tolerance
category: quality-attributes
kind: quality-attribute
summary: Fault tolerance is how well a system keeps working as intended while hardware or software faults
  are present. It is separate from availability and recoverability, and it relies on detecting, recovering
  from and containing faults.
arc42:
- 8
- 10
- 4
step: s04-quality-requirements
related:
- availability
- recoverability
- circuit-breaker
- retry
- graceful-degradation
- heartbeat
- ping-echo
- redundant-spare
checks:
- The document states fault tolerance as its own quality requirement, separate from availability and recoverability.
- Retries are limited to idempotent operations.
- Calls to unreliable dependencies are protected by a circuit breaker or bulkhead.
- The document says how the system degrades gracefully when a component fails.
- Chaos experiments name a specific fault and a clear hypothesis.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=1
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: Tactics and Patterns for Software Robustness | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/retry
  title: Retry pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://martinfowler.com/bliki/CircuitBreaker.html
  title: Circuit Breaker
  site: martinfowler.com
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
  title: Circuit Breaker Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead
  title: Bulkhead Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/reliability/reliability-test
  title: Architecture strategies for designing a reliability testing strategy - Microsoft Azure Well-Architected
    Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A circuit breaker stops calls to a failing service and returns a reduced-mode response.
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC 25010 defines fault tolerance as the degree to which a system keeps operating as intended despite hardware or software faults (see ISO/IEC 25010 Product Quality Model). The aim is that one broken part does not break the whole service.

Two neighboring qualities are separate in the same model. Availability is how far the system is operational and accessible when someone needs it. Recoverability is the ability to recover the data directly affected after an interruption or failure. Fault tolerance is about continuing to work while the fault is present.

Teams combine several tactics. A tactic is a proven design move (see Architectural Tactic).

**Detecting faults**
- Heartbeat: nodes exchange periodic messages, so a missing message signals trouble.
- Ping/echo: one node sends an asynchronous request and expects a reply from another node.
- Exception detection: the system notices a condition that alters normal execution. The exception must then be handled.

**Redundancy and recovery**
- Active redundancy (hot spare): two or more elements process the same inputs in parallel.
- Passive (warm) spare: a standby that receives periodic state updates from the active nodes.
- Cold spare: a standby that takes over without the failed node's state.
- Rollback: return the system to a previous known good state.
- Retry: repeat an action after a suitable delay. This suits transient faults, which usually correct themselves. It is only safe for idempotent operations. Otherwise a repeat may run the operation twice, with unintended side effects.

**Containing faults**
- Circuit breaker: wraps a protected call. After a failure threshold, it rejects further calls without making them. This prevents cascading failure. Retry expects eventual success, while the breaker stops operations likely to fail.
- Bulkhead: isolates parts of an application into pools, so one failing part leaves the others working.

Graceful degradation means a failed component leads to reduced-mode operation, not complete failure. A circuit breaker can trigger it.

To test fault tolerance, run chaos experiments. Each one targets specific faults and has a clear hypothesis, derived from failure mode analysis. Also test that the workload degrades gracefully.

## Example

An online shop calls a separate recommendation service. That service starts failing. The shop retries a read-only request once after a short delay. After repeated failures, a circuit breaker opens and the shop stops calling the service. Product pages still load, without recommendations. Checkout runs in its own pool, so it is not slowed down. The shop works in a reduced mode instead of failing completely.

## Trade-offs

There are some limits. Retry is unsafe for operations that are not idempotent. Retry and circuit breaker serve different purposes, but they can be combined by retrying an operation through a circuit breaker. Choose each tactic for the fault type you expect. Spares also differ in how much state they keep. A cold spare takes over without the failed node's state, while a passive spare receives periodic updates. Compare such options against other qualities (see Quality Attribute Trade-off).
