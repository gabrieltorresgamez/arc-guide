---
title: Interoperability
slug: interoperability
category: quality-attributes
kind: quality-attribute
summary: Interoperability is how well separate systems can exchange information and then use it. It depends
  on shared formats and shared meaning. Open standards help, and translators bridge the gaps that remain.
arc42:
- 3
- 8
- 10
step: s08-integration-data
related:
- compatibility
- message-translator
- iso-iec-25010-quality-model
- interoperability-scenario
- canonical-data-model
- integration
- format-identifier
- datatype-channel
checks:
- The document states which formats or representations each interface uses, and how the parties agree
  on them.
- Where two systems use different data formats, the document names the translator that converts between
  them.
- Where systems must interpret exchanged data meaningfully, the document names the common reference model
  both sides use.
- Interoperability is documented separately from co-existence, as two sub-characteristics of compatibility.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Interoperability
  title: Interoperability - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html
  title: Message Translator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation
  title: Content negotiation - HTTP | MDN
  site: developer.mozilla.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A translator converts data between two systems that use different formats.
review:
  status: generated
  flags: []
---

## Explanation

Interoperability is the degree to which systems, products or components can exchange information and use what they received. ISO/IEC 25010 places it under compatibility, next to co-existence. Co-existence is a different idea: it covers sharing one environment and its resources efficiently. (See the article Compatibility.)

**Two kinds of agreement**

Exchanging data is not enough. Both sides must also understand it.

- **Format agreement.** Both sides must handle the same data representation. In HTTP content negotiation, a server can serve different representations of one resource. In the standard server-driven form, the client sends headers describing its preferences, and the server uses them as hints to choose a representation. The client's Accept header lists the MIME types the client is willing to process, each with a quality factor showing relative preference.
- **Meaning agreement.** Semantic interoperability means a system interprets received information meaningfully and accurately. This needs a common reference model that both sides refer to.

**Standards help**

Standards bodies publish open specifications to make interoperability easier. Products that implement a common protocol defined in an open standard are interoperable by design. However, being open is necessary but not sufficient for a standard to be an interoperability standard.

**When formats differ**

Sometimes two systems use different data formats. A Message Translator can sit between them and convert one format into the other. It answers a specific problem: how can systems with different data formats communicate through messaging? (See the article Message Translator.)

## Example

A web shop sends orders to a warehouse system. The shop produces JSON, but the warehouse reads only XML. A translator between them converts each order from one format to the other. The two systems also need a shared meaning for each field. Both must agree, for example, on what "quantity" counts. A common reference model records that agreement.
