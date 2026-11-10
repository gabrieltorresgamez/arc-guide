---
title: INVEST Criteria
slug: invest-criteria
category: functional-requirements
kind: concept
summary: 'INVEST is a six-point checklist for judging a user story: Independent, Negotiable, Valuable,
  Estimable, Small, Testable. Teams use it to check a story before planning, and to check the story they
  are about to split.'
arc42:
- 1
step: s03-functional-requirements
related:
- user-story
- story-splitting
- acceptance-criteria
- invest-applied-to-architectural-work
- card-conversation-confirmation
- epic
- smart-requirements
- story-mapping
checks:
- Stories are written so they can be scheduled and built in any order, or the dependency and its effect
  on estimates is stated.
- Each story states value to the customer, not only technical work.
- Each story has an estimate good enough for the customer to rank and schedule it.
- Large stories are checked against INVEST before they are split.
sources:
- url: https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/
  title: The Humanizing Work Guide to Splitting User Stories
  site: humanizingwork.com
  accessed: '2026-11-09'
- url: https://xp123.com/invest-in-good-stories-and-smart-tasks/
  title: INVEST in Good Stories, and SMART Tasks - XP123
  site: xp123.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

INVEST gives six questions to ask about a user story. A user story is a description of a change in system behavior from the perspective of a user (see the article User Story). The splitting guide from Humanizing Work credits Wake with the INVEST acronym and calls it six key attributes of a good story.

**Independent.** Stories should not overlap in concept. The team should be able to schedule and build them in any order. Independence cannot always be achieved. For example, the first report may cost 3 points and each later report 1.

**Negotiable.** Over time a story card gains notes and test ideas. The card does not need these details for stories to be prioritized or scheduled. The details are co-created by the customer and programmers during development.

**Valuable.** A story must be valuable to the customer, not just to anybody.

**Estimable.** The estimate does not have to be exact. It only has to be good enough for the customer to rank and schedule the story.

**Small.** Bigger stories are harder to estimate. Above a few person-weeks of work, it becomes hard to know what is in the story's scope. The Humanizing Work guide suggests being able to fit 6 to 10 stories into a sprint.

**Testable.** Several teams report that they are more productive when customer tests are required before a story is built.

**Where to apply it.** The first step of the splitting flowchart is to check that the story you want to split meets the INVEST criteria other than small. See the article Story Splitting for the rest of the process.

## Example

A team has the story "Users can manage their account." Checking it against INVEST shows problems. Nobody can say what "manage" covers, so it is hard to estimate. The team splits it into narrower stories, such as "A user can change their password." Each new story gets the same six checks. Does it help the customer? Can it be ranked? Can we write a test for it?

## Trade-offs

The criteria can pull against each other. Making stories independent is not always possible. Making a story small is useful, but each smaller story must still be valuable to the customer. The estimates only need to be good enough for ranking, so chasing exactness adds little.
