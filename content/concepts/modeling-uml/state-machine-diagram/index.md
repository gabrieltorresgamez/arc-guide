---
title: State Machine Diagram
slug: state-machine-diagram
category: modeling-uml
kind: notation-element
summary: A state machine diagram shows the states an object or behavior can be in. It also shows the events
  that move it between states, and what happens on each move.
arc42:
- 6
- 8
step: s10-document
related:
- state-machine-transition
- transition-syntax
- state-entry-exit-and-do-behavior
- composite-state
- concurrent-region
- state-and-event
- state-machine-diagram-modeling-mistakes
- behavior-diagram
checks:
- Each region has at most one initial vertex.
- Every choice pseudostate has outgoing guards that cover all cases, so at least one is true.
- Transition labels write the guard in square brackets and the effect after a slash.
- Any use of a terminate pseudostate is intentional, since it stops the whole state machine immediately.
sources:
- url: https://en.wikipedia.org/wiki/UML_state_machine
  title: UML state machine - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.webel.com.au/node/424
  title: Unified Modeling Language 2.5.1 | Webel IT Australia
  site: webel.com.au
  accessed: '2026-11-09'
- url: https://www.sparxsystems.eu/languages/uml/diagrams/statediagram/
  title: 'UML State Diagram: Sequence of states'
  site: sparxsystems.eu
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'A small state machine: initial transition, a transition with guard and effect, and a final
    state.'
review:
  status: generated
  flags: []
---

## Explanation

A state machine diagram draws the life of something as **states** and **transitions**. A state is a situation the thing can be in. A transition is a move from one state to another.

**Where it starts and ends**

- The initial transition starts at a solid circle. It points to the default state.
- A region can have at most one initial vertex, meaning one starting point.
- Entering a final state means the enclosing region has completed.
- Entering a terminate pseudostate stops the whole state machine at once.

**Transition labels**

A transition label can carry a guard and an effect. The guard is a condition in square brackets. The effect comes after a slash. See State Machine Transition and Transition Syntax (Trigger, Guard, Behavior).

The event on a transition may be omitted. In that case the state changes once the activities of the previous state have finished.

**Behavior inside a state**

A state may have an entry behavior, a do behavior and an exit behavior. The entry action runs when the state is entered. The exit action runs whenever the state is left. The do action repeats as long as the state does not change. See State Entry, Exit and Do Behavior.

**Branching**

- A junction joins several transitions into compound paths.
- A choice is a dynamic conditional branch. If no guard on its outgoing transitions is true, the model is ill formed.

**Nesting and reuse**

- Composite states contain other states. They can hold several regions that model parallel behavior. See Composite State and Concurrent Region.
- When a composite state is left, exit starts at the innermost active state.
- A submachine state lets you reuse one state machine specification many times. Its connection points match entry and exit points in the referenced machine.

## Example

Picture a simple online order. It starts in *Created*. A payment event moves it to *Paid*, but only if the amount is correct (the guard). The effect sends a receipt. From *Paid*, a shipping event moves it to *Shipped*, and then it reaches a final state. The same event, such as "cancel", could be handled differently in each state.

## Trade-offs

Nesting, parallel regions and reusable submachines let you structure large behavior. Nesting combined with entry and exit actions also makes transition semantics more complicated, because several states can be active at once. A choice whose guards do not cover every case makes the model ill formed. Check that at least one guard is always true.
