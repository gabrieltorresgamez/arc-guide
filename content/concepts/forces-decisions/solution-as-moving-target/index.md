---
title: Solution as Moving Target
slug: solution-as-moving-target
category: forces-decisions
kind: concept
summary: The solution a team delivers rarely matches the one imagined at the start. Business changes and
  decisions made along the way move it. Good practice plans for this drift instead of fighting it.
arc42:
- 4
- 9
- 11
step: s07-solution-strategy
related:
- last-responsible-moment
- iterative-and-incremental-development
- agile-architecture
- arc42-solution-strategy
- evolutionary-domain-modeling
- design-for-change
- architectural-decision
- incrementality
checks:
- The document states which decisions were deliberately deferred instead of pretending everything was
  decided up front.
- The solution strategy is described as able to evolve, with iterative and incremental building.
- Ideas and approaches are documented after they proved useful.
- Reversible decisions are distinguished from hard-to-change ones, with more care given to the latter.
- Open decisions note when the most responsible moment for deciding arrives, guided by cost, effort and
  risk.
sources:
- url: https://www.martinfowler.com/articles/designDead.html
  title: Is Design Dead?
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/4-5/
  title: 'Tip 4-5: Let the solution strategy grow iteratively / incrementally! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://wirfs-brock.com/rebecca/blog/2011/01/18/agile-architecture-myths-2-architecture-decisions-should-be-made-at-the-last-responsible-moment/
  title: 'Rebecca’s Web – Agile Architecture Myths #2 Architecture Decisions Should Be Made At the Last
    Responsible Moment'
  site: wirfs-brock.com
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html
  title: A Definition of Done for Architectural Decision Making
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

At project start, the planned solution is only a rough idea. Many details are still open. As the team builds, it makes decisions and sees results. The solution takes shape and drifts away from the first plan.

**Why the plan drifts**

Fowler describes two ways to design. In planned design, you decide the design first. This idea comes from other branches of engineering. In evolutionary design, the design grows while the team builds the system. Upfront design cannot help with unforeseen changes, and it can even hurt. Many of these changes come from the business, so the target keeps moving.

**Not deciding everything up front**

The arc42 template (see *arc42 Architecture Documentation Template*) gives similar advice. The solution strategy may evolve during development. Do not try to decide everything at once. Build the system in small steps instead, iteratively and incrementally (see *Iterative and Incremental Development*).

**Timing decisions**

Some decisions are easy to undo. These matter less to get right. Fowler advises deferring decisions or finding ways to make them changeable. The *Last Responsible Moment* is the point where not deciding removes an important alternative. Wirfs-Brock warns that this idea can give false confidence that there is always time to change one's mind. She prefers a "most responsible moment". Zimmermann adds that teams should know when that moment arrives. Cost, effort, and risk help rank which decisions come first.

**The change curve**

A traditional belief says changes get exponentially more expensive as a project runs. Fowler calls this the change curve. This belief is what argues against evolutionary design.

**Documentation**

arc42 suggests documenting an idea or approach once it has proven useful.

## Example

A team plans an online ordering system. At the start, they only know that customers should order and pay. They defer the choice of payment provider and build a thin version of ordering first. Meanwhile, the business adds a new sales channel. The team picks the provider when the choice can no longer wait. They document the approach once it works. The delivered system differs from the first sketch, but it fits what the business needs.

## Trade-offs

Deferring decisions keeps options open, but waiting has a cost. If you wait too long, an important alternative disappears. Waiting can also create false confidence that there is always time left. Evolutionary design reacts well to change. It relies on changes staying affordable, which the change curve belief questions.
