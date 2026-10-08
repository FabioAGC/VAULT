---
name: vault-reorg
description: Reestrutura pastas, tags e links do vault em lotes aprovados
version: 1.0.0
metadata:
  hermes:
    tags: [obsidian, organizacao]
    category: obsidian
    requires_toolsets: [terminal]
---
# Reorganização do vault

## When to Use
O usuário pede para reorganizar uma pasta, padronizar tags, criar MOCs, conectar notas ou processar o 12 - INBOX.

## Procedure
1. Conferir `git status`. Se houver mudanças não commitadas, pedir ao usuário para commitar antes.
2. Delimitar o lote: UMA pasta ou no máximo 30 notas por vez.
3. Ler as notas do lote e gerar um plano em .hermes/plans/ com 4 tabelas:
   - Movimentos: origem → destino
   - Renomeações: nome antigo → nome novo
   - Tags: nota → tags removidas / adicionadas (só tags de 99 - META/tags.md; propostas novas em seção separada)
   - Links: nota → [[links]] novos, e MOC de destino
4. Mostrar um resumo do plano e ESPERAR aprovação. O usuário pode aprovar só parte do plano.
5. Executar só o que foi aprovado. Para cada nota movida ou renomeada, buscar `[[nome antigo` no vault inteiro e atualizar os links (inclusive os com alias `|` e âncora `#`).
6. Reescrever o texto das notas no padrão STE SOMENTE se o usuário pedir explicitamente; por padrão, mexer só em frontmatter, tags e links.
7. Atualizar os MOCs afetados.
8. `git add -A && git commit -m "reorg: <lote>"`.

## Modo inbox
Para "processe o inbox": em cada nota de 12 - INBOX/ com status inbox → definir a pasta de destino, revisar tags, trocar status/processar por status/ok, linkar no MOC (tirar da seção Inbox do MOC) e mover. Seguir os passos 3–8.

## Pitfalls
- Mover arquivos fora do Obsidian NÃO atualiza links. O passo 5 é obrigatório.
- Nomes de nota duplicados em pastas diferentes deixam [[links]] ambíguos. Detectar e perguntar antes de mover.
- Nunca editar .obsidian/. Nunca apagar notas.
- Lotes grandes estouram o contexto e geram erros. Manter lotes pequenos.

## Verification
- `git diff --stat` coerente com o plano aprovado.
- Nenhum [[link]] apontando para nota inexistente nas notas do lote (buscar os alvos de cada link).
