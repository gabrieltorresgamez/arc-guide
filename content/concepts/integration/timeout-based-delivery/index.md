---
title: Timeout-Based Delivery
slug: timeout-based-delivery
category: integration
kind: pattern
summary: Timeout-based delivery hides a message from other consumers while one consumer works on it. The
  consumer deletes it when done. If the timeout runs out first, the message reappears and is delivered
  again, so duplicates are possible.
arc42:
- 6
- 8
- 10
step: s08-integration-data
related:
- idempotent-receiver
- dead-letter-channel
- heartbeat
- retry
- messaging
- polling-consumer
- message-channel
- point-to-point-channel
checks:
- The visibility timeout or lock duration is set deliberately and is longer than normal processing time.
- Consumers are designed to handle duplicate delivery, because the queue is at-least-once.
- Long-running jobs extend the timeout with a heartbeat, within the maximum limit.
- A dead-letter queue is configured for messages that keep failing.
sources:
- url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html
  title: Amazon SQS visibility timeout - Amazon Simple Queue Service
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-transfers-locks-settlement
  title: Message Transfers, Locks, and Settlement - Azure Service Bus | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://docs.cloud.google.com/pubsub/docs/lease-management
  title: Extend ack time with lease management  |  Pub/Sub  |  Google Cloud Documentation
  site: docs.cloud.google.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A message becomes visible again after the timeout and is delivered to another consumer.
review:
  status: generated
  flags: []
---

## Explanation

Timeout-based delivery is a way for a message queue to hand out work without losing it. Amazon SQS calls the timeout a *visibility timeout*. Azure Service Bus calls the same idea *Peek-Lock*.

**How it works**

1. A consumer receives a message. The message stays in the queue, but other consumers cannot see it for a limited time. Service Bus does this with an exclusive lock.
2. The consumer processes the message.
3. On success, the consumer deletes the message before the timeout ends. Service Bus calls this step Complete.
4. If the timeout expires first, the message becomes visible again. Another consumer can pick it up.

**Why it matters**

A crash or a connectivity problem means the consumer never deletes the message. The timeout runs out and the message is retried, so it is not lost.

**Duplicates**

This model is *at-least-once* delivery: a message arrives one or more times. Even inside the timeout, SQS gives no absolute guarantee against a second delivery. Pub/Sub acknowledgment deadlines are also not guaranteed to be respected unless exactly-once delivery is enabled. Consumers should therefore cope with duplicates. The Idempotent Receiver article covers this.

**Choosing the timeout**

- Size it to your normal processing time. Service Bus advises a lock longer than normal processing, so you rarely need to renew it. Its lock defaults to 1 minute, with a 5-minute maximum. The SQS default is 30 seconds.
- A long timeout delays retries after a failure.
- For slow jobs, extend the timeout periodically with a heartbeat (see the Heartbeat article). SQS has a 12-hour cap that extensions do not reset. The lock owner can also renew a Service Bus lock.

**Giving a message back early or rejecting it**

- In SQS, setting the timeout to 0 releases a message to other consumers at once.
- In Service Bus, Abandon releases it immediately. DeadLetter rejects it when a retry won't help.

**Messages that keep failing**

A dead-letter queue collects messages that fail after several attempts. They then stop circulating in the main queue. See the Dead Letter Channel article.

## Example

A shop's queue holds order-confirmation emails to send. Worker A receives one and the queue hides it for 30 seconds. Worker A crashes. After 30 seconds the message reappears, and Worker B sends the email. If Worker A had actually sent the email just before crashing, the customer gets two emails. To avoid this, the sender records which order IDs it has already handled.

## Trade-offs

- **Safety versus duplicates.** Explicit deletion means a failed consumer does not lose work. The price is that a message may be processed more than once.
- **Short versus long timeout.** A short timeout retries quickly after a failure. A timeout that is too long delays retries.
- **Compared with at-most-once.** Service Bus Receive-and-Delete consumes the message as soon as it is sent. If the transfer fails, the message is lost. Peek-Lock avoids this loss by requiring explicit settlement.
