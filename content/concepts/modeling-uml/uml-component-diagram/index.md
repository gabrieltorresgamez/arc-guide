---
title: UML Component Diagram
slug: uml-component-diagram
category: modeling-uml
kind: notation-element
summary: A UML component diagram shows the high-level structure of a software system. It shows the parts
  and the behavior they offer and use through interfaces.
arc42:
- 5
step: s10-document
related:
- provided-and-required-interface
- component-port
- component-connector-assembly-and-delegation
- delegation-connector
- nested-components-and-subsystems
- component-view
- component-diagram-modeling-mistakes
- structure-diagram
checks:
- Each component's required interfaces are satisfied by a provided interface of another component, shown
  by a dependency or ball-and-socket.
- Interfaces are attached to components through ports, and each port has an interface as its type.
- Where a component has nested parts, delegations link its outer ports to inner parts.
- The diagram shows components interacting only through a restricted set of inputs and outputs.
sources:
- url: https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2012/dd409390(v=vs.110)
  title: 'UML Component Diagrams: Reference | Microsoft Learn'
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Component_diagram
  title: Component diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/D-4/
  title: 'Question D-4: How can I use UML to communicate a hierarchy of building blocks? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Orders requires two interfaces. Payments and Notifications provide them.
review:
  status: generated
  flags: []
---

## Explanation

A UML component diagram shows the high-level structure of a software system. It also shows the behavior its parts provide and consume through interfaces.

**Components.** A component is a reusable piece of functionality. It provides and consumes behavior through interfaces, and it can use other components. Components can be of any scale and any implementation language. What matters is that each one interacts with the rest only through a restricted set of inputs and outputs.

**Interfaces and ports.** A port sits on the boundary of a component. It is a property of the component, and an interface is its type.
- A provided-interface port stands for the operations the component implements for others to use.
- A required-interface port stands for the calls the component sends out. The component must be coupled to components that offer at least those operations.

**Connecting components.** A dependency arrow can show that one component's required interface is satisfied by another's provided interface. Dependencies can also link other elements more generally. UML also accepts the ball-and-socket convention. A provided interface is drawn as a lollipop (the ball). A required usage dependency is drawn as a half-circle (the socket).

**Internal structure.** A component can contain nested parts. An assembly connects the required ports of sibling parts to the provided ports of other sibling parts. A delegation connects an outer port to an inner part, so the part handles messages sent to the component.

**Place in arc42.** The arc42 building block view shows the static decomposition of a system into building blocks. It is mandatory, and it works like a floor plan. arc42 notes that component diagrams can show building-block hierarchies, because components can be nested. For related notation, see the articles Provided and Required Interface, Port, and Component Connector (Assembly and Delegation).

## Example

An online shop has three components: Orders, Payments and Notifications. Orders has a required-interface port for "charge payment". Payments has a provided-interface port that offers "charge payment". A ball-and-socket joins the two. Orders also needs "send message", which Notifications provides. Orders could itself contain nested parts, such as Cart and Checkout. A delegation would pass messages arriving at the Orders port on to Checkout.
