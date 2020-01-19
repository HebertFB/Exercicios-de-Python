# Ex04
import math
num = int(input('Digite um número: '))

if num < 0:
    print('\nNúmero inválido!!!')
else:
    print(f'\nA raiz de {num} é {math.sqrt(num):.2f}')
    print(f'O quadrado de {num} é {num ** 2}')

