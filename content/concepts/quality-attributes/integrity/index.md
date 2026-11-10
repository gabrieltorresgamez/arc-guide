---
title: Integrity
slug: integrity
category: quality-attributes
kind: quality-attribute
summary: Integrity means a system protects its state and data from unauthorized modification or deletion.
  It is one of several security sub-characteristics in ISO/IEC 25010, alongside confidentiality, non-repudiation,
  accountability and authenticity.
arc42:
- 1
- 8
- 10
step: s04-quality-requirements
related:
- security
- confidentiality
- nonrepudiation
- accountability
- authenticity
- iso-iec-25010-quality-model
- security-tactics
- security-scenario
checks:
- The document states which data and system state must be protected from unauthorized modification or
  deletion.
- Integrity is treated separately from confidentiality, which covers who may access data.
- The document describes how unauthorized changes to software and information are detected.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=6
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://www.fedramp.gov/2026/reference/controls/system-and-information-integrity/
  title: System and Information Integrity - FedRAMP Consolidated Rules for 2026
  site: fedramp.gov
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Integrity is a security sub-characteristic in the ISO/IEC 25010 quality model (see ISO/IEC 25010 Product Quality Model). It describes how well a system, product or component keeps its state and data from being changed or deleted without permission, whether through an attack or a computer error.

Integrity sits next to other security sub-characteristics. Each answers a different question:

- **Confidentiality:** can only authorized parties access the data?
- **Non-repudiation:** can we prove that an action or event took place? See Nonrepudiation.
- **Accountability:** can we trace an entity's actions uniquely back to that entity? See Accountability.
- **Authenticity:** can we prove that a subject or resource has the identity it claims? See Authenticity.

## Example

An online shop stores customer orders. Only the order service may change an order's status. A support agent may view orders but not edit them. A scheduled check compares stored files against known-good versions and raises an alert when something differs. The team writes the integrity goal in its quality requirements: no unauthorized change to an order goes unnoticed.
