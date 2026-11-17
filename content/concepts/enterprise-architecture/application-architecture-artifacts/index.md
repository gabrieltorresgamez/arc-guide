---
title: Application Architecture Artifacts
slug: application-architecture-artifacts
order: 20
category: enterprise-architecture
kind: artifact
summary: Application architecture artifacts document an enterprise's application layer. A catalog lists
  the applications. Interface, interaction, technology and migration views add connections, platforms
  and change over time.
arc42:
- 3
- 5
- 7
step: s10-document
related:
- application-architecture
- togaf
- business-capability
- deployment-view
checks:
- The documentation includes a list of all enterprise applications that is agreed and used to define a
  standard application set.
- Interfaces between applications are documented, and communication views stay logical.
- Applications are mapped to technology platforms.
- A migration view shows baseline and target applications, including temporary ones.
- The application inventory records the business capabilities and user groups of each application.
sources:
- url: https://coe.qualiware.com/resources/togaf/togaf-artifacts/
  title: TOGAF Artifacts | QualiWare Center of Excellence
  site: coe.qualiware.com
  accessed: '2026-11-09'
- url: https://www.leanix.net/en/blog/how-application-rationalization-contributes-to-the-bottom-line-part-two
  title: 'How Application Rationalization Contributes to the Bottom Line: Part Two'
  site: leanix.net
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://open-exam-prep.com/study-guides/togaf/adm-information-systems-architectures/data-application-integration-and-migration
  title: Data and Application Integration, Migration | Free Guide 2026 | OpenExamPrep
  site: open-exam-prep.com
  accessed: '2026-11-09'
- url: https://open-exam-prep.com/study-guides/togaf/adm-information-systems-architectures/phase-c-data-architecture
  title: 'Phase C Data Architecture: Principles, Data | Free Guide 2026 | OpenExamPrep'
  site: open-exam-prep.com
  accessed: '2026-11-09'
- url: https://www.ewsolutions.com/information-value-chain-analysis-and-enterprise-architecture/
  title: 'Enterprise Architecture: Master Information Value Chain'
  site: ewsolutions.com
  accessed: '2026-11-09'
- url: https://bizzdesign.com/blog/practical-archimate-viewpoints-for-the-application-layer
  title: 'Enterprise Architecture modeling: Practical ArchiMate® viewpoints for the application layer'
  site: bizzdesign.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/container
  title: Container diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://documentation.alfabet.com/11-8/en/PortAdmin_ROAD_AppRoad_Over.html
  title: What is our application roadmap?
  site: documentation.alfabet.com
  accessed: '2026-11-09'
- url: https://www.leanix.net/en/blog/gartner-time-tolerate
  title: 'Gartner® TIME Framework For App Rationalization: Tolerate'
  site: leanix.net
  accessed: '2026-11-09'
- url: https://archimate-community.pages.opengroup.org/workgroups/archimate-101/
  title: 'ArchiMate 101: A Practical Introduction'
  site: archimate-community.pages.opengroup.org
  accessed: '2026-11-10'
- url: https://www.ninjaone.com/blog/cmdb-dependency-mapping/
  title: 'Guide: How to Use CMDB Dependency Mapping | NinjaOne'
  site: ninjaone.com
  accessed: '2026-11-10'
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Application architecture artifacts describe which applications an organization runs and how they relate. They are a set of views, not one document. Each view answers a different question.

**Two basic views.**

- The application portfolio catalog lists all applications in the enterprise.
- The application interaction matrix shows which applications communicate with each other.

**Use in rationalization.** Rationalization decides what to do with each application: tolerate, invest, migrate or eliminate. It needs an inventory that records, for each application, the business capabilities it supports and its user groups.

**Level of detail.** The arc42 building block view shows the static decomposition of a system into building blocks and their dependencies. At level 2, it advises choosing which building blocks to detail by relevance rather than completeness.

**More about application artifacts.**

- **Application/Data Matrix:** The Application/Data Matrix shows which applications create, read, update or delete each data entity. It names one system of record per entity and exposes overlaps in the application landscape [src:4].
- **Application Cooperation View:** An application cooperation view shows how applications work together and where a new application affects the existing landscape. A useful addition is the technology interface of each connection, such as a REST API or FTP.
- **Application Lifecycle Diagram:** An application lifecycle diagram is a Gantt chart that shows when each application is planned to start and stop supporting the business. It helps teams spot retirement and replacement needs early.

## Example

A company keeps a catalog with three entries: web shop, billing and old invoicing. An interaction matrix shows that the web shop talks to billing and that old invoicing also talks to billing. The inventory records that old invoicing and billing support the same business capability. The team decides to retire old invoicing and move its data and users to billing. The team draws the planned migration from the current to the target landscape.
