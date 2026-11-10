---
title: Process Analysis and Modeling
slug: purpose-of-process-analysis-and-modeling
category: modeling-bpmn
kind: practice
summary: Process analysis and modeling draws a picture of how work gets done. Notations such as BPMN and
  EPC make that picture shared and precise. BPMN models can also be turned into software.
arc42:
- 3
- 6
- 8
step: s03-functional-requirements
related:
- bpmn-2-0-notation-overview
- process-notations-comparison
- bpmn-swimlane-pool-and-lane
- levels-of-process-modeling
- as-is-and-to-be-view
- process-analysis
- capturing-business-behavior-via-process-modeling
- business-capability
checks:
- Process models use a named, standard notation such as BPMN 2.0 or EPC.
- Actors are shown as pools and lanes at the top-level process or collaboration, not inside subprocesses.
- Exception paths are modeled, for example with events that interrupt a subprocess.
- Where a BPMN model is meant for execution, the same model serves as documentation and as the executable
  artifact.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://www.omg.org/spec/BPMN/2.0/
  title: About the Business Process Model And Notation Specification Version 2.0
  site: omg.org
  accessed: '2026-11-08'
- url: https://www.omg.org/spec/BPMN/2.0.2/About-BPMN
  title: About the Business Process Model and Notation Specification Version 2.0.2
  site: omg.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Event-driven_process_chain
  title: Event-driven process chain - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: An order process with two lanes and an interrupting cancellation path.
review:
  status: generated
  flags: []
---

## Explanation

**Notations.** Several notations exist for modeling business processes. Two appear here.

- BPMN (Business Process Model and Notation) 2.0 is an industry standard for process modeling and execution. Its notation looks like a flowchart and does not depend on any particular implementation environment. See the article *BPMN 2.0 Notation*.
- EPC (event-driven process chain) is an ordered graph of events and functions. It is also a notation for business process modeling. See *Process Notations Comparison (EPC, BPMN, UML Activity Diagram)*.

**Who uses the models.** BPMN is aimed at the people who design, manage, and realize business processes. Its specification asks for enough precision that diagrams can be translated into software process components. That bridges business design and implementation.

**One model, two uses.** A BPMN process is an XML document that also has a visual form. So the same model can serve as documentation and as an executable artifact.

**Actors and responsibilities.** BPMN shows participants with pools and lanes. These exist only at the top-level process or collaboration level. They cannot appear inside a subprocess. See *BPMN Swimlane (Pool and Lane)*.

**Failure paths.** A model should cover more than the smooth case. In BPMN, an event can interrupt a subprocess, whichever step inside it is active.

## Example

A company models how it handles a customer order. The top-level process has two lanes: sales and warehouse. A "pack and ship" subprocess sits in the warehouse lane. A "customer cancels" event is attached to that subprocess. If the event fires, the subprocess stops, whichever step is running, and the process follows the cancellation path. Business staff read the diagram. The same model can also be handed to a system to run.

## Trade-offs

Lanes work only at the top level. They cannot be added inside a subprocess.
