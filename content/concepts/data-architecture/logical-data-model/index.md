---
title: Logical Data Model
slug: logical-data-model
category: data-architecture
kind: artifact
summary: A logical data model defines the structure of business data (entities, keys, relationships) without
  naming any database engine. It sits between the conceptual model and the physical model.
arc42:
- 8
- 5
step: s08-integration-data
related:
- conceptual-data-model
- physical-data-model
- conceptual-vs-logical-vs-physical-data-model
- logical-vs-physical-data-model
- entity
- data-architecture
checks:
- The logical model names no database engine.
- Each entity has a stated identifier, and identifying relationships pass the parent's key into the child's
  identifier.
- Normalization level is stated, with 3NF as the default stopping point unless a measured query says otherwise.
- Mapping rules show how the logical model reaches each target database engine.
sources:
- url: https://dbschema.com/blog/design/logical-design-for-databases/
  title: 'Logical Database Design: Keys and Normalization | DbSchema'
  site: dbschema.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/IDEF1X
  title: IDEF1X - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Data_model
  title: Data model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'Customer, Order and Order Detail: the Order key becomes part of the Order Detail identifier.'
review:
  status: generated
  flags: []
---

## Explanation

Between a business conversation and a working database there are three model levels: conceptual, logical and physical. The conceptual model describes the meaning of the domain. The physical model describes how data are stored. The logical model sits in the middle. It settles the structure of the data and names no database engine.

**Entities, keys and relationships.** An entity stands for a class of real or abstract things, such as a customer. A key is an attribute, or a combination of attributes, whose values uniquely identify each instance of an entity. The chosen candidate key becomes the primary key. A relationship links instances of two entities, or of the same entity.

**Identifying relationships.** Logical design asks what identifies each entity. In an identifying relationship, the parent's key becomes part of the child's identifier.

**Normalization.** Normalization organizes data so each fact lives in one place. Third normal form (3NF) moves customer details into their own entity. A phone number is then updated in one row. Splitting order-level facts from line-level facts, such as Order and Order Detail, illustrates second normal form (2NF). Each kind of fact then sits at its own grain.

**Several engines.** Mapping rules let one logical model target several database engines. The models then do not drift apart.

For the neighboring levels, see the articles on the Conceptual Data Model and the Physical Data Model.

## Example

A shop models Customer, Order and Order Detail.

- Customer holds name and phone number once. A phone change touches one row.
- Order holds facts about the whole order, such as its date.
- Order Detail holds facts about one line of the order. Its identifier includes the key of its parent Order.

None of these definitions names a database product. That choice comes later, at the physical level.

## Trade-offs

Normalizing further is not always better. The advice is to stop at 3NF unless a measured query says otherwise. Keeping the model free of engine details means mapping rules are needed to reach each target engine.
