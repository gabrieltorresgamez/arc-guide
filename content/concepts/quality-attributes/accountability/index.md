---
title: Accountability
slug: accountability
category: quality-attributes
kind: quality-attribute
summary: Accountability means you can trace each action to the one entity that did it. It is a security
  quality in ISO/IEC 25010, next to authenticity, non-repudiation, and confidentiality.
arc42:
- 8
- 10
- 1
step: s04-quality-requirements
related:
- authenticity
- nonrepudiation
- confidentiality
- security
- iso-iec-25010-quality-model
- correlation-identifier
- integrity
- security-tactics
checks:
- The document states that actions must be traceable uniquely to the acting entity.
- Log records have tamper detection, so modified or deleted records are noticed.
- An interaction identifier links the events of one user interaction across components.
- The document says how personal data in logs is avoided or de-identified.
- Log data is copied to read-only media quickly.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=6
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/accountability
  title: Accountability | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
  title: Logging - OWASP Cheat Sheet Series
  site: cheatsheetseries.owasp.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC 25010 is a standard model of software quality (see the article ISO/IEC 25010 Product Quality Model). It defines accountability as the degree to which an entity's actions can be traced uniquely to that entity. The 2023 wording describes it as a capability of a product to enable this tracing.

The NIST definition adds a purpose. Activities on a system can be traced back to individuals, and those individuals can then be held responsible for what they did.

Accountability sits beside other security sub-characteristics, including:

- **Authenticity** is about proving that an identity is the one claimed. See the article Authenticity.
- **Non-repudiation** is about proving that actions or events took place, so nobody can deny them later. See the article Nonrepudiation.
- **Confidentiality** means data is accessible only to authorized parties. See the article Confidentiality.

An interaction identifier links all relevant events of one user interaction. Recording it means later correlation does not have to reconstruct those separate events. See the article Correlation Identifier.

## Example

A web shop lets staff change product prices. Each change is logged with the staff member's identity. The same interaction identifier appears in every component that handles the request. After a wrong price appears, the team follows the identifier across components and finds who made the change.

## Trade-offs

Logging personal data conflicts with privacy. OWASP suggests avoiding personal data in logs or de-identifying it, for example by pseudonymization (replacing identifying values with stand-ins). The identity you log must still be enough to trace the action, so balance the two goals deliberately.
