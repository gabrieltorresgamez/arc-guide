---
title: Enterprise Integration Patterns
slug: enterprise-integration-patterns
order: 60
category: integration
kind: framework
summary: Enterprise Integration Patterns are 61 named designs for connecting applications through messaging, in seven categories. Messaging is asynchronous, program-to-program communication with reliable delivery.
long_ok: true
arc42:
- 3
- 5
- 6
- 8
step: s08-integration-data
related:
- messaging
- file-transfer
- shared-database
- synchronous-vs-asynchronous-communication
- integration-style
- pipes-and-filters
checks:
- The document names the messaging patterns it uses by their EIP names.
- Where a pattern is used, the document says which problem it solves.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Introduction.html
  title: Introduction - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/4.22.x/eips/enterprise-integration-patterns.html
  title: 'EIPs :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html
  title: Point-to-Point Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html
  title: Dead Letter Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html
  title: Message Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Message.html
  title: Message - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PipesAndFilters.html
  title: Pipes and Filters - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageRouter.html
  title: Message Router - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html
  title: Message Translator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageEndpoint.html
  title: Message Endpoint - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html
  title: Publish-Subscribe Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DatatypeChannel.html
  title: Datatype Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/InvalidMessageChannel.html
  title: Invalid Message Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedMessaging.html
  title: Guaranteed Delivery - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelAdapter.html
  title: Channel Adapter - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingBridge.html
  title: Messaging Bridge - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBus.html
  title: Message Bus - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CommandMessage.html
  title: Command Message - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DocumentMessage.html
  title: Document Message - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html
  title: Event Message - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html
  title: Request-Reply - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ReturnAddress.html
  title: Return Address - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CorrelationIdentifier.html
  title: Correlation Identifier - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageSequence.html
  title: Message Sequence - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageExpiration.html
  title: Message Expiration - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/FormatIndicator.html
  title: Format Indicator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html
  title: Content-Based Router - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Filter.html
  title: Message Filter - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DynamicRouter.html
  title: Dynamic Router - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RecipientList.html
  title: Recipient List - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Sequencer.html
  title: Splitter - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html
  title: Aggregator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Resequencer.html
  title: Resequencer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DistributionAggregate.html
  title: Composed Message Processor - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html
  title: Scatter-Gather - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RoutingTable.html
  title: Routing Slip - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html
  title: Process Manager - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBroker.html
  title: Message Broker - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/EnvelopeWrapper.html
  title: Envelope Wrapper - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DataEnricher.html
  title: Content Enricher - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentFilter.html
  title: Content Filter - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html
  title: Claim Check - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Normalizer.html
  title: Normalizer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html
  title: Canonical Data Model - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingGateway.html
  title: Messaging Gateway - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingMapper.html
  title: Messaging Mapper - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/TransactionalClient.html
  title: Transactional Client - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PollingConsumer.html
  title: Polling Consumer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventDrivenConsumer.html
  title: Event-Driven Consumer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html
  title: Competing Consumers - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageDispatcher.html
  title: Message Dispatcher - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageSelector.html
  title: Selective Consumer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DurableSubscription.html
  title: Durable Subscriber - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html
  title: Idempotent Receiver - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingAdapter.html
  title: Service Activator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ControlBus.html
  title: Control Bus - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Detour.html
  title: Detour - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/WireTap.html
  title: Wire Tap - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageHistory.html
  title: Message History - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageStore.html
  title: Message Store - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/SmartProxy.html
  title: Smart Proxy - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/TestMessage.html
  title: Test Message - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelPurger.html
  title: Channel Purger - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-16'
diagrams:
- file: diagram-1.mmd
  caption: Basic messaging flow with a dead letter queue for undeliverable messages.
review:
  status: generated
  flags: []
---

## Explanation

Enterprise Integration Patterns (EIP) are named designs for connecting applications through messaging. Messaging is asynchronous, program-to-program communication with reliable delivery. Asynchronous means the sender does not wait for the receiver (see the article Synchronous vs. Asynchronous Communication). The authors group their patterns into seven categories. This page lists all of them with a short definition. The official page of each pattern has the full description.

