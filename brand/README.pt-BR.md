[English](README.md) | **Português (Brasil)**

# Marca QuectoERP

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logo/quectoerp-logo-on-dark.svg">
  <img src="logo/quectoerp-logo.svg" alt="QuectoERP" height="64">
</picture>

Esta pasta guarda o logotipo, o favicon e os tokens de cor do QuectoERP. A marca vai mudar conforme o projeto cresce, então tudo aqui é **gerado** a partir de um único arquivo, o [`brand.json`](brand.json). Altere esse arquivo, rode o gerador, e todos os logotipos, ícones e tokens acompanham.

## A ideia

**quecto** (símbolo **q**, fator 10⁻³⁰) é o menor prefixo do Sistema Internacional de Unidades. O símbolo da marca é esse **q**, desenhado em traço único e geométrico. O ponto no alto, à direita, é o expoente, como em 10⁻³⁰: a notação da ciência e da medida. O nome aparece em minúsculas, `quecto` na cor de tinta, com `ERP` na cor de destaque.

O verde-petróleo passa estabilidade e calma, e mantém a marca longe do azul usado pela maioria dos ERPs e pela família de marcas "Quec-" da Quectel. Não use azul como cor da marca.

## Arquivos

| Caminho | Uso |
| --- | --- |
| `logo/quectoerp-logo.svg` | Logotipo principal (símbolo + nome) em fundo claro |
| `logo/quectoerp-logo-on-dark.svg` | Logotipo principal em fundo escuro |
| `logo/quectoerp-logo-mono-black.svg`, `-mono-white.svg` | Logotipo em uma cor (impressão, carimbo, relevo, fotos) |
| `logo/quectoerp-wordmark*.svg` | Só o nome, quando o símbolo já aparece por perto |
| `logo/quectoerp-symbol*.svg` | Só o símbolo: avatares, ícone de app, perfis em redes |
| `favicon/favicon.svg`, `favicon.ico`, `favicon-*.png` | Ícone da aba do navegador |
| `favicon/apple-touch-icon.png`, `icon-*.png`, `site.webmanifest` | Ícones de tela inicial e PWA |
| `tokens/colors.css` | Variáveis CSS para a interface, com tema claro e escuro |
| `tokens/colors.json` | Os mesmos tokens para código, ferramentas de design e outras plataformas |

### HTML do favicon

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
```

## Cores

| Papel | Token | Valor | Observações |
| --- | --- | --- | --- |
| Tinta | `--q-color-fg` | `#0F2A2A` | Texto, fundo do símbolo, nome em fundo claro |
| Petróleo | `--q-color-accent` | `#0F766E` | Botões, links, o `ERP` do logotipo. 5,5:1 sobre branco (WCAG AA para texto) |
| Menta | `--q-color-accent` (tema escuro) | `#5EEAD4` | O ponto do expoente e o destaque em fundo escuro. Claro demais para texto sobre branco |
| Névoa | `--q-color-paper` | `#E6F4F1` | Fundo suave para páginas de divulgação e áreas em destaque |

O `tokens/colors.css` também traz as escalas completas de 50 a 950 do petróleo e dos neutros (`--q-brand-*`, `--q-neutral-*`) e as cores de status (`--q-status-success|warning|danger|info`). Os tokens semânticos (`--q-color-*`) mudam para os valores escuros com `prefers-color-scheme` ou `data-theme="dark"`. Use os tokens semânticos nos componentes e as escalas só quando nenhum papel servir.

## Tipografia

O logotipo não depende de fonte: é desenhado em traços vetoriais. Para a interface e os documentos, use **Inter** para texto e **JetBrains Mono** para código e números em tabelas. As duas são gratuitas (SIL Open Font License). Estão no `brand.json` e saem como `--q-font-sans` e `--q-font-mono`.

## Uso do logotipo

- Deixe em volta do logotipo uma área livre igual à metade da altura do símbolo.
- Tamanho mínimo: símbolo com 16 px, logotipo completo com 96 px de largura na tela.
- Use os arquivos fornecidos. Não redesenhe, estique, gire, contorne, aplique sombra nem troque as cores fora das opções do `brand.json`.
- Sobre fotos ou fundos carregados, use o símbolo com fundo ou a versão em uma cor.
- Escreva o nome como **QuectoERP** no texto e `quectoerp` em código, pacotes e domínios.

## Como mudar a marca

Tudo fica no [`brand.json`](brand.json):

- `symbol`: a forma do q. `exponent` (ponto no alto à direita, como o expoente de 10⁻³⁰, atual), `particle` (ponto no meio do q) ou `limit` (a perna termina num pé, o chão da escala).
- `palette`: qual paleta de `palettes` usar. `teal` é a atual; `amber` e `indigo` estão prontas como alternativas. Para criar outra, informe `ink`, `accent` e `paper`, e se quiser um `highlight` mais claro para o ponto e para fundos escuros. O gerador calcula as escalas de 11 tons, escolhe os tons de destaque que respeitam o contraste mínimo e adapta o símbolo para fundo escuro.
- `status`, `typography` e `radius` guardam o resto.

Depois gere de novo:

```sh
python3 brand/scripts/build.py      # logotipos SVG, favicon.svg, manifesto e tokens (Python 3.8+, sem dependências)
node brand/scripts/rasterize.mjs    # ícones PNG e favicon.ico (Node 18+ e Playwright com Chromium)
```

Faça commit dos arquivos gerados junto com a mudança no `brand.json`. Não edite arquivos gerados à mão, porque o próximo build sobrescreve.

## Licença

O nome e o logotipo QuectoERP identificam o projeto. Os arquivos desta pasta fazem parte do repositório e seguem a licença dele, mas usar o nome ou o logotipo de forma que sugira apoio do projeto exige permissão dos mantenedores.
