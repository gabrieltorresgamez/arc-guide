---
title: Process-Application-Infrastructure Mapping
slug: process-application-infrastructure-mapping
category: enterprise-architecture
kind: artifact
summary: A process-application-infrastructure mapping links business processes to the applications that
  support them and to the servers that host those applications. It shows what depends on what, so you
  can judge the effect of an outage or a change.
arc42:
- 7
- 5
step: s10-document
related:
- distribution-view
- deployment-diagram
- technology-architecture
- enterprise-architecture-structure-business-and-it-architecture
- traceability
- togaf
- application-architecture
- it-component-catalogue
checks:
- The deployment view shows which software building blocks run on which infrastructure elements.
- The software-to-hardware mapping is drawn as a UML deployment diagram.
- Dependencies between layers are shown with Serving relationships or with nesting that stands for them.
- The mapping makes clear which applications a server outage would affect.
sources:
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
diagrams:
- file: diagram-1.mmd
  caption: 'Three layers linked by serving relationships: a server serves an application, which serves
    a process.'
review:
  status: generated
  flags: []
---

## Explanation

A mapping like this connects layers. ArchiMate describes three layers (Business, Application and Technology) and uses the Serving relationship to show that one system provides functionality to another.

**Technology layer.** In ArchiMate, a modeling language for enterprise architecture, the technology layer covers software, hardware, network and physical systems. System software such as operating systems belongs there too.

**Links between layers.** ArchiMate uses the Serving relationship to say that one system provides functionality to another.

**Application to infrastructure.** The arc42 deployment view documents how software building blocks map onto infrastructure elements. See the article Deployment View. arc42 documents this mapping because infrastructure can influence the system and some of its cross-cutting concepts. It suggests UML deployment diagrams, but lets stakeholders use any kind of diagram that shows the nodes and channels of the infrastructure. See UML Deployment Diagram.

**Impact analysis.** A dependency map helps when something fails or changes. A configuration management database (CMDB) can show which applications a failing server affects. For example, a server outage may hit both HR and finance applications. The same mapping helps assess changes. For example, it can predict downtime if a firewall rule changes.

## Example

A company runs an invoicing process. An accounting application supports it. That application runs on a database server. The mapping records each link. When the database server needs maintenance, the team follows the links upward. They see that the accounting application is affected, and through it the invoicing process. They can then warn the people who run that process before the work starts.

## Trade-offs

The benefit: you can see which applications a server or a rule change affects. The cost of keeping the mapping current is a question to settle in your own organization.
