---
title: Architecture Canvas
slug: architecture-canvas
category: documentation
kind: artifact
summary: An architecture canvas is a one-page structured sheet for capturing the essentials of a software
  system quickly. It builds on ideas from the Business Model Canvas and comes in three arc42 variants.
arc42:
- 1
- 3
- 9
step: s10-document
related:
- business-model-canvas
- arc42-documentation-template
- bounded-context-canvas
- architectural-decision-record
- arc42-introduction-and-goals
- arc42-context-and-scope
checks:
- The document lists the three most important stakeholder quality goals.
- Architectural assumptions are recorded and, where possible, drafted as decision records.
- The business context shows the system as a black box apart from its communication partners.
- The decisions that led to the current system state are named.
sources:
- url: https://canvas.arc42.org/
  title: Software Architecture Canvas - Software Architecture Canvas
  site: canvas.arc42.org
  accessed: '2026-11-09'
- url: https://arc42.org/resources/canvas-101/
  title: Canvas 101 - arc42
  site: arc42.org
  accessed: '2026-11-09'
- url: https://arc42.org/canvas/
  title: Canvas - arc42
  site: arc42.org
  accessed: '2026-11-09'
- url: https://canvas.arc42.org/architecture-inception-canvas
  title: Architecture Inception Canvas - Software Architecture Canvas
  site: canvas.arc42.org
  accessed: '2026-11-09'
- url: https://canvas.arc42.org/architecture-communication-canvas
  title: Architecture Communication Canvas - Software Architecture Canvas
  site: canvas.arc42.org
  accessed: '2026-11-09'
- url: https://canvas.arc42.org/faq
  title: Frequently Asked Questions - Software Architecture Canvas
  site: canvas.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An architecture canvas turns a complex topic into a single structured page. The arc42 canvases build on ideas from the Business Model Canvas (see the article of that name).

The canvas works as a workshop tool. Stakeholders brainstorm the sections together, ideally on large paper. The shared page helps the group understand each other. The canvas is fully compatible with the arc42 template (see arc42 Architecture Documentation Template).

**Three variants**

- **Inception Canvas.** It is for creating and envisioning new systems from scratch. It builds on Patrick Roos' Software Architecture Canvas.
- **Communication Canvas.** It has fields for describing a system, such as core decisions, components and technologies.
- **Tech Stack Canvas.** It is an INNOQ approach. It puts all relevant technologies on one page. You can use it to plan new projects or to document the status quo of an existing product.

**Selected Inception fields**

- *Business Case* is the "why" field. It names the economic driver behind a software initiative.
- *Quality goals* ask for the three most important goals of the stakeholders. These goals drive the architecture.
- *Architectural hypotheses* record your assumptions. Ideally, you can turn them into draft architecture decision records (see Architectural Decision Record).
- *Business context* treats your system as a black box, separate from its communication partners.

**Selected Communication fields**

- *Core Decisions* asks which decisions led to the current state of the system.
- *Components* lists the major building blocks, such as modules, subsystems, packages, components or services.
- *Technologies* lists the most important technologies for development and operation.

## Example

A small team must start a new booking system next week. They gather around a large sheet of paper laid out as an Inception Canvas. Together they write the business case, pick three quality goals and note their first architectural assumptions. They draw the system as a black box with its communication partners. Later, they turn an assumption into a draft decision record.

## Trade-offs

The sources describe it as a compact, zip-version summary and a starting point for more extensive documentation.
