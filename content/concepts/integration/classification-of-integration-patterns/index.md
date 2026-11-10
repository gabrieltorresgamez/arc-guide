---
title: Software Connector Classification
slug: classification-of-integration-patterns
category: integration
kind: framework
summary: Connector classification compares integration styles on shared questions, such as synchronous
  or asynchronous and one-to-one or one-to-many. The answers show how each style behaves when a side is
  down or an interface changes.
arc42:
- 3
- 5
- 8
step: s08-integration-data
related:
- software-connector
- synchronous-vs-asynchronous-connector
- connector-cardinality
- connector-transparency
- file-transfer
- shared-database
- remote-procedure-call
- messaging
checks:
- For each integration, the document states whether the exchange is synchronous or asynchronous.
- For each synchronous call, the document says what happens when the callee is unavailable.
- Where one message must reach several receivers, the document names this one-to-many link.
- Where interfaces differ between systems, the document says where messages are transformed.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Messaging.html
  title: Messaging - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Integration styles are ways to let separate applications work together. Comparing them on the same questions makes the differences easier to see.

**Synchronous or asynchronous.** In a synchronous call, the caller waits while the callee works. In asynchronous exchange, the sender does not wait for the receiver.

**Sharing data.** In file transfer, each application writes files of shared data and reads files that others wrote. In a shared database, applications store the data they want to share in a common database. See File Transfer and Shared Database.

**Broadcast.** Messaging can broadcast messages to multiple receivers.

**Reliability.** A synchronous call assumes the callee is available when called. If side B is down, the call has a problem. With asynchronous messaging, both systems do not need to be up at the same time. See Messaging.

**Adaptation.** Messaging can transform messages in transit. Neither sender nor receiver knows this happens.

Use these questions as a checklist. Ask the same ones of every candidate style.

## Example

A shop system must tell a billing system about new orders. With a synchronous call, the shop waits for billing to answer. If billing is down, the order step is stuck. With asynchronous messaging, the shop sends the message and moves on. Billing reads it when it is back.

## Trade-offs

Computer processing is typically synchronous, and a synchronous call assumes the callee is available. Asynchronous messaging removes that need and allows in-transit changes and broadcast. Judge the effort and cost of each style for your own case.
