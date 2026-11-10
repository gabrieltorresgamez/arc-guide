---
title: Port
slug: component-port
category: modeling-uml
kind: notation-element
summary: A port is a named interaction point on the edge of a UML class, part, or component. It is where
  the owner offers services to its surroundings and makes requests of them.
arc42:
- 5
step: s10-document
related:
- provided-and-required-interface
- uml-interface
- delegation-connector
- component-connector-assembly-and-delegation
- uml-component-diagram
- nested-components-and-subsystems
- structure-diagram
checks:
- Ports that the environment can see are drawn straddling the boundary of their owner.
- Each port shows which interfaces the owner provides and which it requires through that port.
- Any behavior port belongs to an owner that has a defined behavior, so requests are not lost.
- Ports that pass requests to internal parts are connected to those parts.
sources:
- url: https://en.wikipedia.org/wiki/Composite_structure_diagram
  title: Composite structure diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.eecs.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/9.3.11.html
  title: ''
  site: eecs.uottawa.ca
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A component with one port that provides an interface and one that requires an interface.
review:
  status: generated
  flags: []
---

## Explanation

A port is a place where a structured classifier meets the outside world. A structured classifier is a class whose behavior is described, fully or partly, through interactions between its parts. The port connects it to those parts and to its environment.

**Where it sits.** Public ports are visible to the environment. In a diagram, they are drawn straddling the boundary of the owner.

**What it carries.** A port is linked to interfaces. The articles Provided and Required Interface and UML Interface explain them.
- Provided interfaces describe what the owner offers to its environment.
- Required interfaces describe requests the owner may make to its environment through that port.

**What happens to a request.** A port can pass a received request on to an internal part. This is called delegation. The article Delegation Connector covers it.

**Behavior port.** A behavior port sends requests to the owner's own behavior. If the owner has no behavior defined, anything arriving at that port is lost.

**Lifecycle.** When an instance of the owner is created, an instance of each of its ports is created too. Destroying a port also destroys the connectors attached to it.

## Example

Imagine an "Order Service" component with two ports. A port named "orders" offers an order-placing interface. A port named "payments" requires a payment interface. Callers see only these two named points on the border. The "orders" port hands each request to an internal part that handles it. When an Order Service instance is created, its two port instances are created with it.
