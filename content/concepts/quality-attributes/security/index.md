---
title: Security
slug: security
order: 60
category: quality-attributes
kind: quality-attribute
summary: Security means protecting data from unauthorized access while still serving legitimate users,
  and keeping the system running under attack. It rests on confidentiality, integrity and availability,
  and it can pull against reliability.
arc42:
- 1
- 8
- 10
- 11
step: s04-quality-requirements
related:
- reliability
- security-tactic
checks:
- Confidentiality requirements state who may access which data, using need-to-know (least privilege) access.
- Integrity measures cover authentication, authorization and tamper detection such as digital signatures.
- The design addresses attacks, such as DDoS, that could exhaust resources and cause downtime.
- Audit logging and threat modeling are described as ways to detect threats and recover.
- Trade-offs between security and reliability or availability are stated and weighed.
sources:
- url: https://learn.microsoft.com/en-us/azure/well-architected/security/principles
  title: Security design principles - Microsoft Azure Well-Architected Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=5
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html
  title: Security Pillar - AWS Well-Architected Framework - Security Pillar
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: "ISO 25010"
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://csrc.nist.gov/glossary/term/confidentiality
  title: "confidentiality - Glossary | CSRC"
  site: csrc.nist.gov
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/confidentiality
  title: "Confidentiality | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://www.fedramp.gov/2026/reference/controls/system-and-information-integrity/
  title: "System and Information Integrity - FedRAMP Consolidated Rules for 2026"
  site: fedramp.gov
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/integrity
  title: "Integrity | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://en.wikipedia.org/wiki/Non-repudiation
  title: "Non-repudiation - Wikipedia"
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.rfc-editor.org/info/rfc3161/
  title: "RFC 3161: Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP) | RFC Editor"
  site: rfc-editor.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/non-repudiation
  title: "Non-repudiation | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
  title: "Logging - OWASP Cheat Sheet Series"
  site: cheatsheetseries.owasp.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/accountability
  title: "Accountability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://learn.microsoft.com/en-us/entra/identity-platform/authentication-vs-authorization
  title: "Authentication vs. authorization - Microsoft identity platform | Microsoft Learn"
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://openid.net/specs/openid-connect-core-1_0.html
  title: "Final: OpenID Connect Core 1.0 incorporating errata set 2"
  site: openid.net
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/authenticity
  title: "Authenticity | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://www.sei.cmu.edu/blog/system-resilience-part-5-commonly-used-system-resilience-techniques/
  title: "System Resilience Part 5: Commonly-Used System Resilience Techniques | CMU Software Engineering Institute"
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/resistance
  title: "Resistance | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/tamper-evident-digital-signatures
  title: "Tamper-Evident Digital Contract Signatures"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/authenticity-of-digital-document
  title: "Authenticity of a digital document"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/employee-attempts-to-modify-pay-rate
  title: "Employee attempts to modify pay rate"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/security
  title: "Security | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A secure system resists attacks. Azure's security guidance names the CIA triad: confidentiality, integrity and availability. AWS Well-Architected treats security as one of six pillars. It aims for architectures that protect data, control access and react automatically to security events.

**Confidentiality.** Data is accessible only to those authorized to see it. A common way to achieve this is need-to-know access, also called least privilege. Each person or component gets only the access it needs.

**Integrity.** Access controls that check who is asking (authentication) and what they may do (authorization) support it. Cryptography helps too. For example, a digital signature shows that data was not changed in transit.

**Availability.** The system should not go down because of malicious action. A distributed denial-of-service (DDoS) attack is one example. It can cause downtime.

ISO 25010 adds more terms. See ISO/IEC 25010 Product Quality Model for the full model.

- **Accountability:** an entity's actions can be traced uniquely to that entity.
- **Authenticity:** a claimed identity can be proved.
- **Resistance:** the system keeps operating while a malicious actor attacks it.

**Detection and recovery.** Audit logs support faster detection and recovery after incidents. They also support ongoing security monitoring.

**Tactics.** See the article Security Tactic.

**Subcharacteristics.** The ISO/IEC 25010 model lists these subcharacteristics under this characteristic:

- **Confidentiality** means only authorized parties can read data. Approaches include access controls, encryption and data classification. More: [arc42 quality model](https://quality.arc42.org/qualities/confidentiality), [Security design principles - Microsoft Azure Well-Architected Framework | Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/security/principles), [confidentiality - Glossary | CSRC](https://csrc.nist.gov/glossary/term/confidentiality).
- **Integrity** means a system protects its state and data from unauthorized modification or deletion. More: [arc42 quality model](https://quality.arc42.org/qualities/integrity), [System and Information Integrity - FedRAMP Consolidated Rules for 2026](https://www.fedramp.gov/2026/reference/controls/system-and-information-integrity/) [src:7].
- **Non-repudiation** means actions can be proven to have happened, so an author cannot successfully deny a message or a contract. Digital signatures are a common method, and trusted third parties are a standard approach. More: [arc42 quality model](https://quality.arc42.org/qualities/non-repudiation), [Non-repudiation - Wikipedia](https://en.wikipedia.org/wiki/Non-repudiation), [RFC 3161: Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP) | RFC Editor](https://www.rfc-editor.org/info/rfc3161/).
- **Accountability** means you can trace each action to the one entity that did it. More: [arc42 quality model](https://quality.arc42.org/qualities/accountability), [Logging - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).
- **Authenticity** is the degree to which you can prove that a user, device, or resource is the one it claims to be. More: [arc42 quality model](https://quality.arc42.org/qualities/authenticity), [Authentication vs. authorization - Microsoft identity platform | Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity-platform/authentication-vs-authorization), [Final: OpenID Connect Core 1.0 incorporating errata set 2](https://openid.net/specs/openid-connect-core-1_0.html).
- **Resistance** is how well a system keeps operating while a malicious actor attacks it. More: [arc42 quality model](https://quality.arc42.org/qualities/resistance), [System Resilience Part 5: Commonly-Used System Resilience Techniques | CMU Software Engineering Institute](https://www.sei.cmu.edu/blog/system-resilience-part-5-commonly-used-system-resilience-techniques/), [Security design principles - Microsoft Azure Well-Architected Framework | Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/security/principles).

**In the arc42 quality model.** The arc42 quality model has its own page on [Security](https://quality.arc42.org/qualities/security).

**Example quality requirements.** The arc42 quality model has example quality requirements for this characteristic: [Tamper-Evident Digital Contract Signatures](https://quality.arc42.org/requirements/tamper-evident-digital-signatures), [Authenticity of a digital document](https://quality.arc42.org/requirements/authenticity-of-digital-document), [Employee attempts to modify pay rate](https://quality.arc42.org/requirements/employee-attempts-to-modify-pay-rate).

## Example

A web shop stores customer orders. Only the order service and support staff may read them (confidentiality, need-to-know). Payment messages carry a digital signature, so tampering can be detected (integrity). The shop is designed so a flood of fake requests cannot take it offline (availability). Audit logs record who changed which order (accountability).

## Trade-offs

Security and reliability can pull in opposite directions. Security design can add points of failure and operational complexity, so the team must weigh this trade-off.

Security controls should block attackers but not legitimate users. See the articles Reliability and Quality Attribute Trade-off.
