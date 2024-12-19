import pandas as pd

brasil_df = pd.read_csv('./módulo - 13/brasil.csv', delimiter=';')

# Quais são as 10 cidades mais populosas do Brasil?
mais_populosas_df = brasil_df[[
    'cidade', 
    'populacao'
]].sort_values('populacao', ascending=False)[:10].reset_index(drop=True)


#Quais são as 5 cidades com a menor PIB per capita da região nordeste?
menor_pib_df = brasil_df[[
    'cidade', 
    'pib_percapita', 
    'regiao'
]].query('regiao == "NORDESTE"').sort_values('pib_percapita', ascending=False)[:5].reset_index(drop=True)


# Quais são as 15 cidades com maior PIB do estado de São Paulo?
maior_pib_df = brasil_df[[
    'cidade', 
    'pib', 
    'estado'
]].query('estado == "SAO PAULO"').sort_values('pib', ascending=False)[:15].reset_index(drop=True)


#Qual é o PIB do Estado de Santa Catarina?
santa_catarina_df = brasil_df[[
    'estado',
    'pib'
]].groupby('estado').sum().query('estado == "SANTA CATARINA"')


# Qual é a população da região sul?
populacao_sul_df = brasil_df[[
    'regiao',
    'populacao'
]].groupby('regiao').sum().query('regiao == "SUL"')


# Qual é o PIB per capita médio das cidades do Mato Grosso do Sul?
pib_mato_grosso_df = brasil_df[[
    'estado',
    'pib_percapita'
]].groupby('estado').mean().query('estado == "MATO GROSSO DO SUL"')


# Qual é a população do Brasil?
populacao_brasil = brasil_df[['populacao']].sum()
