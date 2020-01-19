# EX23
print('\033[1;33m=-\033[m' * 33)
print(f'{" " * 18} \033[1;33mVerificação de ano bissexto\033[m')
print('\033[1;33m=-\033[m' * 33)
ano = int(input(f'\n {" " * 13} \033[1;96mInforme o ano que deseja verificar: \033[m'))

if ano % 400 == 0:
    print(f'\n\033[1;92mO ano de {ano} é bissexto!\033[m')

elif ano % 4 == 0 and not ano % 100 == 0:
    print(f'\n\033[1;92mO ano de {ano} é bissexto!\033[m')

else:
    print(f'\n\033[1;91mO ano de {ano} não é bissexto!!!\033[m')

