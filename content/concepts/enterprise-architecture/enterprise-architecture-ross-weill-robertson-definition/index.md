---
title: Enterprise Architecture (Ross/Weill/Robertson Definition)
slug: enterprise-architecture-ross-weill-robertson-definition
category: enterprise-architecture
kind: concept
summary: 'Enterprise architecture is the logic that organizes a company''s business processes and IT infrastructure.
  It follows from the company''s operating model: how far its processes are integrated and standardized.'
arc42:
- 1
- 4
step: s07-solution-strategy
related:
- operating-model
- foundation-for-execution
- enterprise-architecture-maturity-stages
- enterprise-architecture-management
- enterprise-architecture-strategy
- togaf
- zachman-framework
- software-architecture
checks:
- The document states which operating model (diversification, coordination, replication or unification)
  the company follows.
- The architecture description is based on the company's choices for process integration and standardization.
sources:
- url: https://dspace.mit.edu/entities/publication/4fa6b4a6-2c2e-44d3-871d-ce992c2bd5bd
  title: 'Enterprise Architecture: Driving Business Benefits from IT (selected research briefings)'
  site: dspace.mit.edu
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/archive/blogs/jmeier/diversification-coordination-replication-and-unification
  title: Diversification, Coordination, Replication, and Unification | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://mitsloan.mit.edu/ideas-made-to-matter/mit-expert-recaps-30-plus-years-enterprise-architecture
  title: MIT expert recaps 30-plus years of enterprise architecture | MIT Sloan
  site: mitsloan.mit.edu
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The four operating models as combinations of process integration and standardization.
review:
  status: generated
  flags: []
---

## Explanation

MIT CISR's 2006 working paper abstract defines enterprise architecture as the organizing logic for business processes and IT infrastructure. In plain terms, it describes how a company arranges its work and its technology so the two fit together.

**The operating model drives the architecture**

A company's operating model comes from two choices. One is how much its business processes are integrated, meaning linked so that units share data and work together. The other is how much they are standardized, meaning done the same way everywhere. The authors built a two-dimensional model with four quadrants from these two levels. Every company should place itself in one.

**The four operating models**

- **Diversification:** Business units share few customers, suppliers or ways of working. Central control is limited.
- **Coordination:** Integration of shared data is high. Processes are standardized very little.
- **Replication:** Units act autonomously but run highly standardized operations. Success depends on repeatable processes, not shared data.
- **Unification:** Units are tightly integrated around standardized processes. Unit autonomy has little value.

Companies may use different models at different levels.

**Architecture as a long-term practice**

Ross describes enterprise architecture in practice as designing people, processes and technology to meet customer expectations. They call it an approach to managing the company, not an initiative or a project.

**Foundation and maturity**

The authors report that companies with a foundation for execution reached higher strategic effectiveness and operational proficiency. The article Foundation for Execution covers this. CISR research also found that firms pass through four stages of architecture maturity. The article Enterprise Architecture Maturity Stages covers them.

## Example

A retail group has shops in several countries. Each shop must run the same checkout and stocking routines, but shops do not need to share customer data. This fits the replication model. The architecture then stresses repeatable, standardized processes and the technology that supports them. It does not stress a shared customer database.

## Trade-offs

Each operating model gives something up. Replication gives units autonomy but runs operations in a standardized way. Unification gains from tight integration but leaves little room for unit autonomy. Coordination shares data but standardizes processes little. Diversification limits central control. A company must choose a position, and its architecture should follow that choice.
