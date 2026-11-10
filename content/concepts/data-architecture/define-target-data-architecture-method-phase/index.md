---
title: Define Target Data Architecture Method Phase
slug: define-target-data-architecture-method-phase
category: data-architecture
kind: method
summary: This phase defines the major data types and data sources a business needs. It works at the level
  of data entities, not storage design. Its results feed matrices, gap analysis and arc42 documentation.
arc42:
- 3
- 8
step: s08-integration-data
related:
- data-architecture
- togaf-architecture-development-method
- data-entity-business-function-matrix
- arc42-crosscutting-concepts
- arc42-context-and-scope
- data-architecture-documentation-in-arc42
- logical-data-model
- domain-model
checks:
- The data architecture describes data entities, not logical or physical storage design.
- A Data Entity/Business Function matrix shows which data supports which functions and which function
  owns which data.
- A gap matrix is created using the TOGAF Gap Analysis technique.
- The business or domain data model appears in arc42 section 8 as a cross-cutting concept.
- The business context shows which data is exchanged with external partners.
sources:
- url: https://www.opengroup.org/architecture/doc-review/protected-d3/htmlclean/chap10.html
  title: 'The Open Group Architecture Framework (TOGAF) - Phase C: Information Systems Architectures -
    Data Architecture'
  site: opengroup.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/8-5/
  title: 'Tip 8-5: Document business or domain models! | arc42 Documentation'
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

The phase matches TOGAF's Phase C Data Architecture (see the articles on TOGAF and the TOGAF Architecture Development Method). Its goal is to define the major data types and sources the business needs.

The focus is on data entities, meaning the kinds of things the enterprise keeps data about. The phase does not design logical or physical storage systems.

**Matrices**

- The Data Entity/Business Function matrix shows which data supports which business functions. It also shows which function owns which data.
- The System/Data matrix is developed across both the Application Architecture phase and the Data Architecture phase.

**Use in arc42**

- Business or domain data models belong in arc42 section 8, the cross-cutting concepts. Many building blocks refer to them.
- For the data concept, arc42 accepts a domain model in the style of Domain-Driven Design. Without that style, a business or logical data model is the simpler option.
- The business context in section 3 shows which data is exchanged with the environment.

## Example

A retailer lists its main data entities: customer, order and product. It records which business function owns each one. The sales function might own orders, for example, while the support function only uses them. The team then notes which entities an external payment partner receives. That note goes into the business context. The shared entity descriptions go into the cross-cutting concepts section.

## Trade-offs

A Domain-Driven Design model is statically and dynamically expressive, while a business or logical data model covers only the more static aspects of the domain. Without that style, the plain model is the simpler choice. Working at the entity level also means the effort is not concerned with database design.
