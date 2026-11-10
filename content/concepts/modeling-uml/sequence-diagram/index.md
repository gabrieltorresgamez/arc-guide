---
title: UML Sequence Diagram
slug: sequence-diagram
category: modeling-uml
kind: notation-element
summary: A UML sequence diagram shows how participants exchange messages over time, read from top to bottom.
  arc42 recommends it for runtime scenarios because it shows what each building block is responsible for.
arc42:
- 6
step: s10-document
related:
- runtime-view
- common-sequence-diagram-modeling-mistakes
- message-types-in-sequence-diagrams
- uml-unified-modeling-language
- arc42-documentation-template
- behavior-diagram
checks:
- Runtime scenarios in the runtime view are described with sequence diagrams (or another listed notation)
  so each building block's responsibility is visible.
- Each participant in a sequence diagram has its own lifeline, and the diagram reads in time order.
sources:
- url: https://docs.arc42.org/tips/6-11/
  title: 'Tip 6-11: Use sequence diagrams to describe or specify runtime scenarios! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Sequence_diagram
  title: Sequence diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Message_sequence_chart
  title: Message sequence chart - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A generic order scenario with three participants, one activation, and one reply.
review:
  status: generated
  flags: []
---

## Explanation

A sequence diagram shows interactions in time order. Each participant gets a lifeline. A lifeline is a vertical line. The lines run in parallel because the participants exist at the same time.

Messages are arrows between lifelines. Reading down the page follows the order of events.

Two more elements help readers:

- **Activation bars** are thin rectangles drawn on a lifeline. They show that a participant is busy working because of a message it received.
- **Destruction** is drawn as an X below a lifeline. After the X, the line stops.

The notation is strongly inspired by the Message Sequence Chart, a diagram standardized by the ITU. According to Wikipedia, the first version of that standard appeared in 1993.

In architecture work, a main use is the runtime view. This part of the documentation describes how building blocks work together while the system runs. See the article Runtime View. arc42 lists sequence diagrams as one option. Other options are activity diagrams, BPMN or EPCs, state machines, and numbered step lists. arc42 recommends sequence diagrams because they show clearly which building block is responsible for what. That helps teams discuss the building blocks.

## Example

Imagine a web shop with three participants: Browser, Shop, and Payment Service. The Browser sends "place order" to the Shop. The Shop sends "charge card" to the Payment Service. The Payment Service answers, and the Shop answers the Browser. Reading down the page, a reader sees the order of the calls. A reader also sees that the Shop coordinates the work and the Payment Service handles the charge.

## Trade-offs

A sequence diagram is one notation among several for runtime scenarios. arc42 also lists activity diagrams, BPMN or EPCs, state machines, and numbered step lists. Pick the one that fits the scenario and the readers.
