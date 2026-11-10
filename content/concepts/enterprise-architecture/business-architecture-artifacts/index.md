---
title: Business Architecture Artifact
slug: business-architecture-artifacts
category: enterprise-architecture
kind: artifact
summary: Business architecture artifacts are maps and catalogues that describe an organization from the
  business side, such as strategy, capabilities, processes and customer journeys. They link strategy to
  the applications that support it.
arc42:
- 1
- 3
step: s01-goals-stakeholders
related:
- business-architecture
- business-capability-map
- business-capability
- capability-versus-process
- capability-heat-map
- strategy-map
- operational-value-stream
- enterprise-architecture-management
checks:
- Capabilities are described without people, process, data or technology, and are kept separate from processes.
- Applications are linked to the capabilities they support.
- Heat maps color capabilities by a stated criterion such as maturity.
- Strategy map objectives are linked causally across the four perspectives.
sources:
- url: https://bizzdesign.com/blog/business-capabilities-a-complete-guide
  title: 'Business Capabilities: Definition, Examples & Capability Map'
  site: bizzdesign.com
  accessed: '2026-11-09'
- url: https://www.grahamberrisford.com/00EAframeworks/03TOGAF/AMTOGpapers/Business%20architecture%20(inc%20capabilities%20and%20value%20streams)%20in%20TOGAF.htm
  title: ''
  site: grahamberrisford.com
  accessed: '2026-11-09'
- url: https://www.library.hbs.edu/working-knowledge/mapping-your-corporate-strategy
  title: Mapping Your Corporate Strategy | Working Knowledge
  site: library.hbs.edu
  accessed: '2026-11-09'
- url: https://www.nngroup.com/articles/journey-mapping-101/
  title: Journey Mapping 101 - NN/G
  site: nngroup.com
  accessed: '2026-11-09'
- url: https://bizzdesign.com/blog/business-architecture-redefined-mapping-bizbokr-archimater
  title: 'Business Architecture Redefined: Mapping BIZBOK® to ArchiMate®'
  site: bizzdesign.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How business artifacts link strategy to capabilities and applications.
review:
  status: generated
  flags: []
---

## Explanation

Business architecture artifacts are diagrams and lists that describe a business. For related ideas, see the articles Business Architecture and Business Capability Map.

**Strategy map.** A strategy map shows strategy as linked objectives. They sit in four balanced scorecard perspectives. Financial and customer objectives are the outcomes the organization wants. The links are causal, so managers can test whether the theory behind the strategy holds.

**Capability map.** A business capability describes what the business can do. The map groups capabilities into levels. It can also show which applications support them.

**Capabilities versus processes.** A process is a sequence of activities that produces a result of value for consumers. Teams, processes and applications work together to deliver a capability.

**Value stream diagram.** It represents activities in the end-to-end flow of a business process.

**Customer journey map.** It shows the process a person follows to reach a goal. Phases are high-level stages, and they vary by scenario. An emotion line across the phases shows where users are delighted or frustrated.

**Organization.** In BIZBOK, an Organization and a Business Unit map to the ArchiMate Business Actor. The overall BIZBOK mapping uses ArchiMate motivation, strategy, business, implementation and migration elements.

**Linking to IT.** Architects connect applications to capabilities. This helps them understand the business value of applications and make better decisions about how the application portfolio evolves. A heat map uses color to show how capabilities score against a criterion such as maturity or strategic importance. When teams compare these views, they can find the capabilities that matter most for a business goal and are furthest from where they need to be.

## Example

A regional retailer draws a strategy map. One customer objective is faster delivery. It then draws a capability map with a capability called "Order Fulfillment" and marks the applications that support it. A heat map shows how that capability scores on maturity. The team now sees where to focus software work.

 
