---
title: Dead Letter Channel
slug: dead-letter-channel
category: integration
kind: pattern
summary: A Dead Letter Channel is a side queue for messages a messaging system cannot deliver or process.
  Failed messages wait there to be inspected, fixed and resubmitted instead of being lost.
arc42:
- 8
- 6
- 11
step: s08-integration-data
related:
- invalid-message-channel
- message-channel
- retry
- messaging
- timeout-based-delivery
- idempotent-receiver
- point-to-point-channel
- exception-handling
checks:
- The document states how many delivery attempts are allowed before a message moves to the dead-letter
  queue, and that the limit leaves room for retries.
- Someone is named to watch and clear the dead-letter queue, since it is not cleaned automatically.
- The DLQ retention period is longer than the source queue's retention period.
- The document explains how dead-lettered messages are inspected and resubmitted after a fix.
- The effect of a DLQ on message ordering is assessed where FIFO queues are used.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html
  title: Dead Letter Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html
  title: Using dead-letter queues in Amazon SQS - Amazon Simple Queue Service
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues
  title: Service Bus Dead-Letter Queues - Azure Service Bus | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://www.rabbitmq.com/docs/dlx
  title: Dead Letter Exchanges | RabbitMQ
  site: rabbitmq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Failed or expired messages move to a dead-letter queue, then are inspected and resubmitted.
review:
  status: generated
  flags: []
---

## Explanation

A messaging system sometimes gets a message it cannot deliver. The Dead Letter Channel pattern answers what to do with it. Related patterns are the Invalid Message Channel and Message Expiration.

The idea is simple. Move the failed message to a separate queue, often called a dead-letter queue (DLQ). Teams can then look at it and find out why processing failed.

**Why messages end up there**

- No receiver can take the message, or the receiver cannot process it.
- The message is malformed. Applications can also dead-letter unacceptable messages on purpose, for example those with broken payloads.
- Delivery attempts ran out. Azure Service Bus dead-letters a message after a delivery limit, 10 by default.
- In Amazon SQS, a redrive policy sets `maxReceiveCount`, the number of receives allowed before the move. It should be high enough to allow retries.
- The message expired. With dead-lettering on, Service Bus moves expired messages (time to live, or TTL, ran out) to the DLQ with the reason `TTLExpiredException`.
- RabbitMQ republishes messages to a dead letter exchange on four events. These include per-message expiry, queue length overflow, rejection and the delivery limit. The `x-death` record shows which one happened.

**What happens next**

People inspect the messages. Once the cause is fixed, they resubmit the messages for reprocessing. Service Bus supports this individually or in batches, for example with Service Bus Explorer. When an application dead-letters a message itself, it should record the exception type and stack trace. Large stack traces may hit size quotas.

**Operating it**

Service Bus never cleans its DLQ automatically. Messages stay until someone explicitly handles them. An unattended DLQ therefore just grows.

In SQS, retention in a DLQ counts from the original enqueue time for standard queues. Set the DLQ retention longer than the source queue's, or messages may be deleted early.

## Example

An order service reads "place order" messages from a queue. One message has a broken payload, and the service rejects it each time. After the allowed number of attempts, the broker moves it to the dead-letter queue. The other orders keep flowing. A developer opens the dead-lettered message, reads the recorded error, fixes the cause, and resubmits the message.

## Trade-offs

- **Ordering:** SQS warns that using a DLQ with a FIFO queue can break the exact order of messages or operations.
- **Message loss:** RabbitMQ dead-lettering by default has no publisher confirms. Messages can be lost if the target queue is unavailable. Quorum queues offer at-least-once dead-lettering.
- **Neglect:** Service Bus does no automatic cleanup, so a DLQ nobody watches only accumulates messages.
- **Retry settings:** A retry limit that is too low sends recoverable messages to the DLQ too early.
