**English** | [Português (Brasil)](0003-clean-room-development.pt-BR.md)

# ADR-0003: Clean-room development

- **Status:** Accepted
- **Date:** 2026-11-16
- **Deciders:** @pedroisoares

## Context

The people who start QuectoERP know existing commercial ERPs well, and the Brazilian ERP market has established vendors that protect their software. Ideas, business processes and legal rules are not protected by copyright, but source code, database structures, names, screen layouts and documentation can be. A dispute over copied material could stop the project or expose its users.

## Decision

QuectoERP is written from scratch under a clean-room rule. The rule, as published in the [contributing guide](../../CONTRIBUTING.md#clean-room-rule-mandatory), is:

1. No code, database structures, table or field names, screen layouts or documentation copied or derived from other ERPs, proprietary or open source under an incompatible license.
2. People who have worked with another ERP's source code or data dictionary may still help by writing *functional requirements in their own words*, based on business processes and law. They never paste or paraphrase proprietary material.
3. The data model comes from the domain (domain-driven design) with its own vocabulary. No legacy prefixes, routine codes or parameter names.
4. **Public sources are the reference** for legal and tax rules: laws, official manuals (NF-e, SPED, eSocial), public-sector accounting standards (MCASP/PCASP), Febraban CNAB layouts and similar.
5. **Traceability.** Every specification records its source (law, manual, interview, process observation). That record is our defense if the origin of a rule is ever questioned.
6. **Legacy material never enters the repository**: not in code, issues, tests, fixtures or examples.
7. No third-party trademarks in module names, screens or documentation.
8. A legal review happens before the first public release (0.1.0) and before any commercial offer.

Pull requests that break the rule are closed.

## Consequences

- Specification work is slower: requirements are rewritten from public sources instead of being lifted from an existing system.
- Every module needs a list of sources next to its specification, and reviewers check it (the pull request template already asks for it).
- The project can be used, forked and sold by anyone without inheriting legal risk from another vendor.
- Demonstration data (a fictional company and a fictional public agency) must also be original.

## Alternatives considered

- **Port or translate an existing open source ERP:** fastest start, but ties the architecture to someone else's design and may carry license incompatibilities.
- **Informal "just don't copy" guidance:** hard to enforce and hard to defend without traceability.
