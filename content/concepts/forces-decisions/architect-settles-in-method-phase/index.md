---
title: Architect Settles In Method Phase
slug: architect-settles-in-method-phase
category: forces-decisions
kind: method
summary: A new architect first learns who is involved, which forces and constraints apply, and how decisions
  will be managed. Early results are refined over time.
arc42:
- 1
- 2
- 3
step: s01-goals-stakeholders
related:
- stakeholder-identification
- architectural-forces
- requirements-versus-constraints
- arc42-introduction-and-goals
- arc42-constraints
- architectural-decision-management-practices
- architecture-challenges-at-project-start
- stakeholder
checks:
- The document lists the parties involved in or affected by the system.
- Existing requirements documents are referenced rather than duplicated.
- Constraints are identified, and it is stated which are negotiable.
- Organization-wide constraints are captured separately from system-specific ones.
sources:
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

**Reviewing what exists.** Requirements documents may already exist. The architect refers to them instead of copying them into new documents.

**Casting the stakeholder net widely.** A stakeholder is anyone involved in building the system or affected by it. The architect should know all of them. Missing someone can cause nasty surprises late in development. Stakeholders also decide how much detail the architect's work and results need. So the stakeholder net shapes the work itself.

**Understanding forces and constraints.** Forces are the requirements and driving factors that the architect and development team must consider. Constraints limit design freedom. The architect needs to know where freedom ends and constraints begin. Constraints must always be dealt with, but some can be negotiated. Some come from the wider organization, not from one system alone.

## Example

A new architect joins a project that is already running late. They read the existing requirements document and refer to it rather than rewriting it. They list everyone who builds, runs or uses the system. Later they find a team in the wider organization that sets rules for all systems. They add that team to the net and record the rules as constraints. They also check which rules can be negotiated.

## Trade-offs

Missing a stakeholder can cause nasty surprises late in development. Constraints must always be dealt with, but they may be negotiable.
