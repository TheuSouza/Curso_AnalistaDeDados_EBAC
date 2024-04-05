from time import sleep
num = int(input('Digite um numero para calcular a tabuada: '))

for c in range(1, 11):
    sleep(0.5)
    print(f'{num} * {c} = {c * num}')