from openpyxl import load_workbook
import json

planilhas = load_workbook('banco.xlsx')
planilha = planilhas.active

credito = dict()

cabecalho = next(planilha.values)

indice_tipo_cartao = cabecalho.index('tipo_cartao')
indice_escolaridade = cabecalho.index('escolaridade')

tipo_cartao = [linha[indice_tipo_cartao] for linha in planilha.values if linha[indice_tipo_cartao] != 'tipo_cartao']
escolaridade = [linha[indice_escolaridade] for linha in planilha.values if linha[indice_escolaridade] != 'escolaridade']

tipo_cartao = set(tipo_cartao)
escolaridade = set(escolaridade)

tipo_cartao = list(tipo_cartao)
escolaridade = list(escolaridade)

credito['tipo_cartao'] = tipo_cartao
credito['escolaridade'] = escolaridade

credito_json = json.dumps(credito, indent=4)
print(credito_json)