---
title: Messaging Protocol Support in Message Brokers
slug: messaging-systems-and-protocols
category: integration
kind: concept
summary: Message brokers speak different wire protocols, the formats clients use to talk to them. Some
  brokers support several protocols natively or through plugins. Protocol support decides which clients
  can connect.
arc42:
- 3
- 9
- 8
step: s08-integration-data
related:
- messaging
- interoperability
- broker-pattern
- publish-subscribe-pattern
- integration-patterns-vs-middleware-technology
- software-connector
checks:
- The document names each wire protocol that clients use to reach the broker.
- The document states which AMQP version is meant, since 1.0 and 0-9-1 differ on the wire.
- The document lists the supported protocol versions, such as MQTT 3.1.1 or 5.
sources:
- url: https://www.rabbitmq.com/docs/protocols
  title: Which protocols does RabbitMQ support? | RabbitMQ
  site: rabbitmq.com
  accessed: '2026-11-09'
- url: https://artemis.apache.org/components/artemis/documentation/latest/protocols-interoperability.html
  title: Protocols and Interoperability
  site: artemis.apache.org
  accessed: '2026-11-09'
- url: https://docs.nats.io/learn/mqtt/
  title: Connect MQTT devices to NATS | NATS Documentation
  site: docs.nats.io
  accessed: '2026-11-09'
- url: https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
  title: MQTT Version 5.0 | OASIS Standard
  site: docs.oasis-open.org
  accessed: '2026-11-09'
- url: https://stomp.github.io/stomp-specification-1.2.html
  title: ''
  site: stomp.github.io
  accessed: '2026-11-09'
- url: https://github.com/streamnative/kop
  title: 'GitHub - streamnative/kop: Kafka-on-Pulsar - A protocol handler that brings native Kafka protocol
    to Apache Pulsar · GitHub'
  site: github.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A **wire protocol** is the set of rules for how a client and a broker exchange data over the network. When both sides share a protocol, they can work together. This is why protocol support matters when you choose a broker. For background, see the articles on Messaging and Interoperability.

**MQTT** is a lightweight client-server publish/subscribe protocol. Its designers made it light and simple to implement.

**STOMP** is a simple protocol with a text-based message format. Its design goals are simplicity and interoperability.

**AMQP** comes in two very different versions. AMQP 0-9-1 is binary and has strong messaging semantics. Semantics means clear rules about what each messaging operation does. AMQP 1.0 is a different protocol. It shares nothing with 0-9-1 on the wire. It asks less of a broker, so more brokers support it. It is also more complex and has fewer clients.

**Brokers that support several protocols:**
- RabbitMQ supports MQTT 3.1, 3.1.1 and 5.0 natively through a plugin. Its STOMP plugin works by proxying internally over AMQP 0-9-1.
- Apache Artemis accepts any AMQP 1.0 client. It also accepts MQTT 3.1, 3.1.1 and 5 clients.
- The NATS server speaks MQTT 3.1.1, including delivery levels 0, 1 and 2.

**Protocol handlers:** Pulsar can load protocol handlers as plugins. KoP is one. It adds Kafka wire protocol support to Pulsar.

## Example

A factory has sensors that only speak MQTT. The back-office systems use another protocol. The team picks a broker that accepts MQTT directly and also offers a protocol the back-office clients support. Both sides connect to the same broker without extra translation software.

## Trade-offs

A broker that supports a protocol lets existing clients connect without changes. But support can be indirect. RabbitMQ's STOMP plugin, for example, proxies over AMQP 0-9-1 internally. Choosing AMQP 1.0 gives you more broker choices, but it is more complex and has fewer clients than 0-9-1. Check which exact protocol versions a broker supports before you commit.
