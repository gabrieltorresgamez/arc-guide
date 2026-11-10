---
title: BPMN Connecting Object
slug: bpmn-connecting-object
category: modeling-bpmn
kind: notation-element
summary: BPMN connecting objects are the lines that link elements in a process diagram. Sequence flow
  sets the order of steps inside a pool. Message flow links separate pools. Association is a dotted line.
arc42:
- 6
step: s10-document
related:
- bpmn-swimlane-pool-and-lane
- bpmn-collaboration-diagram
- bpmn-core-elements
- bpmn-layout-guideline
- bpmn-modeling-tips
- bpmn-data-element
- bpmn-artifacts-group-and-text-annotation
- bpmn-gateway-semantics
checks:
- Connectors between two elements in the same pool are sequence flows, not message flows.
- Communication between participants is shown as message flow between separate pools.
- The default path from a decision point is marked with a slash on its sequence flow.
- The diagram avoids crossing flows and flows spanning many pools or lanes.
sources:
- url: https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
  title: Business Process Model and Notation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://client.igrafx.com/client/16/en/Content/igrafx/usingbpmn/Connector_Lines_in_BPMN_Diagrams_Reference.htm
  title: Connector Lines in BPMN Diagrams Reference
  site: client.igrafx.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.bpmn
  caption: 'Two pools: solid sequence flows inside each pool, and a message flow between them.'
review:
  status: generated
  flags: []
---

## Explanation

BPMN (Business Process Model and Notation) diagrams use lines to link their elements. Each line type has its own look and its own job. These lines are called connecting objects.

**Sequence flow.** It is a solid line with an arrowhead. It shows the order in which activities are performed. Camunda describes it as the arrow that sets the order of execution between two elements. In iGrafx, a connector between two objects in the same pool is a sequence flow. A pool is a container for one participant's process. See BPMN Swimlane (Pool and Lane).

**Default sequence flow.** This is a sequence flow with a slash on the line. The slash marks the default path.

**Message flow.** It is a dashed arrow between two pools. It runs from a source to a possible target in another pool. It shows communication between participants. A message flow can never connect activities or events inside the same pool. Camunda recommends separate pools joined by message flows to show how participants communicate.

**Association.** It is drawn as a dotted line.

A simple way to choose a line: look at where the two ends sit. Both ends in the same pool means sequence flow. Ends in different pools means message flow.

**Layout tips.** Camunda's readability advice includes:
- Avoid flows that cross each other.
- Avoid flows that span many pools or lanes.

Ordering the pools in a collaboration diagram can reduce message flows that cross pools.

## Example

A customer pool and a shop pool sit one above the other. Inside the customer pool, solid arrows run from "Place order" to "Wait for delivery". Inside the shop pool, a solid arrow runs from "Receive order" to "Ship goods". A dashed arrow runs from "Place order" in the customer pool to "Receive order" in the shop pool. The solid arrows show order within each participant. The dashed arrow shows communication between them.

## Trade-offs

Separate pools with message flows make communication between participants visible. Many message flows can cross pools and make the diagram hard to read. Reordering pools helps reduce this, but it cannot always remove every crossing.
