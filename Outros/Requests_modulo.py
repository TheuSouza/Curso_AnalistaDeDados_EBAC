import requests
from requests.exceptions import Timeout, RequestException, HTTPError

conteudo = None
URL = 'http://www.google.com'

try:
    resposta = requests.get(URL)
    resposta.raise_for_status()

except HTTPError as err_http:
    print(f'Erro de HTTP: {err_http}')

except ConnectionError as err_conn:
    print(f'Erro de conexão: {err_conn}')

except Timeout as err_timeout:
    print(f'Tempo de resposta excedido: {err_timeout}')

except RequestException as err_req:
    print(f'Erro na requisição: {err_req}')

except Exception as exc:
    print(f'Ocorreu um erro inesperado: {exc}')

else:
    conteudo = resposta.text