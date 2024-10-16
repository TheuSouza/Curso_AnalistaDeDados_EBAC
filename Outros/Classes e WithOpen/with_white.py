idades = [30, 33, 35, 30, 59, 35, 36, 39, 41, 43]

with open(file='idades.csv', mode='w', encoding='utf-8') as fp:
    linha = 'idade' + '\n'
    fp.write(linha)
    for i in idades:
        linha = str(i) + '\n'
        fp.write(linha)

with open(file='idades.csv', mode='a', encoding='utf-8') as fp:
    for i in idades:
        linha = str(i + 100) + '\n'
        fp.write(linha)
