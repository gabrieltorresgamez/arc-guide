---
title: Request-Reply
slug: request-reply
category: integration
kind: pattern
summary: Request-Reply lets a requestor send a message on one channel and get the answer on another. A
  correlation ID or a return address tells the requestor which reply belongs to which request.
arc42:
- 6
- 8
step: s08-integration-data
related:
- correlation-identifier
- return-address
- message-channel
- messaging
- point-to-point-channel
- publish-subscribe-channel
- synchronous-vs-asynchronous-communication
- bpmn-event
checks:
- The reply channel is point-to-point, so replies reach only the requestor.
- Replies carry a correlation ID equal to the ID of the request they answer.
- Requests carry a return address in the message header, so the replier does not need to know it in advance.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html
  title: Request-Reply - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CorrelationIdentifier.html
  title: Correlation Identifier - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ReturnAddress.html
  title: Return Address - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/message-events/
  title: Message events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A request and its reply travel on separate channels, matched by the correlation ID.
review:
  status: generated
  flags: []
---

## Explanation

Request-Reply is a messaging pattern with two channels. The requestor sends a request on the request channel. The replier sends its answer back on a separate reply channel. (See Message Channel and Messaging for the basics.)

The two channels often differ in kind. The request channel can be point-to-point (one receiver gets each message) or publish-subscribe (many receivers get a copy). The reply channel is almost always point-to-point. That way the reply goes only to the requestor.

Two questions come up in practice.

**Which reply answers which request?** A requestor may have several requests open at once. A Correlation Identifier solves this. It is a token in the reply with the same value as the request's ID. The replier takes the ID out of the request and puts it into the reply as the correlation ID. The requestor then matches the two.

**Where should the reply go?** The request can carry a Return Address. It tells the replier where to send the reply, so the replier does not need to know the address in advance. The address sits in the message header because it is not part of the transmitted data.

In BPMN (a process modeling notation), a message catch event makes a process wait until a matching message arrives. Messages in BPMN go from one sender to one recipient.

## Example

An online shop sends a "create order" request to an order service. The request carries an ID and a return address in its header. The order service handles it. It copies the ID into the correlation ID of its reply and sends the reply to the return address. The shop has several orders open at once. It uses the correlation ID to pair each reply with the right order.
