---
title: Runtime View
slug: runtime-view
category: documentation
kind: artifact
summary: The runtime view shows how building blocks work together and talk to each other while the system
  runs. It covers a few chosen scenarios, picked for architectural relevance rather than completeness.
arc42:
- 6
step: s10-document
related:
- sequence-diagram
- arc42-documentation-template
- c4-model
- component-view
- contemporary-essential-views
- runtime-view-antipattern-code-level-activity-diagram
- traceability
- bpmn-2-0-notation-overview
checks:
- Scenarios are selected for architectural relevance, not to cover every flow.
- Each activity in a runtime scenario maps to an existing building block.
- The runtime view covers key use cases, external interfaces, start-up or administration, and error cases
  as scenarios.
- Scenarios use a recognized notation, such as sequence diagrams, step lists, flowcharts or BPMN.
sources:
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/dynamic
  title: Dynamic diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'A generic runtime scenario: building blocks exchange messages in order.'
review:
  status: generated
  flags: []
---

## Explanation

A static view shows which building blocks exist. The runtime view shows what they do. It describes concrete behavior and interactions, written as scenarios.

**What to cover**

The arc42 template (see "arc42 Architecture Documentation Template") names several kinds of scenarios:

- Key use cases.
- Interactions across external interfaces.
- Start-up and administration.
- Error cases.

**Choosing scenarios**

You do not document every flow. The main test is architectural relevance. Choose a representative selection of scenarios that matter architecturally. Skip the rest.

**Notations**

Many notations work. arc42 lists step lists, flowcharts, sequence diagrams, BPMN and state machines. See "UML Sequence Diagram" for how sequence diagrams read.

The C4 model has a similar idea, called a dynamic diagram. It shows how elements from the static model collaborate at runtime. It builds on UML communication diagrams, which number the interactions. You can also draw it in sequence style.

**Traceability**

Each activity in a scenario should be mapped to an existing building block.

## Example

Imagine an online shop. The team documents "customer places an order" as a numbered list:

1. The web shop receives the order.
2. The web shop asks the payment service to charge the card.
3. The payment service confirms.
4. The web shop passes the order to the warehouse system.

Each named actor is a building block already shown in the static view. The team skips minor flows, such as changing a profile photo, because they are not architecturally relevant.

## Trade-offs

One limit is clear: you must choose. Scenarios are selected for architectural relevance, not completeness. A runtime view will therefore leave many flows undocumented on purpose.

You also have a choice of notation. arc42 lists several valid options, including sequence diagrams.
