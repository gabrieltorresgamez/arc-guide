---
title: Use of External and Open Data
slug: use-of-external-and-open-data
category: data-architecture
kind: concept
summary: External data, especially open data, is a useful input for applications. Open data is public
  domain or openly licensed, free to access, and machine-readable. Architects should plan for it early.
arc42:
- 3
- 2
step: s02-scope-context
related:
- context-view
- arc42-context-and-scope
- business-and-technical-context
- data-reusability-and-standardized-access
- integration
- interoperability
checks:
- For each open data source, the document states its license, or that it is in the public domain.
- For each open data source, the document states that the data is machine-readable and how it can be obtained.
sources:
- url: https://opendefinition.org/od/2.1/en/
  title: Open Definition 2.1 - Open Definition - Defining Open in Open Data, Open Content and Open Knowledge
  site: opendefinition.org
  accessed: '2026-11-09'
- url: https://www.w3.org/TR/vocab-dcat-3/
  title: Data Catalog Vocabulary (DCAT) - Version 3
  site: w3.org
  accessed: '2026-11-09'
- url: https://data.gov/about/
  title: About Us - Data.gov
  site: data.gov
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Many applications need data they do not produce themselves. Public bodies publish some of it for anyone to use. Architects should know such sources exist and plan how the application will reach them.

**What makes data open**

The Open Definition sets four requirements for an open work:

- **Legal status.** The work is in the public domain or under an open license. An open license must permit use, redistribution, and modification, and may require conditions such as attribution.
- **Access.** The work is available as a whole. It costs no more than a reasonable one-time reproduction fee. It should be downloadable via the Internet without charge.
- **Machine-readable.** The work is provided in a form a computer can process readily, with its individual elements easily accessed and modified.
- **Open format.** The work is provided in an open format, one that places no restrictions on its use and can be fully processed with at least one free/libre/open-source software tool.

**Open government data**

Data.gov is the US government's open data site. The OPEN Government Data Act says that government data must be published in open formats that machines can read.

**Finding data across catalogs**

Data catalogs list datasets. DCAT is an RDF vocabulary that helps data catalogs on the Web work together. Catalogs that use DCAT can describe their datasets in a shared way.

**What this means for architecture**

An external source is a system outside your control. Show it as an external system in your context view. See the article "Context View" for details. Plan the access path to the source as well.

## Example

A city app shows nearby services on a map. The team finds a government portal that offers a free, openly licensed dataset in a machine-readable form. They add the portal to the context diagram as an external system. They also record in the architecture document how the app will obtain the data.

## Trade-offs

This article does not cover the quality, availability, or legal risks of depending on external sources. Check those for each source before you rely on it.
