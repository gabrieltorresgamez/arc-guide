---
title: Requirement Types and Documents (Wiegers/Beatty)
slug: requirement-types-and-documents
category: functional-requirements
kind: concept
summary: 'Requirements exist at different levels: business, user and system. Business requirements go
  into a vision and scope document. The SRS holds functional and nonfunctional requirements. arc42 sections
  1, 2 and 10 reuse them.'
arc42:
- 1
- 2
- 10
step: s03-functional-requirements
related:
- use-case
- user-story
- arc42-introduction-and-goals
- arc42-constraints
- arc42-quality-chapter
- requirements-versus-constraints
- quality-attribute
- traceability
checks:
- Business requirements are recorded in a vision and scope document, separate from detailed software requirements.
- Use cases are backed by functional requirements that itemize specific software behavior.
- Arc42 section 1 lists only top quality goals and points to section 10 for the complete quality requirements.
- Arc42 section 2 lists the requirements that limit design freedom.
sources:
- url: https://www.cs.hmc.edu/~markk/SWE_copies/reqtraps.html
  title: Karl Wiegers Describes 10 Requirements Traps to Avoid
  site: cs.hmc.edu
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://rcpmag.com/articles/2003/07/01/begin-at-the-beginning.aspx
  title: Begin at the Beginning -- Redmond Channel Partner
  site: rcpmag.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Requirement levels and where each is recorded.
review:
  status: generated
  flags: []
---

## Explanation

Requirements are not all the same kind of statement. One useful way to sort them is by level.

**Business requirements** are the high-level objectives of the organization or customer who asks for the system. You can record them in a product vision and scope document.

**User requirements** are the goals or tasks that users must be able to perform with the product. Use cases capture them (see *Use Case*). Use cases alone often lack the detail developers need to know what to build.

**System requirements** are the top-level requirements for a product that contains several subsystems. They differ from the software functional requirements.

**Functional requirements** close the detail gap. They itemize the specific behaviors the software must exhibit.

**Nonfunctional requirements** cover quality attributes, business rules and similar items. The software requirements specification (SRS) is a container for both the functional and the nonfunctional requirements.

**Where this shows up in arc42**

arc42 is a template for documenting architecture (see *arc42 Architecture Documentation Template*).

- Section 1 gives a short overview of the functional requirements and driving forces. It lists only the top quality goals.
- Section 2 documents constraints. These are requirements that limit the architects' freedom of design. Teams must handle them, though some may be negotiable.
- Section 10 holds the complete set of quality requirements, including those of lesser priority. If the overview of quality requirements is already precise, specific and measurable, the quality scenarios in section 10.2 may be skipped.

## Example

A company wants its support team to handle refunds faster. That objective is a business requirement and goes into the vision and scope document. A user requirement follows: "A support agent can issue a refund." A use case captures it. Developers need more detail, so the SRS adds functional requirements, such as the specific checks the software performs before it approves a refund. A target for how quickly the screen responds is a quality requirement. It belongs in the SRS and, in full, in arc42 section 10.

## Trade-offs

Use cases alone often leave developers without enough detail, so functional requirements are still needed.
