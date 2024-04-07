import arg


while True:
    arg.header01('Projeto Calculadora')
    print('  1 - Somar')
    print('  2 - Subtrair')
    print('  3 - Multiplicar')
    print('  4 - Dividir')
    print('  5 - Potencia')
    print('  6 - RaizQ')
    print('  7 - Logaritmo')
    print('~~' * 20)
    while True:
        opcao = int(input('Digite a opção desejada: '))
        if opcao > 0 and opcao < 8:
            break
        else:
            print('\033[1;31mOpção inválida. Tente novamente.\033[0m')
            
    
    if opcao == 1:
        arg.header02('Somar')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        arg.soma(num1, num2)
    elif opcao == 2:
        arg.header02('Subtrair')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        arg.subtracao(num1, num2)
    elif opcao == 3:
        arg.header02('Multiplicar')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        arg.multiplicacao(num1, num2)
    elif opcao == 4:
        arg.header02('Dividir')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        arg.divisao(num1, num2)
    elif opcao == 5:
        arg.header02('Potencia')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo Expoente: '))
        arg.potencia(num1, num2)
    elif opcao == 6:
        arg.header02('RaizQ')
        num1 = float(input('Digite o número: '))
        arg.raizq(num1)
    elif opcao == 7:
        arg.header02('Logaritmo')
        num1 = float(input('Digite o número: '))
        while True:
            num2 = float(input('Digite a base: '))
            if num2 > 0 and num2 != 1:
                break
            else:
                print('Por favor, Digite uma base válida (maior que 0 e diferente de 1).')
        arg.logaritmo(num1, num2)
    
    resposta = str(input('Deseja fazer outra operação? Digite [S/N]: ').strip())
    if resposta.upper() == 'N':
        break