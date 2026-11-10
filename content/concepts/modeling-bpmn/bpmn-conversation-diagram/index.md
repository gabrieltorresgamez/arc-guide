---
title: BPMN Conversation Diagram
slug: bpmn-conversation-diagram
category: modeling-bpmn
kind: notation-element
summary: A BPMN conversation diagram gives a very high-level view of which participants exchange messages.
  It draws each group of exchanges as a hexagon called a conversation.
arc42:
- 3
step: s10-document
related:
- bpmn-collaboration-diagram
- bpmn-diagram-types
- bpmn-swimlane-pool-and-lane
- bpmn-2-0-notation-overview
- bpmn-focus-on-connected-businesses
checks:
- Conversations are drawn as hexagons with a single thin line.
- Sub-conversations carry a small square marker with a plus sign.
- Conversation links use double thin lines.
sources:
- url: https://ariscommunity.com/users/roland-woldt/2011-01-28-learning-bpmn-2-which-models-are-available-bpmn
  title: Learning BPMN 2 - Which models are available in BPMN? | ARIS BPM Community
  site: ariscommunity.com
  accessed: '2026-11-09'
- url: https://cloud.trisotech.com/bpmnrulebook/bpmn-rule-book/conversations.html
  title: 'Conversations :: BPMN Rule Book'
  site: cloud.trisotech.com
  accessed: '2026-11-08'
- url: https://www.visual-paradigm.com/tutorials/bpmn-conversation-diagram.jsp
  title: How to Draw BPMN Conversation Diagram?
  site: visual-paradigm.com
  accessed: '2026-11-09'
review:
  status: generated
  flags: []
---

## Explanation

A BPMN conversation diagram gives a "30,000-foot view" of how participants interact. BPMN is a standard notation for drawing business processes (see BPMN 2.0 Notation). A participant is a party in the exchange, drawn as a pool. Pools are explained in BPMN Swimlane (Pool and Lane).

The diagram shows the messages that pass between those participants. It presents them as conversation objects instead of individual messages.

**Notation rules**

- A conversation is a hexagon drawn with a single thin line.
- A sub-conversation is also a hexagon with a single thin line. It adds a small square marker with a plus sign inside.
- Conversation links are drawn with double thin lines.

The plus marker tells the reader that a hexagon is a sub-conversation, not a plain conversation.

For the notation that shows full message flows, see BPMN Collaboration Diagram. For an overview of all BPMN diagram types, see BPMN Diagram Types.

## Example

Imagine an online shop, a payment provider, and a delivery company. One hexagon, labeled "Order payment," links the shop and the payment provider. A second hexagon, labeled "Shipping," links the shop and the delivery company. A reader sees who exchanges messages with whom, without reading any message detail.

## Trade-offs

The diagram stays at a coarse level. It shows conversations between participants, not the detail of each message.
