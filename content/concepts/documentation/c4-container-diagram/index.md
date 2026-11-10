---
title: Container Diagram (C4 Level 2)
slug: c4-container-diagram
category: documentation
kind: notation-element
summary: 'A container diagram zooms into one software system and shows its separately running parts: applications
  and data stores. It also shows the main technologies and how the parts talk to each other.'
arc42:
- 5
- 3
step: s10-document
related:
- c4-model
- c4-level-1-system-context-diagram
- c4-level-3-component-diagram
- distribution-view
- arc42-documentation-template
- architectural-overview-diagram
checks:
- The container diagram covers a single software system and follows from the system context view.
- Every container is an application or a data store that must be running for the system to work.
- Databases and file systems appear as containers.
- Each container shows its major technology, and the arrows show how containers communicate.
- Clustering, load balancing, replication and failover are not detailed here but in deployment diagrams.
sources:
- url: https://c4model.com/diagrams/container
  title: Container diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://c4model.com/abstractions/container
  title: Container | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.c4.puml
  caption: Generic container diagram of an invented online library system.
review:
  status: generated
  flags: []
---

## Explanation

A container diagram is the second level of the C4 Model (see the article "C4 Model"). It zooms in from the System Context Diagram, which shows the system as a single box. The container diagram opens that box.

**What a container is.** In C4, a container is either an application or a data store. It is a runtime boundary: a border around code that is being executed or data that is being stored. A container is also something that must be running for the whole system to work.

**Typical containers.**
- A server-side web application.
- A client-side single-page application, for example a JavaScript app running in a web browser.
- A desktop application.
- A mobile app.
- Data stores such as a database or a file system. A file system can be a full local one or part of a larger networked one.

**What the diagram shows.** Each container appears with its major technology choice. The arrows show how containers communicate with one another. Readers can see which parts exist, what they are built with, and how they connect.

**Who reads it.** The audience is technical people, both inside and outside the development team.

**What it leaves out.** The diagram says very little about deployment topics such as clustering, load balancers, replication or failover. Those belong in deployment diagrams (see "Deployment View").

**Link to arc42.** In the arc42 building block view, level 1 is the white box of the whole system. Level 2 of that view zooms into some level-1 blocks.

## Example

An online library system could have four containers. A single-page application runs in the reader's browser. A mobile app offers the same features on a phone. A server-side web application handles their requests. A database stores the book catalog. The arrows from the two apps to the web application are labeled with the protocol they use. The arrow from the web application to the database shows reads and writes. Each box names its technology.

## Trade-offs

The diagram gives a clear overview of the parts and their technologies. It does not show how those parts are deployed, such as clustering or failover. The source says deployment information is better captured in deployment diagrams, one per environment. It also does not show the inner structure of a single container. That detail belongs in the next level, the component diagram.
