---
title: Application Architecture Artifacts
slug: application-architecture-artifacts
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
- application-interface-diagram
- application-lifecycle-diagram
- togaf-phase-c-application-architecture
- togaf
- business-capability
- distribution-view
- patterns-for-the-evolution-of-application-landscapes
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
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Application architecture artifacts describe which applications an organization runs and how they relate. They are a set of views, not one document. Each view answers a different question.

**The catalog.** The application portfolio catalog lists all applications in the enterprise. Once the organization agrees on this list, it can define a standard set of applications and govern it.

**Interfaces and interactions.** The interface catalog scopes and documents the interfaces between applications. The application interaction matrix shows which applications communicate with each other. In matrix form, it is the equivalent of the interface catalog or an application communication diagram. The application communication diagram shows components and their interfaces. It stays logical and shows intermediary technology only where that matters architecturally.

**Link to technology.** The application/technology matrix maps applications to technology platforms.

**Change over time.** The application migration diagram is a time-oriented view. It shows the path from the baseline applications to the target applications, including temporary ones.

**Use in rationalization.** Rationalization decides what to do with each application: keep, upgrade, migrate or eliminate. It needs an inventory that records, for each application, the business capabilities it supports and its user groups. One possible decision is to retire a redundant application. Its data and users then move to an existing one.

**Level of detail.** The arc42 building block view shows the static decomposition of a system into building blocks and their dependencies. At level 2, it advises choosing which building blocks to detail by relevance rather than completeness.

## Example

A company keeps a catalog with three entries: web shop, billing and old invoicing. An interaction matrix shows that the web shop talks to billing and that old invoicing also talks to billing. The inventory records that old invoicing and billing support the same business capability. The team decides to retire old invoicing and move its data and users to billing. A migration diagram then shows old invoicing as a baseline application that disappears in the target state.
