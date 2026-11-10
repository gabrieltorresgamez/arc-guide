---
title: Architecture Disciplines
slug: architecture-disciplines
category: fundamentals
kind: concept
summary: Architecture work happens at different scopes. A common picture compares enterprise architecture
  to city planning and solution architecture to a building design. Several specialist disciplines, such
  as network architecture, help shape one solution.
arc42:
- 3
- 4
step: s02-scope-context
related:
- enterprise-architecture-management
- software-architecture
- relationship-between-enterprise-architecture-and-application-architecture
- application-architecture
- architecture-levels
- software-architect-role
- data-architecture
- technology-architecture
checks:
- The document states whether a piece of work belongs to solution scope or enterprise scope, and does
  not leave the boundary implicit.
- Specialist disciplines used for the solution, such as network design, are named.
sources:
- url: https://www.windley.com/archives/2003/09/enterprise_arch_4.shtml
  title: Enterprise Architecture and City Planning
  site: windley.com
  accessed: '2026-11-09'
- url: https://www.leanix.net/en/blog/solution-vs-enterprise-architecture
  title: Solution Architecture Vs Enterprise Architecture
  site: leanix.net
  accessed: '2026-11-09'
- url: https://www.redhat.com/en/blog/what-type-it-architect-are-you
  title: What type of IT architect are you?
  site: redhat.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/archive/blogs/kaevans/solution-architect-vs-enterprise-architect-central-planning
  title: 'Solution Architect vs Enterprise Architect: Central Planning | Microsoft Learn'
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Architecture work does not have one single scope. A popular way to explain the scopes is a city analogy.

**Enterprise architecture** is like city planning. Its scope is the business as a whole, aligned with technical activity. It helps decide how areas relate to each other. It also helps decide how utilities such as water and electricity fit into the bigger picture. It does not decide who builds what.

**Solution architecture** takes the role of "architecture within the land." Software architecture, separately, is likened to building design. (See *Software Architecture* and *Enterprise Architecture* for each topic in depth.)

**Several disciplines work together.** A solution architect uses whatever discipline the problem requires, such as retraining staff, engineering, or a change of strategy. Specialist roles exist beside the enterprise role. A network architect, for example, applies network technology to system designs.

**The boundaries are blurry.** Solution architecture and enterprise architecture are often seen as overlapping. One writer says most IT architects do not understand the boundary between them. One proposal is to let solution architecture own the "architecture within the land" and let enterprise architecture own the "architecture within the city."

## Example

A company plans a new online ordering system. At the city level, planners decide how the ordering area relates to other business areas and how shared services fit in. They do not decide who builds the system. At the plot level, the solution team designs the ordering system itself.
