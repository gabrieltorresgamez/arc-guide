---
title: Architecture Challenges at Project Start
slug: architecture-challenges-at-project-start
category: forces-decisions
kind: concept
summary: At project start, architects must make basic decisions with little certainty. Requirements change,
  constraints limit freedom, and early choices may prove wrong. Good timing and recorded decisions help
  teams correct course.
arc42:
- 2
- 9
step: s05-constraints
related:
- last-responsible-moment
- requirements-versus-constraints
- architectural-decision-record
- arc42-constraints
- architectural-forces
- architecturally-significant-requirement
- solution-as-moving-target
- architectural-decision
checks:
- Constraints are listed, and the document notes which ones may be negotiable and which apply organization-wide.
- Essential architectural decisions are recorded, for example as ADRs, using one consistent template.
- The document states that early decisions may be revisited and corrected.
sources:
- url: https://martinfowler.com/articles/designDead.html
  title: Is Design Dead?
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html
  title: Architectural Decisions — The Making Of
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Several challenges appear together.

**Requirements are unclear and keep changing.** One well-known author calls changing requirements the biggest cause of trouble in the software projects they meet. Such changes hurt planned design, which led the author to look for a new direction.

**Even "clear" requirements can be wrong.** A team may feel sure how a function works and still build it incorrectly. However certain a team is, it can still be wrong, especially without detailed requirements.

**Constraints limit freedom.** A constraint is a fixed condition the architect must respect (see Architectural Constraint). Constraints must always be dealt with, but some can be negotiated. They sometimes reach beyond one system and apply to a whole organization.

**Early decisions may be wrong.** Teams know they may err in early architectural decisions. These decisions are not set in stone, and teams need the courage to fix them.

**Timing matters.** Teams want to decide at the most responsible moment (see Last Responsible Moment). Even very agile teams capture the essential decisions somehow, for example as Architectural Decision Records, or ADRs (see Architectural Decision Record).

## Example

A team starts building an online booking tool. The business says bookings must be "fast" but does not say what that means. Later the customer changes the booking rules. The company also requires one specific database for all systems. The team asks whether that rule is negotiable. It makes its main choices, writes them down in short decision records, and stays ready to revise them as it learns more.

## Trade-offs

Recording decisions costs effort. The advice is to pick one ADR template and stick to it. Do not document everything, only the essential decisions. Staying open to revision also requires the courage to fix early decisions.
