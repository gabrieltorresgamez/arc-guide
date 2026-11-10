---
title: Process Model versus Process Instance
slug: process-model-versus-process-instance
category: modeling-bpmn
kind: concept
summary: A process model is the blueprint of a business process. A process instance is one run of it,
  tracked by a token and identified by a unique key.
arc42:
- 6
- 8
- 12
step: s10-document
related:
- bpmn-gateway-semantics
- bpmn-event
- bpmn-collaboration-diagram
- correlation-identifier
- bpmn-core-elements
- runtime-view
- data-exchange-between-bpmn-processes
- bpm-life-cycle
checks:
- The document states that a model is deployed as a versioned process definition from which instances
  are started.
- Each message a process waits for names the attribute used to correlate it to the right waiting instance.
- Parallel gateways are used where several paths must run at once, and exclusive gateways where data selects
  one path.
sources:
- url: https://docs.camunda.io/docs/reference/glossary/
  title: Glossary | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/best-practices/development/routing-events-to-processes/
  title: Routing events to processes | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'One model: an exclusive gateway picks one path per instance, then a parallel gateway creates
    two tokens.'
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A **process model** is the drawing of a business process. Once deployed to a process engine and versioned, it is called a process definition. You use it to start instances.

A **process instance** is one execution of that definition. Each instance has its own unique key.

A **token** shows where an instance currently is. You can picture execution as tokens running through the model. A token marks the current point of execution. Once the token arrives at the end of the process, it is used up and the instance finishes.

Gateways decide which path a token takes. Gateways control how the flow branches, merges, or synchronizes (see the article BPMN Gateway):

- An **exclusive gateway** picks one outgoing sequence flow based on data.
- A **parallel gateway** creates new tokens by activating several sequence flows at once.

So one instance can hold several tokens at the same time.

**Correlation** links an incoming message to the right running instance. The message carries an attribute that is matched against a variable of the instance. A correlation key is required when you publish a message. A payment, for example, must reach the right waiting instance.

## Example

A company models a "handle complaint" process once and deploys it. Monday's complaint from customer A starts instance 1. Tuesday's complaint from customer B starts instance 2. Each instance has its own key and its own token.

In instance 1, an exclusive gateway sends the token to "refund". In instance 2, the same gateway sends it to "replace item". The model is the same, but each instance takes a different path.

Later, a message "customer replied" arrives. Its correlation attribute, such as a complaint number, tells the engine which waiting instance should receive it.
