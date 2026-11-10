---
title: Additional Architecture Viewpoints (Security, Information, Operational, Development, Process, Evolution)
slug: additional-architecture-views-and-perspectives
category: documentation
kind: concept
summary: Besides the basic structural views, a project can add viewpoints for information, development,
  operations, deployment, security and evolution. Each covers a specific kind of concern that stakeholders
  raise.
arc42:
- 7
- 8
step: s10-document
related:
- architecture-viewpoint
- architecture-view
- architectural-perspective
- distribution-view
- 4-1-view-model
- security
- arc42-crosscutting-concepts
- stakeholder-concern
checks:
- If the software runs as a distributed system, the document includes a deployment view of the technical
  infrastructure.
- 'Security is described as a cross-cutting concern: who can do what to which resources, and how this
  is controlled, monitored and audited.'
- Operation, administration and support in production are described.
- How information is stored, managed and distributed is described.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/perspectives/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Basic structural views do not answer every question. Some stakeholders ask how data is handled, how developers work, or how the system runs in production. Extra viewpoints give those questions a home.

This article draws on the Rozanski & Woods set of viewpoints and on arc42, a documentation template. They describe these topics:

- **Information viewpoint.** It describes how the architecture stores, manipulates, manages and distributes information.
- **Development viewpoint.** It describes the architecture that supports the software development process.
- **Operational viewpoint.** It describes how the system is operated, administered and supported once it runs in production.
- **Deployment viewpoint.** It describes the environment the system is deployed into: hardware, network and runtime dependencies.
- **Security.** Here it is a perspective, not a viewpoint. A perspective is a cross-cutting quality concern. Security is about reliably controlling, monitoring and auditing who can do what to which resources.
- **Evolution.** This is also a perspective. It is about staying flexible as change arrives over the life of a system.

arc42 covers the deployment topic in its deployment view. This view documents the technical infrastructure that runs the system. arc42 says to document it especially when the software runs as a distributed system. Infrastructure can influence the system and its cross-cutting concepts, so the view is needed. See the articles on Deployment View and Crosscutting Concept.

## Example

A team builds a booking service that runs on several servers. Operations staff ask who will run and support it in production, so the team adds an operational view. The security officer asks who may change a booking, so the team describes security as a perspective.
