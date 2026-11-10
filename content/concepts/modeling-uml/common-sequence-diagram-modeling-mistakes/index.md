---
title: Common Sequence Diagram Mistake
slug: common-sequence-diagram-modeling-mistakes
category: modeling-uml
kind: concept
summary: Many sequence diagram errors come from arrow styles. Replies, asynchronous messages, and lost
  or found messages are the usual trouble spots. Knowing what each arrowhead and line style means helps
  you catch them.
arc42:
- 6
step: s10-document
related:
- sequence-diagram
- message-types-in-sequence-diagrams
- synchronous-vs-asynchronous-communication
- runtime-view
- uml-modeling-anti-patterns
- common-class-diagram-modeling-mistakes
- uml-modeling-best-practice
checks:
- Every synchronous call (filled arrowhead) has a dashed reply arrow with an open arrowhead.
- Asynchronous messages have no reply arrow.
- Asynchronous messages are marked by an open arrowhead, not by a dashed line.
- Found messages start at a filled circle, and lost messages end at one.
sources:
- url: https://www.sparxsystems.eu/languages/uml/diagrams/sequencediagram/
  title: 'UML Sequence Diagram: chronological sequence'
  site: sparxsystems.eu
  accessed: '2026-11-09'
- url: https://schematex.js.org/research/uml-synchronous-vs-asynchronous-message-arrows
  title: 'UML synchronous vs asynchronous messages: a 202 Accepted worked sequence | Schematex Research'
  site: schematex.js.org
  accessed: '2026-11-09'
- url: https://www.visual-paradigm.com/guide/mastering-uml-sequence-diagrams-a-comprehensive-guide-from-basic-notation-to-advanced-decomposition/
  title: 'Mastering UML Sequence Diagrams: A Comprehensive Guide from Basic Notation to Advanced Decomposition'
  site: visual-paradigm.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A synchronous call with a dashed reply, and an asynchronous message with no reply.
review:
  status: generated
  flags: []
---

## Explanation

A sequence diagram shows how parts of a system exchange messages over time (see UML Sequence Diagram).

**Lifelines.** Each object sits on a vertical dashed line. The object's rectangle plus that line form the lifeline.

**Synchronous calls and replies.**
- A synchronous call uses a filled arrowhead. The caller waits.
- The reply is a dashed line with an open arrowhead.
- Return arrows are optional. Sequence diagrams usually draw only the method calls, and a return can be shown with a dashed arrow if wanted.

**Asynchronous messages.**
- An asynchronous caller does not wait. It continues right away.
- So an asynchronous call has no response arrow, and no return is modeled.
- The open arrowhead marks a message as asynchronous. The dashed stroke does not.
- Some informal diagrams use dashes to mean "delayed" or "background". In UML, dashes mean a reply, so a dashed "async" arrow is wrong.

**Found and lost messages.**
- A found message starts at a filled circle. Its sender is unknown or external.
- A lost message points to a filled circle. Its sender is known, but its recipient is not.

**Parallel fragments.** In a `par` fragment, events in different operands may happen in any interleaved order. This shows concurrency. Do not read the operands as a fixed sequence.

For message types in more depth, see Message Types in Sequence Diagrams.

## Example

A web shop diagram shows an order service calling a payment service. The call "charge card" is a filled arrow, so the order service waits. The payment service answers with a dashed arrow with an open head. Later, the order service sends "notify warehouse" as an asynchronous message with an open arrowhead. It does not wait, so the diagram draws no reply. A reviewer who sees a dashed arrow back from the warehouse should flag it.
