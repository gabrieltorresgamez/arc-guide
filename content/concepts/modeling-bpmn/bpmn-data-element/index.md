---
title: BPMN Data Element
slug: bpmn-data-element
category: modeling-bpmn
kind: notation-element
summary: BPMN data elements show the information a process uses or creates. Data associations link that
  data to activities. Data flows along these associations, not along sequence flows.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-core-elements
- bpmn-activity
- bpmn-connecting-object
- process-model-versus-process-instance
- data-exchange-between-bpmn-processes
- bpmn-2-0-notation-overview
checks:
- Data stores are used for information that must outlast a single process instance, such as a database
  or file system.
- Data is connected to activities with data associations, not with sequence flows.
- The document states whether the tool treats data objects and data stores as modeling-only or as executable.
sources:
- url: https://www.visual-paradigm.com/guide/bpmn/how-to-use-data-objects-in-bpmn
  title: How to Use Data Objects in BPMN
  site: visual-paradigm.com
  accessed: '2026-11-09'
- url: https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/data-objects-and-data-stores
  title: Maestro Orchestrate - Data objects and data stores
  site: docs.uipath.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-coverage/
  title: BPMN coverage | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: Two tasks share one data object; a data store outlives the process instance.
review:
  status: generated
  flags: []
---

## Explanation

A BPMN process diagram mainly shows the order of work. Data elements add the information that the work uses, creates or changes. The article "BPMN Core Elements" covers the wider notation.

**Data objects.** A data object stands for information that is created, updated or consumed during a process. It sits outside the sequence flow, which is the set of arrows that sets the order of steps. Even so, every flow object in a given process instance can use it. A process instance is one run of the process. The article "Process Model versus Process Instance" explains the difference.

**Data stores.** A data store is a persistent repository, such as a database or a file system. Unlike a data object, it persists beyond the lifetime of the process instance.

**Data associations.** A data association links data elements to activities, processes and global tasks. Tools draw them as dashed lines with arrowheads that connect data objects to activities.

**Data flow versus sequence flow.** Data flow follows data associations. It does not follow sequence flows. The order of tasks and the movement of data are two separate things in the diagram.

**Modeling only.** Tools may treat data elements as documentation. Camunda supports data objects and data stores for modeling purposes only, not execution. UiPath Maestro also treats data objects as modeling-only elements.

## Example

An order process has a task "Check order" and a later task "Ship order". The diagram holds one data object called "Order". A dashed arrow runs from "Check order" to "Order". Another runs from "Order" to "Ship order". The arrows show which task uses the information. A data store called "Customer database" sits beside the process. Its content remains after this order instance ends.

## Trade-offs

Data elements make the information a process depends on visible. They also add symbols and dashed lines to the diagram. Because some tools treat them as modeling-only, they may document the process without changing how it runs. Add them where the information matters to the reader.
