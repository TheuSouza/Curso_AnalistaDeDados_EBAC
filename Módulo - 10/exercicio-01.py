from openpyxl import load_workbook
import csv

planilhas = load_workbook('banco.xlsx')
planilha = planilhas.active

dados = list()

cabecalho = next(planilha.values)

indice_inadimplentes = cabecalho.index('default')
indice_estado_civil = cabecalho.index('estado_civil')
indice_id = cabecalho.index('id')
indice_idade = cabecalho.index('idade')
indice_sexo = cabecalho.index('sexo')

dados = [(linha[indice_id], linha[indice_idade], linha[indice_sexo]) 
         for linha in planilha.values 
         if linha[indice_inadimplentes] == 1 and linha[indice_estado_civil] == 'solteiro']

with open(file='./credito.csv', mode='w', encoding='utf-8') as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=';')
    arquivo_csv.writerows([['id', 'idade', 'sexo']] + list(map(lambda linha: linha, dados)))