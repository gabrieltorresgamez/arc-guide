---
title: Core BPMN Element Subset
slug: bpmn-element-usage-frequency
category: modeling-bpmn
kind: concept
summary: Most BPMN models need only a small part of the notation. A study of 120 diagrams found that analysts
  share a small set of constructs. Using that core set eases modeling and reading.
arc42:
- 8
- 12
step: s10-document
related:
- bpmn-core-elements
- bpmn-swimlane-pool-and-lane
- bpmn-event
- bpmn-activity
- bpmn-modeling-tips
- bpmn-2-0-notation-overview
- process-model-complexity
- bpmn-2-0-model-quality
checks:
- The document states which BPMN elements the models use, and the set stays small.
- Process steps are labeled with well-chosen, meaningful names.
- Swim lanes appear only at the top level, not inside subprocesses.
sources:
- url: https://researchwith.stevens.edu/en/publications/how-much-language-is-enough-theoretical-and-practical-use-of-the-/
  title: How much language is enough? Theoretical and practical use of the business process modeling notation
    - Stevens Institute of Technology
  site: researchwith.stevens.edu
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'A small process using only core elements: pool, lanes, start and end events, tasks, a subprocess
    and sequence flows.'
review:
  status: generated
  flags: []
---

## Explanation

BPMN (Business Process Model and Notation) offers many symbols. Real models use few of them. Zur Muehlen and Recker (2008) studied 120 BPMN diagrams. They found that less than 20% of the notation's vocabulary is regularly used. The average model contains just 9 different constructs, and models of that size have typically only 4-5 constructs in common, so only a small agreed subset has emerged. They said their findings give guidance on reducing language complexity, which should ease and speed modeling.

**Elements the Camunda primer introduces**

- **Sequence flow.** An arrow between two elements. It sets the order of steps in the process.
- **Tasks.** Atomic units of work. You combine them to produce a meaningful result.
- **Events.** They represent things that happen. A process can react to an event (catching) or emit one (throwing).
- **Subprocesses.** Containers for common functionality.
- **Pools and lanes (swim lanes).** They exist only at the top level of a process or collaboration. You cannot place them inside a subprocess.

For the elements themselves, see BPMN Core Elements, BPMN Swimlane (Pool and Lane) and BPMN Event.

**Readability and labels**

Camunda calls well-chosen labels the single most important thing for readable models.

## Example

A team models an order-handling process. They use one pool with two lanes, "Sales" and "Warehouse". They draw a start event, three tasks, sequence flows between them and an end event. One group of steps sits in a subprocess.

## Trade-offs

The paper says reducing language complexity should ease and speed modeling. Check whether a case needs an element outside the subset before you leave it out.
