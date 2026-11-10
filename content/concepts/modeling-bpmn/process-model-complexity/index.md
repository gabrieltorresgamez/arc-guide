---
title: Process Model Complexity
slug: process-model-complexity
category: modeling-bpmn
kind: concept
summary: A process model can be correct and complete yet too complicated to read. Larger models are harder
  to understand. Splitting them into subprocesses, limiting data objects, and following guidelines help.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-2-0-model-quality
- bpmn-modeling-tips
- levels-of-process-modeling
- bpmn-collaboration-diagram
- complexity-reduction
- bpmn-element-usage-frequency
- bpmn-data-element
- fitness-for-purpose
checks:
- Large process models are split into smaller subprocess models.
- Data objects are limited to the most important data aspects.
- Operational models use separate pools per participant rather than lanes.
- Modeling guidelines such as 7PMG are applied or consciously deviated from.
sources:
- url: https://aisel.aisnet.org/icis2014/proceedings/GeneralIS/28/
  title: 'AIS Electronic Library (AISeL) - ICIS 2014 Proceedings: Testing the Impact of Wand and Weber’s
    Decomposition Model on Process Model Understandability'
  site: aisel.aisnet.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://research.tue.nl/p/en/research-outputs/understanding-business-process-models-the-costs-and-benefits-of-s
  title: Understanding business process models — Eindhoven University of Technology Research Portal
  site: research.tue.nl
  accessed: '2026-11-09'
- url: https://research.tue.nl/p/en/research-outputs/seven-process-modeling-guidelines-7pmg
  title: Seven process modeling guidelines (7PMG) — Eindhoven University of Technology Research Portal
  site: research.tue.nl
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A top-level process kept simple by moving detail into a subprocess.
review:
  status: generated
  flags: []
---

## Explanation

Process models are created to help people understand, discuss, and remember processes. So they must be easy to read and understand.

**Where complexity comes from**

Research shows that the bigger a process model gets, the harder it is to understand. Previous research has put forward metrics such as size and degree of block-structuredness as correlated with understandability. Data objects are one example of clutter. Too many of them overload a diagram, so show only the most important data aspects.

**How to reduce it**

- **Decompose.** Split a large model into smaller subprocess models to increase understandability. It is still unclear what characterizes a good decomposition, but an experiment found that Wand and Weber's decomposition conditions had a positive influence on understandability.
- **Choose participants carefully.** For operational models, Camunda recommends a collaboration diagram with a separate pool for each participant, instead of lanes.
- **Follow guidelines.** The Seven Process Modeling Guidelines (7PMG) come from research on how model structure relates to errors and comprehension. They are formulated to be intuitive to practitioners.
- **Limit data objects.** Use them sparingly.

## Example

Imagine a collaboration with three participants: a customer, a bank, and a registration office. One diagram shows every task, every check, and every document. Nobody can follow it. The team keeps a top-level diagram with one step per phase. Each phase opens into its own smaller subprocess diagram. Only the few data objects that matter, such as a payment confirmation, appear.

## Trade-offs

Simplification must be weighed, not applied blindly. Structuredness is not an absolute desideratum for understandability. Trade-offs with other model properties exist.
