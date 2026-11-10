---
title: Transition Syntax (Trigger, Guard, Behavior)
slug: transition-syntax
category: modeling-uml
kind: notation-element
summary: A UML transition moves a state machine from one state to another. Its label can name a trigger
  (the event), a guard (a condition in brackets), and a behavior (what runs after the slash).
arc42:
- 6
- 8
step: s10-document
related:
- state-machine-transition
- state-machine-diagram
- state-and-event
- state-entry-exit-and-do-behavior
- state-machine-diagram-modeling-mistakes
- composite-state
checks:
- Guards on transitions that compete for the same event do not overlap.
- Transitions without a trigger are intended as completion transitions, and each has a guard where it
  should not always fire.
- Each transition that should skip entry and exit behavior is modeled as an internal transition, not an
  external one.
sources:
- url: https://showa-yojyo.github.io/notebook/omg15/ch14-statemachines.html
  title: 14 StateMachines — 読書ノート 1.8dev
  site: showa-yojyo.github.io
  accessed: '2026-11-09'
- url: https://www.boost.org/latest/doc/antora/msm/uml-short-guide.html
  title: 'UML short guide :: Boost Libraries Documentation'
  site: boost.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A transition labeled with trigger, guard, and behavior.
review:
  status: generated
  flags: []
---

## Explanation

A transition is an arrow between states in a state machine. The label on the arrow can have three parts: a trigger, a guard, and an effect. The notation is `trigger [guard] / behavior`. See State Machine Transition and State Machine Diagram for the wider picture.

**Trigger.** The trigger names the event that can set the transition off. A trigger is enabled when the event that arrives matches the trigger's event type. See State and Event for what an event is.

**Guard.** The guard is an extra condition on the transition. A transition may have one. If it has none, it is treated as if its guard were always true.

**Effect.** A transition may have an effect, which is a behavior. It runs when the transition is traversed, meaning when the machine actually takes it.

**Transitions without a trigger.** A transition can have no trigger. A completion event enables it. This is a completion (anonymous) transition. It fires as soon as its source state becomes active, as long as its guard allows.

**External and internal transitions.** An external transition runs the exit behavior of its source state. An internal transition stays inside the active state's scope. It acts like a self-transition, but no entry or exit action is called. See State Entry, Exit and Do Behavior.

**Competing transitions.** If several transitions compete, their guards must not overlap. The UML standard asks for this. Overlapping guards are a modeling mistake. See State Machine Diagram Modeling Mistakes.

## Example

A card reader waits in an "Idle" state. A transition to "Active" is labeled `card inserted [card valid] / show welcome`.

- The trigger is the event "card inserted".
- The guard is "card valid".
- The effect is "show welcome".

When a card arrives, the trigger matches. The machine then checks the guard. If the guard is true, the transition is traversed and "show welcome" runs.

## Trade-offs

Guards let one trigger lead to different transitions. That only works when the guards do not overlap. If two guards can both be true, the model does not say which transition fires.
