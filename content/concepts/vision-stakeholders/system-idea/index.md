---
title: System Idea
slug: system-idea
order: 10
category: vision-stakeholders
kind: concept
summary: A system idea is an early, high-level answer to how a system will be built. In arc42, the solution
  strategy section is its closest counterpart. It reuses proven patterns and is driven by quality goals
  and constraints.
arc42:
- 4
- 5
- 9
step: s07-solution-strategy
related:
- arc42-solution-strategy
- architectural-pattern
- architectural-overview-diagram
- quality-attribute-trade-off
- context-view
- architectural-decision
- architectural-pattern-vs-design-pattern
checks:
- The solution strategy summarizes the fundamental decisions that shape the architecture.
- The top-level decomposition names the pattern used, if any.
- Each strategic decision is tied to the problem statement, quality goals or key constraints.
- The document states how the key quality goals are achieved.
- Trade-offs between designs and their risks are identified and communicated.
sources:
- url: https://docs.arc42.org/section-4/
  title: 4 - Solution strategy | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://public.isaqb.org/curriculum-foundation/curriculum-foundation-en.html
  title: 'Curriculum forCertified Professional forSoftware Architecture (CPSA)®: Foundation Level'
  site: public.isaqb.org
  accessed: '2026-11-09'
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
- url: https://www.romanpichler.com/blog/the-product-vision-board/
  title: 'The Product Vision Board: Vision and Product Strategy'
  site: romanpichler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

In arc42, the solution strategy (see the article arc42 Solution Strategy) briefly sums up and explains the basic decisions and approaches that shape the system's architecture.

**What goes into it**

- **Top-level structure.** The decisions include how to split the system at the highest level. An example is using an architectural pattern or a design pattern. (See Architectural Pattern vs. Design Pattern.)
- **Reasons.** Each decision should be motivated by the problem statement, the quality goals and the key constraints. The strategy should also say how the key quality goals will be reached.

**Showing the idea**

The arc42 whitebox template for the overall system in the building block view contains an overview diagram. (See Architectural Overview Diagram and Context View.)

**Product Vision Board.** This template has sections for the vision, the target group (who benefits, who the users and customers are), the needs (the main problem the product addresses or its primary benefit), the key features and the business goals.

**More about the vision.**

- **Vision Statement:** A vision statement is a short, inspiring statement of the shared goal behind a product.

## Example

A team builds an online booking tool. Its main quality goal is that many people can book at once. A key constraint is a small team. The team writes a short idea: split the system into a web front end and a booking service, using a well-known pattern for that split. Each choice gets a one-line reason tied to the goal or the constraint.
