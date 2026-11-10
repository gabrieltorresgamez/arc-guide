---
title: BPMN Modeling Guidelines
slug: bpmn-modeling-tips
category: modeling-bpmn
kind: practice
summary: BPMN modeling guidelines are simple naming and layout rules that keep process models readable.
  They cover page size, explicit start and end events, question-style XOR gateways, verb-object task names,
  and separate pools for partners.
arc42:
- 6
step: s10-document
related:
- bpmn-2-0-notation-overview
- bpmn-layout-guideline
- bpmn-2-0-model-quality
- bpmn-gateway-semantics
- bpmn-collaboration-diagram
- bpmn-swimlane-pool-and-lane
- levels-of-process-modeling
- antipatterns-for-process-flows
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

**Leave some gateways unnamed.** Camunda advises against naming parallel gateways and all joining gateways. Silver's style also leaves AND and event gateways unlabeled, including their gates.

**Name tasks as actions.** Camunda asks for an object and a verb in the infinitive, for example "Check invoice". Silver says all activities, subprocesses included, should be labeled, preferably as a verb-object action.

**Use pools for participants.** For models at the operational level, Camunda recommends separate pools for process participants instead of lanes, though it says lanes can suit strategic or technical models. Silver models roles or departments within the organization as lanes in a single pool. Name a pool after the process it contains. Order the pools so message flows cross other pools as little as possible.

## Example

An order process starts with the message start event "Receive order". The task "Check stock" leads to an XOR gateway named "Is the item in stock?". The branches are labeled "Yes" and "No". "Yes" leads to the task "Ship order" and the end event "Order shipped". "No" leads to the end event "Order rejected". The two end events show two different end states.
