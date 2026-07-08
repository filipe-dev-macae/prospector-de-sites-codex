# Prospector de Sites para Codex

Plugin local Codex-first para rodar o ciclo:

**Achou -> Refez -> Publicou -> Ofertou.**

Ele ajuda a prospectar negocios bem avaliados com sites ruins, redesenhar paginas com estetica premium, gerar editor visual/comparador, publicar na HostGator e preparar propostas comerciais.

## Estrutura

- `plugins/prospector-de-sites/`: plugin Codex.
- `plugins/prospector-de-sites/.codex-plugin/plugin.json`: manifesto do Codex.
- `.agents/plugins/marketplace.json`: marketplace local deste repo.
- `plugins/prospector-de-sites/skills/`: skills usadas pelo Codex.
- `plugins/prospector-de-sites/scripts/`: utilitarios para editor, comparador e CSV.

## Uso no Codex

Instale o plugin pelo marketplace local deste repositorio e invoque:

- `$prospector-de-sites` para coordenar o fluxo completo.
- `$setup-prospector` para configurar assinatura, nichos e HostGator.
- `$prospeccao-maps` para buscar e qualificar leads.
- `$redesign-premium` para criar paginas, editor e comparador.
- `$deploy-hostgator` para publicar na HostGator.
- `$proposta-email` para preparar propostas.

## Dados locais

O fluxo usa arquivos locais como fonte da verdade:

- `prospector-config.json`
- `leads.md`
- `leads.csv`
- `sites/[slug]/[slug].html`
- `sites/[slug]/[slug]-editor.html`
- `comparar.html`
- `propostas/[slug].md`

A senha da HostGator nunca deve ser escrita no chat. O arquivo de config tem o campo `"senha": ""`, que deve ser preenchido manualmente no computador do usuario.

No primeiro uso, `$setup-prospector` abre um formulario guiado no chat para coletar os dados de uma vez e criar os arquivos locais iniciais.
