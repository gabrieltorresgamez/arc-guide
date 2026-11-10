---
title: 'Step 6: Understand and structure the domain'
id: s06-domain
review:
  status: generated
  flags:
  - unsupported:The ClinicBook context names, classifications, entities and rules are invented for the
    fictional example.
  - unsupported:A small team may own several related contexts at first; the articles only say no team
    should own several unrelated contexts.
  - unsupported:Reminders consuming Booking events, with Booking upstream, is an example design choice,
    not taken from an article.
---

## What you get from this step

- A shared vocabulary that developers and business people both use.
- A list of bounded contexts. A [bounded context](concept:bounded-context) is a boundary inside which one domain model applies.
- A context map that shows how those contexts relate.
- A first sketch of the important data, in business terms only.
- Material for two arc42 sections: section 12 (glossary) and section 5 (building blocks).

## What you need first

- A short description of what the system must do and for whom.
- Access to people who know the business. These are your domain experts.
- A first view of the outside world: which people and external systems exchange data with your system. [Business Domain Understanding](concept:business-domain-understanding) calls this the business context.

## If something is missing

- **No domain expert available.** Ask the people who do the work today. Use [Domain Storytelling](concept:domain-storytelling): they tell how they work, and you draw each story as actors, work objects and activities.
- **No glossary yet.** Start an empty one now. You will fill it in step 2 below.
- **Unclear what the business does at the top level.** Write a small [business capability map](concept:business-capability-map). A capability says what the business can do, not how.
- **Open questions pile up.** Write them down. The [Bounded Context Canvas](concept:bounded-context-canvas) treats many open questions as a sign of high uncertainty.

## How to do it

1. **Collect the business words.** Listen to the domain experts and write down the terms they use. Use their words, not your own. Read [Ubiquitous Language](concept:ubiquitous-language) for why one shared vocabulary matters. If you run Domain Storytelling sessions, label each story as as-is or to-be and as overview or detailed. Keep the experts' own terms on the pictures.
2. **Start the glossary.** Put the key domain and technical terms into arc42 section 12. Follow [arc42 Glossary](concept:arc42-glossary). Name one person who owns it, such as the product owner. Plan to update it as you learn more.
3. **Hunt for words with several meanings.** Words like "Customer" or "Product" often mean different things to different groups. Do not merge the meanings. Write each one down, as [Business Domain Understanding](concept:business-domain-understanding) suggests.
4. **Split the domain into bounded contexts.** Where meanings truly differ, give each meaning its own context. [Reflecting the Business Domain in the Architecture](concept:reflecting-the-business-domain-in-the-architecture) explains why you split instead of forcing one model. For each context:
   - Give it a name the team agrees on.
   - State its purpose in a few sentences of business language.
   - Classify it as core, supporting or generic.
   - Note assumptions and open questions.

   Treat boundaries taken from stories as indications, not proof.
5. **Draw a context map.** Show how the contexts relate, including external systems. Follow [Context Map](concept:context-map). Explain every arrow. Say which side is upstream (provides) and which is downstream (consumes). Label each relationship with a named pattern. Use customer-supplier only if the downstream side can influence the upstream side.
6. **Look inside each context.** Find the main objects and their roles:
   - [Entity](concept:entity): defined by its identity. Its attributes can change.
   - [Value Object](concept:value-object): no identity, immutable, equal when all values match.
   - [Aggregate](concept:aggregate): a group treated as one unit, with one root as the only entry point. Other aggregates are referenced by identity.
   - [Domain Event](concept:domain-event): something that happened, named in the past tense.

   Where a concept has a life cycle that matters to the business, sketch its states. See [Entity Life Cycle](concept:entity-life-cycle).
7. **Sketch the important data.** Draw a conceptual data model with entities, attributes, relationships and business rules. State for each relationship its cardinality (how many) and whether it is mandatory or optional. Leave out data types, tables and indexes. See [Conceptual data model building method](concept:conceptual-data-model-building-method) and [Conceptual Data Model](concept:conceptual-data-model). Show it to business stakeholders and record the gaps they find. [Conceptual Data Model Preparation for Logical and Physical Models](concept:conceptual-data-model-preparation-for-logical-and-physical-models) explains how the checked model is handed on to later modeling.
8. **Note privacy and ownership.** Mark which data is sensitive and which system holds the master data. [Data Architecture](concept:data-architecture) asks you to name the database of record and to identify privacy and security aspects.
9. **Turn the contexts into building blocks.** Group concepts that belong together. Mark external systems as external and put a translating wrapper between them and your own components. See [Deriving System Components from the Domain Model](concept:deriving-system-components-from-the-domain-model). Record the result in arc42 section 5.
10. **Expect to revise.** The model improves as the team learns. Change model and code together. See [Iterative Domain Modeling](concept:evolutionary-domain-modeling).

