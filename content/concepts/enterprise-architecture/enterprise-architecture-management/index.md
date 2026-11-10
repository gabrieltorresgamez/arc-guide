---
title: Enterprise Architecture
slug: enterprise-architecture-management
category: enterprise-architecture
kind: concept
summary: Enterprise architecture (EA) guides how an organization changes toward its business vision. It
  looks across many applications at once. Its goals are efficiency, lower cost and risk, and better alignment
  of business and IT.
arc42:
- 2
- 3
- 4
step: s05-constraints
related:
- relationship-between-enterprise-architecture-and-application-architecture
- zachman-framework
- togaf
- togaf-architecture-development-method
- enterprise-architecture-structure-business-and-it-architecture
- enterprise-architecture-strategy
- business-architecture
- warning-signs-of-poor-enterprise-architecture
checks:
- The document states which business vision or strategy the enterprise-level architecture supports.
- A target (future-state) architecture is described and used to steer decisions.
- The scope of the EA work is limited to the areas that matter most, not the entire organization.
- Organizational and political realities are acknowledged in how the EA approach is applied.
sources:
- url: https://sebokwiki.org/wiki/Enterprise_Architecture_(glossary)
  title: Enterprise Architecture (glossary) - SEBoK
  site: sebokwiki.org
  accessed: '2026-11-09'
- url: https://cioindex.com/reference/what-is-enterprise-architecture/
  title: What Is Enterprise Architecture (EA)? | CIO Portal
  site: cioindex.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/EnterpriseArchitecture.html
  title: Enterprise Architecture
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.brcommunity.com/articles.php?id=b206
  title: The Zachman Framework and Observations on Methodologies (Commentary)
  site: brcommunity.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Enterprise_architecture
  title: Enterprise architecture - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.isaqb.org/certifications/cpsa-certifications/cpsa-advanced-level/eam-enterprise-architecture-management/
  title: Enterprise Architecture Management - iSAQB® - Official Website
  site: isaqb.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Enterprise architecture, or EA, looks at the organization as a whole. A well-known definition calls it a discipline for leading an enterprise's response to disruptive forces. It does this proactively and holistically. It analyzes how change is carried out toward the desired business vision and outcomes.

**Steering toward a target.** The same definition says EA guides decisions so that the organization moves toward its planned future-state architecture.

**Goals.** One commercial source (CIO Portal) lists these goals:

- better efficiency and effectiveness,
- lower cost and risk,
- better alignment between business and IT.

**Difference from application architecture.** Single-application architecture deals with one system. EA deals with how to organize many applications into a coherent whole. The iSAQB advanced EAM module asks how to maintain consistency within a large IT and application landscape. See *Relationship between Enterprise Architecture and Application Architecture*.

**Frameworks.** The Zachman Framework is a classification schema, not a methodology or process. Its author says it is independent of methods and tools. See *Zachman Framework* and *TOGAF*.

**Challenges.**

- EA initiatives must recognize and respect organizational and political realities.
- An organization's full EA is too complex and extensive to document completely.

## Example

A company runs separate systems for orders, billing and customer service. Each team chose its own tools. Leadership wants a clear picture of how these systems fit together and where they should be in a few years. The EA work describes that future state. It then guides each new project toward it. The team does not try to build the whole architecture at once, but builds it piece by piece.

## Trade-offs

EA gives an enterprise-wide view, but it must work within the organization's political realities. Ignoring them puts an initiative at risk. Documenting everything is impractical, so some areas may stay undocumented.
