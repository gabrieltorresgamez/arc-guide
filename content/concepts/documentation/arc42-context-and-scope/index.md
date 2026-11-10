---
title: arc42 Context and Scope
slug: arc42-context-and-scope
category: documentation
kind: artifact
summary: Context and Scope is the arc42 chapter that shows the system as a black box and what it exchanges
  with its environment. The business view covers the data exchanged. The technical view covers the channels.
arc42:
- 3
step: s02-scope-context
related:
- business-and-technical-context
- c4-level-1-system-context-diagram
- context-view
- context-view-antipatterns
- arc42-documentation-template
- arc42-introduction-and-goals
- c4-model
- stakeholder
checks:
- The context diagram shows the system as a black box with its communication partners around it.
- The domain data exchanged with each partner is stated, so all stakeholders can understand it.
- The technical context maps each domain input or output to the channel that carries it.
- A table, alone or next to the diagram, describes the interfaces.
sources:
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/system-context
  title: System context diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.c4.puml
  caption: 'Generic context diagram: the system as a central box with labeled exchanges.'
review:
  status: generated
  flags: []
---

## Explanation

This chapter shows where the system sits in its surroundings. The system appears as a black box: you see its outside, not its inner parts. Around it are its communication partners, meaning the users and neighboring systems it talks to.

**Business context.** This part shows the domain interfaces to each communication partner. It answers a simple question: what data goes in and out? All stakeholders (people with an interest in the system) should be able to understand this exchange. See *Business and Technical Context*.

**Technical context.** This part covers the technical interfaces: the channels and transmission media that link the system to its environment. It also maps each domain input or output to the channel that carries it. Many stakeholders base architectural decisions on these interfaces, so they deserve care.

**Diagram and table.** Any diagram works if it shows the system as a black box and names the domain interfaces to its partners. A table can replace the diagram or sit next to it.

**C4 option.** A C4 system context diagram is a good starting point for documenting a system. It puts the system as a box in the center, surrounded by users and external systems. The focus stays on people and software systems, not on technologies or protocols. See *System Context Diagram*.

## Example

A small online shop is the system. Its business context lists a customer (sends orders, receives confirmations), a payment provider (receives payment requests, returns approvals) and a shipping partner (receives parcel details). The technical context then adds a mapping: for each of these exchanges, it names the channel that carries it. A reader can see at a glance who talks to the shop, what they exchange, and over which channel.

## Trade-offs

A C4 context diagram leaves out technologies and protocols on purpose, keeping the focus on people and software systems.
