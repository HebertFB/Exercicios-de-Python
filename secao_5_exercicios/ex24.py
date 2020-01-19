# EX24
print('\033[1:33m=-\033[m' * 33)
print(f'{" " * 10} \033[3;33mImposto sobre o produto de acordo com cada esta: '
      f'\n {" " * 11} MG 7%   |   SP 12%   |   RJ 15%   |   MS 8%\033[m')
print(f'{" " * 13} \033[1;31m(Obs: Utilize ponto no lugar da vírgula)\033[m')
print('\033[1;33m=-\033[m' * 33)
produto = float(input(f'\n \033[1;96mInforme o valor do produto: R$\033[m'))
estado = input(f'\n \033[1;96mInforme o estado de destino da entrega: \033[m')

if estado.upper() == 'MG':
    taxa = produto * 1.07
    print(f'\n\033[1;92mO preço total do produto no valor de R${produto:.2f} com destino à MG é de R${taxa:.2f}!\033[m')

elif estado.upper() == 'SP':
    taxa = produto * 1.12
    print(f'\n\033[1;92mO preço total do produto no valor de R${produto:.2f} com destino à SP é de R${taxa:.2f}!\033[m')

elif estado.upper() == 'RJ':
    taxa = produto * 1.15
    print(f'\n\033[1;92mO preço total do produto no valor de R${produto:.2f} com destino à Rj é de R${taxa:.2f}!\033[m')

elif estado.upper() == 'MS':
    taxa = produto * 1.08
    print(f'\n\033[1;92mO preço total do produto no valor de R${produto:.2f} com destino à MS é de R${taxa:.2f}!\033[m')

else:
    print(f'\n\033[1;91mEstado Inválido!!!\033[m')

