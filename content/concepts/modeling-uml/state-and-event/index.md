---
title: State and Event
slug: state-and-event
category: modeling-uml
kind: notation-element
summary: A state machine describes a system as explicit states joined by transitions. Events are what
  the machine detects and processes, one at a time, and a guard can decide which transition fires.
arc42:
- 6
- 8
step: s10-document
related:
- state-machine-diagram
- state-machine-transition
- transition-syntax
- state-entry-exit-and-do-behavior
- composite-state
- concurrent-region
- bpmn-event
- domain-event
checks:
- The document states that each event is processed completely before the next one is dispatched.
- Where several transitions react to the same event, guard conditions are given so it is clear which one
  fires.
- Signal and call triggers match the receptions and operations of the owning class.
- Long-running do activities are stated to be aborted before the exit behavior of their state.
sources:
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/15.3.12.html
  title: ''
  site: site.uottawa.ca
  accessed: '2026-11-09'
- url: https://martinfowler.com/dslCatalog/stateMachine.html
  title: State Machine
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://ar5iv.labs.arxiv.org/html/2309.14884
  title: '[2309.14884] To Do or Not to Do: Semantics and Patterns for Do Activities in UML PSSM State
    Machines'
  site: ar5iv.labs.arxiv.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/events/
  title: Overview | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://martinfowler.com/articles/201701-event-driven.html
  title: What do you mean by “Event-Driven”?
  site: martinfowler.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.puml
  caption: Two states joined by transitions. An event triggers each transition, and a guard in square
    brackets limits the first one.
review:
  status: generated
  flags: []
---

## Explanation

A state machine describes a system through named states and the transitions that connect them. An event is what moves the machine along. The machine detects an event occurrence, dispatches it, and then processes it.

**One event at a time.** The machine handles event occurrences one after another. This is called run-to-completion. No other event is dispatched until the current one is fully processed.

**Stable configuration.** Before each processing step, the machine is in a stable configuration. All entry, exit and internal activities are finished. Do activities (work that runs while the machine sits in a state) may still be running. The article State Entry, Exit and Do Behavior covers these in detail.

**Do activities.** A do activity starts once the state is entered and its entry behavior is done. It then runs independently of the state machine. The machine always aborts it before the exit behavior of that state runs.

**Triggers.** A trigger names the event that can cause a transition. Signal triggers and call triggers come from the receptions and operations of the class that owns the state machine. See Transition Syntax (Trigger, Guard, Behavior).

**Guards.** A guard is a condition on a transition. When an event occurs, guards decide which transition fires. If two transitions leave the same state, react to the same event, and both guards are true, only one fires.

**Nested states.** A state machine owns one or more regions, which in turn own vertices and transitions. See Composite State and Concurrent Region.

**The same word in other places.** In BPMN, a catch event is something the process passively waits for from outside. Fowler's event notification means a system sends event messages to tell other systems about a change in its domain. These are related uses of the word "event", not the same construct. See BPMN Event and Domain Event.

## Example

A door controller has the states Closed and Open. The event "open requested" arrives while the controller is in Closed. A guard checks that the door is unlocked. If the guard is true, the transition to Open fires. If another event arrives during that step, the controller finishes the current one first.

## Trade-offs

Run-to-completion keeps each step simple: only one event is processed at a time, so no event is cut off by a newer one. The cost is that a new event waits until the current one is fully processed. Do activities are the exception, since they run independently of the state machine and the machine may abort them.
