---
title: System Idea and Vision Elements
slug: system-idea-and-vision-elements
category: vision-stakeholders
kind: concept
summary: 'A system''s vision is built from linked parts: a vision statement, the target group, needs and
  value behind it, and the context. Each part is written with the others in mind, so requirements and
  context stay consistent.'
arc42:
- 1
- 3
step: s01-goals-stakeholders
related:
- system-idea
- vision-statement
- arc42-introduction-and-goals
- arc42-context-and-scope
- context-view
- stakeholder
- user-story
- business-and-technical-context
checks:
- The documentation has a stakeholder table with roles, names and expectations.
- The business context lists all communication partners and is understandable by all stakeholders.
- The vision statement summarizes the intention and motivation of the idea.
- Value in the vision is linked to business goals and the business case.
sources:
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/building-a-product-users-want-from-idea-to-backlog-with-the-vision-board
  title: 'Building a Product Users Want: From Idea to Backlog with the Vision Board - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Elements of a vision and how they build on each other.
review:
  status: generated
  flags: []
---

## Explanation

A system exists to improve how a business activity is supported. The requirements overview in arc42 (see *arc42 Introduction and Goals*) records those requirements and the driving forces that architects and the team must consider.

**The vision statement.** A vision board is one way to write the vision down. Its vision statement is a short summary of the idea. It covers the intention and the motivation behind it. See *Vision Statement*.

**Elements around the statement.** The vision board adds four more elements: target group, needs, product and value. The target group is the market or segment you want to address. Value explains why investing in the product is worthwhile and how the business goals can be achieved.

**Stakeholders.** arc42 asks for an explicit stakeholder overview. It is a table of roles, names and expectations. See *Stakeholder*.

**Requirements built on the vision.** Four questions about the users, their reasons, the product and the business goals should be answered before writing user stories, and the vision board helps answer them. Meaningful stories are impossible without knowing the users and their reasons. Once the key risks and critical assumptions on the board have been validated, the team uses it to create the initial backlog. See *User Story*.

**Context.** The business context lists all communication partners of the system. All stakeholders should understand which data are exchanged with the system's environment. If needed, the business context (domain-specific inputs and outputs) is kept apart from the technical context. See *Business and Technical Context*.

## Example

A team plans a booking tool for small clinics. The vision statement says the tool should make appointment handling less work for front-desk staff. The target group is small clinics. The need is fewer missed appointments. The value is lower staff cost for the clinic. The team then writes user stories for front-desk staff. It also lists the communication partners, such as patients and a calendar service, in the business context.

## Trade-offs

Meaningful stories are impossible without knowing the users and their reasons, so the vision comes first. The business context should be understandable to all stakeholders, and it can be differentiated from the technical context.
