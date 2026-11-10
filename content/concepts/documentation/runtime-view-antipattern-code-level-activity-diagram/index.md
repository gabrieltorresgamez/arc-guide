---
title: 'Runtime View Antipattern: Code-Level Activity Diagram'
slug: runtime-view-antipattern-code-level-activity-diagram
category: documentation
kind: concept
summary: A runtime view that draws code-level steps, such as package or script names, repeats what the
  source code already shows. It leaves out which building blocks work together and who is responsible
  for what.
arc42:
- 6
step: s10-document
related:
- runtime-view
- unclear-level-of-abstraction-antipattern
- component-view-antipattern-lifting-code-to-model-level
- sequence-diagram
- bpmn-swimlane-pool-and-lane
- responsibility-allocation
- architectural-overview-antipatterns
- self-documentation
checks:
- Each runtime scenario was chosen for its architectural relevance, and the set is a representative selection.
- Scenarios refer to building blocks, not to code-level elements such as package or script names.
- Each scenario assigns activities to building blocks, so responsibilities are visible.
- Activity diagrams use swimlanes for actors or building blocks.
- Detailed single-execution scenarios exist only where stakeholders need them.
sources:
- url: https://docs.arc42.org/tips/6-3/
  title: 'Tip 6-3: Document ‘schematic’ (instead of detailed) scenarios! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/6-1/
  title: 'Tip 6-1: Always map existing building blocks to the activities within runtime scenarios! | arc42
    Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/6-4/
  title: 'Tip 6-4: Document detailed scenarios (with caution)! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/6-7/
  title: 'Tip 6-7: Use activity diagrams with swimlanes to describe or specify runtime scenarios! | arc42
    Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-6-3/
  title: 'Question C-6-3: How can I describe scenarios or execution flows? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A runtime view shows how a system behaves while it runs. It describes how the system fulfills a task and which building blocks take part (see the article Runtime View).

**Why this is a problem**

- Detailed scenarios amount to visualizing single executions of source code. They take immense effort to create and maintain, and very detailed diagrams can be hard to read.
- arc42 advises documenting details with caution, and only if stakeholders really need them.

**What to do instead**

- Choose scenarios by architectural relevance. A small, representative selection beats many scenarios.
- Write schematic scenarios. They refer to higher-level building blocks, not to code-level elements.
- Map building blocks to activities. This assigns responsibilities to the building blocks.
- Many notations are possible, for example numbered steps, activity diagrams, sequence diagrams, BPMN and state machines.
- If you use an activity diagram, use swimlanes. They group activities by actor or building block.
- The arc42 FAQ also suggests a numbered list that names the building block doing each step, or a sequence diagram that maps building blocks to their actions.

## Example

A team documents a "system health check" scenario. The first draft is an activity diagram with three parallel branches and notes naming a code package and a script. A reader learns what the code does, but not which building block owns the check.

The team redraws it as a numbered list. Step 1: the Monitor block asks the Gateway block for status. Step 2: the Gateway block asks each connected system. Step 3: the Monitor block reports the result. Now the reader sees who collaborates and who is responsible.

## Trade-offs

Schematic scenarios leave out detail. That is often enough, because developers tend to look for details in the source code anyway. When stakeholders really need a detailed scenario, arc42 allows one, but only with caution. Detailed diagrams also take immense effort to create and maintain.
