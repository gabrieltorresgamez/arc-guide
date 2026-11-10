---
title: arc42 Glossary
slug: arc42-glossary
category: documentation
kind: artifact
summary: The arc42 glossary is section 12 of the template. It lists the key domain and technical terms
  stakeholders use, so everyone means the same thing by the same word.
arc42:
- 12
step: s06-domain
related:
- ubiquitous-language
- domain-model
- domain-driven-design
- arc42-documentation-template
- stakeholder
- bounded-context
checks:
- The glossary lists the key domain and technical terms that stakeholders use when discussing the system.
- Glossary terms match the domain model used in the software.
- A named person, such as the product owner or project manager, is responsible for the glossary.
- The glossary is updated as the team's understanding of the domain changes.
sources:
- url: https://docs.arc42.org/section-12/
  title: 12 - Glossary | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UbiquitousLanguage.html
  title: Ubiquitous Language
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Section 12 of arc42 is the glossary. It collects the most important domain and technical terms that stakeholders use when they talk about the system.

**Why it exists.** Clearly defined terms let all stakeholders share an identical understanding of them and avoid synonyms and homonyms.

**Link to ubiquitous language.** Domain-Driven Design has a related practice, the ubiquitous language (see the article Ubiquitous Language): a common, rigorous language between developers and users. Fowler, building on Evans, says the language should be based on the domain model that the software uses. The article Domain Model explains that model.

**Keeping it alive.** The language evolves as the team's understanding of the domain grows. arc42 suggests making the product owner or the project manager responsible for the glossary.

**What to put in.** Add the terms your stakeholders actually use. Give each one a clear definition.

## Example

A team builds a system for a library. Developers say "loan" for a book checkout. Staff use "loan" only for borrowing from another library. The glossary lists "loan" with one clear definition, and gives the other case its own term. The code then uses the same names. The product owner updates the entries when staff change how they work.


