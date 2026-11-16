---
title: Synchronous vs. Asynchronous Communication
slug: synchronous-vs-asynchronous-communication
order: 80
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
- enterprise-integration-patterns
- messaging
- remote-procedure-call
- coupling-and-cohesion
- reliability
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

**Asynchronous communication**

A common asynchronous style is messaging over a lightweight message bus. It is an alternative to request/response protocols.

Asynchronous communication can still produce an answer. Request-Reply sends a pair of messages, each on its own channel. The requestor must then match each reply to its request. A Correlation Identifier does this. With the Asynchronous Callback approach to receiving replies, several open requests can share one reply channel.

## Example

An online shop checks stock, takes payment and books shipping. In a synchronous design, the order service calls each one and waits. If the shipping service is down, the order fails or hangs. In an asynchronous design, the order service posts a message and moves on. The reply carries a correlation identifier copied from the request, so the order service knows which request it answers.

## Trade-offs

In return, the design needs extra machinery. Replies must be matched to requests, for example with a Correlation Identifier and separate reply channels.
