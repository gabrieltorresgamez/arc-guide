---
title: UML Behavioral Diagram
slug: behavior-diagram
category: modeling-uml
kind: notation-element
summary: 'UML behavior diagrams show how a system works while it runs: how users interact with it, which
  steps happen, which messages flow, and how states change. Structure diagrams show only the static parts.'
arc42:
- 6
step: s10-document
related:
- uml-diagram-taxonomy
- structure-diagram
- sequence-diagram
- state-machine-diagram
- use-case-diagram
- runtime-view
- matching-diagram-type-to-system-aspect
- uml-unified-modeling-language
checks:
- Runtime scenarios are described with a behavior notation such as an activity diagram, sequence diagram
  or state machine.
- Where a sequence diagram is used, it shows the responsibility of each participating building block.
- Swimlanes in an activity diagram of a runtime scenario correspond to building blocks.
sources:
- url: https://www.drawio.com/docs/diagram-types/uml/
  title: An introduction to UML diagrams | draw.io
  site: drawio.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/6-11/
  title: 'Tip 6-11: Use sequence diagrams to describe or specify runtime scenarios! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/examples/runtime-tpu-1/
  title: 'Example Runtime View: TrafficPursuitUnit | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Behavior diagram types in UML, grouped as in the text above.
review:
  status: generated
  flags: []
---

## Explanation

UML splits its diagrams into two groups. Structure diagrams document the static structure of a system and how its parts relate to each other (see UML Structure Diagram). Behavior diagrams show how control or information passes between those parts as the system runs.

The behavior diagram types answer different questions:

- **Use case diagram:** the ways an end user can interact with the system (see Use Case Diagram).
- **Activity diagram:** the sequence of activities, with the flow of control or the flow of objects through the system.
- **State machine diagram:** the states of a system and the transitions that trigger a move to another state (see State Machine Diagram).
- **Sequence diagram:** the order of messages that elements pass to each other to complete a task or use case (see UML Sequence Diagram).
- **Timing diagram:** how long an action needs to change the state of an element.
- **Interaction overview diagram:** the interactions in a system and how control flows between them.

The arc42 runtime view (see Runtime View) uses these diagrams to describe scenarios. It lists activity diagrams, sequence diagrams and state machines as notations. arc42 advises activity diagrams with swimlanes for runtime scenarios. It also recommends sequence diagrams, because they show the responsibility of each building block.

The arc42 TPU example draws one scenario in four ways: as a sequence diagram, a communication diagram, an activity diagram and a swimlane activity diagram. In the swimlane version, the lanes are the level-1 building blocks.

## Example

A team documents an online order. A use case diagram shows that a customer can place an order. A sequence diagram shows the messages between the shop, the payment service and the warehouse. A state machine diagram shows the order moving between states, each move triggered by a transition.

## Trade-offs

Sequence diagrams make the responsibility of each building block clear. arc42 notes they can be costly to maintain in graphical tools. Because one scenario can be drawn in several notations, pick the diagram that best fits the question you want to answer.
