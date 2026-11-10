---
title: Architectural Constraint
slug: requirements-versus-constraints
category: forces-decisions
kind: concept
summary: An architectural constraint is a requirement that limits how freely architects can design and
  build a system. Teams must always deal with constraints, though some can be negotiated. Writing them
  down shows where the design is free and where it is not.
arc42:
- 2
- 4
- 9
step: s05-constraints
related:
- arc42-constraints
- operational-constraint
- architecturally-significant-requirement
- architectural-forces
- arc42-solution-strategy
- architectural-decision
- quality-attribute
- markdown-architectural-decision-records-madr
checks:
- The document lists its constraints in one place, so architects can see where they are free and where
  they must comply.
- Each constraint states who wants it and why.
- The consequences of each constraint, such as extra cost or effort, are described.
- Constraints are grouped, for example into technical, organizational/political, and conventions.
sources:
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/2-2/
  title: 'Tip 2-2: Clarify the consequences of constraints! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/non-functional-requirements-as-user-stories
  title: Non-functional Requirements as User Stories - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html
  title: The Markdown ADR (MADR) Template Explained and Distilled
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A constraint is any requirement that limits the freedom of architects in their design and implementation decisions. Each constraint removes some design options. The more constraints a system has, the fewer choices remain.

**Constraints must be dealt with.** Some constraints can be negotiated, but the team cannot ignore them. A negotiable constraint still needs a conscious answer.

**Common kinds.** arc42 (a template for documenting architecture, see "arc42 Architecture Documentation Template") suggests three groups when a split helps:

- technical constraints
- organizational and political constraints
- conventions

**Non-functional requirements as constraints.** One view is to treat non-functional requirements (qualities such as speed or security, see "Quality Attribute") as constraints placed on the system. Seen this way, each quality target narrows the design choices a bit.

**Document them.** Written constraints tell architects where they are free and where they must comply.

**Record who and why.** Note who wants a constraint and the reason behind it. Without that, the team may later forget why the limit exists.

**State the consequences.** Constraints can bring extra cost or effort. arc42 advises clarifying these consequences. If a consequence is unreasonable, such as a cost that is excessively high, arc42 advises negotiating it with the relevant stakeholders (people with an interest in the system).

**Where they live.** arc42 has a section for architecture constraints (see "arc42 Constraints"). Decision templates such as MADR list constraints next to qualities, forces and concerns as decision drivers (see "Markdown Architectural Decision Records").

## Example

A team plans an online shop. The company already runs on one cloud provider and requires all services to use it. That is a technical constraint. The team records it, along with who requires it and why. They also note a consequence: some specialized tools from other vendors are off the table, which may mean extra effort. Architects now know the hosting choice is fixed, and they can spend their design freedom elsewhere.

## Trade-offs

Every constraint narrows the design choices a bit. Constraints can also cost money or effort. Some constraints can be negotiated, which may remove that cost. Leaving out the reason behind a constraint risks losing the rationale later.
