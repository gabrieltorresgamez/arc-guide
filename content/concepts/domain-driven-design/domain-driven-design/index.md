---
title: Domain-Driven Design
slug: domain-driven-design
category: domain-driven-design
kind: method
summary: Domain-Driven Design (DDD) is an approach for complex business software. It organizes messy domain
  logic into models built in software, evolved over time, and split into bounded contexts as the domain
  grows.
arc42:
- 4
- 5
- 8
- 12
step: s06-domain
related:
- bounded-context
- ubiquitous-language
- context-map
- ddd-modeling-elements
- aggregate
- domain-model
- evolutionary-domain-modeling
- business-domain-understanding
checks:
- The document names the domain experts' terms and uses them consistently.
- Where terms mean different things to different groups, the document makes the conflicting meanings explicit
  in separate models.
- For a large domain, the document splits the model into bounded contexts instead of one unified model.
- The document describes how the bounded contexts relate to each other.
- Each bounded context has its own self-contained domain model made of aggregates.
sources:
- url: https://martinfowler.com/bliki/DomainDrivenDesign.html
  title: Domain Driven Design
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://ozimmer.ch/modeling/2022/11/23/ContextMapperInsights.html
  title: Domain-Driven Design in Practice — Experience with Context Mapper
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Two bounded contexts, each with its own self-contained model, related to each other.
review:
  status: generated
  flags: []
---

## Explanation

Domain-Driven Design, or DDD, takes its name from a 2003 book by Eric Evans. The book presents the approach as a catalog of patterns.

DDD suits complex domains. These are business areas with a lot of messy logic that someone must organize. The "domain" is the business area the software serves. A "domain model" is the organized description of that area.

**Built in software, evolved over time.** DDD stresses building domain models in software. It also stresses evolving them during the life of the product. See Iterative Domain Modeling.

**A shared language.** A core tenet is to pick up the language of the domain experts. The team then uses that language consistently. See Ubiquitous Language.

**Why explicit models matter.** The same term can mean different things to different people. Conversation can smooth over these differences. Software cannot, because computers are precise. DDD responds by dividing the domain into Bounded Contexts, each with its own unified model.

**Strategic design.** A single unified model gets harder to build as the domain grows. Strategic design deals with large models and teams. Its focus is the Bounded Context. Strategic design also describes several ways to relate bounded contexts to one another. See Context Map.

**Tactical design.** Within an application, tactical DDD is described as a modern, mature approach to object-oriented analysis and design. See DDD Building Blocks (Tactical Patterns) and Aggregate.

## Example

A company sells and ships products. Sales staff use "customer" for someone who placed an order. Billing staff use "customer" for whoever pays the invoice. These can be different people.

In conversation, this goes unnoticed. In software, the team must pick precise meanings. So the team splits the domain into two bounded contexts, one for sales and one for billing. Each context gets its own model of "customer" in the experts' own words. The team then decides how the two contexts relate.

## Trade-offs

DDD is particularly suited to complex domains.
