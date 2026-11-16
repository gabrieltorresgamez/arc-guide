---
title: arc42 Runtime View
slug: arc42-runtime-view
order: 70
category: documentation
kind: artifact
summary: Chapter 6 of arc42 describes how building blocks behave and work together at runtime. It documents a few architecturally relevant scenarios, not all of them.
arc42:
- 6
step: s10-document
related:
- runtime-view
- arc42-building-block-view
- arc42-architecture-documentation-template
- arc42-quality-requirements
- arc42-architecture-decisions
checks:
- The runtime view describes a representative selection of scenarios, not every possible one.
- Each scenario shows how existing building blocks take part in it.
- Error and exception scenarios or start-up and shutdown scenarios are covered where they are architecturally relevant.
- Scenarios use a notation that suits the readers, such as a numbered list, a sequence diagram or an activity diagram.
sources:
- url: https://docs.arc42.org/section-6/
  title: "6 - Runtime view | arc42 Documentation"
  site: docs.arc42.org
  accessed: '2026-11-16'
- url: https://docs.arc42.org/tips/6-2/
  title: "Tip 6-2: Document only a few runtime scenarios! | arc42 Documentation"
  site: docs.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The runtime view describes the concrete behavior and the interactions of the system's building blocks as scenarios. arc42 names these areas the scenarios can come from:

- important use cases or features, and how the building blocks execute them
- interactions at critical external interfaces, where building blocks cooperate with users and neighboring systems
- operation and administration, such as launch, start-up and stop
- error and exception scenarios

**What to include.** The main criterion is architectural relevance. A large number of scenarios is not important. arc42 asks for a representative selection, and its tip says to document only a few runtime scenarios.

**Why it exists.** You should understand how instances of building blocks do their job and communicate at runtime. Scenarios also help you explain the architecture to stakeholders who are less willing or able to read the static models, which are the building block view and the deployment view.

**How to write it.** Many notations work: a numbered list of steps in natural language, activity diagrams or flow charts, sequence diagrams, BPMN or event process chains, and state machines. Each scenario gets its own subsection, with a diagram or text and a description of the notable aspects of the interactions. A further tip says to map existing building blocks to the activities within each scenario.

See the article Runtime View for the view in general.

## Example

A web shop documents three scenarios: placing an order, a payment that the provider rejects, and the start-up of the system. Each is a numbered list of steps that names the building blocks taking part. The shop does not document every other use case.

## Trade-offs

arc42 asks for a few representative scenarios. Detailed scenarios are possible, but its tips say to use them with caution.
