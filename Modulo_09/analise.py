import extracao, visualizacao

try:
    extracao
except Exception as exc:
    print('Erro na Extração dos dados.')
    print(exc)
finally:
    visualizacao
    print('Gráficos criados com sucesso!')

