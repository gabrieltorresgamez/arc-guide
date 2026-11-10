---
title: Application/Data Matrix
slug: application-data-matrix
category: enterprise-architecture
kind: artifact
summary: The Application/Data Matrix shows which applications create, read, update or delete each data
  entity. It names one system of record per entity and exposes overlaps in the application landscape.
arc42:
- 3
- 5
- 8
step: s08-integration-data
related:
- data-entity-business-function-matrix
- data-architecture
- data-architecture-artifacts
- togaf
- logical-data-model
- raci-matrix
- shared-database
- application-architecture-artifacts
checks:
- Each logical data entity has exactly one designated system of record.
- Overlaps where several applications maintain the same data are listed, with a master-and-copy mastering
  policy.
- Redundant or obsolete data stores found in the gap analysis are marked for retirement.
sources:
- url: https://open-exam-prep.com/study-guides/togaf/adm-information-systems-architectures/data-application-integration-and-migration
  title: Data and Application Integration, Migration | Free Guide 2026 | OpenExamPrep
  site: open-exam-prep.com
  accessed: '2026-11-09'
- url: https://grahamberrisford.com/AM%201%20Methods/6PRODUCTSandTECHNIQUES/DataAndInformation/AM%20Information-Data%20architecture.htm
  title: ''
  site: grahamberrisford.com
  accessed: '2026-11-09'
- url: https://open-exam-prep.com/study-guides/togaf/adm-information-systems-architectures/phase-c-data-architecture
  title: 'Phase C Data Architecture: Principles, Data | Free Guide 2026 | OpenExamPrep'
  site: open-exam-prep.com
  accessed: '2026-11-09'
- url: https://www.ewsolutions.com/information-value-chain-analysis-and-enterprise-architecture/
  title: 'Enterprise Architecture: Master Information Value Chain'
  site: ewsolutions.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Application/Data Matrix is a table that links applications to logical data entities. A logical data entity is a business concept, such as Customer or Order, described without storage details (see the article Logical Data Model).

Each cell holds CRUD codes: create, read, update, delete. They show what an application does with an entity.

**System of record.** The matrix identifies a system of record for each logical data entity. One of the goals of Phase C integration is that every logical data entity has a designated software system of record responsible for its lifecycle.

**Ownership.** Naming the system of record gives each entity a responsible system. An Application Organization Matrix can also link applications to organizational structures, to support accountability and business ownership.

**Overlaps and consistency.** The matrix can reveal overlaps, where several applications maintain the same data. When data is duplicated, define a data mastering policy. Such a policy sets out a master and copies.

**Related matrices.** The Data Entity/Business Function Matrix maps entities to business functions with CRUD codes. It highlights ownership and exposes redundant data creation. Information value chain analysis uses an entity/process matrix, often called a CRUD matrix. It shows which processes create, read, update or delete each business data entity.

## Example

A company lists four entities: Customer, Order, Product and Inventory. It lists the applications that touch them. Each entity gets one system of record. For example, a CRM could own Customer, and an ERP billing module could own Order. A product catalog could own Product, and a warehouse system could own Inventory.

| Entity | CRM | ERP billing | Catalog |
|---|---|---|---|
| Customer | C, R, U | R | R |
| Order | R | C, R, U | |
| Product | | R | C, R, U |

The matrix can reveal where several applications maintain the same entity. The team then decides on a master and copies.

## Trade-offs

The matrix shows who does what with data. It can reveal overlaps, and a data mastering policy should be defined when data is duplicated.
