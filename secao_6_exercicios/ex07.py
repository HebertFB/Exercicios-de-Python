# EX07
soma = 0
n = 1
while n != 11:
    num = int(input(f"Informe o {n}° valor: "))
    if num < 0:
        print('\nNúmero Invalìdo!'
              '\nValores devem ser positivos!')
        break
    elif num > 0:
        soma += num
        n += 1

media = soma / 10
print(f'\nA media dos valores é {media}')

