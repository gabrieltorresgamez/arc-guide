---
title: Conceptual Data Model Building Method
slug: conceptual-data-model-building-method
category: data-architecture
kind: method
summary: 'A conceptual data model is built step by step: understand the business, find entities, add attributes
  and relationships, validate with stakeholders, then document. It describes what data is needed, not
  how to store it.'
arc42:
- 3
- 8
- 12
step: s06-domain
related:
- conceptual-data-model
- conceptual-vs-logical-vs-physical-data-model
- conceptual-data-model-preparation-for-logical-and-physical-models
- publishing-the-conceptual-data-model
- entity
- logical-data-model
- physical-data-model
- arc42-glossary
checks:
- The model lists entities and their attributes without data types or storage details.
- Relationships state cardinality and whether they are mandatory or optional.
- Business rules and constraints are captured in the model.
- The model was validated with business stakeholders and data teams, and feedback was applied.
- A glossary of domain terms and definitions accompanies the model.
sources:
- url: https://airbyte.com/data-engineering-resources/conceptual-data-model
  title: 'What is Conceptual Data Modeling: Purpose & Examples | Airbyte'
  site: airbyte.com
  accessed: '2026-11-09'
- url: https://archman.dev/docs/foundational-concepts/data-fundamentals/data-modeling/conceptual
  title: Conceptual Data Modeling | ArchMan
  site: archman.dev
  accessed: '2026-11-09'
- url: https://www.thoughtspot.com/data-trends/data-modeling/conceptual-vs-logical-vs-physical-data-models
  title: 'Conceptual vs Logical vs Physical Data Models: Key Differences'
  site: thoughtspot.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model
  title: Entity–relationship model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'Generic conceptual ER sketch: entities and cardinalities, no data types.'
review:
  status: generated
  flags: []
---

## Explanation

A conceptual data model describes what data the business needs. It does not describe how the data is stored or built. The steps below keep the work at that level.

**1. Understand the business and set the scope.** The model answers one question: what exists in the business domain? The model focuses on business concepts rather than technical structures.

**2. Identify the main entities.** An entity is a core object or concept of the domain. Find these first. The article "Entity" explains the term.

**3. List attributes for each entity.** An attribute is a property of an entity. Keep attributes abstract. Do not give them data types at this level.

**4. Define relationships and cardinality.** Cardinality states how many instances of one entity relate to another. It also states whether the relationship is mandatory or optional.

**5. Capture business rules.** Business rules are the conditions and constraints that govern entities. Record them in the model.

**6. Validate with stakeholders.** Review the model with stakeholders and data teams. Refine it from their feedback. Use business terminology. If you leave business users out, requirements end up misaligned and implementation problems follow.

**7. Document and share.** Keep a glossary of domain terms and definitions. Draw ER (entity-relationship) diagrams for stakeholders. Chen's ER approach views the real world as entities and relationships. Conceptual ER models often define master reference entities that the whole organization uses.

**8. Hand over.** The finished model is the initial blueprint for the more detailed logical and physical models. The logical model adds keys and data types. The physical model specifies storage, indexing and constraints. The conceptual model leaves technology out. The article "Conceptual, Logical and Physical Data Model" compares the three.

## Example

A company wants to model its book lending. The team talks to librarians and finds the entities Member, Book and Loan. Each gets a few abstract attributes, such as a member's name. A Member can have many Loans. Each Loan must refer to exactly one Book. Librarians review the diagram and correct a term. The team adds the agreed terms to a glossary. Later, the logical model adds keys and data types.

## Trade-offs

One risk is clear: skipping business users in validation leads to misaligned requirements. Keep attributes abstract at this stage. Detail such as data types belongs to later models.
