---
title: BPMN Swimlane (Pool and Lane)
slug: bpmn-swimlane-pool-and-lane
category: modeling-bpmn
kind: notation-element
summary: A pool is a box for one participant in a BPMN diagram. Lanes split a pool into parts. Separate
  pools talk only through message flows, never through sequence flow.
arc42:
- 5
- 6
step: s10-document
related:
- bpmn-collaboration-diagram
- bpmn-connecting-object
- bpmn-core-elements
- data-exchange-between-bpmn-processes
- bpmn-conversation-diagram
- bpmn-2-0-notation-overview
- bpmn-layout-guideline
checks:
- Communication between separate pools is shown with dashed message flows, not with sequence flow.
- No message flow connects two elements inside the same pool.
- Every lane sits inside a pool, and the diagram states what its lanes represent.
- Where a partner's pool is collapsed, the document does not rely on it to show dependencies between message
  exchanges.
sources:
- url: https://bpmtips.com/bpmn-in-practice-pools-and-lanes/
  title: BPMN in practice - pools and lanes | BPM Tips
  site: bpmtips.com
  accessed: '2026-11-09'
- url: https://camunda.com/bpmn/reference/
  title: BPMN 2.0 Symbols - A complete guide with examples. | Camunda
  site: camunda.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.bpmn
  caption: 'Two pools: the Shop pool has two lanes. Sequence flow crosses lanes; the dashed message flows
    connect the pools.'
review:
  status: generated
  flags: []
---

## Explanation

A **pool** is a large box that holds a process. A **lane** is a strip inside a pool. Together they are called swimlanes.

**Pool above lane.** BPMN ranks the pool higher than its lanes. Lanes always exist inside a pool. A lane cannot stand alone.

**What a lane means.** BPMN does not say what a lane stands for. Many diagrams use lanes for people, but BPMN does not define that meaning.

**Pools and messages.** BPMN assumes that messages go to participants outside your own pool. Separate pools therefore connect through **message flows**. A diagram with several pools linked this way is called a collaboration diagram (see *BPMN Collaboration Diagram*). Message flows are drawn dashed. They are allowed only between pools, not within a single pool.

**Sequence flow stops at the pool edge.** Sequence flow links steps inside a process. It cannot cross a pool boundary. To show a hand-off between pools, use a message flow instead.

**Hiding a partner's process.** You can collapse a partner's pool so its inner process is hidden. If you collapse your own pool as well, you see only the messages, and you can no longer see how the message exchanges depend on each other.

**Subprocess limit.** Pools and lanes exist only at the top level of a process or collaboration. They cannot be added inside a subprocess. Camunda's documentation describes this as a constraint of the BPMN 2.0 specification.

## Example

An online shop diagram has two pools: "Customer" and "Shop". The Shop pool has two lanes, "Sales" and "Warehouse". Steps inside the Shop pool are linked by sequence flow, even when the flow moves from one lane to the other. The Customer sends an order to the Shop through a dashed message flow. The Shop later sends a confirmation back the same way. The team notes beside the diagram that lanes stand for departments, because BPMN does not decide this.

## Trade-offs

Collapsing both pools shows only the messages and hides how the message exchanges depend on each other.

BPMN gives lanes no fixed meaning, so you can designate them as you like.
