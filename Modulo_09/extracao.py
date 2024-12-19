import os, json, time
from random import random
from datetime import datetime

import requests

URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'
cdi = None

for _ in range(0, 10):

    data_e_hora = datetime.now()
    data = datetime.strftime(data_e_hora, '%Y/%m/%d')
    hora = datetime.strftime(data_e_hora, '%H:%M:%S')
    
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.HTTPError as exc:
        print('Dado não encontrado, Continuando...')
        cdi = None
    except Exception as exc:
        print(f'Error, Parando a execução...{exc}')
    else:
        dado = json.loads(response.text)
        cdi = float(dado['taxa'].replace(',','.')) + (random() - 0.5)
    
    if os.path.exists('./Módulo - 09/taxa-cdi.csv') == False:
        with open(file='./Módulo - 09/taxa-cdi.csv', mode='w', encoding='utf8') as fp:
            fp.write('Data,Hora,Taxa\n')
    
    with open(file='./Módulo - 09/taxa-cdi.csv', mode='a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi}\n')
    
    time.sleep(2 + (random() - 0.5))

print('Sucesso!')

