---
title: BPMN Layout Guideline
slug: bpmn-layout-guideline
category: modeling-bpmn
kind: practice
summary: 'A BPMN layout guideline is a set of drawing habits that make process diagrams easy to read:
  one flow direction, few crossings, no very long arrows, and clearly marked gateways.'
arc42:
- 8
- 5
step: s10-document
related:
- bpmn-modeling-tips
- bpmn-gateway-semantics
- bpmn-link-event
- bpmn-2-0-model-quality
- antipatterns-for-process-flows
- bpmn-connecting-object
- bpmn-swimlane-pool-and-lane
- bpmn-2-0-notation-overview
checks:
- Process diagrams are modeled in one consistent direction, such as left to right.
- Sequence flows do not cross each other, and very long flows are avoided or replaced by link events.
- Every XOR gateway shows the X marker.
- Alternative paths are joined with an explicit XOR merge gateway.
- Naming conventions for BPMN elements are defined and applied.
sources:
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://cloud.trisotech.com/bpmnquickguide/bpmn-quick-guide/bpmn-modeling-best-practices.html
  title: 'BPMN Modeling Best Practices :: BPMN Quick Guide'
  site: cloud.trisotech.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: Left-to-right order process with an explicit XOR split and a matching XOR merge before the
    shared task.
review:
  status: generated
  flags: []
---

## Explanation

A BPMN diagram shows a business process as boxes and arrows. A layout guideline says how to arrange those shapes on the page. Related articles: BPMN Modeling Guidelines, BPMN Gateway, and Link Event.

**Pick one direction.** Camunda recommends modeling from left to right. This matches the reading direction of a western audience. Trisotech adds a convention for line types. Sequence flows run horizontally. Message flows and data associations run vertically.

**Keep lines short and apart.**
- Avoid flows that cross each other. Trisotech says minimizing crossings eases reading.
- Avoid flows that cross many pools or lanes where possible.
- Avoid very long sequence flows, especially ones that run against the reading direction. A link event can replace such a flow.

**Draw gateways explicitly.**
- Always draw the X marker on an XOR gateway, even if your tool allows a blank one.
- Join alternative paths with an explicit XOR merge gateway. Do not mix split and join meaning in one symbol.
- Place split and join gateway pairs symmetrically.

**Name things consistently.** Camunda also recommends naming conventions. Labels then convey the business meaning in the same way throughout.

**Readability wins.** Camunda says not to be dogmatic. If breaking a rule makes the model clearer, aim for the most readable model.

## Example

Imagine an order process. It starts at the left with "Receive order". An XOR gateway with an X splits it into "Standard shipping" and "Express shipping". Both paths run left to right. An explicit XOR merge gateway, placed symmetrically to the split, joins them before "Send invoice". No arrows cross, and no arrow loops back across the whole page. A reader follows the process from left to right.

## Trade-offs

The rules are not absolute. Camunda says explicit modeling should not be dogmatic. Implicit joins can sometimes make a model more readable, for example when splitting and joining points do not form natural blocks. In that case, choose the clearer diagram.
