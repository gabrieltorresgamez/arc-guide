---
title: State Entry, Exit and Do Behavior
slug: state-entry-exit-and-do-behavior
category: modeling-uml
kind: notation-element
summary: A state can carry its own entry, do and exit behavior. Entry and exit run every time the state
  is entered or left. The do activity runs in between and can be aborted.
arc42:
- 6
- 8
step: s10-document
related:
- state-machine-diagram
- state-machine-transition
- state-and-event
- transition-syntax
- composite-state
- state-machine-diagram-modeling-mistakes
checks:
- Entry and exit behaviors are attached to states, not duplicated on each transition.
- Events that must not restart a state or abort its do activity are modeled as internal transitions, not
  self-transitions.
- A state with a do activity has an outgoing completion transition, or an event transition that interrupts
  it.
sources:
- url: https://www.boost.org/latest/doc/antora/msm/uml-short-guide.html
  title: 'UML short guide :: Boost Libraries Documentation'
  site: boost.org
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2309.14884v3
  title: 'To Do or Not to Do: Semantics and Patterns for Do Activities in UML PSSM State Machines'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/UML_state_machine
  title: UML state machine - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A state with entry, do and exit behavior.
review:
  status: generated
  flags: []
---

## Explanation

A state in a state machine can own behavior. (See State Machine Diagram for the basics.) Three kinds exist: entry, do and exit.

**Entry and exit belong to the state.** They do not belong to any transition. So they run whenever the state is entered or left, no matter which path was taken.

**The do activity runs in between.** It starts only after the state is entered and the entry behavior has finished. It is an ongoing activity that lasts while the state is active.

**Leaving a state aborts the do activity.** The do activity is aborted when its state is exited. A do activity may also be interrupted by an event.

**Finishing normally.** When the do activity finishes, an outgoing completion transition can move the machine to the next state. A completion transition has no event of its own. The source state generates a completion event only after its entry behavior and its do activity have both completed. The transition then fires, unless a guard (a condition on the transition) forbids it.

**Internal transitions.** An internal transition handles an event inside the state. It acts like a self-transition without entry or exit actions. A self-transition leaves and re-enters the state, so it runs exit and entry actions. An internal transition never does.

**Why it matters for modeling.** Entry and exit actions are tied to states. For that reason, statecharts behave like Moore machines. Event-dependent actions placed on transitions are Mealy-like.

## Example

A state named "Heating" in a kettle model:

- entry: switch the heating element on
- do: monitor the water temperature
- exit: switch the heating element off

The kettle may leave "Heating" because the water is hot or because someone lifts it off the base. Either way, leaving the state aborts the monitoring, and the exit behavior switches the element off. If the kettle only reports a temperature reading, an internal transition can handle that event.

## Trade-offs

Putting behavior on the state avoids repeating it on every incoming or outgoing transition. The cost is that it runs on every entry and exit, including self-transitions. If you want to react to an event without that, use an internal transition instead.
