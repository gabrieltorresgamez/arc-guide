---
title: Event-Driven Consumer
slug: event-driven-consumer
category: integration
kind: pattern
summary: An Event-Driven Consumer waits until the messaging system hands it a message through a callback.
  It runs no polling loop. Arrivals set its pace, so a burst can overload it.
arc42:
- 5
- 6
- 8
- 10
step: s08-integration-data
related:
- polling-consumer
- message-channel
- dead-letter-channel
- idempotent-receiver
- publish-subscribe-channel
- point-to-point-channel
- messaging
checks:
- The document states how a burst of messages is handled, for example through a buffering queue, autoscaling
  or several competing consumers.
- Where a push consumer is used with RabbitMQ, a prefetch limit is set and is not 0 (unlimited).
- Consumers that compete on one channel are idempotent, and failing messages go to a dead-letter queue.
- For Kafka, the planned consumer count does not exceed the partition count of the topic.
- The document says whether each consumer is event-driven or polling, and so who controls the consumption
  pace.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventDrivenConsumer.html
  title: Event-Driven Consumer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PollingConsumer.html
  title: Polling Consumer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html
  title: Competing Consumers - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/competing-consumers
  title: Competing Consumers Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://www.rabbitmq.com/docs/consumer-prefetch
  title: Consumer Prefetch | RabbitMQ
  site: rabbitmq.com
  accessed: '2026-11-09'
- url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/message-listener-container.html
  title: 'Message Listener Containers :: Spring Kafka'
  site: docs.spring.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The broker calls the listener on arrival; a polling consumer asks for each message.
review:
  status: generated
  flags: []
---

## Explanation

An Event-Driven Consumer is a receiver that the messaging system calls when a message arrives on its channel. The application does not ask for messages. The consumer passes each message to the application through a callback, which is a function the application supplies.

Delivery triggers the consumer, so no thread runs while it waits. How the messaging system itself obtains the message is implementation-specific and may or may not be event-driven.

**Contrast with a Polling Consumer.** A Polling Consumer explicitly asks for a message when it wants one. Its loop is: poll, process, poll again. It controls when it receives.

**Ways to manage load**
- Run several consumers on one channel so they process messages at the same time. This is the Competing Consumers approach.
- With Kafka, partitions are assigned to consumers in advance. A consumer group cannot have more competing consumers than the topic has partitions.
- With RabbitMQ, a prefetch limit caps the unacknowledged messages in flight per consumer. Setting it to 0 means no limit, so any number of messages can wait unacknowledged.

**Concurrency in practice.** Spring Kafka's ConcurrentMessageListenerContainer delegates to several single-threaded containers. Together they consume with multiple threads.

**Kafka detail.** In Spring Kafka, the consumer's poll() method returns records, and the message listener is called for each record.

**Failures and ordering.** Competing consumers give no ordering guarantee, so consumers should be idempotent. That means handling the same message twice causes no harm. Redelivery and poison messages (messages that keep failing) call for dead-letter queues. In Azure Service Bus PeekLock mode, success completes the message. Failure abandons it, so another consumer can retry it.

## Example

A shop publishes an order message to a channel. The billing service registered a listener earlier. When the message arrives, the messaging system calls the listener with the order. Billing has no loop and no thread waiting. During a sale, orders flood in. The team adds more billing consumers on the same channel and sets a prefetch limit so each one holds only a few unfinished messages.

## Trade-offs

More consumers weaken ordering guarantees and require idempotent handling. With Kafka, a consumer group cannot have more competing consumers than the topic has partitions.
