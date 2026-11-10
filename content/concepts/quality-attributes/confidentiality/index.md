---
title: Confidentiality
slug: confidentiality
category: quality-attributes
kind: quality-attribute
summary: Confidentiality means only authorized parties can read data. It is one part of security. Teams
  achieve it with access controls, encryption and data classification, inside defined trust boundaries.
arc42:
- 1
- 2
- 8
- 10
- 11
step: s04-quality-requirements
related:
- security
- integrity
- availability
- nonrepudiation
- accountability
- authenticity
- encrypt-data
- iso-iec-25010-quality-model
checks:
- Data is classified by type, sensitivity and risk, and each class has an assigned confidentiality level.
- Encryption at rest and in transit is chosen based on the confidentiality level of the data.
- Trust boundaries are defined, and sensitive flows are segmented so only roles and assets that need them
  can reach them.
- An audit trail records activity on sensitive data and systems.
- The document notes the trade-off between security measures and availability or operational complexity.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=5
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/security/principles
  title: Security design principles - Microsoft Azure Well-Architected Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://csrc.nist.gov/glossary/term/confidentiality
  title: confidentiality - Glossary | CSRC
  site: csrc.nist.gov
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/training/modules/tm-use-a-framework-to-identify-threats-and-find-ways-to-reduce-or-eliminate-risk/1b-threat-modeling-framework
  title: Threat modeling framework - Training | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_data_classification_define_protection.html
  title: SEC07-BP02 Apply data protection controls based on data sensitivity - AWS Well-Architected Framework
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://gdpr-info.eu/art-32-gdpr/
  title: Art. 32 GDPR – Security of processing - General Data Protection Regulation (GDPR)
  site: gdpr-info.eu
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Sensitive data sits in its own zone. Only authorized access passes the trust boundary, and
    activity is logged.
review:
  status: generated
  flags: []
---

## Explanation

Confidentiality is the degree to which a system makes sure that only authorized parties can access its data. ISO/IEC 25010 uses this definition. NIST words it as sensitive information not being disclosed to unauthorized entities. (See *ISO/IEC 25010 Product Quality Model* and *Security*.)

**How it differs from its neighbors.** Confidentiality limits who can *read* data. Integrity limits who can *change or delete* it. Other security properties in ISO/IEC 25010 ask related questions:

- Non-repudiation: actions can be proven to have happened, so nobody can deny them later.
- Accountability: an action can be traced uniquely to the entity that did it.
- Authenticity: an identity can be proven to be the one claimed.

**The CIA triad.** Azure guidance presents confidentiality, integrity and availability as interrelated principles, called the CIA triad. It applies them within a zero-trust approach. The STRIDE threat model pairs threats with controls. Information disclosure means someone sees data without permission, and confidentiality counters it. Spoofing maps to authentication, tampering to integrity, and repudiation to non-repudiation.

**What teams do about it.** Azure says confidentiality work should focus on three things:

- access controls,
- opacity (making data unreadable to outsiders),
- an audit trail of activity on data and systems.

Data must also stay inside established trust boundaries. Segmentation helps. It limits sensitive flows to the roles and assets that need them.

**Classify data first.** Azure advises classifying data by type, sensitivity and risk, and giving each class a confidentiality level. That level guides the choice of encryption at rest, in transit and during processing. AWS gives example classes: public, internal, confidential and restricted. It suggests isolation boundaries per level. It also suggests tokenization or anonymization to lower the sensitivity of data. Encryption, access controls and auditing protect data at rest and in transit.

**Legal driver.** GDPR Article 32 lists the ongoing confidentiality, integrity, availability and resilience of processing systems as a security requirement. It names encryption and pseudonymisation as measures.

## Example

An online clinic stores patient notes, appointment times and a public price list. The team labels the notes "restricted", the appointments "confidential" and the price list "public". Notes get encryption and tight role-based access, with every read logged. The price list gets none of that. The notes live in a separate network segment that only the clinical application can reach.

## Trade-offs

Security and reliability can pull in opposite directions. Security-focused design can add points of failure and operational complexity. Azure links this effect to reliability, noting that it is often indirect and comes through operational constraints. Separately, AWS warns that applying the same controls to all data can over-protect low-sensitivity data and under-protect highly sensitive data. Classification lets you spend effort where it matters. (See *Quality Attribute Trade-off*.)
