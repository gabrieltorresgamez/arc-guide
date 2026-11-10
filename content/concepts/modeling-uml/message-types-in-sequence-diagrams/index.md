---
title: Message Types in Sequence Diagrams
slug: message-types-in-sequence-diagrams
category: modeling-uml
kind: notation-element
summary: 'A message in a sequence diagram is one step of communication between participants. The key distinction
  is whether the sender waits: a synchronous sender waits until the work is done, an asynchronous sender
  keeps going.'
arc42:
- 6
step: s10-document
related:
- sequence-diagram
- synchronous-vs-asynchronous-communication
- runtime-view
- common-sequence-diagram-modeling-mistakes
- synchronous-vs-asynchronous-connector
checks:
- Runtime scenarios in the architecture document are shown with sequence diagrams, or another deliberately
  chosen scenario notation.
- The sequence diagrams make clear what each participating building block is responsible for.
sources:
- url: https://en.wikipedia.org/wiki/Sequence_diagram
  title: Sequence diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/6-11/
  title: 'Tip 6-11: Use sequence diagrams to describe or specify runtime scenarios! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A sequence diagram (see UML Sequence Diagram) shows how parts of a system talk to each other over time. Each arrow is a message.

A message can be synchronous or asynchronous, depending on whether the sender waits.

- **Synchronous message:** the caller must wait until the message is done.
- **Asynchronous message:** the sender can keep processing. It does not wait for a response.

For a deeper look at this difference outside diagrams, see Synchronous vs. Asynchronous Communication.

Why this matters for documentation: arc42 is a template for documenting architecture. Its runtime view describes how building blocks work together in important scenarios. arc42 lists sequence diagrams as one of several notations for these scenarios. It recommends them because they make each participating building block's responsibility explicit. That helps teams discuss what each building block should do.

When you read an arrow in such a diagram, you can ask: does the sender wait here or not?

## Example

Imagine a web shop. The checkout part asks the payment part to charge a card. Checkout cannot continue until the charge finishes, so this is a synchronous message. Afterward, checkout tells the email part to send a receipt and moves on without waiting. That is an asynchronous message.

## Trade-offs

A synchronous caller is held up until the work is done. An asynchronous sender can keep processing, but it does not wait for a response.
