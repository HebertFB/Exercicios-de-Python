# EX21
print(f'{" " * 25} \033[1;33mEscolha a opção:\033[m')
print('\033[1;33m=-\033[m' * 33)
print('1- Soma de 2 números.')
print('2- Diferença entre 2 números (maior pelo menor).')
print('3- Produto entre 2 números.')
print('4- Divisão entre 2 números (o denominador não pode ser zero).')
print('\033[1;33m=-\033[m' * 33)

opcao = input(f' {" " * 19} \033[1;33mInforme a opção desejada: \033[m')

if opcao == '1':
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    print(f'\nA soma entre {num1} e {num2} é {num1 + num2}')

elif opcao == '2':
    num3 = int(input('Digite um número: '))
    num4 = int(input('Digite outro número: '))
    if num3 > num4:
        print(f'\nA diferença entre {num3} e {num4} é {num3 - num4}')
    else:
        print(f'\nA diferença entre {num3} e {num4} é {num4 - num3}')

elif opcao == '3':
    num5 = int(input('Digite um número: '))
    num6 = int(input('Digite outro número: '))
    print(f'\nO produto entre {num5} e {num6} é {num5 * num6}')

elif opcao == '4':
    num = int(input('Digite um número para ser dividido: '))
    denominador = int(input('Digite o denominador da divisão: '))
    if denominador == 0:
        print(f'\nDenominador Inválido!!! O denominador não pode ser zero')
    else:
        print(f'\nA divisão entre {num} e {denominador} é {num / denominador}')

else:
    print('\nOpção Inválida!!!')

