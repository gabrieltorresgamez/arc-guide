---
title: Architecture Decision Rationale
slug: architecture-decision-rationale
category: forces-decisions
kind: practice
summary: Architecture decision rationale is the written reason behind a key design choice. It lets stakeholders
  later understand why one option won and retrace the decision.
arc42:
- 9
step: s09-decisions
related:
- architectural-decision-record
- y-statement
- arc42-architecture-decisions
- architectural-decision
- architecturally-significant-requirement
- iso-iec-ieee-42010-architecture-description-standard
- adr-common-mistakes-and-remediations
- traceability
checks:
- Each recorded decision names the chosen alternative and the criteria or requirement behind the choice.
- Each ADR covers exactly one decision together with its rationale.
- Consequences list all effects of the decision, not only the positive ones.
- Section 9 holds only important, expensive, large-scale or risky decisions.
- Justifications cite actual requirements and evidence, not pseudo-rationale or killer phrases.
sources:
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html
  title: Architectural Decisions — The Making Of
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://adr.github.io/
  title: Architectural Decision Records (ADRs) | Architectural Decision Records
  site: adr.github.io
  accessed: '2026-11-09'
- url: https://quality.arc42.org/standards/iso-42010
  title: ISO/IEC/IEEE 42010 - Architecture Description | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A design choice says what the team picked. The rationale says why. Answers to "why?" questions matter as much as any other part of a design, and a decision log can supply them.

**What counts as a decision.** arc42 defines a decision as choosing one alternative based on criteria. The ADR community adds that an architectural decision is a justified design choice that addresses an architecturally significant requirement (see Architecturally Significant Requirement).

**Where the standard stands.** The arc42 quality site summarizes ISO/IEC/IEEE 42010 as requiring that decisions and their rationale be documented (see ISO/IEC/IEEE 42010 Architecture Description Standard).

**Record format.** An Architectural Decision Record (ADR) captures exactly one decision and its rationale. arc42 says you might follow the Nygard structure, in which the consequences section lists all effects, not only the positive ones. The Y-statement is a leaner template than Zimmermann's earlier attempts (see Y-Statement).

**Which decisions to record.** Record only the key decisions, because only those justify the effort. arc42 section 9 covers decisions that are important, expensive, large-scale or risky, together with their rationales.

**Quality of the justification.** Only crisp and sound justifications convince a reader. Refer to actual requirements and evidence. Avoid pseudo-rationale and killer phrases.

## Example

A team chooses a message queue over direct calls between two services. The record states the problem: orders must not be lost when the billing service is down. It names the rejected option, direct calls, and its consequence: lost orders during outages. It states the choice and ties the reason to that requirement. It also lists the downsides of the queue, not only the benefits. Years later, a new team member asks why direct calls were not used. The record answers the question.

## Trade-offs

Writing rationale costs effort. That is why only key decisions deserve a record. A log with more than 100 entries will probably put readers to sleep and be hard to maintain, and weak justifications convince nobody. Zimmermann notes that the Y-statement is lean, while the five sections of a Nygard-style ADR can get rather long.
