---
title: Circuit Breaker
slug: circuit-breaker
category: tactics
kind: pattern
summary: A circuit breaker sits between a caller and a service it depends on. After repeated failures
  it fails calls at once instead of waiting. It later tests the service and resumes when the service recovers.
arc42:
- 8
- 6
- 10
step: s07-solution-strategy
related:
- retry
- availability-tactic
- graceful-degradation
- fault-tolerance
- ping-echo
- heartbeat
- exception-handling
- availability
checks:
- The document states the failure threshold and time period that trip each circuit breaker.
- 'The document states how a tripped breaker recovers: a time-out, a health-check probe, or a manual reset.'
- Callers define what they do when the breaker rejects a call, such as degrading functionality or informing
  the user.
- Retry logic stops when the breaker signals a non-transient fault.
- Breaker state changes are logged and exposed for monitoring.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
  title: Circuit Breaker Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://martinfowler.com/bliki/CircuitBreaker.html
  title: Circuit Breaker
  site: martinfowler.com
  accessed: '2026-11-08'
- url: https://resilience4j.readme.io/docs/circuitbreaker
  title: CircuitBreaker
  site: resilience4j.readme.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: The three states of a circuit breaker and the transitions between them.
review:
  status: generated
  flags: []
---

## Explanation

A circuit breaker is a proxy: a stand-in between a caller and the service it calls. It can be implemented as a state machine with these states.

- **Closed:** Calls pass through. The breaker counts recent failures. If they exceed a threshold within a time period, it switches to Open and starts a timer.
- **Open:** Calls fail immediately with an exception.
- **Half-Open:** The timer has expired. A limited number of trial calls pass. If they succeed, the breaker assumes the fault is fixed, resets its counter and returns to Closed. If they fail, it returns to Open and restarts the timer.

Half-Open also protects a recovering service from a sudden flood of requests.

Instead of a timer, an open breaker can probe the service with a ping or a health-check operation. The result decides when to go Half-Open. Operators should also be able to trip or reset a breaker by hand.

**Why it matters.** Blocked requests that wait for time-outs hold threads, memory and database connections. Unrelated parts of the system that need the same resources can then fail too. Failing immediately avoids this.

**What callers do.** Callers must handle the breaker's exception. They can reduce functionality for a while, call an alternative operation to get the same data, or tell the user to try again later.

**Retry.** A circuit breaker and a retry mechanism (see Retry) serve different purposes, but you can combine them. The retry logic must stop when the breaker signals that the fault is not transient.

**Monitoring.** Log every state change. Breakers should also expose their state for deeper monitoring.

**In practice.** Resilience4j implements the circuit breaker as a state machine with CLOSED, OPEN and HALF_OPEN states. It lets you configure how long the breaker waits in Open before moving to half-open.

## Example

A web shop calls a separate recommendation service. That service starts failing. After several failed calls in a short period, the breaker opens. Product pages now skip the recommendations block at once instead of hanging. When the timer expires, the breaker lets a few trial calls through. If they succeed, recommendations return.

## Trade-offs

The wait time in Open needs tuning. If the breaker stays open too long, it raises errors even after the fault is fixed. If it moves to Half-Open too quickly, it keeps flipping between states, and response times suffer.

Callers also take on work. Every caller must decide what to do when the breaker rejects a call.
