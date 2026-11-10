---
title: ISO/IEC 25010 Quality Models and Their Target Entities
slug: quality-models-and-their-target-entities
category: quality-attributes
kind: standard
summary: 'ISO/IEC 25010 and its sibling standards give separate quality models for different targets:
  an ICT product, data, or an IT service. Pick the model that matches what you are judging.'
arc42:
- 1
- 10
- 12
step: s04-quality-requirements
related:
- iso-iec-25010-quality-model
- iso-25010-2023-revision
- quality-attribute
- arc42-quality-chapter
- standard-quality-attribute-checklist
- data-architecture
checks:
- The document states which target (ICT product, data, or IT service) each quality model is applied to.
- Data quality is assessed with a data quality model, separate from the product quality model.
- Hardware and communication components are covered by the product quality model only as components of
  the product.
sources:
- url: https://genorma.com/en/standards/iso-iec-25010-2023
  title: ISO/IEC 25010:2023
  site: genorma.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25012
  title: ISO 25012
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://knowledge.bsigroup.com/products/information-technology-systems-and-software-quality-requirements-and-evaluation-square-service-quality-models
  title: PD ISO/IEC TS 25011:2017 | 31 Dec 2017 | BSI Knowledge
  site: knowledge.bsigroup.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Choosing a quality model by target
review:
  status: generated
  flags: []
---

## Explanation

A quality model is a list of quality characteristics. Each list is built for one kind of thing, called its target.

**Product quality model (ISO/IEC 25010:2023).** Its target is an ICT product that is part of an information system. The 2023 model has nine characteristics. Interaction Capability is one of them. The model also reaches the components of such a product. These include software, firmware, hardware, data and communication infrastructure. So you can apply it to hardware and communication parts when they belong to the product. The articles "ISO/IEC 25010 Product Quality Model" and "ISO/IEC 25010:2023 Product Quality Model Revision" cover the characteristics.

**Data quality model (ISO/IEC 25012).** This is a separate model. Its target is data. It has 15 characteristics. It is the basis for assessing the quality of data products.

**IT service quality (ISO/IEC TS 25011).** This applies to IT services. These services support the needs of an individual user or a business.

A simple rule: first name what you evaluate. Is it a product, its data, or a service? Then choose the matching model.

## Example

A team builds an online booking app. They check the app against the product quality model, for example its interaction capability. They run a separate check on the customer records using the data quality model. The company also offers a support service around the app. They judge that service with the IT service quality standard. Each check uses a model for its own target.

## Trade-offs

A team must decide for itself which targets matter in its system.
