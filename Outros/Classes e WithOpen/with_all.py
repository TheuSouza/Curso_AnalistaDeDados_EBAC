conteudo = None
with open(file='banco.csv', mode='r', encoding='utf-8') as banco:
    conteudo = banco.read()
print(conteudo)