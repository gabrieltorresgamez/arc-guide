---
title: Concurrent Region
slug: concurrent-region
category: modeling-uml
kind: notation-element
summary: A concurrent region is one of several parts of a composite state. An object in such a state sits
  in all its regions at once. Each region has its own start and end.
arc42:
- 6
- 8
step: s10-document
related:
- composite-state
- state-machine-diagram
- state-machine-transition
- state-and-event
- transition-syntax
- state-machine-diagram-modeling-mistakes
checks:
- Each orthogonal composite state has at least two regions.
- Each region has its own initial state and final state.
- No transition connects states that lie in different regions.
- Fork transitions end in different regions and carry no guard or trigger.
- Leaving the composite state by completion is modeled as requiring all regions to reach their final states,
  for example through a join.
sources:
- url: https://arxiv.org/html/2407.17215
  title: Formalizing UML State Machines for Automated Verification – A Survey
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/UML_state_machine
  title: UML state machine - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://content.helpme-codesys.com/de/CODESYS%20UML/_uml_elem_composite_state.html
  title: 'Element: Zusammengesetzter Zustand'
  site: content.helpme-codesys.com
  accessed: '2026-11-09'
- url: https://content.helpme-codesys.com/de/CODESYS%20UML/_uml_elem_fork_and_join.html
  title: 'Element: Gabelung/Verbindung'
  site: content.helpme-codesys.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: An order in fulfillment with two parallel regions, entered by a fork and left by a join.
review:
  status: generated
  flags: []
---

## Explanation

A state machine shows the states an object can be in. A composite state groups other states inside it (see Composite State). An orthogonal composite state has two or more regions. Each region is a separate area inside the composite state. Regions let a diagram show concurrency, meaning several things happening at the same time.

Being in such a composite state means being in all of its regions simultaneously.

**Start and end.** Regions may have an initial state and a final state. When the composite state has an outgoing completion transition, each region contains a start state and an end state.

**Completion.** The composite state reaches its end only when all regions have reached their final states. One finished region is not enough.

**No crossing.** A transition between states in different regions is not allowed. Regions stay separate from each other.

**Fork and join.** Two special markers, called pseudostates, show how control enters and leaves regions explicitly:

- A fork splits one incoming transition into several transitions. These must end in different regions of the composite state. Transitions leaving a fork cannot have a guard or a trigger.
- A join is a shared target for transitions coming from different regions. Its outgoing transition fires only after all incoming transitions have run.

**Terminate.** Entering a terminate pseudostate ends the state machine's execution immediately. It performs no further behavior.

## Example

Picture an order in an online shop. While it is "In fulfillment", it has two regions. One region tracks payment: pending, then paid. The other tracks packing: waiting, then packed. Both regions run side by side. A fork sends the order into both regions at once. A join waits until payment is paid and packing is packed. Only then does the order move on to "Ready to ship". Payment steps never jump directly into packing steps.
