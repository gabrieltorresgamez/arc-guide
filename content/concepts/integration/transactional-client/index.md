---
title: Transactional Client
slug: transactional-client
category: integration
kind: pattern
summary: A transactional client groups its message operations into one transaction. A sent message only
  enters the channel once the sender commits. The cost is slower performance in widely distributed systems.
arc42:
- 8
- 9
- 11
step: s08-integration-data
related:
- idempotent-receiver
- dead-letter-channel
- message-channel
- messaging
- request-reply
- retry
checks:
- If a service updates a database and sends a message, the document states how both are kept consistent,
  for example with an outbox.
- If a relay publishes outbox messages, the document states that duplicates are possible and how receivers
  handle them.
- If transactions span widely distributed systems, the document discusses the performance cost.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/TransactionalClient.html
  title: Transactional Client - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://microservices.io/patterns/data/transactional-outbox.html
  title: 'Pattern: Transactional outbox'
  site: microservices.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Transactional outbox: data and message are saved together, a relay publishes later.'
review:
  status: generated
  flags: []
---

## Explanation

A transactional client is a sender or receiver of messages that wraps its work in a transaction.

**Sending.** With a transactional sender, the message is not really in the channel until the sender commits. Until then, the send is provisional.

**The database-plus-message problem.** A service often must update its database and also send a message to a broker. Both must happen, or neither. The transactional outbox pattern addresses this problem. The service stores the outgoing message in its own database, in the same transaction as the business data. A separate relay process publishes the stored message later. (The article Message Channel explains channels.)

**Duplicates.** The relay might publish a message more than once. So receivers may see duplicates, and consumers must be idempotent. The article Idempotent Receiver covers receivers that cope with repeats.

## Example

An order service saves a new order and must announce it to other systems. It writes the order and an "order created" message into its own database in one transaction. If the transaction fails, neither exists. If it commits, a relay later publishes the message. If the relay fails midway, it may publish the message again, so downstream systems must handle a repeat.

## Trade-offs

Transactional semantics can seriously degrade performance in widely distributed systems. Many cloud messaging systems therefore don't implement transactional clients; Amazon SQS instead offers a visibility timeout to protect against a client crashing after it consumes a message but before it processes it.

The outbox keeps the database change and the message together. In exchange, it accepts possible duplicate messages from the relay.
