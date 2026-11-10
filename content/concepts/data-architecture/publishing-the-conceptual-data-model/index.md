---
title: Publishing the Conceptual Data Model
slug: publishing-the-conceptual-data-model
category: data-architecture
kind: practice
summary: Publishing the conceptual data model makes it available to everyone as a shared glossary. Someone
  must own it, and it must change as the team's understanding of the domain grows.
arc42:
- 12
step: s06-domain
related:
- conceptual-data-model
- arc42-glossary
- ubiquitous-language
- conceptual-data-model-building-method
- data-architecture
- domain-model
- conceptual-vs-logical-vs-physical-data-model
- conceptual-data-model-preparation-for-logical-and-physical-models
checks:
- A named role, such as the product owner or project manager, is responsible for the glossary.
- The glossary lists the key domain and technical terms stakeholders use when discussing the system.
- The published model and glossary are updated as the team's understanding of the domain grows.
sources:
- url: https://docs.arc42.org/section-12/
  title: 12 - Glossary | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UbiquitousLanguage.html
  title: Ubiquitous Language
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

See the article Conceptual Data Model.

The arc42 glossary (section 12) holds the key domain and technical terms that stakeholders use when they talk about the system. See the articles arc42 Glossary and Ubiquitous Language.

Two points matter here.

**Ownership.** arc42 suggests making the product owner or project manager responsible for the glossary.

**Change over time.** As the team learns more about the domain, the ubiquitous language and the model should change with it.

## Example

A team finishes its model of an online shop with the terms Customer, Order and Product. It publishes the model where all teams can find it. It names the product owner as the person responsible. Later the team learns that "Order" and "Delivery" are different things. The owner updates the model and the glossary together, so everyone sees the same terms again.

## Trade-offs

This article does not cover publishing channels, tools or training.
