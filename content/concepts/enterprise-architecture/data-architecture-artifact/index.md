---
title: Data Architecture Artifact
slug: data-architecture-artifact
order: 30
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
- conceptual-data-model
- conceptual-logical-and-physical-data-model
- togaf
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
- url: https://open-exam-prep.com/study-guides/togaf/adm-information-systems-architectures/phase-c-data-architecture
  title: 'Phase C Data Architecture: Principles, Data | Free Guide 2026 | OpenExamPrep'
  site: open-exam-prep.com
  accessed: '2026-11-09'
- url: https://ftpdocs.broadcom.com/cadocs/0/CA%20Gen%208%205-ENU/Bookshelf_Files/HTML/AnalysisGuide/1100395.html
  title: Analyzing Roles and Entity Types
  site: ftpdocs.broadcom.com
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/2011.10866
  title: '[2011.10866] Dynamic Data Consistency Tests Using a CRUD Matrix as an Underlying Model'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://open-exam-prep.com/study-guides/togaf/bdat-architecture-domains-deep-dive/data-architecture-domain-deep-dive
  title: 'Data Architecture Domain: Data Entities, Sto | Free Guide 2026 | OpenExamPrep'
  site: open-exam-prep.com
  accessed: '2026-11-09'
- url: https://www.informatica.com/blogs/business-glossary-vs-data-catalog.html
  title: Business Glossary vs Data Catalog
  site: informatica.com
  accessed: '2026-11-09'
- url: https://if4it.org/best-practices/data-and-information-inventory-and-attributes/glossary-of-terms-and-phrases/
  title: Glossary of Terms and Phrases - Data and Information Inventory and Attributes | The International
    Foundation for Information Technology (IF4IT)
  site: if4it.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How catalogs, matrices and diagrams build on each other in the Data Architecture phase.
review:
  status: generated
  flags: []
---

## Explanation

Data architecture artifacts are the working documents of the data part of enterprise architecture. In TOGAF, they belong to Phase C, the Data Architecture phase. (See the articles TOGAF.) One goal of this phase is to find gaps between the current (baseline) and desired (target) data architecture. Those gaps become candidates for the roadmap.

There are three kinds of artifact, and each does a different job.

- **Catalogs** are inventories. The organization's data inventory is kept as a catalog in the Architecture Repository.
- **Matrices** show relationships between model entities. They feed diagrams and help assess the impact of a change.
- **Diagrams** are visual views.

Catalogs and matrices take their structure from the attributes of entities in the TOGAF Content Metamodel.

**Typical artifacts**

See Data Architecture Artifact.
- *Data Entity/Business Function matrix.* It maps each entity to the business functions that create and use it. See Data Architecture Artifact.
- *Conceptual Data diagram.* This business data model shows the relationships between core entities. See Conceptual Data Model.
- *Other data diagrams.* Phase C also suggests logical, dissemination, lifecycle, security and migration diagrams.
In that case, define which copy is the master and which are copies.

A logical data model is usually normalized to reduce that duplication. See Conceptual, Logical and Physical Data Model.

**More about data artifacts.**

- **Data Entity/Business Function Matrix:** A Data Entity/Business Function Matrix links data entities to business functions. Each cell uses CRUD codes (create, read, update, delete) to show how a function uses an entity. It helps spot unclear ownership.
- **Data Entity/Data Component Catalog:** A data entity catalog is a master list of an organization's data entities. Each entry records the entity's definition, owner and classification level.

## Example

A retailer lists its data entities: Customer, Order, Product. The catalog records which application holds each one. A matrix then shows that the web shop creates Orders, while the warehouse function only reads them. A dissemination diagram shows Customer data stored in two systems. The team decides the CRM is the master and the other system holds a copy. Each gap between this picture and the desired state becomes a roadmap candidate.

## Trade-offs

Phase C only suggests the diagrams ("should be considered"), so teams choose which ones fit their needs. Producing every artifact is not required.
