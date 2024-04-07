idades = list()

with open(file='banco.csv', mode='r', encoding='utf-8') as banco:
    linha = banco.readline()
    linha = banco.readline()
    while linha:
        lseparada = linha.split(sep=',')
        idade = lseparada[0]
        idade = int(idade)
        idades.append(idade)
        linha = banco.readline()

print(idades)

