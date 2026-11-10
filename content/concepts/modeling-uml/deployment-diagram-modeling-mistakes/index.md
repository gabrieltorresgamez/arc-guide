---
title: Deployment Diagram Modeling Mistake
slug: deployment-diagram-modeling-mistakes
category: modeling-uml
kind: concept
summary: 'Deployment diagrams go wrong in a few repeated ways: deploying the wrong kind of element, mixing
  up node types, leaving connections unnamed, and leaving configuration unattached. Each has a simple
  fix.'
arc42:
- 7
step: s10-document
related:
- deployment-diagram
- distribution-view
- distribution-view-antipatterns
- uml-modeling-anti-patterns
- uml-component-diagram
- component-diagram-modeling-mistakes
- uml-modeling-best-practice
checks:
- Every deployment targets a node, and only artifacts (or artifact instances) are deployed onto it.
- Physical hardware nodes are marked «device». Software hosts such as an application server or JVM are
  marked «executionEnvironment».
- Each connection between nodes is labeled with its protocol, such as JDBC, REST or RMI.
- Each deployment specification is linked to the artifact it configures.
- Artifacts and components are shown as separate elements, and the direction of each «deploy» dependency
  has been checked.
sources:
- url: https://www.visual-paradigm.com/VPGallery/diagrams/Deployment.html
  title: Deployment Diagram - UML 2 Diagrams - UML Modeling Tool
  site: visual-paradigm.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Deployment_diagram
  title: Deployment diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A deployment diagram shows where software runs. Nodes appear as boxes. The artifacts allocated to each node appear as rectangles inside the boxes. The diagram also shows how nodes connect. See the article on the UML Deployment Diagram for the basics.

**Deploying the wrong thing.** UML defines a deployment as allocating an artifact (or an artifact instance) to a deployment target. A node is a computational resource on which artifacts may be deployed for execution.

**Confusing artifacts with components.** An artifact is a physical piece of information, such as a file or a script. A component may be manifested by one or more artifacts.

**Wrong node type.** A «device» is physical hardware with processing capability. An «executionEnvironment» is a software node that hosts certain kinds of components.

**Unnamed connections.** A deployment diagram also shows how the different pieces are connected, for example by JDBC, REST or RMI.

**Detached configuration.** A deployment specification holds the execution parameters of a deployed artifact. It is a separate element.

## Example

A team draws a box called "Order Server". They put an artifact, such as "orders.jar", inside the server node. They mark the server as an execution environment, because it is software. They mark the database host as a device, because it is hardware. They label the line between them with the protocol, such as JDBC. Finally, they attach the configuration file's deployment specification to "orders.jar".


