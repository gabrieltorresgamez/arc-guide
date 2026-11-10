---
title: Levels of Process Modeling
slug: levels-of-process-modeling
category: modeling-bpmn
kind: concept
summary: Process models work best in levels. The top level shows the big picture, the middle level breaks
  it into subprocesses, and the lowest level shows detailed activities. Each level suits a different audience.
arc42:
- 5
- 6
step: s10-document
related:
- bpmn-swimlane-pool-and-lane
- bpmn-activity
- bpmn-collaboration-diagram
- process-model-complexity
- bpmn-modeling-tips
- bpmn-2-0-notation-overview
- unclear-level-of-abstraction-antipattern
- capturing-business-behavior-via-process-modeling
checks:
- The top-level end-to-end diagram shows all participating pools, including external parties.
- Readability and traceability, including the choreography between pools, hold from the top level to the
  bottom level.
- Subprocess detail sits in separate child diagrams reached through collapsed subprocesses, not mixed
  into the parent diagram.
- Processes reused in several places are modeled as call activities that reference an independently defined
  process.
- The level of detail of each diagram fits its audience, with high-level views for leadership and detailed
  maps for analysts.
sources:
- url: https://www.signavio.com/wiki/process-discovery/business-process-mapping-levels/
  title: Business Process Mapping Levels - SAP Signavio
  site: signavio.com
  accessed: '2026-11-09'
- url: https://www.bpminstitute.org/resources/articles/bpms-watch-organizing-complex-bpmn-models/
  title: 'BPMS Watch: Organizing Complex BPMN Models | BPMInstitute.org'
  site: bpminstitute.org
  accessed: '2026-11-09'
- url: https://www.trisotech.com/bpmn-call-activity-vs-subprocess-whats-the-difference/
  title: 'BPMN Call Activity vs Subprocess: What''s the Difference?'
  site: trisotech.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/call-activities/
  title: Call activities | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A top-level process with a subprocess (child level with its own activities) and a call activity
    that invokes a reusable process.
review:
  status: generated
  flags: []
---

## Explanation

A large process model is hard to read on one page. Splitting it into levels keeps each page understandable.

**Decomposition**

Subprocess detail moves into child diagrams. A child diagram can contain further subprocesses, each with its own child diagram. Real end-to-end models can therefore nest over many levels. Each modeling tool has its own way of keeping the pieces together; in one tool, each sheet is what the tool calls a process level.

**Roles apply at every level**

The top-level diagram should show every participant, drawn as a pool. This includes external parties. A pool is a BPMN shape for one participant (see BPMN Swimlane (Pool and Lane)). Readability and traceability must hold from top to bottom. That includes the choreography, meaning the exchanges between the pools.

**Linking levels in BPMN**

- A collapsed subprocess is drawn as a small box that links to a separate child diagram. Silver prefers this form. The expanded form mixes parent and child on one diagram, and Silver rarely uses it.
- A call activity invokes an independently defined process. That process can be reused. The child level of a subprocess is only a diagram fragment and is not reusable.
- Camunda also describes call activities as reusable subprocesses.

## Example

A company models its order handling. The top-level diagram shows the customer, the company and an external carrier as pools, with a few large steps between them. One of those steps, "Fulfill order", is a subprocess. Its child diagram lists the detailed activities and decisions. One step in that child diagram, "Check payment", calls a separate payment process that other processes also use.

## Trade-offs

Levels keep each diagram readable, but the reader must move between several diagrams to see the whole flow. Choreography between pools must stay traceable across all of them, which takes care. Collapsed subprocesses keep levels apart, but the child level has no independent definition outside the larger process. A call activity gives reuse, but it needs a separately defined process.
