---
title: Message Translator
slug: message-translator
category: integration
kind: pattern
summary: A Message Translator is a special filter that converts messages from one data format to another.
  It lets systems with different formats communicate through messaging.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- canonical-data-model
- normalizer
- content-enricher
- content-filter
- pipes-and-filters
- messaging
- message-channel
- envelope-wrapper
checks:
- Where applications use different data formats, the document names a translator step between them.
- If a common message format is used, it is independent of any specific application.
- The choice of a canonical model considers how many applications exchange messages.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html
  title: Message Translator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html
  title: Canonical Data Model - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Normalizer.html
  title: Normalizer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/4.22.x/eips/message-translator.html
  title: 'Message Translator :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A translator converts the sender's format into the receiver's format.
review:
  status: generated
  flags: []
---

## Explanation

Systems often use different data formats. When they exchange messages (see Messaging), the receiver may not understand what the sender produced. The Message Translator solves this problem.

The solution is a special filter. You place the translator between other filters or applications. It converts one data format into another. This puts it in a pipes-and-filters arrangement (see Pipes and Filters).

**Common format.** A translator often works together with a Canonical Data Model. This is a shared message format that belongs to no single application. Every application produces and consumes messages in that format. The model minimizes dependencies between applications that use different formats.

**Related patterns.**
- Normalizer: handles messages that mean the same thing but arrive in different formats. It uses a router to send each message to the right translator.
- Content Enricher and Content Filter: listed as related patterns.
- Channel Adapter, Message Channel and Message Endpoint: also listed as related.

**In tools.** Apache Camel supports this pattern. It can use data formats that marshal and unmarshal messages in different encodings. In plain terms, it turns a message into an encoding and back again.

## Example

A web shop sends orders in one layout. The warehouse system expects a different layout. A translator sits between them. It receives each order, converts it to the warehouse layout, and passes it on. A second shop later joins with a third layout. The team adds another translator for it.

## Trade-offs

A shared canonical model pays off as the number of applications grows. With only a few applications, it is overhead.
