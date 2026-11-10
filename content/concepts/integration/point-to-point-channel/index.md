---
title: Point-to-Point Channel
slug: point-to-point-channel
category: integration
kind: pattern
summary: A Point-to-Point Channel makes sure only one receiver gets each message. If several receivers
  share the channel, they compete, and each message goes to just one of them.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- message-channel
- publish-subscribe-channel
- idempotent-receiver
- dead-letter-channel
- messaging
- scalability
- polling-consumer
- event-driven-consumer
checks:
- The document states which channels must deliver each message to exactly one receiver, and uses point-to-point
  channels for them.
- Where several consumers share a channel, the document notes that processing order is not guaranteed
  and says how order is handled if needed.
- Consumers on queue-based channels are designed to be idempotent, because delivery is at least once.
- The document explains how failed messages become available again for another consumer.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html
  title: Point-to-Point Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/competing-consumers
  title: Competing Consumers Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html
  title: Competing Consumers - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Competing consumers on one channel: each message goes to exactly one receiver.'
review:
  status: generated
  flags: []
---

## Explanation

Sometimes a sender needs to be sure that exactly one receiver handles a message or performs a call.

The solution is to send the message on a Point-to-Point Channel. This channel guarantees that only one receiver gets any particular message. The Message Channel article explains channels in general.

**Compared with publish-subscribe.** In a Publish/Subscribe Channel, all consumers receive every message. In a point-to-point setup, one consumer receives each message.

**Competing Consumers.** One consumer may be too slow for the rate at which messages arrive. The fix is to put several consumers on the same channel. They process different messages at the same time.

**Order is not guaranteed.** With several consumers, the order in which they receive messages may differ from the order in which the messages were created. Azure Service Bus sessions can provide first-in, first-out (FIFO) order when it is needed.

**Delivery at least once.** In the Azure pattern, the message queue ensures each message is delivered at least once. Azure advises making operations idempotent, which helps when a message is retrieved and processed more than once. The Idempotent Receiver article covers this.

**Redelivery.** In Azure Service Bus, the PeekLock mode hides a message from other consumers while one consumer works on it. If processing succeeds, the consumer calls Complete to settle the message. If it fails, the runtime may call Abandon. The message then becomes visible again, so another consumer can pick it up.

## Example

An online shop puts "ship order 1042" messages on one channel. Three warehouse workers listen on that channel. Each message goes to exactly one worker, so no order is shipped twice. When orders pile up, the shop adds a fourth worker on the same channel.

## Trade-offs

- **Scaling versus order.** More competing consumers process more messages at once. But the order of processing is no longer guaranteed. Sessions in Azure Service Bus can restore FIFO order.
- **No lost messages versus repeats.** In the Azure pattern, a message may be retrieved and processed more than once, so idempotent operations may be needed.
- **One receiver versus many.** If several parties each need every message, a Publish/Subscribe Channel fits better.
