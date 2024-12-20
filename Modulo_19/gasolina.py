import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abrindo CSV e trasformando em DataFrame
gasolina_df = pd.read_csv('./Módulo - 19/gasolina.csv', delimiter=';')

# Determinando o tamanho da figura
plt.figure(figsize=(12.8, 7.2))

# Plot do gráfico de linhas
grap = sns.lineplot(data=gasolina_df, x='dia', y='venda', color='red')

# Adicionando título e rótulos
plt.title('Preço médio gasolina São Paulo - Julho 2021', fontsize=16, pad=15)
plt.xlabel('Dia', fontsize=12, labelpad=15)
plt.ylabel('Preço', fontsize=12, labelpad=15)

# Adicionando linhas de referência
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Mostrando gráfico
plt.show()

# Salvando figura
grap.figure.savefig('./Módulo - 19/gasolina.png', bbox_inches='tight')