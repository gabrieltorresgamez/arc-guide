---
title: Architectural Decision Record
slug: architectural-decision-record
category: forces-decisions
kind: artifact
summary: An Architectural Decision Record (ADR) is a short document that captures one design decision
  and the reasons behind it. It answers "why this design?" and helps teams avoid reopening settled decisions.
arc42:
- 9
step: s09-decisions
related:
- markdown-architectural-decision-records-madr
- y-statement
- adr-common-mistakes-and-remediations
- architectural-decision
- arc42-architecture-decisions
- architecture-decision-rationale
- middleware-architectural-decision-example
- documentation-as-code
checks:
- The ADR title conveys both the problem solved and the solution chosen.
- The ADR evaluates more than one real option, not dummy alternatives.
- The decision is traced to requirements.
- Consequences are listed as good and bad, with neutral arguments where they apply.
- The ADR is short, and architecture details sit in separate design documents.
sources:
- url: https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html
  title: The Markdown ADR (MADR) Template Explained and Distilled
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/artifact-templates/DPR-ArchitecturalDecisionRecordYForm
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/04/03/ADRCreation.html
  title: How to create Architectural Decision Records (ADRs) — and how not to
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An Architectural Decision Record (ADR) records one architectural decision. It explains why the team chose a design, so later readers see the rationale and not just the result.

**Why write ADRs.** The CALM mnemonic names four benefits: collaboration, accountability, learning and management support.

**Templates.** Several templates exist. The Markdown Architectural Decision Record (MADR) template dates from 2017. It grew out of earlier ADR templates, including the Y-statement, and follows a decision journey from identification to enforcement.

A Y-statement is a single structured sentence. It starts with "In the context of" and "facing", which add feature- and quality-related information. It continues with "to achieve" and "accepting that", which state the goal and the trade-off. An optional "because" adds the reason.

**Title.** A MADR title should convey the problem solved and the solution chosen.

**Consequences.** MADR lists consequences as "Good, because ..." and "Bad, because ...".

**Length.** Keep an ADR short. It can range from a slide-sized note to a few pages. Avoid "Mega-ADRs". Move architecture details into separate design documents.

**Common flaws.**
- Missing options: only one option is considered, or the alternatives are dummies. All neglected options should be evaluated too.
- One-sided "Fairy Tale" rationale.

## Example

A team must pick how its web shop stores sessions. Its ADR has a title naming both problem and solution. It states the requirement that drives the choice. It evaluates at least two real options. It lists consequences as good and bad. Details of the session design live in a separate design document, and the ADR links to it.

## Trade-offs

A short ADR is easy to read, but it cannot hold every detail. Keeping the details in separate design documents solves this. Evaluating all options and listing bad consequences takes effort.
