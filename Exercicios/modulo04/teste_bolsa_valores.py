import wget
import zipfile
import os
import pandas as pd
import seaborn as sns

# wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')  # Faz o download no formato Zip

 # with zipfile.ZipFile('./dados.zip', 'r') as fp:  # Abre arquivo Zip em modo de leitura
  # fp.extractall('./dados')  # Descompacta arquivo em uma pasta

# os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')  # Renomeia o arquivo

df = pd.read_csv('./dados/dow_jones_index.csv')

df.columns.to_list()

linhas, colunas = df.shape
print(f'Numeros de linha do data frame {linhas}')
print(f'Numeros de colunas do data frame {colunas}')

df_ko = df[df['stock'] == 'KO']

df_ko = df_ko[['date','open','close','high','low']]

for col in ['open','close','high','low']:
    df_ko[col] = df_ko[col].apply(lambda value: float(value.replace('$','')))

df_ko.head(n=10)


plot = sns.lineplot(x='date', y='open', data=df_ko)
plot.tick_params(axis='x', labelrotation=45)

plot2 = sns.lineplot(x='date', y='value', hue='variable', data=(pd.melt(df_ko, ['date'])))
plot.tick_params(axis='x', labelrotation=45)

plot.figure.savefig('./ko.png')
