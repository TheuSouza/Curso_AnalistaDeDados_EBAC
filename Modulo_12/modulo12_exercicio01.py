from bs4 import BeautifulSoup
import csv

pagina  = BeautifulSoup(open('fortune.html', mode='r'), 'html.parser')
conteudo = list()

#Tomei a liberdade de pegar uma div diferente, para reduzir a quantidade de linhas do exercício...
linhas = pagina.find_all('div', class_ = 'rt-tr-group')

for linha in linhas:
    colunas = linha.get_text(';').split(';')
    conteudo.append(colunas)

header = [
  'rank', 
  'name', 
  'revenues', 
  'revenues-percent-change', 
  'profits', 
  'profits-percent-change', 
  'assets', 
  'market-value',
  'employees'
]

with open(file='./fortune.csv', mode='w', encoding='utf-8') as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=';')
    arquivo_csv.writerows([header] + list(map(lambda linha: linha, conteudo)))
    
