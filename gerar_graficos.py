import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- OS SEUS DADOS RECOLHIDOS ---
data = {
    (1, 10):   {'RPS': 3.8,   'Mediano': 180},
    (1, 100):  {'RPS': 43.8,  'Mediano': 420},
    (1, 1000): {'RPS': 130.7, 'Mediano': 3700},
    (2, 10):   {'RPS': 4.8,   'Mediano': 170},
    (2, 100):  {'RPS': 38.9,  'Mediano': 390},
    (2, 1000): {'RPS': 154.9, 'Mediano': 3200},
    (3, 10):   {'RPS': 4.8,   'Mediano': 180},
    (3, 100):  {'RPS': 41.5,  'Mediano': 450},
    (3, 1000): {'RPS': 139.7, 'Mediano': 3400},
}

# Organiza os dados numa tabela (DataFrame)
df = pd.DataFrame.from_dict(data, orient='index')
df.index = pd.MultiIndex.from_tuples(df.index, names=['Instâncias', 'Usuários'])
df.reset_index(inplace=True)

# --- GRÁFICO 1: Tempo de Resposta vs. Número de Usuários ---
# (Semelhante ao primeiro gráfico do seu PDF [cite: 91])

# Pivotar a tabela para o formato do gráfico
df_pivot_tempo = df.pivot(index='Usuários', columns='Instâncias', values='Mediano')
df_pivot_tempo = df_pivot_tempo.reindex([10, 100, 1000]) # Garante a ordem correta

# Plotar
ax1 = df_pivot_tempo.plot(
    kind='bar',
    figsize=(10, 6),
    title='Desempenho: Tempo de Resposta Mediano vs. Carga de Usuários',
    width=0.8
)
ax1.set_ylabel('Tempo de Resposta (ms)')
ax1.set_xlabel('Número de Usuários Simulados')
ax1.legend(title='Nº de Instâncias')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0) # Mantém os nomes do eixo X retos
plt.tight_layout()
plt.savefig('grafico_tempo_resposta.png') # Salva a imagem
print("Gráfico 'grafico_tempo_resposta.png' gerado com sucesso.")


# --- GRÁFICO 2: Requisições por Segundo vs. Número de Instâncias ---
# (Semelhante ao segundo gráfico do seu PDF [cite: 105])

# Pivotar a tabela para o formato do gráfico
df_pivot_rps = df.pivot(index='Instâncias', columns='Usuários', values='RPS')

# Plotar
ax2 = df_pivot_rps.plot(
    kind='bar',
    figsize=(10, 6),
    title='Escalabilidade: Requisições por Segundo (RPS) vs. Instâncias',
    width=0.8
)
ax2.set_ylabel('Requisições por Segundo (RPS)')
ax2.set_xlabel('Número de Instâncias do WordPress')
ax2.legend(title='Carga (Usuários)')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0) # Mantém os nomes do eixo X retos
plt.tight_layout()
plt.savefig('grafico_rps.png') # Salva a imagem
print("Gráfico 'grafico_rps.png' gerado com sucesso.")

print("\n--- Análise dos Resultados ---")
print("Gráfico 1 (Tempo de Resposta): Mostra como o tempo de resposta do site piora (aumenta) com mais usuários. Idealmente, adicionar instâncias (barras laranja e verde) deve manter este tempo baixo, especialmente no teste de 1000 usuários.")
print("Gráfico 2 (RPS): Mostra quantos pedidos o sistema aguenta. Idealmente, com mais instâncias (indo da barra 1 para 2 e 3), o sistema deve aguentar mais RPS, especialmente nos testes de 100 e 1000 usuários.")