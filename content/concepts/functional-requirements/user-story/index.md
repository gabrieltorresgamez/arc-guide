---
title: User Story
slug: user-story
order: 30
category: functional-requirements
kind: artifact
summary: A user story is a short requirement written from a stakeholder's point of view. It is a reminder
  to talk, not a full specification. Details follow through conversation and acceptance tests.
arc42:
- 1
- 10
step: s03-functional-requirements
related:
- acceptance-criterion
- user-stories-vs-use-cases
- use-case
- story-splitting
- story-mapping
checks:
- Each story names a type of user, a goal and a reason or benefit.
- Stories are small enough to estimate and rank, and they capture the essence rather than every detail.
- Each story has customer-defined acceptance tests that show it was implemented correctly.
- The document states where story details live, such as conversations or supporting documents, since the
  card holds only part of the requirement.
- Each story is valuable to the customer, not only to some other party.
sources:
- url: https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/
  title: 'Essential XP: Card, Conversation, Confirmation'
  site: ronjeffries.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/user-stories
  title: 'User Stories: What They Are, How to Write Them, and Examples - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/why-the-three-part-user-story-template-works-so-well
  title: 'User Story Template: What It Is and Why It Works So Well - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/advantages-of-user-stories-for-requirements
  title: Advantages of User Stories over Requirements and Use Cases - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://xp123.com/invest-in-good-stories-and-smart-tasks/
  title: INVEST in Good Stories, and SMART Tasks - XP123
  site: xp123.com
  accessed: '2026-11-09'
- url: https://ronjeffries.com/xprog/what-is-extreme-programming/
  title: What is Extreme Programming?
  site: ronjeffries.com
  accessed: '2026-11-09'
- url: https://ronjeffries.com/articles/019-01ff/stories-3cs-yet-again/
  title: Stories and the Three C's - Revisited Yet Again
  site: ronjeffries.com
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/user-story-conversation/
  title: 'User Story: a Placeholder for a Conversation - InfoQ'
  site: infoq.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/user-stories/writing-user-stories
  title: 'Writing User Stories: Template, Examples, and Practical Advice - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/
  title: The Humanizing Work Guide to Splitting User Stories
  site: humanizingwork.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/non-functional-requirements-as-user-stories
  title: Non-functional Requirements as User Stories - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://framework.scaledagile.com/enablers
  title: Enablers - Scaled Agile Framework
  site: framework.scaledagile.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition/
  title: Quality Attribute Workshops (QAWs), Third Edition | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/stories-epics-and-themes
  title: Epics, Features and User Stories - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://agilealliance.org/glossary/epic/
  title: What is an Epic User Story? | Agile Alliance
  site: agilealliance.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'The three elements of a user story: card, conversation and confirmation.'
review:
  status: generated
  flags: []
---

## Explanation

A user story is a brief statement of something a stakeholder needs. It is not a detailed specification. One well-known description names three elements: Card, Conversation and Confirmation (see the article User Story).

**Card.** The card is only a token that stands for the requirement. It does not hold all the information the requirement needs.

**Conversation.** The details come out when people talk. The talk is mostly verbal, but documents can supplement it. Talking also exposes ambiguity that stays hidden in written text.

**Confirmation.** The customer defines acceptance tests. They show that the story has been implemented correctly (see Acceptance Criterion).

**The template.** A common form is: "As a [type of user], I [need/want/am required] to [do something], so that [reason or benefit]." It names who, what and why. Stakeholders find it natural, and it helps the product owner prioritize. It should not become a ritual. It is useful only while it improves the conversation.

**What a good story looks like.** The INVEST checklist (see User Story) says a story must be valuable to the customer, not just to anybody. It is negotiable, so it captures the essence and not the details. It is estimable enough that the team can rank and schedule it.

**Why teams use stories.**
- Compared with use cases or long lists of requirement statements, they are usually simpler to estimate and to rank by priority. This suits projects with limited time.
- They let teams defer detail until the detail is useful.
- Use cases describe generalized interactions and are often too large to estimate (see User Stories vs. Use Cases).

**Planning.** Extreme Programming has release planning and iteration planning. In both, the customer presents features. In iteration planning, programmers break them into tasks and estimate the cost at a finer level of detail than in release planning.

**More about user stories.**

- **Card, Conversation, Confirmation:** A user story has three parts: a short card that names it, conversations that work out the details, and confirmation tests that show when the story is done as agreed.
- **User Story Role Formulation:** A user story names a specific user role, what that role wants, and why. The "so that" part states the benefit and helps the team judge how much the story matters.
- **INVEST Criteria:** INVEST is a six-point checklist for judging a user story: Independent, Negotiable, Valuable, Estimable, Small, Testable. Teams use it to check a story before planning, and to check the story they are about to split.
- **Epic:** An epic is a large user story that is too big to finish in one iteration. It holds a place for a wanted feature until the team splits it into smaller stories.

## Example

A online shop team writes this card: "As a shopper, I want to save items for later, so that I can buy them when I get paid."

The card says nothing about buttons or storage. The team talks with the customer. They ask whether saved items expire and how many can be saved. The customer then writes an acceptance test: a saved item is still there at the next visit. The team can estimate the story and rank it against others.

## Trade-offs

Stories keep requirements short and push detail into conversation. This exposes misunderstandings early and avoids writing detail that is never used. The cost is that the card alone is incomplete. Anyone who reads only the card lacks the details. Those details live in conversations, in supporting documents and in the acceptance tests. The template also helps only while it supports the conversation. Used as a ritual, it adds nothing.
