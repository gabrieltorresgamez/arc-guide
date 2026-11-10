---
title: Correlation Identifier
slug: correlation-identifier
category: integration
kind: pattern
summary: A Correlation Identifier lets a requester match a reply to the request that caused it. The replier
  copies the request's unique ID into a correlation ID field of the reply.
arc42:
- 6
- 8
step: s08-integration-data
related:
- request-reply
- return-address
- messaging
- message-structure
- message-channel
- synchronous-vs-asynchronous-communication
checks:
- The design states that each request carries a unique ID.
- The design states that the replier copies the request ID into the correlation ID field of the reply.
- Where requests expect replies on a callback queue, the document names that queue as the return address
  sent with the request.
- The design says what a requester does with a reply whose correlation ID it does not recognize.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CorrelationIdentifier.html
  title: Correlation Identifier - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.rabbitmq.com/tutorials/tutorial-six-python
  title: RabbitMQ tutorial - Remote procedure call (RPC) | RabbitMQ
  site: rabbitmq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Two requests in flight; each reply carries the ID of its request.
review:
  status: generated
  flags: []
---

## Explanation

A requester sends a request and later receives a reply. The question is simple: which request does this reply belong to? The Correlation Identifier pattern answers it.

**How it works**

- Every request carries an ID that identifies that request uniquely.
- The replier reads this ID from the request.
- The replier stores it in a correlation ID field of the reply.
- The reply therefore holds a token with the same value as the request ID.

The requester reads the correlation ID from the reply. It can then tell which of its requests the reply answers.

**Working with a callback queue**

A request also needs to say where the reply should go. In RabbitMQ's remote-call example, the client sends the name of a callback queue along with the request. The server uses it to know where to reply. The queue name tells the server where to reply. The correlation ID tells the client which request the reply answers.

**Unknown replies**

In the same RabbitMQ example, a client may see a reply with a correlation ID it does not know. It can safely discard that message. The reply does not belong to this client's requests.

For the wider request and reply exchange, see the Request-Reply article.

## Example

A web shop sends two "check stock" requests to a warehouse service, one for shoes and one for hats. Request A has ID 101 and request B has ID 102. The warehouse sends two replies. Each reply carries the matching ID as its correlation ID. The shop reads 102 on one reply and knows it answers the hat request. A reply carrying ID 555 is unknown to the shop, so the shop discards it.
