import math

def soma(a,b):
    print(f'A Soma de {a} + {b} = {a + b}')

def subtracao(a, b):
    print(f'A Subtracao de {a} - {b} = {a - b}')

def multiplicacao(a, b):
    print(f'A Multiplicacao de {a} * {b} = {a * b}')

def divisao(a, b):
    print(f'A Divisao de {a} / {b} = {a / b:.2f}')

def potencia(a, b):
    print(f'A Potencia de {a} ** {b} = {a ** b:.2f}')

def raizq(a):
    print(f'A Raz quadrada de {a} = {a ** 0.5}')

def logaritmo(a, b):
    print(f'O Log de {a} com base {b} = {math.log(a, b)}')

def header01(txt):
    print('==' * 20)
    print(f'{txt:^40}')
    print('==' * 20)

def header02(txt):
    print('--' * 20)
    print(f'{txt:^40}')
    print('--' * 20)