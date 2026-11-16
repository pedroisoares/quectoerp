**English** | [Português (Brasil)](README.pt-BR.md)

# QuectoERP

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/logo/quectoerp-logo-on-dark.svg">
  <img src="brand/logo/quectoerp-logo.svg" alt="QuectoERP" height="72">
</picture>

**The smallest ERP that can run a whole company.**

QuectoERP is an ultra-minimal, open source ERP built from tiny, fast services with a measured resource budget. The same code runs as a single binary on-premises or as independent services in the cloud.

> **quecto** (symbol **q**, factor **10⁻³⁰**) is the smallest prefix in the International System of Units, adopted in 2022. Nothing smaller exists, and that is the idea.

> [!NOTE]
> **Project status: early design.** There is no runnable code yet. We are defining the kernel, the contribution workflow and the first modules. This is the best moment to join the conversation and shape the project. See the [roadmap](ROADMAP.md) for what comes next.

## Why another ERP?

- **Small kernel, pluggable modules.** The kernel provides identity, multi-company, metadata, events, auditing and UI. Business rules live in modules.
- **Metadata-driven.** Entities, fields, validations, screens and permissions are declared, versioned in Git, and the repetitive parts (SQL, API, events, forms) are generated at compile time.
- **Event-first and API-first.** Every business fact is an immutable event. Anything the UI can do, the API can do.
- **Extensible without forking.** Customers and partners extend fields, rules and screens without touching the kernel, so updates stay safe.
- **Light in weight, not fragmented.** Each module is a bounded context that can be composed into one host or deployed on its own.
- **Budget as a test.** Every service has size, memory and latency targets measured in CI. Breaking the budget breaks the build.
- **Built for Brazil, open to the world.** Brazilian tax and public-sector rules (NF-e, SPED, eSocial, Law 14.133) are first-class, kept as versioned open data.

## Planned stack

| Layer | Choice |
| --- | --- |
| Services | C# / .NET with **Native AOT**, Minimal APIs, source generators (no runtime reflection) |
| Database | **PostgreSQL** (one schema per module) |
| Messaging | Outbox in PostgreSQL (`LISTEN/NOTIFY`); **NATS JetStream** when running more than one process |
| Identity | OpenIddict, with OIDC federation |
| Tax engine | Rust compiled to WebAssembly |
| Front end | React + TypeScript, screens generated from metadata, with a bundle budget |
| Observability | OpenTelemetry |

The stack is recorded in [ADR-0004](docs/adr/0004-technology-stack.md) and will be confirmed by the proof of concept in milestone 0.2. Every change goes through an [Architecture Decision Record](docs/adr/README.md) (ADR).

## Initial resource budget (per service)

| Metric | Target |
| --- | --- |
| AOT binary | ≤ 30 MB |
| Memory at rest (RSS) | ≤ 40 MB |
| Startup until ready | ≤ 100 ms |
| Simple read (p99) | ≤ 10 ms |
| Minimal on-prem install | 1 binary + PostgreSQL, ≤ 512 MB RAM in total |

## Contributing

Contributions are welcome in **English or Brazilian Portuguese**. Please read:

- [Contributing guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security policy](SECURITY.md)

QuectoERP is a **clean-room** project: never submit code, database structures, names or documentation copied from other ERPs, proprietary or not. See the contributing guide for details.

## License

QuectoERP is licensed under the [GNU Affero General Public License v3.0](LICENSE) (AGPL-3.0). If you modify QuectoERP and offer it to others, including as a service over a network, you must make your source code available under the same license.
