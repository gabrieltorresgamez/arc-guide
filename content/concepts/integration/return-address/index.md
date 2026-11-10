---
title: Return Address
slug: return-address
category: integration
kind: pattern
summary: A Return Address is a reply destination carried inside the request message. The replier reads
  it and sends the answer there, so it never needs to know in advance who is asking.
arc42:
- 6
- 8
step: s08-integration-data
related:
- request-reply
- correlation-identifier
- message-channel
- point-to-point-channel
- publish-subscribe-channel
- messaging
- remote-procedure-call
- message-structure
checks:
- Request messages carry the reply destination in a header, not in the business data.
- Replies are matched to requests with a correlation identifier alongside the return address.
- Requesters discard replies whose correlation ID they do not recognize.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ReturnAddress.html
  title: Return Address - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html
  title: Request-Reply - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
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
  caption: The replier sends its answer to the channel named in the request header.
review:
  status: generated
  flags: []
---

## Explanation

A service that receives a request must answer somewhere. Without help, it does not know where. Return Address solves this: the requester puts the reply destination into the request itself.

The address travels in the message header, not in the data. It describes where the reply goes, not what the message says. The replier reads the header and sends its answer to that channel. It needs no list of reply destinations in advance.

This pattern supports Request-Reply (see the article on that pattern). Request-Reply sends a pair of messages, each on its own channel. The request channel can be point-to-point or publish-subscribe.

A related pattern is Correlation Identifier. This is a unique ID that tells the requester which request a reply belongs to. The address says where the reply goes. The identifier says which request it answers.

Real products use the same idea. In RabbitMQ RPC (remote procedure call over messaging), the client sends the name of a callback queue along with its request. The client creates its own exclusive callback queue when it starts.

The `correlation_id` property pairs with `reply_to`. If a client sees an unknown `correlation_id`, it can safely discard the message.

## Example

An order service receives price requests from many client applications. Each client creates its own reply queue at startup. Each client sends a request with its queue name in the header and a unique ID. The order service reads the header and sends the answer to that queue, copying the ID into the reply. The client checks the ID. If it does not know the ID, it discards the message.

## Trade-offs

The sources describe the mechanics of Return Address but do not discuss its trade-offs, such as how to guard against untrusted addresses.
