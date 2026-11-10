---
title: Data Architecture
slug: data-architecture
category: data-architecture
kind: concept
summary: Data architecture describes how an organization's data is sourced, stored, managed, integrated
  and protected so it supports business goals. It gives business and technical teams one shared view of
  data repositories, relationships and ownership.
arc42:
- 3
- 5
- 8
step: s08-integration-data
related:
- data-architecture-artifacts
- data-entity-business-function-matrix
- logical-vs-physical-data-model
- data-architecture-principle
- define-target-data-architecture-method-phase
- data-architecture-documentation-in-arc42
- business-architecture
- application-architecture
checks:
- The document gives an overall view of data repositories, their relationships and their owners.
- The document names the database of record for master and reference data.
- A CRUD matrix shows which processes create, read, update or delete each business data entity.
- Data sources, formats, flows and quality are identified, along with privacy and security aspects.
- The data architecture is tied to business goals and to the organization's own context.
sources:
- url: https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/data-management-architecture
  title: Manage your data effectively with the right architecture - Dynamics 365 | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://www.ewsolutions.com/information-value-chain-analysis-and-enterprise-architecture/
  title: 'Enterprise Architecture: Master Information Value Chain'
  site: ewsolutions.com
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/an-enterprise-information-system-data-architecture-guide/
  title: An Enterprise Information System Data Architecture Guide | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/data-arch.html
  title: Data architecture - AWS Prescriptive Guidance
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Operational data flowing to analytics, with a database of record as master source.
review:
  status: generated
  flags: []
---

## Explanation

Data architecture is a high-level concept. It describes how data supports the strategic goals of a business. Data modeling is a lower-level activity. It defines the data flows and relationships inside a system. Together they align data assets with the organization's strategy.

**What it covers**

- It identifies data sources, formats, flows and quality.
- It considers privacy, security, and the technologies and policies that govern data use.
- It asks practical questions. How do we use, store and manage data? How do we integrate it across lines of business?

One short definition: data architecture describes the way a system stores, manages and uses its data. This matters even more when components come from different contractors or vendors.

**A holistic view**

The key point is one overall view of data repositories, their relationships and their owners. Without it, business and technical teams may drift apart.

**Typical building blocks**

- *Enterprise data model.* It is the core of an enterprise data architecture.
- *Logical and physical data models.* Notations include UML, IDEF1X and entity relationship diagrams (ERDs). Physical models are commonly ERDs. See the article *Logical vs. physical data model*.
- *Master data.* This is common business data, such as customers, vendors and products. It is consistent, nontransactional and controlled for accuracy.
- *Database of record.* Data integration architecture names the database of record for reference and master data. It focuses on their quality.
- *CRUD matrix.* This entity/process matrix shows which processes create, read, update or delete each business data entity. See *Data Entity/Business Function Matrix*.
- *Analytics.* Operational data can be exported to a data lake. From there it feeds a data warehouse and analytics, which can facilitate the organization's analytics strategy.
- *Data APIs.* Segmenting data into containers and exposing them through APIs helps the architecture scale across distributed platforms. Data that is exposed externally needs security and compliance controls.

**Serving its context**

A modern data architecture should support both the near-term and the long-term goals of the business. It should also fit the culture and context of the organization.

## Example

A retailer keeps customer records in a billing system, a web shop and a support tool. Nobody knows which copy is correct. The team lists each repository and its owner. It names the billing database as the database of record for customers. A CRUD matrix shows that only the sign-up process creates customers, while support only reads them. Nightly exports feed a data warehouse, so reports no longer load the shop database.

## Trade-offs

A modern data architecture should align with business goals. It must fit the organization's culture and context.
