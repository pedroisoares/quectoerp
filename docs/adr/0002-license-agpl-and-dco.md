**English** | [Português (Brasil)](0002-license-agpl-and-dco.pt-BR.md)

# ADR-0002: AGPL-3.0 license and DCO sign-off

- **Status:** Accepted
- **Date:** 2026-11-16
- **Deciders:** @pedroisoares

## Context

QuectoERP is open source from the first commit, and its future revenue is expected to come from a managed SaaS, compliance subscriptions, support and partner services, not from selling licenses. The main risk to that model is a third party taking the code, improving it privately and offering it as a competing hosted service. The repository was first published under GPL-3.0 and then relicensed to AGPL-3.0 before any outside contribution was received.

Contributors also need a simple, low-friction way to state that they have the right to submit their code, which matters even more for a project bound by a clean-room rule (ADR-0003).

## Decision

1. **The repository is licensed under the GNU Affero General Public License v3.0 only** ([LICENSE](../../LICENSE)). Anyone who modifies QuectoERP and lets users interact with it over a network must offer them the corresponding source code.
2. **Every commit carries a Developer Certificate of Origin 1.1 sign-off** (`git commit -s`). The CI rejects pull requests with commits that are not signed off by their author.
3. Packages meant to be used *by* other software (the extension SDK, client libraries, API contracts, the open tax-rules dataset) may later get a more permissive license, such as Apache-2.0 or CC BY 4.0, so partners can write proprietary extensions. Each of those is decided in its own ADR when the package exists. Until then, everything is AGPL-3.0.

## Consequences

- A competitor cannot close the code and sell it as a service without publishing its changes.
- Some companies have policies against AGPL software. We accept a smaller corporate audience in exchange for protection of the project.
- The DCO keeps contributions easy (no account or paper to sign) and leaves a per-commit record of origin.
- **The DCO does not grant the project the right to relicense contributions.** Every contributor keeps their copyright under AGPL-3.0, so a future dual-license (for example a commercial edition built on community code) would need either a Contributor License Agreement adopted before such contributions arrive, or permission from each author. If dual licensing becomes a goal, it needs a new ADR and a legal review, ideally before the first public release (0.1.0).

## Alternatives considered

- **GPL-3.0 (the initial license):** does not cover use over a network, which is exactly how an ERP is usually offered.
- **Apache-2.0 or MIT for everything:** maximum adoption, but no protection against a closed hosted fork.
- **LGPL (as some open-core ERPs use):** weaker protection for the kernel and modules, with little gain for us.
- **CLA instead of DCO:** keeps relicensing options open, but adds friction and needs legal drafting. Deferred, see consequences.
