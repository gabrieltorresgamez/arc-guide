---
title: Architectural Decision Records as Evaluation Prerequisite
slug: architectural-decision-records-as-evaluation-prerequisite
category: evaluation
kind: practice
summary: Writing down key architectural decisions, with the reasons for each choice, gives an evaluation
  something concrete to check against the quality goals. Reviewers can then see which decisions support
  which goals.
arc42:
- 9
- 10
- 11
step: s11-evaluate
related:
- architectural-decision-record
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- markdown-architectural-decision-records-madr
- y-statement
- arc42-architecture-decisions
- software-architecture-evaluation
- quality-attribute-scenario
checks:
- Important, expensive, large-scale or risky decisions are documented with their rationales.
- Each recorded decision names the chosen alternative and the criteria used to select it.
- Each record lists all consequences, including negative ones.
- Each decision links to the quality scenario it supports.
sources:
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://adr.github.io/madr/
  title: About MADR | MADR
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

An architectural decision means choosing one alternative from several, based on given criteria. Important, expensive, large-scale or risky decisions should be documented together with their rationales. Stakeholders must be able to comprehend and retrace them.

**What a record holds**

Lightweight formats exist. A Nygard-style record has a Context section. It describes the forces at play: technical, political, social and project aspects. Its Consequences section should list all consequences, not only the positive ones.

MADR is another format. Its Decision Outcome names the chosen option and gives a justification. Its optional consequences list good and bad effects of the decision. See the articles on Markdown Architectural Decision Records and Y-Statement.

**Why evaluation needs them**

An evaluation asks whether the architecture supports the quality goals. The Architecture Tradeoff Analysis Method (ATAM) works this way. It turns business drivers into scenarios. It then lists the architectural decisions made in support of each scenario. Analyzing those decisions yields risks, non-risks, sensitivity points and trade-off points. The article on ATAM findings explains these terms.

**Proportionality**

Record only significant decisions: those that matter and are hard and costly to change. 

**Finding risks early**

ATAM exposes architectural risks that could keep an organization from reaching its business goals. The SEI lists identifying such risks early in the life cycle as a benefit.

## Example

A team must pick how a web shop stores orders. One quality scenario says the shop must stay usable during a database failure. The team records two alternatives, the chosen one, and the criteria used. The consequences list a cost as well as a benefit. A reviewer reads the record. They check whether the chosen option supports the scenario. They also note where the choice carries a risk.

## Trade-offs

Recording decisions takes time, so record only the significant ones. A record should list all consequences, not just the positive ones.
