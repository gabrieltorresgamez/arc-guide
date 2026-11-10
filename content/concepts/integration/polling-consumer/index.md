---
title: Polling Consumer
slug: polling-consumer
category: integration
kind: pattern
summary: A Polling Consumer asks a channel for the next message when it is ready, instead of waiting to
  be handed one. The consumer starts every retrieval, so it decides when to take work.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- event-driven-consumer
- message-channel
- messaging
- point-to-point-channel
- publish-subscribe-channel
- synchronous-vs-asynchronous-communication
- idempotent-receiver
- messaging-pattern-language
checks:
- The document states whether each consumer pulls messages (polling) or is handed them (event-driven).
- Where consumers block while waiting, the document accounts for the thread each blocked consumer uses.
- For queue services such as SQS, the document states whether short or long polling is used and the wait
  time.
- Where several consumers read one queue, the document states that each message goes to one consumer.
- The document describes how a pulled message is completed or abandoned.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PollingConsumer.html
  title: Polling Consumer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventDrivenConsumer.html
  title: Event-Driven Consumer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html
  title: Amazon SQS short and long polling - Amazon Simple Queue Service
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/competing-consumers
  title: Competing Consumers Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A consumer asks for each message when it is ready.
review:
  status: generated
  flags: []
---

## Explanation

A Polling Consumer is a receiver that pulls messages from a channel (see Message Channel). It gets nothing until it explicitly asks for a message. The consumer starts each retrieval.

**Blocking receive.** A polling consumer is also called a synchronous receiver. In a blocking receive, the receiving thread waits until a message arrives. The difference between blocking and non-blocking receive only shows when the consumer polls faster than messages arrive.

**Contrast with push.** An Event-Driven Consumer is handed messages as they are delivered on the channel. It needs no running thread while idle. A callback thread invokes it when a message arrives. A blocked polling thread, by comparison, sits and waits.

**Long polling.** Amazon SQS offers two ways to poll. Short polling returns at once, even when no messages are found. Long polling waits, and returns an empty response only if the wait time runs out. It returns messages as soon as they are available. You turn it on with a wait time above 0, up to 20 seconds. It cuts the cost of empty responses.

**Scaling out.** Several consumer instances can pull from one queue. This is the Competing Consumers pattern. Each message goes to only one consumer. The queue acts as a buffer and levels the load between producers and consumers.

**Acknowledgment.** In Azure Service Bus PeekLock mode, a consumer that receives a message hides it from other consumers.

## Example

An order service reads from a queue of new orders. Three copies of the service run. Each copy receives an order in PeekLock mode, which hides that order from the other copies. The copy processes the order and then marks it complete. If processing fails, it might abandon the order so another copy can try. When the queue is empty, a copy waits for up to a set time before it gets an empty answer.

## Trade-offs

- **Blocking costs a thread.** A blocking receive holds a thread while it waits. An Event-Driven Consumer needs no running thread while idle.
- **Empty requests cost money.** Short polling returns at once even when nothing is there, so it can produce many empty responses. Long polling reduces them and lowers cost.
- **Wait time has a cap.** In SQS, the long polling wait is at most 20 seconds.
- **Competing consumers give each message to one consumer only.** This differs from the Publisher-Subscriber pattern, where all consumers receive every message.
