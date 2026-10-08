# Roteiro de TCC — Estudo Comparativo: Bancos Relacionais Adaptados vs Bancos Vetoriais Nativos

## Contexto do projeto 

Este projeto de Claude serve de assistente para um Trabalho de Conclusão de Curso (TCC) cujo tema é:

> **Estudo comparativo de métricas de desempenho entre bancos de dados relacionais adaptados para busca vetorial (PostgreSQL/pgvector, MongoDB Atlas Vector Search, Redis/RediSearch) e bancos de dados vetoriais nativos (ChromaDB, Weaviate, Qdrant), utilizando um dataset a ser definido pelo autor.**

O Claude deve atuar como orientador técnico-metodológico: ajudar a estruturar o texto acadêmico (ABNT ou norma da instituição), revisar código de benchmark, discutir métricas, ajudar a interpretar resultados estatísticos e manter consistência entre os capítulos ao longo dos 3 meses.

**Bancos avaliados:**
- Adaptados: PostgreSQL + pgvector, MongoDB Atlas Vector Search, Redis + RediSearch
- Nativos: ChromaDB, Weaviate, Qdrant

**Dataset:** a ser escolhido pelo autor (ex.: SIFT1M, GloVe, GIST1M, ou um dataset de domínio próprio embeddado com um modelo como `all-MiniLM-L6-v2` ou `text-embedding-3-small`).

**Métricas centrais:**
- Qualidade de busca: Recall@k, Precision@k
- Desempenho: latência (p50/p95/p99), throughput (QPS)
- Custo operacional: tempo de indexação, uso de memória/disco, custo de escalabilidade
- Robustez: comportamento sob concorrência, atualização/exclusão de vetores (upsert), consistência

---

## Estrutura geral (12 semanas / 3 meses)

### **Mês 1 — Fundamentação e Preparação**

**Semana 1: Definição de escopo e revisão bibliográfica inicial**
- Delimitar pergunta de pesquisa e hipóteses
- Levantar 15-20 referências (papers ANN, HNSW, IVF, benchmarks ann-benchmarks.com, artigos dos próprios fornecedores)
- Escrever a Introdução preliminar (problema, justificativa, objetivos geral/específicos)

**Semana 2: Fundamentação teórica — bancos vetoriais**
- Estudar algoritmos de indexação: HNSW, IVF-Flat, IVF-PQ, ScaNN
- Descrever arquitetura de cada banco escolhido (como cada um implementa ANN)
- Rascunhar capítulo de Referencial Teórico (parte 1: fundamentos de busca vetorial)

**Semana 3: Fundamentação teórica — comparação arquitetural**
- Detalhar diferenças conceituais entre "banco relacional com extensão vetorial" vs "banco nativo vetorial"
- Discutir trade-offs esperados (transações ACID, joins, ecossistema vs performance pura, escalabilidade horizontal)
- Continuar Referencial Teórico (parte 2)

**Semana 4: Escolha do dataset e definição da metodologia**
- Selecionar dataset final (tamanho, dimensionalidade, domínio)
- Escrever capítulo de Metodologia: ambiente de testes, hardware/cloud usado, ferramentas de medição, protocolo de execução (nº de repetições, warm-up, etc.)
- **Entregável do mês 1:** capítulos de Introdução + Referencial Teórico + Metodologia (rascunho)

---

### **Mês 2 — Implementação e Coleta de Dados**

**Semana 5: Setup do ambiente**
- Provisionar os 6 bancos (Docker Compose recomendado para padronizar recursos)
- Padronizar configurações comparáveis (mesma dimensão de vetor, mesmo tipo de índice quando aplicável)
- Criar scripts de carga (embedding + ingestão) reutilizáveis

**Semana 6: Benchmark de indexação e ingestão**
- Medir tempo de indexação, uso de memória/disco por banco
- Testar ingestão em lote vs incremental
- Registrar resultados em planilha/CSV estruturado

**Semana 7: Benchmark de busca (qualidade + latência)**
- Rodar queries de teste medindo Recall@k e Precision@k
- Medir latência p50/p95/p99 para diferentes tamanhos de k
- Testar diferentes cargas de concorrência (1, 10, 50, 100 clientes simultâneos) com ferramenta como Locust ou script customizado

**Semana 8: Testes de robustez e consolidação dos dados**
- Testar atualização/exclusão de vetores (upsert) e impacto na performance
- Testar escalabilidade (aumento de dataset, réplicas quando suportado)
- Consolidar todos os dados coletados; começar tratamento estatístico
- **Entregável do mês 2:** dataset de resultados completo + gráficos preliminares

---

### **Mês 3 — Análise, Escrita e Revisão**

**Semana 9: Análise estatística dos resultados**
- Aplicar testes estatísticos (ex.: ANOVA, teste t) se aplicável para validar diferenças significativas
- Construir gráficos comparativos (barras, boxplots, radar chart) por métrica
- Escrever capítulo de Resultados

**Semana 10: Discussão dos resultados**
- Interpretar resultados à luz do referencial teórico
- Discutir cenários de uso ideais para cada tipo de banco (ex.: quando vale a pena usar pgvector vs Qdrant)
- Escrever capítulo de Discussão

**Semana 11: Conclusão e revisão geral**
- Escrever Conclusão, limitações do estudo e trabalhos futuros
- Revisar coerência entre Introdução, Objetivos e Conclusão
- Revisão de formatação ABNT (citações, normalização de tabelas/figuras)

**Semana 12: Revisão final e preparação da defesa**
- Revisão ortográfica e de coesão textual completa
- Preparar slides de apresentação
- Simular perguntas da banca (pontos fracos prováveis: tamanho do dataset, generalização dos resultados, viés de configuração)
- **Entregável final:** TCC completo + apresentação

---

## Checklist de métricas por banco (usar como tabela de coleta)

| Métrica                | pgvector | Atlas Vector Search | RediSearch | ChromaDB | Weaviate | Qdrant |
| ---------------------- | -------- | ------------------- | ---------- | -------- | -------- | ------ |
| Tempo de indexação     |          |                     |            |          |          |        |
| Uso de memória (build) |          |                     |            |          |          |        |
| Uso de disco           |          |                     |            |          |          |        |
| Recall@10              |          |                     |            |          |          |        |
| Latência p50 (ms)      |          |                     |            |          |          |        |
| Latência p95 (ms)      |          |                     |            |          |          |        |
| Latência p99 (ms)      |          |                     |            |          |          |        |
| QPS (throughput)       |          |                     |            |          |          |        |


---

## Riscos e mitigação

- **Configurações não comparáveis entre bancos** → documentar explicitamente todos os parâmetros de índice usados e justificar escolhas de equivalência.
- **Hardware/cloud heterogêneo** → rodar tudo no mesmo ambiente (mesma VM/container specs) para isolar a variável de software.
- **Dataset pequeno demais para generalizar** → escolher dataset com pelo menos 100k-1M vetores, ou justificar explicitamente a limitação.
- **Prazo apertado na escrita** → começar a escrever cada capítulo assim que os dados daquele bloco estiverem prontos, não deixar tudo para o mês 3.

---