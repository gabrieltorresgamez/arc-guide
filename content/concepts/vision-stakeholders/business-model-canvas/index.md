---
title: Business Model Canvas
slug: business-model-canvas
category: vision-stakeholders
kind: artifact
summary: 'The Business Model Canvas describes a business on one page in nine blocks: who it serves, what
  it offers, how it delivers, what it costs and what it earns. Architects read it to understand the business
  behind a system.'
arc42:
- 1
step: s01-goals-stakeholders
related:
- arc42-introduction-and-goals
- stakeholder-identification
- stakeholder
- vision-statement
- architecture-canvas
- business-architecture
- bounded-context-canvas
- business-domain-understanding
checks:
- The stakeholder overview names the customers and partners that appear in the business model.
- If a canvas is cited, it is dated and versioned.
- The introduction lists only the top 3-5 quality goals.
sources:
- url: https://www.strategyzer.com/library/the-business-model-canvas
  title: Business Model Canvas – Download the Official Template
  site: strategyzer.com
  accessed: '2026-11-09'
- url: https://www.strategyzer.com/library/5-questions-business-mode-canvas
  title: 5 Questions You Never Dared to Ask About the Business Model Canvas
  site: strategyzer.com
  accessed: '2026-11-09'
- url: https://www.strategyzer.com/library/what-is-a-business-model
  title: What is a Business Model?
  site: strategyzer.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Business_Model_Canvas
  title: Business model canvas - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://arc42.org/resources/canvas-101/
  title: Canvas 101 - arc42
  site: arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Business Model Canvas is a one-page template. It splits a business model into nine blocks. Together they cover five questions: what it costs, what it earns, how you deliver it, what you offer and who you serve.

The nine blocks are:

- value proposition
- customer segments
- channels
- customer relationships
- key resources
- key activities
- key partners
- revenue streams
- cost structure

Short descriptions of each block work well as guiding questions. For example, revenue streams ask how the company earns income from each customer segment.

**Layout.** Strategyzer explains the layout with a theater analogy. Revenue needs a customer who pays for a value proposition. In the analogy, there is no revenue without a great play and no play without backstage infrastructure.

**Blocks depend on each other.** If you move a customer segment, the channels, activities and costs must move with it. Read the canvas as one connected whole, not nine separate lists.

**How to use it.** Strategyzer gives this advice:

- Use one canvas per business model.
- Treat the canvas as a hypothesis.
- Date and version it.
- Redraw it as evidence arrives.

**Related tools.** Lean Canvas is an adaptation for startups. The Value Proposition Canvas is a later, related tool by the same authors. arc42 lists the Business Model Canvas as the classic canvas for business models.

**Use in architecture documentation.** arc42 section 1 asks for an explicit overview of stakeholders. These are all parties involved in the system or affected by it. Section 1 also limits quality goals to the top 3-5 and separates architecture quality goals from project goals. See *arc42 Introduction and Goals* for details.

## Example

A small online bakery fills in a canvas. Its customer segment is office workers. Its value proposition is fresh bread delivered before work. Partners include a delivery service. When the bakery adds a second segment, restaurants, the team redraws the canvas. Channels, activities and costs change too. The architect then lists office customers, restaurants and the delivery partner as candidate stakeholders.

## Trade-offs

The canvas is static. It says little about how parts interact or about the environment. Because the canvas is a hypothesis, its content can change as evidence arrives.
