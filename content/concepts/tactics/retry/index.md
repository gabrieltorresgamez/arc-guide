---
title: Retry
slug: retry
category: tactics
kind: tactic
summary: Retry repeats a failed call after a delay, assuming the fault is temporary. It needs a cap on
  attempts, growing delays, and care with operations that are unsafe to run twice.
arc42:
- 8
- 6
- 4
step: s07-solution-strategy
related:
- circuit-breaker
- availability-tactics-fault-recovery
- availability-tactic
- idempotent-receiver
- exception-handling
- fault
- timeout-based-delivery
- availability
checks:
- The retry policy sets a maximum number of attempts and states what happens after the last one.
- Delays between retries grow (incrementally or exponentially) and are spread across callers.
- Operations that are retried are idempotent, or the document explains how duplicate execution is handled.
- Retries are applied at one chosen layer, not independently at every layer of a call chain.
- A circuit breaker or retry limit protects a busy service from retry load.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/retry
  title: Retry pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter
  title: Timeouts, retries, and backoff with jitter | AWS Builder Center
  site: builder.aws.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: A retry loop with a limit and growing delays
review:
  status: generated
  flags: []
---

## Explanation

Retry is an availability tactic (see Availability Tactic). It assumes the fault is transient. Such faults tend to fix themselves, so repeating the action after a suitable delay will likely work.

**Set a limit.** Retries stop after a fixed number of attempts. After that, the application treats the problem as an exception and handles it. If the fault looks permanent, or repeating is unlikely to help, cancel the operation and report the exception right away. Policies can also differ by exception type. Some exceptions signal a quick fix. Others signal a longer outage.

**Space out the attempts.** The delay between retries can grow step by step or exponentially. With exponential backoff, the wait grows exponentially after every attempt. Jitter adds randomness to that wait. This spreads retries from many callers across time, so they do not all hit a busy service together.

**Protect the service you call.** Retries add load. An aggressive policy, with short delays and many attempts, can push an already busy service further down. After many failures, a circuit breaker should block further requests (see Circuit Breaker). A token bucket is another guard. Calls may retry while tokens remain. Once the tokens run out, retries continue only at a fixed rate.

**Avoid stacking layers.** If every layer of a call chain retries on its own, the attempts multiply. One source describes a 243x increase in database load, which makes recovery unlikely. A better design lets lower-level tasks fail fast. The higher-level task then applies the retry policy. Nested retries also add long delays.

**Check that the operation is safe.** An operation is idempotent if running it more than once has the same effect as running it once. Such operations are inherently safe to retry. Others may run more than once and cause unintended side effects, for example when only the response was lost.

**Log with care.** Record early failed attempts as informational entries. Record only the final failure as an error. This avoids flooding alerts while keeping the history visible.

## Example

A web shop calls a payment-status service, and the call fails. The shop waits one second and tries again. It waits two seconds after the next failure, then four, each time with a small random extra delay. After five attempts it stops and shows an error. The status check only reads data, so repeating it is safe. A "charge the card" call would need extra protection before it could be retried.

## Trade-offs

Retry can hide short outages from users, but it costs extra load and extra waiting. Too many or too fast retries can make an overloaded service worse. Retries at several layers multiply. Operations that are not idempotent can run twice with side effects. Long delays also slow the final answer when the fault turns out to be permanent. Pair retry with a limit, backoff, and a circuit breaker.
