---
title: Requirements Trawling
slug: requirements-elicitation
category: functional-requirements
kind: practice
summary: Requirements trawling means gathering requirements with several techniques, expecting that you
  will not find them all. Some requirements are overlooked and some only appear during building, so teams
  look actively and early.
arc42:
- 1
- 10
step: s03-functional-requirements
related:
- user-story
- method-phase-working-with-functional-requirements
- requirement-types-and-documents
- requirements-difficulty-and-customer-engagement
- stakeholder
- solution-as-moving-target
- story-mapping
- architecturally-significant-requirement
checks:
- The document shows that requirements were gathered with more than one technique, such as interviews,
  observation, questionnaires or workshops.
- The document looks beyond what users stated and notes how overlooked requirements were sought.
- The document accepts that requirements are incomplete and will change, and does not claim a complete
  specification.
- The document states how emergent requirements will be found early, for example with working product
  in users' hands.
sources:
- url: https://www.mountaingoatsoftware.com/agile/the-three-types-of-requirements
  title: 'Agile Requirements Gathering: Three Types of Requirements - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/books/user-stories-applied
  title: User Stories Applied - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/mastering-requirements-process/
  title: 'Interview and Book Excerpt: Mastering the Requirements Process - InfoQ'
  site: infoq.com
  accessed: '2026-11-09'
- url: https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/6074/The-6-Most-Important-Requirements-Practices.aspx
  title: The 6 Most Important Requirements Practices
  site: modernanalyst.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/services/story-writing-workshop
  title: Story Writing Workshop - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

**Known and overlooked requirements.** Users tell you about some requirements. These are the known ones. Other requirements are overlooked, yet they matter just as much. Teams can often do better at reducing how many of them there are.

**Emergent requirements.** Some requirements only surface while the team builds the product. No up-front technique can find them. The advice is to look for them as early as possible, and to prioritize the risky parts of the system so the team can get working product to users.

**Gathering techniques.** Techniques for gathering known requirements include:

- user interviews,
- questionnaires,
- observation,
- workshops, such as a story-writing workshop,
- open-ended questions.

**No complete specification first.** However carefully a team prepares requirements, they will not be perfect, complete or static. Change is expected. Separately, the Robertsons say their Volere approach does not demand finding every requirement and writing a complete specification up front, though the team must be able to demonstrate the essence of the problem.

For how gathered needs are written down as stories, see the User Story article.

## Example

A team builds an ordering app for a bakery. They interview the owner and send a short questionnaire to regular customers. They also watch staff at the counter during the morning rush. Staff never mentioned a daily paper list of special orders, but the team sees it in use. That is an overlooked requirement. After the first release, customers ask for pickup-time slots. Nobody could have named that earlier, so the team treats it as an emergent requirement and keeps looking.

## Trade-offs

No gathering technique can uncover emergent requirements: they stay hidden until the team builds something and puts it in front of users. Teams can reduce overlooked requirements by asking better questions and listening more actively.
