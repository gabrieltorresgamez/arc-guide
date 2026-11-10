---
title: Synchronous vs. Asynchronous Communication
slug: synchronous-vs-asynchronous-communication
category: integration
kind: concept
summary: A synchronous call makes the caller wait for the answer. An asynchronous call lets the caller
  move on. The choice shapes how failures spread and how replies are matched to requests.
arc42:
- 4
- 6
- 8
- 9
step: s08-integration-data
related:
- synchronous-vs-asynchronous-connector
- request-reply
- correlation-identifier
- messaging
- circuit-breaker
- remote-procedure-call
- loose-coupling
- availability
checks:
- The document states how each remote call handles an unavailable supplier.
- Long chains of synchronous calls between services are identified, with a stated way to handle their
  combined downtime.
- Resilience patterns such as Circuit Breaker, Bulkhead or Timeout are named where services communicate.
- Where Request-Reply messaging is used, the document says how replies are matched to requests, for example
  with a Correlation Identifier.
sources:
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html
  title: Request-Reply - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CorrelationIdentifier.html
  title: Correlation Identifier - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Synchronous call: the caller waits. Asynchronous call: the caller continues and the reply
    is matched later.'
review:
  status: generated
  flags: []
---

## Explanation

A **synchronous** call means the caller sends a request and waits for the reply. An **asynchronous** call means the caller sends the request and carries on. Any reply comes later.

**Synchronous calls and failure**

Any remote call can fail, because the service on the other end may be unavailable. Callers must handle that failure gracefully.

Chained calls make this worse. When services make several synchronous calls to each other, the downtime of the system becomes the product of the downtimes of the individual components. There are two ways out: make the calls asynchronous, or manage the downtime. Circuit Breaker, Bulkhead and Timeout are patterns that, used together, matter for applications that communicate with each other.

Cross-service transactions add another problem. They impose significant temporal coupling, which is problematic across several services.

**Asynchronous communication**

A common asynchronous style is messaging over a lightweight message bus. It is an alternative to request/response protocols.

Asynchronous communication can still produce an answer. Request-Reply sends a pair of messages, each on its own channel. The requestor must then match each reply to its request. A Correlation Identifier does this. With the Asynchronous Callback approach to receiving replies, several open requests can share one reply channel.

## Example

An online shop checks stock, takes payment and books shipping. In a synchronous design, the order service calls each one and waits. If the shipping service is down, the order fails or hangs. In an asynchronous design, the order service posts a message and moves on. The reply carries a correlation identifier copied from the request, so the order service knows which request it answers.

## Trade-offs

Synchronous calls expose the caller to the supplier's downtime, and chains of them multiply that downtime.

Going asynchronous is one way out of the multiplied downtime. In return, the design needs extra machinery. Replies must be matched to requests, for example with a Correlation Identifier and separate reply channels.
