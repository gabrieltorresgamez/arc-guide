---
title: Architectural Decision Record Example
slug: middleware-architectural-decision-example
category: forces-decisions
kind: artifact
summary: 'An ADR example records one decision: the question, the quality goals behind it, every option
  with pros and cons, and the outcome with its consequences. It lets readers retrace why a choice was
  made.'
arc42:
- 9
step: s09-decisions
related:
- architectural-decision-record
- arc42-architecture-decisions
- architecture-decision-rationale
- adr-common-mistakes-and-remediations
- messaging
- remote-procedure-call
- integration-pattern
- y-statement
checks:
- The record names the problem and links it to at least one quality goal or significant requirement.
- Rejected options are listed and evaluated, not only the chosen one.
- Pros, cons and trade-offs of the chosen option are balanced, with a stated judgment.
- Consequences include negative ones, not only positive or harmless-looking ones.
- The rationale is factual and traced back to requirements.
sources:
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/04/03/ADRCreation.html
  title: How to create Architectural Decision Records (ADRs) — and how not to
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2025/07/17/ArchitectureDecisionGuidanceTool.html
  title: 'ADG: A Light Architectural Decision Guidance and Management Tool'
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An architectural decision record (ADR) is a short note about one decision. arc42 section 9 (see "arc42 Architecture Decisions") defines a decision as picking one alternative against given criteria. It asks you to record decisions that are important, costly or risky, together with the reasons.

A good worked example has these parts:

- **The question.** It states the problem and why it matters. An ADR should log how at least one architecturally significant requirement is resolved.
- **All options, not only the winner.** Every neglected option gets evaluated too. The pros and cons of the chosen option should be balanced. The record explains the trade-offs and states a judgment.
- **The outcome and its consequences.** In the Nygard-style ADR that arc42 describes, consequences must cover more than the positive ones. The status can move from proposed to accepted, then to deprecated or superseded.
- **Factual rationale.** The argument should be factual and traced back to requirements.

arc42 also wants rejected alternatives and decision criteria documented. Then stakeholders can retrace the decision later.

**An integration-style example.** One worked example asks how programs should exchange information. It lists four options: File Transfer, Shared Database, Remote Procedure Invocation (RPI) and Messaging. It picks Messaging. The reasons are loose coupling in time and the throttling behavior of messaging channels.

Messaging means applications connect to a common messaging system. They exchange data and trigger behavior through messages. See "Messaging" and "Remote Procedure Call".

**Format.** arc42 recommends ADRs for important decisions. It also allows a list, a table, or a separate section per decision. Small records are easier to maintain.

## Example

A team must decide how a booking system passes updates to a reporting tool.

- **Question:** How should the two programs exchange information? The booking system must stay responsive when reporting is slow.
- **Quality goal:** Reliability. A slow reporting tool must not block bookings.
- **Options:** File transfer, shared database, direct remote call, messaging. Each gets pros and cons.
- **Decision:** Messaging. Status: accepted.
- **Consequences:** Bookings no longer wait for reporting. Reports may lag. The team must run and monitor a messaging system.

## Trade-offs

arc42 limits ADRs to important, costly or risky decisions. Small records are easier to read, create and maintain than one large document.

The main risk is listing only upsides. Zimmermann calls this the "Free Lunch Coupon" anti-pattern: no consequences, or only harmless-looking ones, are recorded. Every option has costs. In the messaging example, the choice rests on specific needs (loose coupling in time, throttling). Under other requirements the same reasoning may not hold. The rationale must stay tied to the context and requirements.
