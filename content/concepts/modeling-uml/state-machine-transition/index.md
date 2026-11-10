---
title: State Machine Transition
slug: state-machine-transition
category: modeling-uml
kind: notation-element
summary: A state machine transition is the switch from one active state to another, triggered by an event.
  A guard can block it. Transitions can be external, local, or internal, which differ in whether they
  leave the state.
arc42:
- 5
- 6
- 8
step: s10-document
related:
- transition-syntax
- state-machine-diagram
- state-and-event
- composite-state
- state-entry-exit-and-do-behavior
- state-machine-diagram-modeling-mistakes
checks:
- Each transition that must not always fire has a guard, and the guard is a yes/no check.
- Transitions without a trigger are intentional completion transitions, and any guard on them is stated.
- Internal transitions are documented somewhere other than as arrows, since diagrams do not draw them.
- Local transitions appear only inside composite states.
- Events that a state defers are identified, because they are kept and not processed while that state
  is active.
sources:
- url: https://www.boost.org/latest/doc/antora/msm/uml-short-guide.html
  title: 'UML short guide :: Boost Libraries Documentation'
  site: boost.org
  accessed: '2026-11-09'
- url: https://webel.com.au/taxonomy/term/758
  title: TransitionKind | Webel IT Australia
  site: webel.com.au
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A guarded transition from Placed to Paid, and a trigger-free completion transition from Paid
    to Shipped.
review:
  status: generated
  flags: []
---

## Explanation

A state machine describes the states an object can be in. A **transition** is the switch from one active state to another. An event triggers it (see State and Event).

**Guard.** A guard is a yes/no check. The system runs it first. If it returns false, the transition does not fire.

**Completion transitions.** Some transitions have no trigger event. They are called completion (or anonymous) transitions. They fire as soon as their source state becomes active, unless a guard blocks them.

**Kinds of transitions.** The kind tells you whether the source state is left:

- An *external* transition exits its source state.
- A *local* transition exists only inside a composite state (see Composite State). It does not exit that containing state.
- An *internal* transition runs inside the source state. It does not exit or enter that state. It can only be defined when the source is a state.

Internal transitions are not shown explicitly in diagrams.

**Deferred events.** A state can defer an event. While that state is active, the system does not process the event. It keeps the event for later.

For the label format of trigger, guard, and effect, see Transition Syntax (Trigger, Guard, Behavior).

## Example

Picture an order object with the states "Placed" and "Paid".

The event "payment received" triggers a transition from "Placed" to "Paid". A guard checks the amount. If the check returns false, the transition does not fire and the order stays in "Placed".

Now suppose "Paid" has a transition with no trigger. It fires as soon as "Paid" becomes active, unless its guard blocks it.

## Trade-offs

Internal transitions keep a state active, so they avoid leaving and re-entering it. Completion transitions fire as soon as their source state becomes active, unless a guard blocks them.
