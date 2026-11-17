---
title: BPMN 2.0 Notation
slug: bpmn-2-0-notation
order: 10
category: modeling-bpmn
kind: standard
summary: BPMN 2.0 is an industry standard notation for modeling and running business processes. Its core
  elements are tasks, events, gateways, and sequence flow, which together show the order of work.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-core-elements
- bpmn-event
- bpmn-gateway
- bpmn-activity
- bpmn-swimlane-pool-and-lane
- runtime-view
checks:
- Each process model uses sequence flow to show the order of steps.
- Every outgoing flow of an event-based gateway leads to an intermediate catch event.
- Boundary events are modeled as intermediate catch events, and each is marked as interrupting or not
  on purpose.
- Inclusive gateways have conditions on their outgoing flows and a default flow.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/events/
  title: Overview | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/event-based-gateways/
  title: Event-based gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/inclusive-gateways/
  title: Inclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://www.omg.org/spec/BPMN/2.0/
  title: About the Business Process Model And Notation Specification Version 2.0
  site: omg.org
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
  title: Business Process Model and Notation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://www.trisotech.com/bpmn-introduction-and-history/
  title: BPMN Introduction and History
  site: trisotech.com
  accessed: '2026-11-09'
- url: https://www.omg.org/spec/BPMN/2.0.1/About-BPMN
  title: About the Business Process Model And Notation Specification Version 2.0.1
  site: omg.org
  accessed: '2026-11-09'
- url: https://www.omg.org/spec/BPMN/About-BPMN/
  title: About the Business Process Model and Notation Specification Version 2.0.2
  site: omg.org
  accessed: '2026-11-09'
- url: https://www.omg.org/spec/BPMN/2.0.2/About-BPMN
  title: About the Business Process Model and Notation Specification Version 2.0.2
  site: omg.org
  accessed: '2026-11-09'
- url: https://www.omg.org/bpmn/
  title: Business Process Model & Notation™ (BPMN™) | Object Management Group
  site: omg.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/
  title: Modeling with BPMN | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/message-events/
  title: Message events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://researchwith.stevens.edu/en/publications/how-much-language-is-enough-theoretical-and-practical-use-of-the-/
  title: How much language is enough? Theoretical and practical use of the business process modeling notation
    - Stevens Institute of Technology
  site: researchwith.stevens.edu
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
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
- url: https://github.com/bpmn-io/bpmn-js
  title: 'GitHub - bpmn-io/bpmn-js: A BPMN 2.0 rendering toolkit and web modeler. · GitHub'
  site: github.com
  accessed: '2026-11-09'
- url: https://camunda.com/platform/modeler/
  title: Camunda Modeler | BPMN Process Modeler | Camunda
  site: camunda.com
  accessed: '2026-11-09'
- url: https://bpmn.io/
  title: Web-based tooling for BPMN, DMN, CMMN, and Forms | bpmn.io
  site: bpmn.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: Order process with an inclusive gateway and an interrupting boundary event.
review:
  status: generated
  flags: []
---

## Explanation

BPMN stands for Business Process Model and Notation. Version 2.0 is an industry standard for both modeling and executing processes. OMG, the standards body behind it, calls it a de-facto standard notation. Stakeholders can use it directly, and it does not depend on any implementation environment.

**Sequence flow.** Sequence flow is a core concept of BPMN. A sequence flow defines the order in which the steps of a process happen.

**Tasks.** Tasks are the basic elements. Each is an atomic unit of work, meaning one step that is not split further. Tasks combine to produce a meaningful result.

**Events.** A process can react to events. These are catching events. It can also emit events. These are throwing events.

**Boundary events.** A boundary event models what should happen if something occurs while an activity is running. It must be an intermediate catch event. If it is interrupting, it ends the activity it is attached to once it triggers. See the article BPMN Event.

**Gateways.** A gateway routes tokens in more complex patterns than plain sequence flow. A token marks the current position of a running process.
- The event-based gateway waits until one of its events fires. It then follows that event's flow, and the other events cannot fire afterward. Its outgoing flows must lead to intermediate catch events. In Camunda, these are timer, message, or signal events.
- The inclusive (OR) gateway follows every outgoing flow whose condition is true. If none is true, it uses the default flow.

**More about BPMN.**

- **History of BPMN:** BPMN began at an industry group, BPMI, and reached the public as version 1.0 in May 2004 [src:7]. OMG took over in 2005 [src:7]. Version 2.0 arrived in January 2011 [src:6]. Version 2.0.2, from January 2014, is the latest [src:6].
- **BPMN Motivation:** BPMN is a standard process notation built on flowcharting. Diagrams are precise enough to become software process components and are stored as XML. OMG maintains it, and it is also ISO 19510.
- **BPMN as Modeling Language, Not Method:** BPMN is a notation, a set of drawing conventions for business processes. It aims to be readable by business users and precise enough to translate into software process components.
- **BPMN Focus on Connected Businesses:** BPMN can model processes that cross company borders. Each organization gets its own pool, and message flows show the messages passing between them. Business and technical people can both read the result.
- **Core BPMN Element Subset:** Most BPMN models need only a small part of the notation. A study of 120 diagrams found that analysts share a small set of constructs. Using that core set eases modeling and reading.
- **Process Notations Comparison (EPC, BPMN, UML Activity Diagram):** EPC, UML activity diagrams, and BPMN can describe the same process with different elements. Most EPC elements have a clear BPMN equivalent, so conversion follows rules, but the result usually needs manual cleanup.
- **BPMN Modeling Tool:** A BPMN modeling tool is software for drawing process models. Camunda Modeler and bpmn.io are two examples. They differ in form, such as desktop or web, and viewer or editor.

## Example

An order process starts when an order arrives. A task checks stock. An inclusive gateway then looks at the order. If the customer wants gift wrapping and express delivery, both tasks start. If neither applies, the default flow goes straight to shipping. While the stock check runs, an interrupting boundary event for a cancellation message can stop it.

## Trade-offs

This article covers only the basic elements, not every BPMN element or variant. The event-based gateway limits its outgoing flows to intermediate catch events. An interrupting boundary event ends the running activity, so any work in progress there stops.
