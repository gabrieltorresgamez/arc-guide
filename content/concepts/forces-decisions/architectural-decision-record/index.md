---
title: Architectural Decision Record
slug: architectural-decision-record
order: 10
category: forces-decisions
kind: artifact
summary: An Architectural Decision Record (ADR) is a short document that captures one design decision
  and the reasons behind it. It answers "why this design?" and helps teams avoid reopening settled decisions.
arc42:
- 9
step: s09-decisions
related:
- architectural-decision
- arc42-architecture-decisions
- architecture-decision-rationale
- architectural-decision-record-example
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
- url: https://adr.github.io/madr/
  title: About MADR | MADR
  site: adr.github.io
  accessed: '2026-11-09'
- url: https://adr.github.io/
  title: Architectural Decision Records (ADRs) | Architectural Decision Records
  site: adr.github.io
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
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
- url: https://ozimmer.ch/practices/2026/09/12/ADRMistakes.html
  title: Ten Common Mistakes in Architectural Decision Records (ADRs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/04/05/ADRReview.html
  title: How to review Architectural Decision Records (ADRs) — and how not to
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://www.equalexperts.com/blog/ai/accelerating-architectural-decision-records-adrs-with-generative-ai/
  title: Accelerating Architectural Decision Records (ADRs) with Generative AI | Equal Experts
  site: equalexperts.com
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2604.03826
  title: 'Context Matters: Evaluating Context Strategies for Automated ADR Generation Using LLMs'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://handsonarchitects.com/blog/2025/using-generative-ai-as-architect-buddy-for-adrs/
  title: Using Generative AI to Help Write ADRs | Hands-on Architects
  site: handsonarchitects.com
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2504.20781v3
  title: Using LLMs in Generating Design Rationale for Software Architecture Decisions
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
  title: "Documenting Architecture Decisions (Michael Nygard)"
  site: cognitect.com
  accessed: '2026-11-16'
- url: https://raw.githubusercontent.com/adr/madr/main/template/adr-template-minimal.md
  title: "MADR minimal template"
  site: raw.githubusercontent.com
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An Architectural Decision Record (ADR) records one architectural decision. It explains why the team chose a design, so later readers see the rationale and not just the result.

**Why write ADRs.** The CALM mnemonic names four benefits: collaboration, accountability, learning and management support.

**Templates.** Several templates exist. The Markdown Architectural Decision Record (MADR) template dates from 2017 [src:1]. It grew out of earlier ADR templates, including the Y-statement, and follows a decision journey from identification to enforcement.

A Y-statement is a single structured sentence. It starts with "In the context of" and "facing", which add feature- and quality-related information. It continues with "we decided for" the chosen option, "and neglected" the options that were not chosen, then "to achieve" and "accepting that", which state the goal and the trade-off. An optional "because" adds the reason.

**Origin and structure.** Michael Nygard proposed ADRs in 2011 for agile projects [src:16]. His record has a title and four parts: context, decision, status and consequences. The decision is written in full sentences and active voice ("We will ..."). The consequences list all effects, not only the positive ones. The whole record should be one or two pages long.

**Status.** A decision is "proposed" while the stakeholders have not agreed with it, and "accepted" once they have. If a later ADR changes or reverses it, the old record is marked "deprecated" or "superseded", with a reference to its replacement. MADR's full template also has a status field, whose values include proposed, rejected, accepted, deprecated and superseded.

**A MADR skeleton.** The minimal MADR template has these parts:

```markdown
# {short title, representative of solved problem and found solution}
## Context and Problem Statement
## Considered Options
## Decision Outcome
### Consequences
```

The "Decision Outcome" names the chosen option with its justification, and "Consequences" records its effects.

**Title.** A MADR title should convey the problem solved and the solution chosen.

**Consequences.** MADR lists consequences as "Good, because ..." and "Bad, because ..." [src:4].

**Length.** Keep an ADR short. It can range from a slide-sized note to a few pages. Avoid "Mega-ADRs". Move architecture details into separate design documents.

**Common flaws.**
- Missing options: only one option is considered, or the alternatives are dummies. All neglected options should be evaluated too.
- One-sided "Fairy Tale" rationale.

**More about decision record formats and quality.**

- **Markdown Architectural Decision Records:** MADR is a short Markdown template for recording architecturally significant decisions in a structured way. Each decision is one file in docs/decisions. Full, minimal, and bare versions exist.
- **Y-Statement:** A Y-Statement records one architectural decision in a single sentence. It names the context, the concern, the chosen option, the rejected options, the quality gained and the downside accepted [src:7].
- **ADR Common Mistakes and Review Checklist:** Weak decision records often hide their criteria, skip alternatives, give no real "why," or leave out downsides. A short review checklist helps catch these gaps before the record is accepted.
- **GenAI Support for Architectural Decision Records:** Teams use generative AI to draft architectural decision records (ADRs) quickly and to explore options. The output can be wrong or invented, so humans must check every ADR before it enters the record.

## Example

A team must pick how its web shop stores sessions. Its ADR has a title naming both problem and solution. It states the requirement that drives the choice. It evaluates at least two real options. It lists consequences as good and bad. Details of the session design live in a separate design document, and the ADR links to it.

## Trade-offs

A short ADR is easy to read, but it cannot hold every detail. Keeping the details in separate design documents solves this.
