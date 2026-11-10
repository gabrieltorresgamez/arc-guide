---
title: Package Relationships (Import, Access, Merge, Use)
slug: package-relationships-import-access-merge-use
category: modeling-uml
kind: notation-element
summary: Package relationships are directed links between packages that show how their contents are shared.
  Import and merge are covered here. A dependency with no label is read as an import, so label every one.
arc42:
- 5
step: s10-document
related:
- package-diagram
- package-diagram-modeling-mistakes
- class-component-and-package-diagram-differences
- uml-modeling-best-practice
- coupling-and-cohesion
checks:
- Every dependency between packages carries an explicit label for its relationship type.
- Each merge connects two packages and its intent (combining their contents) is clear to the reader.
- Where imported elements and a merge interact, the document states what is intended.
sources:
- url: https://en.wikipedia.org/wiki/Package_diagram
  title: Package diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://support.ptc.com/help/modeler/r10.2/en/Modeler/umlprofile/UML_Import.html
  title: Import (UML Standard profile)
  site: support.ptc.com
  accessed: '2026-11-09'
- url: https://support.ptc.com/help/modeler/r10.2/en/Modeler/umlprofile/UML_Package_Merge.html
  title: Package merge (UML Standard profile)
  site: support.ptc.com
  accessed: '2026-11-09'
- url: https://issues.omg.org/issues/UMLR-797
  title: UML 2.6 RTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Package relationships show how one package depends on or builds on another. They appear on a package diagram (see the article Package Diagram).

**Import.** A package import runs from an importing namespace to a package. In the PTC modeler profile, an import means one item imports another with public visibility.

**Merge.** A package merge runs between two packages. It says their contents are to be combined. In the PTC modeler profile, you create a merge on a package diagram. It shows that one package merges the content of another.

**Matching rule.** When two packages merge, elements with the same name and the same metatype are merged.

**Unlabeled dependencies.** By default, a dependency between two packages with no label is interpreted as a package import.

**An open question.** One issue raised against the UML standard asked whether elements imported into a package are merged too. The reporter found the specification unclear on this.

## Example

A team models a shop with two packages, "Catalog" and "Ordering". Ordering needs elements from Catalog. The diagram draws an arrow from Ordering to Catalog and labels it "import". 

## Trade-offs

An unlabeled dependency between packages is interpreted as an import by default. An open issue raised against the UML specification noted that it was unclear whether imported elements are merged by a package merge.
