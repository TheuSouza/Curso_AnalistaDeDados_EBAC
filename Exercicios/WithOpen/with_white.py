idades = [30, 33, 35, 30, 59, 35, 36, 39, 41, 43]

with open(file='./idades.csv', mode='w', encoding='utf-8') as fp:
    linha = 'idade' + '\n'
    fp.write(linha)
    for i in idades:
        linha = str(i) + '\n'
        fp.write(linha)

with open(file='./idades.csv', mode='a', encoding='utf-8') as fp:
    for i in idades:
        linha = str(i + 100) + '\n'
        fp.write(linha)





# Escreva seu código abaixo

quadrado_diferencas = map(lambda num: (num - media_aritmetica) ** 2, valor_emprestimos_filtrado)

soma_quadrado_diferencas = reduce(lambda x, y: x + y, quadrado_diferencas)

quantidade = len(list(valor_emprestimos_lista)) - 1
print(quantidade)

desvio_padrao_emprestimos = (soma_quadrado_diferencas / quantidade) ** 2

print(desvio_padrao_emprestimos)