---
title: Provided and Required Interface
slug: provided-and-required-interface
category: modeling-uml
kind: notation-element
summary: A provided interface lists what a component offers. A required interface lists what it needs
  from others. UML draws them as a ball and a socket, which makes the dependencies between building blocks
  visible.
arc42:
- 5
- 3
step: s10-document
related:
- uml-interface
- uml-component-diagram
- component-port
- component-connector-assembly-and-delegation
- component-view
- component-diagram-modeling-mistakes
checks:
- Provided interfaces are drawn as balls that name the services, data, or events a building block offers.
- Required interfaces are drawn as sockets on the component that depends on them.
- Ball and socket notation is combined with port symbols where a component has several interfaces.
sources:
- url: https://en.wikipedia.org/wiki/Component_diagram
  title: Component diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/D-5/
  title: 'Question D-5: How can I describe interfaces with UML? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/RequiredInterface.html
  title: Required Interface
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.nomagic.com/MT/2026x/magic-cyber-systems-engineer---cameo-systems-modeler/provided-and-required-interfaces-272731184.html
  title: Provided and Required Interfaces
  site: docs.nomagic.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Payment provides the Charge interface (realization). Order requires it (usage dependency).
review:
  status: generated
  flags: []
---

## Explanation

A component is a building block of a system. It usually works with other building blocks. Two ideas describe how it connects to them: what it offers, and what it needs.

**Provided interface.** This is what a component offers to others. In a UML component diagram (see UML Component Diagram), it appears as a ball, also called a lollipop. The ball carries the name of the interface. A solid line links it to the component that provides it.

**Required interface.** This is what a component needs from others. It is a usage dependency. UML draws it as a half-circle, called a socket, attached to the component that has the need.

**Who defines it.** A common view is that the supplier decides what to expose. A required interface turns this around. The client of an interaction defines it.

**Why show them.** Ball and socket notation makes explicit which services, data, or events a providing building block offers.

**Ports.** arc42 suggests using ball and socket together with port symbols. In a modeling tool, the port shows its provided and required interfaces in ball-socket notation. If you pick the port type manually, the tool automatically creates a realization dependency (provided) or a usage dependency (required) from that port type to the interface. A port can provide or require many interfaces, and you can choose which ones to display or hide.

## Example

An online shop has an Order component and a Payment component. Payment offers a "Charge" interface, drawn as a ball. Order needs a way to charge customers, so it shows a socket named "Charge". Reading the diagram, you see that Order depends on Payment through "Charge". Order's needs define what "Charge" must contain. Payment provides it.

## Trade-offs

A port can provide or require many interfaces, so a diagram can show only some of them.
