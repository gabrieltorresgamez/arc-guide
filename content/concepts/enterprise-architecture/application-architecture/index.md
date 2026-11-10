---
title: Application Architecture
slug: application-architecture
category: enterprise-architecture
kind: concept
summary: Application architecture is the enterprise-level view of which applications an organization uses
  and how they relate. It stays logical and does not cover the internal design of any single application.
arc42:
- 3
- 5
step: s10-document
related:
- togaf-phase-c-application-architecture
- togaf
- enterprise-architecture-management
- application-architecture-artifacts
- relationship-between-enterprise-architecture-and-application-architecture
- data-architecture
- business-architecture
- technology-architecture
checks:
- The document describes applications as logical groups of capabilities, not as specific computer systems.
- Application descriptions do not depend on particular technologies.
- The application portfolio is kept as a catalog in the architecture repository.
- Each application is linked to the data it manages and the business functions it supports.
- The enterprise-level application view covers choice of and relationships between applications, not the
  internal design of one application.
sources:
- url: https://www.opengroup.org/architecture/doc-review/protected-d3/htmlclean/chap11.html
  title: 'The Open Group Architecture Framework (TOGAF) - Phase C: Information Systems Architectures -
    Application Architecture'
  site: opengroup.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Enterprise_architecture_framework
  title: Enterprise architecture framework - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Enterprise architecture is commonly split into four domains: business, data, applications and technology. Application architecture is one of these four. It deals with the choice of applications and the relationships between them. It does not deal with how one application is built inside.

TOGAF handles this work in Phase C (see "TOGAF Phase C: Application Architecture"). Its aim is to define the major kinds of application system the business needs to process its data and support its work. The phase decides which kinds of application are relevant to the enterprise. It is not application system design.

TOGAF describes applications as logical groups of capabilities, not as computer systems. Each group manages data objects and supports business functions. That ties the application layer to the data and business architectures.

TOGAF also defines applications without reference to particular technologies. This keeps the layer logical and free of implementation choices.

The organization's application portfolio is kept as a catalog in the Architecture Repository.

## Example

A company lists the kinds of application it needs: one group of capabilities for handling orders, another for customer records. For each group, it notes which business functions it supports and which data it manages. It does not pick products or design screens. That detail belongs to the design of each individual system.

## Trade-offs

Keeping applications logical and free of technology gives a stable, high-level view across the portfolio. The price is that this view does not tell you how any one system is built. That needs separate design work.
