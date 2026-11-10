---
title: Composite State
slug: composite-state
category: modeling-uml
kind: notation-element
summary: A composite state is a state that contains inner states in one or more regions. With two or more
  regions, the regions run at the same time. Each region can have its own start and end.
arc42:
- 6
step: s10-document
related:
- state-machine-diagram
- concurrent-region
- state-machine-transition
- state-entry-exit-and-do-behavior
- state-machine-diagram-modeling-mistakes
- state-and-event
checks:
- Each region of a composite state has at most one initial state indicator.
- Fork transitions leaving a fork target states in different regions of an orthogonal state.
- Composite states with two or more regions are treated as orthogonal, with regions running concurrently.
sources:
- url: https://2022.help.altair.com/2022/embedse/compositestate.htm
  title: composite state
  site: 2022.help.altair.com
  accessed: '2026-11-09'
- url: https://www.site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/15.3.8.html
  title: ''
  site: site.uottawa.ca
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A composite state with two concurrent regions, each with its own initial and final state.
review:
  status: generated
  flags: []
---

## Explanation

A composite state is a state that has at least one region. See State Machine Diagram for the basics.

**Orthogonal composite states.** A composite state with two or more regions is called orthogonal. Each of its regions has states and transitions that can execute in parallel, but cannot transition between regions.

**Starting and finishing.** Each region may have its own initial state indicator and its own final state. A region has at most one initial indicator. An initial pseudostate is the source of a single transition to the default state of the composite state.

A transition to a final state completes the region that contains it. When all orthogonal regions complete, the enclosing composite state is complete.

**History.** History pseudostates represent a composite state's most recent configuration.
- Shallow history restores the most recent active substate of the containing state.
- Deep history restores the most recent active configuration of the composite state.

**Fork and join.** A fork splits one incoming transition into several transitions that end in different orthogonal regions, and a join merges transitions that come from different orthogonal regions. All transitions leaving a fork must target states in different regions of an orthogonal state.

## Example

Imagine a checkout screen modeled as one composite state called Checkout. It has two regions. One region tracks payment steps. The other tracks delivery choices. Each region starts at its own initial indicator and ends at its own final state. When both regions reach their final states, Checkout is complete.
