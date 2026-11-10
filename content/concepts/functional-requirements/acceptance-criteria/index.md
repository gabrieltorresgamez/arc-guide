---
title: Acceptance Criterion
slug: acceptance-criteria
category: functional-requirements
kind: concept
summary: An acceptance criterion is a condition a user story must meet before the product owner accepts
  it as complete. Each criterion belongs to one story, and clear ones can feed test cases.
arc42:
- 1
- 10
step: s03-functional-requirements
related:
- user-story
- card-conversation-confirmation
- invest-criteria
- frequent-mistakes-in-defining-acceptance-criteria
- story-splitting
- method-phase-working-with-functional-requirements
- testability
- epic
checks:
- Each user story lists its own acceptance criteria, separate from the team-wide Definition of Done.
- The product owner supplied or confirmed the high-level criteria for each story.
- Criteria can be turned into detailed test cases.
sources:
- url: https://www.mountaingoatsoftware.com/agile/clarifying-the-relationship-between-definition-of-done-and-conditions-of-sa
  title: Relationship between Definition of Done and Conditions of Satisfaction - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/the-two-ways-to-add-detail-to-user-stories
  title: The Two Ways to Add Detail to User Stories - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/GivenWhenThen.html
  title: Given When Then
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Acceptance criteria say when a user story counts as complete and accepted. Some people use the term "conditions of satisfaction" for nearly the same thing.

**Story-level, not team-wide.** Criteria belong to one backlog item. The Definition of Done is different. It is an agreed list of things that must be true before any item counts as complete. The developers create that list. The product owner supplies the high-level criteria for a single story.

**Where they lead.** Quality assurance (QA) can turn the product owner's high-level criteria into more detailed test cases. This is how criteria feed testing.

**When they appear.** Detail, including criteria, is added as a story moves toward the top of the backlog. If the story is too large, split it (see Story Splitting).

**A note on naming.** One well-known author finds the term "acceptance criteria" confusing and prefers "conditions of satisfaction". Both names point to nearly the same idea.

## Example

Story: "As a shopper, I want to reset my password so that I can regain access."

Criteria written as Given-When-Then:

- Given a registered shopper, when they request a reset, then a reset message goes to their address.
- Given an unknown address, when someone requests a reset, then no message goes out.

The Definition of Done is separate. It might say that every item must be reviewed and tested. It applies to all stories, not just this one.

## Trade-offs

Naming varies between teams. "Acceptance criteria" and "conditions of satisfaction" are used almost interchangeably. Criteria also differ from the Definition of Done: criteria are specific to one story, while the Definition of Done applies to all stories.
