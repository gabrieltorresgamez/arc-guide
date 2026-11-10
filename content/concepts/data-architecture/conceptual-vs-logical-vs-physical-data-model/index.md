---
title: Conceptual, Logical and Physical Data Model
slug: conceptual-vs-logical-vs-physical-data-model
category: data-architecture
kind: concept
summary: Data models come in three levels. The conceptual level describes the business domain. The logical
  level shapes it for a chosen kind of data technology. The physical level describes how one specific
  database stores the data.
arc42:
- 8
- 5
- 12
step: s08-integration-data
related:
- conceptual-data-model
- logical-data-model
- physical-data-model
- logical-vs-physical-data-model
- data-architecture
- entity
- domain-model
- conceptual-data-model-preparation-for-logical-and-physical-models
checks:
- The conceptual model lists entity classes and their relationships without naming any storage technology.
- The logical model is independent of a specific DBMS or storage technology.
- Indexes, partitioning and tablespaces appear only in the physical model.
- The documentation states that storage technology can change without changing the logical or conceptual
  model.
sources:
- url: https://en.wikipedia.org/wiki/Data_model
  title: Data model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.datamation.com/big-data/logical-vs-physical-data-model/
  title: 'Logical vs Physical Data Model: A Comprehensive Guide | Datamation'
  site: datamation.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Data_modeling
  title: Data modeling - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/ANSI-SPARC_Architecture
  title: ANSI-SPARC Architecture - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The three levels move from business meaning to database-specific implementation.
review:
  status: generated
  flags: []
---

## Explanation

A data model describes what data a system keeps and how that data fits together. Teams usually work at three levels. Each level answers a different question.

**Conceptual model.** It describes the meaning of a domain. Entity classes (the kinds of things the business cares about) and the relationships between them set its scope. It records data requirements without tying them to any technology. An entity–relationship model can express it in abstract form. See the articles Conceptual Data Model and Entity.

**Logical model.** It describes the same meaning as one particular data technology represents it. That can be tables and columns, classes, or XML tags. It does not depend on a specific database product or storage technology. It helps stakeholders understand the data requirements. See Logical Data Model.

**Physical model.** It describes how the data is physically stored, including partitions, CPUs and tablespaces. It organizes data into tables and deals with access, performance and storage. It specifies indexes and keys that speed up data access. It also covers storage choices such as filegroups, tablespaces and partitioning. It is tailored to one database system. It is developer-oriented and guides the actual implementation. See Physical Data Model and Logical vs. physical data model.

**Why three levels.** The levels keep the perspectives independent. Storage technology can change without affecting the logical or conceptual model.

| Level | Describes | Tied to a specific DBMS or storage? | Typical use |
|---|---|---|---|
| Conceptual | Domain meaning: entity classes and relationships | No | Recording requirements |
| Logical | The meaning as tables, classes or tags | No | Helping stakeholders understand requirements |
| Physical | Storage, indexes, partitioning, access | Yes | Guiding implementation |

**Relation to ANSI-SPARC.** ANSI-SPARC is an older three-level idea for databases. Its external level gives each user a view of only the part of the database that matters to them. Its conceptual level is a global view that does not say how data is physically stored. Its internal level covers how the database is physically represented on the computer. The terms differ from the three data models above, although both split logical meaning from physical storage. ANSI-SPARC never became a formal standard. Its idea of logical data independence is still widely adopted.

## Example

A company builds an order system. At the conceptual level, the team notes that a Customer places Orders and an Order contains Products. At the logical level, they turn these into tables with columns. At the physical level, a developer adds an index to speed up order lookups and decides how to partition the order table. If the company later moves to different storage, the first two models stay as they are.

## Trade-offs

The structures in each model must stay consistent with the other models. Decide per project whether a level can be skipped. Storage changes need not affect the logical or conceptual model.
