---
name: prospeccao-maps
description: Prospecta clientes no Google Maps para o Prospector de Sites. Use quando o usuario quiser buscar clientes, achar leads, qualificar negocios bem avaliados com sites ruins, avaliar qualidade de sites de terceiros, gerar leads.md ou exportar leads.csv.
---

# Prospecção no Google Maps

Objetivo: encontrar negocios com boa reputacao e site fraco. O contraste entre nota alta e presenca digital ruim vira o argumento da proposta.

## Perfil do lead ideal

- Nota `>= 4.7` no Google e `>= 40` avaliacoes.
- Site proprio ativo, mas ruim.
- E-mail publico no perfil ou no site.
- Nichos prioritarios: nutricionistas, psicologos, advogados, psiquiatras, dentistas e fisioterapeutas.

## Filtros eliminatorios

Aplicar nesta ordem e sempre registrar o descarte em `leads.md`:

1. Sem site proprio: descartar. Instagram, Facebook, WhatsApp, Doctoralia, iFood, Linktree e diretorios nao contam.
2. Site bom: descartar. Se a pagina ja e moderna, responsiva e bem estruturada, nao ha dor clara.
3. Sem e-mail publico: descartar. Procurar no perfil, contato, rodape, politica de privacidade e HTML visivel.

## Fluxo Codex-first

1. Ler `prospector-config.json`. Se nao existir, usar a skill `prospector-de-sites` para setup.
2. Ler `leads.md`, se existir, e excluir negocios ja avaliados.
3. Definir nicho e cidade pelos argumentos do usuario ou pelos padroes do config.
4. Usar navegador disponivel no Codex/Chrome quando possivel para abrir o Google Maps e buscar `"[nicho] em [cidade]"`.
5. Se a automacao de navegador nao estiver disponivel, orientar coleta manual assistida: o usuario fornece nomes/URLs/dados e o Codex qualifica e registra.
6. Avaliar ate 25 estabelecimentos ou ate atingir a meta de leads qualificados.
7. Para cada candidato, abrir o site, avaliar qualidade e coletar dados publicos.

## Avaliacao de site ruim

Qualifica quando houver pelo menos 2 sinais objetivos:

- nao responsivo em celular;
- layout datado, fontes pobres, imagens esticadas ou cores berrantes;
- sem hierarquia visual ou caminho claro de leitura;
- CTA ausente ou escondido;
- lentidao, sliders pesados ou plugins antigos;
- conteudo abandonado, copyright antigo ou links quebrados;
- template generico com secoes vazias ou lorem ipsum.

Registrar o motivo com frase verificavel, por exemplo: `nao responsivo + sem CTA; telefone aparece apenas no rodape`.

## Dados a coletar

Para cada avaliado, qualificado ou descartado:

- numero;
- nome;
- nota;
- quantidade de avaliacoes;
- e-mail;
- telefone/WhatsApp;
- site atual;
- motivo;
- situacao (`Qualificado` ou `Descartado: motivo`);
- status (`novo` para qualificados; vazio ou `descartado` para descartados);
- URL nova;
- 2 ou 3 trechos curtos de avaliacoes reais, quando coletados.

## Saida local obrigatoria

- Atualizar `leads.md` como fonte principal de trabalho.
- Regenerar `leads.csv` para importacao manual em Google Sheets ou outro editor de planilha. Se `leads.md` estiver em tabela Markdown, usar `scripts/export-leads-csv.py`.
- Nunca criar duplicatas em novas rodadas.
- Ordenar por potencial: melhor nota, mais avaliacoes e pior site primeiro.

## Boas praticas

- Coletar apenas dados publicos necessarios para proposta comercial.
- Se houver poucos resultados, sugerir nicho alternativo ou cidade vizinha.
- Fechar abas de sites ja avaliados quando usar navegador.
- Ao final, mostrar tabela resumida e sugerir redesenhar os melhores leads.
