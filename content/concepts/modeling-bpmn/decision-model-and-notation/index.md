---
title: Decision Model and Notation
slug: decision-model-and-notation
category: modeling-bpmn
kind: standard
summary: DMN is a standard for modeling business decisions. It pairs a graphical notation with an expression
  language, so business users can read decisions and a decision engine can run them alongside a BPMN process.
arc42:
- 8
- 5
step: s10-document
related:
- bpmn-2-0-notation-overview
- bpmn-activity
- bpmn-task-marker
- bpmn-core-elements
- bpmn-motivation
checks:
- Decision logic sits in a DMN model, not inside the process flow; the process calls it through a business
  rule task.
- Decision tables list their inputs, outputs and rules.
- Modeling of decisions starts from a Decision Requirements Diagram.
sources:
- url: https://www.omg.org/spec/DMN
  title: About the Decision Model and Notation Specification Version 1.7 beta
  site: omg.org
  accessed: '2026-11-09'
- url: https://www.omg.org/spec/DMN/1.4/About-DMN
  title: About the Decision Model and Notation Specification Version 1.4
  site: omg.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/business-rule-tasks/
  title: Business rule tasks | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/dmn/decision-table/
  title: Overview | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/dmn/
  title: Modeling with DMN | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A process calls a DMN decision through a business rule task, then routes on the result.
review:
  status: generated
  flags: []
---

## Explanation

Decision Model and Notation (DMN) is owned by the OMG, a standards body. It gives you two tools for modeling decisions: a graphical notation and an expression language. Its primary goal is a common notation that all business users can understand.

**Decisions apart from process flow**

DMN is designed to work alongside BPMN, the standard notation for business processes. See BPMN 2.0 Notation for that language. A BPMN business rule task models the evaluation of a business rule. When a process instance reaches such a task, a decision engine evaluates a DMN decision.

**Two views of a decision**

- **Decision Requirements Diagram (DRD).** Modeling starts in this view.
- **Decision table.** This is decision logic shown as a table. It has inputs, outputs and rules. DMN includes decision tables as a built-in feature.

**Expressions**

DMN also has an expression language, called FEEL. A business knowledge model (BKM) can hold a literal expression. That expression can take parameters, which serve as inputs to the FEEL expression.

## Example

An online shop wants to decide whether an order needs a manual check. The order process reaches a business rule task named "Check order risk". The decision engine evaluates a decision table. Its inputs are order amount and customer history. Its output is "manual check" or "auto-approve". The process then continues along the matching path. A business user can read the table rows without reading the process logic.
