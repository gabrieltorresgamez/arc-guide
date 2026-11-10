---
title: Data Entity/Business Function Matrix
slug: data-entity-business-function-matrix
category: enterprise-architecture
kind: artifact
summary: A Data Entity/Business Function Matrix links data entities to business functions. Each cell uses
  CRUD codes (create, read, update, delete) to show how a function uses an entity. It helps spot unclear
  ownership.
arc42:
- 8
step: s08-integration-data
related:
- data-architecture
- logical-data-model
- data-entity-data-component-catalog
- data-architecture-artifacts
- raci-matrix
- bounded-context
- togaf
checks:
- Each entity in the matrix is linked to business functions using CRUD codes.
- Where several roles create the same entity, the document names one owner or describes a split by role
  ownership.
sources:
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
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A Data Entity/Business Function Matrix maps logical data entities to core business functions. A logical data entity is a kind of business data, such as a customer or an order. The article "Logical Data Model" explains the term further.

Each cell of the matrix uses CRUD designations. CRUD stands for create, read, update and delete. A cell tells you what a function does with an entity.

Teams also use CRUD matrices to check consistency. The matrix captures how functions use data. That record becomes a model against which the data can be checked.

A related matrix, the Entity Type/Role Matrix described in CA Gen guidance, shows which roles use which data. When more than one role creates the same entity, that guidance suggests two responses:

- Decide which single role should own the entity type.
- Split the entity type so that each role owns one part.

Either way, the matrix makes the question visible.

## Example

Imagine a small company with three functions: Sales, Finance and Support. The rows are Customer and Invoice.

In the Customer row, Sales shows C and U. Support shows C and R. Finance shows R.

Two functions create customers. That is a signal to ask who should own the Customer entity. The team could name Sales the owner. Or it could split customers by role, for example sales customers and support contacts.
