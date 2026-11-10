---
title: User Story
slug: user-story
category: functional-requirements
kind: artifact
summary: A user story is a short requirement written from a stakeholder's point of view. It is a reminder
  to talk, not a full specification. Details follow through conversation and acceptance tests.
arc42:
- 1
- 10
step: s03-functional-requirements
related:
- card-conversation-confirmation
- invest-criteria
- acceptance-criteria
- user-story-vs-use-case
- use-case
- story-splitting
- epic
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
diagrams:
- file: diagram-1.mmd
  caption: 'The three elements of a user story: card, conversation and confirmation.'
review:
  status: generated
  flags: []
---

## Explanation

A user story is a brief statement of something a stakeholder needs. It is not a detailed specification. One well-known description names three elements: Card, Conversation and Confirmation (see the article Card, Conversation, Confirmation).

**Card.** The card is only a token that stands for the requirement. It does not hold all the information the requirement needs.

**Conversation.** The details come out when people talk. The talk is mostly verbal, but documents can supplement it. Talking also exposes ambiguity that stays hidden in written text.

**Confirmation.** The customer defines acceptance tests. They show that the story has been implemented correctly (see Acceptance Criterion).

**The template.** A common form is: "As a [type of user], I [need/want/am required] to [do something], so that [reason or benefit]." It names who, what and why. Stakeholders find it natural, and it helps the product owner prioritize. It should not become a ritual. It is useful only while it improves the conversation.

**What a good story looks like.** The INVEST checklist (see INVEST Criteria) says a story must be valuable to the customer, not just to anybody. It is negotiable, so it captures the essence and not the details. It is estimable enough that the team can rank and schedule it.

**Why teams use stories.**
- Compared with use cases or long lists of requirement statements, they are usually simpler to estimate and to rank by priority. This suits projects with limited time.
- They let teams defer detail until the detail is useful.
- Use cases describe generalized interactions and are often too large to estimate (see User Stories vs. Use Cases).

**Planning.** Extreme Programming has release planning and iteration planning. In both, the customer presents features. In iteration planning, programmers break them into tasks and estimate the cost at a finer level of detail than in release planning.

## Example

A online shop team writes this card: "As a shopper, I want to save items for later, so that I can buy them when I get paid."

The card says nothing about buttons or storage. The team talks with the customer. They ask whether saved items expire and how many can be saved. The customer then writes an acceptance test: a saved item is still there at the next visit. The team can estimate the story and rank it against others.

## Trade-offs

Stories keep requirements short and push detail into conversation. This exposes misunderstandings early and avoids writing detail that is never used. The cost is that the card alone is incomplete. Anyone who reads only the card lacks the details. Those details live in conversations, in supporting documents and in the acceptance tests. The template also helps only while it supports the conversation. Used as a ritual, it adds nothing.
