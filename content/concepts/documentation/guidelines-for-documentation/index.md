---
title: Guidelines for Documentation
slug: guidelines-for-documentation
category: documentation
kind: principle
summary: Write only what readers will use. Match detail to their needs, describe each thing once and reference
  it elsewhere, and keep the text short so people actually read it.
arc42:
- 1
- 5
- 8
- 9
step: s10-document
related:
- arc42-documentation-template
- arc42-crosscutting-concepts
- documentation-as-code
- motivation-for-architecture-documentation
- stakeholder-identification
- architecture-decision-rationale
- undetected-duplication-antipattern
- software-architecture-documentation-consensus
checks:
- Each section of the document was included because a named stakeholder needs it, not just because the
  template has it.
- Each interface is described in detail in one place, and other places only reference it.
- The document is short and focused on important or risky topics.
- Important decisions are recorded with their motivation and reasoning.
- A named person is responsible for the amount and quality of the documentation.
sources:
- url: https://faq.arc42.org/questions/B-1/
  title: 'Question B-1: Which parts of arc42 are essential, which are optional? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/E-3/
  title: 'Question E-3: How can arc42 help us in reducing documentation effort? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-5-10/
  title: 'Question C-5-10: How can I avoid redundancy with interfaces in the building block view? | arc42
    FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://agilemodeling.com/essays/agileDocumentationBestPractices.htm
  title: Core Practices for Lean/Agile Documentation
  site: agilemodeling.com
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/B-16/
  title: 'Question B-16: What does ''economical'' documentation mean? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/8-1/
  title: 'Tip 8-1: Explain the Concepts! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/H-3/
  title: 'Question H-3: How can I keep architecture documentation in sync with source code? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Documentation exists to serve its readers. These rules of thumb help you decide what to write and what to leave out.

**Write only what will be read.** If nobody will read something, do not write it. arc42 (see "arc42 Architecture Documentation Template") says the same: write down only facts and reasons that you or your stakeholders find important enough to justify it. Do not fill in every section just because it exists.

**Ask your readers.** Set the level of detail by what readers need, not by what the writer knows. arc42 advises asking stakeholders one by one what they need. Ambler's agile documentation principle agrees: focus on the actual consumers of the document. Ideally, a document is just barely sufficient for its situation.

**Keep it short.** arc42 says less is often more. Shorter documentation is read and digested faster, and it needs fewer changes later. Prioritize important, special or risky topics over completeness. Shortness has a limit, though: the text should not become cryptic. Decide deliberately how much to document.

**Say each thing once.** Describe an interface in full once, at the level where it is handled. Everywhere else, add a reference to that description. Crosscutting concepts work the same way. A crosscutting concept is a decision that several building blocks share (see "Crosscutting Concept"). Documenting it once saves effort and avoids repeating the decision in every block.

**Prefer decisions over obvious detail.** Document a few important, architecturally relevant decisions with their motivation and reasoning. Stakeholders should be able to retrace them. arc42 also prefers crosscutting concepts to many detailed building-block diagrams, because developers can learn those details from the code.

**Keep it current.** arc42 suggests appointing a person responsible for the amount and quality of the documentation. It also suggests waiting to document volatile parts until they stabilize.

## Example

A team plans a document for a small web shop. They ask the support lead and the developers what they need. Support wants a one-page overview of how the shop connects to the payment provider. Developers want to know why the team chose that provider.

The team writes the payment interface in detail in one place, next to the component that handles it. The overview page only points to that description. They add a short decision note with the reasons. They skip a detailed diagram of internal components, since the code shows it. They also name one person who owns the document.

## Trade-offs

Short documentation is read faster and needs fewer changes, but it can become cryptic. Teams must decide deliberately how much to write. Referencing instead of copying avoids redundancy. Leaving out detail also means some readers may have to look elsewhere, for example in the code.
