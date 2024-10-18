import csv

gasolina = [[1,5.11],[2,4.99],[3,5.02],[4,5.21],[5,5.07],[6,5.09],[7,5.13],[8,5.12],[9,4.94],[10,5.03]]

with open('./Módulo - 17/gasolina.csv', mode='w', encoding='utf-8') as file:
    file_csv = csv.writer(file, delimiter=';')
    file_csv.writerows([['dia', 'venda']] + list(map(lambda rows: rows, gasolina)))