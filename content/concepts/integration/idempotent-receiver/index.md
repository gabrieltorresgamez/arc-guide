---
title: Idempotent Receiver
slug: idempotent-receiver
category: integration
kind: pattern
summary: An idempotent receiver handles the same message more than once without repeating its effect.
  A common way is to record the IDs of processed messages and ignore any repeat.
arc42:
- 8
- 6
- 4
step: s08-integration-data
related:
- messaging
- retry
- transactional-client
- dead-letter-channel
- correlation-identifier
- request-reply
- messaging-pattern-language
checks:
- The document states that receivers must tolerate receiving the same message more than once.
- The document says how duplicates are detected, for example by storing the IDs of processed messages.
- The ID record and the business effect are saved in the same database transaction.
- The retention period for processed IDs or keys is stated.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html
  title: Idempotent Receiver - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://microservices.io/patterns/communication-style/idempotent-consumer.html
  title: 'Pattern: Idempotent Consumer'
  site: microservices.io
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/patterns-of-distributed-systems/idempotent-receiver.html
  title: Idempotent Receiver
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html
  title: Using the message deduplication ID in Amazon SQS - Amazon Simple Queue Service
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://docs.stripe.com/api/idempotent_requests
  title: Idempotent requests | Stripe API Reference
  site: docs.stripe.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A receiver ignores a repeated message by checking processed IDs in the same transaction.
review:
  status: generated
  flags: []
---

## Explanation

A receiver may get the same message more than once. The Idempotent Receiver pattern says to design the receiver so it tolerates this. The core question is how a consumer handles duplicate messages correctly.

**Why duplicates happen.** A client cannot always know whether its request was processed. To be sure, it sends the request again. So the server may see the same request twice.

**Recording processed IDs.** One solution is deduplication, which means detecting and skipping repeats. The consumer stores the ID of each message it has processed in the database. If a message arrives with a known ID, the consumer skips it. The IDs can live in a separate table. They can also live inside the business entities the consumer creates or updates.

**Keeping it atomic.** After starting a database transaction, the handler inserts the message ID. A duplicate then violates the primary key, which is the database rule that each ID may appear only once. The handler rolls back the transaction and ignores the message.

**Saving the response.** The server can also save the response for each client and request number. On a retry, it returns the saved response without processing the request again.

**Examples in products.**
- Amazon SQS FIFO queues deduplicate by a message deduplication ID. Within a 5-minute window, only one message with the same ID is processed and delivered.
- Stripe lets clients attach an idempotency key to a request. After a connection error, the client can retry without creating a second object or applying an update twice. For API v1, Stripe stores the first response for each key and returns it on retries.

## Example

A shop sends a "charge order 1042" message with ID `m-77` to a payment service. The network drops the reply, so the shop sends the message again.

The payment service starts a transaction. It tries to insert `m-77` into its table of processed IDs. The ID already exists, so the insert fails. The service rolls back and ignores the message. The customer is charged once.

## Trade-offs

Stripe, for example, may prune keys after 24 hours. SQS FIFO deduplicates only within a 5-minute window. A duplicate that arrives after the window is no longer caught by that mechanism.
