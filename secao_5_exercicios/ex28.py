# EX28
x = int(input('Informe o valor de x: '))
y = int(input('Informe o valor de y: '))
z = int(input('Informe o valor de z: '))
print('\nOpção: (a) Geométria (b) Ponderada (c) Harmônica (d) Aritmética')
opcao = input('Informe a opção desejada: ')

if opcao.lower() == 'a':
    resultado = (x * y * z) ** (1/3)
    print(f'\nA geométria de {x}, {y} e {z} é \033[1;32m{resultado:.2f}\033[m')
elif opcao.lower() == 'b':
    resultado = (x + 2 * y + 3 * z) / 6
    print(f'\nA ponderada de {x}, {y} e {z} é \033[1;32m{resultado:.2f}\033[m')
elif opcao.lower() == 'c':
    resultado = 1 / ((1/x) + (1/y) + (1/z))
    print(f'\nA harmônica de {x}, {y} e {z} é \033[1;32m{resultado:.2f}\033[m')
elif opcao.lower() == 'd':
    resultado = (x + y + z) / 3
    print(f'\nA aritmética de {x}, {y} e {z} é \033[1;32m{resultado:.2f}\033[m')
else:
    print('\nOpção Inválida!!!')

