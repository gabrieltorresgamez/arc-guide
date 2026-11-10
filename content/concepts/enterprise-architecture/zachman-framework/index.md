---
title: Zachman Framework
slug: zachman-framework
category: enterprise-architecture
kind: framework
summary: The Zachman Framework is a grid that sorts the descriptions of an enterprise. It is a structure,
  not a process. Each cell holds one kind of description for one audience.
arc42:
- 1
- 12
step: null
related:
- enterprise-architecture-management
- togaf
- architecture-view
- architecture-viewpoint
- stakeholder-perspective-and-concern
- common-features-of-architecture-frameworks
- architecture-view-model
checks:
- The document states which framework cells are formalized and which are deliberately left out, with the
  risk accepted.
- Each framework cell describes only one type of thing.
- The framework is used as a classification structure, and the order of work and tools are defined separately.
sources:
- url: https://zachman-feac.com/zachman/about-the-zachman-framework
  title: About the Zachman Framework - Zachman International - FEAC Institute
  site: zachman-feac.com
  accessed: '2026-11-09'
- url: https://www.brcommunity.com/articles.php?id=c066
  title: 7 Common Myths (Plus 1) About the Zachman Architecture Framework (Commentary)
  site: brcommunity.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Zachman_Framework
  title: Zachman Framework - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Zachman Framework is a way to classify the descriptions of an enterprise. Its author calls it an ontology, meaning a structure. He says it is not a methodology, which would be a process. It tells you what kinds of descriptions exist. It does not tell you how to make them.

**The grid.** The framework is a matrix. The columns are communication questions, called interrogatives. The rows are transformations (reifications) of an idea for different audiences. Six question types times six audiences gives 36 cells.

**Rows are audiences, not detail levels.** Each row transforms the previous row into a new form for a new audience. A lower row is not just a more detailed copy of the one above.

**One thing per cell.** Each cell classifies exactly one type of thing. Each cell can vary independently of every other cell.

**Where it came from.** The author saw that "architecture" was used loosely in information systems. He looked to classical architecture and engineering. There he found architectures on many levels, seen from several perspectives. The structure was also observed in the descriptions of built products such as buildings and airplanes.

**No prescribed order.** The framework sets no order for doing architecture work. Order, tools, and starting point are methodological choices. They sit outside the framework.

**Skipping cells has a cost.** Choosing not to formalize a cell, or part of one, creates enterprise risk.

## Example

A company wants to understand its order handling. The team lists which cells of the grid it has filled. It has a description of the data for the business owners. It has no description of the people and roles for the builders. The empty cell shows a gap. The team then decides to fill it or to accept the risk knowingly.

## Trade-offs

Filling every cell costs time and money. Skipping a cell saves effort but creates enterprise risk. The framework does not say where to start or which tools to use. You must make those choices yourself, with a method of your own.
