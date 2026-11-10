---
title: Integration Style
slug: integration-pattern
category: integration
kind: style
summary: An integration style is the basic way separate applications are connected so they can share data
  and behavior. The classic options are file transfer, shared database, remote procedure call and messaging.
  Teams choose one deliberately.
arc42:
- 4
- 9
- 8
step: s08-integration-data
related:
- file-transfer
- shared-database
- remote-procedure-call
- messaging
- architectural-decision
- loose-coupling
- messaging-pattern-language
checks:
- The document records which integration style was chosen, the alternatives considered, and the reason
  for the choice.
- If a shared database is used, the document explains how one schema serves all applications and how changes
  are controlled.
- If file transfer is used, the document describes how data is transformed between application formats.
- If messaging is chosen for loose coupling in time, the document states that sender and receiver need
  not be available together.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2025/07/17/ArchitectureDecisionGuidanceTool.html
  title: 'ADG: A Light Architectural Decision Guidance and Management Tool'
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Messaging.html
  title: Messaging - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/SharedDataBaseIntegration.html
  title: Shared Database - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/FileTransferIntegration.html
  title: File Transfer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/IntegrationDatabase.html
  title: Integration Database
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Companies often run several applications that must work together. An integration style is the general approach used to connect them.

Four classic styles exist:

- **File transfer.** Each application writes files with data that others need. It also reads files that other applications wrote. See the article File Transfer.
- **Shared database.** Applications store the data they want to share in one common database. See the article Shared Database.
- **Remote procedure invocation.** Each application exposes some of its procedures so that others can invoke them remotely, to run behavior and exchange data. See the article Remote Procedure Call.
- **Messaging.** Applications connect to a common messaging system. They use messages both to exchange data and to trigger behavior. See the article Messaging.

Messaging moves packets of data frequently, immediately, reliably and asynchronously, in formats you can customize. Asynchronous means the sender and receiver do not have to be up at the same time.

Choosing a style is an architectural decision. Teams can record it with the options considered and the reasons for the pick. See the articles Architectural Decision and Architecture Decision Rationale.

## Example

A shop's order system must pass new orders to a warehouse system. The warehouse system is sometimes offline for maintenance. The team compares the four styles. The two systems are not always running at the same time, so they pick messaging. The order system sends a message and carries on. The warehouse system reads it later. The team records the choice and the reason in the architecture document.

## Trade-offs

Each style gives up something to gain something else.

- **File transfer** needs data to be transformed between the formats of different applications. Output from one application rarely fits another exactly. Still, a whole industry of readers, writers and transformation tools has grown up around standard file formats.
- **Shared database** keeps applications consistent, and transaction management systems handle simultaneous updates well. But designing one schema (the structure of the data) that serves many applications is very hard. As Martin Fowler argues, the shared database becomes a deep point of coupling that raises the risk of changing the applications. He notes that most architects he respects take the view that it should be avoided.
- **Messaging** keeps much of the decoupling that file transfer offers. It also does not require sender and receiver to be up at the same time.
