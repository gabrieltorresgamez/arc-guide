---
title: UML State Machine Diagram
slug: uml-state-machine-diagram
order: 30
category: modeling-uml
kind: notation-element
summary: A state machine diagram shows the states an object or behavior can be in. It also shows the events
  that move it between states, and what happens on each move.
arc42:
- 6
- 8
step: s10-document
related:
- uml-behavioral-diagram
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
- url: https://2022.help.altair.com/2022/embedse/compositestate.htm
  title: composite state
  site: 2022.help.altair.com
  accessed: '2026-11-09'
- url: https://www.site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/15.3.8.html
  title: "15.3.8 Pseudostate"
  site: site.uottawa.ca
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2407.17215
  title: Formalizing UML State Machines for Automated Verification – A Survey
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://content.helpme-codesys.com/de/CODESYS%20UML/_uml_elem_composite_state.html
  title: 'Element: Zusammengesetzter Zustand'
  site: content.helpme-codesys.com
  accessed: '2026-11-09'
- url: https://content.helpme-codesys.com/de/CODESYS%20UML/_uml_elem_fork_and_join.html
  title: 'Element: Gabelung/Verbindung'
  site: content.helpme-codesys.com
  accessed: '2026-11-09'
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/15.3.12.html
  title: "15.3.12 StateMachine"
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
- url: https://www.boost.org/latest/doc/antora/msm/uml-short-guide.html
  title: 'UML short guide :: Boost Libraries Documentation'
  site: boost.org
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2309.14884v3
  title: 'To Do or Not to Do: Semantics and Patterns for Do Activities in UML PSSM State Machines'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://webel.com.au/taxonomy/term/758
  title: TransitionKind | Webel IT Australia
  site: webel.com.au
  accessed: '2026-11-09'
- url: https://showa-yojyo.github.io/notebook/omg15/ch14-statemachines.html
  title: 14 StateMachines — 読書ノート 1.8dev
  site: showa-yojyo.github.io
  accessed: '2026-11-09'
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/15.3.14.html
  title: "15.3.14 Transition"
  site: site.uottawa.ca
  accessed: '2026-11-09'
- url: https://www.visual-paradigm.com/VPGallery/diagrams/State.html
  title: State Machine Diagram - UML Diagrams - Unified Modeling Language Tool
  site: visual-paradigm.com
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

A transition label can carry a guard and an effect. The guard is a condition in square brackets. The effect comes after a slash.

The event on a transition may be omitted. In that case the state changes once the activities of the previous state have finished.

**Behavior inside a state**

A state may have an entry behavior, a do behavior and an exit behavior. The entry action runs when the state is entered. The exit action runs whenever the state is left. The do action repeats as long as the state does not change.

**Branching**

- A junction joins several transitions into compound paths.
- A choice is a dynamic conditional branch. If no guard on its outgoing transitions is true, the model is ill formed.

**Nesting and reuse**

- Composite states contain other states. They can hold several regions that model parallel behavior.
- When a composite state is left, exit starts at the innermost active state.
- A submachine state lets you reuse one state machine specification many times. Its connection points match entry and exit points in the referenced machine.

**More about state machine elements.**

- **Composite State:** A composite state is a state that contains inner states in one or more regions. With two or more regions, the regions run at the same time. Each region can have its own start and end.
- **Concurrent Region:** A concurrent region is one of several parts of a composite state. Each region has its own start and end.
- **State and Event:** A state machine describes a system as explicit states joined by transitions. Events are what the machine detects and processes, one at a time, and a guard can decide which transition fires.
- **State Entry, Exit and Do Behavior:** A state can carry its own entry, do and exit behavior. Entry and exit run every time the state is entered or left. The do activity runs in between and can be aborted.
- **State Machine Transition:** A state machine transition is the switch from one active state to another, triggered by an event. A guard can block it. Transitions can be external, local, or internal, which differ in whether they leave the state.
- **Transition Syntax (Trigger, Guard, Behavior):** A UML transition moves a state machine from one state to another. Its label can name a trigger (the event), a guard (a condition in brackets), and a behavior (what runs after the slash).

## Example

Picture a simple online order. It starts in *Created*. A payment event moves it to *Paid*, but only if the amount is correct (the guard). The effect sends a receipt. From *Paid*, a shipping event moves it to *Shipped*, and then it reaches a final state. The same event, such as "cancel", could be handled differently in each state.

## Trade-offs

Nesting, parallel regions and reusable submachines let you structure large behavior. A choice whose guards do not cover every case makes the model ill formed. Check that at least one guard is always true.
