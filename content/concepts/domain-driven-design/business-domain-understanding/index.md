---
title: Business Domain Understanding
slug: business-domain-understanding
category: domain-driven-design
kind: practice
summary: Business domain understanding means architects and stakeholders share one clear picture of the
  business and its terms. Where meanings truly differ, bounded contexts keep each meaning in its own place.
arc42:
- 3
- 12
step: s06-domain
related:
- ubiquitous-language
- bounded-context
- domain-model
- domain-driven-design
- arc42-glossary
- arc42-context-and-scope
- system-idea-and-vision-elements
- context-map
checks:
- The glossary lists the key domain and technical terms that stakeholders use when discussing the system.
- Terms with several meanings, such as Customer or Product, are identified and explained.
- Where meanings differ between parts of the organization, the document separates them into bounded contexts.
- The business context describes the domain interfaces and the data exchanged with the environment in
  a way all stakeholders can understand.
sources:
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UbiquitousLanguage.html
  title: Ubiquitous Language
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-12/
  title: 12 - Glossary | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Business domain understanding is a shared picture of the business area a system serves. The picture rests on common terms that everyone uses in the same way.

**Terms drift apart in large organizations.** Different groups use slightly different vocabularies. The same word can mean different things in different parts of the organization. Words like "Customer" and "Product" are typical examples. They have several meanings and cause confusion again and again.

**Language is a tool for testing understanding.**
- Domain experts should object when a term or structure feels awkward or inadequate. Using the language with domain experts helps test the model.
- Developers should watch for ambiguity or inconsistency in the language. Such gaps will trip up the design.
- The language and the model should change as the team learns more about the domain.

**When meanings really differ.** Domain-driven design (see Domain-Driven Design) divides a large system into bounded contexts. Each bounded context can have its own unified model, so a term keeps one clear meaning inside it. See Bounded Context for details.

**Where to record it in arc42.** The arc42 glossary (see arc42 Glossary) lists the most important domain and technical terms stakeholders use when they discuss the system. The context and scope section calls domain and technical interfaces to communication partners among the system's most critical aspects. All stakeholders should understand the data the system exchanges with its environment (see arc42 Context and Scope).

## Example

A company has a sales team and a billing team. Both say "Customer". For sales, it means a person who might buy. For billing, it means a party with a signed contract. The architect notices the gap when the two groups describe the same system. The team splits the system into two bounded contexts, each with its own definition of "Customer". They write both meanings in the glossary.

## Trade-offs

Keeping several meanings of one term, each in its own bounded context, reflects that total unification of the domain model for a large system is not feasible or cost-effective. The language and model keep changing as understanding grows.
