import pandas as pd

fortune_df = pd.read_csv('fortune.csv', sep=';')

#Criei uma lista com os nomes das colunas para a linha da função lambda não ficar muito longa... 
#colunas_float = ['revenues', 'profits', 'assets', 'market-value', 'employees']
#colunas_percent = ['revenues-percent-change', 'profits-percent-change']
header = [
  'revenues', 
  'revenues-percent-change', 
  'profits', 
  'profits-percent-change', 
  'assets', 
  'market-value',
  'employees'
]

#Substitui alguns valores das linhas que tinham '-' por 0 para conseguir trasformar os valores em Float64...
fortune_df.replace('-', 0, inplace=True)

#Fiz a substituição dos símbolos por '' e das , por '' e por fim trasformei em Float64...
fortune_df[header] = fortune_df[header].replace('[$%,]', '', regex=True).astype(float)

fortune_df.to_csv('fortune-limpo.csv', index=False, sep=';')

#Rodando o código você pode abrir o novo arquivo .csv e verificar que todos os valores estão com seus valores no formato correto...
data_df = pd.read_csv('fortune-limpo.csv', sep=';')
print(data_df.head())
print(data_df.info())

