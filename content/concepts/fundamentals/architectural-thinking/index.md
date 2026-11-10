---
title: Architectural Thinking
slug: architectural-thinking
category: fundamentals
kind: method
summary: Architectural thinking is a repeated cycle of designing, checking and refining. It starts from
  requirements, quality goals and constraints, and ends in a documented architecture whose risks and trade-offs
  are understood.
arc42:
- 4
- 9
- 10
- 11
step: s07-solution-strategy
related:
- architectural-trade-off-thinking
- architectural-pattern
- architectural-decision-record
- software-architecture-evaluation
- iterative-and-incremental-development
- architecture-view
- quality-attribute
- requirements-versus-constraints
checks:
- The document lists the functional requirements, quality requirements and constraints that the design
  started from.
- Conflicting goals are recorded together with how the relevant stakeholders resolved them.
- Key decisions are documented, for example as ADRs.
- The architecture is described with views and broken down into parts.
- The document names risks to meeting the requirements, and the trade-offs behind them.
sources:
- url: https://www.sei.cmu.edu/library/attribute-driven-design-method-collection/
  title: Attribute-Driven Design Method Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://public.isaqb.org/curriculum-foundation/curriculum-foundation-en.html
  title: 'Curriculum forCertified Professional forSoftware Architecture (CPSA)®: Foundation Level'
  site: public.isaqb.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A design cycle: design, document, evaluate, then repeat.'
review:
  status: generated
  flags: []
---

## Explanation

Architectural thinking is how architects move from what a system must do to a design that can be built. It works in cycles, not in one pass.

**Inputs.** A well-known design method, Attribute-Driven Design (ADD), names three inputs: functional requirements (what the system does), quality attribute requirements (how well it must do it) and constraints (limits that are fixed). See the articles on Quality Attribute and Architectural Constraint.

**Resolving conflicts.** Goals often pull in different directions. Architects cannot settle this alone. They involve the relevant stakeholders, meaning the people with an interest in the system. ADD also brings quality trade-offs to light early in design.

**Applying known solutions.** Patterns are one way to reach certain qualities for a problem in a given context. The context matters, because a pattern that fits one situation may not fit another. See Architectural Pattern.

**Documenting.** Architects record their architectural decisions. The result of ADD is an architecture broken into parts and described with architectural views.

**Evaluating.** Architects check the design mainly for risks to meeting the requirements. They also name the trade-offs they made and the risks those trade-offs carry.

**Iterating.** ADD is recursive. It repeats its steps for successive parts of the system, so each round goes deeper. Iterations are needed, especially when decisions must be made under uncertainty.

## Example

A team designs an online booking system. Fast response and strict data privacy are both required, and they conflict. The architect meets the stakeholders and agrees on priorities. The team picks a structure, writes down the decision and its reasons, and checks the draft against the requirements. The check shows a risk in one part. The team then repeats the steps for that part in more detail.

## Trade-offs

Iterating is needed when decisions rest on uncertain information. Early trade-off analysis surfaces conflicts sooner. Resolving them requires involving stakeholders.
