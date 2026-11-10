---
title: Patterns for API Design
slug: patterns-for-api-design
category: integration
kind: framework
summary: Patterns for API Design is a pattern language for remote APIs. It sorts patterns into five categories
  and treats each choice as a decision with options and criteria. Its focus is the messages that APIs
  exchange.
arc42:
- 4
- 8
- 9
step: s08-integration-data
related:
- architectural-decision
- message-structure
- integration
- architectural-pattern
- messaging-pattern-language
- microservices-architecture
- loose-coupling
- architectural-decision-record
checks:
- API design choices, such as pagination or rate limiting, are recorded as decisions with options and
  criteria.
- Each API endpoint has a stated role, for example Processing Resource or Information Holder Resource.
- The document states how long clients can rely on a published API version.
sources:
- url: https://microservice-api-patterns.org/
  title: Patterns for API Design
  site: microservice-api-patterns.org
  accessed: '2026-11-09'
- url: https://www.ozimmer.ch/patterns/2022/12/16/APIPatternsBookWebsite.html
  title: API Patterns Website Redesigned and Sample Book Chapter Available
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://microservice-api-patterns.org/book/
  title: Our Book "Patterns for API Design"
  site: microservice-api-patterns.org
  accessed: '2026-11-09'
- url: https://microservice-api-patterns.org/patterns/
  title: Pattern Index
  site: microservice-api-patterns.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The five categories of the pattern language, with example patterns.
review:
  status: generated
  flags: []
---

## Explanation

A pattern language is a set of related patterns that work together. This one covers the design of remote APIs. Its online home is the Microservice API Patterns (MAP) site. MAP focuses on message representations, meaning the payloads exchanged when a client calls an API. The structures you choose for these messages strongly shape the API's qualities, both at design time and at runtime.

**How the book is organized**

The book has two parts. The first covers fundamentals: a domain model and a decision model. The second presents 44 patterns in Chapters 4 to 9, grouped into five theme categories. Thirty of the 44 patterns were peer-reviewed and published in papers before the book appeared.

The decision model identifies pattern selection questions, with options and criteria. The book's decision narratives identify 29 recurring decisions. The book's Chapter 2 covers these decisions.

**The five categories**

- **Foundation:** the first category of the language.
- **Responsibility:** defines endpoint roles. Processing Resource lets clients trigger an action in the provider. Information Holder Resource exposes domain data and hides how it is implemented.
- **Structure:** covers message structure. Parameter Tree expresses containment. Id Element tells API elements apart at design time and at runtime.
- **Quality:** includes Pagination, which delivers large data sequences without overwhelming clients. Rate Limit stops clients from using the API excessively. Wish List is also in this category.
- **Evolution:** includes Limited Lifetime Guarantee, which tells clients how long they can rely on a published API version.

## Example

A team builds an API for an online shop. They give the order list the role of an Information Holder Resource, because it exposes data. They give "cancel order" the role of a Processing Resource, because it triggers an action. Next they ask the quality questions. Should the order list use Pagination? Should the API apply a Rate Limit? Last, they ask an evolution question: how long will version 1 stay available? They write each answer down as a decision with its options and reasons.

## Trade-offs

Message structure choices influence both design-time and runtime qualities. Weigh each decision against its criteria and record the result.
