---
title: 'TOGAF Phase C: Application Architecture'
slug: togaf-phase-c-application-architecture
category: enterprise-architecture
kind: method
summary: Application Architecture in TOGAF Phase C designs the target applications that support the business
  architecture and vision. It compares today's applications with the target and turns the gaps into roadmap
  components.
arc42:
- 5
- 3
- 4
step: s10-document
related:
- togaf-architecture-development-method
- togaf
- application-architecture
- application-architecture-artifacts
- data-architecture
- business-architecture
- technology-architecture
- application-interface-diagram
checks:
- The document states a target application architecture that enables the business architecture and the
  architecture vision.
- Baseline and target application architectures are both described, and a gap analysis between them exists.
- Candidate roadmap components are derived from the gaps and feed a prioritized application roadmap.
- An application portfolio catalog and an interface catalog are present.
- Wider impacts of the finalized application architecture across the landscape are addressed.
sources:
- url: https://coe.qualiware.com/resources/togaf/9-1/part2-adm/phase-c-information-systems-architectures-application-architecture/
  title: 'Phase C: Information Systems Architectures – Application Architecture | QualiWare Center of
    Excellence'
  site: coe.qualiware.com
  accessed: '2026-11-09'
- url: https://www.visual-paradigm.com/guide/a-comprehensive-guide-to-togaf-adm-phase-c-information-systems-architectures/
  title: 'A Comprehensive Guide to TOGAF ADM Phase C: Information Systems Architectures'
  site: visual-paradigm.com
  accessed: '2026-11-09'
- url: https://coe.qualiware.com/resources/togaf/togaf-artifacts/
  title: TOGAF Artifacts | QualiWare Center of Excellence
  site: coe.qualiware.com
  accessed: '2026-11-09'
- url: https://s.visual-paradigm.com/guide/deep-dive-mastering-togaf-10-phase-c-deliverables/
  title: 'Deep Dive: Mastering TOGAF 10 Phase C Deliverables'
  site: s.visual-paradigm.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Application architecture work inside Phase C, between Phases B and D
review:
  status: generated
  flags: []
---

## Explanation

Phase C of the TOGAF Architecture Development Method covers two architectures: data and application. This article covers the application part.

**Objectives**

The first objective is a target application architecture. It must enable the business architecture and the architecture vision. The second objective is to find candidate roadmap components. These come from the gaps between the baseline (today's applications) and the target.

**Place in the method**

TOGAF does not fix the order inside Phase C. A team can do data first, application first, or both at the same time. Phase C follows the same rhythm as Phases B and D. The team documents the baseline, designs the target, and then performs a gap analysis. The finished data and application architectures feed the Technology Architecture in Phase D.

**Roadmap and impacts**

The candidate roadmap components add up to an application roadmap. It sets priorities for the activities in the coming phases. Once the application architecture is final, the team must also understand its wider impacts across the architecture landscape.

**Outputs**

The Architecture Definition Document is the core descriptive artifact of the method. The outputs of the application part of Phase C may include some or all of the following catalogs, matrices and diagrams:

- The Application Portfolio Catalog, a list of all applications in the enterprise.
- The Interface Catalog, which scopes and documents the interfaces between applications.
- Matrices, such as the Application/Organization matrix. It relates applications to organizational units.
- The Application Communication diagram. It shows application components and the interfaces between them.
- The Software Engineering diagram. From a development perspective, it splits applications into packages, modules, services and operations.
- The Application Migration diagram. It shows how application components move from baseline to target.

## Example

A company wants to support a new online ordering process. The team lists its current applications and the interfaces between them. It then designs the target set of applications. The gap analysis shows that no application handles order tracking. The team records "add order tracking" as a candidate roadmap component. It then checks which other parts of the landscape this change affects.
