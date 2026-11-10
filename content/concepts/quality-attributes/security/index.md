---
title: Security
slug: security
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
- confidentiality
- integrity
- availability
- accountability
- authenticity
- resistance
- security-tactics
- security-scenario
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
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A secure system resists attacks. It rests on three linked principles, known as the CIA triad: confidentiality, integrity and availability. AWS Well-Architected treats security as one of six pillars. It aims for architectures that protect data, control access and react automatically to security events.

**Confidentiality.** Data is accessible only to those authorized to see it. A common way to achieve this is need-to-know access, also called least privilege. Each person or component gets only the access it needs.

**Integrity.** Controls must check who is asking (authentication) and what they may do (authorization). Cryptography helps too. For example, a digital signature shows that data was not changed in transit.

**Availability.** The system should not go down because of malicious action. A distributed denial-of-service (DDoS) attack is one example. It exhausts the system's resources and causes downtime.

ISO 25010 adds more terms. The article ISO/IEC 25010 Product Quality Model covers the full model.

- **Accountability:** an entity's actions can be traced uniquely to that entity.
- **Authenticity:** a claimed identity can be proved.
- **Resistance:** the system keeps operating while a malicious actor attacks it.

**Detection and recovery.** Audit logs speed up detection and recovery after incidents. They also support ongoing security monitoring. Threat modeling is recommended to identify and reduce threats.

## Example

A web shop stores customer orders. Only the order service and support staff may read them (confidentiality, need-to-know). Payment messages carry a digital signature, so tampering can be detected (integrity). The shop is designed so a flood of fake requests cannot take it offline (availability). Audit logs record who changed which order (accountability).

## Trade-offs

Security and reliability can pull in opposite directions. Security design can add points of failure and operational complexity, so the team must weigh this trade-off.

Security controls should block attackers but not legitimate users. See the articles Availability and Quality Attribute Trade-off.
