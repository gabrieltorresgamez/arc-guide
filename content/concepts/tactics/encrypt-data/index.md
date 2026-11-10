---
title: Encrypt Data
slug: encrypt-data
category: tactics
kind: tactic
summary: Encrypting data scrambles it so only holders of the right key can read it. It protects stored
  data beyond access control and protects data moving over networks. Careful key management makes it work.
arc42:
- 8
- 7
- 10
step: s07-solution-strategy
related:
- security-tactics
- confidentiality
- security
- architectural-tactic
- arc42-crosscutting-concepts
- integrity
- security-scenario
- distribution-view
checks:
- Stored private data is encrypted at rest as an extra layer on top of access control.
- Traffic is encrypted in transit, for example with TLS.
- Keys are mapped to data classifications, and key access is not overly permissive.
- A formal, tested key management process covers generation, storage, rotation and decommissioning.
- Keys are not hard-coded or committed to version control, and are held in a key management service or
  HSM.
sources:
- url: https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_encrypt.html
  title: SEC08-BP02 Enforce encryption at rest - Security Pillar
  site: docs.aws.amazon.com
  accessed: '2026-11-08'
- url: https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html
  title: Transport Layer Security - OWASP Cheat Sheet Series
  site: cheatsheetseries.owasp.org
  accessed: '2026-11-08'
- url: https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html
  title: Cryptographic Storage - OWASP Cheat Sheet Series
  site: cheatsheetseries.owasp.org
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-overview
  title: Azure encryption overview | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Encryption protects data in transit and at rest, with keys held in a key service.
review:
  status: generated
  flags: []
---

## Explanation

Encrypt Data is a security tactic (see Security Tactic). It protects confidentiality: only intended parties can read the data. It covers data at rest (stored) and data in transit (moving over a network).

**Data at rest.** Access control decides who may read data. Encryption adds a second layer. If someone bypasses access control or copies data out, they still cannot read it without the key.

**Data in transit.** TLS is a standard protocol for encrypting network traffic. Done correctly, it stops attackers from reading the traffic. It also protects against tampering and replay of intercepted requests. Azure uses TLS for traffic to its services. TLS provides authentication, privacy and integrity. Forward secrecy gives each connection its own unique keys. Between datacenters, over links the provider does not physically control, Azure encrypts packets in the network hardware. This helps prevent wiretapping and man-in-the-middle attacks.

**Keys matter as much as the algorithm.** Good practice from the sources:

- Treat key management as a formal, tested process. It covers generation, storage, distribution, deployment, rotation and decommissioning.
- Generate keys randomly with a cryptographically secure function.
- Rotate keys by criteria such as the end of a set usage period, called the cryptoperiod.
- Never hard-code keys in source code. Never commit them to version control.
- Use cloud key management services and hardware security modules (HSMs, dedicated devices that hold keys) where possible. Azure Key Vault spares teams from configuring, patching and maintaining this hardware, and applications have no direct access to the keys. Azure Key Vault Managed HSM goes further, with a customer-owned security domain where Microsoft has no access to key material.

**Cloud options.** AWS offers envelope encryption and client-side encryption. A wrapping key protects a unique data key for each object. CloudHSM provides a managed HSM used by a single customer. With customer-managed keys, you control rotation and access policy. Default service-managed keys are run by the provider. AWS advises mapping keys to data classifications instead of using one key for everything. It also warns against overly permissive key access.

## Example

A shop stores customer records in a database and serves them through a web app. The team encrypts the database storage, so a stolen disk copy is unreadable. The web app only accepts TLS connections, so nobody on the network can read orders. Payment data gets its own key, separate from the key for marketing data. Keys live in a cloud key service, never in the code, and rotate on a schedule.

## Trade-offs

Encryption shifts the risk to keys. Keys need generation, storage, rotation and decommissioning processes, and these need testing. Using one key for all data, or giving broad key access, weakens the protection. Customer-managed keys give more control, but your team then owns rotation and access policy. Default service-managed keys leave that work to the provider.
