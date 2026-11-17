---
title: BPMN Modeling Guidelines
slug: bpmn-modeling-guidelines
category: modeling-bpmn
kind: practice
summary: BPMN modeling guidelines are simple naming and layout rules that keep process models readable.
  They cover page size, explicit start and end events, question-style XOR gateways, verb-object task names,
  and separate pools for partners.
arc42:
- 6
step: s10-document
related:
- bpmn-2-0-notation
- soundness-of-process-models
- bpmn-gateway
- bpmn-collaboration-diagram
- bpmn-swimlane-pool-and-lane
- process-analysis-and-modeling
checks:
- Each process level has about 10 activities or fewer, so it fits on one page.
- Every process shows explicit start and end events.
- XOR gateways show the X symbol, carry a question, and have outgoing flows labeled as answers.
- Tasks are named with a verb and an object.
- Parallel and joining gateways carry no name.
sources:
- url: https://docs.camunda.io/docs/components/best-practices/modeling/naming-bpmn-elements/
  title: Naming BPMN elements | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://www.trisotech.com/bpmn-style-rules/
  title: BPMN Style Rules
  site: trisotech.com
  accessed: '2026-11-09'
- url: https://cloud.trisotech.com/bpmnquickguide/bpmn-quick-guide/bpmn-modeling-best-practices.html
  title: 'BPMN Modeling Best Practices :: BPMN Quick Guide'
  site: cloud.trisotech.com
  accessed: '2026-11-09'
- url: https://cloud.trisotech.com/bpmnrulebook/bpmn-rule-book/use-of-text-color-size-lines-in-diagram.html
  title: 'Use of Text, Color, Size and Lines in Diagram :: BPMN Rule Book'
  site: cloud.trisotech.com
  accessed: '2026-11-09'
- url: https://skills.visual-paradigm.com/docs/common-dfd-mistakes-and-how-to-avoid-them/dfd-readability-issues/dfd-color-misuse/
  title: 'DFD Color Misuse: Avoiding Visual Noise in Data Flow Diagrams'
  site: skills.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://bpmn.io/blog/posts/2016-colors-bpmn-js
  title: Colors are Here | Blog | bpmn.io
  site: bpmn.io
  accessed: '2026-11-09'
- url: https://github.com/bpmn-io/bpmn-js-examples/blob/main/colors/README.md
  title: bpmn-js-examples/colors/README.md at main · bpmn-io/bpmn-js-examples · GitHub
  site: github.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A small order process with a named start event, a question gateway, labeled answers, and two
    end states.
review:
  status: generated
  flags: []
---

## Explanation

BPMN is a notation for drawing business processes. See the article BPMN 2.0 Notation for the basics. The rules below come from Camunda's documentation and from Silver's Method and Style.

**Keep each model small.** Silver's style allows about 10 activities in one process level, so the model fits on one printed page. Also avoid very long sequence flows that span pages or run against the reading direction.

**Show start and end events.** Always draw them explicitly. Readers then see what triggers the process and how it ends. A message start event is labeled "Receive" plus the message name. Events are named with an object plus a verb that describes a state. So an end event states the resulting state, such as "Invoice paid". In Silver's style, end events stand for distinct end states of a process or subprocess.

**Connect subprocess and parent.** When a subprocess has multiple end states, the parent level follows the collapsed subprocess with an XOR gateway. Its gates match the subprocess's end event labels.

**Phrase XOR gateways as questions.** Label it with a question. Label each outgoing flow as an answer to that question. Draw the X symbol inside the gateway, even if your tool allows a blank one.

**Leave some gateways unnamed.** Camunda advises against naming parallel gateways and all joining gateways [src:1]. Silver's style also leaves AND and event gateways unlabeled, including their gates.

**Name tasks as actions.** Camunda asks for an object and a verb in the infinitive, for example "Check invoice". Silver says all activities, subprocesses included, should be labeled, preferably as a verb-object action [src:3].

**Use pools for participants.** For models at the operational level, Camunda recommends separate pools for process participants instead of lanes, though it says lanes can suit strategic or technical models [src:2]. Silver models roles or departments within the organization as lanes in a single pool. Name a pool after the process it contains. Order the pools so message flows cross other pools as little as possible.

**More about layout and color.**

- **BPMN Layout Guideline:** A BPMN layout guideline is a set of drawing habits that make process diagrams easy to read: one flow direction, few crossings, no very long arrows, and clearly marked gateways.
- **Color Coding in BPMN Models:** Color coding adds a second visual layer to a BPMN diagram, on top of the standard shapes. It works best with few colors, a legend, and a diagram that still reads in grayscale.

## Example

An order process starts with the message start event "Receive order". The task "Check stock" leads to an XOR gateway named "Is the item in stock?". The branches are labeled "Yes" and "No". "Yes" leads to the task "Ship order" and the end event "Order shipped". "No" leads to the end event "Order rejected". The two end events show two different end states.
