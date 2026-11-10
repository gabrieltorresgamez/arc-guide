---
title: Refining Complex Context Views
slug: refining-complex-context-views
category: vision-stakeholders
kind: practice
summary: A complex system context stays readable when the top-level diagram remains a simple overview.
  Many external systems are grouped by clear criteria, and the detail of each interface, business and
  technical, is described separately.
arc42:
- 3
step: s02-scope-context
related:
- context-view
- arc42-context-and-scope
- business-and-technical-context
- c4-level-1-system-context-diagram
- context-view-antipatterns
- c4-model
- deployment-diagram
- context-view-antipattern-forgetting-bidirectional-data-flows
checks:
- The top-level context diagram shows the system as a black box and stays an overview without excessive
  detail.
- Where many external systems exist, they are clustered by explicitly stated criteria.
- The business context covers all communication partners, users and IT systems, and shows data flows rather
  than dependencies.
- The technical context describes the channels and transmission media to the environment, for example
  in a deployment diagram.
- Each communication partner has a row in a context table.
sources:
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/system-context
  title: System context diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Overview context with external systems clustered by an explicit criterion
review:
  status: generated
  flags: []
---

## Explanation

A context view shows your system as a black box. That means you see the system from outside, with no internal parts. Around the box sit the users and external systems that talk to it. See Context View and arc42 Context and Scope for the basics.

**Keep the top level an overview.** arc42 advises restricting the context to an overview and avoiding too many details. The C4 system context diagram likewise stresses that detail isn't important. It is a zoomed-out, low-detail picture that technical and non-technical readers can both follow. See System Context Diagram.

**Group many partners.** If many external systems are involved, arc42 says to cluster them by explicit criteria.

**Cover all partners.** The business context includes every communication partner, users and IT systems alike. It specifies the domain interfaces to each partner. It should show data flows, not dependencies.

**Describe the technical side too.** The technical context covers the channels and transmission media that link the system to its environment. Many stakeholders base architectural decisions on these technical interfaces. arc42 calls domain and technical interfaces among the most critical aspects of a system. See Business and Technical Context.

**Choose a notation for the detail.** arc42 suggests a table titled with the system name, with columns for the communication partner, the inputs, and the outputs. For technical channels, it suggests a UML deployment diagram.

## Example

An online shop talks to customers, a payment provider, three shipping companies and two marketing tools. The top-level diagram shows the shop as one box. It groups the shipping companies and the marketing tools into two clusters, labeled "logistics" and "marketing". A table then lists each partner in one row, with the data it exchanges and the direction of the flow. A separate deployment diagram shows the technical channels to the payment provider.

## Trade-offs

Keeping the overview small means readers must look elsewhere for detail, such as a table or a second diagram.
