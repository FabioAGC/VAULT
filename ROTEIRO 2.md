**Abertura**

- Olá, pessoal! Eu sou o Fabio, esse é o Bruno e esse é o Gustavo.
- Nosso TCC se chama _Arquiteturas para Busca de Dados Vetoriais: Um Estudo Comparativo entre Bancos de Propósito Geral Adaptados contra Bancos Vetoriais Nativos_.
- Nome grande, mas a ideia é simples.

**Por que escolhemos esse tema**

- Com a alta da IA, a gente percebeu que ela não entende texto do jeito que a gente entende.
	Precisa de um contexto em milisegundo para dar uma resposta 
	Bancos vetorias são performaticos
- A pergunta prática para uma empresa é: compensa adotar uma tecnologia nova ou o banco que ela já usa resolve?
- Só que não dá pra medir só quem é mais rápido, porque um banco pode ser rápido justamente por estar errando mais.
- Daí veio a ideia de montar os seis bancos nas mesmas condições de hardware e testar de forma justa.

**O resultado que pretendemos**

- Uma comparação justa entre os seis bancos.

utilizando as metricas definidas

Entregar graficos e tabelas

Ao fim recomendações sobre qual banco usar em qual cenario e descobrir se realmente existe alguma diferença entre usar bancos vetoriais nativos e bancos vetoriais adaptados

**O que já fizemos**
lemos artigos sobre o tema
- Decisões de escopo: definimos os seis bancos.
- PostgreSQL, o Redis e o Cassandra  VS weaviate qdrant e chromaDB
- Desenho do experimento: todos os bancos em Docker, com os mesmos limites (8 CPUs e 12 GB de RAM por container).
  escolhemos um data set, vetorizamos e segmentamos em 3 recortes um de 100k, um de 500k e um 1M
  
- Criamos um script proprio para termos as nossas proprias metricas
  e Rodamos um piloto utilizando o qdrant e o recorte de 100k
mostrar resultado piloto

Feito a introdução , fundamentos da busca vetorial e da arquitetura
Finalizando a metodologia no artigo

**O que falta fazer**

- Calibrar os parâmetros de cada banco até atingir os 95% de acerto.
   Calibrar os filtros e as metricas 
- Rodar os testes em cada um dos bancos.
- Coletar as métricas.
- Fazer a análise estatística pra garantir que as diferenças são reais e não sorte.
- Escrever os capítulos de Resultados, Discussão e Conclusão.
- Revisão final.

**Fechamento**

- No fim, a ideia é responder com dados, e não com achismo ou propaganda de fornecedor, se vale a pena trocar de banco ou se o que você já tem resolve.
- É isso, obrigado!