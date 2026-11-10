---
title: Warning Signs of Poor Enterprise Architecture
slug: warning-signs-of-poor-enterprise-architecture
category: enterprise-architecture
kind: concept
summary: Poor enterprise architecture shows up as duplicated capabilities, little reuse, fragile system
  connections, and workarounds. Typical causes are rewarded local optimization and no shared inventory
  of capabilities.
arc42:
- 1
- 11
step: s01-goals-stakeholders
related:
- enterprise-architecture-management
- business-capability-map
- business-capability
- togaf
- undetected-duplication-antipattern
- enterprise-architecture-maturity-levels
- technical-debt
- unsystematic-accidental-architecture
checks:
- The document or an inventory lists existing business capabilities, so teams can find and reuse them
  instead of rebuilding.
- The number of point-to-point interfaces between systems is known and kept under control.
- Known workarounds (kludges) are recorded as risks rather than left implicit.
- Redundant systems, for example after a merger, have a plan to share information or consolidate.
sources:
- url: https://www.thoughtworks.com/en-us/insights/articles/capability-gap-visibility-problem
  title: Capability gap or a visibility problem? | Thoughtworks United States
  site: thoughtworks.com
  accessed: '2026-11-09'
- url: https://www.cio.com/article/230483/9-warning-signs-of-bad-it-architecture.html
  title: 9 warning signs of bad IT architecture | CIO
  site: cio.com
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/TOGAF-enterprise-architecture/
  title: How the TOGAF Standard Serves Enterprise Architecture - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How common root causes lead to duplication and fragile systems.
review:
  status: generated
  flags: []
---

## Explanation

Enterprise architecture (see "Enterprise Architecture") describes how an organization's business and IT fit together. When it is weak or missing, the effects show up in daily work. The signs below work as a checklist.

**Duplicated capabilities.** Different teams build the same business capability again and again, in slightly different forms. A business capability is something the organization can do, such as verifying a customer's identity.

**Disconnected systems and inconsistent solutions.** Without an enterprise architecture practice, there could be disconnects between systems and inconsistencies in solutions.

**Fragile connections.** Many point-to-point interfaces (direct links between two systems) make a landscape fragile. The more interfaces there are, the more fragile the architecture and the harder it is to maintain, though interfaces are better than having none.

**Kludges.** A kludge is a quick workaround. It fixes today's problem but leaves a fragile system behind.

**Redundant systems after mergers.** When two companies merge, their overlapping systems must share information or be consolidated. This exposes the missing shared architecture.

**Root causes**

- Duplication is the default when reuse takes more effort than building new.
- Organizations reward local optimization, where each unit improves only its own area. This leads to fragmentation.
- No authoritative, up-to-date inventory of capabilities exists. Without one, nobody can find what already exists or see gaps. A capability map (see "Business Capability Map") that is typically outdated and ignored has not prevented fragmentation from recurring.

**Why it matters.** One author argues that leveraging a mature standard such as TOGAF (see "TOGAF") offers a better return on investment, less risk of future redundant spending, and faster, cheaper procurement. Spotting these symptoms early helps make the case for such a practice.

## Example

A bank has three business units. Each built its own customer identity check. They behave slightly differently. A new product team needs one, finds no list of existing ones, and builds a fourth. Meanwhile the units link their systems with many direct interfaces and patch gaps with quick scripts. Every change now risks breaking something. A shared capability inventory would have shown the existing checks.

## Trade-offs

This article covers only a subset of symptoms: duplication, fragility, and mergers. Other signs, such as slow regulatory response or manual data transfer, are not covered. A symptom also does not prove one single cause. Treat the list as a prompt for investigation, not a verdict.
