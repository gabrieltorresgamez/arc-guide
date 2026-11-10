---
title: Data Architecture Artifact
slug: data-architecture-artifacts
category: enterprise-architecture
kind: artifact
summary: 'Data architecture artifacts are the catalogs, matrices and diagrams that document an organization''s
  data. Each one answers a different question: what data exists, who uses it, how it relates, and where
  the master copy lives.'
arc42:
- 5
- 8
- 12
step: s08-integration-data
related:
- data-architecture
- data-architecture-diagram-types
- data-entity-data-component-catalog
- data-entity-business-function-matrix
- conceptual-data-model
- conceptual-vs-logical-vs-physical-data-model
- togaf
- define-target-data-architecture-method-phase
checks:
- The data inventory is kept as a catalog in the Architecture Repository.
- Each data entity is mapped to the application or data component that holds it.
- A matrix maps data entities to the business functions that create and use them.
- Where data is duplicated, a mastering policy names the master and the copies.
- Gaps between baseline and target data architecture are identified as roadmap candidates.
sources:
- url: https://coe.qualiware.com/resources/togaf/9-1/part2-adm/phase-c-information-systems-architectures-data-architecture/
  title: 'Phase C: Information Systems Architectures – Data Architecture | QualiWare Center of Excellence'
  site: coe.qualiware.com
  accessed: '2026-11-09'
- url: https://grahamberrisford.com/AM%201%20Methods/6PRODUCTSandTECHNIQUES/DataAndInformation/AM%20Information-Data%20architecture.htm
  title: ''
  site: grahamberrisford.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How catalogs, matrices and diagrams build on each other in the Data Architecture phase.
review:
  status: generated
  flags: []
---

## Explanation

Data architecture artifacts are the working documents of the data part of enterprise architecture. In TOGAF, they belong to Phase C, the Data Architecture phase. (See the articles TOGAF and TOGAF Architecture Development Method.) One goal of this phase is to find gaps between the current (baseline) and desired (target) data architecture. Those gaps become candidates for the roadmap.

There are three kinds of artifact, and each does a different job.

- **Catalogs** are inventories. The organization's data inventory is kept as a catalog in the Architecture Repository.
- **Matrices** show relationships between model entities. They feed diagrams and help assess the impact of a change.
- **Diagrams** are visual views.

Catalogs and matrices take their structure from the attributes of entities in the TOGAF Content Metamodel.

**Typical artifacts**

- *Data Entity/Data Component catalog.* Avancier suggests mapping data entities to the data components that hold them, and TOGAF describes catalogs as hierarchical inventories. See Data Entity/Data Component Catalog.
- *Data Entity/Business Function matrix.* It maps each entity to the business functions that create and use it. See Data Entity/Business Function Matrix.
- *Conceptual Data diagram.* This business data model shows the relationships between core entities. See Conceptual Data Model.
- *Other data diagrams.* Phase C also suggests logical, dissemination, lifecycle, security and migration diagrams.
- *Mastering policy.* A dissemination diagram can reveal duplicated data. In that case, define which copy is the master and which are copies.

A conceptual data model specifies few if any attributes and is primarily used to identify data duplication. A logical data model is usually normalized to reduce that duplication. See Conceptual, Logical and Physical Data Model.

## Example

A retailer lists its data entities: Customer, Order, Product. The catalog records which application holds each one. A matrix then shows that the web shop creates Orders, while the warehouse function only reads them. A dissemination diagram shows Customer data stored in two systems. The team decides the CRM is the master and the other system holds a copy. Each gap between this picture and the desired state becomes a roadmap candidate.

## Trade-offs

Phase C only suggests the diagrams ("should be considered"), so teams choose which ones fit their needs. Producing every artifact is not required.
