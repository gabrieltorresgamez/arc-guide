---
title: Application Interface Diagram
slug: application-interface-diagram
category: enterprise-architecture
kind: artifact
summary: An application interface diagram shows how an organization's applications connect to each other.
  Each connection is labeled with its technology, such as REST or FTP. This makes integration dependencies
  visible.
arc42:
- 3
- 5
step: s08-integration-data
related:
- application-architecture-artifacts
- togaf
- c4-container-diagram
- architecture-viewpoint
- integration
- application-lifecycle-diagram
- uml-component-diagram
- enterprise-architecture-management
checks:
- Interfaces between applications are labeled with the technology used, such as REST or FTP.
- The diagram shows dependencies between applications, not only a list of applications.
- The view is scoped to the application landscape, not to the internals of one software system.
sources:
- url: https://bizzdesign.com/blog/practical-archimate-viewpoints-for-the-application-layer
  title: 'Enterprise Architecture modeling: Practical ArchiMate® viewpoints for the application layer'
  site: bizzdesign.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/container
  title: Container diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Generic application interface diagram: three applications, with each interface labeled by
    its technology.'
review:
  status: generated
  flags: []
---

## Explanation

An application cooperation view shows what the cooperation between applications looks like.

**Where the idea appears.** Other frameworks use other names. TOGAF has an application communication view. ArchiMate has an application cooperation viewpoint. Both show how applications cooperate. Dependencies between applications are often drawn in one of these two views. (See the articles TOGAF and Architecture Viewpoint.)

**Technology interfaces.** Showing the technology interface, such as REST or FTP, is a useful addition to a cooperation view.

**Dependencies.** A dependency means one element is used to support another.

**How it differs from a C4 container diagram.** A container diagram also shows technology choices and how its parts communicate. But it covers one software system. (See Container Diagram (C4 Level 2).)

## Example

A company has a web shop, an order system, and a warehouse system. The diagram draws one box for each. A line from the web shop to the order system is labeled "REST". A line from the order system to the warehouse system is labeled "FTP". A reader sees which application relies on which. They also see that two different technologies are in use.

## Trade-offs

The diagram shows connections and their technologies. It does not replace a view of one system's internals. For that, a C4 container diagram is scoped to a single software system. Choose the view that matches the question you need to answer.
