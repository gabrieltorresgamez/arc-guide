---
title: Normalizer
slug: normalizer
category: integration
kind: pattern
summary: A Normalizer handles messages that mean the same thing but arrive in different formats. A router
  sends each message to a matching translator, so later steps deal with only one format.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- message-translator
- content-based-router
- canonical-data-model
- message-routing
- format-identifier
- invalid-message-channel
- dead-letter-channel
- messaging-pattern-language
checks:
- The document names the formats that arrive and states which translator handles each one.
- The document explains how the router detects the format of each message, including messages with no
  explicit type.
- The document names the common target format that all translators produce.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Normalizer.html
  title: Normalizer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html
  title: Message Translator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html
  title: Canonical Data Model - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/biztalk/esb-toolkit/message-transformation-patterns
  title: Message Transformation Patterns - BizTalk Server | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A router sends each message to the translator for its format. All translators output the same
    common format.
review:
  status: generated
  flags: []
---

## Explanation

Sometimes several senders report the same kind of information, but each uses its own format. The messages are semantically equivalent: they carry the same meaning. Only their shape differs.

The Normalizer solves this by sending each message type through its own custom translator. It has two parts:

- A **router** that looks at each incoming message and picks the right translator. See Content-based Router and Message Routing.
- One **translator** per format. A translator converts data from one format into another, so systems with different formats can communicate by messaging. See Message Translator.

The router must be able to detect what type a message is. That is easy when the message states its type. It is harder when it does not, for example with XML that has no schema, or with CSV. Then you need more general ways to identify the format.

The Canonical Data Model is a related idea. Every application produces and consumes one common format, so applications depend less on each other's formats. A Normalizer can be seen as a way to bring incoming messages into such a shared format.

The pattern also appears in products. The BizTalk ESB Toolkit documents it as an extension of data model transformation. Its implementation uses a transformation service plus a resolver. The resolver picks the right map (the conversion rules) for each message type at runtime.

## Example

A company receives order notices from three partners. One sends XML, one sends CSV, and one sends a third format. The router inspects each notice and passes it to the XML, CSV, or third translator. Each translator outputs the same order format. The order system reads only that format.

## Trade-offs

A common format reduces the number of translators as more applications join. With only a few applications taking part, it can look overly complicated.

The router also has to recognize every format. When messages carry no explicit type, this needs more general detection methods.
