---
title: User Story Role Formulation
slug: user-story-role-formulation
category: functional-requirements
kind: practice
summary: A user story names a specific user role, what that role wants, and why. The "so that" part states
  the benefit and helps the team judge how much the story matters.
arc42:
- 1
step: s03-functional-requirements
related:
- user-story
- card-conversation-confirmation
- acceptance-criteria
- user-story-vs-use-case
- invest-criteria
- story-splitting
- epic
- story-mapping
checks:
- Stories name a specific user role instead of starting generically with 'As a user'.
- Each story states a reason or benefit, or the team has chosen on purpose to omit it.
- Each story has acceptance criteria that show how the team will know it is complete.
- Purely technical work is kept as technical backlog items, not forced into story form.
sources:
- url: https://www.mountaingoatsoftware.com/agile/user-stories/writing-user-stories
  title: 'Writing User Stories: Template, Examples, and Practical Advice - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/why-the-three-part-user-story-template-works-so-well
  title: 'User Story Template: What It Is and Why It Works So Well - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/user-stories
  title: 'User Stories: What They Are, How to Write Them, and Examples - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A user story is a short statement of something a user needs from a system. A common template gives it a three-part shape: a role, a need or want, and a reason or benefit. The template is a thinking aid, not a required formula. In template form: "As a [role], I want [function], so that [benefit]."

**Where it comes from.** This template started with an agile coach at a UK company called Connextra in the early 2000s.

**The role.** The first part names who wants the function. Teams often fall into starting every story with "As a user". That generic label tells the team little. Name the real kind of person who will use the feature instead.

**The function.** The middle part says what the role needs or wants to do.

**The "so that" clause.** The last part gives the reason or benefit. It is often the most valuable part of the story. It shows the decision behind the request. That reason can change the design, the priority and the scope of the work. It is described as the most important part of a story, yet it should not be mandatory.

**Confirming the story.** Confirmation, expressed as acceptance criteria, tells the team how to know a story is complete. See the articles Card, Conversation, Confirmation and Acceptance Criterion.

**Not everything is a story.** Some technical work is clearer as a plain technical backlog item. Do not force it into the template.

## Example

A team building a recipe website might write:

*As a home cook, I want to filter recipes by cooking time, so that I can find a meal that fits the time I have tonight.*

The role is a home cook, not "a user". The reason shows that speed matters. That could affect how prominent the filter is and how many filters the team builds first.

A task such as upgrading a database version would stay a technical backlog item. It does not need a role.

## Trade-offs

Writers may fill the "so that" clause with superfluous text just to comply with the template. Cohn says it should not be mandatory, so teams can leave it out when the reason is obvious. The template also does not fit all work. Forcing technical tasks into it makes them less clear.
