import pandas as pd

'''
Fiz a leitura dos dois arquivos...
Fiz o merge usando inner mais independente do opção o resultado era o mesmo.
Por último salvei o arquivo.csv...
'''

estados_df = pd.read_csv('./módulo - 13/estados-limpo.csv', delimiter=';')
cidades_df = pd.read_csv('./módulo - 13/cidades-limpo.csv',delimiter=';')

brasil_df = pd.merge(estados_df, cidades_df, on='estado', how='inner')

brasil_df.to_csv('./módulo - 13/brasil.csv', sep=';', index=False)





