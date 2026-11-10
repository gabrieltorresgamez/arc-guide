---
title: BPMN Collaboration Diagram
slug: bpmn-collaboration-diagram
category: modeling-bpmn
kind: notation-element
summary: A BPMN collaboration diagram shows each participant's process in its own pool. Dashed message
  flows connect the pools, so interaction is explicit. Camunda recommends it over lanes for operational-level
  models.
arc42:
- 6
step: s10-document
related:
- bpmn-swimlane-pool-and-lane
- bpmn-diagram-types
- bpmn-conversation-diagram
- data-exchange-between-bpmn-processes
- bpmn-layout-guideline
- bpmn-event
- levels-of-process-modeling
- bpmn-2-0-notation-overview
checks:
- Operational-level process models use a separate pool per participant instead of lanes.
- Interaction between participants is shown with message flows between pools.
- Pools are ordered so message flows cross other pools as little as possible.
- Pools of parties whose internal process is of little interest are collapsed.
- Processes with different frequencies are modeled in separate pools.
sources:
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://camunda.com/bpmn/reference/
  title: BPMN 2.0 Symbols - A complete guide with examples. | Camunda
  site: camunda.com
  accessed: '2026-11-09'
- url: https://camunda.com/bpmn/examples/
  title: BPMN 2.0 Examples | Camunda
  site: camunda.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A customer pool exchanging messages with a collapsed restaurant pool.
review:
  status: generated
  flags: []
---

## Explanation

A collaboration diagram is the BPMN name for a picture in which separate pools exchange messages (see BPMN Swimlane (Pool and Lane)). Each participant gets its own pool. Message flows between the pools show the interaction and communication explicitly.

**Pools versus lanes**

A pool ranks above its lanes. Lanes always sit inside a pool, and their boundaries are process boundaries from start to end. For operational-level models, Camunda recommends separate pools for the participants instead of lanes. It also advises avoiding lanes in most models, because lanes make changes harder to maintain.

**What separate pools show**

Separate pools show who controls which process. Processes that run at different frequencies belong in separate pools.

**Collapsed pools**

A pool can be collapsed when the other party's internal process is of little interest. A customer, for example, has little interest in how a deliverer works inside.

**Messages and signals**

A message goes to a specific recipient. A signal is a broadcast: any receiver that wants to react may do so. Signals are compact for interaction between process instances. But they do not address any specific instance.

**Layout**

Order the pools so that message flows cross other pools as little as possible.

## Example

A customer orders a meal from a restaurant. The diagram has two pools: "Customer" and "Restaurant". The customer pool is expanded. The restaurant pool is collapsed, because the customer does not care how the kitchen works. A dashed message flow carries the order to the restaurant. Another dashed flow carries the confirmation back.

## Trade-offs

Separate pools make interaction explicit and show who controls each process. Pools should be ordered so message flows do not cross other pools. Camunda advises avoiding lanes in most models because they make changes harder to maintain. A signal is compact, but it cannot address one specific instance.
