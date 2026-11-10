---
title: Common Features of Architecture Frameworks
slug: common-features-of-architecture-frameworks
category: enterprise-architecture
kind: concept
summary: 'An enterprise architecture framework defines how to create and use an enterprise architecture.
  Zachman and TOGAF differ in purpose, but TOGAF shows common traits: architecture levels, linked artifacts,
  and tailoring.'
arc42:
- 4
- 9
step: null
related:
- zachman-framework
- togaf
- togaf-architecture-development-method
- enterprise-architecture-meta-model
- business-architecture
- data-architecture
- technology-architecture
- enterprise-architecture-management
checks:
- The document states which enterprise architecture framework is used and whether it was tailored to the
  organization.
- Business, data, and technology architecture are described as separate levels.
- Artifacts are linked through a content metamodel, with a repository for storing them.
sources:
- url: https://en.wikipedia.org/wiki/Enterprise_architecture_framework
  title: Enterprise architecture framework - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework
  title: TOGAF - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://zachman-feac.com/zachman/about-the-zachman-framework
  title: About the Zachman Framework - Zachman International - FEAC Institute
  site: zachman-feac.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An enterprise architecture framework defines how to create and use an enterprise architecture. Frameworks do this in different ways. A few traits are worth knowing.

**Different purposes.** Zachman is a classification scheme. It sorts descriptive artifacts, meaning documents and models that describe an enterprise. It is not a process for planning systems or changes to them. Its matrix uses communication interrogatives (question words) as columns. It uses reification transformations as rows.

**Levels of architecture.** TOGAF splits the architecture into levels:

- Business architecture covers strategy, governance, organization, and key business processes.
- Data architecture covers the organization's logical and physical data assets.
- Technology architecture covers hardware, software, and network infrastructure.

See the articles Business Architecture, Data Architecture, and Technology Architecture for details.

**Linked artifacts.** TOGAF 9 added a content metamodel. It links the artifacts of TOGAF together. TOGAF 9 also added an architecture repository and the Enterprise Continuum. See Enterprise Architecture Meta Model for the general idea of a metamodel.

**Tailoring.** An organization may tailor TOGAF to its own needs. Treat a framework as a starting point, not a fixed rulebook.

## Example

A company wants to understand its order handling. One team uses a Zachman-style grid to file each description: a process model, a data model, a network diagram. Another team uses TOGAF and records the same material by level: business, data, technology. The second team then drops the parts of TOGAF it does not need.

## Trade-offs

Tailoring lets a framework fit an organization's needs. A classification scheme such as Zachman tells you where artifacts belong. It does not tell you how to plan change.
