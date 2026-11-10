---
title: Enterprise Architecture Meta Model
slug: enterprise-architecture-meta-model
category: enterprise-architecture
kind: framework
summary: An enterprise architecture meta model is a shared set of entity types and relationships for describing
  an organization. The TOGAF content metamodel is a key example. Teams also use it to configure EA tools
  and repositories.
arc42:
- 8
- 12
step: s10-document
related:
- togaf
- enterprise-architecture-management
- enterprise-architecture-structure-business-and-it-architecture
- data-entity-data-component-catalog
- conceptual-vs-logical-vs-physical-data-model
- traceability
- data-architecture
- business-capability
checks:
- Logical and physical data components are kept separate, so the target architecture does not depend on
  a specific technology.
- Each data entity is mapped to the data components that hold it.
- The EA tool configuration maps each metamodel entity to a component type and each relationship to a
  typed reference.
sources:
- url: https://help.ardoq.com/en/articles/534168-frameworks-resources-togaf-v9-2-architecture-content-metamodel
  title: 'Frameworks & Resources: TOGAF v9.2 Architecture Content Metamodel | Ardoq Help'
  site: help.ardoq.com
  accessed: '2026-11-09'
- url: https://github.com/cadmiumkitty/togaf-content-metamodel-ontology
  title: 'GitHub - cadmiumkitty/togaf-content-metamodel-ontology: OWL ontology and SKOS taxonomy for TOGAF
    9.2 Content Metamodel · GitHub'
  site: github.com
  accessed: '2026-11-09'
- url: https://grahamberrisford.com/AM%201%20Methods/6PRODUCTSandTECHNIQUES/DataAndInformation/AM%20Information-Data%20architecture.htm
  title: ''
  site: grahamberrisford.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Data realization chain: from data entity to logical to physical data component.'
review:
  status: generated
  flags: []
---

## Explanation

A meta model defines the building blocks, such as "data entity" or "logical data component", and the allowed links between them.

**The TOGAF core**

The TOGAF content metamodel has a core. The core holds the minimum entities and relationships needed for traceability across all architecture domains. It is meant to stay stable. For traceability, see the article on Traceability.

**Extensions**

Extensions add deeper modeling on top of the core. They cover:

- governance
- services
- process modeling
- data
- infrastructure consolidation
- motivation

**Logical and physical**

In the information systems layer, the metamodel separates logical from physical. This lets a team define the target architecture without choosing technology first.

For data, this gives a chain:

1. A data entity is the thing the business describes.
2. A logical data component is a logical definition of the data held in a data store.
3. A physical data component realizes a logical one in a vendor- or technology-specific form.

Data entities are mapped to the data components that hold them. See the articles on Conceptual, Logical and Physical Data Model and on Data Entity/Data Component Catalog.

**Using the meta model in practice**

- *Tool configuration:* In an EA tool such as Ardoq, each metamodel entity becomes a component type. Each relationship becomes a typed reference.
- *Repositories:* A TOGAF content metamodel ontology (version 2), an OWL ontology and SKOS taxonomy built on TOGAF 9.2, formalizes the metamodel. It uses "Business Service". It adds decomposition of Business Capability. It keeps process sequencing as a single property.

## Example

A bank sets up an EA tool. It creates one component type for "Data Entity", one for "Logical Data Component" and one for "Physical Data Component". It also creates typed references between them. The team records "Customer" as a data entity. It maps Customer to a logical component for customer data. That component links to the physical component of one specific database product. Later, the team can replace the database. The logical definition stays the same.

## Trade-offs

The stable core holds only the minimum needed for traceability. Teams that need more depth can adopt extensions selectively. Separating logical from physical frees the target design from technology choices.
