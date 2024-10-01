import requests
from requests.exceptions import HTTPError

conteudo = None
URL = 'http://www.google.com'

try:
    resposta = requests.get(URL)
    resposta.raise_for_status()
except HTTPError as exc:
    print(exc)
else:
    conteudo = resposta.text

