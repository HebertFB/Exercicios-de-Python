# EX08
menor = 0
maior = 0
n = 1
while n != 11:
    num = int(input(f"Informe o {n}° valor: "))
    n += 1
    if num > maior:
        maior = num
    elif num < maior:
        menor = num
        if num < menor:
            menor = num
print(f'o maior número é {maior} e menor número é {menor}')


