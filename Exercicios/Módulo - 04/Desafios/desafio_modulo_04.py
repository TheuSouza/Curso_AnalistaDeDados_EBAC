quantidade = int(input('Qual a quantidade de cds da sua coleção:'))
soma = 0
for i in range(quantidade):
    valor = float(input(f'Qual o valor do CD número {i + 1}º:'))
    soma += valor
print(f'A sua coleção tem um total de {quantidade} CDS\nVocê investiu um total de RS:{soma:.2f}\nMédia gasta em cada CD foi de {soma/quantidade:.2f}')
