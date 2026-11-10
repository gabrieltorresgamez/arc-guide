---
title: Business and Technical Context
slug: business-and-technical-context
category: documentation
kind: concept
summary: Business context shows which data a system exchanges with people and neighboring systems. Technical
  context shows the channels and protocols that carry that data. Documenting both, and linking them, helps
  stakeholders decide.
arc42:
- 3
step: s02-scope-context
related:
- arc42-context-and-scope
- context-view
- c4-level-1-system-context-diagram
- deployment-diagram
- context-view-antipatterns
- refining-complex-context-views
- component-port
- provided-and-required-interface
checks:
- The business context shows the system as a black box with its domain interfaces to each communication
  partner.
- Business context arrows show data flows, not dependencies.
- Business and technical context are kept as separate views.
- Each domain interface is explained by its technical realization (protocol or channel).
- All external interfaces are shown, and the context stays an overview.
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
- file: diagram-1.mmd
  caption: 'Same neighbors seen twice: data flows (business) and channels (technical).'
review:
  status: generated
  flags: []
---

## Explanation

A system does not work alone. It talks to users and to neighboring systems. arc42 (a template for architecture documentation) describes this in section 3, Context and Scope. It offers two views of the same boundary.

**Business context**

- The goal is that all stakeholders understand which data the system exchanges with its environment.
- The diagram treats the system as a black box. You see only the outside, not the inner parts.
- It names the domain interfaces to each communication partner.
- It should show data flows, not dependencies.

**Technical context**

- It covers the technical interfaces that link the system to its environment. These are channels and transmission media.
- Use it to describe protocols or channels.
- It matters because many stakeholders base architectural decisions on these interfaces.
- arc42 suggests a UML deployment diagram for the channels to neighboring systems. See the article UML Deployment Diagram.

**Keeping the views apart, then linking them**

arc42 advises you to differentiate the two views. It also advises you to explain how each domain interface is technically realized. A simple table can do this: one row per business interface, with its channel or protocol.

**Notation**

A C4 system context diagram puts the system in the center, among users and external systems. It is a zoomed-out view. It deliberately leaves out technologies and protocols. See the article System Context Diagram.

**Common mistakes to avoid**

- Leaving out an external interface. arc42 says to show all of them.
- Adding excess detail. Keep the context an overview.
- Drawing dependencies instead of data flows in the business view.

If several neighbors are alike, you can cluster them using ports.

## Example

An invented online shop. The business context shows a customer sending orders and receiving confirmations. It shows a payment provider receiving payment requests and returning results. The technical context then adds a table.

| Business interface | Channel |
|---|---|
| Order from customer | Web page over HTTPS |
| Payment request | Provider's web API |
| Shipping notice | Daily file drop |

The first view answers "what data moves?". The second answers "how does it move?".

## Trade-offs

A C4 context diagram is simple and leaves out protocols.
