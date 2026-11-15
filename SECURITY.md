**English** | [Português (Brasil)](SECURITY.pt-BR.md)

# Security Policy

## Supported versions

QuectoERP is in early design and has no released version yet. Until the first release, security fixes are applied only to the `main` branch. This table will be updated when releases start.

| Version | Supported |
| --- | --- |
| `main` | ✅ |

## Reporting a vulnerability

**Please do not report security vulnerabilities through public issues, discussions or pull requests.**

Report them privately through GitHub: go to the repository's **Security** tab and click **[Report a vulnerability](https://github.com/pedroisoares/quectoerp/security/advisories/new)**.

Please include, in English or Brazilian Portuguese:

- The type of issue (for example SQL injection, authentication bypass, tenant data leak).
- The affected component, file or endpoint, and the version or commit.
- Step-by-step instructions to reproduce, and proof-of-concept code if possible.
- The impact, including how an attacker could exploit it.

## What to expect

- We acknowledge your report within **3 business days**.
- We send an initial assessment within **10 business days**.
- We keep you informed while we work on a fix and agree on a disclosure date with you, usually within **90 days**.
- We credit you in the advisory, unless you prefer to remain anonymous.

## Scope

Of special interest for an ERP: isolation between tenants and companies, authentication and authorization, audit trail integrity, fiscal document signing and certificates, and exposure of personal data protected by the LGPD (Brazil's General Data Protection Law).

Thank you for helping keep QuectoERP and its users safe.
