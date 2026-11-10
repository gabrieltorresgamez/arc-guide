---
title: Distribution View Antipatterns
slug: distribution-view-antipatterns
category: documentation
kind: concept
summary: 'A deployment view shows how software maps onto hardware and infrastructure. Reviewers should
  check three things: the mapping, the environments covered, and whether infrastructure nodes appear.'
arc42:
- 7
step: s10-document
related:
- distribution-view
- deployment-diagram-modeling-mistakes
- deployment-diagram
- c4-model
- arc42-crosscutting-concepts
- component-view-antipattern-lifting-code-to-model-level
- context-view-antipatterns
- load-balancer
checks:
- The deployment view documents which building blocks run on which hardware or infrastructure.
- All relevant environments are documented.
- Each deployment diagram covers a single environment, such as production or staging.
- Infrastructure nodes such as DNS, load balancers, and firewalls appear where they matter.
sources:
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/deployment
  title: Deployment diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The deployment view describes the technical infrastructure that runs a system. The article "Deployment View" explains the basics.

**Why the view exists.** The infrastructure under a system can influence the system. It can also influence cross-cutting concepts, so you need to know the infrastructure.

**Keep the mapping at the center.** arc42 advises documenting which building blocks run on which hardware or infrastructure.

**Show each environment.** Many systems run in more than one environment, such as production and staging. arc42 says to document all relevant environments.

**Use the C4 convention as a guide.** A C4 deployment diagram shows one or more software systems within a single deployment environment, for example production, staging, or development. C4 also lets you add infrastructure nodes such as DNS services, load balancers, and firewalls. See "C4 Model" and "Load Balancer" for more.

**What to ask in a review.** Does the diagram link building blocks to infrastructure? Does it cover every relevant environment? Is the infrastructure that shapes the system visible?

## Example

A team documents an online shop. Their first deployment diagram lists the shop's building blocks but never says where they run. The team revises it. They draw one diagram for production and one for staging. Each diagram links the building blocks to the machines they run on. The production diagram also shows the load balancer and the firewall in front of the shop.


