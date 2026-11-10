---
title: Process Notations Comparison (EPC, BPMN, UML Activity Diagram)
slug: process-notations-comparison
category: modeling-bpmn
kind: concept
summary: EPC, UML activity diagrams, and BPMN can describe the same process with different elements. Most
  EPC elements have a clear BPMN equivalent, so conversion follows rules, but the result usually needs
  manual cleanup.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-2-0-notation-overview
- aris-process-views
- history-of-bpmn
- bpmn-core-elements
- bpmn-gateway-semantics
- uml-unified-modeling-language
- bpmn-event
- foundation-for-execution
checks:
- When EPC models are converted to BPMN, the result is reviewed for unnecessary intermediate events.
- 'The conversion mapping is stated: functions to tasks, events to events, connectors to gateways.'
- The document states whether EPC roles become BPMN lanes or remain roles.
sources:
- url: https://www.gbtec.com/blog/from-epc-to-bpmn/
  title: 'EPC to BPMN Conversion: What to Expect | GBTEC'
  site: gbtec.com
  accessed: '2026-11-09'
- url: https://doc.scheer-pas.com/business-modeler/latest/epc-to-bpmn-conversion
  title: EPC to BPMN Conversion | Business Modeler | Scheer PAS Documentation
  site: doc.scheer-pas.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Event-driven_process_chain
  title: Event-driven process chain - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Activity_diagram
  title: Activity diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://ariscommunity.com/users/ivo/2011-04-11-bpmn-vs-epc-revisited-part-1
  title: BPMN vs. EPC revisited, part 1 | ARIS BPM Community
  site: ariscommunity.com
  accessed: '2026-11-09'
- url: https://ariscommunity.com/users/robpotter/2011-05-04-transitioning-epc-bpmn-any-experiences-people-are-able-share
  title: Transitioning from EPC to BPMN - Any experiences people are able to share? | ARIS BPM Community
  site: ariscommunity.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'An EPC order chain converted to BPMN: the redundant middle event is dropped.'
review:
  status: generated
  flags: []
---

## Explanation

A process notation is a set of symbols and rules for drawing how work flows. Three are common: the Event-driven Process Chain (EPC), the UML activity diagram, and BPMN. See the articles "BPMN 2.0 Notation" and "Unified Modeling Language (UML)" for background.

**EPC.** It was developed in 1992 at Saarland University in a research project with SAP, and it is an essential element of ARIS. It has functions, which are active elements, and events, which are passive and drawn as hexagons. Connectors (XOR, AND, and OR) split and join branches. As a rule, an EPC diagram begins and ends with an event.

**BPMN.** Its basic building blocks are tasks, which are small units of work. Gateways route the flow. An exclusive gateway picks one path based on data. A parallel gateway forks paths that run side by side. BPMN is also an XML document with a visual form, and workflow engines can interpret it.

**UML activity diagram.** It uses actions and decisions. Bars represent the start (split) or end (join) of concurrent activities. Object nodes carry data between actions along object flows.

**Mapping.**

| Idea | EPC | UML activity | BPMN |
|---|---|---|---|
| Something that happens | Event | not covered here | Event |

Responsibilities need a separate decision: EPC attaches roles or organizational units to functions, while BPMN typically uses pools, lanes, or resource assignments.

**Converting EPC to BPMN.**
- Functions typically become tasks, events remain events, and logical connectors can be mapped to gateways.
- Scheer's tool converts by predefined rules. The result may need manual correction.
- One practitioner who translated about 120 EPCs into BPMN reported finding many unnecessary intermediate events that came from direct translation of EPC events.

## Example

A team has an EPC for handling an order. It reads: event "Order received", function "Check order", event "Order checked", function "Ship order". Converting it directly gives a BPMN start event, a task, an intermediate event, and another task. The middle event "Order checked" only restates that the task finished. The team removes it and connects the two tasks directly. They also decide whether the EPC roles become lanes.

## Trade-offs

EPC's simplicity is claimed as a major strength. One practitioner on a forum found BPMN more complex than EPC and recommended real training before starting it. Automatic conversion may still need manual adjustments and a careful review. Direct translation of EPC events can produce unnecessary intermediate events in the BPMN model.
