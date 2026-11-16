---
title: arc42 Deployment View
slug: arc42-deployment-view
order: 80
category: documentation
kind: artifact
summary: Chapter 7 of arc42 describes the technical infrastructure that runs the system and how building blocks are mapped onto it, for each relevant environment.
arc42:
- 7
step: s10-document
related:
- deployment-view
- arc42-building-block-view
- arc42-context-and-scope
- arc42-architecture-documentation-template
- arc42-crosscutting-concepts
- uml-deployment-diagram
checks:
- The deployment view shows the infrastructure and maps the building blocks to it.
- Every relevant environment, such as development, test and production, is documented.
- The deployment view exists when the system runs on more than one computer, server or container.
- Important reasons for the deployment structure are given.
sources:
- url: https://docs.arc42.org/section-7/
  title: "7 - Deployment view | arc42 Documentation"
  site: docs.arc42.org
  accessed: '2026-11-16'
- url: https://docs.arc42.org/tips/7-1/
  title: "Tip 7-1: Document your technical infrastructure (hardware)! | arc42 Documentation"
  site: docs.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The deployment view describes the technical infrastructure used to run the system. It covers elements such as locations, environments, computers, processors, channels and network topologies. It also shows the mapping of the software building blocks onto these infrastructure elements.

**Environments.** Systems often run in several environments, for example development, test and production. arc42 says to document all relevant environments.

**When it matters most.** Document the deployment view when the software runs as a distributed system with more than one computer, processor, server or container, or when you design your own hardware processors and chips. From a software perspective it is enough to capture the infrastructure elements that are needed to show where the building blocks run.

**Why it exists.** Software does not run without hardware. The infrastructure can and will influence your system and some cross-cutting concepts, so you need to know it.

**How to write it.** The highest-level deployment diagram may already be in section 3.2 as the technical context, with your own infrastructure as one black box. This chapter zooms into that black box with further deployment diagrams. UML deployment diagrams fit well, with nesting when the infrastructure is complex. Stakeholders who prefer other diagram kinds may use any kind that shows nodes and channels.

Section 7.1 describes the infrastructure at level 1: the distribution to locations and environments, the physical connections, the reasons for the structure, quality and performance features of the infrastructure, and the mapping of building blocks to infrastructure elements.

See the article Deployment View for the view in general.

## Example

A web shop runs on two application servers behind a load balancer and one database server in production. A UML deployment diagram shows the three nodes and their connections, and a table maps the order service and the web interface to the application servers. A second, smaller diagram shows the single-server test environment.

## Trade-offs

arc42 asks to document all relevant environments, and to copy the section for each environment.
