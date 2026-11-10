---
title: Bounded Context Canvas
slug: bounded-context-canvas
category: domain-driven-design
kind: artifact
summary: The Bounded Context Canvas is a collaborative template for designing and documenting one bounded
  context. It captures name, purpose, importance, behavior, assumptions, and open questions.
arc42:
- 5
- 12
step: s06-domain
related:
- bounded-context
- domain-driven-design
- context-map
- ubiquitous-language
- domain-storytelling
- arc42-glossary
- evolutionary-domain-modeling
checks:
- The purpose of each bounded context is stated in a few sentences of business language, without technical
  details.
- The team has agreed on the name of each bounded context.
- Each bounded context is classified as core, supporting, or generic.
- Assumptions and open questions are written down, and many open questions are treated as a sign of high
  uncertainty.
sources:
- url: https://github.com/ddd-crew/bounded-context-canvas
  title: 'GitHub - ddd-crew/bounded-context-canvas: A structured approach to designing and documenting
    each of your bounded contexts · GitHub'
  site: github.com
  accessed: '2026-11-09'
- url: https://github.com/ddd-crew/bounded-context-canvas/blob/main/resources/model-traits-worksheet.md
  title: bounded-context-canvas/resources/model-traits-worksheet.md at main · ddd-crew/bounded-context-canvas
    · GitHub
  site: github.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

The Bounded Context Canvas helps a team design and document exactly one bounded context (see the article Bounded Context). The team works on it together.

The canvas has several sections. These are the ones covered here.

**Name.** The team writes down the context's name and agrees on it. The name frames how the team designs the context.

**Purpose.** A few sentences explain why the context exists and what it does. They use business language and contain no technical details.

**Strategic classification.** This asks how important the context is to the organization: core, supporting, or generic. The canvas also covers the business model and how far the context has evolved, from genesis through custom built and product to commodity.

**Domain roles.** This section describes how the context behaves, for example in analysis or execution roles. Two examples:
- A specification (or draft) role produces a document that describes a job or request to be performed.
- A gateway role sits at the edge of the system. It manages inbound and/or outbound communication.

**Assumptions.** Nobody designs with full knowledge of the domain. This section gives the team a place to record what it is assuming.

**Verification metrics.** These rest on the idea that domain-driven design (see Domain-Driven Design) is iterative and based on continuous learning.

**Open questions.** Many open questions signal high uncertainty in the design.

## Example

A team documents an "Order Fulfillment" context. They agree on the name first. The purpose reads: "Make sure every paid order reaches the customer on time." They classify it as core, because it matters to the company's success. They give it a gateway role for the messages it sends and receives. They list assumptions, such as "carriers deliver within three days," and several open questions. The long question list tells them the design is still uncertain.

## Trade-offs

The canvas covers one context at a time. A long list of open questions is not a flaw in the canvas. It is a useful signal of uncertainty.
