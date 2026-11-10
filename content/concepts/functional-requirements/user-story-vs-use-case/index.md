---
title: User Stories vs. Use Cases
slug: user-story-vs-use-case
category: functional-requirements
kind: concept
summary: User stories are small, brief requirements that a team estimates and talks through. Use cases
  are more detailed and can be understood on their own. A story is roughly a use case at very low precision.
arc42:
- 1
- 3
step: s03-functional-requirements
related:
- user-story
- use-case
- card-conversation-confirmation
- consistency-of-user-story-and-use-case
- acceptance-criteria
- smart-requirements
- use-case-goal-levels
- use-case-template
checks:
- Each user story is backed by acceptance tests or examples that confirm it.
- Use cases in the document are detailed enough to be understood without the author.
- Requirements chosen for estimation and prioritization are small enough to estimate usefully.
sources:
- url: https://www.mountaingoatsoftware.com/agile/advantages-of-user-stories-for-requirements
  title: Advantages of User Stories over Requirements and Use Cases - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Use_case
  title: Use case - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/User_story
  title: User story - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/
  title: 'Essential XP: Card, Conversation, Confirmation'
  site: ronjeffries.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Both ideas capture what a system should do. They differ in size, detail, and how teams use them.

**Scope and estimation.** A use case (see Use Case) is often too large to estimate in a useful way. A user story (see User Story) is smaller. Compared with use cases or long lists of requirement statements, stories are usually simpler to estimate and to rank by priority.

**Detail.** A use case aims to give enough detail to be understood on its own. A story does not. A story works as a token for the requirement. The detail travels through conversation between the customer and the programmers.

**The Three Cs.** Stories rely on three parts (see Card, Conversation, Confirmation):

- A card, which is a physical token.
- A conversation between stakeholders.
- A confirmation that the goals of the conversation were met.

Acceptance tests provide the confirmation. They make the simple card-and-conversation approach workable.

**How they relate.** One view treats a story as a use case at 2 bits of precision. That means a goal plus a main scenario, and little else. So the two are not opposites. They sit at different levels of precision.

**Teams new to this.** Inexperienced teams often want to try use cases. One view holds that use cases are rarely ideal compared with confirming a requirement through examples.

## Example

A shop team needs a "return an item" feature. On a story card, they write one line: a customer returns an item and gets a refund. The team estimates it quickly. In conversation, the customer explains the details. They agree on example checks, such as "a returned item with a receipt is refunded."

A use case for the same goal would describe the goal and its steps in a document. A reader who missed the conversation could still follow it.

## Trade-offs

Stories are easy to estimate, but the detail lives in conversations, not on the card. Use cases stand on their own, but they tend to be too large to estimate usefully. Which one fits depends on whether you need quick planning or a self-contained description.
