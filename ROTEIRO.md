# introduz os nossos nomes : bruno gustavo e fabio

# nome do tcc : Arquiteturas para Busca de Dados Vetoriais: Um Estudo Comparativo entre Bancos de Propósito Geral Adaptados contra Bancos Vetoriais Nativos

# - porque escolhemos fazer esse tema ? 

hoje em dia com a alta da IA chegamos a conclusão que ela não entende texto do jeito que a gente entende. Ela transforma cada frase num vetor, que é basicamente uma lista com centenas de números que representam o _significado_ daquele texto. Aí, quando você faz uma pergunta, o sistema precisa achar, no meio de milhões desses vetores, quais são os mais parecidos com a sua pergunta. E precisa fazer isso em milissegundos. Só que responder isso direito não é muito simples. Não dá pra só medir quem é mais rápido, porque um banco pode ser rápido justamente por estar errando mais. Então a gente teve a ideia de montar seis bancos nas mesmas condições de hardware com a curiosidade de testar quais deles perfomam melhor , bancos tradicionais que ganharam extensões (PostgreSQL com pgvector, Redis, Cassandra) contra bancos nativos criados só pra isso (Qdrant, Weaviate, ChromaDB). A pergunta prática é se compensa adotar tecnologia nova ou se o banco que a empresa já usa resolve.  

# - resultado do que pretendemos :

O resultado principal é uma comparação justa entre os seis bancos. Expliquem que o diferencial é a metodologia de iso-recall: primeiro igualamos a precisão de todos (Recall@10 de pelo menos 95%), e só depois comparamos velocidade, porque um banco rápido que erra mais não é realmente mais rápido.
Os entregáveis concretos são as curvas de recall versus latência de cada banco, uma tabela com tempo de indexação, memória, disco, latência p50/p95/p99 e QPS, o comportamento com filtros, e, no fim, recomendações de qual tipo de banco faz sentido para cada cenário de uso.

# - o que ja fizemos :

Primeiro, as decisões de escopo Segundo, o desenho do experimento: todos os bancos rodando em Docker com os mesmos limites (8 CPUs e 12 GB de RAM por container), um de cada vez em terceiro ja fizemos o codigo (ler o read.me)

# - o que nos falta fazer :

calibrar os parâmetros até atingir o recall alvo, rodar os testes em cada um dos bancos , retirar as métricas, e por fim a análise estatística, os capítulos de Resultados, Discussão e Conclusão e a revisão final. 
