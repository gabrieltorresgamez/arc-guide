---
title: Requirements Difficulty and Customer Engagement
slug: requirements-difficulty-and-customer-engagement
category: functional-requirements
kind: principle
summary: Deciding exactly what to build is the hardest part of software work, and clients cannot specify
  it fully up front. Frequent customer contact, such as reviews and daily collaboration, corrects direction
  early.
arc42:
- 1
- 11
step: s03-functional-requirements
related:
- iterative-and-incremental-development
- stakeholder
- stakeholder-identification
- architecturally-significant-requirement
- solution-as-moving-target
- agile-architecture
- requirements-elicitation
- method-phase-working-with-functional-requirements
checks:
- The document names how and how often the team gets feedback from customers or users, such as sprint
  reviews or an on-site customer.
- The customer representatives are named, and the document states whether they represent the wider customer
  side.
- The document states who invites stakeholders to reviews and who receives priority change requests.
- The document does not rely on the claim that late requirements errors always cost more as the only reason
  for early feedback.
sources:
- url: https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet
  title: No Silver Bullet
  site: cgl.ucsf.edu
  accessed: '2026-11-09'
- url: https://agilemanifesto.org/principles.html
  title: Principles behind the Agile Manifesto
  site: agilemanifesto.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/OnsiteCustomer.html
  title: Onsite Customer
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.martinfowler.com/bliki/PleasingTheCustomer.html
  title: Pleasing The Customer
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://scrumguides.org/scrum-guide-2017.html
  title: Scrum Guide 2017 | Scrum Guides
  site: scrumguides.org
  accessed: '2026-11-09'
- url: https://arxiv.org/html/1609.04886v1
  title: Are Delayed Issues Harder to Resolve? Revisiting Cost-to-Fix of Defects throughout the Lifecycle
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Each customer contact point corrects the direction of the work.
review:
  status: generated
  flags: []
---

## Explanation

Brooks calls deciding precisely what to build the hardest single part of building a software system. He adds that no other part cripples the finished system as badly when done wrong. He also says no other part is more difficult to rectify later.

Clients cannot state their requirements completely at the start. Brooks therefore asks for extensive iteration between client and designer.

The Agile principles take a similar view:
- Early and continuous delivery of valuable software is the highest priority.
- Late changes to requirements are welcome.
- Business people and developers work together daily throughout the project.

**Common practices**

- **Sprint Review.** In Scrum, the team shows its latest working result (the Increment) to stakeholders. The goal is to get feedback and encourage collaboration. The Product Owner invites the key stakeholders.
- **Product Owner.** This person is the one whom anyone wanting to change a backlog item's priority must address.
- **On-site customer.** In Extreme Programming (XP), a business-side person sits with the developers. They answer questions and make decisions about the business value of features. The customer may be one person but is more commonly a team.

Fowler says interactive communication can avoid much of the misunderstanding that documents or intermediaries cause.

**Risks**

- If developers only see customers through intermediaries or documents, the motivational link to customers is broken.

See also Iterative and Incremental Development for the wider working style.

## Example

A team builds an internal booking tool. Every two weeks it shows working screens to the people who will use it. In the second review, a user points out that bookings often change after confirmation. The team had not known this. It adjusts its plan before building more on the wrong assumption. Had the team waited until the end, the gap between what users needed and what existed would have been much larger.

## Trade-offs

In Scrum, the Product Owner is one person, and anyone who wants to change a backlog item's priority must go through them. XP's on-site customer must be physically present with the developers.

The belief that requirements errors cost most when found late is widely cited. However, a 2016 empirical study of 171 projects found no evidence for a delayed issue effect, and suggested it may occur only intermittently.
