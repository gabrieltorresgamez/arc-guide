---
title: UML Component Diagram
slug: uml-component-diagram
order: 20
category: modeling-uml
kind: notation-element
summary: A UML component diagram shows the high-level structure of a software system. It shows the parts
  and the behavior they offer and use through interfaces.
arc42:
- 5
step: s10-document
related:
- component-view
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
- url: https://en.wikipedia.org/wiki/Composite_structure_diagram
  title: Composite structure diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.eecs.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/9.3.11.html
  title: ''
  site: eecs.uottawa.ca
  accessed: '2026-11-09'
- url: https://developer.ibm.com/articles/the-component-diagram/
  title: The component diagram
  site: developer.ibm.com
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/B-9/
  title: 'Question B-9: What is a whitebox? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://guides.visual-paradigm.com/docs/mastering-uml-2-5-a-use-case-driven-approach-to-agile-modeling/module-3-the-skeleton-the-7-structural-uml-diagrams/component-diagrams/
  title: Component Diagrams - Visual Paradigm Guides
  site: guides.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://issues.omg.org/issues/UML25-566
  title: Unified Modeling Language 2.5 (UML) FTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/D-5/
  title: 'Question D-5: How can I describe interfaces with UML? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/RequiredInterface.html
  title: Required Interface
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html
  title: Interfaces (The Java™ Tutorials > Learning the Java Language > Interfaces and Inheritance)
  site: docs.oracle.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/5-6/
  title: 'Tip 5-6: Hide the inner workings of blackboxes! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/interfaces
  title: Interfaces - define behavior for multiple types - C# | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BallAndSocket.html
  title: Ball And Socket
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-5-11/
  title: 'Question C-5-11: How does the hierarchy of building blocks relate to the arc42 sections (5.1,
    5.2 etc.)? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/abstractions/component
  title: Component | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://download.eclipse.org/modeling/mdt/uml2/javadoc/4.0.0/org/eclipse/uml2/uml/Connector.html
  title: Connector (UML2 Javadoc)
  site: download.eclipse.org
  accessed: '2026-11-09'
- url: https://issues.omg.org/issues/UML25-197
  title: Unified Modeling Language 2.5 (UML) FTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Acyclic_dependencies_principle
  title: Acyclic dependencies principle - Wikipedia
  site: en.wikipedia.org
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

**Place in arc42.** The arc42 building block view shows the static decomposition of a system into building blocks. It is mandatory, and it works like a floor plan. arc42 notes that component diagrams can show building-block hierarchies, because components can be nested.

**More about component diagram elements.**

- **Port:** A port is a named interaction point on the edge of a UML class, part, or component. It is where the owner offers services to its surroundings and makes requests of them.
- **Delegation Connector:** A delegation connector passes a component's external port inward to an internal part that does the real work. Outsiders see one contract, and the internal structure stays hidden.
- **Provided and Required Interface:** A provided interface lists what a component offers. A required interface lists what it needs from others. UML draws them as a ball and a socket.
- **UML Interface:** A UML interface is a contract that lists operations without implementing them. Classes or components realize it. Clients rely on the contract, not on the implementation behind it.
- **Nested Components and Subsystems:** A component can contain smaller parts that work together inside it. Ports on its edge pass outside requests to those parts. This lets you describe a system level by level, from a coarse view to detail.
- **Component Connector (Assembly and Delegation):** A connector links parts inside a component design. An assembly connector joins parts so some provide services and others use them. A delegation connector links a component's outer contract to the inner parts that realize it.

## Example

An online shop has three components: Orders, Payments and Notifications. Orders has a required-interface port for "charge payment". Payments has a provided-interface port that offers "charge payment". A ball-and-socket joins the two. Orders also needs "send message", which Notifications provides. Orders could itself contain nested parts, such as Cart and Checkout. A delegation would pass messages arriving at the Orders port on to Checkout.
