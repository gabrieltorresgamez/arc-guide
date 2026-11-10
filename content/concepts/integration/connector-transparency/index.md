---
title: Connector Transparency (Direct vs Indirect Connection)
slug: connector-transparency
category: integration
kind: concept
summary: An indirect connector puts a channel between components, so a sender does not need to know who
  receives its data. This lowers coupling, but it makes the overall flow harder to follow.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- software-connector
- message-channel
- publish-subscribe-channel
- loose-coupling
- messaging
- remote-procedure-call
- synchronous-vs-asynchronous-connector
- classification-of-integration-patterns
checks:
- Each message channel or topic has a documented purpose, because the channel name is the assumption sender
  and receiver share.
- Where publishers broadcast events, the document says that each subscriber gets its own copy and the
  publisher does not name recipients.
- For event-based flows, the document describes the end-to-end flow somewhere explicit, since it is not
  visible in program text.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html
  title: Message Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/201701-event-driven.html
  title: What do you mean by “Event-Driven”?
  site: martinfowler.com
  accessed: '2026-11-08'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Messaging.html
  title: Messaging - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html
  title: Publish-Subscribe Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: A publisher sends to one channel. The channel delivers a copy to each subscriber, and the publisher
    knows none of them.
review:
  status: generated
  flags: []
---

## Explanation

See the article Software Connector for what a connector is.

**Indirect connection.** A message channel sits between sender and receiver. The sender does not need to know which application will read the data. Because the messaging system has separate channels for different kinds of information, the sender can expect that whatever reads from a channel will be interested in that kind of data.

**What the intermediary gives you:**

- **Less knowledge of the other side.** The sender does not name its receivers.
- **Independent timing.** Sender and receiver do not have to run at the same time. Sending a message does not require both systems to be ready.
- **Broadcast.** The decoupling allows integrators to broadcast messages to multiple receivers.
- **Changes in transit.** The intermediary can transform messages without the sender or receiver knowing.

**Publish-subscribe.** The publisher sends an event to one input channel. The channel delivers a copy to every subscriber. It splits into one output channel per subscriber. The publisher never names its recipients. See Publish/Subscribe Channel and Message Channel.

**Low coupling.** With event notification, the source does not care about the response. Event notification also implies a low level of coupling. See Loose Coupling for the general idea.

## Example

An online shop publishes an "order placed" event to a channel. A billing service and a shipping service each subscribe. The shop code never mentions either one. Later, a team adds a reporting service as a third subscriber. The shop code does not change.

## Trade-offs

With event notification, a logical flow that runs over several notifications can be hard to see, because it is not explicit in any program text. Often the only way to discover it is to monitor a live system. This makes such a flow hard to debug and modify.
