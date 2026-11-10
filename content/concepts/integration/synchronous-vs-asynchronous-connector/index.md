---
title: Synchronous vs Asynchronous Connector
slug: synchronous-vs-asynchronous-connector
category: integration
kind: concept
summary: A synchronous connector needs sender and receiver to be up at the same time. An asynchronous
  connector, such as a queue, lets them work at different times, which limits how failures spread.
arc42:
- 4
- 5
- 6
- 8
step: s08-integration-data
related:
- synchronous-vs-asynchronous-communication
- software-connector
- circuit-breaker
- retry
- message-channel
- dead-letter-channel
- availability
- request-reply
checks:
- Each synchronous call chain is identified, and its composite availability is calculated as the product
  of the components' availabilities.
- Synchronous remote calls have timeouts and, where useful, retries or a circuit breaker.
- Where a sender must keep working while the receiver is down, a queue or similar asynchronous connector
  is used.
- For queue-based connectors, the document addresses duplicate delivery, ordering and queue growth.
- Where a reply is needed over a queue, the reply mechanism is described.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Messaging.html
  title: Messaging - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling
  title: Queue-Based Load Leveling Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/CircuitBreaker.html
  title: Circuit Breaker
  site: martinfowler.com
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
  title: Circuit Breaker Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics
  title: Architecture strategies for defining reliability targets - Microsoft Azure Well-Architected Framework
    | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A synchronous call needs both parties up together. A queue lets each party talk only to the
    queue.
review:
  status: generated
  flags: []
---

## Explanation

**Synchronous connectors.** The sender calls the receiver and waits. Both must be up and ready at the same moment. Remote calls can fail or hang until a timeout. While callers wait on an unresponsive service, they hold threads, memory and connections. Many waiting callers can use up these resources. Then unrelated parts of the system that share them can fail too. Failures cascade across systems this way.

**Chains add risk.** The combined availability of chained components is the product of their individual values. Each new dependency therefore lowers the total. See the Availability article for the term.

**Asynchronous connectors.** A queue sits between sender and receiver. The sender posts a message and moves on. The queue stores the message until the receiver picks it up. Neither side needs to be up at the same time as the other. The sender is not delayed when the receiver is down. It can keep posting messages.

**Protecting synchronous calls.** If you keep a synchronous connector, you can add safeguards:

- A timeout stops a caller from waiting forever. Alone, it still lets blocked requests hold resources.
- A retry repeats an operation. It suits temporary faults.
- A circuit breaker trips once failures pass a threshold. After that, calls return an error at once without making the remote call. It prevents repeating operations likely to fail, and it can be combined with retry.

Message-driven designs often need a circuit breaker less. They have built-in failure isolation, and they can route failed messages to a dead letter queue.

## Example

An online shop takes an order and must send a confirmation email. In a synchronous design, the checkout calls the email service and waits. If the email service hangs, checkout requests pile up and the shop slows down. In an asynchronous design, checkout drops a message on a queue and finishes. The email service reads the message when it is back up.

## Trade-offs

Queues are one-way. If the sender needs an answer, you must build an extra reply mechanism. Queues might not be suitable when the caller requires a low-latency, synchronous response.

Delivery has costs too. At-least-once delivery means a message can arrive more than once, so receivers must tolerate duplicates. Order is not guaranteed when several receivers work in parallel. When messages arrive faster than receivers process them, the queue grows and latency rises.
