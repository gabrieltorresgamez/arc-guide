---
title: Architectural Perspective
slug: architectural-perspective
category: quality-attributes
kind: concept
summary: An architectural perspective is guidance for making sure a system has a group of related quality
  properties, such as security. You apply it to each architectural view, instead of adding a new view
  per property.
arc42:
- 8
- 10
step: s04-quality-requirements
related:
- architecture-viewpoint
- architecture-view
- quality-attribute
- concern
- architectural-tactic
- security
- additional-architecture-views-and-perspectives
- architecture-view-model
checks:
- Quality properties such as security are handled by applying a perspective to each view, not by adding
  a separate viewpoint for each property.
- The document shows that each relevant perspective was considered with each view, not in isolation.
- Security is treated as risk management, not as a yes-or-no state.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/perspectives/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/perspectives/security/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Some quality properties, such as security, touch many parts of a system. Handling them with their own viewpoint does not work well. A viewpoint is a way of looking at a system (see Architecture Viewpoint). A security viewpoint would overlap with the other viewpoints.

A perspective takes a different route. It gives the architect a framework to guide and formalize the work of ensuring a quality property in the views. The architect applies the perspective to a view. Perspectives are never used alone. Each one is used with each view.

Security shows why this is needed. Which security qualities matter depends on the view you are looking at. So security cuts across views. Security is also not a yes-or-no state. It is a matter of managing risk.

Related articles: Architecture View, Quality Attribute, Concern, Architectural Tactic.

## Example

A team has a view of how data is stored and a view of how the system runs. They apply a security perspective to each one. In the data view, they ask which data needs protection. In the runtime view, they ask which interactions carry risk. They do not add a separate security view. Each existing view absorbs the findings.

## Trade-offs

Security is a matter of risk management. So a perspective cannot promise that a system "is secure". It helps the team manage risk in each view.
