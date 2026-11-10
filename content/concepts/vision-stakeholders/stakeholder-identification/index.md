---
title: Stakeholder Identification
slug: stakeholder-identification
category: vision-stakeholders
kind: practice
summary: Stakeholder identification means finding the people, teams and organizations with an interest
  in a system. It comes first, before you rank stakeholders or plan how to talk to them.
arc42:
- 1
step: s01-goals-stakeholders
related:
- stakeholder
- stakeholder-concern
- stakeholder-power-grid
- concern
- arc42-introduction-and-goals
- togaf
- iso-iec-ieee-42010-architecture-description-standard
- stakeholder-perspective-and-concern
checks:
- The document lists stakeholders in a table with role or name, contact and expectations.
- Each stakeholder is linked to concerns, and the concerns are addressed explicitly.
- Every stakeholder class is considered, for example acquirers and assessors.
- Identification used guiding questions such as who gains or loses, who decides and who controls resources.
sources:
- url: https://togaf.visual-paradigm.com/2025/03/04/comprehensive-guide-to-stakeholder-management-in-togaf/
  title: Comprehensive Guide to Stakeholder Management in TOGAF - Visual Paradigm
  site: togaf.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/standards/iso-42010
  title: ISO/IEC/IEEE 42010 - Architecture Description | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/stakeholders/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Stakeholder management steps, starting with identification.
review:
  status: generated
  flags: []
---

## Explanation

Stakeholders are individuals, teams or organizations with an interest in the system being described. Their interests are called concerns. Examples are performance, security or maintainability. See the articles Stakeholder and Stakeholder Concern.

**Where it sits in the process.** Stakeholder management starts with identification. Analysis follows. It rates each stakeholder's influence and interest. Tailored communication plans come after that.

**Questions that help you find them.** A guide to stakeholder management lists guiding questions. Examples:

- Who gains from this change, and who loses?
- Who decides?
- Who controls resources?
- Who has specialist skills?
- Who has influence?

**Cover every class.** An architect should make sure stakeholders are adequately represented. Every stakeholder class needs consideration. Two classes are examples:

- Acquirers oversee the procurement of the system or product.
- Assessors check conformance to standards and legal regulation.

**Record them.** The architecture description must address stakeholder concerns explicitly. The arc42 template includes a stakeholder table. Each row has a role or name, a contact and expectations. Stakeholders can be persons, roles or organizations.

## Example

A company plans a new online ordering system. The team asks the guiding questions. Who gains? Customers and the sales team. Who loses? Staff whose manual work disappears. Who decides? The department head. Who controls the budget? The finance lead. Who has specialist skills? A long-time developer. Who checks legal rules? A compliance officer. Each answer becomes a row in the stakeholder table with a role, a contact and expectations.

## Trade-offs

One risk is clear: if you do not consider each stakeholder class, you will have problems in the future.
