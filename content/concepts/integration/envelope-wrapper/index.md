---
title: Envelope Wrapper
slug: envelope-wrapper
category: integration
kind: pattern
summary: An Envelope Wrapper puts application data inside an envelope that the messaging system accepts.
  The receiver removes the envelope at the destination and gets the original data back.
arc42:
- 3
- 5
- 8
step: s08-integration-data
related:
- message-structure
- message-translator
- content-enricher
- canonical-data-model
- messaging
- messaging-pattern-language
- messaging-systems-and-protocols
- interoperability
checks:
- Where a messaging exchange imposes format requirements such as header fields, the document states that
  application data is wrapped in a compliant envelope.
- The document states where the envelope is removed, so the receiving application gets the original data.
- 'Where SOAP is used, headers and payload are kept separate: headers in the envelope header, content
  in the body.'
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/EnvelopeWrapper.html
  title: Envelope Wrapper - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.w3.org/TR/soap12-part1/
  title: 'SOAP Version 1.2 Part 1: Messaging Framework (Second Edition)'
  site: w3.org
  accessed: '2026-11-09'
- url: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
  title: spec/cloudevents/spec.md at main · cloudevents/spec · GitHub
  site: github.com
  accessed: '2026-11-09'
- url: https://cloudevents.io/
  title: CloudEvents |
  site: cloudevents.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Data is wrapped before it enters the messaging system and unwrapped at the destination.
review:
  status: generated
  flags: []
---

## Explanation

Some messaging exchanges demand a specific message format. They may require header fields or encryption. Endpoint systems are generally unaware of such header fields and may even treat them as erroneous.

The Envelope Wrapper pattern solves this. The sender wraps the application data in an envelope that the messaging infrastructure accepts. When the message arrives at the destination, it is unwrapped.

**SOAP as an example.** A SOAP message has an outermost element called the envelope. Inside it sit two parts:

- A header, made of blocks. Each block may target any receiver along the message path.
- A body, which carries content for the ultimate receiver.


**CloudEvents as an example.** CloudEvents is a specification that gives event data one common description format. Events carry context metadata in Context Attributes alongside the event data. Its protocol bindings describe how events are sent and received over a given protocol. A binding may map an event directly to the body of the transport envelope, or add further formatting and structure to that envelope.

For related ideas, see Content-Based Router, Content Enricher, Messaging Bridge, and Pipes and Filters.

## Example

A legacy billing system produces plain invoice records. The company's messaging platform only accepts messages with a set of header fields. A small component on the sending side wraps each invoice in an envelope that carries those fields. The platform handles the message. A matching component on the receiving side unwraps it. The accounting application sees the same invoice record the billing system produced.
