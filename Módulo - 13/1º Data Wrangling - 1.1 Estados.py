from bs4 import BeautifulSoup
import csv

conteudo = list()

soup = BeautifulSoup(open('./módulo - 13/estados-bruto.xml', 'r'), 'xml')

estados = soup.find_all('ESTADO')

for estado in estados:
    
    '''
    Ao fazer o for obtive essa lista: 
    ['\n', '1', '\n', 'ACRE', '\n', '16', '\n', 'AC', '\n', 'NORTE', '\n'].

    Fiz um fatiamento onde continham os índices de interesse [3, -1] Obtendo uma nova lista.
    ['ACRE', '\n', '16', '\n', 'AC', '\n', 'NORTE']

    Deletei o índice de IDCAPITAL localizado em dados[2] Obtendo uma nova lista.
    ['ACRE', '\n', '\n', 'AC', '\n', 'NORTE']

    Removei os espaços em branco da lista "\n" usando função lambda.
    Sobrando somente os valores de interesse: ['ACRE', 'AC', 'NORTE']
    Por último fiz o append da lista dentro da lista conteudo.
    '''
    
    dados = estado.get_text(';').split(';')[3:-1]
    del dados[2]
    dados = list(filter(lambda valor: valor.strip(), dados))
    conteudo.append(dados)

with open('./módulo - 13/estados-limpo.csv', 'w', encoding='utf-8') as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=';')
    arquivo_csv.writerows([['estado', 'sigla', 'região']] 
                          + list(map(lambda valor: valor, conteudo)))

