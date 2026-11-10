---
title: Authenticity
slug: authenticity
category: quality-attributes
kind: quality-attribute
summary: Authenticity is the degree to which you can prove that a user, device, or resource is the one
  it claims to be. ISO/IEC 25010 lists it as a security sub-characteristic.
arc42:
- 8
- 10
- 4
step: s04-quality-requirements
related:
- security
- confidentiality
- nonrepudiation
- accountability
- resistance
- integrity
- iso-iec-25010-quality-model
- security-tactics
checks:
- The document states which subjects and resources must have a provable identity.
- Authentication and authorization are described as separate steps.
- The document says whether multifactor authentication is used and why.
- If authentication is delegated to a central identity provider, the document names it and the single
  sign-on approach.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=6
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/articles/iso-25010-update-2023
  title: Update on ISO 25010, version 2023 | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/entra/identity-platform/authentication-vs-authorization
  title: Authentication vs. authorization - Microsoft identity platform | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://openid.net/specs/openid-connect-core-1_0.html
  title: 'Final: OpenID Connect Core 1.0 incorporating errata set 2'
  site: openid.net
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Authentication proves the claimed identity; authorization then decides what that identity may
    do.
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC 25010 is a standard quality model (see ISO/IEC 25010 Product Quality Model). It places authenticity under security. It defines authenticity as how far you can prove that a subject or resource really has the identity it claims.

**Where it sits in security.** Security means defending against attack patterns by malicious actors and protecting information and data. Authenticity has several siblings under security:

- Confidentiality: data are accessible only to those authorized. See Confidentiality.
- Non-repudiation: actions or events can be proven to have happened, so nobody can deny them later. See Nonrepudiation.
- Accountability: the actions of an entity can be traced uniquely to that entity. See Accountability.
- Resistance: the system keeps operating while under attack. See Resistance.

**Authentication versus authorization.** These words sound alike but differ.

- Authentication is the process of proving you are who you say you are. It verifies the identity of a person or device.
- Authorization gives an authenticated party permission. It says what data the party may access and what it may do with that data.

**Mechanisms.** Multifactor authentication adds another authentication factor to an account. It is often used to protect against brute force attacks.

**Federated identity.** An application can delegate authentication to a central identity provider. A user can then sign in once and be signed in automatically to the web apps that share the same centralized directory. This is called single sign-on.

**OpenID Connect.** OpenID Connect is an identity layer on top of OAuth 2.0. It lets a client verify the identity of the end user, based on authentication done by an authorization server.

**2023 revision.** The 2023 revision added resistance as a sub-characteristic of security. The source describing the changes mentions no change to authenticity.

## Example

A company runs an online ordering system and several internal tools. Instead of each tool keeping its own passwords, all tools send sign-in to one central identity provider. Staff sign in once, and a second factor is required. The ordering system then checks what each signed-in person may do. The architecture document states which identities must be provable (staff and partner systems) and names the provider that proves them.

## Trade-offs

Delegating authentication to a central identity provider spares each app from administering its own credentials. Weigh these choices against other qualities (see Quality Attribute Trade-off).
