---
title: Risk Identification and Safe Integration
slug: risk-identification
category: quality-attributes
kind: quality-attribute
summary: Risk identification is a product's ability to spot events or operations that could put people,
  property or the environment at unacceptable risk. Safe integration is its ability to stay safe during
  and after joining with other components.
arc42:
- 10
- 11
step: s04-quality-requirements
related:
- safety
- iso-iec-25010-quality-model
- iso-25010-2023-revision
- safety-tactics
- operational-constraint
- hazard-warning
- integration
- quality-attribute-scenario
checks:
- The document states which events or operations could expose life, property or the environment to unacceptable
  risk.
- Safety expectations are stated for both the integration moment and the system after integration.
- The conditions under which safety must hold are defined.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=9
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Both ideas are sub-characteristics of Safety in ISO/IEC 25010. See the articles on Safety and the ISO/IEC 25010 Product Quality Model for the wider picture.

Safety itself means avoiding states in which human life, health, property or the environment is endangered. This applies under defined conditions.

**Risk identification**

Risk identification is the ability to identify courses of events or operations that can expose life, property or the environment to unacceptable risk. The word "unacceptable" matters. The idea concerns risks that are unacceptable.

**Safe integration**

Safe integration is the ability to keep safety intact when the product is combined with one or more other components. The definition covers two moments: during integration and after it. So safety is not a one-time check at the moment of connecting. It must still hold in the combined system afterward.

For the general topic of joining components, see the article on Integration.

**How they fit together**

Risk identification asks what could go wrong. Safe integration asks whether safety survives when parts are joined.

## Example

A team builds a monitoring unit for a chemical storage room. It must recognize events that could endanger staff or the building. That is a risk identification goal.

Later, the team connects the unit to a building alarm system from another vendor. They ask two questions. Does safety hold while the connection is made? Does it still hold once both systems run together? The second question is the one that is easy to forget.
