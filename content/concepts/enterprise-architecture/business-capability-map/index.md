---
title: Business Capability Map
slug: business-capability-map
order: 30
category: enterprise-architecture
kind: artifact
summary: A business capability map lists what a business must be able to do, in a few levels, without
  saying how or by whom. It stays stable for years while processes, systems and teams change.
arc42:
- 1
- 3
- 4
step: s06-domain
related:
- business-capability
- business-architecture
checks:
- Each capability states what the business must be able to do, not how it is done or who does it.
- The map has about seven to ten level-1 capabilities and uses three levels or fewer.
- The map was drafted from strategic documents such as annual goals, roadmaps or investment themes.
- The map has a review schedule, at least once a year.
- Capabilities change only when the business model changes, not when teams, processes or applications
  change.
sources:
- url: https://www.leanix.net/en/wiki/ea/how-to-create-a-business-capability-map
  title: How to Create a Business Capability Map? | SAP LeanIX
  site: leanix.net
  accessed: '2026-11-09'
- url: https://www.leanix.net/en/wiki/ea/best-practices-to-define-business-capabilities
  title: Best Practices to Define Business Capability Maps | SAP LeanIX
  site: leanix.net
  accessed: '2026-11-09'
- url: https://www.ardoq.com/knowledge-hub/business-capability-map
  title: 'Business Capability Map: The Essential Guide With Examples'
  site: ardoq.com
  accessed: '2026-11-09'
- url: https://if4it.org/best-practices/designing-building-and-maintaining-comprehensive-and-usable-enterprise-capability-models/use-enterprise-capability-models-for-assessment-health-checks-and-heatmaps/
  title: Use Enterprise Capability Models for Assessment, Health Checks, and Heatmaps - Designing, Building,
    and Maintaining Comprehensive and Usable Enterprise Capability Models | The International Foundation
    for Information Technology (IF4IT)
  site: if4it.org
  accessed: '2026-11-09'
- url: https://www.boc-group.com/en/blog/ea/how-to-assess-your-business-capabilities/
  title: Business Capability Assessment with ADOIT
  site: boc-group.com
  accessed: '2026-11-09'
- url: https://bizzdesign.com/blog/how-to-measure-business-capability-aspects
  title: How to measure business capability aspects /image/how-measure-business-capabilitywebp
  site: bizzdesign.com
  accessed: '2026-11-09'
- url: https://albumi-docs.pages.dev/concepts/business-capabilities/
  title: Business Capabilities | Albumi Docs
  site: albumi-docs.pages.dev
  accessed: '2026-11-09'
- url: https://www.brcommunity.com/articles.php?id=b927
  title: 'Developing your Capability Architecture: It''s All about Being Able to Get Things Done (Commentary)'
  site: brcommunity.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/Azure/architecture/guide/architecture-styles/microservices
  title: Microservices Architecture Style - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://www.bpminstitute.org/resources/articles/capability-mapping-efforts-not-getting-you-your-destination/
  title: Capability mapping efforts not getting you to your destination? | BPMInstitute.org
  site: bpminstitute.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Business_capability
  title: Capability management in business - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://bizzdesign.com/blog/business-capabilities-a-complete-guide
  title: 'Business Capabilities: Definition, Examples & Capability Map'
  site: bizzdesign.com
  accessed: '2026-11-09'
- url: https://acorn.works/blog/business-capability-heat-map
  title: Using a Business Capability Heat Map in Business Strategy | Acorn
  site: acorn.works
  accessed: '2026-11-09'
- url: https://if4it.org/best-practices/designing-building-and-maintaining-comprehensive-and-usable-enterprise-capability-models/avoid-common-capability-modeling-pitfalls/
  title: Avoid Common Capability Modeling Pitfalls - Designing, Building, and Maintaining Comprehensive
    and Usable Enterprise Capability Models | The International Foundation for Information Technology
    (IF4IT)
  site: if4it.org
  accessed: '2026-11-09'
- url: https://www.leanix.net/en/blog/business-capabilities-vs-business-processes-whats-the-difference
  title: 'Business Capabilities vs Business Processes: What’s the Difference?'
  site: leanix.net
  accessed: '2026-11-09'
- url: https://www.ardoq.com/knowledge-hub/value-streams
  title: Differences Between Business Capabilities, Processes, & Value Streams
  site: ardoq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A generic three-level capability map as a hierarchy.
review:
  status: generated
  flags: []
---

## Explanation

A business capability is something the business must be able to do. It says nothing about how the work is done or who does it [src:1].

A capability map arranges these capabilities in a hierarchy. Maps usually have seven to ten level-1 capabilities. Three levels are typically enough for enterprise analysis. The aim is traceability without overcomplication.

**Stable by design**

Capabilities stay stable for years. Processes, systems and organizational structures change around them. So update a capability only when the business model changes. Do not update it because a team, a process or an application shifts.

**What it is not**

- *Process model:* a capability does not describe activities, workflows or systems. It describes what is needed [src:15].
- *Org chart:* org charts change often. Capabilities should stay stable.

**Building a first draft**

Start from strategic documents. Examples are annual goals, transformation roadmaps and investment themes.

**Keeping it sound**

Treat the map as a living asset. Review it regularly, at least once a year.

For related ideas, see the article Business Capability.

**More about capability maps.**

- **Capability Heat Map:** A capability heat map colors a map of business capabilities by assessment scores, such as maturity or strategic importance. It shows where to act and supports decisions about roadmaps.
- **Capability Identification and Naming:** A business capability says what a business does, not how it does it. Identify capabilities that stay stable over time, and name them with nouns or gerunds, not verbs.
- **Capability Map Development Method:** Build a capability map in steps: set its purpose, keep it shallow, name owners, and describe what the business does rather than how. Capabilities should not overlap and should stay stable for years.
- **Capability Map Use Cases:** A capability map shows what a business does. Teams use it to plan strategy, find gaps and overlaps, set investment priorities, and decide where to focus resources and projects.
- **Capability versus Process:** A capability says what an organization can do. A process says how the work gets done, step by step. Keep the two apart and link them, because capabilities stay stable while processes change.

## Example

A small online retailer drafts its map from its annual goals. Level 1 has areas such as "Customer", "Product" and "Finance". Under "Customer", level 2 might hold "Customer Service". A level-3 capability there could be "Handle Complaints".

Later the retailer moves complaints to a new team and buys a new ticket tool. The capability "Handle Complaints" does not change. Only the team and the tool change.

## Trade-offs

Keeping the map abstract and stable means it does not show how work flows or who does it. You need process models or org charts for that. Adding more levels gives more detail but works against the aim of avoiding overcomplication. A map that is never reviewed stops matching the business.
