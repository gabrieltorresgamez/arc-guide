---
title: Card, Conversation, Confirmation
slug: card-conversation-confirmation
category: functional-requirements
kind: method
summary: 'A user story has three parts: a short card that names it, conversations that work out the details,
  and confirmation tests that show when the story is done as agreed.'
arc42:
- 1
step: s03-functional-requirements
related:
- user-story
- acceptance-criteria
- invest-criteria
- story-splitting
- frequent-mistakes-in-defining-acceptance-criteria
- user-story-role-formulation
- user-story-vs-use-case
- epic
checks:
- Each story has a brief card or name, and the details are not stuffed into it.
- Each story has confirmation (acceptance criteria, examples or tests) that tells the team when it is
  complete.
- Agreements on a story are documented as confirmation tests, not only on the card.
- Confirmation tests run against the real system and report whether the expected result occurs.
sources:
- url: https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/
  title: 'Essential XP: Card, Conversation, Confirmation'
  site: ronjeffries.com
  accessed: '2026-11-09'
- url: https://ronjeffries.com/articles/019-01ff/stories-3cs-yet-again/
  title: Stories and the Three C's - Revisited Yet Again
  site: ronjeffries.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/user-stories
  title: 'User Stories: What They Are, How to Write Them, and Examples - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/user-story-conversation/
  title: 'User Story: a Placeholder for a Conversation - InfoQ'
  site: infoq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The three parts of a user story and how they lead to done.
review:
  status: generated
  flags: []
---

## Explanation

A user story (see the article User Story) is more than a piece of text. It has three parts, often called the three Cs.

**Card.** The card says briefly what the story is. It can be a literal card, and it needs only a short name. It is a reminder, not a full description. One way to put it: the card is a ticket to a conversation. Many teams write the card with the template "As a [type of user], I want to [do something], so that [reason]". That template is a thinking tool. Use it when it improves the conversation.

**Conversation.** The requirement itself passes from customer to programmers through conversation, which is largely verbal but can be supplemented with documents. The card only points to that talk. The details come out of the dialogue.

**Confirmation.** As the conversation goes on, the group focuses more and more on concrete examples. These examples become confirmation tests. They can be written as acceptance criteria, examples or tests. Acceptance criteria are details that help the team judge whether the story was completed correctly. See the article Acceptance Criterion.

If all the examples pass, the story is done as agreed. This gives everyone a shared view of "done". For best results, the examples are executable tests that exercise the real system and report whether the expected result occurs.

The model also connects to other story practices:
- INVEST is a set of criteria for well-sliced stories. See INVEST Criteria.
- Story splitting breaks a large story into smaller ones that still show meaningful progress. See Story Splitting.

## Example

A team keeps a card that reads "Customer resets password". That is all it says.

The product owner and a developer then talk. They work out what should happen with an unknown email address and what the customer sees afterward.

Those answers become concrete examples, such as "unknown address: show a neutral message". The team turns the examples into tests. When all the tests pass against the real system, everyone agrees the story is done.

## Trade-offs

The card is short on purpose, so it cannot carry the details.

The model also relies on real dialogue with the customer. Without that talk, the card stays a vague reminder.
