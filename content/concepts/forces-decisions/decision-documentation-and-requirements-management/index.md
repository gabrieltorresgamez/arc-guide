---
title: Architecture Decision Documentation and Requirements Management
slug: decision-documentation-and-requirements-management
category: forces-decisions
kind: practice
summary: Architects write down important decisions with their context, reasons and consequences. That
  lets stakeholders retrace why the system looks the way it does, and see where constraints limited the
  choices.
arc42:
- 2
- 9
step: s09-decisions
related:
- architectural-decision-record
- arc42-architecture-decisions
- architecture-decision-rationale
- requirements-versus-constraints
- y-statement
- markdown-architectural-decision-records-madr
- adr-common-mistakes-and-remediations
- architectural-decision
checks:
- Each important decision is documented with its motivation and reasoning.
- Each decision lists all consequences, including negative ones.
- The context of a decision covers technical, political, social and project aspects.
- Rationale cites actual requirements or evidence, not killer phrases.
- The document shows where constraints bind the design and where the architect is free.
sources:
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://adr.github.io/
  title: Architectural Decision Records (ADRs) | Architectural Decision Records
  site: adr.github.io
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html
  title: Architectural Decisions — The Making Of
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An architectural decision is a choice that shapes the system. Teams record the important ones so others can follow them later. Stakeholders (people with an interest in the system) should be able to understand and retrace the decisions. So each record states the motivation and the reasoning, not only the outcome.

**Know where you are free.** Before deciding, an architect needs to know where design is free and where constraints bind. A constraint may be negotiable, but the team must still deal with it. See the article Architectural Constraint.

**One record per decision.** An Architectural Decision Record (ADR) captures a single decision and its rationale. All ADRs of a project together form its decision log. A 2011 blog post titled "Documenting Architecture Decisions" popularized the idea.

**What to write down.**
- **Context.** Describe the situation. It covers technical, political, social and project aspects, not only technology.
- **Rationale.** Answers to "why" questions matter as much as the rest of the design. Keep the justification short and solid.
- **Evidence.** Point to actual requirements and evidence. Avoid pseudo rationale and killer phrases.
- **Consequences.** List all of them, including the negative ones.

## Example

A team picks a managed database service for a small web shop. The record describes the context: a short deadline, a team with little operations experience, and a budget set by management. It states the decision and the reason, which is a requirement to launch within three months. It lists the consequences. The good one is less operations work. The bad one is a stronger tie to one vendor. Later, a new team member reads the record and sees why the choice was made.

## Trade-offs

Listing all consequences, including the negative ones, gives readers the full picture.
