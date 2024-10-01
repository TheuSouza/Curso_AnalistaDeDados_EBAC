import pandas as pd
from unicodedata import normalize

'''
Criei uma lista "header" com as colunas de interesse,
Coloquei a lista na ordem que o exercício pede,
Fiz a leitura somente delas para ser mais rápido e poupar memória...
Utilizei novamente para ordenar as colunas do dataframe,
Renomeei as colunas do dataframe,
Dropei uma linha do data frame onde PERNAMBUCO não tinha cidade.
Retirei os acentos dos estados para ficar compatível com a coluna
estados do arquivo estados-limpo.csv
Por último salvei o arquivo cidades-limpo.csv
'''

header = ['UF', 'nome', 'Pop_est_2009', 'PIB', 'PIB_percapita']

cidades_df = pd.read_csv('./módulo - 13/cidades-bruto.csv', usecols=header)
cidades_df = cidades_df[header]
cidades_df.columns = ['estado', 'cidade', 'populacao', 'pib', 'pib_percapita']
cidades_df = cidades_df.dropna()

cidades_df['estado'] = cidades_df['estado'].apply(
    lambda x: normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII'))

cidades_df.to_csv('./módulo - 13/cidades-limpo.csv', sep=';', index=False)