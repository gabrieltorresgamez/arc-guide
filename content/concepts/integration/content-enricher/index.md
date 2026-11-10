---
title: Content Enricher
slug: content-enricher
category: integration
kind: pattern
summary: A Content Enricher adds data that a receiver needs but the sender lacks. A Content Filter does
  the opposite and removes data the receiver does not need. Both reshape messages to fit the receiver.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- message-translator
- message-filter
- content-filter
- envelope-wrapper
- claim-check
- canonical-data-model
- messaging-pattern-language
- pipes-and-filters
checks:
- Where a receiver needs data the sender does not hold, the document names an enrichment step that supplies
  it.
- Where receivers need only a few items from a large message, the document names a filtering step that
  removes the rest.
- Where enrichment calls another source through Camel's Enrich EIP, the document states the producer cache
  setting.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DataEnricher.html
  title: Content Enricher - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentFilter.html
  title: Content Filter - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/4.22.x/eips/enrich-eip.html
  title: 'Enrich :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A message gains missing data in the enricher, then loses unneeded data in the filter.
review:
  status: generated
  flags: []
---

## Explanation

Systems exchange messages, which are packages of data sent between applications. A receiver often needs more information than the sender provides. Two patterns fix this in opposite directions.

**Content Enricher.** It handles the case where the sender does not have all the data items the receiver requires. The enricher adds the missing items to the message before it moves on.

An enricher can get the missing data in several ways, including:

- It computes the missing data itself and needs no external source. This form is very similar to a Message Translator.
- It fetches the data from another system, which is the most common source. Apache Camel's Enrich EIP is one example. It uses a producer to obtain the data. Camel caches producers for reuse. You can set the cache size or turn the cache off.

**Content Filter.** It handles the opposite problem. A message is large, but the receiver cares about only a few items. The filter strips the unimportant items and keeps the important ones. The pattern description notes that surprisingly many situations call for removing data.

The two patterns are mirror images. One grows a message. The other shrinks it.

## Example

An order system sends a message with a customer ID and a list of items. A shipping system needs the customer's delivery address, which the order system does not hold. An enricher gets the address and adds it to the message.

The same message also carries many order details that shipping ignores. A filter removes them. Shipping receives a smaller message with only what it needs.

## Trade-offs

In Camel, the Enrich EIP uses a producer, and you can tune or disable its producer cache, so caching is a setting you can choose.
