---
title: Domain Model
slug: domain-model
category: domain-driven-design
kind: concept
summary: A domain model is a system of abstractions that describes selected aspects of a business domain.
  Software is built on it, and teams evolve it in code over the product's life.
arc42:
- 4
- 5
- 8
- 12
step: s06-domain
related:
- domain-driven-design
- ubiquitous-language
- entity
- value-object
- aggregate
- ddd-modeling-elements
- evolutionary-domain-modeling
- bounded-context
checks:
- The document states which aspects of the domain the model covers.
- The Ubiquitous Language is based on the domain model used in the software.
- The model is implemented in software and has a way to evolve over the product's life.
- Domain experts can challenge awkward terms, and the model is refined in response.
sources:
- url: https://en.wikipedia.org/wiki/Domain-driven_design
  title: Domain-driven design - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/DomainDrivenDesign.html
  title: Domain Driven Design
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/eaaCatalog/domainModel.html
  title: Domain Model
  site: martinfowler.com
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

A domain is the business area a software system serves. A domain model describes only chosen aspects of that area. It does not try to copy everything. It is a system of abstractions, meaning simplified ideas that stand in for real things.

Domain-Driven Design (see the article "Domain-Driven Design") centers development on a rich domain model. "Rich" means the model understands the processes and rules of the domain. Software systems should rest on a well-developed model of this kind.

In one common definition, a domain model is an object model of the domain. It combines behavior and data in one place.

**Shared language.** The Ubiquitous Language embeds domain terminology into the software. It should be based on the domain model used in the software. See the article "Ubiquitous Language".

**Models live in software.** DDD stresses implementing models in software. It also stresses evolving them during the life of the product. The model is not a one-time document.

**Refinement with experts.** Domain experts should speak up when a term or structure feels awkward or does not fit. Their objections show where the model does not yet express what they know about the domain.

**Building blocks.** Several building blocks turn a model into software structure:

- An entity is defined by its identity, not by its attributes. See "Entity".
- A value object is immutable and has no conceptual identity. See "Value Object".
- Models can be bound together by a root entity into an aggregate. See "Aggregate".

## Example

A team builds software for a library. Staff talk about "members" and "loans". The team puts Member and Loan into the model and uses the same words in the code. A member is an entity: the same person stays the same member even if their details change. A due date is a value object: it has no identity of its own. A librarian says the word "borrower" is confusing. The team renames the concept, and the model gets clearer.

## Trade-offs

A model covers only selected aspects of a domain.
