---
title: Domain Storytelling
slug: domain-storytelling
category: domain-driven-design
kind: method
summary: Domain Storytelling lets domain experts describe how they work, while the group draws each story
  as a simple picture of actors, work objects, and activities. The drawings help business and IT people
  share one language.
arc42:
- 1
- 3
- 12
step: s06-domain
related:
- ubiquitous-language
- bounded-context
- domain-driven-design
- business-domain-understanding
- arc42-glossary
- domain-model
- as-is-and-to-be-view
- requirements-elicitation
checks:
- Stories that feed the documentation are labeled with the domain experts' own terms.
- Each story states whether it describes the current process (as-is) or a future one (to-be).
- Each story states its level of detail (overview or detailed).
- Context boundaries taken from stories are labeled as indications, not proof.
sources:
- url: https://www.infoq.com/news/2018/02/storytelling-domain-contexts/
  title: Finding Bounded Contexts Using Domain Storytelling - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
- url: https://domainstorytelling.org/quick-start-guide
  title: Quick-Start Guide - Domain Storytelling
  site: domainstorytelling.org
  accessed: '2026-11-09'
- url: https://egon.io/
  title: Egon.io
  site: egon.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A tiny domain story: actors, work objects, and numbered activities.'
review:
  status: generated
  flags: []
---

## Explanation

Domain Storytelling is a way to learn how a business works. Domain experts describe their own work, and the group records it as a diagram.

**The picture language**

Each story is built from a few elements:

- **Actors** are the active participants. They are drawn as icons.
- **Work objects** are what actors create, work with, and exchange. Examples are documents, physical things, and digital objects. Each carries a domain term as its label.
- **Activities** are arrows labeled with a verb. Actors and work objects are nouns.
- **Sequence numbers** sit at the start of each activity arrow. They put the sentences in order.
- **Textual annotations** add what the picture cannot show. Examples are variations, term definitions, and assumptions.

**Scope and detail**

A story can describe the current process (as-is) or a possible future one (to-be). Granularity sets the level of detail, from overview to fine detail.

**The workshop**

Participants include domain experts, often from several departments, plus IT experts and a moderator. The group uses the participants' own words, not the facilitator's. The article Ubiquitous Language covers that idea.

**Tool support**

Egon.io supports the method. It is free and runs in the browser. It needs no account and does not store your data.

**Finding boundaries**

Stories can hint at where a bounded context ends. The article Bounded Context explains that term. These hints are indications, not proof.

## Example

A small online shop wants to understand how returns work. A customer service agent tells one concrete story, and the group draws it step by step:

1. The customer sends a return request.
2. The agent checks the order.
3. The agent sends a return label to the customer.

The customer and the agent are actors. The request, the order, and the label are work objects. A note beside step 2 records the shop's own definition of "valid order". The group uses the agent's words in every label.
