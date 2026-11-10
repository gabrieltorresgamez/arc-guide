---
title: Component Connector (Assembly and Delegation)
slug: component-connector-assembly-and-delegation
category: modeling-uml
kind: notation-element
summary: A connector links parts inside a component design. An assembly connector joins parts so some
  provide services and others use them. A delegation connector links a component's outer contract to the
  inner parts that realize it.
arc42:
- 5
step: s10-document
related:
- delegation-connector
- provided-and-required-interface
- component-port
- uml-component-diagram
- nested-components-and-subsystems
- uml-interface
- software-connector
- component-view
checks:
- Each delegation connector runs from a port on the component boundary to an inner part that realizes
  the behavior.
- Each assembly connector joins a part that provides a service to a part that uses it.
- The elements at both ends of every connector have compatible interface features.
sources:
- url: https://download.eclipse.org/modeling/mdt/uml2/javadoc/4.0.0/org/eclipse/uml2/uml/Connector.html
  title: Connector (UML2 Javadoc)
  site: download.eclipse.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Delegation from an outer port to an inner part, and an assembly connector between two inner
    parts.
review:
  status: generated
  flags: []
---

## Explanation

A **connector** is a link between parts in a component design. UML defines two kinds: assembly and delegation. (For the basics of components, see UML Component Diagram. For ports, see Port.)

**Assembly connector.** It joins two or more parts, or ports on parts. Some parts provide services, and other parts use them.

**Delegation connector.** It links the external contract of a component to the inner parts that realize that behavior. The contract is expressed through the component's ports.

**How the kind is decided.** The kind is derived from where the ends attach. If an end attaches to a port that is not on a part, and is not a behavior port, the connector is a delegation. Otherwise it is an assembly.

**Compatibility.** The elements at both ends must be compatible. When one end requires certain interface features, the other end needs compatible provided features. See Provided and Required Interface for these terms.

**Instances, not classes.** Connectors specify links only between the instances that play the connected parts. They do not state a general relationship between classes.

**In arc42.** The building block view shows the static decomposition of a system into building blocks. arc42 gives no interface template. In the best case, examples or simple signatures are enough.

## Example

An "Order Service" component has an outer port named "orders". Inside it sit two parts: "Order Handler" and "Price Calculator".

- A delegation connector runs from the "orders" port to "Order Handler". Callers use the port. The handler does the work.
- An assembly connector joins "Order Handler", which uses prices, to "Price Calculator", which provides them.

## Trade-offs

Connectors describe links between instances playing parts, in contrast to associations, which specify links between any instances of the associated classifiers. The kind is derived from where the ends attach.
