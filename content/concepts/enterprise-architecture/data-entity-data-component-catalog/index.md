---
title: Data Entity/Data Component Catalog
slug: data-entity-data-component-catalog
category: enterprise-architecture
kind: artifact
summary: A data entity catalog is a master list of an organization's data entities. Each entry records
  the entity's definition, owner, classification and system of record, so teams share one view of the
  data.
arc42:
- 8
- 5
- 12
step: s08-integration-data
related:
- data-architecture
- data-entity-business-function-matrix
- data-architecture-artifacts
- togaf
- it-component-catalogue
- arc42-glossary
- data-architecture-diagram-types
- entity
checks:
- Every data entity in the catalog has a definition, an owner and a classification level.
- Each entity names exactly one system of record.
- Owner and steward roles are distinguished for each entity.
- Classification levels are linked to handling requirements such as encryption and access control.
- Entities are mapped to the physical storage systems or components that hold them.
sources:
- url: https://open-exam-prep.com/study-guides/togaf/bdat-architecture-domains-deep-dive/data-architecture-domain-deep-dive
  title: 'Data Architecture Domain: Data Entities, Sto | Free Guide 2026 | OpenExamPrep'
  site: open-exam-prep.com
  accessed: '2026-11-09'
- url: https://www.snowflake.com/en/data-governance/frameworks/togaf/
  title: TOGAF Framework Explained for Enterprise Data Architecture | Snowflake
  site: snowflake.com
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
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A data entity is a kind of business data, such as a customer or an order. The catalog is the master inventory of all such entities in the enterprise. For each one it records a definition, an owner and a classification level.

**System of record.** Each entity should have exactly one designated system of record. This is the authoritative source that creates and updates the entity. Other systems may use the data, but they do not own it.

**Owner and steward.** The owner holds strategic accountability for the entity. A steward is a different role. Stewards handle day-to-day data quality.

**Classification.** The catalog states how sensitive each entity is. This level drives encryption, access control, retention and compliance requirements. A sensitive entity therefore gets stricter handling than an ordinary one.

**Links to other artifacts.**
- A Data Entity/Data Component Matrix maps logical entities to the physical storage systems that hold them.
- A CRUD matrix maps application components to data entities. It declares which application holds authority over each entity. (CRUD stands for create, read, update, delete.)
- In TOGAF Phase C, Data Architecture work can include data entity and data component catalogs. See the article on TOGAF.

**Neighboring tools.** A data catalog is a technical metadata tool that scans and organizes metadata from physical data assets such as tables, columns, files and APIs. It complements a logical-level inventory like the entity catalog rather than replacing it.

**Keeping it current.** DAMA-DMBOK practices help keep entities, definitions, metadata, quality rules and stewardship up to date.

## Example

A retail company lists "Customer" in its catalog. The entry gives a short definition and names a business owner and a steward. It marks the entity as sensitive. It names the customer management application as the single system of record. When a new web shop needs customer data, the team reads the entry. They learn who to ask, how strictly to protect the data, and which system is authoritative.

## Trade-offs

A catalog only helps while it is accurate. Definitions, owners and stewardship change, so someone must keep them current. Insisting on a single system of record also means every other system must treat that source as authoritative for the entity.
