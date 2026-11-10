---
title: Architect's Four Key Work Products
slug: architect-s-four-key-work-products
category: fundamentals
kind: framework
summary: The architect's four key work products are a vision, a context view, an architecture overview
  and an operational model. Together they cover goals, environment, main parts and how the system runs.
arc42:
- 1
- 3
- 5
- 7
step: s10-document
related:
- context-view
- c4-model
- as-is-and-to-be-view
- arc42-documentation-template
- additional-architecture-views-and-perspectives
- c4-container-diagram
- distribution-view
- vision-statement
checks:
- The context view shows the system as a black box with its communication partners and the data exchanged.
- The most important stakeholder quality goals are stated, for example the top three.
- The deployment or operational description shows only the infrastructure needed to place the building
  blocks.
- At least a context and a container level view exist, which suffices for most teams.
sources:
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://canvas.arc42.org/architecture-inception-canvas
  title: Architecture Inception Canvas - Software Architecture Canvas
  site: canvas.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=1766161&seqNum=6
  title: 'Our Viewpoint Catalog | Software Systems Architecture: Viewpoints and Views | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams
  title: Diagrams | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

**Vision.** The arc42 inception canvas asks for the three most important quality goals of the stakeholders.

**Context view.** The context view shows the system as a black box. It lists the communication partners and the data exchanged with them, so all stakeholders can see what flows in and out. The arc42 inception canvas adds that the business context helps identify communication paths and thus potential technical risks. See the articles Context View and System Context Diagram.

**Operational model.** Rozanski and Woods' Operational viewpoint covers how a system is run, administered and supported in production. From a software perspective, arc42 says it is sufficient to capture the infrastructure elements needed to show where building blocks are deployed. Detailed hardware decisions go to hardware experts.

**Mapping to other approaches.** C4 names four diagram levels: context, containers, components and code. It says the context and container diagrams are enough for most teams.

**Talking to stakeholders.** C4's levels of zoom let you tell different stories to different audiences.

## Example

A team builds an online booking tool. The vision names three quality goals that matter most to its users. The context view draws the tool as one box, with arrows to the payment provider and the email service. The overview splits the tool into a web app, a booking service and a database. The operational model shows where those parts run and who administers them.

## Trade-offs

Keeping to C4's context and container levels leaves out detail such as component and code views.
