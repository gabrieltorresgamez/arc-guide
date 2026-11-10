---
title: Capturing Business Behavior via Process Modeling
slug: capturing-business-behavior-via-process-modeling
category: modeling-bpmn
kind: method
summary: Process models describe business behavior at different levels of detail. A high-level model explains
  a process to stakeholders. A more detailed one supports analysis. A BPMN model can also be run by a
  workflow engine.
arc42:
- 3
- 6
step: s03-functional-requirements
related:
- levels-of-process-modeling
- bpmn-2-0-notation-overview
- process-analysis
- purpose-of-process-analysis-and-modeling
- bpmn-diagram-types
- process-notations-comparison
- bpm-life-cycle
checks:
- Each process model states whether it is a high-level descriptive model for stakeholders or a more detailed
  analytical model.
- Analytical process models include data such as time, cost and resources where inefficiencies are to
  be analyzed.
- Where a process is meant to be executed, the BPMN model and its XML are identified as the executable
  level.
sources:
- url: https://camunda.com/blog/2024/05/what-is-business-process-modeling/
  title: What is Business Process Modeling? | Camunda
  site: camunda.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'A small order process: the kind of high-level model that stakeholders review and that can
    later gain detail.'
review:
  status: generated
  flags: []
---

## Explanation

A process model is a diagram of how work flows through a business. Process models serve different purposes, so choosing the level of detail matters.

**Descriptive models.** A descriptive model gives a high-level view of a process. It outlines the key steps and flow without too much detail, and suits uses such as onboarding new employees, communicating processes to stakeholders, or giving a compliance overview.

**Analytical models.** An analytical model adds detail. It often records time, cost and resources. With that data, you can look for inefficiencies in the process. It is more complex than a descriptive model.

**Executable models.** An executable model can be deployed directly into a business process management system. It contains the exact logic, rules and sequences needed to automate a process. BPMN (Business Process Model and Notation) is an industry standard for process modeling and execution. See the article "BPMN 2.0 Notation". A BPMN model is documentation that people can read. It is also source code that machines can interpret. Both roles are held in one artifact.

A BPMN process is an XML document that also has a visual representation. The XML holds the information that workflow engines such as Zeebe need to interpret the process.

For more on the levels, see "Levels of Process Modeling".

## Example

A company models its order handling. First, it draws a short descriptive model: receive order, check stock, ship. Business stakeholders read it and confirm it matches how work is done. Later, the team adds time, cost and staff per step. This analytical model shows the stock check is the slowest step. Finally, the team builds an executable model with the exact logic, rules and sequences needed to automate the process.

## Trade-offs

A descriptive model is easy to read, but it lacks the data needed to find inefficiencies. An analytical model reveals more, but it is more complex. A BPMN model that serves as both documentation and source keeps both roles in one artifact.
