---
title: 'Step 8: Design integration and data'
id: s08-integration-data
review:
  status: generated
  flags:
  - unsupported:This step also touches arc42 sections 5 and 6 (taken from the guide brief; the articles
    do not say what goes in them).
  - unsupported:The 99.7% figure is my own arithmetic (0.999 cubed), not stated in an article.
  - unsupported:ClinicBook decisions (reminder channel, vendor translators, deferring CQRS and a canonical
    model, the highest classification for health data) are illustrative choices, not article content.
  - unsupported:The description of an anti-corruption layer as a translation layer is my paraphrase; the
    article only names it as an example and lists its costs.
---

## What you get from this step

You decide how your parts and the outside systems talk to each other. You also decide where each kind of data lives and who owns it.

You end up with:

- a list of connections, each with a chosen [integration style](concept:integration-pattern) and a reason for the choice;
- a decision for each connection: does the caller wait for the answer, or not?
- a simple model of your business data, with one place that holds the master copy of each item;
- notes on how you handle failures, duplicates and different data formats.

The business data model goes into arc42 section 8 as a cross-cutting concept (see [Define Target Data Architecture Method Phase](concept:define-target-data-architecture-method-phase)). This step also touches sections 5 and 6.

## What you need first

- A list of your own building blocks and of the external systems they must talk to.
- A list of the data your partners send or receive.
- The main business functions, in plain words (for example "book an appointment").
- Your quality needs that affect integration and data, such as availability and privacy.
- Your constraints, such as team size and deadline. They limit how much machinery you can afford.

## If something is missing

- **No list of external systems.** Ask the people who run the business. Write each system down with the data it exchanges. The [Application Interface Diagram](concept:application-interface-diagram) is a good place to collect this.
- **No list of business data.** Start with the [Conceptual data model building method](concept:conceptual-data-model-building-method). Understand the business first, then find the entities.
- **No quality needs.** Ask what happens when a connection is down for an hour. The answer tells you where you need to keep working during an outage.

## How to do it

1. **Draw the connections.** Draw each application and each link between them. Label every link with its technology, such as REST or FTP. Show dependencies, not just a list of applications. See [Application Interface Diagram](concept:application-interface-diagram).
2. **Pick an integration style per connection.** The classic styles are [File Transfer](concept:file-transfer), [Shared Database](concept:shared-database), [Remote Procedure Call](concept:remote-procedure-call) and [Messaging](concept:messaging). Prefer styles that keep the applications' dependence on each other low ([Principles Influencing EAI Pattern Selection](concept:principles-influencing-eai-pattern-selection)). Record the alternatives you considered and why you chose one.
3. **Decide synchronous or asynchronous.** A synchronous call makes the caller wait for the answer. An asynchronous call lets the caller move on ([Synchronous vs. Asynchronous Communication](concept:synchronous-vs-asynchronous-communication)).
   - For each synchronous call, write down what happens when the other side is down. Give it a timeout.
   - Compute the availability of a call chain as the product of its parts ([Synchronous vs Asynchronous Connector](concept:synchronous-vs-asynchronous-connector)).
   - Where a sender must keep working while the receiver is down, put a queue between them.
4. **Describe the messaging channels.** Where you use messaging, state for each [Message Channel](concept:message-channel) whether it is point-to-point (one receiver per message, see [Point-to-Point Channel](concept:point-to-point-channel)) or publish-subscribe (a copy for each subscriber, see [Publish/Subscribe Channel](concept:publish-subscribe-channel)). Assume a receiver may see a message twice. Say how it ignores the repeat ([Idempotent Receiver](concept:idempotent-receiver)). Add a [Dead Letter Channel](concept:dead-letter-channel) for messages that cannot be delivered, and name who watches it.
5. **Handle different formats and legacy systems.** Where two systems use different formats, name a [Message Translator](concept:message-translator) between them. For a legacy or external system, say how its meaning stays out of your design, for example with an anti-corruption layer ([Integration](concept:integration)). That layer is a translation layer. It adds latency and operations work. A [Canonical Data Model](concept:canonical-data-model) (one shared format) pays off only with many integrated applications.
6. **Build the conceptual data model.** List the entities (the business things you keep data about), their attributes, their relationships and the business rules. Leave out data types, tables and indexes ([Conceptual Data Model](concept:conceptual-data-model)). Check the model with business people and keep a glossary of terms. See [Conceptual Data Model Preparation for Logical and Physical Models](concept:conceptual-data-model-preparation-for-logical-and-physical-models) and [Publishing the conceptual data model](concept:publishing-the-conceptual-data-model).
7. **Decide where each entity lives.** Name exactly one system of record per entity. Give each entity a definition, an owner and a classification level ([Data Entity/Data Component Catalog](concept:data-entity-data-component-catalog)). Link the classification to handling rules such as encryption and access control. Use a CRUD matrix (create, read, update, delete) to see which function touches which entity ([Data Entity/Business Function Matrix](concept:data-entity-business-function-matrix)). If several applications hold the same data, name the master and the copies ([Application/Data Matrix](concept:application-data-matrix)).
8. **Leave storage details for later.** Database engines, indexes and partitioning belong in the physical model only ([Conceptual, Logical and Physical Data Model](concept:conceptual-vs-logical-vs-physical-data-model)).
9. **Add heavier patterns only with a reason.** [CQRS](concept:command-query-responsibility-segregation) splits reads from writes. Use it only where read volume far exceeds write volume, and accept that reads may be stale.
10. **Write it down.** Put the data model in arc42 section 8. Record each integration decision with its reason and its known risks.

