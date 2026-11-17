---
title: Conceptual Data Model
slug: conceptual-data-model
order: 30
category: data-architecture
kind: artifact
summary: A conceptual data model is a high-level description of the business information an organization
  needs. It leaves out database details. Logical modeling later turns it into a structured database design.
arc42:
- 3
- 8
- 12
step: s06-domain
related:
- logical-data-model
- conceptual-logical-and-physical-data-model
- physical-data-model
- data-architecture
- ddd-building-blocks-tactical-patterns
- domain-model
checks:
- The conceptual data model contains entities, attributes, relationships and business rules.
- The conceptual data model contains no database-specific concepts such as indexes, data types or storage
  details.
- The relationships in the model reflect business processes and rules.
sources:
- url: https://aisel.aisnet.org/ajis/vol4/iss2/7/
  title: '"Conceptual Data Modelling: an empirical study of expert and novice dat" by Graeme Shanks'
  site: aisel.aisnet.org
  accessed: '2026-11-09'
- url: https://airbyte.com/data-engineering-resources/conceptual-data-model
  title: 'What is Conceptual Data Modeling: Purpose & Examples | Airbyte'
  site: airbyte.com
  accessed: '2026-11-09'
- url: https://www.thoughtspot.com/data-trends/data-modeling/conceptual-vs-logical-vs-physical-data-models
  title: 'Conceptual vs Logical vs Physical Data Models: Key Differences'
  site: thoughtspot.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model
  title: Entity–relationship model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-12/
  title: 12 - Glossary | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UbiquitousLanguage.html
  title: Ubiquitous Language
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://aws.amazon.com/compare/the-difference-between-logical-and-physical-data-model/
  title: Logical vs Physical Data Model - Difference in Data Modeling - AWS
  site: aws.amazon.com
  accessed: '2026-11-09'
- url: https://www.red-gate.com/blog/conceptual-logical-and-physical-data-model/
  title: How to Implement a Conceptual, Logical, and Physical Data Model in Redgate Data Modeler
  site: red-gate.com
  accessed: '2026-11-09'
- url: https://www.ewsolutions.com/conceptual-data-modeling-starts-with-business-use-cases/
  title: 'Conceptual Data Model: Building a Business-Driven Data Model'
  site: ewsolutions.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'Small conceptual model: three entities with named relationships and no database details.'
review:
  status: generated
  flags: []
---

## Explanation

Conceptual data modeling is the process of creating a high-level picture of business information requirements. It describes the information the business needs, not how a database stores it [src:3].

The core elements are:

- **Entities:** the things the business cares about.
- **Attributes:** the facts recorded about each entity.
- **Relationships:** the links between entities. They reflect business processes and rules.
- **Business rules:** the rules that govern the entities and their links.

The model deliberately leaves out database-specific concerns. Indexes, data types and storage considerations do not belong in it. Logical modeling is a related topic that translates conceptual models into structured database designs.

One empirical study compared conceptual data models made by expert and novice practitioners. It judged them with quality factors drawn from earlier studies and frameworks on modeling quality. Experts' models were more correct, complete, innovative and flexible than novices' models.

**More about building and publishing a conceptual model.**

- **Conceptual Data Model Building Method:** A conceptual data model is built step by step: understand the business, find entities, add attributes and relationships, validate with stakeholders, then document. It describes what data is needed, not how to store it [src:2].

## Example

A small online library lists three entities: Member, Book and Loan. Member has a name. Book has a title. Loan links a member to a book through a business rule, such as "a member may borrow books". The model says nothing about tables, data types or indexes.

## Trade-offs

The sources say little about costs and benefits. One point comes from the study: models by experts were more correct, complete, innovative and flexible than models by novices. The study calls for further research on which aspects of expertise lead to these differences, and on how training courses can narrow the gap between experts and novices.
