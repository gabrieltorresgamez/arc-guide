---
title: Motivation for Architecture Documentation
slug: motivation-for-architecture-documentation
category: documentation
kind: concept
summary: Code shows what a system does, but not why it was built that way. Architecture documentation
  records those reasons, so knowledge does not stay locked in a few people's heads.
arc42:
- 1
- 9
step: s10-document
related:
- architecture-decision-rationale
- architectural-decision-record
- arc42-documentation-template
- guidelines-for-documentation
- architecture-decay
- arc42-architecture-decisions
- self-documentation
- documentation-as-code
checks:
- The document records the reasons behind important decisions, not only the decisions themselves.
- The document covers what cannot be read from the code.
- The content is limited to what stakeholders need, so people can find and update it.
- The documentation is current enough that readers can trust it.
sources:
- url: https://www.infoq.com/podcasts/simon-brown-architecture/
  title: Simon Brown on the Role of the Software Architect in a Continuous Delivery Environment - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
- url: https://arc42.org/documentation/
  title: arc42 Documentation - arc42
  site: arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
  title: Architecture Decision Record
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Teams often say the code is the only documentation they need. That claim is wrong. Code cannot tell you the reasons behind decisions. Architecture documentation fills that gap.

Without it, knowledge about the architecture ends up in one of three places. It sits in a few people's heads, it is scattered across the code, or it is lost.

Decisions are a good example. Teams often remember what they decided but forget why. Stakeholders (people with an interest in the system) should be able to understand and retrace those decisions. Written rationale supports that conversation. Months or years later, a short decision record can still explain why the system looks the way it does. See the articles on Architectural Decision Record and Architecture Decision Rationale.

Documentation can also fail in two opposite ways:

- It is missing, or it is outdated and nobody trusts it.
- There is too much of it, so nobody can find or update anything.

The way out is to write just enough. Document what stakeholders need, and focus on what the code cannot show. Short pieces are easier to read, create and maintain. Low effort also keeps documentation current. For a few important decisions, write a brief note with the reasons.

## Example

A new developer joins a team and asks why the system uses a message queue instead of direct calls. The code shows that a queue exists. It does not show why. The people who made the choice are no longer around. A half-page decision note would have answered the question quickly. Without it, the team has to work out the reasons again from scratch.

## Trade-offs

More documentation is not always better. Piles of documents fail because nobody can find or update anything. Missing or outdated documentation fails too, because nobody trusts it. Limit the content to what stakeholders need, and keep the effort low so the documents stay current.
