---
title: Reflecting the Business Domain in the Architecture
slug: reflecting-the-business-domain-in-the-architecture
category: domain-driven-design
kind: principle
summary: Architecture works better when it follows the business domain. Teams use the business's own words,
  let domain experts correct those words, and split large domains into bounded contexts instead of forcing
  one model.
arc42:
- 4
- 5
- 12
step: s06-domain
related:
- ubiquitous-language
- bounded-context
- domain-driven-design
- domain-model
- context-map
- arc42-glossary
- deriving-system-components-from-the-domain-model
- business-domain-understanding
checks:
- Names of building blocks and terms in the documentation use the vocabulary of the business domain, and
  domain experts have reviewed them.
- Terms that stakeholders understand differently, such as Customer or Product, are identified and their
  meanings are written down.
- The domain is split into bounded contexts instead of one single unified model.
- The document shows how the shared language and model are updated as understanding of the domain grows.
- Team organization is aligned with the bounded contexts, taking Conway's law into account.
sources:
- url: https://martinfowler.com/bliki/UbiquitousLanguage.html
  title: Ubiquitous Language
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/ConwaysLaw.html
  title: Conway's Law
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A software system serves a business. If its names and structure follow the business domain, people on both sides understand each other more easily.

**Share one language.** The team and the domain experts agree on a common vocabulary (see Ubiquitous Language). Domain experts act as a check. They object when a term or structure poorly conveys what they know about the domain. The language is not fixed. It should change as the team's understanding of the domain grows, and the model should change with it.

**Watch for words with several meanings.** Terms such as Customer and Product often mean different things to different stakeholders. This confusion comes back again and again.

**Do not force one model on a big domain.** The larger the domain, the harder it is to build a single unified model. Bounded contexts address this. A bounded context (see Bounded Context) is a central Domain-Driven Design pattern for structuring systems around the domain.

**Link structure to teams.** Bounded contexts also group people around a subject matter. That lets the organization line up with the flow of value. This connects to Conway's law. The law matters because human communication enables software coupling. So it should influence how teams are organized.

## Example

A retailer's sales team uses "Customer" for a person who has placed an order. The billing team uses "Customer" for whoever pays the invoice. A discussion between both teams and the domain experts surfaces this difference. The team defines a Sales context and a Billing context. Each context defines "Customer" in its own terms and records that definition in a shared glossary.

## Trade-offs

Several contexts mean several models and several meanings of one word. Teams must then be explicit about how the contexts relate to each other. A single unified model is the alternative, but it gets harder to build as the domain grows, and total unification for a large system is not feasible or cost-effective.
