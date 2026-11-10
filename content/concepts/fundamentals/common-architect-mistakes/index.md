---
title: Common Architect Mistakes
slug: common-architect-mistakes
category: fundamentals
kind: concept
summary: 'Architects repeat the same mistakes: weak scoping, narrow stakeholder lists, a focus on functions,
  vague platform details, and self-built security. A published list of ten such mistakes works as a self-review
  checklist.'
arc42:
- 1
- 3
- 10
- 11
step: s01-goals-stakeholders
related:
- stakeholder-identification
- stakeholder
- quality-attribute
- security
- architectural-decision-making-fallacies
- software-architect-role
- arc42-quality-chapter
- recoverability
checks:
- Assumptions about scope and security needs, such as 'only a simple login', are written down and have
  been challenged.
- The document does not describe security as home-built technology when established solutions exist.
- Quality attributes are described explicitly and not only functions.
- Platform parts are named with specific versions and configurations.
- A disaster recovery plan and a backout plan exist.
sources:
- url: https://www.infoq.com/news/2007/10/top-ten-architecture-mistakes/
  title: Top Ten Software Architecture Mistakes - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/avoid-architecture-pitfalls/
  title: 12 Software Architecture Pitfalls and How to Avoid Them - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Some architect mistakes come up again and again. Eoin Woods collected them in a list of top ten mistakes. You can use it as a checklist to review your own work.

**Scoping woes.** The list opens here. Projects grow beyond their original purpose. Assumptions also go unchallenged. One example is the belief that security needs nothing beyond a simple login.

**A narrow stakeholder net.** The list warns against not casting the net widely enough. It names the usual mistake: attention goes to just a couple of stakeholders, typically the acquirer (who pays for the system) and the end users.

**Only functions, no quality attributes.** Functions say what the system does. The list warns against focusing only on functions, because a system is unlikely to succeed unless it also shows qualities such as performance, security and maintainability (see Quality Attribute).

**Box-and-line diagrams.** The list warns against describing a system only with boxes and lines. It also warns against forgetting that the system must actually be built.

**Vague platform, unchecked performance.** The list asks for precision about the specific versions and configurations of each part of the platform. It also warns against assuming performance without verifying it. It advises considering performance early, with performance models and proof-of-concept work.

**Do-it-yourself security.** Architects tend to think they can build clever security technology quickly. They are usually wrong, and home-brew security is rarely a good idea.

**No disaster recovery and no backout plan.** The list names both as mistakes.

## Example

A team plans an online booking tool. The brief says security means "a simple login." The architect asks whether that is really true and finds that payment data is involved. The architect also asks who else cares: support staff, finance and operations. The team writes down exact platform versions, tests expected load early, and picks a proven login product instead of building one. It also writes a recovery plan and a plan for rolling back a failed release.

## Trade-offs

The verified material covers only part of the topic: brief excerpts from one list. It is not a complete catalog. A checklist also cannot replace judgment. Use the list to prompt questions, not to prove a design is sound.
