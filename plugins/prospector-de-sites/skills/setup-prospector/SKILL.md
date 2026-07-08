---
name: setup-prospector
description: Configura o Prospector de Sites uma unica vez no Codex com uma experiencia guiada tipo formulario. Use quando o usuario quiser setup, configuracao inicial, assinatura, nichos padrao, cidade, quantidade de leads, modo de envio, HostGator, cPanel ou criar prospector-config.json.
---

# Setup do Prospector de Sites

Conduza uma configuracao inicial com cara de formulario. O objetivo e coletar tudo uma vez, criar os arquivos locais e deixar o usuario pronto para prospectar.

## Principio de UX

Na primeira execucao, nao saia fazendo perguntas soltas uma por vez. Mostre um bloco unico de formulario preenchivel, com defaults e opcoes marcaveis. Depois que o usuario responder, faca follow-up somente dos campos faltantes ou inconsistentes.

Use tom direto e de onboarding:

```markdown
Nao ha configuracao ainda. Vou montar um formulario para coletar seus dados de uma vez so.

## Prospector details

**Assinatura**
- Nome completo:
- Como quer se apresentar nas propostas:
- WhatsApp/telefone:

**Prospecção**
- Cidade/regiao padrao:
- Leads qualificados por busca: 10
- Nichos desejados: nutricionistas, psicologos, advogados, psiquiatras
- Outros nichos:

**Envio**
- Modo de envio: rascunho

**HostGator**
- Ja tem hospedagem/cPanel? sim/nao
- Usuario do cPanel:
- Dominio principal:
- Servidor ou IP:
- Pasta base para publicar: clientes

Preencha o que souber e envie. A senha da HostGator nao deve ser enviada no chat.
```

Se o usuario responder de forma livre, extraia os campos. Se responder parcialmente, mantenha os defaults e pergunte apenas o que impede criar o config.

## Arquivos criados

Criar ou atualizar na pasta de trabalho:

- `prospector-config.json`: preferencias e credenciais locais.
- `leads.md`: pipeline inicial vazio.
- `leads.csv`: cabecalhos para abrir em planilha.

Esses arquivos sao dados locais de uso e devem ficar fora do Git.

## Quando ja existe configuracao

Se `prospector-config.json` existir:

1. Ler o arquivo.
2. Mostrar resumo sem imprimir senha.
3. Perguntar se o usuario quer alterar assinatura, prospeccao, envio ou HostGator.
4. Atualizar somente os campos solicitados.

Nunca sobrescrever dados existentes sem confirmar.

## Campos e defaults

Coletar:

- assinatura: nome, apresentacao curta e WhatsApp/telefone;
- prospeccao: nichos, cidade/regiao e leads por busca;
- envio: `rascunho` ou `enviar direto`;
- HostGator: usuario do cPanel, dominio principal, servidor e pasta base.

Defaults:

- nichos: `nutricionistas`, `psicologos`, `advogados`, `psiquiatras`;
- leads por busca: `10`;
- modo de envio: `rascunho`;
- pasta base: `clientes`.

Se o usuario ainda nao tiver HostGator, salve os campos de HostGator vazios e prossiga. Publicacao pode ser configurada depois.

## Senha da HostGator

Nunca pedir senha no chat. Criar o config com:

```json
"senha": ""
```

Orientar o usuario a preencher esse campo diretamente no arquivo local somente quando for publicar.

## Formato do config

```json
{
  "assinatura": {
    "nome": "",
    "apresentacao": "",
    "whatsapp": ""
  },
  "prospeccao": {
    "nichos": ["nutricionistas", "psicologos", "advogados", "psiquiatras"],
    "cidade": "",
    "leadsPorBusca": 10
  },
  "envio": {
    "modo": "rascunho"
  },
  "hostgator": {
    "usuario": "",
    "dominio": "",
    "servidor": "",
    "senha": "",
    "pastaBase": "clientes"
  }
}
```

## Leads iniciais

Criar `leads.md`:

```markdown
# Leads Prospector

| # | Nome | Nota | Avaliacoes | E-mail | Telefone | Site atual | Motivo | Situacao | Status | URL nova |
| - | ---- | ---- | ---------- | ------ | -------- | ---------- | ------ | -------- | ------ | -------- |
```

Criar `leads.csv`:

```csv
#,Nome,Nota,Avaliacoes,E-mail,Telefone,Site atual,Motivo,Situacao,Status,URL nova
```

## Validacao final

Antes de terminar:

- validar se `prospector-config.json` e JSON valido;
- confirmar que o campo `senha` existe e esta vazio ou mascarado;
- confirmar que `leads.md` e `leads.csv` existem;
- explicar o proximo passo: usar `$prospeccao-maps` para buscar leads.
