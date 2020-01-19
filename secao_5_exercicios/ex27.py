# EX27
idade = int(input('Informe sua idade: '))

if idade == 5 or idade < 8:
    print(f'\nCategoria Infantil A | Idade: {idade}')
elif idade == 8 or idade < 11:
    print(f'\nCategoria Infantil B | Idade: {idade}')
elif idade == 11 or idade < 14:
    print(f'\nCategoria Juvenil A | Idade: {idade}')
elif idade == 14 or idade < 18:
    print(f'\nCategoria Juvenil B | Idade: {idade}')
else:
    print(f'\nCategoria Sênior | Idade: {idade}')

