---
title: Data Architecture Diagram Type
slug: data-architecture-diagram-types
category: data-architecture
kind: artifact
summary: Data diagrams work at different levels of detail. A conceptual diagram names core business entities.
  A logical diagram adds keys and attributes. A physical model fits one specific database.
arc42:
- 5
- 8
step: s08-integration-data
related:
- conceptual-data-model
- logical-data-model
- physical-data-model
- conceptual-vs-logical-vs-physical-data-model
- data-architecture-artifacts
- data-architecture
- togaf
- data-entity-data-component-catalog
checks:
- The conceptual data diagram names core business entities and is used to find duplicated data.
- The logical data diagram gives each entity a primary key and attributes without database-specific detail.
- Any denormalization for performance appears only in the physical, database-specific model.
- Each physical data component is traced to the logical data component it realizes.
sources:
- url: https://www.grahamberrisford.com/AM%201%20Methods/6PRODUCTSandTECHNIQUES/DataAndInformation/AM%20Information-Data%20architecture.htm
  title: ''
  site: grahamberrisford.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Data architecture describes data at several levels.

**Conceptual level.** A conceptual data model names the core business entities, the main things the business cares about. It gives few attributes, or none. People use it mainly to spot duplicated data. See Conceptual Data Model.

**Logical level.** A logical data model adds a primary key and attributes to each entity. The model also shows relationships. It stays purely logical: it declares business terms and concepts, not database details. See Logical Data Model.

**Physical level.** A physical data model is the schema for one particular database. It may be denormalized to speed up storage or retrieval. See Physical Data Model, and Conceptual, Logical and Physical Data Model.

**Link to TOGAF.** TOGAF is an architecture framework (see TOGAF). In TOGAF, a physical data component is the vendor- or technology-specific form of a logical data component. This ties the logical and physical levels together.

## Example

A retailer first draws a conceptual diagram with Customer, Order and Product, joined by simple relationships. A logical diagram then gives each entity attributes and a primary key, such as a customer number. A physical model finally fixes the schema for the chosen database.

## Trade-offs

A physical model may be denormalized to speed up storage or retrieval. Conceptual diagrams say little about attributes.
