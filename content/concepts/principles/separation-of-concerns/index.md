---
title: Separation of Concerns
slug: separation-of-concerns
category: principles
kind: principle
summary: Separation of concerns means studying one aspect of a problem on its own while staying aware
  of the others. In software, it means splitting an application by responsibility so the code stays organized
  and manageable.
arc42:
- 4
- 5
- 8
step: s07-solution-strategy
related:
- layered-architecture
- layers-pattern
- clean-architecture
- microservices-architecture
- modularity
- information-hiding
- coupling-and-cohesion
- concern
checks:
- The building block view divides the system by responsibility, such as UI, business logic and data access.
- The document states which layers may communicate with which, for example UI only with the business layer.
- If dependencies are inverted, the document shows business logic at the center with other parts depending
  on it.
- Where the system is split into separate services, the document justifies the added overhead, for example
  with independent feature slices.
sources:
- url: https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html
  title: 'E.W. Dijkstra Archive: On the role of scientific thought (EWD447)'
  site: cs.utexas.edu
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures
  title: Common web application architectures - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Three layers, each with one responsibility. Each layer talks only to the one below it.
review:
  status: generated
  flags: []
---

## Explanation

A complex problem has many aspects at once. Separation of concerns is the habit of looking at one aspect in depth, on its own terms, so it can be made consistent. Dijkstra sometimes called this technique "the separation of concerns".

Isolation does not mean ignoring the rest. You stay focused on one aspect and aware of the others at the same time. Dijkstra described this as being one-track and multiple-track minded simultaneously.

**In software.** The same idea breaks an application up by its responsibilities, or concerns. This helps manage growing complexity. It also keeps the codebase organized, so developers can find where a given function lives.

**Layers.** The classic example is three layers:

- the user interface (UI),
- the business logic layer (BLL), and
- the data access layer (DAL).

Each has a well-known responsibility. The UI talks only to the business layer. The business layer reaches data through the data access layer. Layering can also restrict which layers may talk to each other. This gives encapsulation, meaning a layer's inner workings stay hidden. A change then affects mainly the neighboring layers. See the articles Layered Architecture and Layers Pattern.

**Clean Architecture.** This style inverts the usual dependencies. Business logic sits in the center. Infrastructure and UI depend on it, so dependencies point inward. See the article Clean Architecture.

**Easier replacement and testing.** Separated layers make it easier to replace an implementation. You can swap the persistence layer, or use fakes in tests.

## Example

An online shop keeps three concerns apart. The screens show products and take orders. A business layer holds the rules, such as how a discount is calculated. A data layer reads and writes the stored records. The team later replaces the database. Only the data layer changes. In tests, a fake data layer stands in for the real one, so the discount rules can be checked on their own.

## Trade-offs

Splitting things up has a cost. Moving parts into separate processes or services (see Microservices Architecture) adds overhead and complexity. Without features that can vary independently, that cost is not worth paying.
