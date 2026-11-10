---
title: Software Connector
slug: software-connector
category: fundamentals
kind: concept
summary: A connector is the element of an architecture description that stands for an interaction between
  components. It plugs into component ports, and its interface is a set of roles, one per participant.
arc42:
- 5
- 6
step: s10-document
related:
- component-port
- component-view
- classification-of-integration-patterns
- connector-cardinality
- connector-transparency
- connectors-and-distribution
- component-connector-assembly-and-delegation
- provided-and-required-interface
checks:
- Interactions between components are shown as explicit connectors in the architecture description.
- Each connector names its roles, so each participant in the interaction is identifiable.
- Each connector plugs into identified ports of the components it joins.
sources:
- url: https://arxiv.org/html/cs/0105009
  title: Using Dependence Analysis to Support Software Architecture Understanding
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A connector joins the ports of two components. Each end of the connector is a role.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Software is built from parts called components. Components rarely work alone. They interact. An architecture description needs a way to show these interactions. That is the job of a **connector**.

A connector represents an interaction between components.

**Ports.** A component has ports. A port is a point where the component interacts with its environment. Connectors plug in at these points. The article *Port* covers ports in more detail.

**Roles.** A connector has an interface, just as a component does. The connector's interface is a set of roles. Each role is one participant in the interaction. A connector for an interaction between two parties therefore has a role for each side.

Putting the pieces together:

- Components own the ports.
- Connectors own the roles.
- Plugging a connector into a port ties a component into the interaction.

This keeps two questions apart. Components answer "what are the parts?" Connectors answer "how do the parts interact?"

## Example

Imagine a small shop system with two components: an "Order Service" and a "Payment Service". The Order Service has a port where it asks for payments. The Payment Service has a port where it receives payment requests. A connector joins the two ports. It has two roles: one for the party that asks and one for the party that answers. In a diagram, you would draw this as a line between two boxes.
