---
title: Module
slug: module
category: domain-driven-design
kind: pattern
summary: A module groups related domain concepts so people can understand one group at a time. Choose
  modules by meaning, not by technical category, and give them names the whole team uses.
arc42:
- 5
- 8
- 12
step: s06-domain
related:
- bounded-context
- ubiquitous-language
- coupling-and-cohesion
- high-cohesion
- domain-model
- modularity
- cargo-shipping-domain-model-example
- package-diagram
checks:
- Module names appear in the glossary and the team uses them as part of its shared vocabulary.
- Modules are grouped by concepts of the domain, not by technical aspects or developer work assignments.
- Each module holds a cohesive set of concepts, and the module list tells the story of the system.
- Coupling between modules is judged by whether concepts can be understood independently.
sources:
- url: http://uniknow.github.io/AgileDev/site/0.1.8-SNAPSHOT/parent/ddd/core/modules.html
  title: Domain Driven Design - Modules
  site: uniknow.github.io
  accessed: '2026-11-09'
- url: https://herbertograca.com/2015/09/29/domain-driven-design-by-eric-evans-chap-5-a-model-expressed-in-software/
  title: DDD.5 – A model expressed in software – @hgraca
  site: herbertograca.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A person can only think about a limited number of things at once. Modules respond to that limit. They split a large model into smaller groups, so you can reason about one group without holding the rest in your head.

Modules divide concepts, not just code. Code often gets split by technical aspects of the architecture or by developer work assignments. Module guidance pushes against this. The question is not "who works on this?" but "which ideas belong together?"

Two rules guide the choice:

- **High cohesion.** Each module holds a set of concepts that fit together. (See the articles High Cohesion and Coupling and Cohesion.)
- **Low coupling.** Modules depend on each other as little as possible. Here, low coupling means concepts you can understand and reason about independently. It is not only a code metric.

Pick modules that tell the story of the system. A reader who sees the module names should learn what the system is about.

Module names should also enter the ubiquitous language, the shared vocabulary of the team (see the article Ubiquitous Language). If people say "Billing" in conversation and the structure says the same, the two match.

Domain-Driven Design also divides large models into bounded contexts with explicit relationships (see the article Bounded Context).

When you implement a domain model, conceptual clarity comes before technical complexity.

## Example

A team builds a system for shipping goods. One option splits the code into "data access," "services," and "screens." Every business idea is then spread across all three. Another option creates modules named after business ideas: "Customer," "Billing," and "Shipping." Each module holds the concepts that belong together. The names are short, the team uses them in conversation, and a newcomer learns what the system does by reading them.

## Trade-offs

The sources say conceptual clarity should come before technical complexity. If modules end up highly coupled, the sources suggest rethinking and clarifying the domain model.
