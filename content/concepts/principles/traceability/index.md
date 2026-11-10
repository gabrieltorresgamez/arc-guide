---
title: Traceability
slug: traceability
category: principles
kind: principle
summary: Traceability links requirements to the architecture that serves them. arc42 describes a full
  form, where every requirement is referenced, and a pragmatic form, where key decisions are explained
  by their requirements. It advises avoiding the full form when possible.
arc42:
- 5
- 9
step: s10-document
related:
- arc42-documentation-template
- arc42-architecture-decisions
- decision-documentation-and-requirements-management
- architectural-decision
- smart-requirements
- modifiability
- accountability
- architecturally-evident-coding-style
checks:
- The documentation states whether traceability is full-scale or pragmatic.
- Important architecture decisions name the requirements behind them.
- The fulfilled-requirements field of a building block is filled only where traceability is truly needed.
sources:
- url: https://faq.arc42.org/questions/H-1/
  title: 'Question H-1: What does ''traceability'' mean (with arc42)? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/H-2/
  title: 'Question H-2: Shall we strive for traceability in our documentation? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/5-7/
  title: 'Tip 5-7: Use tables to efficiently document/specify blackboxes! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Traceability means you can link a requirement back to the rationale of its stakeholders and forward to the design artifacts, code and test cases that deal with it.

arc42 (a template for documenting architecture, see the article arc42 Architecture Documentation Template) describes two forms.

**Full-scale traceability.** Every single requirement is referenced somewhere in the architecture or solution documentation. No requirement is left without a link.

**Pragmatic traceability.** You explain the important or fundamental decisions by naming the requirements behind them. This helps readers understand why the architecture looks the way it does.

The arc42 building block template supports linking too. Its blackbox template has an optional field for the requirements that the block fulfills. That field lists the requirements the block fulfills or satisfies.

arc42 attaches a warning to this field. Add fulfilled requirements only if you really need traceability, because the effort is large.

## Example

A team builds an online shop. One requirement says customers can pay by invoice. In the description of the payment building block, the team fills the optional field with this requirement. The team also records the decision to use an external payment provider and names the requirement behind it. A new team member can now see why the provider exists. The team does not link minor requirements, such as button labels. This follows the pragmatic form.

## Trade-offs

The arc42 FAQ calls traceability in general horribly expensive, slow and difficult, and advises avoiding it when you can. Fill the optional requirements field only where you truly need the links.