Messaging is one of four integration styles. The others are File Transfer, Shared Database and Remote Procedure Invocation (see Integration Style). Apache Camel supports most of these patterns.

**Messaging systems**

- **Message Channel:** A pipe between applications. One application writes messages into it and another reads them out, so the sender does not need to know the receiver. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html)
- **Message:** A data record that the messaging system can transmit through a channel. Any data to be sent must be turned into one or more messages. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Message.html)
- **Pipes and Filters:** A larger processing task is split into small, independent steps (filters) that are connected by channels (pipes). [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PipesAndFilters.html)
- **Message Router:** A component that passes messages on to different filters depending on a set of conditions, so the processing steps stay decoupled. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageRouter.html)
- **Message Translator:** A special filter that converts messages from one data format to another, so systems with different formats can communicate. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html)
- **Message Endpoint:** The client of the messaging system that an application uses to send or receive messages. It keeps the rest of the application free of messaging details. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageEndpoint.html)

**Messaging channels**

- **Point-to-Point Channel:** Only one receiver gets each message. If several receivers share the channel, they compete and each message goes to just one of them. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html)
- **Publish-Subscribe Channel:** Every interested subscriber gets its own copy of each message. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html)
- **Datatype Channel:** Each type of data gets its own channel. The sender picks the matching channel, and the receiver knows the type from the channel it reads. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DatatypeChannel.html)
- **Invalid Message Channel:** A dedicated channel where a receiver puts messages it cannot process, so people can inspect them later. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/InvalidMessageChannel.html)
- **Dead Letter Channel:** A side channel where the messaging system can move messages it cannot deliver. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html)
- **Guaranteed Delivery:** Messages are stored persistently so they are not lost even if the messaging system fails. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedMessaging.html)
- **Channel Adapter:** A component that connects an application to the messaging system. It publishes messages based on the application's data and calls the application's functions when messages arrive. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelAdapter.html)
- **Messaging Bridge:** A connection between messaging systems that replicates messages from channels in one system to corresponding channels in another. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingBridge.html)
- **Message Bus:** Middleware that combines a common data model, a common command set and a messaging infrastructure. Applications can be added or removed without affecting the others. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBus.html)

**Message construction**

- **Command Message:** A regular message that contains a command, used to invoke a procedure in another application. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CommandMessage.html)
- **Document Message:** A message that passes data and lets the receiver decide what, if anything, to do with it. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DocumentMessage.html)
- **Event Message:** A message that announces an event for reliable, asynchronous notification between applications. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html)
- **Request-Reply:** The requestor sends a message on one channel and gets the answer on another. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html)
- **Return Address:** A reply destination carried inside the request message, so the replier does not need to know in advance who is asking. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ReturnAddress.html)
- **Correlation Identifier:** The replier copies the request's unique ID into the reply, so the requestor can match each reply to its request. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CorrelationIdentifier.html)
- **Message Sequence:** Data too big for one message is split into several smaller messages. Each carries a position, so the receiver can rebuild the whole. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageSequence.html)
- **Message Expiration:** A message carries the time after which it is stale. Consumers ignore it once that time has passed. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageExpiration.html)
- **Format Indicator:** A tag on each message that names its data format, which helps a message format cope with future change. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/FormatIndicator.html)

**Message routing**

- **Content-Based Router:** Reads each message and sends it to a channel chosen from data inside the message. Its fixed rules need careful upkeep. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html)
- **Message Filter:** Checks each message against a condition on its content. Matching messages move on and the rest are discarded. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Filter.html)
- **Dynamic Router:** Sends messages to recipients using rules it learns at runtime. Recipients tell the router what they want over a control channel. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DynamicRouter.html)
- **Recipient List:** Sends one message to a list of recipients that is decided dynamically. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RecipientList.html)
- **Splitter:** Breaks a message that contains several elements into a series of individual messages, so each element can be processed separately. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Sequencer.html)
- **Aggregator:** Collects and stores individual messages until a complete set of related messages has arrived. It then publishes a single message distilled from them. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html)
- **Resequencer:** Collects out-of-sequence messages and publishes them to the output channel in a specified order. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Resequencer.html)
- **Composed Message Processor:** Keeps the overall message flow intact when one message holds several elements that may need different processing. An aggregator gathers the results. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DistributionAggregate.html)
- **Scatter-Gather:** Sends one request to several recipients, then combines their replies into a single answer. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html)
- **Routing Slip:** A list attached to a message that names the processing steps it must visit, in order, so every message can follow its own path. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RoutingTable.html)
- **Process Manager:** A central component that tracks the state of a process and decides the next processing step. It fits cases where the needed steps are not known in advance. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html)
- **Message Broker:** Receives messages from multiple destinations, determines the correct destination and routes each message there, which keeps central control over the flow. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBroker.html)

