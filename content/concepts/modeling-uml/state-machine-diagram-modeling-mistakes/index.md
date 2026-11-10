---
title: State Machine Diagram Modeling Mistakes
slug: state-machine-diagram-modeling-mistakes
category: modeling-uml
kind: concept
summary: State machine diagrams go wrong when start and end markers are misused, when completion transitions
  compete, or when guards overlap. Knowing these errors helps you build models with one clear behavior.
arc42:
- 5
- 6
- 8
step: s10-document
related:
- state-machine-diagram
- state-machine-transition
- transition-syntax
- composite-state
- concurrent-region
- state-and-event
- state-entry-exit-and-do-behavior
- uml-modeling-anti-patterns
checks:
- Each region has an initial pseudostate with a single transition to the default state.
- Completion transitions leaving the same state have mutually exclusive guards.
- Where an else transition is used, it is the fallback for a source whose other guards can all be false.
- Entry and exit points appear only on a state machine or a composite state.
- A final state is used where a region is meant to complete.
sources:
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/15.3.14.html
  title: ''
  site: site.uottawa.ca
  accessed: '2026-11-09'
- url: https://www.visual-paradigm.com/VPGallery/diagrams/State.html
  title: State Machine Diagram - UML Diagrams - Unified Modeling Language Tool
  site: visual-paradigm.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Disjoint guards with an else branch leave one clear choice.
review:
  status: generated
  flags: []
---

## Explanation

A state machine diagram shows the states an object can be in and the transitions between them (see State Machine Diagram and State Machine Transition). Most mistakes fall into a few groups.

**Initial and final markers**

- An initial pseudostate is the starting marker. It is the source of a single transition to the default state.
- A final state means the enclosing region is completed. Use it when the behavior is meant to end.

**Completion transitions**

- A completion transition has no explicit trigger. An implicit completion event fires it.
- Completion events are dispatched ahead of other pooled events.
- If one state has several completion transitions, give them mutually exclusive guards.

**Guards and the else branch**

- A guard is a condition on a transition.
- For a junction, a predefined "else" guard may be defined for at most one outgoing transition. That transition is enabled if all the guards on the other outgoing transitions are false.

**Entry and exit points**

- Entry and exit point pseudostates belong to a state machine or a composite state.
- A composite state contains other states (see Composite State).

**Transition kinds**

- UML defines three transition kinds: external, internal and local. Choose the kind on purpose.

## Example

A "Payment" object leaves the "Checking" state through two completion transitions. One has the guard [amount <= limit] and goes to "Approved". The other has the guard [amount >= limit] and goes to "Declined". At exactly the limit, both guards are true, which breaks the recommendation that completion transitions have mutually exclusive guards.
