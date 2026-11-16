[English](0002-license-agpl-and-dco.md) | **Português (Brasil)**

# ADR-0002: Licença AGPL-3.0 e assinatura DCO

- **Status:** Aceito
- **Data:** 16/11/2026
- **Decisores:** @pedroisoares

## Contexto

O QuectoERP é open source desde o primeiro commit, e a receita futura deve vir de SaaS gerenciado, assinatura de conformidade, suporte e rede de parceiros, não da venda de licenças. O maior risco para esse modelo é alguém pegar o código, melhorá-lo de forma privada e oferecê-lo como serviço hospedado concorrente. O repositório foi publicado primeiro sob GPL-3.0 e depois relicenciado para AGPL-3.0, antes de receber qualquer contribuição externa.

Quem contribui também precisa de um jeito simples de declarar que tem direito de enviar o código, o que pesa ainda mais num projeto sujeito à regra clean-room (ADR-0003).

## Decisão

1. **O repositório é licenciado somente sob a GNU Affero General Public License v3.0** ([LICENSE](../../LICENSE)). Quem modificar o QuectoERP e permitir que usuários interajam com ele pela rede precisa oferecer o código-fonte correspondente.
2. **Todo commit leva a assinatura do Developer Certificate of Origin 1.1** (`git commit -s`). O CI recusa pull requests com commits que não estejam assinados pelo próprio autor.
3. Pacotes feitos para serem usados *por* outros softwares (o SDK de extensões, bibliotecas cliente, contratos de API, o repositório aberto de regras fiscais) podem receber depois uma licença mais permissiva, como Apache-2.0 ou CC BY 4.0, para que parceiros escrevam extensões proprietárias. Cada caso será decidido em um ADR próprio quando o pacote existir. Até lá, tudo é AGPL-3.0.

## Consequências

- Um concorrente não consegue fechar o código e vendê-lo como serviço sem publicar as mudanças.
- Algumas empresas têm políticas contra software AGPL. Aceitamos um público corporativo menor em troca da proteção do projeto.
- O DCO mantém a contribuição simples (sem cadastro nem documento para assinar) e deixa, em cada commit, um registro da origem.
- **O DCO não dá ao projeto o direito de relicenciar as contribuições.** Cada contribuidor mantém o seu direito autoral sob a AGPL-3.0, então um licenciamento duplo no futuro (por exemplo, uma edição comercial feita sobre código da comunidade) exigiria um Contrato de Licença de Contribuidor (CLA) adotado antes dessas contribuições chegarem, ou a autorização de cada autor. Se o licenciamento duplo virar objetivo, isso pede um ADR novo e revisão jurídica, de preferência antes da primeira versão pública (0.1.0).

## Alternativas consideradas

- **GPL-3.0 (a licença inicial):** não cobre o uso pela rede, que é justamente como um ERP costuma ser oferecido.
- **Apache-2.0 ou MIT para tudo:** máxima adoção, mas nenhuma proteção contra um fork hospedado e fechado.
- **LGPL (usada por alguns ERPs open-core):** proteção mais fraca para o kernel e os módulos, com pouco ganho para nós.
- **CLA em vez de DCO:** mantém aberta a opção de relicenciar, mas cria atrito e exige redação jurídica. Adiado; veja as consequências.
