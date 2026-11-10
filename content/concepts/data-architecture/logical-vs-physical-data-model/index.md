---
title: Logical vs. Physical Data Model
slug: logical-vs-physical-data-model
category: data-architecture
kind: concept
summary: A logical data model describes business data without tying it to any database. A physical data
  model refines it for one specific database, adding names, data types, keys and indexes. One logical
  model can yield several physical designs.
arc42:
- 5
- 8
- 12
step: s08-integration-data
related:
- conceptual-vs-logical-vs-physical-data-model
- logical-data-model
- physical-data-model
- conceptual-data-model
- data-architecture
- data-architecture-diagram-types
- entity
- canonical-data-model
checks:
- The logical model is free of database-specific details and does not depend on a chosen DBMS.
- The physical model names the target DBMS and follows its naming rules.
- Data types are stated for all stored data objects in the physical model.
- Keys and indexes are defined at the physical stage.
- The physical model was compared with the logical model to confirm business requirements were translated
  correctly.
sources:
- url: https://aws.amazon.com/compare/the-difference-between-logical-and-physical-data-model/
  title: Logical vs Physical Data Model - Difference in Data Modeling - AWS
  site: aws.amazon.com
  accessed: '2026-11-09'
- url: https://www.red-gate.com/blog/conceptual-logical-and-physical-data-model/
  title: How to Implement a Conceptual, Logical, and Physical Data Model in Redgate Data Modeler
  site: red-gate.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Data_model
  title: Data model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Data_vault_modeling
  title: Data vault modeling - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: One logical model can lead to several physical designs.
review:
  status: generated
  flags: []
---

## Explanation

A data model shows what data a system keeps and how the pieces relate. It exists at several levels of detail. The article *Conceptual, Logical and Physical Data Model* covers all three. This article compares the logical and the physical level.

**Logical data model.** Teams design it independently of the database that will later run it. It describes the business data, not the technology. Business analysts and data architects can use it to visualize processes.

**Physical data model.** It refines the logical model for one specific database technology. It is always built for a specific database management system (DBMS), which is the software that stores the data. So it must follow that platform's rules, such as naming conventions. It states the data type of every stored data object. Developers and database administrators implement it.

**Keys, indexes and more.** The physical stage is where you define primary keys, foreign keys, indexes, user roles, authorizations and stored procedures.

**Where the conceptual model fits.** The conceptual model is abstract and high-level. In practice, the line between conceptual and logical is somewhat blurry.

**Independence between levels.** In the three-level view, storage technology can change without affecting the logical or conceptual model.

## Example

A shop's logical model has a Customer entity and an Order entity. A customer places many orders. Nothing says which database will store them.

The team then picks a specific DBMS. The physical model gives the tables and columns names that follow the platform's rules. Each column gets a data type. Keys link orders to customers, and an index is added where lookups need it. If the team later changes database, the logical model stays the same. Only the physical model changes.

## Trade-offs

The boundary between conceptual and logical models is blurry.
