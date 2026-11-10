---
title: Operating Model
slug: operating-model
category: enterprise-architecture
kind: concept
summary: An operating model describes how a company delivers value. It sets the needed level of process
  standardization and integration, and that level tells architects which process and IT capabilities matter
  most.
arc42:
- 1
- 4
step: s07-solution-strategy
related:
- enterprise-architecture-management
- enterprise-architecture-ross-weill-robertson-definition
- foundation-for-execution
- business-capability
- enterprise-architecture-strategy
- business-model-canvas
- as-is-and-to-be-view
- business-architecture
checks:
- The document states how much process standardization and integration the business needs.
- Critical IT and business process capabilities are derived from the operating model, not from strategy
  alone.
- The operating model is kept separate from the business model and describes only how value is delivered.
- A target operating model, if present, is labeled as the future-state view.
sources:
- url: https://cisr.mit.edu/publication/2005_12_3C_OperatingModels
  title: 'Forget Strategy: Focus IT on Your Operating Model | MIT CISR'
  site: cisr.mit.edu
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Operating_model
  title: Operating model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://lethain.com/notes-on-enterprise-architecture-as-strategy/
  title: Notes on Enterprise Architecture as Strategy | Irrational Exuberance
  site: lethain.com
  accessed: '2026-11-09'
- url: https://cisr.mit.edu/research-library/glossary
  title: CISR Glossary | MIT CISR
  site: cisr.mit.edu
  accessed: '2026-11-09'
- url: https://cisr.mit.edu/publication/enterprise-architecture-as-strategy
  title: 'Enterprise Architecture as Strategy: Creating a Foundation for Business Execution | MIT CISR'
  site: cisr.mit.edu
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An operating model describes how an organization delivers value. It is narrower than the business model, which covers the business as a whole. The operating model deals only with the delivery side.

**Why it matters.** Strategy alone rarely gives clear enough direction for stable IT and process capabilities. A defined operating model fills that gap. It also lets IT act proactively.

**Two dimensions.** The operating model sets the level of business process integration and standardization the company needs. That level decides which IT and business process capabilities are critical.

- *Standardization* means running different business units the same way.
- *Integration* means one unit depends on other units' data being available, accurate and timely.

**Four types.** Facts cover how the types differ in focus:

- *Replication* focuses on process standardization.
- *Coordination* focuses on integration.
- *Diversification* is a decentralized organizational design.
- *Unification* is a centralized organizational design.

**Link to enterprise architecture.** Enterprise architecture (see the article Enterprise Architecture) is the organizing logic for business processes and IT infrastructure. The operating model is the firm's vision of how it will survive and grow. Enterprise architecture implements that vision.

**Target operating model.** A target operating model is the future-state view of an operating model. It shows the model at a later point in time.

## Example

A retail group runs shops in several countries. Its leaders decide every shop must run checkout and restocking the same way. That is a high need for standardization. The shops do not rely on each other's data, so the need for integration stays low. Architects then treat shared, uniform checkout and restocking processes as critical capabilities. They build IT around those first.

## Trade-offs

Strategy alone is too vague to steer IT, so an operating model adds needed direction. But it forces a choice about how much to standardize and integrate. Standardization means units give up their own ways of working. Integration means units depend on each other's data quality and timeliness.
