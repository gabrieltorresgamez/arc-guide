---
title: Deployment View
slug: distribution-view
category: documentation
kind: artifact
summary: The deployment view shows which hardware and environments run the system's building blocks. arc42
  documents it because infrastructure affects the system, and it suggests UML deployment diagrams.
arc42:
- 7
step: s10-document
related:
- deployment-diagram
- arc42-documentation-template
- arc42-crosscutting-concepts
- c4-model
- load-balancer
- 4-1-view-model
- deployment-diagram-modeling-mistakes
- distribution-view-antipatterns
checks:
- The document maps building blocks onto hardware.
- If the system runs in several environments, each relevant environment is documented.
- The deployment view uses a UML deployment diagram.
- The document explains how the infrastructure influences the system or its cross-cutting concepts.
sources:
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/deployment
  title: Deployment diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'A generic deployment diagram: building blocks mapped onto nodes.'
review:
  status: generated
  flags: []
---

## Explanation

A deployment view describes the infrastructure under your system. It shows which building blocks are mapped to which infrastructure elements. arc42 covers it in chapter 7, the Deployment View.

**Why document it.** According to arc42, the infrastructure under a system can and will influence the system and/or some of its cross-cutting concepts (see the article Crosscutting Concept). Because of this influence, arc42 says you need to know the infrastructure.

**How to express it.** arc42 says to use UML deployment diagrams, though stakeholders may use any diagram kind that shows nodes and channels. See the article UML Deployment Diagram for the notation.

**The mapping.** arc42 tip 7-5 says to document the mapping of building blocks onto hardware.

**Several environments.** Some systems run in more than one environment. In that case, arc42 advises documenting all relevant environments.

**Infrastructure nodes.** The C4 model has a similar deployment diagram. It can show infrastructure nodes next to deployment nodes. Examples are DNS services, load balancers and firewalls. (See the article Load Balancer.)

## Example

A team builds an online shop. Its deployment diagram shows a web server node running the shop application and a database node running the order database. A load balancer and a firewall sit in front of the web server.

## Trade-offs

The source pages name no explicit trade-offs.
