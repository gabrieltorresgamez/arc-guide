---
title: BPMN Motivation
slug: bpmn-motivation
category: modeling-bpmn
kind: concept
summary: BPMN is a standard process notation built on flowcharting. Diagrams are precise enough to become
  software process components and are stored as XML. OMG maintains it, and it is also ISO 19510.
arc42:
- 8
- 12
step: s10-document
related:
- history-of-bpmn
- process-notations-comparison
- bpmn-2-0-notation-overview
- uml-unified-modeling-language
- foundation-for-execution
- bpmn-modeling-tools
- bpmn-as-modeling-language-not-method
checks:
- The document states which BPMN version is used, and execution is only assumed for version 2.0 or later.
- Process models are stored as BPMN XML so tools can exchange them.
- Models that are meant to run are precise enough to translate into software process components.
sources:
- url: https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
  title: Business Process Model and Notation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://www.omg.org/spec/BPMN/2.0.2/About-BPMN
  title: About the Business Process Model and Notation Specification Version 2.0.2
  site: omg.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.bpmn
  caption: 'A minimal process: the same diagram is both a readable picture and an XML document that software
    can run.'
review:
  status: generated
  flags: []
---

## Explanation

BPMN (Business Process Model and Notation) is a standard way to draw business processes. Its notation builds on flowcharting. It looks very similar to UML activity diagrams (see the article on the Unified Modeling Language).

**Why the notation aims at software**

OMG, the standards body that maintains BPMN, sets a clear goal. A BPMN diagram must be precise enough to translate into software process components. A diagram is therefore more than a picture. Software can act on it.

**One artifact for drawing and running**

A BPMN process is an XML document with a visual representation. XML is a plain, structured text format. Because the diagram sits in this document, tools can exchange it and engines can execute it.

BPMN 2.0 came out in January 2011 and added execution semantics. In plain terms, it defined what a process means when software runs it.

**Standards and ownership**

BPMI first developed BPMN. OMG has maintained it since the two organizations merged in 2005. BPMN is also ratified as ISO standard 19510. The article on the history of BPMN has more.

**Relation to other notations**

An EPC model (event-driven process chain, another process notation) can be transformed into BPMN with only a slight loss of information. The article on process notations compares EPC, BPMN and UML activity diagrams.

## Example

A company draws its order process in a BPMN tool. Business staff review the diagram. The tool saves it as an XML file. Another tool opens the same file, and a workflow engine runs it. Nobody redraws the process for each audience.

## Trade-offs

BPMN is very close to UML activity diagrams, so the two can look alike. The choice between them needs a closer comparison (see the article on process notations). Moving from EPC to BPMN loses a little information. Execution only became part of BPMN with version 2.0, so older models may lack it.