**Message transformation**

- **Envelope Wrapper:** Puts application data inside an envelope that the messaging system accepts. The receiver removes the envelope to get the original data back. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EnvelopeWrapper.html)
- **Content Enricher:** Adds data that a receiver needs but the sender lacks. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DataEnricher.html)
- **Content Filter:** Removes unimportant data items from inside a message and keeps only the important ones. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentFilter.html)
- **Claim Check:** Keeps large data out of messages. The sender stores the data externally and sends a small reference that the receiver uses to fetch it. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html)
- **Normalizer:** Handles messages that mean the same thing but arrive in different formats. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Normalizer.html)
- **Canonical Data Model:** One shared, application-independent data format that systems translate to and from. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html)

**Messaging endpoints**

- **Messaging Gateway:** Encapsulates access to the messaging system, so the rest of the application does not depend on messaging-specific code. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingGateway.html)
- **Messaging Mapper:** Moves data between domain objects and the messaging infrastructure while keeping the two independent of each other. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingMapper.html)
- **Transactional Client:** A client controls its transactions with the messaging system. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/TransactionalClient.html)
- **Polling Consumer:** The consumer asks a channel for the next message when it is ready, so it decides when to take work. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PollingConsumer.html)
- **Event-Driven Consumer:** The consumer receives messages automatically as they become available. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventDrivenConsumer.html)
- **Competing Consumers:** Several consumers read from one channel, so the channel's messages are processed concurrently. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html)
- **Message Dispatcher:** Coordinates the message processing of several consumers on a single channel. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageDispatcher.html)
- **Selective Consumer:** The consumer filters which messages it receives from its channel. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageSelector.html)
- **Durable Subscriber:** The messaging system saves messages published while a subscriber is disconnected and delivers them when the subscriber reconnects. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DurableSubscription.html)
- **Idempotent Receiver:** Handles the same message more than once without repeating its effect. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html)
- **Service Activator:** Connects the messages on a channel to a service, so the service can be invoked through messaging and through non-messaging techniques. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingAdapter.html)

**System management**

- **Control Bus:** Uses the same messaging mechanism but separate channels to carry data for managing the components involved in the message flow. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ControlBus.html)
- **Detour:** A router that sends messages through additional steps, for example for validation, testing or debugging, when instructed to, and directly to the destination otherwise. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Detour.html)
- **Wire Tap:** Inserts a recipient list into a point-to-point channel so each message also goes to a secondary channel, which makes it possible to inspect the messages. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/WireTap.html)
- **Message History:** A list of all applications the message passed through since its origin. It helps to analyze and debug message flows. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageHistory.html)
- **Message Store:** Sends a duplicate of each message to a special channel that stores it centrally, so you can report on messages without disturbing the system. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageStore.html)
- **Smart Proxy:** Stores the return address supplied by the requestor and replaces it with its own, so replies pass through the proxy and can be tracked. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/SmartProxy.html)
- **Test Message:** Test messages are sent to a component to check the health of its message processing. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/TestMessage.html)
- **Channel Purger:** Removes stray messages that are left on a channel, such as a leftover reply from an earlier test run. [Official page](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelPurger.html)

## Example

An online shop has an order application and a shipping application. The order application puts each new order on a Point-to-Point Channel. Two shipping workers read from that channel, so each order goes to only one worker. If an order cannot be delivered, it lands in a Dead Letter Channel, where staff can inspect it.

## Trade-offs

Messaging is asynchronous, so the sender does not wait for the receiver. Delivery is meant to be reliable.
