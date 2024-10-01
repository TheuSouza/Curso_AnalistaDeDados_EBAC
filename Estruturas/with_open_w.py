import csv


# Escrevendo arquivo CSV
with open(file='./Nome do Arquivo que vai ser salvo.csv', mode='w', encoding='utf-8') as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=';')
    arquivo_csv.writerows([['Cabeçalho do arquivo','id', 'idade', 'sexo']] + list(map(lambda linha: linha, Nossa lista com dados)))