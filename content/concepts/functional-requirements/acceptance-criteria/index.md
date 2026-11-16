---
title: Acceptance Criterion
slug: acceptance-criteria
order: 60
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
- story-splitting
- method-phase-working-with-functional-requirements
- maintainability
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
- url: https://www.mountaingoatsoftware.com/agile/user-stories/acceptance-criteria
  title: Acceptance Criteria for User Stories - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://technology.blog.gov.uk/2015/03/04/creating-better-acceptance-criteria-for-user-stories/
  title: Creating better acceptance criteria for user stories – Technology in government
  site: technology.blog.gov.uk
  accessed: '2026-11-09'
- url: https://modernanalyst.com/Resources/Articles/tabid/115/ID/4903/5-Common-User-Story-Mistakes.aspx
  title: 5 Common User Story Mistakes
  site: modernanalyst.com
  accessed: '2026-11-09'
- url: https://www.thoughtworks.com/en-in/insights/blog/applying-bdd-acceptance-criteria-user-stories
  title: Applying BDD acceptance criteria in user stories | Thoughtworks India
  site: thoughtworks.com
  accessed: '2026-11-09'
- url: https://agilealliance.org/glossary/invest/
  title: What does INVEST Stand For? | Agile Alliance
  site: agilealliance.org
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

**Common mistakes.**

- **Frequent Mistakes in Defining Acceptance Criteria:** Acceptance criteria go wrong when they replace conversation, hide the user's goal, or drift into technical detail. Good criteria stay user-focused and testable, and they support the team's discussion of the story.

## Example

Story: "As a shopper, I want to reset my password so that I can regain access."

Criteria written as Given-When-Then:

- Given a registered shopper, when they request a reset, then a reset message goes to their address.
- Given an unknown address, when someone requests a reset, then no message goes out.

The Definition of Done is separate. It might say that every item must be reviewed and tested. It applies to all stories, not just this one.

## Trade-offs

Naming varies between teams. "Acceptance criteria" and "conditions of satisfaction" are used almost interchangeably. Criteria also differ from the Definition of Done: criteria are specific to one story, while the Definition of Done applies to all stories.
