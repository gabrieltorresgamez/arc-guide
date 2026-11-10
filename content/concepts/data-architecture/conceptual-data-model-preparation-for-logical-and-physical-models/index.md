---
title: Conceptual Data Model Preparation for Logical and Physical Models
slug: conceptual-data-model-preparation-for-logical-and-physical-models
category: data-architecture
kind: practice
summary: Preparing a conceptual data model means checking that it covers the business needs and defines
  its entities, attributes and relationships clearly. The checked model then becomes the basis for the
  logical and physical models.
arc42:
- 8
- 5
step: s08-integration-data
related:
- conceptual-data-model
- conceptual-data-model-building-method
- conceptual-vs-logical-vs-physical-data-model
- logical-data-model
- physical-data-model
- logical-vs-physical-data-model
- publishing-the-conceptual-data-model
- traceability
checks:
- The conceptual model was validated with business stakeholders, and found gaps were recorded.
- The conceptual diagram shows only entities and relationships, in terms a business audience understands.
- The conceptual model contains no data types, tables, columns or indexes.
- The document states how the conceptual model is handed over to the logical and physical models.
sources:
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
- file: diagram-1.mmd
  caption: Handover path from the conceptual model to the logical and physical models
review:
  status: generated
  flags: []
---

## Explanation

A conceptual data model is a high-level, abstract view of the business data. It shows entities (the things the business cares about), attributes (facts about them) and relationships between them. See *Conceptual Data Model* for the basics.

The model is the base for two later models. The logical model refines it. The physical model then refines the logical one for a specific database technology. See *Conceptual, Logical and Physical Data Model* for the comparison.

**What to check before handover**

- **Coverage.** Validating and clarifying the model can help detect gaps and missed requirements.
- **Business rules.** Engaging business stakeholders helps ensure the model meets their needs and captures accurate business rules.
- **Audience fit.** The conceptual diagram shows only entities and relationships, written for a business audience.

**What stays out**

Technical detail belongs to later stages. Indexes are listed among the physical model's details. Normalizing the data model appears in the logical and physical design steps.

**The blurry boundary**

The line between conceptual and logical models is somewhat blurry. In practice the two are rarely distinguished. Keep the conceptual model at the business level.

## Example

A team models an online bookshop. The conceptual model has the entities Customer, Order and Book. Customer places Order, and Order contains Book. Before handover, the team walks through the model with sales staff. They notice that returns are missing, so they add a Return entity and its relationship to Order. The model contains no data types or tables. The database team can now refine it into the logical model and then the physical one.

## Trade-offs

Keeping the model free of technical detail makes it readable for the business. It also means technical questions wait until later stages.
