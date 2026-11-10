---
title: Last Responsible Moment
slug: last-responsible-moment
category: forces-decisions
kind: principle
summary: The last responsible moment is the point where not deciding would remove an important option.
  Teams delay commitment until then. Waiting past the right moment is also harmful, so timing needs care.
arc42:
- 9
- 4
step: s09-decisions
related:
- definition-of-ready-for-architectural-decisions
- architectural-decision
- architectural-decision-management-practices
- architectural-decision-making-in-project-development
- architectural-decision-making-fallacies
- decision-dependencies
- agile-architecture
- levels-of-architectural-decisions
checks:
- Each open decision states whether its most responsible moment has come.
- Decisions are checked for being useful and needed now before they are made.
- Big architectural decisions with an early most responsible moment are identified and not postponed.
- Decisions are not delayed past their most responsible moment without a stated reason.
sources:
- url: https://blog.codinghorror.com/the-last-responsible-moment/
  title: The Last Responsible Moment
  site: blog.codinghorror.com
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://wirfs-brock.com/rebecca/blog/2011/01/18/agile-architecture-myths-2-architecture-decisions-should-be-made-at-the-last-responsible-moment/
  title: 'Rebecca’s Web – Agile Architecture Myths #2 Architecture Decisions Should Be Made At the Last
    Responsible Moment'
  site: wirfs-brock.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A team makes many choices while building software. Some are costly to undo. The Last Responsible Moment (LRM) is a timing rule for such choices. It names the point where failing to decide eliminates an important alternative. The advice is to delay commitment until that point.

**Most Responsible Moment.** A related idea is the Most Responsible Moment (MRM). It was proposed as a reaction to the lean principle "Decide as late as possible". The MRM asks for decisions to be taken when the time is right. They should be neither forced nor delayed. LRM thinking can invite late decisions, which is the risk the MRM addresses.

**Too early and too late.** Deciding too early harms flexibility. Deciding too late is also bad. Postponing a decision beyond its MRM can signal uncertainty or even fear.

**Readiness check.** A decision readiness check has five criteria: stakeholders, time, alternatives, requirements, and template. The time criterion asks three things:

- Is the problem important and urgent?
- Has the MRM of the decision come?
- Is the outcome useful and needed now?

The Architectural Decision Definition of Ready also stresses hitting the MRM. It links this to the lean idea of deciding late.

**Big decisions.** Some architectural decisions have an early MRM, so they should become ready early and not be revisited in every sprint. Rules of thumb exist for such "big" decisions to guide their timing.

## Example

A team must pick a database for a new product. Nothing built in the next few weeks depends on the choice, so the team keeps working with a simple storage layer.

Then a planned feature needs a kind of query that only some databases support. If the team does not choose now, a good option will be lost. That is the last responsible moment. The team runs the readiness check: the problem is urgent and the outcome is needed now. The team decides.

A decision that shapes the whole system may reach its right moment much earlier. Such a decision cannot wait for the feature.

## Trade-offs

Waiting keeps options open, but it has costs. Deciding too early harms flexibility. Deciding too late is also bad. Pure "decide as late as possible" thinking can invite late decisions, so the MRM asks for the right time instead. Procrastinating can also hide uncertainty or fear.
