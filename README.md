\# Atividade: Teste de Carga com Locust no WordPress



\[cite\_start]Este projeto realiza testes de carga numa arquitetura WordPress de alta disponibilidade (com Nginx e múltiplas instâncias), conforme configurado no Trabalho 2\[cite: 4]. \[cite\_start]O objetivo é avaliar o desempenho e a escalabilidade da aplicação \[cite: 75] \[cite\_start]usando a ferramenta de testes Locust\[cite: 3].



\## Metodologia do Teste



\[cite\_start]A avaliação foi dividida em 3 cenários de arquitetura (1, 2 e 3 instâncias do WordPress)\[cite: 82]. \[cite\_start]Para cada arquitetura, foram executados 3 testes de carga simulando 10, 100 e 1000 utilizadores simultâneos\[cite: 82].



\[cite\_start]Os utilizadores simulados pelo Locust (definidos em `locustfile.py`) acederam aleatoriamente a três tipos de posts, criados para simular diferentes cargas de trabalho, conforme solicitado\[cite: 78, 79, 80]:

1\.  Um post com uma imagem de ~1MB.

2\.  Um post com um ficheiro de texto de ~400KB.

3\.  Um post com uma imagem de ~300KB.



\## Ficheiros de Configuração



\* \*\*`docker-compose.yml`\*\*: Contém a definição dos 6 serviços (1 DB, 3 WordPress, 1 Nginx, 1 Locust).

\* \*\*`nginx/nginx.conf`\*\*: Configuração do Nginx para atuar como balanceador de carga.

\* \*\*`locustfile.py`\*\*: Script Python que define o comportamento dos utilizadores virtuais no teste.

\* \*\*`gerar\_graficos.py`\*\*: Script Python (usando Pandas e Matplotlib) para processar os dados brutos e gerar os gráficos de resultados.



---



\## Resultados Finais: Análise dos Gráficos



Abaixo estão os gráficos finais que comparam o desempenho da arquitetura sob diferentes cargas e configurações.



\### Gráfico 1: Tempo de Resposta vs. Carga de Utilizadores



Este gráfico mostra o tempo de resposta mediano (em milissegundos) que os utilizadores experienciaram. Valores mais baixos são melhores.



!\[Gráfico de Tempo de Resposta](grafico\_tempo\_resposta.png)



\*\*Análise:\*\*

\* Com cargas baixas (10 e 100 utilizadores), o desempenho é excelente em todas as arquiteturas.

\* No teste de stress com \*\*1000 utilizadores\*\*, vemos claramente os benefícios da escalabilidade. A arquitetura com 1 instância (barra azul) teve um tempo de resposta muito alto (3700ms). Ao adicionar uma segunda instância (barra laranja), o tempo de resposta caiu para 3200ms, mostrando que a carga foi distribuída.



\### Gráfico 2: Requisições por Segundo (RPS) vs. Instâncias



Este gráfico mostra a capacidade total do sistema (quantas requisições por segundo ele aguentou). Valores mais altos são melhores.



!\[Gráfico de Requisições por Segundo](grafico\_rps.png)



\*\*Análise:\*\*

\* Este gráfico prova o conceito de escalabilidade horizontal.

\* No teste de \*\*1000 utilizadores\*\*, a arquitetura com 1 instância (barra 1) conseguiu processar \*\*130.7 RPS\*\*.

\* Ao adicionar uma segunda instância (barra 2), a capacidade do sistema aumentou para \*\*154.9 RPS\*\*, provando que o Nginx distribuiu a carga e a segunda instância ajudou a processar mais pedidos.

\* \*(Nota: O desempenho com 3 instâncias foi ligeiramente inferior ao de 2, sugerindo que o "gargalo" do sistema pode ter passado a ser outro componente, como o próprio Nginx ou o contentor da base de dados, que era único.)\*

