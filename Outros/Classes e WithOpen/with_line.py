conteudo = list()
with open(file='banco.csv', mode='r', encoding='utf-8') as banco:
    linha = banco.readline()
    while linha:
        conteudo.append(linha)
        linha = banco.readline()

for linha in conteudo:
    print(linha)