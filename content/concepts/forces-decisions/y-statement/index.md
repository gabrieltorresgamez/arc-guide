---
title: Y-Statement
slug: y-statement
category: forces-decisions
kind: artifact
summary: A Y-Statement records one architectural decision in a single sentence. It names the context,
  the concern, the chosen option, the rejected options, the quality gained and the downside accepted.
arc42:
- 9
step: s09-decisions
related:
- architectural-decision-record
- arc42-architecture-decisions
- markdown-architectural-decision-records-madr
- architectural-decision
- architecture-decision-rationale
- architectural-trade-off-thinking
- middleware-architectural-decision-example
- adr-common-mistakes-and-remediations
checks:
- Each decision statement names its context, concern, chosen option, neglected options, desired qualities
  and accepted downside.
- The downside clause ('accepting that...') states a concrete cost, not a generic remark.
- The decision is written as one sentence, kept lean.
sources:
- url: https://www.ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html
  title: Architectural Decisions — The Making Of
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://adr.github.io/adr-templates/
  title: ADR Templates | Architectural Decision Records
  site: adr.github.io
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/artifact-templates/DPR-ArchitecturalDecisionRecordYForm.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The six parts of a Y-Statement, read left to right as one sentence.
review:
  status: generated
  flags: []
---

## Explanation

A Y-Statement is a short template for writing down a decision about a system's design. Its six sections together form one (rather long) sentence. The letter Y sounds like "why", which explains the name.

The long form reads like this:

- **In the context of** a use case or user story,
- **facing** a concern,
- **we decided for** an option **and neglected** other options,
- **to achieve** the desired qualities or consequences,
- **accepting** the downside or undesired consequences.

An optional "because" clause can add further rationale.

The first half says what the situation was and what the team chose. The second half says what the choice buys and what it costs. The downside clause makes the trade-off visible. Readers see the price of the decision, not only its benefits.

**Where it comes from.** Olaf Zimmermann first suggested the WH(Y) template for decision records in a SATURN 2012 presentation. George Fairbanks's Architecture Haikus inspired it. Projects at ABB have used it, and it has been taught at HSR/OST since 2013. Zimmermann also contributed to ADMentor, an add-in for Enterprise Architect, as joint work with Heiko Koziolek and Thomas Goldschmidt from ABB.

**Compared with other formats.** Nygard's decision records and the arc42 tip each have five sections. Those sections can get rather long. The Y-Statement is the leaner form.

**Tool support.** ADMentor, an add-in for Enterprise Architect, offers a Y-Statement template for its solution space models and diagrams.

## Example

A team builds a web shop. Their statement might read:

In the context of the checkout flow, facing the need to keep each request independent of one server, we decided for keeping session data in a separate session database and neglected storing it on the web servers, to achieve flexible request handling, accepting that the session database must be designed, implemented, and replicated.

The last clause names the cost openly. A later reader can judge whether that cost is still acceptable.

## Trade-offs

The one-sentence form is lean, but it leaves little room. The optional "because" clause can hold extra rationale that does not fit the trade-off format. Formats with more sections (Nygard's, the arc42 tip) give more space, but their sections can grow long.
