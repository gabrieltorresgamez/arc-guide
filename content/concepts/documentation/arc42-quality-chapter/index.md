---
title: arc42 Quality Requirements Chapter
slug: arc42-quality-chapter
category: documentation
kind: artifact
summary: Chapter 10 of arc42 turns quality requirements into concrete scenarios. A quality tree gives
  the overview, and each scenario lets you decide whether a requirement is met.
arc42:
- 10
- 1
step: s04-quality-requirements
related:
- quality-attribute-scenario
- iso-iec-ieee-42010-architecture-description-standard
- iso-iec-25010-quality-model
- arc42-introduction-and-goals
- quality-attribute
- architecture-tradeoff-analysis-method-atam
- arc42-documentation-template
checks:
- Quality requirements are written as scenarios concrete enough to decide whether each one is fulfilled.
- The most important quality requirements are only referenced in chapter 10, because they are described
  in section 1.2.
- A quality tree starts with the generic term quality at its root and refines it into categories or topics.
- Usage scenarios describe the runtime reaction to a stimulus, and change scenarios describe the effect
  of modifying or extending the system.
sources:
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: 'A small quality tree: quality at the root, categories below, scenarios at the leaves.'
review:
  status: generated
  flags: []
---

## Explanation

Chapter 10 of the arc42 template holds the quality requirements of a system. A vague wish such as "the system should be fast" cannot be checked. Quality scenarios fix that. They make a requirement specific enough that you can decide whether it is fulfilled.

**Quality tree**

The chapter can start with a quality tree. The tree puts the generic term "quality" at its root and refines it step by step. One way to build the branches is to use categories or topics. arc42 suggests ISO 25010:2023 or Q42 as sources for them. ISO/IEC 25010 defines a product quality model with nine quality characteristics. It serves as a basis for evaluating software quality. The article on the ISO/IEC 25010 Product Quality Model has details.

**Quality scenarios**

Scenarios describe the individual requirements. This article covers two kinds:

- Usage scenarios describe how the system reacts at runtime to a certain stimulus. A stimulus is an event that hits the system.
- Change scenarios describe the desired effect of changing or extending the system or its immediate environment.

**Short and long forms**

arc42 offers a short scenario form (Q42). A long form also exists. The SEI and Bass et al. favor it. It is more detailed and has more elements, such as an ID, a stimulus and a response measure. The Quality Attribute Scenario article covers this idea.

**Link to chapter 1**

The most important quality requirements are already described in section 1.2, the quality goals. Chapter 10 therefore only references them. See arc42 Introduction and Goals for the goals themselves.

## Example

A team documents a web shop. The quality tree has the root "quality" and a branch called "performance". Under that branch sits one usage scenario: a customer opens the product page (the stimulus), and the system shows it within a stated time (the response and its measure). A second branch, "changeability", holds a change scenario: the team adds a new payment method, and the effort stays within a stated limit. The top two goals are already in section 1.2, so chapter 10 only points to them.

## Trade-offs

The long form is more detailed and has more elements, such as an ID, a stimulus and a response measure. The top goals from section 1.2 are only referenced in chapter 10.
