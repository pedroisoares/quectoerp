[English](README.md) | **Português (Brasil)**

# QuectoERP

**O menor ERP capaz de gerir uma empresa inteira.**

O QuectoERP é um ERP open source ultra-minimalista, feito de serviços pequenos e rápidos, com orçamento de recursos medido. O mesmo código roda como binário único on-premises ou como serviços independentes na nuvem.

> **quecto** (símbolo **q**, fator **10⁻³⁰**) é o menor prefixo do Sistema Internacional de Unidades, adotado em 2022. Menor que isso não existe, e essa é a ideia.

> [!NOTE]
> **Situação do projeto: desenho inicial.** Ainda não há código executável. Estamos definindo o kernel, o fluxo de contribuição e os primeiros módulos. É o melhor momento para entrar na conversa e ajudar a moldar o projeto. Veja o [roadmap](ROADMAP.pt-BR.md) para saber o que vem a seguir.

## Por que mais um ERP?

- **Kernel pequeno, módulos plugáveis.** O kernel oferece identidade, multiempresa, metadados, eventos, auditoria e interface. As regras de negócio ficam nos módulos.
- **Orientado a metadados.** Entidades, campos, validações, telas e permissões são declarados e versionados em Git, e a parte repetitiva (SQL, API, eventos, formulários) é gerada em tempo de compilação.
- **Eventos e API primeiro.** Todo fato de negócio vira um evento imutável. Tudo que a tela faz, a API faz.
- **Extensível sem fork.** Clientes e parceiros estendem campos, regras e telas sem mexer no kernel, e as atualizações continuam seguras.
- **Leve no peso, não fragmentado.** Cada módulo é um contexto delimitado que pode ser composto num único host ou implantado sozinho.
- **Orçamento como teste.** Cada serviço tem metas de tamanho, memória e latência medidas no CI. Estourar o orçamento quebra o build.
- **Feito para o Brasil, aberto ao mundo.** Regras fiscais e do setor público brasileiro (NF-e, SPED, eSocial, Lei 14.133) são cidadãs de primeira classe, mantidas como dados abertos versionados.

## Stack prevista

| Camada | Escolha |
| --- | --- |
| Serviços | C# / .NET com **Native AOT**, Minimal APIs, source generators (sem reflexão em tempo de execução) |
| Banco de dados | **PostgreSQL** (um schema por módulo) |
| Mensageria | Outbox no PostgreSQL (`LISTEN/NOTIFY`); **NATS JetStream** quando houver mais de um processo |
| Identidade | OpenIddict, com federação OIDC |
| Motor tributário | Rust compilado para WebAssembly |
| Front-end | React + TypeScript, telas geradas a partir de metadados, com orçamento de bundle |
| Observabilidade | OpenTelemetry |

A stack ainda está em discussão. Mudanças são registradas como ADRs (Architecture Decision Records).

## Orçamento inicial de recursos (por serviço)

| Métrica | Meta |
| --- | --- |
| Binário AOT | ≤ 30 MB |
| Memória em repouso (RSS) | ≤ 40 MB |
| Inicialização até pronto | ≤ 100 ms |
| Leitura simples (p99) | ≤ 10 ms |
| Instalação on-prem mínima | 1 binário + PostgreSQL, ≤ 512 MB de RAM no total |

## Como contribuir

Contribuições são bem-vindas em **português do Brasil ou inglês**. Leia antes:

- [Guia de contribuição](CONTRIBUTING.pt-BR.md)
- [Código de Conduta](CODE_OF_CONDUCT.pt-BR.md)
- [Política de segurança](SECURITY.pt-BR.md)

O QuectoERP é um projeto **clean-room**: nunca envie código, estruturas de banco, nomes ou documentação copiados de outros ERPs, proprietários ou não. Veja os detalhes no guia de contribuição.

## Licença

O QuectoERP é licenciado sob a [GNU Affero General Public License v3.0](LICENSE) (AGPL-3.0). Se você modificar o QuectoERP e oferecê-lo a outras pessoas, inclusive como serviço pela rede, precisa disponibilizar o seu código-fonte sob a mesma licença.
