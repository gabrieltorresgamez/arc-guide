---
title: Message Structure
slug: message-structure
category: integration
kind: concept
summary: A message has a body that carries the data and a header that carries information for the messaging
  system. Header fields such as a correlation ID and a return address let a reply find its way back to
  the right request.
arc42:
- 8
- 6
- 5
step: s08-integration-data
related:
- correlation-identifier
- return-address
- envelope-wrapper
- routing-slip
- message-sequence
- messaging
- request-reply
- format-identifier
checks:
- Request messages that expect a reply carry a unique request ID, and replies copy it into a correlation
  ID.
- Request messages carry a Return Address in the header rather than in the application data.
- The document states where an expiration time applies and that consumers ignore expired messages.
- Where large payloads are split into smaller messages, the document describes sequencing, correlation
  and reassembly.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Message.html
  title: Message - Enterprise Integration Patterns
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
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/EnvelopeWrapper.html
  title: Envelope Wrapper - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageExpiration.html
  title: Message Expiration - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RoutingTable.html
  title: Routing Slip - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check
  title: Claim Check pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A request and its reply: the replier copies the request ID into the correlation ID and sends
    the reply to the return address.'
review:
  status: generated
  flags: []
---

## Explanation

A message sent through a messaging system has two parts: a header and a body.

**Body.** The body holds the data you want to send. The messaging system generally ignores it and passes it along unchanged.

**Header.** The header holds information that the messaging system itself uses. It describes the data being sent.

**Header fields that support replies.** Some fields make two-way conversations possible:

- **Request ID.** A token that uniquely identifies a request.
- **Correlation Identifier.** The replier copies the request ID into the reply. The original sender can then match the reply to its request. See the article Correlation Identifier.
- **Return Address.** The request carries this field to tell the replier where to send the reply. It sits in the header because it is metadata, not application data. See the article Return Address.

**Expiration.** A Message Expiration sets a time limit on how long a message stays viable. Consumers ignore messages that have expired.

**Routing.** A Routing Slip is attached to a message. It lists the sequence of processing steps, so the message can pass through a series of components. See the article Routing Slip.

**Envelope.** Most messaging systems split message data into a header and a body. An Envelope Wrapper builds on this. It wraps the application data in an envelope that the messaging infrastructure accepts. The message is unwrapped at the destination. See the article Envelope Wrapper.

**Sequences.** A large payload can be divided into a sequence of smaller messages. This then requires sequencing, correlation and reassembly. See the article Message Sequence.

## Example

An order service sends a request message to a pricing service. The body holds the order lines. The header holds a unique request ID and a return address, the queue where the order service wants answers. The pricing service computes prices. It sends a reply to that queue and copies the request ID into the reply's correlation ID. The order service reads the reply and matches it to the right order. If the request header also had an expiration time, the pricing service would ignore the request once that time passed.

## Trade-offs

Splitting a large payload into a sequence of smaller messages suits cases where consumers can process chunks independently or reassemble them after delivery. It also adds the need for sequencing, correlation and reassembly. An envelope makes a message fit the infrastructure, but it must be unwrapped at the destination.
