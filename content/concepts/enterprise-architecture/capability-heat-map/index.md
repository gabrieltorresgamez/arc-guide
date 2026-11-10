---
title: Capability Heat Map
slug: capability-heat-map
category: enterprise-architecture
kind: practice
summary: A capability heat map colors a map of business capabilities by assessment scores, such as maturity
  or strategic importance. It shows where to act and supports decisions about roadmaps.
arc42:
- 4
- 11
step: s12-evolve
related:
- business-capability-map
- business-capability
- capability-map-use-cases
- capability-map-development-method
- enterprise-architecture-strategy
- adaptability
checks:
- Each heat map states its purpose, scoring method, audience and how to interpret it.
- The meaning of each color is explicit, and the underlying scores are available.
- Assessment data records dates, reviewers and sources.
- Ratings do not rely only on expert opinion.
sources:
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
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A business capability map lists what an organization can do, arranged in a hierarchy (see the article Business Capability Map). A capability heat map adds assessment values to that hierarchy. Each capability gets a color that reflects its score.

**What it is for**

The heat map supports decisions. It is not decoration. It also works as a starting point for strategic planning and for roadmap requirements.

**What you can assess**

Common aspects include:

- strategic importance
- adaptability
- maturity, covering people, process, information and technology

The same map view works for each aspect. You only change the scores behind it.

**Scoring examples**

- Maturity can use the five levels of CMMI. These levels rest on process efficiency, IT support level and staffing.
- Strategic importance can use VRIO criteria.

**What each heat map needs**

Define these four things before you publish:

1. A clear purpose.
2. A scoring method.
3. An audience.
4. A guide to reading the map.

If you use color, state what each color means. Keep the underlying scores available, so readers can check them.

**Keeping scores trustworthy**

Record dates, reviewers and sources for each assessment. This protects against stale and subjective scores.

## Example

A company maps its capabilities and scores each one for maturity. Its map uses three colors, and each color has a written meaning. The score table sits next to the map. The team shows the map to the planning board. The board sees which capabilities score lowest and discusses them first. Each score carries a review date and a named reviewer. Next quarter, the team can see which scores are old.

## Trade-offs

- **Subjectivity:** Ratings based only on expert opinion are personal and hard to defend. Use a defined scoring method and record sources.
- **Effort:** A broad, detailed assessment across the whole enterprise often costs too much effort. Limit the number of statements you assess per aspect to keep the work manageable.
- **Stale data:** Scores without dates and reviewers can age unnoticed.
