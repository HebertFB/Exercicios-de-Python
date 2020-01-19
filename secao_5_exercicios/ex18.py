# EX18
opcao = str(input('Escolha uma operação matemática (+ - X ou /): '))
num = int(input('\nInforme o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if opcao == '+':
    print(f'\n{num} + {num2} = {num + num2}')
elif opcao == '-':
    print(f'\n{num} - {num2} = {num - num2}')
elif opcao.upper() == 'X' or opcao == '*':
    print(f'\n{num} X {num2} = {num * num2}')
elif opcao == '/':
    print(f'\n{num} / {num2} = {num / num2}')
else:
    print('\nNúmero Inválido!!!')

