# Ex03
import math
num = float(input('Digite um número real: '))

if num < 0:
    print(f'\nO quadrado de {num} é {num ** 2}')
else:
    print(f'\nA raiz de {num} é {math.sqrt(num):.2f}')

