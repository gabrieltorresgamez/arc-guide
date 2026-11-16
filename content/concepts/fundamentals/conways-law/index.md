---
title: Conway's Law
slug: conways-law
order: 55
category: fundamentals
kind: principle
summary: Conway's law says that the structure of a system tends to copy the communication structure of the organization that builds it. Teams and architecture should be designed together.
arc42:
- 1
- 4
step: s07-solution-strategy
related:
- software-architecture
- big-ball-of-mud
- microservices-architecture
- architecture-principle
- agile-architecture
- modularity
checks:
- The documentation states how the planned architecture relates to the structure of the teams that build it.
- Where teams work in different places or time zones, the interactions between their components are well defined and limited.
sources:
- url: https://martinfowler.com/bliki/ConwaysLaw.html
  title: "Conway's Law"
  site: martinfowler.com
  accessed: '2026-11-16'
- url: https://en.wikipedia.org/wiki/Conway%27s_law
  title: "Conway's law - Wikipedia"
  site: en.wikipedia.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Conway's law links the way an organization communicates to the systems it designs. Melvin Conway described it in his article "How Do Committees Invent?". His wording is that organizations that design systems are constrained to produce designs that are copies of the communication structures of those organizations. Martin Fowler calls it important enough to affect every system he has come across.

**Why it happens.** For a product to work, the authors of its parts must communicate to make the parts fit together. The technical structure of the system therefore reflects the social boundaries of the organization, because communication is harder across them.

**What it says, and what it does not.** In a strict sense the law is about correspondence. It does not say that the communication structure causes the system structure. Commentators differ on the direction of causality.

**Effects in practice.**

- If an architecture is designed at odds with the structure of the development organization, tensions appear in the software. Interactions meant to be simple become complicated because the teams responsible for them do not work well together.
- Design alternatives are not even considered when the groups that would have to build them do not talk to each other.
- Teams on separate floors communicate less, and teams in separate cities or time zones even less. Components built in different places need a well-defined and limited interaction.
- A dozen or two people can communicate deeply and informally. The law therefore predicts that they build a monolith.

**Responses.** Fowler's first step is to not fight the law. Organizing teams by software layer (front end, back end, database) or by life-cycle activity (analysis, design, coding, testing) works against feature development. Each feature then needs close collaboration across teams, or many hand-offs. A third way is to deliberately change the team organization to encourage the architecture you want.

## Example

A shop has a front-end team, a back-end team and a database team. Every new feature, such as a discount code, needs all three. The software ends up as three layers with many requests passing between them, which mirrors the three teams. If the shop forms one team per business area instead, each team builds its feature from the screen down to the data.

## Trade-offs

Opinions vary on whether the mirroring is desirable. Some call it a helpful feature of such systems. Others call it an undesirable result of organizational bias.
