---
title: Quality Attribute
slug: quality-attribute
category: quality-attributes
kind: concept
summary: A quality attribute describes how well a system meets stakeholder needs, such as speed or security.
  Teams write them as specific, measurable scenarios because they strongly shape architectural decisions.
arc42:
- 1
- 10
step: s04-quality-requirements
related:
- quality-attribute-scenario
- arc42-quality-chapter
- iso-iec-25010-quality-model
- architecturally-significant-requirement
- architectural-trade-off-thinking
- smart-requirements
- architectural-tactic
- standard-quality-attribute-checklist
checks:
- Quality requirements are written as specific, measurable scenarios, not as vague terms like "high quality".
- The document separates usage scenarios (runtime reaction to a stimulus) from change scenarios (modifying
  the system).
- Quality requirements have their own section, and architectural decisions refer to them.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://quality.arc42.org/articles/specify-quality-requirements
  title: How to specify quality requirements | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC 25010 defines system quality as the degree to which a system satisfies the stated and implied needs of its stakeholders. See the article "ISO/IEC 25010 Product Quality Model" for details.

**A catalog of qualities.** The ISO/IEC 25010 product quality model lists nine quality characteristics. Examples are functional suitability, performance efficiency, compatibility and interaction capability.

**Why the word "quality" alone is not enough.** The term is vague and broad. Quality requirements must describe stakeholder expectations in a specific and measurable way.

**Scenarios make qualities concrete.** Scenarios turn vague quality requirements into concrete ones. They should be specific and measurable. They are a practical way to document what quality is required. Bass et al. at the SEI coined the term "quality attribute scenarios" for this kind of structured requirement. See "Quality Attribute Scenario".

**Two kinds of scenarios.** arc42 describes two especially useful kinds:

- Usage scenarios describe how the running system reacts to a stimulus.
- Change scenarios describe a modification or extension of the system.

**Influence on architecture.** Quality requirements strongly influence architectural decisions. arc42 covers them in a dedicated section. See "arc42 Quality Requirements".

## Example

A team writes "the shop must be fast." Nobody can test that. They rewrite it as a usage scenario: a customer submits an order, and the system confirms it within a stated time limit. They also write a change scenario: a developer adds a new payment method, and the work stays within a stated effort. Both statements are specific and measurable, so the team can check them and use them when choosing a design.
