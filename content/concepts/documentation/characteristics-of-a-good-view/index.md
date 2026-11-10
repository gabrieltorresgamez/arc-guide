---
title: Characteristics of a Good View
slug: characteristics-of-a-good-view
category: documentation
kind: concept
summary: A good view serves a named stakeholder and a clear purpose. It shows only the detail readers
  need, and it lets them check that their concerns are covered.
arc42:
- 1
- 5
- 12
step: s10-document
related:
- architecture-view
- architecture-viewpoint
- stakeholder
- stakeholder-concern
- purpose-of-views
- view-creation-method
- c4-model
- component-view-refinement-levels
checks:
- The documentation records which stakeholders were asked what information they expect.
- Each view or viewpoint names the stakeholders it serves and the concerns it addresses.
- Deeper levels of the building block view exist only where there is real demand for them.
- Each diagram has a title stating its type and scope, and it can be mostly understood without a narrative.
- Notation such as color coding is consistent within and across diagrams, and every element has a name.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/B-15/
  title: 'Question B-15: What kind of information shall I provide for which stakeholder? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/5-11/
  title: 'Tip 5-11: Show multiple levels of the building block view! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/notation
  title: Notation | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/checklist
  title: Review checklist | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A view shows how the architecture addresses the concerns of certain stakeholders. See the articles Architecture View and Stakeholder.

**Start with the reader.** Ask your own stakeholders which artifacts or information they expect from the documentation. General guidance only gives rough approximations, because the right content depends on your stakeholders. To start the conversation, show them examples of what you could deliver with low effort.

**Name the audience.** A viewpoint is a reusable set of conventions for one type of view. It also names the stakeholders that this type of view serves. So you can judge a view by asking who it is for and what it should tell them.

**Match detail to demand.** Deeper levels of a building block view cost a lot to create and maintain. Create them only where real demand for the information exists. Building blocks are refined step by step, from level 1 down to the detail that is appropriate.

**Make each diagram readable on its own.** C4 gives these tips:
- Give each diagram a title that states its type and scope.
- Make it understandable without a separate narrative.
- Use acronyms that every audience understands.
- Keep notation, such as color coding, consistent within and across diagrams.

**Review with questions.** C4 offers a checklist. It asks, for example, whether the scope is clear and whether every element has a name.

## Example

A team documents an online shop. The support manager says she needs to know which parts handle orders. The team shows her a rough one-page sketch of the main building blocks. She confirms it answers her question. The team then adds deeper detail only for the order part, where people have asked for it. Each diagram has a title with its type and scope.

## Trade-offs

Deeper detail costs effort to create and maintain, so adding it everywhere wastes time. To find the right amount of detail, ask your stakeholders. A stakeholder's needs can also differ from general guidance.
