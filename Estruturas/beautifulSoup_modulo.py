from bs4 import BeautifulSoup

# Lendo arquivos HTML
pagina = BeautifulSoup(open('local do arquivo', mode='r'), features='html.parser')