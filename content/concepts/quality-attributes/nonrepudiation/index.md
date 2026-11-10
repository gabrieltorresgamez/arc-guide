---
title: Nonrepudiation
slug: nonrepudiation
category: quality-attributes
kind: quality-attribute
summary: Nonrepudiation means actions can be proven to have happened, so an author cannot successfully
  deny a message or a contract. Digital signatures and trusted third parties are the usual tools.
arc42:
- 8
- 10
step: s04-quality-requirements
related:
- security
- accountability
- authenticity
- integrity
- iso-iec-25010-quality-model
- security-tactics
- confidentiality
checks:
- The document states which actions must be provable and how, for example with digital signatures.
- Signing keys are protected, and the document says how, because forged signatures would undermine non-repudiation.
- The document names a trusted third party, such as a certificate authority or time stamping authority,
  where proof must hold up against disputes.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=2
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Non-repudiation
  title: Non-repudiation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.rfc-editor.org/info/rfc3161/
  title: 'RFC 3161: Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP) | RFC Editor'
  site: rfc-editor.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Nonrepudiation is a sub-characteristic of security in the ISO/IEC 25010 quality model (see the article ISO/IEC 25010 Product Quality Model). The standard describes it as how far you can prove that actions or events really happened.

In practice, an author cannot successfully dispute that they wrote a statement. They also cannot dispute the validity of a contract tied to it.

**Related properties.** Two sibling sub-characteristics sit alongside it:

- **Accountability** means tracing actions uniquely to one entity.
- **Authenticity** means proving that an identity is the one claimed.

**Digital signatures.** A digital signature gives non-repudiation that anyone can verify. A message authentication code (MAC) is different. It relies on a shared secret, so it cannot offer the same public proof.

**Certificates.** A public key certificate lets anyone check a signature. Certificate authorities attest to whom a certificate belongs.

**Trusted third parties.** A trusted third party is an independent party that all sides rely on. Involving one is the standard way to reduce the risk that signers disown their signatures. A time stamping authority is one kind. It issues tokens showing that data existed at a given point in time.

## Example

An online shop receives an order from a customer. The customer signs the order with a private key. The shop checks the signature using the customer's public key certificate. A time stamping authority adds a token showing when the order existed. Later, the customer claims they never placed the order. The shop shows the signed, time-stamped order as proof.

## Trade-offs

If a signing key is not properly safeguarded, someone can forge signatures. That undermines non-repudiation. Teams that rely on signatures must therefore protect keys carefully.
