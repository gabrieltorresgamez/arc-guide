---
title: BPMN Diagram Types
slug: bpmn-diagram-types
category: modeling-bpmn
kind: notation-element
summary: BPMN offers collaboration diagrams, which show pools and the messages between them, and conversation
  diagrams, which give a high-level view of what participants talk about. Choreography diagrams are a
  newer third type.
arc42:
- 3
- 6
step: s10-document
related:
- bpmn-collaboration-diagram
- bpmn-conversation-diagram
- bpmn-swimlane-pool-and-lane
- bpmn-2-0-notation-overview
- data-exchange-between-bpmn-processes
- levels-of-process-modeling
- bpmn-modeling-tips
- runtime-view
checks:
- A diagram meant as a topic overview omits internal process steps and does not imply message order.
- Where a collaboration diagram shows a partner's internals as hidden, that partner's pool is drawn as
  a black box.
- Where message order between participants matters, a collaboration diagram is used rather than a conversation
  diagram.
sources:
- url: https://www.visual-paradigm.com/guide/bpmn/bpmn-orchestration-vs-choreography-vs-collaboration/;WWWSESSIONID=EC70CA1EB8C6EE5DFB98B1231D2FED1A.www1
  title: BPMN Orchestration vs Choreography vs Collaboration
  site: visual-paradigm.com
  accessed: '2026-11-09'
- url: https://skills.visual-paradigm.com/docs/bpmn-diagram-types-explained/bpmn-conversation-diagram/bpmn-conversation-diagram/
  title: What Is a BPMN Conversation Diagram? | BPMN Guide
  site: skills.visual-paradigm.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'A collaboration: a black-box customer pool sends a message to a white-box shop pool that shows
    its process.'
review:
  status: generated
  flags: []
---

## Explanation

BPMN is a notation for drawing business processes. It has more than one diagram type. Each type shows a different level of detail.

**Collaboration diagram**

A collaboration shows pools and the message flows between them. A pool stands for a participant. A message flow is a line showing a message passing from one pool to another.

A pool can take one of three forms:

- It can be empty.
- It can be a black box. You see the participant but not its inner workings.
- It can be a white box. You see the process inside the pool.

In a public process, the partners' internal processes stay hidden as black boxes. Only the messages between the partners are visible.

**Conversation diagram**

A conversation diagram is a high-level view of communication. It leaves out the internal steps of each process. It answers one question: which communication topics exist between the participants?

Conversation links carry no order or timing. They are not sequence flows. A conversation diagram also does not show the order of messages. A collaboration diagram does show this. So the two types complement each other.

**Choreography diagram**

Choreography diagrams are new in BPMN 2.0. They focus on interactions and message flows between processes. Their focus is the messages between the participant pools.

**Choosing a type**

- Use a conversation diagram for an overview of which topics the participants discuss.
- Use a collaboration diagram when you need to see how messages flow between participants.
- Use a choreography diagram when the interaction between processes is the main subject.

## Example

A web shop works with a payment provider. A conversation diagram lists the topics the two talk about, such as payment. It shows no steps and no order. A collaboration diagram then draws the shop as a white-box pool with its process inside. It draws the payment provider as a black-box pool. A message flow connects them, so readers see the exchange without the provider's internals.

## Trade-offs

A conversation diagram is quick to read, but it hides sequence and timing. A collaboration diagram shows the message flow, at a medium level of detail. Black-box pools keep partner internals out of view. The cost is that readers cannot see what happens inside those partners.
