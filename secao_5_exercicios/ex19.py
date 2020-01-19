# EX19
num = int(input('Informe o número que deseja verificar: '))
opcao = input('Informe 3 ou 5 como divisor que deseja vericar: ')

if opcao == '3':
    if num % 3 == 0:
        print(f'\nO número {num} é divisível por 3!')
    else:
        print(f'\nO número {num} não é divisível por 3!')
elif opcao == '5':
    if num % 5 == 0:
        print(f'\nO número {num} é divisível por 5!')
    else:
        print(f'\nO número {num} não é divisível por 5!')
else:
    print('\nOpção de divisor Inválida!!!')

