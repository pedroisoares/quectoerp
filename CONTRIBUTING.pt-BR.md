[English](CONTRIBUTING.md) | **Português (Brasil)**

# Como contribuir com o QuectoERP

Obrigado pelo interesse no QuectoERP! Este guia explica como propor mudanças e o que esperamos de cada contribuição. Ao participar, você concorda em seguir o nosso [Código de Conduta](CODE_OF_CONDUCT.pt-BR.md).

## Idiomas

O projeto é bilíngue. Você pode abrir issues, pull requests e discussões em **português do Brasil ou inglês**; os mantenedores respondem no mesmo idioma.

- **Código** (identificadores, mensagens de commit, comentários no código): inglês.
- **Termos de negócio** que só existem na legislação brasileira (por exemplo *NF-e*, *SPED*, *eSocial*, *CFOP*) mantêm o nome original; acrescente uma breve explicação em inglês na primeira vez em que aparecem.
- **Documentação para usuários**: arquivo em inglês como padrão (`NOME.md`) e a versão em português ao lado (`NOME.pt-BR.md`), cada um com link para o outro na primeira linha. Se você só escrever em um idioma, tudo bem: abra o PR e marque a tradução como pendente, que alguém ajuda.

## Formas de contribuir

- Relatar bugs e sugerir funcionalidades pelas [issues](https://github.com/pedroisoares/quectoerp/issues/new/choose).
- Discutir decisões de desenho e arquitetura (ADRs).
- Melhorar a documentação e as traduções.
- Escrever código para o kernel, o SDK ou os módulos.
- Descrever processos de negócio e regras legais a partir de fontes públicas (veja *Clean-room* abaixo).

Issues com o rótulo `good first issue` são um bom ponto de partida.

## Regra clean-room (obrigatória)

O QuectoERP é escrito do zero. Para proteger o projeto e quem o usa:

1. **Nunca envie código, estruturas de banco, nomes de tabelas ou campos, leiautes de tela ou documentação copiados ou derivados de outros ERPs**, sejam proprietários ou open source com licença incompatível.
2. Se você já trabalhou com o código-fonte ou o dicionário de dados de um ERP proprietário, ainda pode ajudar escrevendo **requisitos funcionais com as suas próprias palavras**, com base em processos de negócio e na legislação. Não cole nem parafraseie material proprietário.
3. As fontes primárias para regras legais e fiscais são **públicas**: leis, manuais oficiais (NF-e, SPED, eSocial), normas de contabilidade pública (MCASP/PCASP), leiautes CNAB da Febraban e similares.
4. Registre a fonte de cada especificação (lei, manual, entrevista, observação de processo).
5. Não use marcas de terceiros em nomes de módulos, telas ou documentação.

Pull requests que descumprirem essa regra serão fechados.

## Antes de começar

- Para qualquer coisa maior que uma correção pequena, **abra uma issue antes** para combinarmos a abordagem.
- Mudanças de arquitetura, no contrato público entre módulos ou novas dependências precisam de um **ADR** (Architecture Decision Record). Uma dependência nova deve informar quanto custa em tamanho, memória e operação, e qual módulo precisa dela.
- Respeite o **orçamento de recursos**: tamanho, memória e latência são medidos no CI. Regressão acima de 10% em relação à `main` precisa ser justificada no PR.

## Fluxo de desenvolvimento

1. Faça um fork do repositório e crie uma branch a partir da `main`:
   `feat/descricao-curta`, `fix/descricao-curta`, `docs/descricao-curta`.
2. Faça commits pequenos e focados.
3. Escreva as mensagens de commit no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/), em inglês:
   `feat(kernel): add tenant resolver`, `fix(fiscal): round ICMS base`, `docs: translate SECURITY`.
4. Assine cada commit (veja *DCO* abaixo).
5. Inclua ou atualize testes e documentação.
6. Abra um pull request e preencha o modelo.

### Ambiente local

As ferramentas de build ainda estão sendo definidas. Quando o primeiro código entrar, esta seção vai listar os comandos exatos. Os pré-requisitos previstos são:

- [.NET SDK](https://dotnet.microsoft.com/) (versão fixada no `global.json`)
- [PostgreSQL](https://www.postgresql.org/) ou Docker
- Opcional: [NATS](https://nats.io/), toolchain do Rust (motor tributário), Node.js (front-end)

### Diretrizes de código

- **Sem reflexão em tempo de execução** nos serviços: use source generators para que tudo funcione com Native AOT.
- Cada módulo é dono do próprio schema no PostgreSQL. Nenhum módulo lê ou grava os dados de outro diretamente; use APIs e eventos.
- Código escrito à mão fica para regra de negócio; o código repetitivo deve vir dos geradores do SDK.
- Siga o `.editorconfig` do repositório e rode o formatador antes de fazer commit.

## Revisão de pull requests

- É necessária a aprovação de pelo menos um mantenedor (veja [CODEOWNERS](.github/CODEOWNERS)).
- O CI precisa passar, incluindo as verificações do orçamento de recursos.
- Os mantenedores podem pedir ajustes; responda aos comentários ou envie as alterações.
- Fazemos squash-merge usando o título do PR, então mantenha-o no formato Conventional Commits.

## Developer Certificate of Origin (DCO)

Toda contribuição precisa ser assinada conforme o [Developer Certificate of Origin 1.1](https://developercertificate.org/). Ao assinar, você declara que escreveu a contribuição ou que tem o direito de enviá-la sob a licença do projeto.

Adicione a assinatura com `git commit -s`, que acrescenta:

```
Signed-off-by: Seu Nome <seu.email@exemplo.com>
```

Use seu nome real e um e-mail que seja seu. Para corrigir commits sem a assinatura: `git rebase --signoff main` e faça force-push da sua branch.

## Relatando problemas de segurança

**Não** abra issues públicas para vulnerabilidades. Siga a [política de segurança](SECURITY.pt-BR.md).

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a [GNU General Public License v3.0](LICENSE), a mesma licença do projeto.
