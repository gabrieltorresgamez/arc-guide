---
title: Architecture Viewpoint
slug: architecture-viewpoint
category: documentation
kind: concept
summary: 'An architecture viewpoint is a set of patterns, templates and conventions for building one type
  of view. It names the stakeholders whose concerns that view addresses. A perspective differs: it applies
  quality guidelines across views.'
arc42:
- 5
- 6
- 7
step: s10-document
related:
- architecture-view
- architectural-perspective
- stakeholder
- concern
- 4-1-view-model
- architecture-view-model
- iso-iec-ieee-42010-architecture-description-standard
- model-vs-view
checks:
- Each view in the document is built from a named viewpoint.
- Each viewpoint names the stakeholders whose concerns it reflects.
- Quality perspectives are applied to views, not treated as views of their own.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/perspectives/
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

A **viewpoint** is a set of patterns, templates and conventions. You use it to build one type of architecture view. A view is a representation of one or more structural aspects of an architecture, showing how it addresses stakeholder concerns (see Architecture View).

A viewpoint also identifies the stakeholders whose concerns it reflects. (see Stakeholder and Concern).

**A published catalog.** The authors Rozanski and Woods present a catalog of six core viewpoints for information systems architecture:

- Functional
- Information
- Concurrency
- Development
- Deployment
- Operational


**Viewpoints and perspectives.** A perspective is a different thing. It is a set of activities, tactics and guidelines. Its goal is to make sure the system shows required quality properties. You never use a perspective alone. You apply it to a view. Perspectives address quality properties that require consideration across a number of views (see Architectural Perspective).

## Example

A team documents an online shop. One viewpoint guides a deployment view, which shows where the software runs. Another guides a functional view, which shows what the system does. Each viewpoint tells the team what to draw and which stakeholders it serves. Later, the team applies a security perspective to both views. It uses the perspective's guidelines to check that each view shows what security needs.
