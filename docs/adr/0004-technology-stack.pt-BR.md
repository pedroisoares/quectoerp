[English](0004-technology-stack.md) | **Português (Brasil)**

# ADR-0004: Stack tecnológica

- **Status:** Aceito
- **Data:** 16/11/2026
- **Decisores:** @pedroisoares

## Contexto

O QuectoERP promete serviços pequenos e rápidos, com orçamento de recursos medido, e uma instalação on-prem mínima de **um binário + PostgreSQL**. Ele é desenvolvido principalmente por um mantenedor trabalhando com um assistente de IA, então a stack precisa favorecer ciclos curtos de escrever, compilar e testar, uma base grande de contribuidores no Brasil e boas bibliotecas para documentos fiscais brasileiros (NF-e e outros). O gargalo de um ERP é o banco de dados e o I/O, não a CPU.

O primeiro rascunho de arquitetura usava uma stack .NET convencional (JIT, EF Core, um barramento de mensagens de aplicação, Keycloak). Uma revisão posterior trocou as peças pesadas para que todo serviço possa ser compilado antecipadamente e caiba no orçamento.

## Decisão

| Camada | Escolha |
| --- | --- |
| Linguagem e runtime | C# no **.NET 10 (LTS)**, compilado com **Native AOT** em todos os serviços. A versão do SDK fica fixada no `global.json` |
| Geração de código | Source generators no lugar de reflexão em tempo de execução: Minimal APIs com o Request Delegate Generator, `System.Text.Json` com source generation, mapeamento SQL gerado a partir dos metadados |
| Estrutura | Monólito modular: um projeto por contexto delimitado, composto num único host ou implantado como serviços separados, com os mesmos contratos |
| Banco de dados | **PostgreSQL**, um schema por módulo. A única infraestrutura obrigatória |
| Acesso a dados | **Npgsql** com SQL gerado pelo SDK a partir dos metadados. Nenhum ORM nos serviços |
| Eventos | Outbox transacional no PostgreSQL com `LISTEN/NOTIFY` em processo único; **NATS JetStream** quando houver mais de um processo |
| Identidade | **OpenIddict** embutido no módulo de identidade; provedores de identidade externos só por federação OIDC |
| Front-end | React e TypeScript, telas geradas a partir dos metadados num único shell, com orçamento de tamanho do bundle |
| Motor tributário | Rust compilado para WebAssembly, para que o mesmo cálculo rode no servidor, no navegador e no PDV. C# fica como alternativa se não compensar |
| Observabilidade | OpenTelemetry. A instalação mínima não exige backend de monitoramento (logs JSON no stdout e um endpoint `/metrics`) |
| Testes | xUnit, Testcontainers para o PostgreSQL, testes de arquitetura para as fronteiras entre módulos |
| CI | GitHub Actions |

O marco 0.2 (prova de conceito) precisa confirmar as partes de risco com um módulo de exemplo real: suporte a Native AOT no OpenIddict, no Npgsql e na pilha HTTP, o outbox, e os números reais contra o orçamento de recursos. Toda peça que falhar é trocada por um ADR novo que substitui a linha correspondente deste.

## Consequências

- Inicialização em dezenas de milissegundos e binários pequenos tornam realistas o orçamento e a instalação de "um binário + PostgreSQL".
- Bibliotecas que dependem de reflexão ou de geração dinâmica de código em tempo de execução não podem ser usadas nos serviços. Isso exclui, por exemplo, o EF Core em execução e a maioria dos barramentos de mensagens baseados em reflexão, e reduz a escolha de pacotes de terceiros.
- SQL gerado dá mais responsabilidade ao SDK; em troca, o kernel conhece toda consulta que um módulo pode executar.
- Rust acrescenta uma segunda toolchain para um único componente. Continua opcional até o motor tributário começar, na Fase 1.
- Toda nova dependência de execução precisa do seu próprio ADR, com o custo (veja o ADR-0001).

## Alternativas consideradas

- **.NET convencional (JIT, EF Core, Wolverine, Keycloak):** começo mais rápido, mas o EF Core e a geração dinâmica de código funcionam mal com Native AOT, e só o Keycloak pede centenas de megabytes de memória para o login.
- **Rust para tudo:** desempenho máximo, mas quase nada pronto para documentos fiscais brasileiros e iteração mais lenta em código de negócio cheio de entidades.
- **Java ou Kotlin na JVM:** ecossistema maduro, mas mais memória em repouso, e a compilação nativa traz restrições parecidas com as do .NET AOT sem as mesmas ferramentas para o nosso time.
- **RabbitMQ ou Kafka desde o primeiro dia:** infraestrutura extra de que uma instalação pequena não precisa.
