---
title: Iterative Domain Modeling
slug: evolutionary-domain-modeling
category: domain-driven-design
kind: practice
summary: Iterative domain modeling means a domain model starts simple and improves over time. The team
  builds it in code, learns more about the domain, and revises model and code together.
arc42:
- 4
- 8
- 12
step: s06-domain
related:
- domain-driven-design
- domain-model
- ubiquitous-language
- refactoring
- iterative-and-incremental-development
- cargo-shipping-domain-model-example
- entity-life-cycle
- business-domain-understanding
checks:
- The documentation states that the domain model evolves as the team's understanding grows, rather than
  being fixed up front.
- The team's shared language is based on the domain model used in the software.
- The domain model is tied to its implementation in code.
sources:
- url: https://www.dddcommunity.org/wp-content/uploads/files/books/evans_pt03.pdf
  title: III
  site: dddcommunity.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/DomainDrivenDesign.html
  title: Domain Driven Design
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/refactoring-deeper-model/
  title: Refactoring to a Deeper Model - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UbiquitousLanguage.html
  title: Ubiquitous Language
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The model is built, learned from, and refactored in a loop together with the code.
review:
  status: generated
  flags: []
---

## Explanation

A domain model describes the business area a software system serves. Teams often want to design it fully on paper first and build it afterward. Domain-Driven Design (see the article Domain-Driven Design) takes a different view. It evolves the model in software during the life of the product.

**Why the first model is not the final one.** Initial models are usually naive and superficial. They rest on shallow knowledge, so they need to be improved.

**How the model grows.** The team's understanding of the domain deepens, and the model and its shared language should change with it. See the article Ubiquitous Language. In one shipping example, months of work with domain experts and many iterations produced a quite different model from the starting one.

**Breakthroughs.** Repeated refactoring toward deeper insight can lead to a breakthrough. Chapter 8 of Evans's book tells such a project story. Refactoring means changing the structure of code step by step. See the article Refactoring.

**Model and code stay tied together.** Because model and design are closely related, the modeling process comes to a halt when the code is hard to refactor. The team's language is based on the model used in the software. A project case shows this: as the team added domain logic, the code used more of the shared language.

## Example

A team builds a simple model of a clinic: a patient has appointments. They put it in code and release it. Later, talks with clinic staff show a different picture of the work. The team renames concepts, reshapes the code, and updates the shared vocabulary together. After several rounds, the model looks quite different from the first version, and the code still reads like the model.

## Trade-offs

One risk is that modeling comes to a halt when the code is hard to refactor.
