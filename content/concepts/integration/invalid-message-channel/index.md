---
title: Invalid Message Channel
slug: invalid-message-channel
category: integration
kind: pattern
summary: An Invalid Message Channel is a dedicated channel where a receiver puts messages it cannot process.
  The receiver handles bad messages gracefully, and people can inspect them later.
arc42:
- 8
- 6
- 11
step: s08-integration-data
related:
- dead-letter-channel
- message-channel
- message-filter
- selective-consumer
- content-based-router
- retry
- datatype-channel
- messaging-pattern-language
checks:
- The document names a dedicated channel where the receiver puts messages it cannot process.
- The document separates receiver-judged invalid content from delivery failures handled by the messaging
  system (Dead Letter Channel).
- Rejected messages carry error metadata such as a reason and description.
- A retry or delivery limit caps repeated failures of poison messages.
- The document says who inspects, corrects, resubmits, or removes messages in the invalid channel.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/InvalidMessageChannel.html
  title: Invalid Message Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html
  title: Dead Letter Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues
  title: Service Bus Dead-Letter Queues - Azure Service Bus | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A receiver routes messages it cannot process to a dedicated channel.
review:
  status: generated
  flags: []
---

## Explanation

A receiver sometimes gets a message that makes no sense to it. The Invalid Message Channel pattern answers one question: how can the receiver handle such a message gracefully?

The solution is simple. The receiver moves the improper message to a special, dedicated channel. That channel holds messages that their receivers could not process. (A channel is the path that carries messages between systems. See Message Channel.)

**How it differs from a Dead Letter Channel.** The two patterns solve different problems. A Dead Letter Channel covers what the messaging system does with a message it cannot deliver. The Invalid Message Channel covers a message the receiver judges to have unusable content. See Dead Letter Channel.

**Products blur the line.** Azure Service Bus has a dead-letter queue (DLQ). It holds messages that cannot be delivered or processed. Applications can also put messages there on purpose, for example messages with malformed payloads or failed message-level authentication. That second use resembles an Invalid Message Channel.

**Error metadata.** A rejected message is easier to diagnose when it carries the reason. Service Bus adds a dead-letter reason and a description to each dead-lettered message. Applications can define their own reason codes. Microsoft recommends putting the exception type in the reason and the stack trace in the description. A Dead Letter Channel can also record where the message died.

**Repeated failures.** Two messaging products cap redelivery attempts with a counter:

- In Amazon SQS, each redelivery raises the message's receive count. At a configured limit, the message moves to a dead letter queue.
- In Service Bus, the default maximum delivery count is 10. Past it, the message moves to the DLQ with the reason MaxDeliveryCountExceeded.

**What happens next.** In Service Bus, people can remove and inspect dead-lettered messages. A user may correct and resubmit them once the cause is fixed.

## Example

An order service reads messages from an "orders" channel. One message arrives with a garbled body. The service cannot read it, so it moves the message to an "orders-invalid" channel. It adds a short reason, such as "payload not readable". Later, a support engineer opens that channel, finds the cause, fixes the data, and sends the message again.

## Trade-offs

Dead-lettered messages do not clean themselves up. In Service Bus they stay until someone explicitly retrieves and completes them.
