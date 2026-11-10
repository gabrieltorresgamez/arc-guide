---
title: Consistency of User Story and Use Case
slug: consistency-of-user-story-and-use-case
category: functional-requirements
kind: practice
summary: A user story and a use case describe one goal at different levels of detail. Keep them consistent
  so they never contradict each other. Treat the story as the brief, early form.
arc42:
- 3
- 5
- 6
step: s03-functional-requirements
related:
- user-story
- use-case
- user-story-vs-use-case
- use-case-template
- use-case-goal-levels
- acceptance-criteria
- card-conversation-confirmation
- traceability
checks:
- Each story's role matches the primary actor of its use case.
- Story benefits state business impact and are not written as formal postconditions.
- Use cases carry a goal level, aimed at user goal or subfunction for API and service design.
- Use cases list preconditions and postconditions that do not contradict the story's acceptance criteria.
sources:
- url: https://socadk.github.io/design-practice-repository/artifact-templates/DPR-UseCase.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/artifact-templates/DPR-UserStory.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/user-stories
  title: 'User Stories: What They Are, How to Write Them, and Examples - Mountain Goat Software'
  site: mountaingoatsoftware.com
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

A user story is a short statement of a need. A common template names a role, a feature, and a benefit. The role is who wants it. The feature is what they want. The benefit is why. Acceptance criteria go with the story. They help the team judge whether the story was completed correctly. A story can also be read in three parts: a brief card, a conversation that builds understanding, and a confirmation that tells the team when the story is complete (see the article Card, Conversation, Confirmation).

A use case can carry a goal level, which tells readers how detailed it is. For API and service design, aim at the user goal or subfunction level. The primary actor is the user from whose perspective the use case is written, and who starts it. Templates also list preconditions, which say what must hold before the use case can run. Postconditions describe what changes in the system afterward (see Use Case Template and Use Case Goal Level).

**How the parts differ**

- A story's benefit should not be confused with an outcome. A benefit states business impact. It should not formally specify a postcondition.
- The Design Practice Repository points to Given-When-Then, from behavior-driven development, as a template for acceptance criteria.

Stories and use cases have no simple one-to-one mapping.

**How they work together**

Stories can be seen as a preliminary stage to use cases, but they are not a direct alternative. You can derive use cases from early stories. Keep use cases short and readable. They should not take weeks of upfront documentation before development starts.

## Example

A story reads: "As a customer, I can cancel an order, so that I avoid paying for goods I no longer want." Its criteria say what counts as done.

A matching use case could name the customer as primary actor. Its precondition says the order exists. Its postcondition says the order is marked canceled.


