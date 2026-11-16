---
title: arc42 Risks and Technical Debt
slug: arc42-risks-and-technical-debt
order: 120
category: documentation
kind: artifact
summary: Chapter 11 of arc42 is a list of identified technical risks and technical debt, ordered by priority, with measures to reduce them.
arc42:
- 11
step: s11-evaluate
related:
- technical-debt
- placing-atam-evaluation-in-arc42
- architecture-tradeoff-analysis-method-atam
- arc42-documentation-template
- arc42-quality-chapter
- risk-storming
checks:
- Technical risks and technical debt are listed in one place, ordered by priority.
- Entries suggest measures to minimize, mitigate or avoid a risk, or to reduce the debt.
- Risks were searched for with different stakeholders, not only by the architects.
sources:
- url: https://docs.arc42.org/section-11/
  title: "11 - Risks and technical debt | arc42 Documentation"
  site: docs.arc42.org
  accessed: '2026-11-16'
- url: https://docs.arc42.org/tips/11-1/
  title: "Tip 11-1: Search for problems and risks with different stakeholders! | arc42 Documentation"
  site: docs.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Chapter 11 of arc42 is a list of identified technical risks or technical debts, ordered by priority. It is where the architecture documentation records the identified technical risks and technical debt.

**Why it exists.** Management stakeholders, for example project managers and product owners, need this list as part of the overall risk analysis and measurement planning. arc42 asks for systematic detection and evaluation of risks and technical debt in the architecture.

**Form.** A list or table of risks and technical debts, probably with suggested measures to minimize, mitigate or avoid the risks, or to reduce the debts.

**How to find entries.** arc42 gives tips for searching:

- ask different stakeholders about problems and risks
- analyze external interfaces
- identify problems and risks by qualitative evaluation, for example with ATAM
- analyze processes
- analyze data and data structures
- analyze the source code


## Example

A web shop lists three entries in priority order. The payment provider has no fallback, which is a risk, and the measure is a second provider or a queue. The order service has no automated tests, which is technical debt, and the measure is to add tests before the next release. The search feature relies on a library that is no longer maintained, which is a risk, and the measure is to plan its replacement.

## Trade-offs

The list is ordered by priority, and each entry can suggest a measure to deal with it.
