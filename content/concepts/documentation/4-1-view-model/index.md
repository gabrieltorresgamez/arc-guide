---
title: 4+1 View Model
slug: 4-1-view-model
category: documentation
kind: framework
summary: The 4+1 View Model describes a software system through several views at once. Each view speaks
  to different stakeholders. A fifth view, made of scenarios, illustrates how the architecture works.
arc42:
- 5
- 6
- 7
step: s10-document
related:
- architecture-view-model
- architecture-view
- architecture-viewpoint
- c4-model
- use-case
- stakeholder
- distribution-view
- runtime-view
checks:
- The architecture description uses several views, each aimed at named stakeholders.
- The description covers the logical, development, process and physical (deployment) views.
- A small set of scenarios or use cases illustrates the architecture as a fifth view.
sources:
- url: https://en.wikipedia.org/wiki/4%2B1_architectural_view_model
  title: 4+1 architectural view model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://c4model.com/faq
  title: FAQ | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Scenarios illustrate the architecture across the four views.
review:
  status: generated
  flags: []
---

## Explanation

The 4+1 View Model is a way to describe the architecture of software-intensive systems. It uses several views at the same time. Each view shows the system as one group of stakeholders sees it: end users, developers, system engineers or project managers, for example. (See the article Stakeholder.)

**The four views**

- **Logical view.** It covers the functionality the system gives to end users.
- **Development view.** It shows the system from the programmer's perspective. It concerns software management.
- **Process view.** It covers the dynamic side of the system. It explains the system's processes and how they communicate.
- **Physical view.** It is also called the deployment view. It takes the system engineer's standpoint. It concerns the topology of software components on the physical layer and the physical connections between them.

**The "+1": scenarios**

A small set of use cases, called scenarios, illustrates the architecture. These scenarios form a fifth view. (See the article Use Case.)

**Link to other approaches**

The C4 model was inspired by UML and by the 4+1 model. See the articles C4 Model and Unified Modeling Language (UML).

## Example

A team builds an online ticket shop. The logical view describes what customers can do: search events, pick seats, pay. The development view shows how programmers organize the code. The process view shows how the system's processes communicate while it runs. The physical view shows which hardware runs which parts. One scenario, "a customer buys two tickets", illustrates the architecture across these views.
