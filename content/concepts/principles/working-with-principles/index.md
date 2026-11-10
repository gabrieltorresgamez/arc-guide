---
title: Working with Principles
slug: working-with-principles
category: principles
kind: method
summary: Working with principles means writing short rules that tie design decisions to requirements.
  A good principle has a name, a statement, a rationale and implications. Teams may break one only for
  a justified reason.
arc42:
- 4
- 8
- 9
step: s09-decisions
related:
- architecture-principle
- structure-of-an-architecture-principle
- conflicting-architecture-principles
- relationships-between-architecture-principles
- architectural-decision-record
- traceability
- togaf
- arc42-architecture-decisions
checks:
- Each principle can be traced to a requirement it supports.
- Each principle has a memorable name and a brief, direct statement.
- Each principle gives a rationale in business terms.
- Each principle lists implications for business and IT.
- Every case where a principle was broken has a justification.
sources:
- url: https://www.infoq.com/articles/architectural-design-principles/
  title: Harnessing the Power of Architectural Design Principles - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
- url: https://cio-wiki.org/wiki/Architectural_Principles
  title: Architectural Principles - CIO Wiki
  site: cio-wiki.org
  accessed: '2026-11-09'
- url: https://docs.sunnycalc.griesser.com/architecture/05-principles-and-guidelines/
  title: Principles and Guidelines | Sunny Calculator Add-On
  site: docs.sunnycalc.griesser.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A principle links requirements to design decisions and guidelines.
review:
  status: generated
  flags: []
---

## Explanation

An architecture principle is a rule that guides design decisions. Its purpose is to link those decisions to requirements. It makes sure some part of a design choice meets some part of the requirements.

Principles also help people decide consistently. They clarify priorities and constraints, helping people make consistent, informed decisions. For background, see the article *Architecture Principle*.

**How to write one**

One format, used by TOGAF, has four parts:

- **Name:** It captures the essence of the rule and is easy to remember.
- **Description:** It succinctly and directly conveys the fundamental rule.
- **Rationale:** It gives the benefits of following the rule, in business terms.
- **Implications:** They list what the business and IT must do to comply.

The article *Architecture Principle Structure* covers this template in more detail.

**Principles as developer guidelines**

One example repository pairs developer guidelines with motivation and architectural significance. It also uses Architectural Decision Records (ADRs). One guideline there says to use ADRs to document significant choices and their rationale.

**Breaking a principle**

Teams will occasionally break a principle. That is allowed. The reason must be justifiable.

## Example

A shop has a requirement that customers can order at any hour. The team writes a principle named "Keep ordering available". The description is one sentence. The rationale says lost orders mean lost revenue. Later, one team wants to skip the rule for a small internal tool. They write down why, so the exception can be reviewed.

## Trade-offs

Principles help people make consistent decisions, but they are hard to define well. Principles that are long on philosophy and short on actionable specifics are hard to apply. Broken principles can also give useful information about the design, and a principle that is routinely and justifiably broken signals a mismatch between assumptions and reality.
