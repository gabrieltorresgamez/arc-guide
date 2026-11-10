---
title: BPMN as Modeling Language, Not Method
slug: bpmn-as-modeling-language-not-method
category: modeling-bpmn
kind: principle
summary: BPMN is a notation, a set of drawing conventions for business processes. It aims to be readable
  by business users and precise enough to translate into software process components.
arc42:
- 8
- 12
step: s10-document
related:
- bpmn-2-0-notation-overview
- bpmn-motivation
- modeling-method
- levels-of-process-modeling
- foundation-for-execution
- process-notations-comparison
- history-of-bpmn
- bpmn-modeling-tips
checks:
- The document states that process diagrams use BPMN as a notation that business users can read.
- Diagrams meant for execution name the specific engine they target.
- BPMN is used only for business-process concepts, not for other modeling needs.
sources:
- url: https://www.omg.org/bpmn/
  title: Business Process Model & Notation™ (BPMN™) | Object Management Group
  site: omg.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
  title: Business Process Model and Notation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/
  title: Modeling with BPMN | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A small process any business user can read and a process engine could later run.
review:
  status: generated
  flags: []
---

## Explanation

BPMN stands for Business Process Model and Notation. The key word is *notation*. It is a graphical language for drawing processes. Camunda describes it as a graphical notation for representing complex processes.

**Two design goals**

- **Readable for business users.** The main goal is a notation that all business users can readily understand. It looks like a flowchart and does not depend on any particular implementation environment.
- **Precise enough for software.** The notation is exact enough to translate diagrams into software process components. The specification maps the graphics to constructs of execution languages. These are languages that a process engine can run.

**Bridging business and technical roles**

BPMN is meant for direct use by the people who design, manage, and realize processes. It supports both technical and business users. It also aims to avoid communication gaps between process design and implementation.

**A limited scope**

BPMN covers only the modeling concepts that apply to business processes. It is a language for drawing process models. It is not a general-purpose modeling language. For related topics, see the articles BPMN 2.0 Notation and Modeling Method.

**Execution needs a target**

A diagram can be translated to executable form. In Camunda's tooling, a diagram must be created for the process engine it is meant to be deployed on. A diagram modeled for Camunda 7 cannot run in Camunda 8, or vice versa.

## Example

A team draws an "Approve order" process. A sales manager reads the diagram and confirms the steps match daily work. A developer later maps the same diagram to a process engine. The drawing stays the shared reference for both roles.

## Trade-offs

One notation serves two audiences, business users and technical users. That is its strength. The readable, flowchart-like look supports business understanding. Its scope is limited to business processes, so it is not a tool for every modeling need.
