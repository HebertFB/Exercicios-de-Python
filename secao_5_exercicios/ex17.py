# EX17
base_maior = int(input('Informe o valor da base maior: '))
base_menor = int(input('Informe o valor da base menor: '))
altura = int(input('Informe a altura: '))

if base_maior <= 0:
    print('\nValor da base maior Inválido!!!')
elif base_menor <= 0:
    print('\nValor da base menor Inválido!!!')
elif altura <= 0:
    print('\nValor de altura Inválido!!!')
else:
    print(f'\nA área do trapézio é {((base_maior + base_menor) * altura) / 2}')

