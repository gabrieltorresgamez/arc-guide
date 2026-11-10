---
title: Use Case Template
slug: use-case-template
category: functional-requirements
kind: artifact
summary: A use case template is a fixed form for writing a use case as text. Every use case gets the same
  fields, so readers can compare and review them. Teams can use a full or a short version.
arc42:
- 1
- 3
step: s03-functional-requirements
related:
- use-case
- use-case-goal-levels
- use-case-completeness-check
- use-case-diagram
- user-story-vs-use-case
- use-case-goal-hierarchy-with-include-relationships
- method-phase-working-with-functional-requirements
- quality-attributes-in-use-case-descriptions
checks:
- Each use case names a primary actor, a trigger and the preconditions that must hold before it starts.
- The main success scenario is a numbered list of simple actor-system interaction steps.
- Extensions cover error handling and special cases, each as a condition that leads to different interactions.
- Each use case states its design scope and goal level.
- Postconditions or guarantees state what changes in the system after the use case runs.
sources:
- url: https://en.wikipedia.org/wiki/Use_case
  title: Use case - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/artifact-templates/DPR-UseCase.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://www.martinfowler.com/bliki/IncludeAndExtend.html
  title: Include And Extend
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UseCase.html
  title: Use Case
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A use case describes how a user reaches a goal with a system (see the article Use Case). A use case template is the form you fill in to write one down. The text carries the value. One source notes that the value of use cases lies in the text, which UML does not standardize.

Most templates are variations of Cockburn's fully dressed template. His book *Writing Effective Use Cases* is the standard reference.

**Fields of the fully dressed form**

- **Precondition:** what must hold before the use case can run.
- **Trigger:** what starts it.
- **Primary actor:** the user from whose perspective the use case is written and started.
- **Scope:** how much of the system the use case covers. It ranges from a whole organization seen as a black box down to a single component.
- **Goal level:** how detailed the use case is. For API and service design, aim for user goal or subfunction level (see Use Case Goal Level).
- **Main success scenario:** a numbered list of steps. Each step is a simple statement of an interaction between actor and system.
- **Extensions:** conditions that lead to different interactions than the main scenario. They cover error handling and special cases.
- **Guarantees:** minimal and success guarantees. Postconditions state what changes in the system afterwards.
- **Stakeholders and interests:** who cares about the outcome and why.

**Casual version**

The casual format is lighter. The body is a paragraph or two of informal text that describes what happens. The fully dressed form can also be simplified when less detail is needed.

**Relations between use cases**

Fowler advises using include when steps repeat across use cases or form their own chunk. He advises ignoring extend.

## Example

A shop writes a use case called "Place order".

- Primary actor: customer.
- Precondition: the customer is signed in.
- Trigger: the customer presses "Checkout".
- Main success scenario:
  1. The customer reviews the cart.
  2. The customer enters payment details.
  3. The system confirms the order.
- Extension 2a: the payment is declined. The system asks for another payment method.
- Guarantees: the order is stored only if payment succeeded.

The extension number ties to step 2 of the main scenario. A casual version would describe the same story in one short paragraph.

## Trade-offs

The casual form has fewer fields than the fully dressed form: title, primary actor, scope, level and a short story. Choose the level of detail that your readers need. The template can be simplified when less detail is enough.
