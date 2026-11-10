---
title: Conceptual Data Model
slug: conceptual-data-model
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
- conceptual-vs-logical-vs-physical-data-model
- physical-data-model
- conceptual-data-model-building-method
- data-architecture
- entity
- domain-model
- conceptual-data-model-preparation-for-logical-and-physical-models
checks:
- The conceptual data model contains entities, attributes, relationships and business rules.
- The conceptual data model contains no database-specific concepts such as indexes, data types or storage
  details.
- The relationships in the model reflect business processes and rules.
sources:
- url: https://archman.dev/docs/foundational-concepts/data-fundamentals/data-modeling/conceptual
  title: Conceptual Data Modeling | ArchMan
  site: archman.dev
  accessed: '2026-11-09'
- url: https://aisel.aisnet.org/ajis/vol4/iss2/7/
  title: '"Conceptual Data Modelling: an empirical study of expert and novice dat" by Graeme Shanks'
  site: aisel.aisnet.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'Small conceptual model: three entities with named relationships and no database details.'
review:
  status: generated
  flags: []
---

## Explanation

Conceptual data modeling is the process of creating a high-level picture of business information requirements. It describes the information the business needs, not how a database stores it.

The core elements are:

- **Entities:** the things the business cares about.
- **Attributes:** the facts recorded about each entity.
- **Relationships:** the links between entities. They reflect business processes and rules.
- **Business rules:** the rules that govern the entities and their links.

The model deliberately leaves out database-specific concerns. Indexes, data types and storage considerations do not belong in it. Logical modeling is a related topic that translates conceptual models into structured database designs.

One empirical study compared conceptual data models made by expert and novice practitioners. It judged them with quality factors drawn from earlier studies and frameworks on modeling quality. Experts' models were more correct, complete, innovative and flexible than novices' models.

## Example

A small online library lists three entities: Member, Book and Loan. Member has a name. Book has a title. Loan links a member to a book through a business rule, such as "a member may borrow books". The model says nothing about tables, data types or indexes.

## Trade-offs

The sources say little about costs and benefits. One point comes from the study: models by experts were more correct, complete, innovative and flexible than models by novices. The study calls for further research on which aspects of expertise lead to these differences, and on how training courses can narrow the gap between experts and novices.
