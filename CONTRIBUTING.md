**English** | [Português (Brasil)](CONTRIBUTING.pt-BR.md)

# Contributing to QuectoERP

Thank you for your interest in QuectoERP! This guide explains how to propose changes and what we expect from every contribution. By taking part, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Languages

The project is bilingual. You can open issues, pull requests and discussions in **English or Brazilian Portuguese**; maintainers will reply in the same language.

- **Code** (identifiers, commit messages, code comments): English.
- **Business terms** that only exist in Brazilian law (for example *NF-e*, *SPED*, *eSocial*, *CFOP*) keep their original names; add a short English explanation the first time they appear.
- **User documentation**: English file as the default (`NAME.md`) and a Brazilian Portuguese version next to it (`NAME.pt-BR.md`), each linking to the other on the first line. If you only write one language, that is fine: open the PR and mark the translation as pending, and someone will help.

## Ways to contribute

- Report bugs and suggest features through [issues](https://github.com/pedroisoares/quectoerp/issues/new/choose).
- Discuss design and architecture decisions (ADRs).
- Improve documentation and translations.
- Write code for the kernel, the SDK or modules.
- Describe business processes and legal rules from public sources (see *Clean-room* below).

Issues labeled `good first issue` are a good place to start.

## Clean-room rule (mandatory)

QuectoERP is written from scratch. To protect the project and its users:

1. **Never submit code, database structures, table or field names, screen layouts or documentation copied or derived from other ERPs**, proprietary or open source with an incompatible license.
2. If you have worked with the source code or data dictionary of a proprietary ERP, you can still help by writing **functional requirements in your own words**, based on business processes and legislation. Do not paste or paraphrase proprietary material.
3. The primary sources for legal and tax rules are **public**: laws, official manuals (NF-e, SPED, eSocial), public-sector accounting standards (MCASP/PCASP), Febraban CNAB layouts and similar.
4. Record the source of each specification (law, manual, interview, process observation).
5. Do not use third-party trademarks in module names, screens or docs.

Pull requests that break this rule will be closed.

## Before you start

- For anything larger than a small fix, **open an issue first** so we can agree on the approach.
- Changes to architecture, the public contract between modules, or new dependencies need an **ADR** (Architecture Decision Record). A new dependency must state its cost in size, memory and operations, and which module needs it.
- Respect the **resource budget**: size, memory and latency are measured in CI. A regression above 10% against `main` must be justified in the PR.

## Development workflow

1. Fork the repository and create a branch from `main`:
   `feat/short-description`, `fix/short-description`, `docs/short-description`.
2. Make small, focused commits.
3. Write commit messages following [Conventional Commits](https://www.conventionalcommits.org/):
   `feat(kernel): add tenant resolver`, `fix(fiscal): round ICMS base`, `docs: translate SECURITY`.
4. Sign off every commit (see *DCO* below).
5. Add or update tests and documentation.
6. Open a pull request and fill in the template.

### Local setup

The build tooling is still being defined. When the first code lands, this section will list the exact commands. The expected prerequisites are:

- [.NET SDK](https://dotnet.microsoft.com/) (version pinned in `global.json`)
- [PostgreSQL](https://www.postgresql.org/) or Docker
- Optional: [NATS](https://nats.io/), Rust toolchain (tax engine), Node.js (front end)

### Code guidelines

- **No runtime reflection** in services: use source generators so everything works with Native AOT.
- Each module owns its own PostgreSQL schema. No module reads or writes another module's data directly; use APIs and events.
- Keep handwritten code for business rules; repetitive code should come from the SDK generators.
- Follow the repository `.editorconfig` and run the formatter before committing.

## Pull request review

- At least one maintainer approval is required (see [CODEOWNERS](.github/CODEOWNERS)).
- CI must be green, including the resource budget checks.
- Maintainers may ask for changes; please answer review comments or push updates.
- We squash-merge using the PR title, so keep it in Conventional Commits format.

## Developer Certificate of Origin (DCO)

All contributions must be signed off under the [Developer Certificate of Origin 1.1](https://developercertificate.org/). By signing off, you certify that you wrote the contribution or otherwise have the right to submit it under the project's license.

Add the sign-off with `git commit -s`, which appends:

```
Signed-off-by: Your Name <your.email@example.com>
```

Use your real name and an email you control. To fix commits that are missing it: `git rebase --signoff main` and force-push your branch.

## Reporting security issues

Do **not** open public issues for vulnerabilities. Follow the [security policy](SECURITY.md).

## License

By contributing, you agree that your contributions will be licensed under the [GNU Affero General Public License v3.0](LICENSE) (AGPL-3.0), the same license as the project.
