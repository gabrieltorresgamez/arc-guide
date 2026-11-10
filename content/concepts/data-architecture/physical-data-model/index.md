---
title: Physical Data Model
slug: physical-data-model
category: data-architecture
kind: artifact
summary: A physical data model describes how data is stored in one specific database product. It defines
  keys, indexes, and storage settings, and it may bend the logical design for speed.
arc42:
- 8
- 5
- 9
step: s08-integration-data
related:
- logical-data-model
- conceptual-vs-logical-vs-physical-data-model
- logical-vs-physical-data-model
- conceptual-data-model
- data-architecture
- data-architecture-artifacts
checks:
- The physical model names the target DBMS it is designed for.
- Primary keys, foreign keys, and indexes are defined for data access.
- Storage choices such as partitioning and tablespaces are documented.
- Deviations from the logical model, such as denormalization, are stated and justified.
sources:
- url: https://www.datamation.com/big-data/logical-vs-physical-data-model/
  title: 'Logical vs Physical Data Model: A Comprehensive Guide | Datamation'
  site: datamation.com
  accessed: '2026-11-09'
- url: https://www.techtarget.com/news/Steps-for-converting-a-logical-data-model-into-a-physical-data-model/846220/
  title: Steps for converting a logical data model into a physical data model | TechTarget
  site: techtarget.com
  accessed: '2026-11-09'
- url: https://www.dbta.com/Columns/DBA-Corner/Transforming-a-Logical-Database-Design-to-a-Physical-Database-158539.aspx
  title: Transforming a Logical Database Design to a Physical Database - Database Trends and Applications
  site: dbta.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Data_vault_modeling
  title: Data vault modeling - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: From logical model to a refined physical model
review:
  status: generated
  flags: []
---

## Explanation

A physical data model is the most concrete level of data modeling. The logical data model is more abstract. The physical model is tied to one database management system (DBMS), the product that stores and serves the data. See the articles Logical Data Model and Conceptual, Logical and Physical Data Model for the other levels.

**What it contains**

- Primary keys and foreign keys. A primary key identifies a row. A foreign key points to a row in another table.
- Indexes. These help the database find data faster.
- Storage details such as filegroups, tablespaces, and partitioning. Partitioning splits stored data into parts.

**How it is produced**

Converting the logical model into a physical one includes assigning storage, for example partitioning and tablespace assignment. A data modeler drafts a first-cut physical model. The database administrator (DBA) then refines it.

**Deviating from the logical model**

The physical model may denormalize the design for performance. Denormalizing means deliberately departing from the clean logical structure. Choices about indexes, clustering, and denormalization can force the physical model to differ from the logical one.

**Data Vault**

Data Vault is a database modeling method for long-term historical storage of data in data warehouses. It uses three kinds of tables:

- Hubs hold unique business keys that rarely change.
- Links are essentially many-to-many join tables with some metadata.
- Satellites hold descriptive attributes, usually grouped by source system.

## Example

A team has a logical model with Customer and Order. The modeler drafts a first physical version for the chosen database. The DBA then adds an index on the customer key to speed up lookups. The DBA also partitions the large order table and assigns it to its own tablespace. If a slow report needs it, the team may denormalize a table and accept a gap from the logical model.

## Trade-offs

Tuning for performance can pull the physical model away from the logical model. Because the physical model is tied to one DBMS, it is also specific to that product.