## Example: ClinicBook

ClinicBook books appointments for 40 small practices. It must connect to practice-management software from different vendors. It must send SMS and e-mail reminders and protect health data. The team is small and the launch date is fixed.

**Connections.** The team draws web app, mobile app, booking service, reminder sender, SMS provider, e-mail provider and each vendor's practice software. Each link gets a technology label.

**Style per connection.**

- *Apps to booking service:* a synchronous call, because the patient waits for the answer. Each call has a timeout. The team multiplies the availabilities along the chain. For example, three links at 99.9% each give about 99.7%. That is a worse number than any single link.
- *Booking service to reminders:* messaging over a point-to-point channel. A booking must still succeed when the SMS provider is down. Each reminder is sent by one receiver only. The receiver is idempotent, so a repeated message does not send a second SMS. Failed messages go to a dead letter channel. One named developer checks it each morning.
- *Booking service to practice software:* the style depends on what each vendor offers. For a vendor with only a file export, the team uses file transfer. It writes down the file format and how often the file arrives. For a vendor with an API, it uses a remote call with a timeout.

**Different vendor formats.** Each vendor gets a translator and an anti-corruption layer, so vendor terms stay out of the booking model. The team does not introduce a canonical data model yet. It counts the vendor formats first. It will add the canonical model if the count grows.

**Data.** The conceptual model has Patient, Practice, Appointment, Calendar and Reminder. Relationships carry business rules, such as "an appointment belongs to one practice and one patient". The model has no tables or data types. Business and technical staff check it with practice staff. A glossary defines "appointment" and "slot".

The catalog gives each entity an owner and a classification. Patient and Appointment hold health data, so they get the highest level. That level requires encryption and tight access control. The team names one system of record per entity. Where a practice's own software also holds appointments, the team writes a mastering policy that names the master and the copies.

**CQRS.** The team considers it for the "free slots" search at morning peaks. It has no measured read volume yet. With a small team and a fixed launch date, it does not use CQRS at launch. It records this as a decision. It will revisit the decision if measurements show reads far above writes.

**Documentation.** The data model goes into arc42 section 8. The integration decisions are written down with their reasons and risks.

## Done when

- Every connection has a labeled technology and a chosen [integration style](concept:integration-pattern) with a recorded reason.
- Each connection states whether it is synchronous or asynchronous, and what happens when the other side is down ([Synchronous vs Asynchronous Connector](concept:synchronous-vs-asynchronous-connector)).
- Each messaging channel is marked point-to-point or publish-subscribe, and undeliverable messages have a [Dead Letter Channel](concept:dead-letter-channel) with a named watcher.
- Systems with different formats have a named [Message Translator](concept:message-translator), and legacy meaning is kept out of the new design ([Integration](concept:integration)).
- A [conceptual data model](concept:conceptual-data-model) exists, was checked with business people, and has a glossary.
- Every data entity has one system of record, an owner and a classification ([Data Entity/Data Component Catalog](concept:data-entity-data-component-catalog)).
- The data model is in arc42 section 8 ([Define Target Data Architecture Method Phase](concept:define-target-data-architecture-method-phase)).

## Learn more

- [Integration Style](concept:integration-pattern)
- [Integration](concept:integration)
- [Enterprise Integration Patterns](concept:messaging-pattern-language)
- [Integration Pattern vs. Middleware Technology](concept:integration-patterns-vs-middleware-technology)
- [Connect or Disconnect](concept:connect-or-disconnect)
- [Messaging](concept:messaging)
- [Message Channel](concept:message-channel)
- [Point-to-Point Channel](concept:point-to-point-channel)
- [Publish/Subscribe Channel](concept:publish-subscribe-channel)
- [Idempotent Receiver](concept:idempotent-receiver)
- [Invalid Message Channel](concept:invalid-message-channel)
- [Transactional Client](concept:transactional-client)
- [Synchronous vs. Asynchronous Communication](concept:synchronous-vs-asynchronous-communication)
- [Connectors and Distribution](concept:connectors-and-distribution)
- [Canonical Data Model](concept:canonical-data-model)
- [Interoperability](concept:interoperability)
- [Data Architecture](concept:data-architecture)
- [Conceptual data model building method](concept:conceptual-data-model-building-method)
- [Application/Data Matrix](concept:application-data-matrix)
- [Data Entity/Business Function Matrix](concept:data-entity-business-function-matrix)
- [Data Architecture Principle](concept:data-architecture-principle)
- [Logical vs. physical data model](concept:logical-vs-physical-data-model)
- [Command Query Responsibility Segregation](concept:command-query-responsibility-segregation)
- [Use of external and open data](concept:use-of-external-and-open-data)
