---
title: Frequent Mistakes in Defining Acceptance Criteria
slug: frequent-mistakes-in-defining-acceptance-criteria
category: functional-requirements
kind: concept
summary: Acceptance criteria go wrong when they replace conversation, hide the user's goal, or drift into
  technical detail. Good criteria stay user-focused and testable, and they support the team's discussion
  of the story.
arc42:
- 1
- 10
step: s03-functional-requirements
related:
- acceptance-criteria
- invest-criteria
- user-story
- card-conversation-confirmation
- smart-requirements
- quality-attribute-scenario
- definition-of-done-for-architectural-decisions
- testability
checks:
- Acceptance criteria are written in the user's behavior and language, not as implementation steps.
- Each criterion is precise enough that QA can tell how to test it.
- The user's goal stays visible next to the criteria.
- Given-When-Then criteria have a single trigger in the When clause.
- Stories are marked done only when their own criteria and the Definition of Done are met.
sources:
- url: https://www.mountaingoatsoftware.com/agile/user-stories/acceptance-criteria
  title: Acceptance Criteria for User Stories - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/clarifying-the-relationship-between-definition-of-done-and-conditions-of-sa
  title: Relationship between Definition of Done and Conditions of Satisfaction - Mountain Goat Software
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
- url: https://martinfowler.com/bliki/GivenWhenThen.html
  title: Given When Then
  site: martinfowler.com
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

Acceptance criteria are details that let a product owner and team check whether a story is done correctly. Teams often repeat the same few mistakes when they write them.

**Replacing the conversation.** Criteria should clarify the discussion about a story, not stand in for it. Criteria help when they invite discussion. They hurt when they become a checklist for avoiding collaboration.

**Forgetting the user.** A long list of criteria can hide the user's goal. Keep that goal visible. 

**Too much technical detail.** Criteria should say what must be true for the user or product. They should not list every implementation step. Technical detail in criteria is also a warning sign that the story itself is too technical. It pushes a solution before developers have looked at the problem.

**Vague criteria.** Good criteria make a story more precise and testable. The "T" in the INVEST checklist (see INVEST Criteria) means testable: a story must be verifiable in principle, even if no test exists yet.

**Missing shared criteria.** The Definition of Done can be thought of as a special set of criteria added to every story. A story is done only when its own criteria and the Definition of Done are both met.

**Format help.** Given-When-Then describes a scenario from the user's perspective. It comes from Behavior-Driven Development (BDD). Keep a single trigger in the When clause. Mixing preconditions and triggers defeats the format.

The author Roman Pichler calls acceptance criteria maybe the most misunderstood part of user stories.

## Example

A team writes a story: "As a shopper, I want to reset my password, so that I can get back into my account."

Weak criteria: "The system calls the mail service through a queue and stores a hash in table X." This is technical and says nothing the shopper can see. It also gives QA no clear check.

Better criteria: "Given I forgot my password, when I request a reset, then I receive a reset link." A second one: "Given I opened a valid link, when I enter a new password, then I can log in with it." Each one is written from the shopper's view and can be tested. The team still talks through edge cases, such as expired links, instead of relying on the list alone.

## Trade-offs

Too much detail too soon can waste effort and limit the team's ability to find a better solution.
