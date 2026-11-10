---
title: Process Mining
slug: process-mining
category: modeling-bpmn
kind: method
summary: Process mining is a family of techniques that analyze event data from information systems. It
  shows how a process actually runs, not how people believe it runs, and helps improve it.
arc42:
- 6
step: null
related:
- process-analysis
- bpm-life-cycle
- as-is-and-to-be-view
- process-model-versus-process-instance
- runtime-view
- bpmn-2-0-notation-overview
checks:
- The document states that event data for process analysis links to a case ID, activities and timestamps.
- If event data is exchanged between tools, the document names the format used, such as XES (IEEE 1849).
sources:
- url: https://en.wikipedia.org/wiki/Process_mining
  title: Process mining - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.celonis.com/insights/topics/what-is-process-mining
  title: What is Process Mining? Definition and benefits | Celonis
  site: celonis.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/IEEE_1849
  title: IEEE 1849 - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.tf-pm.org/resources/manifesto
  title: Process Mining Manifesto - IEEE Task Force on Process Mining
  site: tf-pm.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'Process mining flow: from event logs in systems to a view of how the process actually runs.'
review:
  status: generated
  flags: []
---

## Explanation

Process mining is a group of techniques. They analyze event data to understand and improve operational processes.

**Where the data comes from.** Every step of a business process leaves a digital footprint in the systems that handle it. This is called event log data. Process mining software extracts it from those transactional systems.

**What an event log needs.** The minimum input is data linked to three things:

- a case ID, which ties events to one run of the process,
- the activities that happened,
- timestamps, which say when they happened.

**Reality, not belief.** The main value is a view of how processes actually run. People often hold a different picture of how they think the process runs. Event data gives a factual basis for comparison.

**Three classes of techniques.** Process mining techniques fall into three main classes: discovery, conformance checking and enhancement.

**Exchanging event data.** The XES standard (IEEE 1849) defines a language to transport, store and exchange event data. Process mining is one example use. The standard was revised in 2023 as IEEE 1849-2023.

**Community.** The IEEE Task Force on Process Mining promotes the topic. It published the Process Mining Manifesto.

For related ideas, see the articles Process Analysis and BPM Life Cycle.

## Example

A support team handles customer tickets in a ticketing tool. Each ticket is a case with its own ID. Each status change is an activity with a timestamp. The team extracts these records from the tool. Analysts then study how tickets actually moved. They compare that with the flow the team believes it follows.

## Trade-offs

Process mining only works when the systems record events with a case ID, activities and timestamps. Without these three, the data cannot serve as input.