## Example: ClinicBook

ClinicBook is the online booking system for 40 small practices.

**Words and conflicts.** The team talks to practice staff and collects: patient, appointment, slot, practice, calendar, reminder. "Patient" turns out to mean two things. In ClinicBook's booking flow, a patient is a person with an account who books. In a practice's own software, a patient is a full medical record. The team writes both meanings into the glossary (arc42 section 12). The product owner owns the glossary.

**Bounded contexts.** The team proposes these, with a purpose and a class for each:

| Context | Purpose (business language) | Class |
|---|---|---|
| Booking | Patients find, book, move and cancel appointments. | Core |
| Practice Calendar | Staff manage when they are available. | Core |
| Reminders | Patients get told about upcoming appointments. | Supporting |
| Practice Software Link | Appointment data stays aligned with each practice's own software. | Supporting |

Open questions go on the canvas. One example: do all 40 practices define a "slot" the same way? The team has a small team, so one team may own several of these contexts at first. It writes the owner of each down and keeps the owned contexts related.

**Context map.** The practice-management software is external, and it comes from different vendors. ClinicBook cannot influence it, so the team does not label that link customer-supplier. A translating wrapper in Practice Software Link keeps the vendors' models out of ClinicBook's own contexts. Booking is upstream of Reminders. Reminders consumes booking events and sends them by SMS and e-mail. The team explains each arrow in the diagram's legend.

**Inside Booking.**
- *Appointment* is an entity. Its identity is an appointment id. Its life cycle is requested, booked, moved or cancelled, then completed. A cancelled or completed appointment cannot change.
- *Time slot* (start and end) is a value object. To move an appointment, the team replaces the slot with a new one.
- *Appointment* is also the aggregate root. It refers to the patient and the practice by identity only.
- *AppointmentCancelled* is a domain event, named in the past tense. Reminders reacts to it so that no reminder goes out for a cancelled visit.

**Data sketch.** Entities: Patient, Practice, Appointment, Reminder. Each appointment belongs to exactly one patient and one practice. A patient has zero or more appointments. A business rule says one slot holds at most one appointment. The sketch has no data types or tables. The team marks which attributes are health data. Booking holds only the patient attributes it needs. The full medical record stays in the practice's own software.

**Building blocks.** The four contexts become the first candidates for level 1 blocks in arc42 section 5. The practice software is drawn as external and sits behind the wrapper.

## Done when

- Domain experts have reviewed a glossary with a named owner. It lists the key terms and explains the ones with several meanings. See [arc42 Glossary](concept:arc42-glossary).
- Terms that differ between groups are kept apart, not merged. See [Business Domain Understanding](concept:business-domain-understanding).
- Each bounded context has an agreed name, a business-language purpose and a core, supporting or generic class. See [Bounded Context Canvas](concept:bounded-context-canvas).
- A context map shows all contexts and external systems, with explained arrows and named patterns. See [Context Map](concept:context-map).
- Each aggregate has one root, and other aggregates are referenced by identity. See [Aggregate](concept:aggregate).
- A conceptual data model with cardinalities and business rules exists. It has no storage details, and business stakeholders have checked it. See [Conceptual Data Model](concept:conceptual-data-model).
- Building blocks follow the contexts, with external systems marked. See [Deriving System Components from the Domain Model](concept:deriving-system-components-from-the-domain-model).

## Learn more

- [Domain-Driven Design](concept:domain-driven-design)
- [Domain Model](concept:domain-model)
- [Domain-Driven Design of the Data Model](concept:domain-modeling-procedure)
- [Bounded Context](concept:bounded-context)
- [Domain Storytelling](concept:domain-storytelling)
- [Publishing the conceptual data model](concept:publishing-the-conceptual-data-model)
- [Entity and Value Object](concept:entity-vs-value-object)
- [Domain Event](concept:domain-event)
- [Conceptual, Logical and Physical Data Model](concept:conceptual-vs-logical-vs-physical-data-model)
- [Data Architecture](concept:data-architecture)
- [Business Capability Map](concept:business-capability-map)
- [Module](concept:module)
